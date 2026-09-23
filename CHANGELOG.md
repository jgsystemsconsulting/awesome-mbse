# Changelog

Maintenance sweeps and notable changes. The "Last full sweep" badge in the README
tracks the most recent dated entry here.

## [1.1.0] - 2026-09-22

### Added
- Root `COPYRIGHT` file, `CITATION.cff`, bug-report issue form plus issue
  config, `docs/.nojekyll`, and a committed `docs/favicon.svg` (release
  standard packaging).
- Private security advisory route in `SECURITY.md` (GitHub security
  advisories, email as fallback).

### Changed
- README sweep 2026-09: anchors refreshed (OMG SysML v2.0 publication,
  SysML-v2-Release 2026-08 train, Capella 7.1.0, INCOSE SE Handbook v5.0,
  SEBoK v2.14), CATIA Magic naming applied, Model Gallery prose counts
  fixed.
- CHANGELOG restructured to Keep-a-Changelog form; prior sweep history
  preserved verbatim below.
- Branch protection on `main`; About homepage set to the Pages URL and
  topics expanded.
- Soft-404 findings from the manual pass: one mild move, no dead entries.
  Manual curl sweep of 116 unique README URLs (2026-09-22): 107 HTTP 200; 7
  HTTP 403 already listed in .lycheeignore (DoD WAF, TriMech/Cloudflare,
  Wiley/INCOSE Online Library, ResearchGate, INCOSE.org); 1 transient GitHub
  429 on Package-Delivery-Drone blob (repo root 200 on recheck); 1 transient
  OMG UPDM 521 (recheck 200, correct UPDM 2.1.1 title). Soft-404: JPL State
  Analysis URL https://mds.jpl.nasa.gov/public/sa/ redirects to the JPL MDS
  overview page (still MDS-related; left in place). No entries pruned.

## 2026-09 - Spoke launch: awesome-archimate

