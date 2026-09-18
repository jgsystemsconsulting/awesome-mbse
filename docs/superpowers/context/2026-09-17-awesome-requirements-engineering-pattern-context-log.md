# Context log: awesome-requirements-engineering pattern

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| FAMILY one-hub many-spokes + shared standard file set | R1 | R1 | SINGLE-SOURCE | FAMILY.md docs only (cartographer+prospector same file family); decision-bearing OK named |
| Registry RE Planned namespace empty 2026-09 | R1 | R1 | SINGLE-SOURCE | FAMILY.md:40 three lenses same loc |
| Hub CONTRIBUTING SoT year/dedupe/neutrality | R1 | R1 | SINGLE-SOURCE | FAMILY.md + CONTRIBUTING.md docs |
| Entry format tags (YYYY) mandated | R1 | R1 | SINGLE-SOURCE | FAMILY.md entry format |
| README skeleton badges ToC | R1 | R1 | SINGLE-SOURCE | FAMILY.md:108 |
| PR template inclusion bar | R1 | R1 | SINGLE-SOURCE | hub .github/PULL_REQUEST_TEMPLATE.md |
| CI lychee+awesome-lint+markdownlint required | R1 | R1 | SINGLE-SOURCE | FAMILY doc + hub workflow config; no code kind |
| Hub PR lychee fail:true vs sysml fail:false | R1 | R1 | SINGLE-SOURCE | two config sites; hub gate wins for new spoke |
| Hub under-implements markdownlint vs FAMILY | R1 | R1 | SINGLE-SOURCE | skeptic; copy sysml .markdownlint-cli2.jsonc |
| sysml-v2 template workflows + submission runbook | R1 | R1 | SINGLE-SOURCE | config+doc analog |
| Sibling org repo not nested in hub | R1 | R1 | SINGLE-SOURCE | FAMILY registry model + awesome-sysml-v2 URL |
| Hub registry/README update after go-live step 5 | R1 | R1 | SINGLE-SOURCE | FAMILY.md:102 |
| LICENSE CC0-1.0 both repos | R1 | R1 | SINGLE-SOURCE | LICENSE docs |
| Starting new list 6 steps incl 40+ candidates | R1 | R1 | SINGLE-SOURCE | FAMILY.md:93 |
| CONTRIBUTING.md casing: FAMILY upper vs sysml lower | R1 | R1 | SINGLE-SOURCE | use CONTRIBUTING.md per FAMILY |
| Hub tagged format wins over sysml untagged exemplar | R1 | R1 | SINGLE-SOURCE | FAMILY vs sysml README/contributing contradiction resolved toward FAMILY |
| sysml README omits Last full sweep + family pointer | R1 | R1 | SINGLE-SOURCE | do not copy that omission |
| archimate context stem is different spoke | R1 | R1 | SINGLE-SOURCE | do not reuse archimate research/context as RE |

## Round 1

Triage by parent (ctx-triage agent unavailable: model-not-found GLM-5.2).
No CONFLICTED unresolved (sysml vs FAMILY tensions framed as design constraints, not fact conflicts about hub).
No STALE.

Verdict: CONTEXT_COMPLETE
Coverage: SC1–SC6 met with SINGLE-SOURCE decision-bearing claims (named).

## Round 1 Summary

| Claim | Lenses | Grade | Action |
|-------|--------|-------|--------|
| Shared standard / file set | cart, prosp | SS | Keep |
| RE Planned registry | all | SS | Keep |
| Hub CONTRIBUTING SoT | cart, prosp | SS | Keep |
| Tagged entry format | cart, prosp, skep | SS | Keep; win over sysml |
| CI blocking lychee + markdownlint | cart, prosp, skep | SS | Keep; hybrid hub+sysml |
| Sibling repo location | cart, skep | SS | Keep |
| Go-live hub updates | cart | SS | Keep |
| Casing CONTRIBUTING.md | skep | SS | Keep FAMILY name |
| Ignore archimate stem | skep | SS | Keep |

Fixes applied: 0
Coverage: 6/6 criteria met
Validation: PASS (parent triage fallback)

## Converged: Round 1

Track 1: Merged verdict CONTEXT_COMPLETE.
Total rounds: 1 | Total fixes: 0
Document is ready.
