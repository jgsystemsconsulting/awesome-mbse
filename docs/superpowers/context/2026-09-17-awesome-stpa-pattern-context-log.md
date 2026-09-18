# Context log: awesome-stpa-pattern

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| FAMILY start checklist + depth bar (FAMILY.md:93) | R1 | R1 | SINGLE-SOURCE | Doc-only; cartographer+prospector same section = one site |
| Shared standard section (FAMILY.md:66) | R1 | R1 | SINGLE-SOURCE | Doc-only one section |
| sysml-v2 root + workflows as template | R1 | R1 | SINGLE-SOURCE | Directory inventory one lens; config sites on workflows separate |
| Hub registry / scope / pointer (FAMILY.md:33) | R1 | R1 | SINGLE-SOURCE | Doc-only |
| CONTRIBUTING port targets (FAMILY.md:81 + CONTRIBUTING.md:71) | R1 | R1 | CORROBORATED | FAMILY pointer + hub CONTRIBUTING body; two independent doc sites |
| README skeleton + family pointer (FAMILY.md:108) | R1 | R1 | SINGLE-SOURCE | Doc-only |
| sysml-v2 links.yml live CI analog | R1 | R1 | SINGLE-SOURCE | Config one site |
| Standard files list (FAMILY.md:86) | R1 | R1 | SINGLE-SOURCE | Doc-only |
| awesome-stpa Planned in registry (FAMILY.md:42) | R1 | R1 | SINGLE-SOURCE | Doc fact for go-live |
| CONTRIBUTING.md vs contributing.md casing conflict | R1 | R1 | CORROBORATED | FAMILY.md:86 doc + sysml lint.yml:35 config |
| sysml lychee advisory vs FAMILY blocking + fragments | R1 | R1 | CORROBORATED | sysml links.yml + hub link-check-pr.yml |
| FAMILY entry tags/(YYYY) vs sysml bare format | R1 | R1 | CORROBORATED | FAMILY standard + sysml contributing.md:18 |
| sysml missing year/dedupe/neutrality sections | R1 | R1 | CORROBORATED | FAMILY:81 + sysml contributing absence (prospector hub port target) |
| sysml README missing Last full sweep + family pointer | R1 | R1 | SINGLE-SOURCE | README:1 vs FAMILY skeleton |
| Hub README no per-spoke links | R1 | R1 | SINGLE-SOURCE | README:20 |
| CITATION.cff MIT vs LICENSE CC0 on sysml | R1 | R1 | SINGLE-SOURCE | config |
| Hub vs spoke CI tree divergence | R1 | R1 | CORROBORATED | multiple workflow configs + contributing advisory text |

## Round 1

Triage parent-fallback (ctx-triage model unavailable: zai GLM-5.2). Graded from ctx-merge JSON.

Coverage: SC1-SC5 met at SINGLE-SOURCE or better. Decision-bearing port/CI/format claims CORROBORATED where multi-site.

genuine_fixes_needed: 0 (context gathering only)
verdict: CONTEXT_COMPLETE (criteria covered; SINGLE-SOURCE named for doc-only map claims)

## Round 1 Summary

| Claim | Lenses | Grade | Action |
|-------|--------|-------|--------|
| Start checklist | cart, prosp | SS | Resourced |
| Shared standard | cart | SS | Resourced |
| sysml template tree | cart, prosp, skep | SS/CORR | Resourced + gotchas |
| Registry/scope | cart, skep | SS | Resourced |
| CONTRIBUTING ports | cart, prosp, skep | CORR | Resourced |
| Casing/CI/format gotchas | skep | CORR | Named for plan |

Fixes applied: 0
Coverage: 5/5 criteria met
Validation: PASS (parent fallback)

## Converged: Round 1

Track 1: Merged verdict CONTEXT_COMPLETE.
Total rounds: 1  |  Total fixes: 0
Document is ready.
