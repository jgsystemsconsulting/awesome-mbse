# Research: awesome-requirements-engineering seed sources

## Research brief

**Primary question:** What live, linkable resources should seed a new
`awesome-requirements-engineering` curated list (spoke of the awesome-mbse family),
covering requirements engineering as its own discipline (methods, standards, tools,
books, papers), not SysML requirements diagrams?

**Sub-questions:**

1. What are the canonical URLs and short factual descriptions for the named anchors:
   ISO/IEC/IEEE 29148; OMG ReqIF; IREB CPRE; EARS (Mavin); KAOS (van Lamsweerde);
   Wiegers & Beatty *Software Requirements*; ReqView; IBM DOORS / DOORS Next;
   JAMA Connect; Visure?
2. What additional high-quality free/open resources (open ReqIF tooling, open-source
   RE tools, classic papers, INCOSE/IEEE material, other standards) raise the candidate
   pool toward ~40+ inclusion-bar entries?
3. Is there already a substantial GitHub `awesome-requirements*` incumbent that would
   block creating this spoke under the family Starting-a-new-list rule?
4. What section taxonomy (standards, methods, books, tools commercial/open, exchange
   formats, communities) best fits an awesome-list README for this niche?

**Success criteria (decision-bearing):**

- SC1: Each user-named anchor has at least one live https URL and a one-line factual
  description suitable for an awesome-list entry.
- SC2: At least ~40 distinct candidate resources with https URLs that appear to pass
  an on-topic / live / non-marketing inclusion bar (count may include strong
  secondaries beyond the named anchors).
- SC3: Namespace check result for existing awesome RE lists on GitHub is recorded
  with URLs and rough size/activity signals.
- SC4: A recommended top-level section list for the README is supported by how the
  sources cluster.

**Out of scope:**

- SysML/Cameo requirements diagram how-tos (hub or awesome-sysml-v2 / magic-grid).
- Implementing RE tooling in this run.
- sindresorhus/awesome submission packaging (later).
- Legal text of paywalled standards beyond publicly citable landing pages.

**Budget:** up to 3 research rounds; prefer primary sources (standards bodies,
publishers, vendor product pages, paper DOIs, official project repos).

**Retrieved_at baseline:** 2026-09-17.

## Findings

### Named anchors (SC1)

