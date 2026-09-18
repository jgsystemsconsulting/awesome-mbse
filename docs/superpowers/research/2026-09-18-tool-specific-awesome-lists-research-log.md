# Research log: tool-specific awesome lists

Verdict legend: ESTABLISHED, PROVISIONAL, CONTRADICTED, SOURCE-ROT. Round verdicts: RESEARCH_COMPLETE, CONTRADICTIONS_OPEN, GAPS_REMAIN, TRIAGE_ABORTED (log unreadable/write failed/log corrupted).

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| awesome-capella exists as family spoke jgsystemsconsulting/awesome-capella (0 stars) | R1 | R1 | PROVISIONAL | scout+digger hit same URL; same URL twice = 1 independent source |
| sindresorhus/awesome has no MBSE/tool entries; no external awesome-* for major MBSE tools in available fetches | R1 | R1 | PROVISIONAL | scout+digger same URL = single source; claim self-scoped to "available fetches" (429 gaps) |
| no dedicated awesome-enterprise-architect/sparx/ea | R1 | R1 | PROVISIONAL | scout only, single search pass |
| enterprise-architect topic 50 repos, some Sparx, no awesome | R1 | R1 | PROVISIONAL | scout only, single source |
| no dedicated awesome-cameo/magicdraw/catia-magic | R1 | R1 | PROVISIONAL | scout only, single source |
| magicdraw topic 27; cameo topic 20; no awesome | R1 | R1 | PROVISIONAL | scout only, single source |
| no awesome-simulink/system-composer | R1 | R1 | PROVISIONAL | scout only, single source |
| no awesome for rhapsody/scade/papyrus/syson/openmbee | R1 | R1 | SOURCE-ROT | scout search was rhapsody-only URL; OpenMBEE org in fetch_fails (404); openmbee leg unfetched, other legs unsearched; demoted to PROVISIONAL for decisions, re-source next round |
| sysml topic 128 repos, no awesome | R1 | R1 | PROVISIONAL | scout only, single source |
| jgs org 22 repos MBSE, no awesome except capella | R1 | R1 | PROVISIONAL | digger only, single source |
| awesome-mbse hub 404 on public github (may be private; local workspace exists) | R1 | R1 | SOURCE-ROT | the 404 itself sits in fetch_fails; digger + scout hit same URL = 1 source; demoted to PROVISIONAL for decisions; re-source via API/authenticated check next round |
| family spoke bar ~40+ entries | R1 | R1 | PROVISIONAL | skeptic FAMILY.md primary, single source |
| awesome-cameo would duplicate hub flagship Cameo + magic-grid | R1 | R1 | PROVISIONAL | skeptic README only, single source |
| canonical routing: Magic Grid/Cameo how-tos go to awesome-magic-grid | R1 | R1 | PROVISIONAL | skeptic FAMILY.md only, single source |
| Cameo .mdzip proprietary, open corpus small | R1 | R1 | PROVISIONAL | skeptic README only, single source; world-claim resting on tertiary-style project doc |
| Cameo mdzip corpus grew 3 to 9 | R1 | R1 | PROVISIONAL | skeptic CHANGELOG primary, single source |
| has-model bar requires downloadable, openable files | R1 | R1 | PROVISIONAL | skeptic CONTRIBUTING only, single source |
| adjacent SE awesome lists abandoned (kktse 2021) | R1 | R1 | PROVISIONAL | skeptic FAMILY secondary, single source |
| vendor 403/WAF hostility to link checkers | R1 | R1 | ESTABLISHED | skeptic CHANGELOG primary + this round's own fetch_fails (MathWorks/Sparx/SO 403s) as independent corroboration |
| hub tags: Cameo, CATIA-Magic, Papyrus, Rhapsody, SysON; not EA/Simulink | R1 | R1 | PROVISIONAL | skeptic CONTRIBUTING only, single source |
| Capella poor template for proprietary tools (eclipse-capella is OSS) | R1 | R1 | PROVISIONAL | skeptic prior research secondary, single source |
| awesome-magic-grid not yet a clean niche spoke | R1 | R1 | PROVISIONAL | skeptic FAMILY only, single source |
| one-canonical-home rule raises dedupe burden | R1 | R1 | PROVISIONAL | skeptic FAMILY only, single source; analyst interpretation |

## Round 1 summary

