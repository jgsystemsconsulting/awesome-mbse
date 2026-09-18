# ARL triage log: 2026-09-17-awesome-digital-engineering

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| Example missing required type | R1 | R1 | Genuine | Fixed legal example with report+standard |
| type enum no standards/policy mapping | R1 | R1 | Genuine | type=report for storefronts; pairing rule |
| create push vs AC6 PR | R1 | R1 | Genuine | CI proof via launch PR after main exists |
| empty sections policy | R1 | R1 | Genuine | Empty H2 + italic stub allowed |
| inclusion bar undefined | R1 | R1 | Genuine | Restated hub §2 |
| section→domain routing | R1 | R1 | Genuine | Routing table + DE-general rule |
| family pointer relative | R1 | R1 | Genuine | Absolute hub FAMILY URL |
| ESTABLISHED skips verify | R1 | R1 | Genuine | Research grades are hints only |
| lycheeignore active vs comment | R1 | R1 | Genuine | Active pattern + trailing comment |
| DoD hash without URL | R1 | R1 | Genuine | Hash notes only; URL required |
| AC1 Windows path hard requirement | R1 | R1 | Genuine | Preferred path; any clone OK |
| AC11 host set mismatch | R1 | R1 | Genuine | Full provisional host set |
| domain rename not in AC | R1 | R1 | Genuine | AC2 requires CONTRIBUTING docs |
| 140/year/dedupe undefined local | R1 | R1 | Genuine | Restated inline |
| has-model tool vs file circular | R1 | R1 | Genuine | has-model only on file primary URL |
| tag CI unenforced | R1 | R1 | Design | v1 human review; lychee+awesome-lint only |
| sibling spoke edit required | R1 | R1 | Design | v1 hub cross-link only |
| 429 accepted in CI vs execute | R1 | R1 | Genuine | 429 not launch-verified |
| saboteur M2 lycheeignore missing config | R1 | R1 | FP | Spec already requires .lycheeignore file |
| inflation/merge loc compression noise | R1 | R1 | FP | Several merge locs were compressed placeholders |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Example type | saboteur, new_hire, auditor | CRIT | Genuine | Fixed |
| type enum standards | saboteur, new_hire, auditor | CRIT | Genuine | Fixed |
| AC6 vs create push | saboteur | CRIT | Genuine | Fixed |
| inclusion bar | new_hire | MAJ | Genuine | Fixed |
| section domain routing | auditor | MAJ | Genuine | Fixed |
| empty sections | saboteur, new_hire | MAJ | Genuine | Fixed |
| family pointer / verify / ignore / AC | multi | MAJ | Genuine | Fixed |
| tag linter absent | saboteur | MAJ | Design | Wontfix v1 |

Fixes applied: 14
Inflation rate: ~15%
Validation: SKIP
Note: saboteur+auditor R1 used GP fallback (GLM pin model-not-found).

## Round 2 Summary (confirmation)

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Items 1-12 R1 fixes | saboteur, new_hire, auditor | - | resolved by this change | Confirmed |
| New critical/major | all | - | none | - |

Fixes applied: 0
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: SKIP
Note: saboteur+auditor R2 used GP fallback after pin fail; new_hire native.

## Converged: Round 2

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 2  |  Total fixes: 14
Document is ready.


## Amendment 1 (in progress)

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| AC5 private-hub FAMILY pointer ignore exemption | A1 | A1 | Design | Spec/plan alignment for private hub + absolute pointer + green lychee |

Why: without exemption AC3 and AC6 contradict on private hub. Normative one-line exception.

## Amendment 1

Parent confirmed wording is scoped (only FAMILY.md pointer, remove when public).

## Converged: Round 2 (amended)

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 2  |  Total fixes: 14 (+1 Design amendment)
Document is ready.
