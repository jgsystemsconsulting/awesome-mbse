# Research: awesome-capella canonical sources

## Research brief

**Primary question:** What durable official and community URLs, versions, and resources should seed an `awesome-capella` curated list (Capella tool and the Arcadia method)?

**Sub-questions:**
1. Eclipse Capella official site, download/docs, and GitHub org `eclipse-capella` (capella and related repos)
2. Arcadia method at arcadia-method.com and durable method documentation
3. python4capella and other scripting / API / addon ecosystems
4. Capella Collaboration Manager and related collaboration tooling
5. Pascal Roques books and Capella Days talks / proceedings
6. Example models, add-on marketplace / catalog, training and courses
7. GitHub namespace check for `awesome-capella`, `awesome-arcadia`, and close incumbents
8. Depth bar: roughly 40 candidate entry types that pass a substantive inclusion bar (FAMILY.md spoke threshold)

**Success criteria:**
- R1: Canonical https URLs for Capella product home, docs, and primary GitHub repos with version identity where public
- R2: Canonical Arcadia method home and primary method docs
- R3: Confirmed links for python4capella and other high-signal addons / APIs
- R4: Capella Collaboration Manager (or current collab product) durable URL
- R5: Pascal Roques book identity (title/year/publisher page) and Capella Days hub
- R6: Example model collections and training entry points
- R7: Namespace check result for awesome-capella / similar lists
- R8: Enough named candidate types to justify a spoke (~40+) or an honest shortfall

**Out of scope:** Writing list prose; hub FAMILY edits; commercial sales copy without a durable product page; building the repo.

**Budget:** light tier, 1 round preferred. Retrieved_at target: 2026-09-17.

## Findings

- **ESTABLISHED.** Official Capella product home is `https://mbse-capella.org/`. `https://www.eclipse.org/capella/` and `https://eclipse.dev/capella/` 302-redirect off-host to it. Prefer mbse-capella.org as the canonical entry URL. Sources: mbse-capella.org home; eclipse.org redirect; eclipse.dev redirect. Retrieved 2026-09-17.
- **ESTABLISHED.** Primary source repo is `https://github.com/eclipse-capella/capella` (open-source MBSE tool, EPL-2.0). Sources: GitHub repo pages via scout and digger. Retrieved 2026-09-17.
- **PROVISIONAL.** Latest public release identity reported as v7.1.0 (03 Aug 2026) from the releases list; direct tag URL `.../releases/tag/7.1.0` 404'd in the same wave. Treat version as provisional until tag/page re-check on seed. Source: releases list. Retrieved 2026-09-17.
- **PROVISIONAL (method page) / ESTABLISHED (dead alternate).** Arcadia method durable page is `https://mbse-capella.org/arcadia.html` (ARChitecture Analysis and Design Integrated Approach; AFNOR Z67-140 cited). The brief seed `arcadia-method.com` does not resolve (www and apex DNS ENOTFOUND); archive probe failed. Do not list arcadia-method.com. Sources: arcadia.html (PROVISIONAL single lens); DNS failures multi-URL ESTABLISHED. Retrieved 2026-09-17.
- **ESTABLISHED.** Jean-Luc Voirin, *Model-based System and Architecture Engineering with the Arcadia Method*, Elsevier, 2017, ISBN 978-1-78548-169-7. URL: Elsevier shop page. Retrieved 2026-09-17.
- **ESTABLISHED.** Pascal Roques, *Systems Architecture Modeling with the Arcadia Method*, Elsevier, 2017, ISBN 978-1-78548-168-0. URL: Elsevier shop page. Retrieved 2026-09-17.
- **ESTABLISHED.** python4capella: `https://github.com/labs4capella/python4capella`. Official addons page also lists it (Thales & Obeo, EPL) as PROVISIONAL single-lens corroboration. Retrieved 2026-09-17.
- **PROVISIONAL.** py-capellambse headless Python: `https://github.com/DSD-DBS/py-capellambse`. Retrieved 2026-09-17.
- **ESTABLISHED (org depth) / PROVISIONAL (individual stars).** eclipse-capella org hosts addon repos including capella-requirements-vp, capella-cybersecurity, capella-xhtml-docgen, capella-sss-transition, capella-studio. Labs4Capella hosts stpa-capella, DSM4Capella, mms-capella, bridge-capella-ea (PROVISIONAL). Official catalog: `https://mbse-capella.org/addons.html`. Retrieved 2026-09-17.
- **OPEN (R4).** No durable public URL found for "Capella Collaboration Manager". Candidate GitHub paths under ObeoNetwork and eclipse-capella 404. Wiki mentions "Team for Capella" as the collab product name. Execute must resolve the current Obeo/Thales commercial product page before listing, or omit until found.
- **ESTABLISHED.** Capella Days hub: `https://mbse-capella.org/capella_days_2026.html` (10th edition, 1–3 Dec 2026, online, free; editions back to 2017 with replay playlists). Retrieved 2026-09-17.
- **ESTABLISHED.** Case-study PDF paths under mbse-capella.org resources (Rolls-Royce, ArianeGroup, CNES). IFE example model referenced from addons/resources. Training pointer from home toward Obeo Capella professional offer. Retrieved 2026-09-17.
- **PROVISIONAL (R7).** Exact `awesome-capella` org and `awesome-capella/awesome-capella` repo 404. Search for awesome-capella / awesome-arcadia returned no prominent incumbent but hit GitHub 429. Recheck namespace the day the repo is created (FAMILY.md rule). Retrieved 2026-09-17.
- **OPEN (R8).** No lens produced a counted inventory of ~40 inclusion-bar candidates. Named seeds above are well under 40 as listed; ecosystem pages (addons, Days archives, eclipse-capella repos, case studies, books, training) make the bar plausible but uncounted. Seed pass during execute must gather ≥40 or keep Status Planned and stay hub-only.

