# Context: awesome-capella vs Release Repo Standard

## Context brief

**Primary question:** What does the live awesome-capella tree already ship, and what family/hub constraints bind a release-standard pass?

**Success criteria:**
- S1: File inventory of the spoke today
- S2: CI already present (family triad) vs RR-B-15 expectations
- S3: Hub FAMILY private-mode rules that affect public spoke pointers
- S4: Sibling sysml-v2 release-ish files to copy patterns from

**Workspace baseline:** porcelain sha256 `0933b130d260f82993853e7b62552af5ff0dccda8cd3a8192496cf60092999d2`; HEAD informational.

**Budget:** light.

## Findings

- **S1.** Spoke ships: README (73 entries), LICENSE CC0, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, CHANGELOG, scripts/check_entries.py, .github workflows (link-check PR + schedule), issue/PR templates, .markdownlint-cli2.jsonc, empty .lycheeignore. Missing relative to RR-B audit: COPYRIGHT, NOTICE, CITATION.cff, RELEASE-INFO.txt, docs/DISTRIBUTION.md, .gitignore, SPDX header on checker, fuller README sections, bug_report form completeness.
- **S2.** Family CI triad already green (lychee anchor-only, awesome-lint, markdownlint). RR-B-15 "gate script" may mean a release/audit gate beyond list CI; plan must map family CI to RR-B-15 or add a thin `scripts/release-gate` / document equivalence.
- **S3.** FAMILY Private mode: public spokes use **text-only** family pointer (no hub FAMILY.md URL). Capella already follows that. Do not reintroduce blob links.
- **S4.** awesome-sysml-v2 has CITATION.cff (entity JG Systems Consulting Ltd, year 2026). Prefer that shape for Capella. Sysml LICENSE is MIT; Capella stays CC0 (do not change licence class).

## Synthesis

Release-standard work is **spoke-local** under `../awesome-capella` (and GitHub settings). Hub docs only if DISTRIBUTION or family text needs a cross-link. Prefer copy patterns from sysml-v2 CITATION and hub SECURITY/NOTICE where they exist; keep Capella CC0 and family list CI.

## Evidence index

| loc | kind |
|-----|------|
| ../awesome-capella/README.md | doc |
| ../awesome-capella/LICENSE | doc |
| ../awesome-capella/.github/workflows/ | config |
| ../awesome-capella/scripts/check_entries.py | code |
| ../awesome-sysml-v2/CITATION.cff | doc |
| FAMILY.md Private mode | doc |
| audit.py output 2026-09-17 | config |
