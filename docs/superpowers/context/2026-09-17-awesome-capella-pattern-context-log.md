# Context log: awesome-capella pattern

triage: fallback (model-not-found on ctx-triage pin GLM-5.2). Parent graded Round 1 from ctx-merge output.

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| FAMILY.md is SoT for hub-spoke, registry, shared standard | R1 | R1 | SINGLE-SOURCE | multi-doc restates; no code site |
| awesome-capella registry row Planned already present | R1 | R1 | SINGLE-SOURCE | FAMILY.md only (3 lenses same doc) |
| Scope routes Capella/Arcadia to awesome-capella | R1 | R1 | SINGLE-SOURCE | FAMILY.md |
| Shared standard file set locked | R1 | R1 | SINGLE-SOURCE | FAMILY.md |
| README skeleton (badge, scope, sweep, family, ToC) | R1 | R1 | SINGLE-SOURCE | FAMILY.md |
| Entry format tags+year hyphen | R1 | R1 | SINGLE-SOURCE | FAMILY.md + hub README examples are same standard restated |
| Year + canonical-URL rules copy hub CONTRIBUTING §5–6 | R1 | R1 | SINGLE-SOURCE | FAMILY.md |
| sysml-v2 uses simpler untagged entry format | R1 | R1 | SINGLE-SOURCE | spoke contributing + README same list |
| Hub CI lychee --include-fragments=anchor-only | R1 | R1 | SINGLE-SOURCE | config only (no code) |
| Go-live: flip Status + hub README spoke link | R1 | R1 | SINGLE-SOURCE | FAMILY.md |
| Sibling path next to hub is convention not FAMILY lock | R1 | R1 | SINGLE-SOURCE | skeptic; cartographer inferred from sysml path |
| Hub README ships tags+year | R1 | R1 | SINGLE-SOURCE | README.md |
| Documented divergence: FAMILY/hub tagged format vs sysml-v2 untagged | R1 | R1 | SINGLE-SOURCE | multi-doc independent files FAMILY + sysml contributing + sysml README — still no code; named as design constraint |
| sysml-v2 missing sweep badge and family pointer | R1 | R1 | SINGLE-SOURCE | sysml README |
| sysml links.yml advisory fail:false, no fragments | R1 | R1 | SINGLE-SOURCE | config |
| Neither hub nor sysml alone implements full FAMILY CI triad | R1 | R1 | SINGLE-SOURCE | config compare |
| Spoke CONTRIBUTING lacks year/dedupe/neutrality | R1 | R1 | SINGLE-SOURCE | doc |
| Hub README points at FAMILY.md only (no per-spoke links yet) | R1 | R1 | SINGLE-SOURCE | README + FAMILY model text |
| Hub still hosts Arcadia/Capella entries pending split | R1 | R1 | SINGLE-SOURCE | hub README |
| CONTRIBUTING.md vs contributing.md casing differs | R1 | R1 | SINGLE-SOURCE | paths |

## Round 1 Summary

| Claim | Lenses | Grade | Action |
|-------|--------|-------|--------|
| FAMILY shared standard is clone target | cart, prosp | SS | Prefer FAMILY+hub over sysml-v2 shape |
| Capella registry/scope already written | all three | SS | Go-live = Status + hub link |
| Entry format tags+year | cart, prosp, skep | SS | Do not clone sysml untagged format |
| CI: combine hub fragments + sysml lint triad | cart, prosp, skep | SS | New spoke CI = FAMILY triad |
| Sibling path convention | cart, skep | SS | Create at ../awesome-capella |

Fixes applied: 0
Coverage: 6/6 criteria covered (all decision-bearing SINGLE-SOURCE named)
Validation: PASS (parent fallback grades)

## Converged: Round 1

Track 1: Merged verdict CONTEXT_COMPLETE.
Every S1–S6 criterion covered. No CONFLICTED or STALE. Decision-bearing claims are SINGLE-SOURCE (doc/config family) and named for Synthesis.
Total rounds: 1  |  Total fixes: 0
Document is ready.