- **Launched [awesome-archimate](https://github.com/jgsystemsconsulting/awesome-archimate)**
  (public) as an additional Live spoke: ArchiMate 3.x and 4, the Archi tool, EA
  modeling practice. Opened with 17 verified seed entries under the depth waiver.
- **FAMILY.md registry**: awesome-archimate flipped Planned -> Live, repo link added,
  scope text updated to "ArchiMate 3.x and 4, the Archi tool, EA modeling practice".
- **Hub README**: List family paragraph and mirror table updated for the Live
  awesome-archimate spoke (full Live census remains the mirror table).

## 2026-06: Enable CI link-checking

- **Activated the link-check + awesome-lint workflows** (previously untracked, pending a
  workflow-scope token): `link-check-pr.yml` gates PRs, `link-check-schedule.yml` runs a
  weekly link-rot report.
- **Added `.lycheeignore`** for URLs that are live in a browser but return 403 to automated
  checkers (DoD WAF, TriMech/Cloudflare, Wiley/INCOSE Online Library, ResearchGate).
  Verified live manually; re-checked each quarterly sweep.
- **Removed `jgs-magic-sysmlv2-mcp`**: the repo is private, so the link 404s publicly and
  failed the inclusion bar's "publicly accessible" rule (§2.5). Re-add when it ships
  public. Editorial neutrality preserved: the independent `cameo-mcp-bridge` and
  `jgs-magic-sysmlv1-mcp` entries remain side by side.

## 2026-06: Architecture frameworks + section orientation

- **New `### Architecture frameworks` sub-section**: the defence/enterprise frameworks
  SysML models are built against: OMG UAF (spec hub + program page + Cameo plugin docs),
  OMG UPDM, NATO NAF v4, US DoDAF 2.02, UK MODAF. 7 entries.
- **Orientation blurbs** added to the Magic Grid and Broader Context section intros so each
  reads as a short "what this is / where to start", per the type-organized structure
  (deliberately did **not** split the list into v1/v2/Magic Grid sections: version is
  already a tag on every entry, and splitting would scatter the cross-version resources).
- Link note: the official DoDAF page (dodcio.defense.gov) is live in a browser but returns
  403 to automated clients (DoD WAF). When CI link-checking is enabled, add it to the
  lychee exclude list rather than treating it as a dead link.

## 2026-06: Rebrand to Awesome MBSE + domain libraries

- **Rebranded** from "Awesome Magic Grid & SysML MBSE" to **Awesome MBSE**: broadened the
  positioning so the list reads as a full MBSE index with Magic Grid / Cameo as its
  standout-deep section, not its whole identity. Updated README title/intro, the
  competitive-landscape framing, CONTRIBUTING, LICENSE, NOTICE, and RELEASE-INFO.
  (Repo slug renamed to `awesome-mbse`; the old GitHub URL auto-redirects.)
- **New `### Domain & reusable libraries` sub-section**: import-into-your-model building
  blocks (vs. whole-system models): SysML v2 Standard Library and QUDT (moved here from
  tooling), plus 6 new verified libraries: SysML v2 AADL library, SYSMOD for SysML v2,
  elan8 domain libraries (61 `.sysml` robotics blocks), openCAESAR metrology vocabularies
  (ISO 80000), GfSE SAF Cameo profile, SCRE Cameo profiles, UAF-for-Papyrus.
- All new links independently curl-verified HTTP 200; all library files confirmed in-tree.
- Scope note: excluded pure web-of-things/upper ontologies (SOSA/SSN, BFO): kept the
  section to libraries a SysML/MBSE modeler actually imports.

## 2026-06: Methodology & learning expansion

- Added 21 verified entries (all links independently curl-checked HTTP 200).
- **New `### Methodology & method references` sub-section** under Broader Context: Estefan
  MBSE methodology survey, OMG MBSE Wiki directory, OOSEM, SYSMOD, Harmony aMBSE Deskbook,
  Arcadia (×2), FAS, JPL State Analysis, OPM (Dori), SpesML: the "how to model", free.
- **Specs & standards: +4**: OMG KerML, OMG Systems Modeling API & Services, OMG SysML
  v2.0, NASA-HDBK-1009 Systems Modeling Handbook.
- **Free learning: +5**: OMG/INCOSE SysML Tutorial, JHU/APL Modeling-with-SysML, MIT OCW
  16.842, NASA NESC Academy video catalog, Eclipse SysON tutorials. (First non-`paid`
  entries in Courses & learning paths.)
- **SysML v2 libraries: +2**: SysML v2 Standard Library, QUDT units vocabulary.
- Scope note: deliberately excluded upstream-of-MBSE ontologies (BFO/IOF) and niche arXiv
  papers: kept the list coherent as an MBSE/Magic Grid index, not a general ontology list.

## 2026-06: Corpus expansion

- Added 19 verified entries (all links 200, all model files confirmed present).
- **Cameo `.mdzip` corpus: 3 → 9**: added GfSE SAF Fire-Fighting Drone System, GTRI
  INGRID demo models, Open-MBEE MDK DocGen sample, Package Delivery Drone, EOSS satellite
  system, and a MOSA implementation. (Found via repo-tree enumeration, not code search,
  which under-indexes `.mdzip`.)
- **SysML v2 model gallery: +8**: robot vacuum cleaner, fusion-tea, yutaro sample
  project, sensmetry DETECT, DLR-FT STPA library, GfSE SAF-SysMLV2, Open-MBEE DesertKite
  (OOSEM), TU Ilmenau CMBSE.
- **Tooling: +5**: Gaphor, Modelio, openCAESAR/OML, py-capellambse, Open-MBEE Flexo-MMS.

## 2026-06: Initial release

- First full sweep and publication. 47 vetted entries.
- Multi-source scour: GitHub (models + tooling), web (methodology/tutorials/courses/
  books/communities), and known anchors (OMG/INCOSE/Eclipse).
- Corpus finding: openable Cameo `.mdzip` models on the open web are scarce (3 found);
  the Model Gallery is therefore led by the abundant SysML v2 textual (`.sysml`) corpus.
- Competitive finding: no pre-existing `awesome-cameo`/`awesome-mbse`/`awesome-magic-grid`
  list; the one active SysML awesome-list has zero MagicDraw/Magic Grid coverage.