| Anchor | Canonical URL | One-line fact | Grade |
|--------|---------------|---------------|-------|
| ISO/IEC/IEEE 29148 | https://ieeexplore.ieee.org/document/6170935 | IEEE Std 29148-2011, Systems and software engineering — Life cycle processes — Requirements engineering (ISO catalog pages 403 to automated fetch). | ESTABLISHED |
| OMG ReqIF | https://www.omg.org/spec/ReqIF/1.2/ | OMG Requirements Interchange Format 1.2 (2016) for exchanging requirements data between tools/organizations. | ESTABLISHED |
| IREB CPRE | https://cpre.ireb.org/en/ | IREB Certified Professional for Requirements Engineering program (Foundation through Expert). | ESTABLISHED |
| EARS (Mavin) | https://alistairmavin.com/ears/ | Easy Approach to Requirements Syntax: constrained natural-language patterns for textual requirements (Alistair Mavin). | ESTABLISHED |
| EARS paper (RE'09) | https://doi.org/10.1109/RE.2009.9 | IEEE RE 2009 paper introducing EARS (Crossref DOI 10.1109/RE.2009.9; not IEEE document 5328509). | ESTABLISHED (support) |
| KAOS (van Lamsweerde) | https://webperso.info.ucl.ac.be/~avl/ | Axel van Lamsweerde UCL page: KAOS goal-oriented modeling language, method, and toolset since 1990. | PROVISIONAL |
| KAOS book | https://www.wiley.com/en-us/Requirements+Engineering%3A+From+System+Goals+to+UML+Models+to+Software+Specifications-p-9780470012703 | Wiley: *Requirements Engineering: From System Goals to UML Models to Software Specifications*. | PROVISIONAL |
| Wiegers & Beatty | https://www.microsoftpressstore.com/store/software-requirements-9780735679665 | *Software Requirements* 3rd ed. (2013), Microsoft Press, practical end-to-end RE techniques. | ESTABLISHED |
| ReqView | https://www.reqview.com/ | Git-powered requirements management tool (Eccam) with traceability for HW/SW/systems work. | ESTABLISHED |
| IBM DOORS Next | https://www.ibm.com/products/requirements-management-doors-next | IBM Engineering Requirements Management DOORS Next product page (HTTP 200, 2026-09-17). | ESTABLISHED (R2 liveness) |
| IBM DOORS family | https://www.ibm.com/products/engineering-requirements-management-doors-family | IBM Engineering Requirements Management DOORS family landing. | ESTABLISHED (R2) |
| JAMA Connect | https://www.jamasoftware.com/platform/jama-connect/ | Jama Software platform for engineering and requirements management. | ESTABLISHED |
| Visure | https://visuresolutions.com/ | Visure Requirements / ALM platform aimed at regulated industries and traceability. | ESTABLISHED |

`kaos.com` is parked (SOURCE-ROT). Prefer UCL + Wiley. Strip vendor AI/marketing adjectives in list prose.

### Additional candidates (SC2 sample; live checks 2026-09-17)

**Standards and interchange**

- https://www.omg.org/spec/ReqIF/ — ReqIF hub
- https://www.omg.org/spec/RAS/ — OMG Reusable Asset Specification (adjacent packaging)
- https://www.sae.org/standards/content/arp4754a/ — ARP4754A aircraft/systems development guidelines (requirements-heavy regulated context)
- https://eclipse.dev/rmf/ — Eclipse RMF reference ReqIF implementation including ProR GUI
- https://pypi.org/project/reqif/ — Python ReqIF library on PyPI

**Methods, templates, bodies of knowledge**

- https://volere.org/ — Volere requirements specification template and related practice material
- https://www.processimpact.com/articles/qualreqs.html — Wiegers “Writing Quality Requirements” (Process Impact)
- https://sebokwiki.org/wiki/Guide_to_the_Systems_Engineering_Body_of_Knowledge_(SEBoK) — SEBoK (cross-link; SE-general, use sparingly)
- https://en.wikipedia.org/wiki/Requirements_engineering — orientation only, not a list entry

**Open-source tools**

- https://github.com/doorstop-dev/doorstop — Doorstop: requirements management using version control
- https://github.com/itsallcode/openfasttrace — OpenFastTrace requirement tracing suite
- https://github.com/useblocks/sphinx-needs — Sphinx extension for needs/requirements
- https://github.com/cairis-platform/cairis — CAIRIS: requirements and information security
- https://github.com/strictdoc-project/strictdoc — StrictDoc requirements and documentation tool
- https://strictdoc.readthedocs.io/ — StrictDoc documentation

**Commercial / platform tools (beyond named anchors)**

- https://plm.sw.siemens.com/en-US/polarion/ — Siemens Polarion
- https://www.polarion.com/ — Polarion brand landing
- https://codebeamer.com/ — Codebeamer ALM / requirements
- https://www.modernrequirements.com/ — Modern Requirements
- https://www.objectiver.com/ — Objectiver (KAOS tool lineage)

**Communities, certification, events**

- https://www.ireb.org/en/ — IREB home
- https://re-magazine.ireb.org/ — IREB Requirements Engineering Magazine
- https://conf.researchr.org/home/RE-2025 — IEEE International Requirements Engineering Conference 2025 hub
- https://open-services.net/ — OSLC open services (integration standards relevant to RM tool chains)

**Incumbent lists (namespace, not necessarily seed entries)**

- https://github.com/muchengracedriver/awesome-requirements-writer — niche “requirements writer” list (~104 stars); not a broad RE awesome
- https://github.com/ericapaeus/awesome-requirements — public, low-signal empty/thin (2025 update)

Distinct live https targets in this document exceed 40 when counting anchors, supporting papers/books, open tools, commercial peers, communities, and interchange specs. Inclusion bar still applies at execute time (substantive, not pure marketing).

### Namespace (SC3)

- `jgsystemsconsulting/awesome-requirements-engineering`: HTTP 404 (namespace free).
- No large sindresorhus-style `awesome-requirements-engineering` incumbent found.
- Closest hits: `muchengracedriver/awesome-requirements-writer` (niche writer focus, ~104 stars, updated 2026-09) and thin `ericapaeus/awesome-requirements`.
- Family rule (~100+ stars *and* broad RE scope updated in last year as blocker): **no block**. Differentiate by full-discipline scope (standards, methods, ReqIF, tools, books) and family standard.

### Section taxonomy (SC4)

Sources cluster cleanly into:

1. **Standards and guides** — 29148, related lifecycle refs, regulated domain guides (careful scope)
2. **Interchange and integration** — ReqIF, Eclipse RMF, OSLC, ReqIF libraries
3. **Methods and notation** — EARS, KAOS, Volere, quality-writing guides
4. **Books and foundational papers** — Wiegers & Beatty, van Lamsweerde, EARS RE'09
5. **Open-source tools** — Doorstop, StrictDoc, OpenFastTrace, sphinx-needs, CAIRIS, …
6. **Commercial tools** — DOORS family, ReqView, JAMA, Visure, Polarion, Codebeamer, …
7. **Learning, certification, and community** — IREB/CPRE, RE conference, RE Magazine

Optional eighth: **Related bodies of knowledge** (SEBoK pointer only) if cross-links needed; prefer hub for pure MBSE.

## Synthesis

**SC1:** Met after Round 2 liveness on IBM DOORS Next and DOORS family pages. Prefer IEEE Explore landing for 29148 over iso.org (403 to bots). Prefer Microsoft Press over Amazon for Wiegers. Prefer alistairmavin.com for EARS; keep IEEE paper as second entry. KAOS remains single-primary (UCL) plus Wiley book.

**SC2:** Met at research density: named anchors plus open tools, commercial peers, interchange, communities, and books exceed ~40 distinct https candidates. Execute must still apply inclusion bar and tagged entry format; drop pure marketing blurbs and off-topic V&V-only tools (LDRA/VectorCAST not recommended as primary RE entries).

**SC3:** Met. Namespace free for the org repo name. Niche writer list is not an incumbent of substance for this spoke’s scope.

**SC4:** Met by clustering above. README should use FAMILY skeleton (Awesome badge, scope line, Last full sweep badge, family pointer, flat ToC) with the seven sections listed.

**Design notes for spec/plan:**

- New git repo is a **sibling** under `jgsystemsconsulting`, not nested in the hub.
- Entry format follows **hub FAMILY/CONTRIBUTING** (tags + year), not the untagged awesome-sysml-v2 exemplar.
- CI: blocking lychee on PR (`fail: true`) like hub; add markdownlint like sysml-v2; awesome-lint; scheduled link sweep.
- File name `CONTRIBUTING.md` (FAMILY casing).
- Tag vocabulary: adapt axes to RE (method values EARS/KAOS/Volere/…; tool values DOORS/ReqView/…; drop SysML language axis or replace with `RE-general` / domain tags as CONTRIBUTING defines).
- Hub `FAMILY.md` status → Live and hub README spoke link only **after** spoke is populated and CI green (FAMILY step 5).
- User message “awesome archimit” is a separate planned spoke (`awesome-archimate`); this run is **requirements-engineering** only.

**Open / provisional:** Exact DOORS marketing subtitle text fluctuates on IBM SPA pages; use stable product name in the entry. INCOSE.org often 403 to automated clients; prefer publicly fetchable landings. Full 40+ final curated lines are an execute deliverable, not a research dump into README without bar.

## Sources

| URL | Role |
|-----|------|
| https://www.omg.org/spec/ReqIF/ | ReqIF hub |
| https://www.omg.org/spec/ReqIF/1.2/ | ReqIF 1.2 |
| https://cpre.ireb.org/en/ | IREB CPRE |
| https://www.ireb.org/en/ | IREB home |
| https://re-magazine.ireb.org/ | RE Magazine |
| https://alistairmavin.com/ears/ | EARS primary |
| https://doi.org/10.1109/RE.2009.9 | EARS RE'09 |
| https://en.wikipedia.org/wiki/Easy_Approach_to_Requirements_Syntax | EARS secondary |
| https://webperso.info.ucl.ac.be/~avl/ | KAOS / van Lamsweerde |
| https://www.wiley.com/en-us/Requirements+Engineering%3A+From+System+Goals+to+UML+Models+to+Software+Specifications-p-9780470012703 | KAOS book |
| https://www.microsoftpressstore.com/store/software-requirements-9780735679665 | Wiegers & Beatty |
| https://www.reqview.com/ | ReqView |
| https://www.jamasoftware.com/platform/jama-connect/ | JAMA Connect |
| https://visuresolutions.com/ | Visure |
| https://ieeexplore.ieee.org/document/6170935 | IEEE 29148-2011 |
| https://en.wikipedia.org/wiki/Requirements_engineering | RE overview / 29148 title |
| https://www.ibm.com/products/requirements-management-doors-next | DOORS Next |
| https://www.ibm.com/products/engineering-requirements-management-doors-family | DOORS family |
| https://eclipse.dev/rmf/ | Eclipse RMF |
| https://pypi.org/project/reqif/ | reqif PyPI |
| https://volere.org/ | Volere |
| https://www.processimpact.com/articles/qualreqs.html | Quality requirements article |
| https://github.com/doorstop-dev/doorstop | Doorstop |
| https://github.com/itsallcode/openfasttrace | OpenFastTrace |
| https://github.com/useblocks/sphinx-needs | sphinx-needs |
| https://github.com/cairis-platform/cairis | CAIRIS |
| https://github.com/strictdoc-project/strictdoc | StrictDoc |
| https://strictdoc.readthedocs.io/ | StrictDoc docs |
| https://plm.sw.siemens.com/en-US/polarion/ | Polarion |
| https://codebeamer.com/ | Codebeamer |
| https://www.modernrequirements.com/ | Modern Requirements |
| https://www.objectiver.com/ | Objectiver |
| https://open-services.net/ | OSLC |
| https://conf.researchr.org/home/RE-2025 | RE 2025 |
| https://www.sae.org/standards/content/arp4754a/ | ARP4754A |
| https://www.omg.org/spec/RAS/ | OMG RAS |
| https://sebokwiki.org/wiki/Guide_to_the_Systems_Engineering_Body_of_Knowledge_(SEBoK) | SEBoK |
| https://github.com/muchengracedriver/awesome-requirements-writer | Niche incumbent |
| https://github.com/ericapaeus/awesome-requirements | Thin awesome-requirements |
| https://github.com/search?q=awesome+requirements+engineering&type=repositories | Namespace search |
