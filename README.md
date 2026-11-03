# Dependency Licence Triage Demo

This optional workflow creates an npm dependency licence report and fails closed when a dependency is unknown, ambiguous, or not on the sample allowlist. A maintainer must inspect any flagged package against its actual licence and the project's release plan.

## Use in an npm project

Copy `scan_licenses.py` and `.github/workflows/license-audit.yml` into the repository. The target project needs a `package.json` and committed `package-lock.json`. Install dependencies with `npm ci --ignore-scripts`, create the report with `npx --yes license-checker --production --json > licenses.json`, then run `python3 automation/scan_licenses.py licenses.json`.

The sample allowlist includes MIT, ISC, BSD-2-Clause, BSD-3-Clause, Apache-2.0, and 0BSD. It is intentionally narrow. A permissive-looking name does not guarantee compatibility; package-specific terms, exceptions, multiple licences, source files, and transitive dependencies may need separate review. Edit the allowlist only after maintainer approval. Do not treat a passing scan as legal clearance.

The included GitHub Actions file runs on pull requests that change package manifests or the scanner. The workflow is a demonstration and may need version and permissions review for your organization.