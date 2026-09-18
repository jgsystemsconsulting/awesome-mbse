# ARL triage log: 2026-09-17-awesome-capella

arl-saboteur and arl-auditor pins model-not-found; GP fallback used. Parent graded.

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| language axis cannot tag pure Arcadia | R1 | R1 | Genuine | Capella covers Arcadia-home resources |
| verified entry / depth bar unevaluable | R1 | R1 | Genuine | Defined count rules |
| M6 redirect host unevaluable | R1 | R1 | Genuine | Banned pattern list + definition |
| AC4 misses eclipse.org/capella bans | R1 | R1 | Genuine | Extended AC4 |
| inclusion bar soft | R1 | R1 | Genuine | Inlined five checks |
| hub cross-cutting undefined | R1 | R1 | Genuine | keep/move primary-subject rule |
| namespace soft thresholds | R1 | R1 | Design | FAMILY "roughly 100+" intentional |
| M4 tag cardinality not in AC | R1 | R1 | Genuine | M4/AC5 extended |
| .lycheeignore hide banned hosts | R1 | R1 | Genuine | S3 forbids ignoring ban list |
| neutrality unenforced | R1 | R1 | Design | Hub parity |
| other-tool graduate no trigger | R1 | R1 | Genuine | Same-change CONTRIBUTING update |
| markdownlint vs tagged lines | R1 | R1 | Genuine | Config note + inventory file |
| collab decision 5 vs thin section | R1 | R1 | Genuine | Omit product entry only |
| year rule not inlined | R1 | R1 | Genuine | Frozen year text |
| FAMILY skeleton not concrete | R1 | R2 | Genuine | Full nine Contents+H2 fence |
| CI bodies missing | R1 | R1 | Design | Port paths named |
| markdownlint config missing inventory | R1 | R1 | Genuine | Added file |
| ISSUE_TEMPLATE Must vs Should | R1 | R1 | Genuine | Split inventory |
| absolute Windows path AC | R1 | R1 | Genuine | Sibling clone wording |
| PR template missing inventory | R1 | R1 | Genuine | Should-inventory |
| schedule fail:false vs triad green | R1 | R1 | Genuine | AC2 = PR workflow |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Core implementability gaps | saboteur, new_hire, auditor | CRIT/MAJ | Genuine | Fixed (Round 1) |
| Namespace/neutrality/CI-body | mixed | MAJ | Design | Wontfix |

Fixes applied: 12+
Inflation rate: ~25%
Validation: SKIP

## Round 2 Summary (confirmation)

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Most R1 fixes | all | — | resolved by this change | Confirmed |
| Skeleton truncated Contents | saboteur | MAJ | still stands then fixed | Fixed + reconfirm |

Fixes applied: 1 (skeleton Contents+H2 complete)
Inflation rate: n/a
Validation: SKIP

## Converged: Round 2

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Confirmation: skeleton residual fixed and reconfirmed resolved by this change. Other prompted locs resolved. No still stands remaining.
Total rounds: 2  |  Total fixes: 13+
Document is ready.