**Dead hosts to exclude:** arcadia-method.com; capella.polarsys.org; projects.eclipse.org/projects/modeling.capella (404); legacy eclipse.org/capella/* content paths (redirect only, prefer mbse-capella.org targets).

## Synthesis

Canonical Capella list should center on **mbse-capella.org** and **github.com/eclipse-capella**, not eclipse.org paths or PolarSys. Arcadia method content lives under mbse-capella.org/arcadia.html; the user-supplied arcadia-method.com seed is dead as of 2026-09-17.

Seed pillars that are solid enough to ship: Capella core + docs/download pages; Arcadia method page; Voirin and Roques books; python4capella; official addons page and named eclipse-capella / labs4capella repos; Capella Days hub; case studies; Obeo training entry once URL confirmed on seed.

Blockers for a full spoke claim:
1. **R4** collab product: resolve "Team for Capella" (or current name) commercial URL, or leave the collab section thin.
2. **R8** depth: run an explicit seed inventory to ≥40 inclusion-bar URLs before calling the spoke "live" with a full list; FAMILY.md allows Planned until then.

Namespace looks free for `jgsystemsconsulting/awesome-capella` but must be rechecked on create day. No Track 1 RESEARCH_COMPLETE: light-tier halt with R4/R8 open and named.

## Sources

| URL | Role |
|-----|------|
| https://mbse-capella.org/ | Capella product home |
| https://mbse-capella.org/arcadia.html | Arcadia method |
| https://mbse-capella.org/addons.html | Official addons catalog |
| https://mbse-capella.org/resources.html | Resources / case studies |
| https://mbse-capella.org/capella_days_2026.html | Capella Days hub |
| https://www.eclipse.org/capella/ | Legacy redirect to mbse-capella.org |
| https://eclipse.dev/capella/ | Legacy redirect to mbse-capella.org |
| https://github.com/eclipse-capella/capella | Core Capella repo |
| https://github.com/eclipse-capella | Capella GitHub org / addons |
| https://github.com/eclipse-capella/capella/releases | Release list (v7.1.0 provisional) |
| https://github.com/eclipse-capella/capella/wiki | Wiki / release notes |
| https://github.com/labs4capella/python4capella | python4capella |
| https://github.com/labs4capella | Labs4Capella org |
| https://github.com/DSD-DBS/py-capellambse | Headless Python Capella |
| https://shop.elsevier.com/books/model-based-system-and-architecture-engineering-with-the-arcadia-method/voirin/978-1-78548-169-7 | Voirin book |
| https://shop.elsevier.com/books/systems-architecture-modeling-with-the-arcadia-method/roques/978-1-78548-168-0 | Roques book |
| https://www.obeosoft.com/en/capella-professional-offer#coaching | Training pointer (confirm on seed) |
| https://github.com/awesome-capella | 404 namespace probe |
| https://api.github.com/repos/awesome-capella/awesome-capella | 404 namespace probe |
| https://arcadia-method.com/ | Dead DNS (exclude) |
| https://www.arcadia-method.com/ | Dead DNS (exclude) |
| https://capella.polarsys.org/ | Dead DNS (exclude) |
