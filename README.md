# Awesome MBSE [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated, vetted, dated index of **Model-Based Systems Engineering** — SysML v1/v2,
> methods, tools, and openable models — with the deepest **Magic Grid / Cameo / CATIA
> Magic** coverage anywhere.

![Last full sweep: 2026-06](https://img.shields.io/badge/last%20full%20sweep-2026--06-brightgreen)

Built for the **practitioner hunting a real, openable model to learn from or copy**, and
for anyone who wants one trustworthy starting point for SysML/MBSE. Every link is
checked; dead links are pruned; each entry is dated and tagged. Coverage spans the whole
MBSE ecosystem — language, method, tooling, and reusable libraries — with the Magic Grid /
Cameo section as the standout-deep part no other list covers.

> **Maintained by [JG Systems Consulting Ltd.](https://github.com/jgsystemsconsulting), a
> commercial vendor of SysML/Cameo tooling.** JGS products are listed below by the same
> inclusion criteria as everything else, alongside competing alternatives. See
> [Editorial neutrality](CONTRIBUTING.md#7-editorial-neutrality).

## Contents

- [Magic Grid & Cameo / CATIA Magic](#magic-grid--cameo--catia-magic)
- [Model Gallery](#model-gallery)
- [Broader SysML / MBSE Context](#broader-sysml--mbse-context)
- [The competitive landscape](#the-competitive-landscape)
- [Contributing](#contributing)
- [License](#license)

## Magic Grid & Cameo / CATIA Magic

The flagship. Magic Grid is the SysML modeling method developed at No Magic (now
Dassault Systèmes) and applied in Cameo Systems Modeler / CATIA Magic — a grid of
problem/solution domains × structure/behaviour/requirements/parametrics that tells you
*what to model next*. **New here?** Start with the [MagicGrid Book of
Knowledge](#methodology--guides), then open a real model from the
[Model Gallery](#model-gallery). This is the deepest part of the list and the one no other
awesome-list covers.

### Methodology & guides

- [MagicGrid Book of Knowledge](https://discover.3ds.com/magicgrid-book-of-knowledge) - The definitive practitioner guide to the MagicGrid method, by Aleksandravičienė & Morkevičius `SysML-general` `MagicGrid` `Cameo` `book` (2021).
- [MBSE Grid: A Simplified SysML-Based Approach for Modeling Complex Systems](https://epubl.ktu.edu/object/elaba:31768092/31768092.pdf) - Open-access PDF of the foundational paper introducing the grid method that became MagicGrid `SysML-general` `MagicGrid` `paper` (2017).
- [System Verification and Validation Using the MagicGrid Framework](https://incose.onlinelibrary.wiley.com/doi/full/10.1002/inst.12429) - INCOSE INSIGHT article extending MagicGrid to cover V&V workflows `SysML-general` `MagicGrid` `paper` (2023).
- [Systems Architecture Meta-Model for the MagicGrid Framework](https://incose.onlinelibrary.wiley.com/doi/abs/10.1002/iis2.13284) - Paper formalizing MagicGrid's underlying architecture meta-model `SysML-general` `MagicGrid` `paper` (2024).

### Tutorials

- [Cameo Systems Modeler — Product Documentation](https://docs.nomagic.com/spaces/CSM2022xR1/pages/106636564/Cameo+Systems+Modeler+Home+Page) - Official vendor docs: projects, SysML diagramming, requirements, collaboration `SysMLv1` `Cameo` `tutorial` (2022).
- [Cameo Simulation Toolkit — Tutorial](https://docs.nomagic.com/spaces/CST2024x/pages/136730007/Tutorial) - Official step-by-step tutorial for executing and simulating SysML models in Cameo `SysMLv1` `Cameo` `tutorial` (2024).
- [Colorado State University — Cameo Tutorial Script](https://www.engr.colostate.edu/se/wp-content/uploads/2026/01/CAMEO-TUTORIAL-SCRIPT.pdf) - University-authored written walkthrough: new project, Systems Engineer role, SysML setup `SysMLv1` `Cameo` `tutorial` (2026).
- [CameoMagic — Free MBSE & SysML Resources](https://cameomagic.com/free-resources/) - Practitioner blog and YouTube with hands-on Cameo tutorials (BDD, IBD, parametrics, state machines) `SysML-general` `Cameo` `tutorial` (2024).
- [Webel MBSE/SysML Video Tutorials](https://vimeopro.com/webel/mbse) - Large library of Cameo Simulation Toolkit and SysML v1 mini-tutorials `SysMLv1` `Cameo` `video` (2023).

### Courses & learning paths

- [SysML Intensive with MBSE Using Cameo Systems Modeler](https://www.3ds.com/edu/catia-magic-training/sysml-intensive-mbse-using-cameo-systems-modeler) - Official Dassault 5-day SysML lecture plus 2-day MBSE lab using Cameo `SysML-general` `Cameo` `course` `paid` (2024).
- [Intro to MBSE and SysML with Cameo (TriMech)](https://enterprise.trimech.com/training-course/intro-to-mbse-and-sysml-with-cameo/) - Beginner-friendly instructor-led Cameo and MBSE course with lecture, demo, and workshops `SysMLv1` `Cameo` `course` `paid` (2024).
- [Intro to MBSE and SysML v2 with Cameo (TriMech)](https://trimech.com/intro-to-mbse-and-sysml-v2-training-course/) - SysML v2 introductory course for newcomers, taught using Cameo `SysMLv2` `Cameo` `course` `paid` (2024).
- [Transitioning Models to SysML v2 with MBSE (Caltech CTME)](https://ctme.caltech.edu/transitioning-models-to-sysml-v2-with-mbse.html) - 3-day Caltech course on moving SysML v1 Cameo models to SysML v2 `SysMLv2` `Cameo` `course` `paid` (2024).
- [SysML v2 Workshop on Cameo / CATIA Magic (Webel)](https://webel.com.au/node/4399) - 5-day Webel SysML v2 workshop run on Cameo/CATIA Magic with a Balls & Boxes sample `SysMLv2` `Cameo` `course` `paid` (2024).
- [OMG/INCOSE SysML Tutorial (Friedenthal et al.)](https://www.omg.org/sysml/INCOSE-OMGSysML-Tutorial-Final-090901.pdf) - The canonical 175-slide SysML tutorial by the spec authors; free, foundational `SysML-general` `course` (2009).
- [Modeling with SysML Tutorial (Friedenthal & Oster, JHU/APL)](https://www.jhuapl.edu/sites/default/files/2023-03/ModelingwithSysMLTutorial.pdf) - INCOSE tutorial deck on building SysML models, freely hosted by JHU/APL `SysML-general` `course` (2023).
- [MIT OCW 16.842 — Fundamentals of Systems Engineering](https://ocw.mit.edu/courses/16-842-fundamentals-of-systems-engineering-fall-2015/) - de Weck's open graduate SE course; Session 3 covers SysML/OPM. Free video and notes `SysML-general` `course` (2015).
- [NASA NESC Academy — Systems Engineering Catalog](https://nescacademy.nasa.gov/catalogs/systemseng) - NASA's public on-demand video library with multiple freely viewable MBSE lectures `SysML-general` `video` (2024).
- [Eclipse SysON — Tutorials (YouTube)](https://www.youtube.com/@EclipseSysON) - Free tutorial and demo videos for the open-source web-based SysML v2 modeler `SysMLv2` `SysON` `video` (2025).

### Books & papers

- [Analysis of the Mainstream MBSE Methodologies from the Modeling Practice View](https://www.researchgate.net/publication/366507453_Analysis_of_the_Mainstream_MBSE_Methodologies_from_the_Modeling_Practice_View) - Comparative paper evaluating MBSE methodologies including MagicGrid and OOSEM `SysML-general` `MagicGrid` `paper` (2022).

### Example models

Real, openable models that use Cameo / MagicDraw. Cameo's `.mdzip` is a proprietary
binary, so the open-web Cameo corpus is small — see the [Model Gallery](#model-gallery)
for the much larger SysML v2 textual corpus.

<a id="mbse4u-the-sysml-v2-book-examples"></a>
- [MBSE4U — The SysML v2 Book Examples](https://github.com/MBSE4U/the-sysmlv2-book-examples) - Companion Cameo `.mdzip` models (incl. a Drone) for Weilkiens & Muggeo's SysML v2 book `SysMLv2` `Cameo` `has-model` `paper` (2026).
<a id="verse-opensut"></a>
- [GaloisInc — VERSE-OpenSUT](https://github.com/GaloisInc/VERSE-OpenSUT/tree/main/models/SysMLv1) - Open System-Under-Test reference with Cameo SysML v1 `.mdzip` models (MPS, system overview) `SysMLv1` `Cameo` `has-model` `paper` (2025).
<a id="multiagent-warehouse"></a>
- [Multiagent Warehouse (MaaS)](https://github.com/autarchprinceps/Multiagent-Warehouse/blob/master/Documentation/maas-warehouse.mdzip) - A MagicDraw `.mdzip` model of a multi-agent warehouse system `SysMLv1` `CATIA-Magic` `has-model` `paper` (2017).
<a id="gfse-saf-ffds-cameo-model"></a>
- [GfSE SAF — Fire-Fighting Drone System (Cameo)](https://github.com/GfSE/SAF-Cameo-Profile/tree/main/SAF_Plugin/samples/SAF) - Openable Cameo `.mdzip` reference model of a fire-fighting drone system, built with the System Architecture Framework `SysMLv1` `Cameo` `has-model` `tool` (2026).
<a id="gtri-ingrid-rapid-modeling"></a>
- [GTRI INGRID Rapid-Modeling Demo Models](https://github.com/gtri/rapid-modeling-tools/tree/master/ingrid-quick-start) - Cameo/MagicDraw `.mdzip` demo models shipped with GTRI's INGRID pattern-based rapid-modeling tooling `SysMLv1` `CATIA-Magic` `has-model` `tool` (2023).
<a id="open-mbee-mdk-docgen-sample"></a>
- [Open-MBEE MDK DocGen Sample Model](https://github.com/Open-MBEE/exec-cameo-mdk/tree/develop/src/main/dist/samples/MDK) - Cameo `.mdzip` sample model demonstrating the Model Development Kit's DocGen document generation `SysMLv1` `Cameo` `has-model` `tool` (2024).
<a id="package-delivery-drone-cameo"></a>
- [Package Delivery Drone (Cameo)](https://github.com/jmgogo/Package-Delivery-Drone/blob/main/model/Package%20Delivery%20Drone.mdzip) - Self-contained Cameo `.mdzip` SysML model of a package-delivery drone system architecture (Apache-2.0) `SysMLv1` `Cameo` `has-model` `paper` (2023).
<a id="eoss-cameo-model"></a>
- [EOSS — Earth Observation Satellite System (Cameo)](https://github.com/seakers/cameo-LLM-plugin/tree/main/cameo/examples) - Cameo `.mdzip` model of an Earth-observation satellite system from the SEAK Lab `SysMLv1` `Cameo` `has-model` `paper` (2023).
<a id="enola-mosa-cameo-model"></a>
- [MOSA Implementation (CUSA 2026, Cameo)](https://github.com/EnolaTechnologies/cusa26) - Cameo `.mdzip` model of a Modular Open Systems Approach implementation, from a CATIA User Symposium talk `SysMLv1` `Cameo` `has-model` `paper` (2026).

### Tools, plugins & automation

Listed by merit, JGS products alongside alternatives (see
[Editorial neutrality](CONTRIBUTING.md#7-editorial-neutrality)).

- [Open-MBEE MBSEPlugin](https://github.com/Open-MBEE/MBSEPlugin) - Open-source MagicDraw/Cameo plugin (DocGen document generation, Cameo Simulation Toolkit integration) `SysMLv1` `Cameo` `plugin` (2024).
- [cameo-mcp-bridge](https://github.com/ajhcs/cameo-mcp-bridge) - Independent MIT-licensed MCP server bridging AI assistants to Cameo/CATIA Magic for SysML/UML create and query `SysMLv1` `Cameo` `mcp` (2026).
- [jgs-magic-sysmlv1-mcp](https://github.com/jgsystemsconsulting/jgs-magic-sysmlv1-mcp) - JG Systems SysML v1 MCP bridge (~115 tools) over a local link to CATIA Magic; FREE/PRO/ENTERPRISE `SysMLv1` `CATIA-Magic` `mcp` `paid` (2026).
- [jgs-magic-sysmlv1-read-skills](https://github.com/jgsystemsconsulting/jgs-magic-sysmlv1-read-skills) - Free read-only SysML v1 analysis skills for CATIA Magic (navigate, inspect, audit, report) `SysMLv1` `CATIA-Magic` `plugin` (2026).

### Communities & blogs

- [MBSE4U (Tim Weilkiens)](https://mbse4u.com/) - Long-running practitioner blog and bookshop covering MBSE, SysML v1/v2, SYSMOD, FAS, and VAMOS `SysML-general` `blog` (2025).
- [CameoMagic](https://cameomagic.com/) - Practitioner site focused on Cameo/MBSE tutorials, training, and certification prep `SysML-general` `Cameo` `blog` (2024).

## Model Gallery

Openable models, fast path. The Cameo `.mdzip` corpus on the open web is small (3 above),
so this gallery is dominated by **SysML v2 textual (`.sysml`) models** — abundant,
high-quality, and openable in any SysML v2 tool (SysIDE, SysON, the Pilot
Implementation). Cameo entries link back to [Example models](#example-models).

| Model | Where | Tags |
|-------|-------|------|
| [MBSE4U SysML v2 Book Examples](#mbse4u-the-sysml-v2-book-examples) | Magic Grid › Example models | `Cameo` `has-model` `(2026)` |
| [VERSE-OpenSUT](#verse-opensut) | Magic Grid › Example models | `Cameo` `has-model` `(2025)` |
| [Multiagent Warehouse](#multiagent-warehouse) | Magic Grid › Example models | `CATIA-Magic` `has-model` `(2017)` |
| [GfSE SAF Fire-Fighting Drone (Cameo)](#gfse-saf-ffds-cameo-model) | Magic Grid › Example models | `Cameo` `has-model` `(2026)` |
| [GTRI INGRID Demo Models](#gtri-ingrid-rapid-modeling) | Magic Grid › Example models | `CATIA-Magic` `has-model` `(2023)` |
| [Open-MBEE MDK DocGen Sample](#open-mbee-mdk-docgen-sample) | Magic Grid › Example models | `Cameo` `has-model` `(2024)` |
| [Package Delivery Drone (Cameo)](#package-delivery-drone-cameo) | Magic Grid › Example models | `Cameo` `has-model` `(2023)` |
| [EOSS Satellite System (Cameo)](#eoss-cameo-model) | Magic Grid › Example models | `Cameo` `has-model` `(2023)` |
| [MOSA Implementation (Cameo)](#enola-mosa-cameo-model) | Magic Grid › Example models | `Cameo` `has-model` `(2026)` |
| [OMG SysML v2 Release examples](https://github.com/Systems-Modeling/SysML-v2-Release/tree/master/sysml/src/examples) | 300+ official `.sysml` example & training models | `SysMLv2` `has-model` `(2026)` |
| [GfSE SysML v2 Models](https://github.com/GfSE/SysML-v2-Models) | Curated, CI-validated collection (Drone, HVAC, Vehicle…) | `SysMLv2` `has-model` `(2025)` |
| [Airbus Apollo-11 SysML v2](https://github.com/airbus/apollo-11-sysml-v2) | Apollo 11 reference model, full traceability | `SysMLv2` `has-model` `(2026)` |
| [jhaws1982 OOSEM Reference](https://github.com/jhaws1982/sysmlv2-mbse-reference) | OOSEM reference model in SysML v2 | `SysMLv2` `has-model` `(2026)` |
| [sensmetry Advent of SysML v2](https://github.com/sensmetry/advent-of-sysml-v2) | 44 bite-sized SysML v2 example models | `SysMLv2` `has-model` `(2026)` |
| [SysML v2 Astronomy Reference](https://github.com/elan8/sysml-v2-astronomy-reference) | A worked astronomy-domain SysML v2 model | `SysMLv2` `has-model` `(2026)` |
| [Don't Panic Batmobile](https://github.com/MBSE4U/dont-panic-batmobile) | Companion model for Weilkiens & Muggeo's "Don't Panic" | `SysMLv2` `has-model` `(2025)` |
| [Robot Vacuum Cleaner (SysML v2)](https://github.com/elan8/sysml-robot-vacuum-cleaner) | 21-file autonomous-robot model: architecture, behavior, firmware, analysis | `SysMLv2` `has-model` `(2026)` |
| [fusion-tea](https://github.com/1cFE/fusion-tea) | Fusion-energy model + units/costing libraries (36 `.sysml` files) | `SysMLv2` `has-model` `(2026)` |
| [yutaro-ito Sample SysML v2 Project](https://github.com/yutaro-ito/sample-sysml-v2-project) | End-to-end method walkthrough: context→requirements→logical architecture | `SysMLv2` `has-model` `(2022)` |
| [sensmetry DETECT](https://github.com/sensmetry/detect) | Hazard-analysis (DEM&S) tool modeled in SysML v2 | `SysMLv2` `has-model` `(2026)` |
| [DLR-FT STPA Library](https://github.com/DLR-FT/SysMLv2LibrarySTPA) | DLR System-Theoretic Process Analysis safety library + worked example | `SysMLv2` `has-model` `(2026)` |
| [GfSE SAF-SysMLV2](https://github.com/GfSE/SAF-SysMLV2) | System Architecture Framework expressed in SysML v2 (33 files) | `SysMLv2` `has-model` `(2026)` |
| [Open-MBEE DesertKite (OOSEM)](https://github.com/Open-MBEE/DesertKite.sysml) | Unusual real-world OOSEM domain model (archaeological desert kites) | `SysMLv2` `has-model` `(2025)` |
| [TU Ilmenau CMBSE](https://github.com/ziruili-tu-ilmenau/CMBSE) | Collaborative-MBSE research model: force-measurement / load-cell system | `SysMLv2` `has-model` `(2025)` |

## Broader SysML / MBSE Context

Curated, not exhaustive — the wider ecosystem any MBSE practitioner runs into: the
**language** (SysML v1, the stable incumbent; SysML v2, the textual successor now in
release), the **methods** to apply it, the **architecture frameworks** to structure it,
the **tools** to run it, and **reusable libraries** to build from.

### Specifications & standards

- [OMG SysML Specification](https://www.omg.org/spec/SysML/) - Canonical OMG SysML spec page; now defaults to v2.0 (2025), with v1.7 the final v1 release `SysML-general` `spec` (2025).
- [OMG SysML v1.7](https://www.omg.org/spec/SysML/1.7/) - The final SysML v1 release; the general-purpose v1 MBSE modeling language `SysMLv1` `spec` (2024).
- [Systems-Modeling/SysML-v2-Release](https://github.com/Systems-Modeling/SysML-v2-Release) - "Start here" for SysML v2: the latest incremental release with spec, training, examples, libraries `SysMLv2` `spec` (2026).
- [INCOSE Systems Engineering Handbook](https://www.incose.org/resources-publications/technical-publications/se-handbook/) - The practitioner reference for SE life-cycle processes, aligned to ISO/IEC/IEEE 15288 `SysML-general` `standard` `paid` (2023).
- [OMG KerML Specification](https://www.omg.org/spec/KerML/) - The Kernel Modeling Language spec — the formal semantic foundation underlying SysML v2 `SysMLv2` `spec` (2025).
- [OMG Systems Modeling API & Services](https://www.omg.org/spec/SystemsModelingAPI/) - OMG spec defining platform-independent REST/SOAP/Java APIs for KerML and SysML v2 models `SysMLv2` `spec` (2025).
- [OMG SysML v2.0 Specification](https://www.omg.org/spec/SysML/2.0/) - The dedicated landing page for the SysML v2.0 language release `SysMLv2` `spec` (2025).
- [NASA Systems Modeling Handbook (NASA-HDBK-1009)](https://standards.nasa.gov/standard/NASA/NASA-HDBK-1009) - Official NASA tool-agnostic guidance on building and using system models `SysML-general` `standard` (2022).

### Methodology & method references

Cross-tool MBSE methods — the "how to model", not the language itself.

- [Survey of MBSE Methodologies (Estefan, INCOSE/OMG)](https://www.omg.org/sysml/MBSE_Methodology_Survey_RevB.pdf) - The standard comparative reference: OOSEM, Harmony-SE, RUP-SE, Vitech, JPL State Analysis, OPM side by side `SysML-general` `paper` (2008).
- [OMG MBSE Wiki — Methodology Directory](https://www.omgwiki.org/MBSE/doku.php?id=mbse:methodology) - Master index of MBSE methodologies (OOSEM, SYSMOD, Harmony, Arcadia, and more) `SysML-general` `blog` (2024).
- [OOSEM (OMG MBSE Wiki)](https://www.omgwiki.org/MBSE/doku.php?id=mbse:incoseoosem) - Vendor-neutral reference for the Object-Oriented Systems Engineering Method `SysML-general` `blog` (2023).
- [SYSMOD (Tim Weilkiens)](https://mbse4u.com/sysmod/) - Canonical page for the SYSMOD method toolbox: roles, activities, products, and SysML integration `SysML-general` `blog` (2022).
- [Harmony aMBSE Deskbook (IBM)](https://jazz.net/library-content/wp-content/uploads/2020/11/Harmony-aMBSE-Deskbook-Version-1.pdf) - The full IBM Harmony agile-MBSE method deskbook, freely available `SysMLv1` `Rhapsody` `book` (2020).
- [Arcadia Method (official)](https://mbse-capella.org/arcadia.html) - Canonical page for the Arcadia method (AFNOR Z67-140) implemented by Eclipse Capella `SysML-general` `blog` (2024).
- [An Introduction to Arcadia (Voirin)](https://download.eclipse.org/capella/publis/An_Introduction_to_Arcadia_20150115.pdf) - Open primer on the Arcadia method's perspectives and engineering workflow `SysML-general` `paper` (2015).
- [FAS Method](https://fas-method.org/) - Official site for Functional Architectures for Systems (Lamm & Weilkiens), with open publications and plugins `SysML-general` `blog` (2024).
- [JPL State Analysis](https://mds.jpl.nasa.gov/public/sa/) - NASA/JPL's primary state-based MBSE method for control-system and mission modeling `SysML-general` `blog` (2023).
- [Object-Process Methodology (Dori, Technion)](https://esml.technion.ac.il/opm/overview/) - Authoritative overview of OPM (ISO 19450), a self-contained graphical-plus-textual modeling method `SysML-general` `blog` (2022).
- [SpesML — Open Methodology Docs (TUM/fortiss)](https://spesml.github.io/) - Full open documentation of the SPES-based SpesML method: viewpoints, concepts, case studies, Cameo plugin `SysML-general` `Cameo` `blog` (2024).

### Architecture frameworks

The defence/enterprise architecture frameworks SysML models get built against. **UAF** is
the modern OMG framework — it supersedes UPDM/DoDAF/MODAF and runs natively in Cameo; start
there unless a specific programme mandates DoDAF or NAF.

- [OMG UAF Specification](https://www.omg.org/spec/UAF) - The Unified Architecture Framework spec hub: Domain Metamodel (DMM) and the UAFML profile Cameo implements `SysML-general` `spec` (2022).
- [OMG UAF Program Page](https://www.omg.org/uaf/) - OMG's UAF overview and community page: concepts, videos, certification, and adoption guidance `SysML-general` `blog` (2024).
- [UAF Plugin Documentation (Cameo/No Magic)](https://docs.nomagic.com/spaces/UAFP190SP3/pages/47112606/UAF+Plugin+Documentation) - Official Dassault/No Magic docs for the UAF plugin in Cameo/MagicDraw, with sample models `SysMLv1` `Cameo` `tutorial` (2024).
- [OMG UPDM Specification](https://www.omg.org/spec/UPDM/) - The Unified Profile for DoDAF/MODAF — UAF's predecessor profile, still referenced by legacy programmes `SysML-general` `spec` (2013).
- [NATO Architecture Framework v4](https://www.nato.int/en/about-us/organization/nato-structure/digital-policy-committee-dpc/nato-architecture-framework-version) - Official NATO landing page for NAF v4.1, the current NATO architecture framework `SysML-general` `standard` (2020).
- [DoD Architecture Framework (DoDAF 2.02)](https://dodcio.defense.gov/library/dod-architecture-framework/) - Official US DoD CIO page for DoDAF 2.02, the US defence architecture framework `SysML-general` `standard` (2010).
- [MOD Architecture Framework (MODAF)](https://www.gov.uk/guidance/mod-architecture-framework) - Official UK gov.uk MODAF page; now withdrawn in favour of NAF/UAF but still widely referenced `SysML-general` `standard` (2016).

### SysML v2 tooling

- [SysML v2 Pilot Implementation](https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation) - OMG reference pilot: Xtext editors, PlantUML visualization, and a Jupyter kernel for SysML v2 `SysMLv2` `tool` (2026).
- [Eclipse SysON](https://github.com/eclipse-syson/syson) - Open-source web-based SysML v2 modeler (graphical, form, tabular editors), by Obeo and CEA List `SysMLv2` `SysON` `tool` (2026).
- [SysIDE Editor (Sensmetry)](https://github.com/sensmetry/sysml-2ls) - VS Code extension for SysML v2: highlighting, autocompletion, and formatting `SysMLv2` `other-tool` `plugin` (2025).
- [Sysand (Sensmetry)](https://github.com/sensmetry/sysand) - Open-source package manager for SysML v2 and KerML model libraries `SysMLv2` `other-tool` `tool` (2026).

### Domain & reusable libraries

Building-block libraries and profiles you **import** into your own model — units, domain
components, frameworks, and standard profiles — rather than whole-system reference models.

- [SysML v2 Standard Library](https://github.com/Systems-Modeling/SysML-v2-Release/tree/master/sysml.library) - The normative KerML/SysML v2 standard libraries: ISQ quantities, SI units, geometry, analysis, domain libs `SysMLv2` `tool` (2026).
- [SysML v2 Library for AADL](https://github.com/Systems-Modeling/SysML-v2-AADL-Release) - Official SysML v2 rendering of AADL (base types, property sets, component categories) for avionics/embedded `SysMLv2` `tool` (2026).
- [SYSMOD for SysML v2](https://github.com/MBSE4U/sysmod-sysmlv2) - Tim Weilkiens' SYSMOD method as an importable SysML v2 language-extension library, with examples `SysMLv2` `tool` (2026).
- [elan8 SysML v2 Domain Libraries](https://github.com/elan8/sysml-domain-libraries) - Importable domain building-block libraries (robotics: actuation, control, autonomy, operations) `SysMLv2` `has-model` `tool` (2026).
- [QUDT — Quantities, Units, Dimensions & Types](https://github.com/qudt/qudt-public-repo) - RDF/OWL vocabulary of quantities and units widely reused for units handling in MBSE models `SysML-general` `other-tool` `tool` (2024).
- [openCAESAR Metrology Vocabularies](https://github.com/opencaesar/metrology-vocabularies) - ISO/IEC 80000 quantities-and-units plus JCGM VIM4 metrology, as importable OML libraries `SysML-general` `other-tool` `tool` (2026).
- [GfSE SAF Cameo Profile](https://github.com/GfSE/SAF-Cameo-Profile) - System Architecture Framework profile, UAF-tracing profile, and library packaged for Cameo `SysMLv1` `Cameo` `plugin` (2026).
- [SCRE Cameo Profiles](https://github.com/tsherburne/scre-profile) - Secure Cyber Resilient Engineering profiles for Cameo, built on RAAML and SACM (safety/assurance) `SysMLv1` `Cameo` `plugin` (2025).
- [UAF for Papyrus (Adocus)](https://github.com/Adocus/UAF-for-Papyrus) - OMG Unified Architecture Framework profile plus a UAF Measurement Library for Eclipse Papyrus `SysMLv1` `Papyrus` `plugin` (2022).

### Other MBSE tools

- [Cameo Systems Modeler / CATIA Magic](https://www.3ds.com/products/catia/no-magic/cameo-systems-modeler) - Commercial cross-platform MBSE environment: SysML, UML, DoDAF/MODAF, requirements traceability `SysMLv1` `Cameo` `tool` `paid` (2024).
- [Eclipse Papyrus](https://eclipse.dev/papyrus/) - Industrial-grade open-source Eclipse modeling tool for UML with full SysML support `SysMLv1` `Papyrus` `tool` (2024).
- [IBM Engineering Systems Design Rhapsody](https://www.ibm.com/products/engineering-rhapsody) - Commercial MBSE tool: SysML plus the Harmony method, UAF/DoDAF, AUTOSAR, FMI co-simulation `SysMLv1` `Rhapsody` `tool` `paid` (2024).
- [Eclipse Capella](https://mbse-capella.org/) - Open-source MBSE tool implementing the Arcadia method (adjacent to SysML) `SysML-general` `other-tool` `tool` (2024).
- [Gaphor](https://github.com/gaphor/gaphor) - Lightweight open-source Python UML/SysML/RAAML modeler with a clean, readable OMG-standard metamodel `SysML-general` `other-tool` `tool` (2026).
- [Modelio](https://github.com/ModelioOpenSource/Modelio) - Open-source (GPL-3.0) enterprise modeling environment with a full SysML v1 diagram suite incl. parametrics `SysMLv1` `other-tool` `tool` (2024).
- [openCAESAR / OML](https://github.com/opencaesar/oml) - JPL-originated ontology-based modeling language and OWL toolchain for traceable MBSE, with worked examples `SysML-general` `other-tool` `tool` (2025).
- [py-capellambse](https://github.com/DSD-DBS/py-capellambse) - Headless Python library to load, traverse, diff, and generate from Capella/Arcadia models — "models as data" `SysML-general` `other-tool` `tool` (2026).

### APIs & automation

- [SysML v2 API Services](https://github.com/Systems-Modeling/SysML-v2-API-Services) - Proof-of-concept REST implementation of the OMG Systems Modeling API & Services spec `SysMLv2` `tool` (2026).
- [SysML v2 API Python Client](https://github.com/Systems-Modeling/SysML-v2-API-Python-Client) - Official Python client for the SysML v2 Systems Modeling API & Services `SysMLv2` `tool` (2021).
- [SysML v2 API Cookbook](https://github.com/Systems-Modeling/SysML-v2-API-Cookbook) - Recipes and worked examples for using the SysML v2 API `SysMLv2` `tool` (2025).
- [Open-MBEE Flexo-MMS for SysML v2](https://github.com/Open-MBEE/flexo-mms-sysmlv2) - Git+RDF-backed Model Management System implementing the OMG SysML v2 REST/HTTP API ("Git for models") `SysMLv2` `tool` (2026).

## The competitive landscape

Why this list exists, with evidence (gathered 2026-06-23). Existing SysML/SE awesome-lists
are either abandoned, narrow, or carry no Cameo / Magic Grid coverage at all:

| List | Stars | Last update | MBSE coverage |
|------|-------|-------------|---------------|
| [mycr0ft/awesome-sysml](https://github.com/mycr0ft/awesome-sysml) | ~2 | 2026-06 (active) | Narrow: SysML v2 textual tooling only; ~3 Cameo mentions, **0 MagicDraw / Magic Grid**, no methods/libraries |
| [kktse/awesome-systems-engineering](https://github.com/kktse/awesome-systems-engineering) | ~11 | 2021 (abandoned) | Broad SE links, **no MBSE depth**, stale |
| [rolling-robot/awesome-systems-engineering](https://github.com/rolling-robot/awesome-systems-engineering) | ~1 | 2024 (stagnant) | **None** |

No actively-maintained `awesome-mbse` with this breadth existed before this list. The
differentiator is **scope** — SysML v1/v2 + methods + tooling + reusable libraries +
openable models, with **Magic Grid / Cameo** depth no other list has — plus freshness.

## Contributing

Contributions welcome — see [CONTRIBUTING.md](CONTRIBUTING.md) for the inclusion bar,
entry format, and tag vocabulary. Suggest a resource via the
[issue form](../../issues/new/choose) or open a pull request.

## Support & security

Questions or a problem with a linked resource? Open an
[issue](../../issues/new/choose). To report a malicious or compromised link privately,
email **support@jgsystemsconsulting.com** — see [SECURITY.md](SECURITY.md).

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the maintainers have waived all copyright and related
or neighboring rights to this work. See [LICENSE](LICENSE).
