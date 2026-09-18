# Research log: awesome-stpa-sources

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| No dedicated awesome-stpa list | R1 | R2 | ESTABLISHED | R1 scout/digger + parent gh api (unrelated stamp hits only) + topics |
| MIT PSAS central hub | R1 | R2 | ESTABLISHED | multi-lens + HTTP 200 |
| STPA Handbook free PDF | R1 | R2 | ESTABLISHED | PSAS + HTTP 200 |
| 40+ candidate inventory | R1 | R2 | ESTABLISHED | scout R2 40+ named URLs; parent HTTP spot-checks |
| Tool set XSTAMPP/MicroSTAMP/PASTA/Capella | R1 | R2 | ESTABLISHED | digger quotes + HTTP 200 |
| ARP4761A catalog | R1 | R2 | ESTABLISHED | SAE HTTP 200 |
| ISO 26262 as context not mandate | R1 | R2 | PROVISIONAL | 403 on ISO; skeptic gap on mandate text — list must not overclaim |
| Dead hosts sunnyday/sahra/safetbox | R1 | R2 | ESTABLISHED | fetch_fails multi-round |
| awesome badge/lint/CC0 | R1 | R2 | ESTABLISHED | scout + FAMILY local |
| STPA tag axes | R1 | R2 | PROVISIONAL | proposal for CONTRIBUTING |
| SafetyHAT/MathWorks live | R1 | R2 | SOURCE-ROT | timeouts/403 — exclude or recheck at execute |
| Skeptic R2 fetch broken | R2 | R2 | — | backend error; parent HTTP used |

## Round 1

Triage parent-fallback. verdict: GAPS_REMAIN (SC2 unmet).

## Round 1 Summary

Coverage: SC2 open. next=Round 2

## Round 2

Gap slice: candidate expansion + namespace reconfirm. Parent HTTP + gh api. Skeptic WebFetch broken (honest zero).

Coverage: SC1–SC4 met with named PROVISIONAL on ISO mandate wording and tag list polish.
genuine_fixes_needed: 0 for research gate
verdict: RESEARCH_COMPLETE

## Round 2 Summary

| Claim | Lenses | Grade | Action |
|-------|--------|-------|--------|
| Namespace clear | scout, parent | EST | Done |
| 40+ candidates | scout, digger, parent | EST | Done |
| Skeleton | scout, FAMILY | EST | Done |
| Tags | scout | PROV | Named in Synthesis |
| ISO mandate | — | PROV | Guardrail in Synthesis |

Fixes applied: 0
Coverage: 4/4 criteria met (2 provisional named)
Validation: PASS (parent fallback triage)

## Converged: Round 2

Track 1: Merged verdict RESEARCH_COMPLETE.
Total rounds: 2  |  Total fixes: 0
Document is ready.
