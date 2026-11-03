# Quick Licence Guide for AI-Assisted Projects

A licence grants permissions under stated conditions. A provider's output clause is not a third-party licence and is not a copyrightability ruling. Check the exact licence file, version, and jurisdiction.

## Software

**MIT — permissive.** Broadly permits use, copying, modification, distribution, sublicensing, and sale. Keep the copyright and permission notice in copies or substantial portions. It is provided without warranty. SPDX identifier: `MIT`. [1]

**GPL-3.0 — copyleft.** When conveying a covered modified work, GPL-3.0 includes conditions such as keeping notices, marking changes, licensing the covered work under GPL-3.0, and providing or offering corresponding source as required by the licence. How a combination is characterized depends on facts; do not decide compatibility from the name alone. SPDX identifier: `GPL-3.0-only`. [2]

**Practical rule:** A code repository without a licence is not automatically open source. Keep a dependency inventory and inspect both direct and transitive dependencies. SPDX IDs are useful labels, not substitutes for the full licence text.

## Creative Commons

- **CC BY:** reuse and adaptation are permitted under the licence, with attribution and other specified conditions.
- **CC BY-SA:** attribution plus share-alike obligations apply to adaptations under the licence.
- **CC BY-NC:** non-commercial restriction applies; credit alone does not make a commercial use permissible.
- **CC0:** a public-domain dedication tool where legally effective; it does not clear privacy, trademark, or other rights.

Creative Commons says a creator may apply a CC licence to their human contributions in a work made using generative AI. That does not mean the creator controls copyright in all AI-generated parts or can license rights belonging to someone else. A CC licence cannot override legal exceptions, privacy rules, or rights it does not cover. [3] [4]

## Check before release

1. Identify where each component came from.
2. Read the full licence and note any exception or dual-licensing language.
3. Confirm how the project will be distributed and whether commercial use is planned.
4. Preserve required notices and attribution.
5. Get human review for unknown or conflicting terms.

## References

[1]: https://spdx.org/licenses/MIT.html "SPDX MIT License"
[2]: https://www.gnu.org/licenses/gpl-3.0.en.html "GNU General Public License Version 3"
[3]: https://creativecommons.org/cc-licenses/ "Creative Commons Licenses"
[4]: https://creativecommons.org/2023/08/18/understanding-cc-licenses-and-generative-ai/ "Understanding CC Licenses and Generative AI"