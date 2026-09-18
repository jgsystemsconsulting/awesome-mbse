# Context: RR-B for awesome-stpa

## Context brief

Map Capella RR-B packaging + family runbook Checklist A onto private awesome-stpa.

## Findings

- Spoke path `../awesome-stpa`, private Live, HEAD after awesome-stpa ship has 43 entries, triad CI, CONTRIBUTING uppercase, NOTICE, text-only pointer.
- Capella locked decisions D1–D11 in `docs/superpowers/specs/2026-09-17-repo-release-standard-capella.md` are the list-product template.
- Hub FAMILY already lists awesome-stpa Live|private; public flip updates Visibility only.
- Family runbook Checklist A is normative for visibility; RR-B does not replace it.
- RR-B-34 auditor flags `/home/` inside MIT PSAS URLs; not machine-local.

## Synthesis

Implement spoke-local RR-B files mirroring Capella; then Checklist A public release; hub registry Visibility→public. No entry list rewrite. No hub FAMILY.md hyperlink while hub private.

## Evidence index

| loc | kind |
|-----|------|
| ../awesome-stpa/README.md | doc |
| docs/runbooks/family-public-release.md | doc |
| docs/superpowers/specs/2026-09-17-repo-release-standard-capella.md | doc |
