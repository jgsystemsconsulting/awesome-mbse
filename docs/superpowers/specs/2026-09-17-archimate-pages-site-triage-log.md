# ARL triage log: 2026-09-17-archimate-pages-site

| Finding | First seen | Last seen | Verdict | Rationale |
|---|---|---|---|---|
| C1 section anchors/href underspec | R1 | R1 | Genuine | Fixed: eight labels + README deep-link form |
| C2 R-F6 no AC | R1 | R1 | Genuine | Fixed: AC-first-run |
| C3 tokens unenforced | R1 | R1 | Genuine | Fixed: inline R-V1 table + AC-tokens |
| C4 plex/CDN denylist | R1 | R1 | Genuine | Fixed: forbid absolute @font-face; face list |
| C5 Goal4 vs F3 | R1 | R1 | Genuine | Fixed: Goal 4 exception for light-only |
| C6 a11y AC gap | R1 | R1 | Genuine | Fixed: AC-a11y expanded |
| C7 CTA dual href | R1 | R1 | Genuine | Fixed: pinned blob/main/README.md |
| C8 scanners undefined | R1 | R1 | Genuine | Fixed: check_release only oracle |
| M1 count hardcoded | R1 | R1 | Design | Snapshot 17 locked; freeze binds |
| M2 R-V7 wider than AC | R1 | R1 | Genuine | Fixed: AC-anti-pattern expanded |
| M3 DESIGN not inlined | R1 | R1 | Genuine | Fixed: tokens inlined; DESIGN companion |
| M4 CONTRIBUTING soft | R1 | R1 | Genuine | Fixed: exact blob URL link-only |
| A1-A7 advisories | R1 | R1 | mixed | Fixed or skipped as listed Round 1 |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---|---|---|---|---|
| C1-C8 | multi | CRIT | Genuine | Fixed |
| M2-M4 | multi | MAJ | Genuine | Fixed |
| M1 | saboteur | MAJ | Design | Snapshot lock |
| A* | multi | ADV | mixed | Fixed/skipped |

Fixes applied: 15
Inflation rate: 8% (1/12 CRITICAL+MAJOR Design)
Validation: SKIP

## Round 2 Summary (confirmation wave)

| Finding | Lens | Severity | Verdict | Action |
|---|---|---|---|---|
| Fixed locks C1-C8 M2-M4 | all | n/a | resolved / locks hold | Confirmed |
| Companion DESIGN wording | new_hire | ADV | Advisory-skipped | Non-blocking |

Fixes applied: 0
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: SKIP

## Converged: Round 2

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 2  |  Total fixes: 15
Document is ready.
