# FCL triage log: 2026-09-17-awesome-digital-engineering

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| M1 hub DE policy strands claim | R1 | R1 | Genuine | Hub README has no DE section; fixed problem statement |
| M2 domain first-axis as FAMILY-compliant | R1 | R1 | Genuine | FAMILY keeps language first; fixed as intentional deviation |
| M3 Live without 40 silent override of FAMILY | R1 | R1 | Genuine | Explicit FAMILY earn-a-repo override named |
| A1 NTRS ~79 without provisional caveat | R1 | R1 | Genuine | Cheap; added PROVISIONAL/API-signal caveat |
| A2 has-model tool-project vs hub file rule | R1 | R1 | Genuine | Cheap; labeled DE extension |
| A3 short HEAD hash | R1 | R1 | Genuine | Cheap; full SHA from context |
| R2 M1 has-model formats misattributed to hub | R2 | R2 | Genuine | Split hub structure vs DE format set; fixed |
| R2 correspondent L10 hub README not in corpus | R2 | R2 | FP | Source+skeptic verified README has no DE section; claim true |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Hub DE strands | skeptic | MAJ | Genuine | Fixed (R1) |
| domain axis rename | skeptic | MAJ | Genuine | Fixed (R1) |
| Live vs FAMILY 40+ | skeptic | MAJ | Genuine | Fixed (R1) |
| NTRS provisional | skeptic | ADV | Genuine | Fixed (R1) |
| has-model extension | skeptic | ADV | Genuine | Fixed (R1) |
| HEAD full SHA | skeptic | ADV | Genuine | Fixed (R1) |

Fixes applied: 6
Inflation rate: 0% (0/3 CRITICAL+MAJOR triaged FP/Design/Recurring)
Validation: SKIP

## Round 2 Summary (confirmation wave)

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| L9-11 hub DE section | skeptic, source | - | resolved by this change | Confirmed |
| L156-162 domain deviation | skeptic, source | - | resolved by this change | Confirmed |
| L198-204 Live override | skeptic, source | - | resolved by this change | Confirmed |
| L207 NTRS provisional | skeptic, source | - | resolved by this change | Confirmed |
| L168 has-model extension | skeptic, source | - | resolved by this change | Confirmed |
| L65 full SHA | skeptic, source | - | resolved by this change | Confirmed |
| has-model formats as hub | skeptic | MAJ | Genuine | Fixed (R2) |
| L10 hub README corpus | correspondent | MAJ | FP | Wontfix; README verified by source |

Fixes applied: 1
Inflation rate: 50% (1/2 CRITICAL+MAJOR FP)
Validation: SKIP

## Round 3 Summary (confirmation of R2 has-model fix)

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| L168 hub vs DE formats | skeptic, source, correspondent | - | resolved by this change | Confirmed |
| R1 locs regression | skeptic | - | intact | Confirmed |

Fixes applied: 0
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: SKIP

## Converged: Round 3

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 3  |  Total fixes: 7
Document is ready.



## Amendment 1 (in progress)

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| AC5 private-hub FAMILY lycheeignore exemption | A1 | A1 | Design | Access-control exemption for absolute pointer while hub private; only non-browser ignore allowed |

Why: plan Known deviation needed for AC3+AC6; locked into AC5 so plan/spec align. No world-fact change.

## Amendment 1

Confirmation: parent re-read AC5; exemption is one-line, named, removable at public release. No new CRITICAL/MAJOR world claims.

## Converged: Round 3 (amended)

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 3  |  Total fixes: 7 (+1 Design amendment)
Document is ready.
