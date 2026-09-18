# FCL triage log: 2026-09-17-archimate-pages-site (plan)

| Finding | First seen | Last seen | Verdict | Rationale |
|---|---|---|---|---|
| SK-01 broken freeze Python | R1 | R1 | Genuine | Fixed: valid script + before/after dirs |
| SK-02 before/after procedure | R1 | R1 | Genuine | Fixed: argv out dir |
| SK-03 AC verification overclaim | R1 | R1 | Genuine | Fixed: source half vs manual |
| SK-04 primary class oracle | R1 | R1 | Genuine | Fixed: href+count verifier |
| SK-05 validate.yml baseline | R1 | R1 | Genuine | Fixed: hash include validate.yml |
| SK-06 plex tag unpinned | R1 | R1 | Design | Pin at Task 1 implement time per spec |
| SK-07 entry freeze scope | R1 | R1 | Genuine | Fixed: catalogue-section scoped |
| M1 Pages /docs cite wrong page | R1 | R1 | Genuine | Fixed: publishing-source URL |
| A1 D11 "the registry" | R1 | R1 | Design | Spec lock sentence stands |
| Correspondent F2/D11/Path S | R1 | R1 | Advisory-skipped | Confirmed aligned |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---|---|---|---|---|
| Freeze script broken | skeptic | MAJ/blocker | Genuine | Fixed |
| Verification overclaim | skeptic | MAJ | Genuine | Fixed |
| Pages /docs cite | source | MAJ | Genuine | Fixed |
| Plex tag pin | skeptic | MAJ | Design | Implement-time |
| D11 the | source | ADV | Design | Spec lock |

Fixes applied: 7
Inflation rate: ~22% (2/9 Design-ish)
Validation: SKIP

## Round 2 Summary (confirmation wave)

| Finding | Lens | Severity | Verdict | Action |
|---|---|---|---|---|
| SK-01..05,07 + M1 | all | n/a | resolved by this change | Confirmed |
| Freeze 8/17 live | source | n/a | resolved | Live dry-run exit 0 |
| Task 5 validate.yml echo | skeptic | ADV | Advisory-skipped | Residual minor |

Fixes applied: 0
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: SKIP

## Converged: Round 2

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 2  |  Total fixes: 7
Document is ready.
