# ARL triage log: 2026-09-17-awesome-capella (plan)

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| AC3 Live grep vs linked FAMILY row | R1 | R1 | Genuine | Grep awesome-capella + Live |
| download.eclipse.org false ban substring | R1 | R1 | Genuine | Host-path bans in checker + AC4 |
| check_entries not committed before push | R1 | R1 | Genuine | Step 1b commit |
| axis order not in checker / AC5 overclaim | R1 | R1 | Genuine | AC5 wording + manual axis pass |
| Task 9 hub py-capellambse URL | R1 | R1 | Genuine | Remove DSD-DBS hub href; seed dbinfrago |
| PR paths omit CONTRIBUTING | R1 | R1 | Genuine | paths include CONTRIBUTING + scripts |
| file map omit scripts | R1 | R1 | Genuine | File map note |
| Namespace soft abort / padding depth | R1 | R1 | Design | FAMILY judgment; no-pad human gate |
| Schedule verbatim / year 2026 examples | R1 | R1 | Advisory-skipped | Operational |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| AC3 Live grep | new_hire, auditor, saboteur | CRIT | Genuine | Fixed |
| download.eclipse ban | new_hire, auditor, saboteur | CRIT | Genuine | Fixed |
| checker commit path | all | MAJ/CRIT | Genuine | Fixed Step 1b |
| axis order AC5 | new_hire, auditor, saboteur | MAJ | Genuine | Fixed wording |
| hub DSD-DBS remove URL | new_hire, auditor | MAJ | Genuine | Fixed |
| PR paths CONTRIBUTING | saboteur | CRIT | Genuine | Fixed |

Fixes applied: 6
Inflation rate: ~20%
Validation: SKIP

## Round 2 Summary (parent disk confirmation)

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Fixed strings on disk | parent | — | resolved by this change | BANNED_HOST_PATH, Step 1b, paths, AC3, DSD-DBS hub remove |

Fixes applied: 0
Inflation rate: n/a
Validation: SKIP

## Converged: Round 2

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Parent confirmed residual critical fix strings present after R1 mechanical edits (light tier). No remaining still-stands on the named criticals.
Total rounds: 2  |  Total fixes: 6
Document is ready.
