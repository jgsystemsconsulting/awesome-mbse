# ARL triage log: plan 2026-09-17-awesome-stpa

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| M mkdir workflows missing | R1 | R1 | Genuine | Fixed mkdir -p .github/workflows |
| M/C watch only one CI run | R1 | R1 | Genuine | Fixed dual watch by name+sha |
| C AC1 non-recursive contents | R1 | R1 | Genuine | Fixed 14-path gh api loop |
| C MathWorks quarantine vs ship | R1 | R1 | Genuine | Fixed never-ship until 2xx |
| M link-rot label never created | R1 | R1 | Genuine | Fixed Task 6 label create |
| M hub §5/6 not diff-gated | R1 | R1 | Design | Phrase greps + sed remain; full diff optional |
| A format gate cardinalities | R1 | R1 | Genuine | Fixed has-model/tool and caps |
| A living year tie-break | R1 | R1 | Genuine | Fixed precedence |
| A private hub contingency expected | R1 | R1 | Genuine | Fixed wording |
| A AC2 extras / AC1 nested | R1 | R1 | Genuine | Fixed table rows |
| A 7b vs commit count | R1 | R1 | Design | Already had amend note from FCL |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| mkdir workflows | new_hire | MAJ | Genuine | Fixed |
| dual CI watch | new_hire, saboteur | MAJ | Genuine | Fixed |
| AC1 14 paths | saboteur, auditor | CRIT | Genuine | Fixed |
| MathWorks ban | saboteur | CRIT | Genuine | Fixed |
| link-rot label | multi | MAJ | Genuine | Fixed |
| format cardinalities | auditor | ADV | Genuine | Fixed |
| hub §5/6 diff | saboteur | MAJ | Design | Wontfix full byte-diff |

Fixes applied: 8
Inflation rate: ~12%
Validation: SKIP
GP fallback saboteur/auditor (GLM pins unavailable).

## Converged: Round 1 (pending confirmation)

Genuine fixes applied; Round 2 confirmation required before Track 1 clean for Superpowers resume.

## Round 2 confirmation (GP fallback, 2026-09-17)

| Item | Status |
|------|--------|
| mkdir .github/workflows | resolved by this change (Task 2 Step 1 L173 `mkdir -p .github .github/workflows`) |
| dual CI watch + link-rot label | SPLIT: label resolved (Task 6 L938 `gh label create link-rot`); dual watch still stands |
| AC1 14 path checks | resolved by this change (Task 8 AC1: 14 explicit `gh api .../contents/$p` paths) |
| MathWorks never-ship | resolved by this change (CONTRIBUTING known-rot: never ship until 2xx without ignore) |
| format gate has-model/tool + cardinalities | resolved by this change (Task 5 Step 4 asserts lang=1, type=1, method/spec/paid<=1, has-model=>tool) |
| private hub contingency expected wording | resolved by this change (Task 6 Step 5: expected path; ignore template with private-hub 404 rationale) |

| NEW Finding | Lens | Severity | Verdict | Action |
|-------------|------|----------|---------|--------|
| Task 6 Step 4 dual-watch uses `gh ... --jq --arg n ...` | multi | MAJOR (CRIT if treated as AC9 blocker) | Genuine | `gh run list --jq` does not accept jq `--arg`; flag errors `unknown flag: --arg`. Dual-watch intent present, command dead. Fix: shell-expand name/sha into the `--jq` expression, or pipe JSON to real `jq --arg`. |

Overall R2: NOT clean. Five of six confirmation items resolved; dual CI watch still stands via broken `gh --jq --arg`. One NEW MAJOR. Fix watch command, then R3 confirm that locus only (or full R3 if parent prefers).

## Amendment 1 (post R2)

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| gh --jq --arg invalid | R2 | A1 | Genuine | Parent rewrote dual-watch to `gh ... --json | jq -r --arg n --arg sha` |

Why: live gh CLI rejects --arg on --jq; plan now pipes to jq.

## Converged: Round 2 (amended)

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 2  |  Total fixes: 9
Document is ready.
