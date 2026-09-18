# ARL triage log: 2026-09-17-awesome-stpa

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| C1 AC3 MIT text ban | R1 | R2 | Genuine | Fixed; R2 resolved |
| C2 AC9 schedule on push | R1 | R2 | Genuine | Fixed; R2 resolved |
| C3 AC7 vs lycheeignore | R1 | R2 | Genuine | Fixed; R2 resolved |
| M Related lists AC6 | R1 | R2 | Genuine | Fixed; R2 resolved |
| M FAMILY absolute URL | R1 | R2 | Genuine | Fixed then superseded by Private mode |
| M seed pool / tags / paid | R1 | R2 | Genuine | Fixed; R2 resolved |
| M format CI | R1 | R2 | Design | PR template + review v1 |
| C-NEW Private mode absolute FAMILY URL | R2 | R3 | Genuine | Fixed text-only pointer; R3 resolved |
| M-NEW stale FAMILY.md:line cites | R2 | R3 | Genuine | Fixed section names; R3 resolved |
| M R3 public wording L75/L93 | R3 | R3 | Genuine | Fixed private-first; parent grep CLEAN |

## Round 1 Summary

Fixes applied: 12+
Inflation rate: ~15%
Validation: SKIP
GP fallback for saboteur/auditor (GLM pins unavailable).

## Round 2 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Prior fixed locs | all | — | resolved by this change | Confirmed |
| Absolute FAMILY vs Private mode | saboteur | CRIT | Genuine | Fixed R2→R3 |
| Stale line cites | saboteur | MAJ | Genuine | Fixed R2→R3 |

Fixes applied: 2 (Private mode + cites)
Inflation rate: n/a for clean prior set
Validation: SKIP

## Round 3 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Text-only pointer / AC1 private / AC13 / no line cites | all | — | resolved by this change | Confirmed |
| public wording approach/deliverable | new_hire, saboteur, auditor | MAJ | Genuine | Fixed same round |

Fixes applied: 1 residual wording
Inflation rate: n/a
Validation: SKIP

## Amendment 1

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| public sibling / New public GitHub repo | R3 | A1 | Genuine | Changed to private-first; parent `rg` CLEAN for public sibling, New public, FAMILY.md:N, blob/main/FAMILY |

Why: R3 confirmation residual; parent verified no leftover strings.

## Converged: Round 3 (amended)

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 3  |  Total fixes: 15+
Document is ready.
