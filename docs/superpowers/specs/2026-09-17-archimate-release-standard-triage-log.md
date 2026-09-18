# ARL triage log: 2026-09-17-archimate-release-standard

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| M1 lint workflow_dispatch vs triad lock | R1 | R1 | Genuine | Fixed: AC4/5 use push for lint, dispatch for links only |
| M2 LICENSE Capella claim | R1 | R1 | Genuine | Fixed: archimate-specific append + NOASSERTION fallback |
| M1 auditor D5 meta/Playwright | R1 | R1 | Genuine | Fixed: D5/AC6 meta + Playwright/SEO |
| M1-M7 new_hire template inlines | R1 | R1 | Design | Plan clones Capella files; not all bodies inlined in spec |
| A tracked file count 11 vs 10 | R1 | R1 | Genuine | Fixed: 10 |
| A checkout@v4 vs SHA | R1 | R1 | Genuine | Fixed: pin full SHA |
| A RR-B-24 FAIL mislabel | R1 | R1 | Genuine | Fixed |
| A ledger vocab | R1 | R1 | Genuine | Fixed submitted vocabulary |
| A seed freeze counts only | R1 | R1 | Genuine | Fixed: hash/diff of 25 bullets |
| A check name validate | R1 | R1 | Genuine | Fixed: use GitHub-reported context string |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| lint dispatch vs triad | saboteur | MAJ | Genuine | Fixed (Round 1) |
| LICENSE Capella claim | saboteur | MAJ | Genuine | Fixed (Round 1) |
| D5 meta MANUAL | auditor | MAJ | Genuine | Fixed (Round 1) |
| template bodies | new_hire | MAJ | Design | Plan clones Capella (Round 1) |

Fixes applied: 8
Inflation rate: ~30% (new_hire majors Design as plan-owned)
Validation: SKIP

## Round 2 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Prior genuine | parent | CONF | resolved by this change | Confirmed by re-read (Round 2) |

Fixes applied: 0
Inflation rate: n/a
Validation: SKIP

## Converged: Round 2

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 2  |  Total fixes: 8
Document is ready.
