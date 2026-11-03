#!/usr/bin/env python3
"""Fail-closed screening for npm `license-checker --json` reports.

This is a triage aid, not a legal compatibility determination. It accepts only
an explicit allowlist and asks a maintainer to review everything else.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ALLOWLIST = {
    "MIT",
    "ISC",
    "BSD-2-Clause",
    "BSD-3-Clause",
    "Apache-2.0",
    "0BSD",
}


def normalized_license(value: object) -> str | None:
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, list) and len(value) == 1 and isinstance(value[0], str):
        return value[0].strip()
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path, help="JSON output from license-checker")
    args = parser.parse_args()

    try:
        packages = json.loads(args.report.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read licence report: {exc}", file=sys.stderr)
        return 2

    if not isinstance(packages, dict):
        print("ERROR: expected a JSON object keyed by package name/version", file=sys.stderr)
        return 2

    flagged: list[tuple[str, str]] = []
    for package, metadata in sorted(packages.items()):
        if not isinstance(metadata, dict):
            flagged.append((package, "invalid package metadata"))
            continue
        license_id = normalized_license(metadata.get("licenses"))
        if license_id is None:
            flagged.append((package, "missing, multiple, or ambiguous licence expression"))
        elif license_id not in ALLOWLIST:
            flagged.append((package, license_id))

    if flagged:
        print("REVIEW REQUIRED — the following dependencies are not auto-approved:")
        for package, license_id in flagged:
            print(f"  - {package}: {license_id}")
        print("A human maintainer must inspect the package metadata and full licence text.")
        return 1

    print(f"PASS — {len(packages)} package(s) use an allowlisted identifier.")
    print("This screening result is not a legal opinion or compatibility guarantee.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
