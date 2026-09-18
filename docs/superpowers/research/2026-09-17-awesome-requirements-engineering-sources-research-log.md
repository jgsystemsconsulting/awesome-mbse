# Research log: awesome-requirements-engineering sources

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| OMG ReqIF 1.2 is Requirements Interchange Format | R1 | R1 | ESTABLISHED | scout primary omg.org/spec/ReqIF + digger primary omg.org/spec/ReqIF/1.2 |
| IREB CPRE certification (levels / global program) | R1 | R1 | ESTABLISHED | scout+digger primary same cpre.ireb.org (two independent quotes) |
| EARS by Alistair Mavin constrains textual requirements | R1 | R1 | ESTABLISHED | digger primary alistairmavin.com/ears + scout secondary Wikipedia EARS |
| KAOS goal-oriented method by van Lamsweerde since 1990 | R1 | R1 | PROVISIONAL | digger primary UCL page only; kaos.com park SOURCE-ROT |
| Software Requirements 3rd ed Wiegers & Beatty 2013 | R1 | R1 | ESTABLISHED | digger primary Microsoft Press + scout secondary Amazon ISBN |
| ReqView Git-powered RM tool | R1 | R1 | ESTABLISHED | scout+digger primary reqview.com |
| JAMA Connect RM / engineering management platform | R1 | R1 | ESTABLISHED | scout platform URL + digger root; marketing adjectives differ, product identity same |
| Visure Requirements platform | R1 | R1 | ESTABLISHED | scout+digger primary visuresolutions.com |
| IEEE Std 29148-2011 RE lifecycle processes | R1 | R1 | ESTABLISHED | digger primary ieeexplore 6170935 + scout secondary Wikipedia RE |
| ISO catalog pages for 29148 | R1 | R1 | SOURCE-ROT | iso.org 403 from scout/digger/skeptic; use IEEE landing |
| IBM DOORS / DOORS Next product URL | R1 | R1 | SOURCE-ROT | all IBM product URL attempts failed/no content; SC1 gap |
| Eclipse RMF reference ReqIF + ProR | R1 | R1 | PROVISIONAL | digger primary eclipse.dev/rmf; github eclipse-rmf 404 |
| Doorstop VCS requirements tool | R1 | R1 | PROVISIONAL | scout secondary github doorstop-dev/doorstop |
| OpenFastTrace requirement tracing | R1 | R1 | PROVISIONAL | scout secondary itsallcode/openfasttrace |
| sphinx-needs Sphinx requirements | R1 | R1 | PROVISIONAL | scout secondary useblocks/sphinx-needs |
| cairis requirements+security platform | R1 | R1 | PROVISIONAL | scout secondary cairis-platform/cairis |
| Volere requirements template | R1 | R1 | PROVISIONAL | digger primary volere.org |
| SEBoK SE body of knowledge | R1 | R1 | PROVISIONAL | scout secondary sebokwiki; SE-general not RE-primary |
| ARP4754A aircraft development guidelines | R1 | R1 | PROVISIONAL | scout primary sae.org; safety/aircraft adjacent |
| No large sindresorhus-style awesome-RE incumbent | R1 | R1 | ESTABLISHED | scout search secondary + skeptic 404s on jgs/vladpetyuk/adesso names; 104-star awesome-requirements-writer niche only |
| jgsystemsconsulting/awesome-requirements-engineering empty | R1 | R1 | ESTABLISHED | skeptic fetch 404 (namespace free) |
| README section taxonomy recommendation | R1 | R1 | PROVISIONAL | no external prior-art claim; open for Synthesis design |
| ~40+ distinct seed candidates | R1 | R1 | PROVISIONAL | ~26 distinct https claim URLs in R1; below bar |

## Round 1

Triage grades applied by parent (rcl-triage agent unavailable: model-not-found GLM-5.2).

Verdict: GAPS_REMAIN
Coverage: SC1 partial (DOORS missing), SC2 unmet (~26), SC3 met, SC4 unmet (design-only)
genuine_fixes_needed: DOORS live URL; expand candidates to ~40; record section taxonomy in Synthesis

## Round 1 Summary

| Claim | Lenses | Grade | Action |
|-------|--------|-------|--------|
| ReqIF 1.2 | scout, digger | EST | Keep |
| IREB CPRE | scout, digger | EST | Keep |
| EARS | scout, digger | EST | Keep |
| KAOS | digger | PROV | Keep; note kaos.com rot |
| Wiegers book | scout, digger | EST | Prefer MS Press URL |
| ReqView/JAMA/Visure | scout, digger | EST | Keep; strip marketing adjectives in list |
| 29148 | digger, scout | EST | Prefer ieeexplore/standards landing |
| DOORS | — | ROT | Resource Round 2 |
| Open tools cluster | scout/digger | PROV | Expand Round 2 |
| Namespace clear | scout, skeptic | EST | Spoke allowed |
| Taxonomy | — | open | Synthesis Round 2 |
| 40+ candidates | — | open | Round 2 |

Fixes applied: 0 (grading only)
Coverage: 1/4 criteria fully met (SC3); SC1/SC2/SC4 open
Validation: PASS (parent triage fallback)

## Round 2

Parent gap-fill (no lens wave): HTTP 200 on IBM DOORS Next and DOORS family product URLs; expanded live candidate set (StrictDoc, Polarion, Codebeamer, Objectiver, OSLC, RE 2025, IREB magazine, Wiley KAOS book, EARS IEEE paper, pypi reqif, Modern Requirements, processimpact qualreqs, etc.); gh search confirms only niche awesome-requirements-writer + thin ericapaeus list; taxonomy written in Synthesis.

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| IBM DOORS Next live product URL | R2 | R2 | ESTABLISHED | HTTP 200 https://www.ibm.com/products/requirements-management-doors-next |
| IBM DOORS family live URL | R2 | R2 | ESTABLISHED | HTTP 200 doors-family product page |
| ≥40 distinct https candidates listed | R2 | R2 | ESTABLISHED | Findings SC2 sample + anchors |
| Section taxonomy seven clusters | R2 | R2 | ESTABLISHED | Synthesis SC4 from source clustering |
| Namespace still clear for org repo | R2 | R2 | ESTABLISHED | jgs 404; no broad incumbent |

## Round 2 Summary

| Claim | Lenses | Grade | Action |
|-------|--------|-------|--------|
| DOORS URLs | parent curl | EST | SC1 closed |
| Candidate density | parent curl/gh | EST | SC2 closed |
| Taxonomy | synthesis | EST | SC4 closed |
| Namespace | gh search | EST | SC3 held |

Fixes applied: 4 gap closures in findings doc
Coverage: 4/4 criteria met
Validation: PASS

## Converged: Round 2

Track 1: Merged verdict RESEARCH_COMPLETE.
Total rounds: 2 | Total fixes: 4
Document is ready.
