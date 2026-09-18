# FCL triage log: 2026-09-17-awesome-capella (plan)

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| Public FAMILY.md hyperlink vs Private mode | R1 | R1 | Genuine | Text-only pointer |
| AC4 falsely bans download.eclipse.org via substring | R1 | R1 | Genuine | Different host; primers allowed |
| check_entries deleted then AC5 requires it | R1 | R1 | Genuine | Commit scripts/check_entries.py |
| Year probe uses repo.tag_name | R1 | R1 | Genuine | releases/tags endpoints |
| DSD-DBS/py-capellambse owner stale | R1 | R1 | Genuine | dbinfrago live owner |
| awesome-lint@2.3.0 vs hub unpinned | R1 | R1 | Genuine | Note sysml pin; hub unpinned |
| Neutrality #7- vs #editorial-neutrality | R1 | R1 | Genuine | Match spec slug |
| 100+ stars thresholds vs FAMILY | R1 | R1 | Design | FAMILY step 1 working test; named as family judgment |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| FAMILY private hyperlink | skeptic | CRIT | Genuine | Fixed |
| download.eclipse ban overreach | skeptic | MAJ | Genuine | Fixed |
| check_entries lifecycle | skeptic | MAJ | Genuine | Fixed |
| year gh api field | skeptic | MAJ | Genuine | Fixed |
| py-capellambse owner | source | CRIT | Genuine | Fixed |
| awesome-lint pin source | source | MAJ | Genuine | Fixed note |
| neutrality anchor | correspondent | CRIT | Genuine | Fixed |
| 100+ stars | correspondent | MAJ | Design | Wontfix named FAMILY test |

Fixes applied: 7
Inflation rate: ~12%
Validation: SKIP

## Round 2 Summary (parent confirmation of fixed strings)

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| All R1 genuine string fixes present in plan body | parent | — | resolved by this change | Verified via grep residual-clean |

Fixes applied: 0
Inflation rate: n/a
Validation: SKIP

## Converged: Round 2

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Residual bad patterns grepped clean (DSD-DBS, blob FAMILY URL, #7-editorial, false substring ban, deleted checker). Parent confirmation of fix presence after R1 (light tier; full three-lens confirm deferred risk accepted only because fixes are mechanical string replacements verified on disk).
Total rounds: 2  |  Total fixes: 7
Document is ready.
