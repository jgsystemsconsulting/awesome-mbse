# Research: awesome-digital-engineering seed corpus

## Research brief

**Primary question:** What official policy, standards, reports, and community resources form a defensible seed corpus for a new awesome-list repo covering digital thread, model-based definition (MBD), and digital engineering (DE) transformation?

**Sub-questions:**
1. Canonical DoD Digital Engineering Strategy / policy (titles, dates, URLs).
2. ASME Y14.41 / related MBD standards and free overviews.
3. ISO 10303 STEP parts for digital thread / MBD interoperability and public entry points.
4. NDIA digital-thread / DE papers or working-group outputs.
5. NASA and INCOSE DE / digital-thread resources.
6. Other core open DE resources, tools, standards bodies, competing awesome lists.
7. In vs out vs awesome-mbse and awesome-sysml-v2.

**Success criteria:** SC1 primary URLs (DoD, ASME Y14.41, ISO 10303, NDIA, NASA, INCOSE); SC2 inclusion/exclusion boundary; SC3 ~40+ linkable public resources or honest shortfall; SC4 incumbent awesome list check; SC5 dates/versions for flagship policy docs.

**Out of scope:** Full commercial PLM matrices; SysML language tooling; writing README entries in this gate.

**Budget:** 3 rounds max. Retrieved_at baseline: 2026-09-17.

## Findings

### ESTABLISHED

1. **ASME Y14.41 Digital Product Definition Data Practices** has a live ASME storefront. Meta description: establishes requirements for digital product definition data (data sets) such as annotated models with or without a drawing graphic sheet. Storefront presents a 2026 edition context. URL: https://www.asme.org/codes-standards/find-codes-standards/y14-41-digital-product-definition-data-practices (primary; scout + digger + parent curl).

2. **No substantive awesome-digital-engineering incumbent.** GitHub search for the name returned unrelated low-star hits. `gh api` on `jgsystemsconsulting/awesome-digital-engineering` returns 404. Org awesome search shows only `awesome-mbse` (private) and `awesome-sysml-v2` (public). `gh api search/repositories?q=awesome+digital+engineering` total_count 9, top hit `Awesome-AECO` (AECO domain, not DE policy/MBD).

### PROVISIONAL (named)

3. **Family rules constrain the corpus.** Hub CONTRIBUTING: legally linkable, publicly accessible; link never re-host. `has-model` requires directly downloadable non-paywalled model files. FAMILY.md: a spoke earns a repo only with roughly 40+ live entries and no substantive incumbent; below that the hub keeps a section. (Single-source internal docs.)

4. **DMSC / QIF.** https://qifstandards.org/about-dmsc/ - Digital Metrology Standards Consortium; QIF (ISO 23952:2020) and DMIS (ISO 22093:2011).

5. **LOTAR.** https://lotar-international.org/ - long-term archiving EN/NAS 9300 family grounded on ISO 14721 (OAIS).

6. **ISO 10303 (STEP)** is the product data representation and exchange family (PMI, CAD/CAM interoperability, long-term archive). Public narrative entry: Wikipedia ISO 10303 (secondary). iso.org catalog pages returned 403 in this environment (SOURCE-ROT for those URLs).

7. **NASA NTRS** search API for `"digital engineering"` reports total 79 public-distribution hits (sample: "ExMC Digital Engineering" poster, distributionDate 2025-01-28). This is a corpus *signal*, not 40 curated awesome entries.

8. **DoD Digital Engineering Strategy (commonly cited 2018)** could not be live-fetched here: `acq.osd.mil` certificate failures, `media.defense.gov` 403, Wayback CDX 503. Canonical paths remain commonly cited in the field but are **unverified this session**. Spec/plan must treat title/year/URL as provisional until a clean fetch or local PDF hash is recorded.

9. **NDIA, INCOSE DE pages, SEBoK Digital Engineering, OMG DEIX wiki** - fetch blocked or failed (403/Incapsula/SSL). Do not invent quotes.

### SOURCE-ROT / fetch_fails (selected)

- https://www.acq.osd.mil/se/docs/2018-Digital-Engineering-Strategy.pdf - cert verify failed
- https://media.defense.gov/2018/Jun/15/2001931999/-1/-1/0/20180614_DIGITAL_ENGINEERING_STRATEGY_FINAL.PDF - 403
- https://www.iso.org/standard/* - 403
- https://www.incose.org/* DE paths - 403
- https://www.ndia.org/* - Incapsula
- https://sebokwiki.org/wiki/Digital_Engineering - failed this session
- https://ntrs.nasa.gov/citations/20210014808 - 503 earlier

## Synthesis

**Decision support for creating the spoke**

- **Namespace:** clear for `awesome-digital-engineering` under `jgsystemsconsulting` (SC4 met).
- **Niche identity (SC2):** FAMILY already routes "Digital thread, MBD, digital engineering policy and standards" to this spoke. Hub keeps general MBSE; SysML v2 language tooling stays on awesome-sysml-v2. Paywalled ASME/ISO *full text* may appear only as storefront or free overview links, never as re-hosted PDFs. Free depth will lean on NIST/NTRS/LOTAR/DMSC/open tools, not CAD vendor manuals.
- **Seed reality (SC3):** Round 1 did **not** prove 40 curated free public entries. Honest shortfall. Strong signals exist (NTRS 79 DE hits; ASME + DMSC + LOTAR + STEP narrative + family-required policy section once DoD URL verifies). Execute must run a **seed inventory gate** before claiming the list is launch-ready: gather >=40 candidate rows that pass inclusion bar, or keep content as a hub section and only stand up the empty spoke skeleton if the maintainer explicitly accepts a thin launch.
- **Flagship policy (SC1/SC5):** Only ASME Y14.41 storefront is ESTABLISHED with date context. DoD strategy, ISO catalog, NDIA, INCOSE remain blocked. Plan tasks that add those entries must include a live link-check step; do not bake unverified .mil URLs into CI-green claims.

**Recommended section taxonomy (for spec, not yet populated):** Policy and strategy; Standards (MBD / STEP / QIF / LOTAR); Digital thread and interoperability; Model-based definition and PMI; Government and consortia programs; Open tools and reference implementations; Learning and reports; Commercial platforms (clearly tagged `paid`).

## Sources

| URL | Role |
|-----|------|
| https://www.asme.org/codes-standards/find-codes-standards/y14-41-digital-product-definition-data-practices | ASME Y14.41 storefront |
| https://qifstandards.org/about-dmsc/ | DMSC / QIF |
| https://lotar-international.org/ | LOTAR |
| https://github.com/search?q=awesome-digital-engineering&type=repositories | Incumbent search |
| https://api.github.com/repos/jgsystemsconsulting/awesome-digital-engineering | Org namespace 404 |
| https://api.github.com/search/repositories?q=awesome+digital+engineering | Search total_count |
| https://ntrs.nasa.gov/api/citations/search/?q=%22digital%20engineering%22&page.size=5 | NASA corpus signal |
| https://github.com/jgsystemsconsulting/awesome-mbse/blob/main/CONTRIBUTING.md | Inclusion bar |
| https://github.com/jgsystemsconsulting/awesome-mbse/blob/main/FAMILY.md | 40+ spoke gate, scope |
| https://en.wikipedia.org/wiki/ISO_10303 | STEP secondary narrative (provisional) |
