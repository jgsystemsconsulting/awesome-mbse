# Research: Release Repo Standard applied to awesome-capella

## Research brief

**Primary question:** What does Release Repo Standard v1.14 require for a public CC0 curated awesome-list spoke (`awesome-capella`), and which requirement IDs are in scope vs N/A for list products?

**Sub-questions:**
1. Standard version, skill path, and normative file location
2. Profile selection (Base vs M/S/R) for an awesome list
3. Licence posture for existing CC0-1.0 spoke
4. Placeholder substitution for JG Systems Consulting
5. Gap list from automated audit of the live spoke

**Success criteria:**
- R1: Cite skill path and standard version
- R2: Locked profile + licence posture for awesome-capella
- R3: Named FAIL set from audit.py on the spoke
- R4: List-product interpretation notes for Usage / landing / marketplace rows

**Out of scope:** Implementing fixes; applying the standard to other spokes in this research doc.

**Budget:** light. Retrieved_at: 2026-09-17.

## Findings

- **ESTABLISHED (local primary).** Normative standard lives at `C:\Users\gower\.zcode\skills\release-repo-standard\references\release-repo-standard.md`, version **1.14 (generic edition)**. Skill entry: `release-repo-standard`. Auditor: `tools/audit.py`.
- **ESTABLISHED.** Product type for a curated awesome list is **Base only** (not RR-M MCP, not RR-S skills pack, not RR-R research instrument). Verify lines still apply where file-shaped.
- **ESTABLISHED.** awesome-capella already ships **CC0-1.0** LICENSE (OSS posture). CONTRIBUTING + CoC already present (OSS community files MUST).
- **ESTABLISHED (audit 2026-09-17).** `python tools/audit.py --repo …/awesome-capella --profile base` reported **14 FAIL, 2 WARN, 8 PASS**, including missing COPYRIGHT/NOTICE, no SPDX/header on `scripts/check_entries.py`, README section gaps (Usage/License/Support + licensing URL), SECURITY advisory route, version/RELEASE-INFO mismatch, no `.gitignore`, no gate script/CI shape expected by RR-B-15, em dash in SECURITY.md, no CITATION.cff, incomplete issue forms (RR-B-32), no `docs/DISTRIBUTION.md` (RR-B-36). Landing HTML absent (RR-B-24 WARN).
- **PROVISIONAL (list-product interpretation).** For an awesome list, "Usage" is contribute + browse the list (not a CLI first-run). Landing page MAY be GitHub README-as-landing until Pages is stood up; RR-B-20/24 still apply if Pages is chosen. RR-B-29 marketplace rows are largely N/A for a plain awesome list (not an agent plugin); ledger must record deliberate N/A with date.
- **ESTABLISHED sibling pattern.** Live spoke `awesome-sysml-v2` already has `CITATION.cff`; Capella does not.

## Synthesis

Apply **RR-B + OSS posture + standalone build model** to `jgsystemsconsulting/awesome-capella`. Close the 14 FAIL items with list-sensible Usage/Support wording, CITATION.cff, COPYRIGHT/NOTICE, SECURITY advisory route, RELEASE-INFO + version alignment, issue forms, DISTRIBUTION ledger, SPDX header on the checker script, `.gitignore`, and either Pages landing or deliberate N/A with ledger note. Do not invent MCP/skills profile work.

## Sources

| URL / path | Role |
|------------|------|
| file://C:/Users/gower/.zcode/skills/release-repo-standard/references/release-repo-standard.md | Normative RR standard v1.14 |
| file://C:/Users/gower/.zcode/skills/release-repo-standard/SKILL.md | Skill how-to apply/audit |
| file://C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py | Automated auditor (run 2026-09-17 on awesome-capella) |
| https://github.com/jgsystemsconsulting/awesome-capella | Target spoke |
| https://github.com/jgsystemsconsulting/awesome-sysml-v2 | Sibling spoke with CITATION.cff |
