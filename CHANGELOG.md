# Changelog

Maintenance sweeps and notable changes. The "Last full sweep" badge in the README
tracks the most recent dated entry here.

## 2026-06 — Rebrand to Awesome MBSE + domain libraries

- **Rebranded** from "Awesome Magic Grid & SysML MBSE" to **Awesome MBSE** — broadened the
  positioning so the list reads as a full MBSE index with Magic Grid / Cameo as its
  standout-deep section, not its whole identity. Updated README title/intro, the
  competitive-landscape framing, CONTRIBUTING, LICENSE, NOTICE, and RELEASE-INFO.
  (Repo slug renamed to `awesome-mbse`; the old GitHub URL auto-redirects.)
- **New `### Domain & reusable libraries` sub-section** — import-into-your-model building
  blocks (vs. whole-system models): SysML v2 Standard Library and QUDT (moved here from
  tooling), plus 6 new verified libraries — SysML v2 AADL library, SYSMOD for SysML v2,
  elan8 domain libraries (61 `.sysml` robotics blocks), openCAESAR metrology vocabularies
  (ISO 80000), GfSE SAF Cameo profile, SCRE Cameo profiles, UAF-for-Papyrus.
- All new links independently curl-verified HTTP 200; all library files confirmed in-tree.
- Scope note: excluded pure web-of-things/upper ontologies (SOSA/SSN, BFO) — kept the
  section to libraries a SysML/MBSE modeler actually imports.

## 2026-06 — Methodology & learning expansion

- Added 21 verified entries (all links independently curl-checked HTTP 200).
- **New `### Methodology & method references` sub-section** under Broader Context: Estefan
  MBSE methodology survey, OMG MBSE Wiki directory, OOSEM, SYSMOD, Harmony aMBSE Deskbook,
  Arcadia (×2), FAS, JPL State Analysis, OPM (Dori), SpesML — the "how to model", free.
- **Specs & standards: +4** — OMG KerML, OMG Systems Modeling API & Services, OMG SysML
  v2.0, NASA-HDBK-1009 Systems Modeling Handbook.
- **Free learning: +5** — OMG/INCOSE SysML Tutorial, JHU/APL Modeling-with-SysML, MIT OCW
  16.842, NASA NESC Academy video catalog, Eclipse SysON tutorials. (First non-`paid`
  entries in Courses & learning paths.)
- **SysML v2 libraries: +2** — SysML v2 Standard Library, QUDT units vocabulary.
- Scope note: deliberately excluded upstream-of-MBSE ontologies (BFO/IOF) and niche arXiv
  papers — kept the list coherent as an MBSE/Magic Grid index, not a general ontology list.

## 2026-06 — Corpus expansion

- Added 19 verified entries (all links 200, all model files confirmed present).
- **Cameo `.mdzip` corpus: 3 → 9** — added GfSE SAF Fire-Fighting Drone System, GTRI
  INGRID demo models, Open-MBEE MDK DocGen sample, Package Delivery Drone, EOSS satellite
  system, and a MOSA implementation. (Found via repo-tree enumeration, not code search,
  which under-indexes `.mdzip`.)
- **SysML v2 model gallery: +8** — robot vacuum cleaner, fusion-tea, yutaro sample
  project, sensmetry DETECT, DLR-FT STPA library, GfSE SAF-SysMLV2, Open-MBEE DesertKite
  (OOSEM), TU Ilmenau CMBSE.
- **Tooling: +5** — Gaphor, Modelio, openCAESAR/OML, py-capellambse, Open-MBEE Flexo-MMS.

## 2026-06 — Initial release

- First full sweep and publication. 47 vetted entries.
- Multi-source scour: GitHub (models + tooling), web (methodology/tutorials/courses/
  books/communities), and known anchors (OMG/INCOSE/Eclipse).
- Corpus finding: openable Cameo `.mdzip` models on the open web are scarce (3 found);
  the Model Gallery is therefore led by the abundant SysML v2 textual (`.sysml`) corpus.
- Competitive finding: no pre-existing `awesome-cameo`/`awesome-mbse`/`awesome-magic-grid`
  list; the one active SysML awesome-list has zero MagicDraw/Magic Grid coverage.
