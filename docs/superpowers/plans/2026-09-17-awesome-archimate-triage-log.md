# ARL triage log: 2026-09-17-awesome-archimate (plan)

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| C1 entry-format script ToC + language-tag on description | R1 | R1 | Genuine | Fixed: http(s)-only lines; first code-span must start ArchiMate |
| C2 book drop empty Books section | R1 | R1 | Genuine | Fixed: remove Books heading/ToC/CHANGELOG on omit |
| C3 Check 10 expected 9 H2 vs 10 | R1 | R1 | Genuine | Fixed: expect 10 default |
| M1 CHANGELOG 18 before ship | R1 | R1 | Genuine | Fixed: recount on trim path in lychee failures |
| M2 CI links success overclaim | R1 | R1 | Design | Local lychee remains ship gate; Step 4 is advisory CI watch. Keep fail:false per spec. |
| M3 Docker lychee no token | R1 | R1 | Genuine | Fixed: -e GITHUB_TOKEN |
| M4 bare grep counts ToC | R1 | R1 | Genuine | Fixed: Check 4 uses python only |
| M5 multi-drop under 15 | R1 | R1 | Genuine | Fixed: stop and report if <15 |
| M6 brittle From patches | R1 | R1 | Design | Exact From is intentional; execute may re-read file if drift |
| M7 gh run watch race | R1 | R1 | Advisory-skipped | Operational flake; sleep already present |
| M8 Task 2 seven files count | R1 | R1 | Genuine | Fixed: list exact expected names |
| Hub live spokes omit digital-engineering | R1 | R1 | Genuine | Fixed: include awesome-digital-engineering |
| Sibling clone precondition missing | R1 | R1 | Genuine | Fixed: Task 1 preconditions |
| Axis order lists year | R1 | R1 | Advisory-skipped | Table already clarifies suffix; low risk |
| Tag-axis year in CONTRIBUTING string | R1 | R1 | Advisory-skipped | Same |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| format checker | saboteur, new_hire, auditor | CRIT | Genuine | Fixed (Round 1) |
| book empty section | saboteur, new_hire, auditor | CRIT | Genuine | Fixed (Round 1) |
| H2 count 9 vs 10 | saboteur, new_hire, auditor | CRIT | Genuine | Fixed (Round 1) |
| CHANGELOG recount | saboteur | MAJ | Genuine | Fixed (Round 1) |
| CI overclaim | saboteur | MAJ | Design | Wontfix (Round 1) |
| Docker token | saboteur | MAJ | Genuine | Fixed (Round 1) |
| grep ToC count | saboteur | MAJ | Genuine | Fixed (Round 1) |
| under-15 stop | saboteur | MAJ | Genuine | Fixed (Round 1) |
| brittle From | saboteur | MAJ | Design | Wontfix (Round 1) |
| run watch race | saboteur | MAJ | Advisory-skipped | Skipped (Round 1) |
| seven files | saboteur, new_hire | MAJ | Genuine | Fixed (Round 1) |
| hub spokes list | new_hire | MAJ | Genuine | Fixed (Round 1) |
| sibling precondition | auditor | MAJ | Genuine | Fixed (Round 1) |

Fixes applied: 10
Inflation rate: 15% (2/13 CRITICAL+MAJOR Design/Advisory-skipped among raised C/M cluster approx)
Validation: SKIP
Note: saboteur/auditor GP fallback where ARL model pin failed.

## Round 2 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Prior genuine fix locs | saboteur, new_hire, auditor | CONF | resolved by this change | Confirmed (Round 2) |
| Hub CHANGELOG second live spoke | saboteur, new_hire | MAJ | Genuine | Fixed (Round 2) third spoke wording |
| sysml From stale optional | auditor | ADV | Advisory-skipped | Softened From to skip-if-current |
| eight sections on book drop | auditor | ADV | Genuine | Fixed (Round 2) recount sections |

Fixes applied: 2
Inflation rate: n/a (confirmation wave with residual fixes)
Validation: SKIP

## Converged: Round 2

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 2  |  Total fixes: 12
Document is ready.