- fetch_fails noted: many GitHub 429s, MathWorks/Sparx/SO 403s, awesome-mbse 404, OpenMBEE org 404, trademark pages fail.
- Round metrics: total 23, established 1, provisional 20, contradicted 0, source_rot 2, demoted_rot 2.
- No CONTRADICTED claims this round.
- SOURCE-ROT handling: claims 8 and 11 demoted to PROVISIONAL pending re-source; neither left undemoted.
- Coverage: SC1 met (gap evidence provisional quality), SC2 met, SC3 met, SC4 partial, SC5 met, SC6 unmet.
- Genuine fixes needed:
  1. Claim 11: confirm awesome-mbse public/private status via GitHub API or authenticated check before hub decisions.
  2. Claim 8: run per-tool searches for scade, papyrus, syson, openmbee; rhapsody-only URL left four tools unsearched.
  3. Claim 2 / SC4: retry 429'd GitHub searches so absence claims rest on complete fetch coverage.
- Round verdict: GAPS_REMAIN (SC6 unmet, SC4 partial; no contradictions open; no undemoted SOURCE-ROT).

## Round 2 summary

Parent gh API (2026-09-18) re-sourced R1 gaps before rate limit:
- awesome-mbse private=true (explains public 404) → claim 11 fixed
- exact awesome-enterprise-architect, awesome-sparx, awesome-cameo, awesome-magicdraw: total_count 0
- awesome-rhapsody|papyrus|syson|openmbee|scade exact awesome search: 0
- mathworks/awesome-matlab-students 742★; mathworks-robotics/awesome-matlab-robotics 1714★
- Open-MBEE org ~150 repos (org page ~167); eclipse-capella/capella 343★
- "enterprise architect" sparx ~89; topic enterprise-architect ~49
- magicdraw|"cameo systems"|nomagic ~252
- "system composer" matlab OR simulink mbse ~2
- ORNL-Modelica/awesome-modelica + traversaro/awesome-fmi exist
- Rate limit hit mid namespace loop after confirming key exact names

Lens R2: scout/digger corroborated MathWorks/Modelica/FMI/Capella/OpenMBEE pages; Sparx/MathWorks vendor hubs still 403. Skeptic established EA name collision with ArchiMate, .eap outside has-model formats, magic-grid unfinished, DE under 40, Capella OSS non-transfer.

| Claim | Lenses | Grade | Action |
|-------|--------|-------|--------|
| No Sparx EA awesome (exact name 0) | scout, digger, parent-gh | EST | SC1 closed |
| No external Cameo/MagicDraw awesome | scout, digger, parent-gh | EST | SC2 closed |
| awesome-capella family spoke public | scout, digger, parent-gh | EST | SC3 closed |
| MathWorks already has MATLAB/Simulink awesomes | scout, digger, parent-gh | EST | Blocks family awesome-simulink |
| Open-MBEE ~150+ repos mass | scout, digger, parent-gh | EST | Platform candidate, not rush spoke |
| System Composer MBSE GitHub ~2 | parent-gh | PROV | Hub-only |
| EA name collides with ArchiMate "EA" | skeptic FAMILY/spec | EST | Naming landmine |
| .eap not in has-model formats | skeptic CONTRIBUTING | EST | Gallery bar friction |
| magic-grid unfinished hub fork | skeptic FAMILY | EST | Finish before new Cameo name |
| Vendor trademark guideline quotes | — | PROV | SC6 residual; 403/404 |
| Ranked shortlist SC4 | synthesis | EST (decision) | Written in findings doc |

Fixes applied: 3 (hub privacy, multi-tool awesome absence, ecosystem counts)
Coverage: SC1–SC5 met; SC6 provisional trademarks only
Validation: PASS with named provisional
Verdict: Track 3 brief-covered (Round 2); no Round 3

## Round 2 Summary

| Claim | Lenses | Grade | Action |
|-------|--------|-------|--------|
| No Sparx EA awesome list | scout, digger, parent-gh | EST | Resourced (Round 2) |
| No external Cameo awesome | scout, digger, parent-gh | EST | Resourced (Round 2) |
| Capella family spoke | scout, digger, parent-gh | EST | Resourced (Round 2) |
| Shortlist ranked | parent synthesis | EST | Closed SC4 |
| Hub-only flags | skeptic + counts | EST | Closed SC5 |
| Trademark prose | blocked fetches | PROV | Named in Synthesis |

Fixes applied: 3
Coverage: 5/6 criteria met (SC6 provisional)
Validation: PASS
Track 3: brief-covered. Merged residual: SC6 trademarks PROVISIONAL only.
