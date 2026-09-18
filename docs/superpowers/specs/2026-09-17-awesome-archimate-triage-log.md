# ARL triage log: 2026-09-17-awesome-archimate

arl-saboteur and arl-auditor type missing; GP fallback, same-model. Parent graded merged findings.

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| C1 type enum no value for specs (L108-133) | R1 | R1 | Genuine | Hub format is language + `spec` without type; type axis says exactly 1 but seed specs omit type. Clarify exception: when `spec`/`standard` present, type may be omitted (or add type values / require both). |
| C2 incomplete seed/example tags (L108-150) | R1 | R1 | Genuine | Spec format examples and seed table omit required axes inconsistently (language missing on plugins, type missing on specs/TOGAF). Align every seed and example to axis rules after C1 fix. |
| C3 registry 3.x vs ArchiMate4 (L15,L172,L188) | R1 | R1 | Genuine | Goal and seeds list ArchiMate 4 (C260) but hub registry scope stays "ArchiMate 3.x". Expand registry/scope text to cover 3.x and 4, or document 4 as in-list-only with registry note. |
| C4 FAMILY 40-before-create vs 18 seeds (L159) | R1 | R1 | Genuine | FAMILY step 2 ~40 candidates before create; ship plan is 18 seeds / 15 live. Write explicit maintainer waiver naming growth buckets and 15-live open bar. |
| C5 has-model vs repo collections (L113) | R1 | R1 | Genuine | has-model defined as directly downloadable single file; seeds tag whole GitHub repos `has-model` `example`. Define collection rule: repo/collection uses `example`; `has-model` only when a concrete model file URL is the entry. |
| C6 foundational-value undefined (L59) | R1 | R1 | Genuine | stale.yml reword cites foundational-value exception; term never defined in this spec. Inline definition or drop the phrase and point only at inclusion bar. |
| M1 live entries unenforced with advisory lychee (L18,L50,L190) | R1 | R1 | Genuine | Success/AC require 15 live entries but PR lychee is advisory fail:false. Define live = URL resolves at execute (manual or workflow_dispatch proof); advisory pattern does not waive the 15-live bar. |
| M2 year axis vs suffix (L106) | R1 | R1 | Genuine | Axis order lists `year` as an axis; year is terminal `(YYYY)` suffix, not a tag span. Drop year from tag-axis table; keep as required suffix only. |
| M3 wiki as blog (L138) | R1 | R1 | Genuine | Archi Wiki seeded as `blog`; wiki is docs, not blog. Use type that fits (or add `docs` and map wiki→docs); do not force `blog`. |
| A1 branding overreach | R1 | R1 | Advisory-skipped | "OMG ArchiMate" ban already in AC and brand-correction lock; no extra must-fix beyond existing Open Group wording. |
| A2 clone path hardcode | R1 | R1 | Genuine | AC/deliverable hardcode `C:\Users\...`. Cheap fix: sibling-clone wording (clone next to awesome-mbse / awesome-sysml-v2). |
| A3 AC undercover | R1 | R1 | Genuine | Several must-behaviors live only in prose (live definition, tag exceptions, registry scope, 40-entry waiver). Cheap fix: mirror each Genuine into AC checkboxes once body text lands. |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| type enum vs specs | saboteur, new_hire, auditor | CRIT | Genuine | Fixed (Round 1) |
| incomplete seed tags | saboteur, new_hire, auditor | CRIT | Genuine | Fixed (Round 1) |
| registry 3.x vs ArchiMate4 | saboteur, new_hire | CRIT | Genuine | Fixed (Round 1) |
| FAMILY 40 vs 18 | saboteur, auditor | CRIT | Genuine | Fixed (Round 1) |
| has-model vs repos | saboteur, auditor | CRIT | Genuine | Fixed (Round 1) |
| foundational-value undefined | saboteur, new_hire, auditor | CRIT | Genuine | Fixed (Round 1) |
| live/lychee unenforced | saboteur | MAJ | Genuine | Fixed (Round 1) |
| year axis vs suffix | saboteur, new_hire, auditor | MAJ | Genuine | Fixed (Round 1) |
| wiki as blog | saboteur, auditor | MAJ | Genuine | Fixed (Round 1) |
| branding overreach | saboteur | ADV | Advisory-skipped | Fixed cheaply with branding scope (Round 1) |
| clone path hardcode | saboteur | ADV | Genuine | Fixed (Round 1) |
| AC undercover | auditor | ADV | Genuine | Fixed (Round 1) |

Fixes applied: 11
Inflation rate: 0% (0/9 CRITICAL+MAJOR triaged FP/Design/Recurring)
Validation: SKIP
Note: saboteur/auditor/triage used GP fallback where ARL model pin failed.

## Round 2 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Prior genuine fix locs (11) | saboteur, new_hire, auditor | CONF | resolved by this change | Confirmed (Round 2) |

Fixes applied: 0
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: SKIP

## Converged: Round 2

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 2  |  Total fixes: 11
Document is ready.
