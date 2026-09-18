# Research log: awesome-digital-engineering

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| ASME Y14.41 digital product definition data practices (2026 storefront) | R1 | R1 | ESTABLISHED | Scout + digger primary same ASME URL; parent curl confirms title/meta |
| No jgsystemsconsulting/awesome-digital-engineering repo; no substantive DE awesome incumbent | R1 | R1 parent | ESTABLISHED | Scout GitHub search + gh api repo 404 + gh search total_count 9 unrelated |
| Family public-link inclusion bar; paywalled full texts are link-only | R1 | R1 | PROVISIONAL | Single primary: hub CONTRIBUTING |
| has-model excludes paywalled files | R1 | R1 | PROVISIONAL | Single primary: hub CONTRIBUTING |
| Spoke needs ~40+ live entries else stay hub section | R1 | R1 | PROVISIONAL | Single primary: FAMILY.md |
| DMSC QIF ISO 23952 / DMIS | R1 | R1 | PROVISIONAL | Scout primary qifstandards.org only |
| LOTAR EN/NAS 9300 / OAIS | R1 | R1 | PROVISIONAL | Scout primary lotar-international.org; parent curl confirms homepage |
| NASA NTRS has public DE-tagged corpus (79 hits for digital engineering) | R1 parent | R1 parent | PROVISIONAL | NTRS search API only |
| DoD Digital Engineering Strategy primary PDF/HTML | R1 | R1 | SOURCE-ROT | acq.osd.mil cert fail; media.defense.gov 403; wayback CDX 503 |
| ISO.org STEP catalog pages | R1 | R1 | SOURCE-ROT | iso.org 403 throughout |
| NDIA systems-engineering DE pages | R1 | R1 | SOURCE-ROT | Incapsula / no content |
| INCOSE DE working-group pages | R1 | R1 | SOURCE-ROT | 403 |
| SEBoK Digital Engineering page | R1 parent | R1 parent | SOURCE-ROT | fetch failed this session |
| ISO 10303 identity (STEP / PMI exchange) | R1 parent | R1 parent | PROVISIONAL | Wikipedia HTML observed; REST summary SSL fail later |

## Round 1

Triage: parent-written (rcl-triage agent model pin unavailable: GLM-5.2 model-not-found). Graded from rcl-merge output plus parent alternate fetches (gh api, NTRS, ASME curl, LOTAR/DMSC curl).

Coverage: SC1 partial / SC2 partial / SC3 unmet-as-count / SC4 met / SC5 partial (ASME 2026 only).
Verdict: GAPS_REMAIN then Track 3 halt.

## Round 1 Summary

| Claim | Lenses | Grade | Action |
|-------|--------|-------|--------|
| ASME Y14.41-2026 storefront | scout, digger, parent | EST | Keep |
| No DE awesome incumbent / org repo empty | scout, digger, parent gh | EST | Keep |
| Family inclusion + 40+ gate | skeptic | PROV | Name in Synthesis |
| DMSC / LOTAR | scout | PROV | Seed candidates |
| DoD / ISO.org / NDIA / INCOSE / SEBoK | - | ROT | Cite known paths as provisional; plan must not claim live fetch |
| NTRS DE corpus size signal | parent | PROV | Partial SC3 signal, not 40 curated entries |
| ~40 curated free public entries proven | - | unmet | Honest shortfall |

Fixes applied: 0 (parent synthesis only)
Coverage: SC4 met; others partial or unmet with named gaps
Validation: PASS (parent triage after agent pin fail)

## Converged: Round 1

Track 3: diminishing-return halt. Predicate: brief-covered.
Reason: SC4 established; ASME established; org namespace empty established; remaining SC1 hosts blocked by SSL/403/WAF this environment; SC3 cannot be closed without manual seed inventory in execute. Further lens waves would repeat fetch_fails.
Total rounds: 1  |  Total fixes: 0
Document is ready.
