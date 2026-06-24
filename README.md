# Awesome MBSE [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated, vetted, dated index of **Model-Based Systems Engineering** — SysML v1/v2,
> methods, tools, and openable models — with the deepest **Magic Grid / Cameo / CATIA
> Magic** coverage anywhere.

![Last full sweep: 2026-06](https://img.shields.io/badge/last%20full%20sweep-2026--06-brightgreen)

Built for the **practitioner hunting a real, openable model to learn from or copy**, and
for anyone who wants one trustworthy starting point for SysML/MBSE. Every link is
checked; dead links are pruned; each entry is dated and tagged. Coverage spans the whole
MBSE ecosystem — language, method, tooling, and reusable libraries — organised **by
modelling language** so you can go straight to what you work in.

> **Maintained by [JG Systems Consulting Ltd.](https://github.com/jgsystemsconsulting), a
> commercial vendor of SysML/Cameo tooling.** JGS products are listed below by the same
> inclusion criteria as everything else, alongside competing alternatives. See
> [Editorial neutrality](CONTRIBUTING.md#7-editorial-neutrality).

> **This README is generated** from [`data/entries.yaml`](data/entries.yaml) +
> [`data/tags.yaml`](data/tags.yaml) by [`scripts/generate.py`](scripts/generate.py).
> Don't edit it directly — edit the data and regenerate (see Contributing below).

**Choosing a notation:**

- **Run Cameo / a programme today** → SysML v1 · Magic Grid.
- **Greenfield, text-friendly, tool-flexible** → SysML v2.
- **Defence / enterprise architecture** → UAF & architecture frameworks.
- **Eclipse / non-SysML world** → Adjacent & non-SysML notations.
- **Just want an openable model** → Find it your way (linked at the end of this list).

## Contents

<!-- AUTOGEN:START section=contents -->
- [SysML v1](#sysml-v1)
- [SysML v2](#sysml-v2)
- [UAF & architecture frameworks](#uaf--architecture-frameworks)
- [Adjacent & non-SysML notations](#adjacent--non-sysml-notations)
- [Cross-cutting (language-general)](#cross-cutting-language-general)
- [Find it your way](#find-it-your-way)
- [The competitive landscape](#the-competitive-landscape)
- [Contributing](#contributing)
- [Support & security](#support--security)
<!-- AUTOGEN:END section=contents -->

## SysML v1

Use this when you already model in Cameo / CATIA Magic, or your programme mandates SysML
v1. It is the stable incumbent with the deepest tool support — and the **Magic Grid /
Cameo** coverage below is the standout-deep part of this list that no other awesome-list
has. **New here?** Start with the MagicGrid Book of Knowledge, then open a real model.

<!-- AUTOGEN:START section=sysml-v1 -->
### Magic Grid & Cameo / CATIA Magic

#### Methodology & guides

- [Systems Architecture Meta-Model for the MagicGrid Framework](https://incose.onlinelibrary.wiley.com/doi/abs/10.1002/iis2.13284) - Paper formalizing MagicGrid's underlying architecture meta-model `SysML-general` `MagicGrid` `paper` (2024).
- [System Verification and Validation Using the MagicGrid Framework](https://incose.onlinelibrary.wiley.com/doi/full/10.1002/inst.12429) - INCOSE INSIGHT article extending MagicGrid to cover V&V workflows `SysML-general` `MagicGrid` `paper` (2023).
- [MagicGrid Book of Knowledge](https://discover.3ds.com/magicgrid-book-of-knowledge) - The definitive practitioner guide to the MagicGrid method, by Aleksandravičienė & Morkevičius `SysML-general` `MagicGrid` `Cameo` `book` (2021).
- [MBSE Grid: A Simplified SysML-Based Approach for Modeling Complex Systems](https://epubl.ktu.edu/object/elaba:31768092/31768092.pdf) - Open-access PDF of the foundational paper introducing the grid method that became MagicGrid `SysML-general` `MagicGrid` `paper` (2017).

#### Tutorials

- [Colorado State University — Cameo Tutorial Script](https://www.engr.colostate.edu/se/wp-content/uploads/2026/01/CAMEO-TUTORIAL-SCRIPT.pdf) - University-authored written walkthrough: new project, Systems Engineer role, SysML setup `SysMLv1` `Cameo` `tutorial` (2026).
- [Cameo Simulation Toolkit — Tutorial](https://docs.nomagic.com/spaces/CST2024x/pages/136730007/Tutorial) - Official step-by-step tutorial for executing and simulating SysML models in Cameo `SysMLv1` `Cameo` `tutorial` (2024).
- [CameoMagic — Free MBSE & SysML Resources](https://cameomagic.com/free-resources/) - Practitioner blog and YouTube with hands-on Cameo tutorials \(BDD, IBD, parametrics, state machines\) `SysML-general` `Cameo` `tutorial` (2024).
- [Webel MBSE/SysML Video Tutorials](https://vimeopro.com/webel/mbse) - Large library of Cameo Simulation Toolkit and SysML v1 mini-tutorials `SysMLv1` `Cameo` `video` (2023).
- [Cameo Systems Modeler — Product Documentation](https://docs.nomagic.com/spaces/CSM2022xR1/pages/106636564/Cameo+Systems+Modeler+Home+Page) - Official vendor docs: projects, SysML diagramming, requirements, collaboration `SysMLv1` `Cameo` `tutorial` (2022).

#### Courses & learning paths

- [Intro to MBSE and SysML with Cameo \(TriMech\)](https://enterprise.trimech.com/training-course/intro-to-mbse-and-sysml-with-cameo/) - Beginner-friendly instructor-led Cameo and MBSE course with lecture, demo, and workshops `SysMLv1` `Cameo` `course` `paid` (2024).
- [SysML Intensive with MBSE Using Cameo Systems Modeler](https://www.3ds.com/edu/catia-magic-training/sysml-intensive-mbse-using-cameo-systems-modeler) - Official Dassault 5-day SysML lecture plus 2-day MBSE lab using Cameo `SysML-general` `Cameo` `course` `paid` (2024).

#### Books & papers

- [Analysis of the Mainstream MBSE Methodologies from the Modeling Practice View](https://www.researchgate.net/publication/366507453_Analysis_of_the_Mainstream_MBSE_Methodologies_from_the_Modeling_Practice_View) - Comparative paper evaluating MBSE methodologies including MagicGrid and OOSEM `SysML-general` `MagicGrid` `paper` (2022).

#### Example models

- [GfSE SAF — Fire-Fighting Drone System \(Cameo\)](https://github.com/GfSE/SAF-Cameo-Profile/tree/main/SAF_Plugin/samples/SAF) - Openable Cameo .mdzip reference model of a fire-fighting drone system, built with the System Architecture Framework `SysMLv1` `Cameo` `has-model` `tool` (2026).
- [MOSA Implementation \(CUSA 2026, Cameo\)](https://github.com/EnolaTechnologies/cusa26) - Cameo .mdzip model of a Modular Open Systems Approach implementation, from a CATIA User Symposium talk `SysMLv1` `Cameo` `has-model` `paper` (2026).
- [GaloisInc — VERSE-OpenSUT](https://github.com/GaloisInc/VERSE-OpenSUT/tree/main/models/SysMLv1) - Open System-Under-Test reference with Cameo SysML v1 .mdzip models \(MPS, system overview\) `SysMLv1` `Cameo` `has-model` `paper` (2025).
- [Open-MBEE MDK DocGen Sample Model](https://github.com/Open-MBEE/exec-cameo-mdk/tree/develop/src/main/dist/samples/MDK) - Cameo .mdzip sample model demonstrating the Model Development Kit's DocGen document generation `SysMLv1` `Cameo` `has-model` `tool` (2024).
- [EOSS — Earth Observation Satellite System \(Cameo\)](https://github.com/seakers/cameo-LLM-plugin/tree/main/cameo/examples) - Cameo .mdzip model of an Earth-observation satellite system from the SEAK Lab `SysMLv1` `Cameo` `has-model` `paper` (2023).
- [GTRI INGRID Rapid-Modeling Demo Models](https://github.com/gtri/rapid-modeling-tools/tree/master/ingrid-quick-start) - Cameo/MagicDraw .mdzip demo models shipped with GTRI's INGRID pattern-based rapid-modeling tooling `SysMLv1` `CATIA-Magic` `has-model` `tool` (2023).
- [Package Delivery Drone \(Cameo\)](https://github.com/jmgogo/Package-Delivery-Drone/blob/main/model/Package%20Delivery%20Drone.mdzip) - Self-contained Cameo .mdzip SysML model of a package-delivery drone system architecture \(Apache-2.0\) `SysMLv1` `Cameo` `has-model` `paper` (2023).
- [Multiagent Warehouse \(MaaS\)](https://github.com/autarchprinceps/Multiagent-Warehouse/blob/master/Documentation/maas-warehouse.mdzip) - A MagicDraw .mdzip model of a multi-agent warehouse system `SysMLv1` `CATIA-Magic` `has-model` `paper` (2017).

#### Tools, plugins & automation

- [cameo-mcp-bridge](https://github.com/ajhcs/cameo-mcp-bridge) - Independent MIT-licensed MCP server bridging AI assistants to Cameo/CATIA Magic for SysML/UML create and query `SysMLv1` `Cameo` `mcp` (2026).
- [jgs-magic-sysmlv1-mcp](https://github.com/jgsystemsconsulting/jgs-magic-sysmlv1-mcp) - JG Systems SysML v1 MCP bridge \(~115 tools\) over a local link to CATIA Magic; FREE/PRO/ENTERPRISE `SysMLv1` `CATIA-Magic` `mcp` `paid` (2026).
- [jgs-magic-sysmlv1-read-skills](https://github.com/jgsystemsconsulting/jgs-magic-sysmlv1-read-skills) - Free read-only SysML v1 analysis skills for CATIA Magic \(navigate, inspect, audit, report\) `SysMLv1` `CATIA-Magic` `plugin` (2026).
- [Open-MBEE MBSEPlugin](https://github.com/Open-MBEE/MBSEPlugin) - Open-source MagicDraw/Cameo plugin \(DocGen document generation, Cameo Simulation Toolkit integration\) `SysMLv1` `Cameo` `plugin` (2024).

#### Communities & blogs

- [CameoMagic](https://cameomagic.com/) - Practitioner site focused on Cameo/MBSE tutorials, training, and certification prep `SysML-general` `Cameo` `blog` (2024).

### Tools, plugins & automation

- [GfSE SAF Cameo Profile](https://github.com/GfSE/SAF-Cameo-Profile) - System Architecture Framework profile, UAF-tracing profile, and library packaged for Cameo `SysMLv1` `Cameo` `plugin` (2026).
- [SCRE Cameo Profiles](https://github.com/tsherburne/scre-profile) - Secure Cyber Resilient Engineering profiles for Cameo, built on RAAML and SACM \(safety/assurance\) `SysMLv1` `Cameo` `plugin` (2025).
- [Cameo Systems Modeler / CATIA Magic](https://www.3ds.com/products/catia/no-magic/cameo-systems-modeler) - Commercial cross-platform MBSE environment: SysML, UML, DoDAF/MODAF, requirements traceability `SysMLv1` `Cameo` `tool` `paid` (2024).
- [Eclipse Papyrus](https://eclipse.dev/papyrus/) - Industrial-grade open-source Eclipse modeling tool for UML with full SysML support `SysMLv1` `Papyrus` `tool` (2024).
- [IBM Engineering Systems Design Rhapsody](https://www.ibm.com/products/engineering-rhapsody) - Commercial MBSE tool: SysML plus the Harmony method, UAF/DoDAF, AUTOSAR, FMI co-simulation `SysMLv1` `Rhapsody` `tool` `paid` (2024).
- [Modelio](https://github.com/ModelioOpenSource/Modelio) - Open-source \(GPL-3.0\) enterprise modeling environment with a full SysML v1 diagram suite incl. parametrics `SysMLv1` `Modelio` `other-tool` `tool` (2024).

### Specifications & standards

- [OMG SysML v1.7](https://www.omg.org/spec/SysML/1.7/) - The final SysML v1 release; the general-purpose v1 MBSE modeling language `SysMLv1` `spec` (2024).
<!-- AUTOGEN:END section=sysml-v1 -->

## SysML v2

Use this when you're starting fresh and want a textual, tool-portable model. SysML v2 is
the released successor: its `.sysml` text is openable in any v2 tool (SysIDE, SysON, the
Pilot Implementation), and the open-web corpus of v2 example models is large and growing.

<!-- AUTOGEN:START section=sysml-v2 -->
### Tutorials

- [Eclipse SysON — Tutorials \(YouTube\)](https://www.youtube.com/@EclipseSysON) - Free tutorial and demo videos for the open-source web-based SysML v2 modeler `SysMLv2` `SysON` `video` (2025).

### Courses & learning paths

- [Intro to MBSE and SysML v2 with Cameo \(TriMech\)](https://trimech.com/intro-to-mbse-and-sysml-v2-training-course/) - SysML v2 introductory course for newcomers, taught using Cameo `SysMLv2` `Cameo` `course` `paid` (2024).
- [SysML v2 Workshop on Cameo / CATIA Magic \(Webel\)](https://webel.com.au/node/4399) - 5-day Webel SysML v2 workshop run on Cameo/CATIA Magic with a Balls & Boxes sample `SysMLv2` `Cameo` `course` `paid` (2024).
- [Transitioning Models to SysML v2 with MBSE \(Caltech CTME\)](https://ctme.caltech.edu/transitioning-models-to-sysml-v2-with-mbse.html) - 3-day Caltech course on moving SysML v1 Cameo models to SysML v2 `SysMLv2` `Cameo` `course` `paid` (2024).

### Example models

- [Airbus Apollo-11 SysML v2](https://github.com/airbus/apollo-11-sysml-v2) - Apollo 11 reference model, full traceability `SysMLv2` `has-model` (2026).
- [DLR-FT STPA Library](https://github.com/DLR-FT/SysMLv2LibrarySTPA) - DLR System-Theoretic Process Analysis safety library + worked example `SysMLv2` `has-model` (2026).
- [fusion-tea](https://github.com/1cFE/fusion-tea) - Fusion-energy model + units/costing libraries \(36 .sysml files\) `SysMLv2` `has-model` (2026).
- [GfSE SAF-SysMLV2](https://github.com/GfSE/SAF-SysMLV2) - System Architecture Framework expressed in SysML v2 \(33 files\) `SysMLv2` `has-model` (2026).
- [jhaws1982 OOSEM Reference](https://github.com/jhaws1982/sysmlv2-mbse-reference) - OOSEM reference model in SysML v2 `SysMLv2` `has-model` (2026).
- [MBSE4U — The SysML v2 Book Examples](https://github.com/MBSE4U/the-sysmlv2-book-examples) - Companion Cameo .mdzip models \(incl. a Drone\) for Weilkiens & Muggeo's SysML v2 book `SysMLv2` `Cameo` `has-model` `paper` (2026).
- [OMG SysML v2 Release examples](https://github.com/Systems-Modeling/SysML-v2-Release/tree/master/sysml/src/examples) - 300+ official .sysml example & training models `SysMLv2` `has-model` (2026).
- [Robot Vacuum Cleaner \(SysML v2\)](https://github.com/elan8/sysml-robot-vacuum-cleaner) - 21-file autonomous-robot model: architecture, behavior, firmware, analysis `SysMLv2` `has-model` (2026).
- [sensmetry Advent of SysML v2](https://github.com/sensmetry/advent-of-sysml-v2) - 44 bite-sized SysML v2 example models `SysMLv2` `has-model` (2026).
- [sensmetry DETECT](https://github.com/sensmetry/detect) - Hazard-analysis \(DEM&S\) tool modeled in SysML v2 `SysMLv2` `has-model` (2026).
- [SysML v2 Astronomy Reference](https://github.com/elan8/sysml-v2-astronomy-reference) - A worked astronomy-domain SysML v2 model `SysMLv2` `has-model` (2026).
- [Don't Panic Batmobile](https://github.com/MBSE4U/dont-panic-batmobile) - Companion model for Weilkiens & Muggeo's Don't Panic `SysMLv2` `has-model` (2025).
- [GfSE SysML v2 Models](https://github.com/GfSE/SysML-v2-Models) - Curated, CI-validated collection \(Drone, HVAC, Vehicle…\) `SysMLv2` `has-model` (2025).
- [Open-MBEE DesertKite \(OOSEM\)](https://github.com/Open-MBEE/DesertKite.sysml) - Unusual real-world OOSEM domain model \(archaeological desert kites\) `SysMLv2` `has-model` (2025).
- [TU Ilmenau CMBSE](https://github.com/ziruili-tu-ilmenau/CMBSE) - Collaborative-MBSE research model: force-measurement / load-cell system `SysMLv2` `has-model` (2025).
- [yutaro-ito Sample SysML v2 Project](https://github.com/yutaro-ito/sample-sysml-v2-project) - End-to-end method walkthrough: context→requirements→logical architecture `SysMLv2` `has-model` (2022).

### Tools, plugins & automation

- [Eclipse SysON](https://github.com/eclipse-syson/syson) - Open-source web-based SysML v2 modeler \(graphical, form, tabular editors\), by Obeo and CEA List `SysMLv2` `SysON` `tool` (2026).
- [elan8 SysML v2 Domain Libraries](https://github.com/elan8/sysml-domain-libraries) - Importable domain building-block libraries \(robotics: actuation, control, autonomy, operations\) `SysMLv2` `has-model` `tool` (2026).
- [Sysand \(Sensmetry\)](https://github.com/sensmetry/sysand) - Open-source package manager for SysML v2 and KerML model libraries `SysMLv2` `other-tool` `tool` (2026).
- [SysML v2 Library for AADL](https://github.com/Systems-Modeling/SysML-v2-AADL-Release) - Official SysML v2 rendering of AADL \(base types, property sets, component categories\) for avionics/embedded `SysMLv2` `tool` (2026).
- [SysML v2 Pilot Implementation](https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation) - OMG reference pilot: Xtext editors, PlantUML visualization, and a Jupyter kernel for SysML v2 `SysMLv2` `tool` (2026).
- [SysML v2 Standard Library](https://github.com/Systems-Modeling/SysML-v2-Release/tree/master/sysml.library) - The normative KerML/SysML v2 standard libraries: ISQ quantities, SI units, geometry, analysis, domain libs `SysMLv2` `tool` (2026).
- [SYSMOD for SysML v2](https://github.com/MBSE4U/sysmod-sysmlv2) - Tim Weilkiens' SYSMOD method as an importable SysML v2 language-extension library, with examples `SysMLv2` `tool` (2026).
- [SysIDE Editor \(Sensmetry\)](https://github.com/sensmetry/sysml-2ls) - VS Code extension for SysML v2: highlighting, autocompletion, and formatting `SysMLv2` `SysIDE` `other-tool` `plugin` (2025).

### Specifications & standards

- [Systems-Modeling/SysML-v2-Release](https://github.com/Systems-Modeling/SysML-v2-Release) - Start here for SysML v2: the latest incremental release with spec, training, examples, libraries `SysMLv2` `spec` (2026).
- [OMG KerML Specification](https://www.omg.org/spec/KerML/) - The Kernel Modeling Language spec — the formal semantic foundation underlying SysML v2 `SysMLv2` `spec` (2025).
- [OMG SysML v2.0 Specification](https://www.omg.org/spec/SysML/2.0/) - The dedicated landing page for the SysML v2.0 language release `SysMLv2` `spec` (2025).
- [OMG Systems Modeling API & Services](https://www.omg.org/spec/SystemsModelingAPI/) - OMG spec defining platform-independent REST/SOAP/Java APIs for KerML and SysML v2 models `SysMLv2` `spec` (2025).

### APIs & automation

- [Open-MBEE Flexo-MMS for SysML v2](https://github.com/Open-MBEE/flexo-mms-sysmlv2) - Git+RDF-backed Model Management System implementing the OMG SysML v2 REST/HTTP API \(Git for models\) `SysMLv2` `tool` (2026).
- [SysML v2 API Services](https://github.com/Systems-Modeling/SysML-v2-API-Services) - Proof-of-concept REST implementation of the OMG Systems Modeling API & Services spec `SysMLv2` `tool` (2026).
- [SysML v2 API Cookbook](https://github.com/Systems-Modeling/SysML-v2-API-Cookbook) - Recipes and worked examples for using the SysML v2 API `SysMLv2` `tool` (2025).
- [SysML v2 API Python Client](https://github.com/Systems-Modeling/SysML-v2-API-Python-Client) - Official Python client for the SysML v2 Systems Modeling API & Services `SysMLv2` `tool` (2021).
<!-- AUTOGEN:END section=sysml-v2 -->

## UAF & architecture frameworks

Use this when you build defence or enterprise architectures. **UAF** is the modern OMG
framework — it supersedes UPDM/DoDAF/MODAF and runs natively in Cameo; start there unless
a specific programme mandates DoDAF or NAF.

<!-- AUTOGEN:START section=uaf -->
### Tutorials

- [UAF Plugin Documentation \(Cameo/No Magic\)](https://docs.nomagic.com/spaces/UAFP190SP3/pages/47112606/UAF+Plugin+Documentation) - Official Dassault/No Magic docs for the UAF plugin in Cameo/MagicDraw, with sample models `SysMLv1` `Cameo` `tutorial` (2024).

### Tools, plugins & automation

- [UAF for Papyrus \(Adocus\)](https://github.com/Adocus/UAF-for-Papyrus) - OMG Unified Architecture Framework profile plus a UAF Measurement Library for Eclipse Papyrus `SysMLv1` `Papyrus` `plugin` (2022).

### Communities & blogs

- [OMG UAF Program Page](https://www.omg.org/uaf/) - OMG's UAF overview and community page: concepts, videos, certification, and adoption guidance `SysML-general` `blog` (2024).

### Specifications & standards

- [OMG UAF Specification](https://www.omg.org/spec/UAF) - The Unified Architecture Framework spec hub: Domain Metamodel \(DMM\) and the UAFML profile Cameo implements `SysML-general` `spec` (2022).
- [NATO Architecture Framework v4](https://www.nato.int/en/about-us/organization/nato-structure/digital-policy-committee-dpc/nato-architecture-framework-version) - Official NATO landing page for NAF v4.1, the current NATO architecture framework `SysML-general` `standard` (2020).
- [MOD Architecture Framework \(MODAF\)](https://www.gov.uk/guidance/mod-architecture-framework) - Official UK gov.uk MODAF page; now withdrawn in favour of NAF/UAF but still widely referenced `SysML-general` `standard` (2016).
- [OMG UPDM Specification](https://www.omg.org/spec/UPDM/) - The Unified Profile for DoDAF/MODAF — UAF's predecessor profile, still referenced by legacy programmes `SysML-general` `spec` (2013).
- [DoD Architecture Framework \(DoDAF 2.02\)](https://dodcio.defense.gov/library/dod-architecture-framework/) - Official US DoD CIO page for DoDAF 2.02, the US defence architecture framework `SysML-general` `standard` (2010).
<!-- AUTOGEN:END section=uaf -->

## Adjacent & non-SysML notations

Use this when your toolchain is Eclipse-based or you work in a non-SysML notation.
Arcadia/Capella, OPM, and OML each bring their own method and tooling that MBSE
practitioners regularly run into alongside SysML.

<!-- AUTOGEN:START section=arcadia -->
### Arcadia / Capella

#### Methodology & guides

- [Arcadia Method \(official\)](https://mbse-capella.org/arcadia.html) - Canonical page for the Arcadia method \(AFNOR Z67-140\) implemented by Eclipse Capella `SysML-general` `blog` (2024).
- [An Introduction to Arcadia \(Voirin\)](https://download.eclipse.org/capella/publis/An_Introduction_to_Arcadia_20150115.pdf) - Open primer on the Arcadia method's perspectives and engineering workflow `SysML-general` `paper` (2015).

#### Tools, plugins & automation

- [py-capellambse](https://github.com/DSD-DBS/py-capellambse) - Headless Python library to load, traverse, diff, and generate from Capella/Arcadia models \(models as data\) `SysML-general` `Capella` `other-tool` `tool` (2026).
- [Eclipse Capella](https://mbse-capella.org/) - Open-source MBSE tool implementing the Arcadia method \(adjacent to SysML\) `SysML-general` `Capella` `other-tool` `tool` (2024).
<!-- AUTOGEN:END section=arcadia -->

<!-- AUTOGEN:START section=opm -->
### OPM

#### Methodology & guides

- [Object-Process Methodology \(Dori, Technion\)](https://esml.technion.ac.il/opm/overview/) - Authoritative overview of OPM \(ISO 19450\), a self-contained graphical-plus-textual modeling method `SysML-general` `blog` (2022).
<!-- AUTOGEN:END section=opm -->

<!-- AUTOGEN:START section=oml -->
### OML

#### Tools, plugins & automation

- [openCAESAR Metrology Vocabularies](https://github.com/opencaesar/metrology-vocabularies) - ISO/IEC 80000 quantities-and-units plus JCGM VIM4 metrology, as importable OML libraries `SysML-general` `other-tool` `tool` (2026).
- [openCAESAR / OML](https://github.com/opencaesar/oml) - JPL-originated ontology-based modeling language and OWL toolchain for traceable MBSE, with worked examples `SysML-general` `other-tool` `tool` (2025).
<!-- AUTOGEN:END section=oml -->

## Cross-cutting (language-general)

Use this when the resource applies regardless of notation — the methods (OOSEM, SYSMOD,
Harmony, FAS), specifications and standards, communities, and reusable vocabularies that
span SysML v1, v2, and beyond.

<!-- AUTOGEN:START section=cross-cutting -->
### Methodology & guides

- [FAS Method](https://fas-method.org/) - Official site for Functional Architectures for Systems \(Lamm & Weilkiens\), with open publications and plugins `SysML-general` `blog` (2024).
- [OMG MBSE Wiki — Methodology Directory](https://www.omgwiki.org/MBSE/doku.php?id=mbse:methodology) - Master index of MBSE methodologies \(OOSEM, SYSMOD, Harmony, Arcadia, and more\) `SysML-general` `blog` (2024).
- [SpesML — Open Methodology Docs \(TUM/fortiss\)](https://spesml.github.io/) - Full open documentation of the SPES-based SpesML method: viewpoints, concepts, case studies, Cameo plugin `SysML-general` `Cameo` `blog` (2024).
- [JPL State Analysis](https://mds.jpl.nasa.gov/public/sa/) - NASA/JPL's primary state-based MBSE method for control-system and mission modeling `SysML-general` `blog` (2023).
- [OOSEM \(OMG MBSE Wiki\)](https://www.omgwiki.org/MBSE/doku.php?id=mbse:incoseoosem) - Vendor-neutral reference for the Object-Oriented Systems Engineering Method `SysML-general` `blog` (2023).
- [SYSMOD \(Tim Weilkiens\)](https://mbse4u.com/sysmod/) - Canonical page for the SYSMOD method toolbox: roles, activities, products, and SysML integration `SysML-general` `blog` (2022).
- [Harmony aMBSE Deskbook \(IBM\)](https://jazz.net/library-content/wp-content/uploads/2020/11/Harmony-aMBSE-Deskbook-Version-1.pdf) - The full IBM Harmony agile-MBSE method deskbook, freely available `SysMLv1` `Rhapsody` `book` (2020).
- [Survey of MBSE Methodologies \(Estefan, INCOSE/OMG\)](https://www.omg.org/sysml/MBSE_Methodology_Survey_RevB.pdf) - The standard comparative reference: OOSEM, Harmony-SE, RUP-SE, Vitech, JPL State Analysis, OPM side by side `SysML-general` `paper` (2008).

### Courses & learning paths

- [NASA NESC Academy — Systems Engineering Catalog](https://nescacademy.nasa.gov/catalogs/systemseng) - NASA's public on-demand video library with multiple freely viewable MBSE lectures `SysML-general` `video` (2024).
- [Modeling with SysML Tutorial \(Friedenthal & Oster, JHU/APL\)](https://www.jhuapl.edu/sites/default/files/2023-03/ModelingwithSysMLTutorial.pdf) - INCOSE tutorial deck on building SysML models, freely hosted by JHU/APL `SysML-general` `course` (2023).
- [MIT OCW 16.842 — Fundamentals of Systems Engineering](https://ocw.mit.edu/courses/16-842-fundamentals-of-systems-engineering-fall-2015/) - de Weck's open graduate SE course; Session 3 covers SysML/OPM. Free video and notes `SysML-general` `course` (2015).
- [OMG/INCOSE SysML Tutorial \(Friedenthal et al.\)](https://www.omg.org/sysml/INCOSE-OMGSysML-Tutorial-Final-090901.pdf) - The canonical 175-slide SysML tutorial by the spec authors; free, foundational `SysML-general` `course` (2009).

### Tools, plugins & automation

- [Gaphor](https://github.com/gaphor/gaphor) - Lightweight open-source Python UML/SysML/RAAML modeler with a clean, readable OMG-standard metamodel `SysML-general` `Gaphor` `other-tool` `tool` (2026).
- [QUDT — Quantities, Units, Dimensions & Types](https://github.com/qudt/qudt-public-repo) - RDF/OWL vocabulary of quantities and units widely reused for units handling in MBSE models `SysML-general` `other-tool` `tool` (2024).

### Communities & blogs

- [MBSE4U \(Tim Weilkiens\)](https://mbse4u.com/) - Long-running practitioner blog and bookshop covering MBSE, SysML v1/v2, SYSMOD, FAS, and VAMOS `SysML-general` `blog` (2025).

### Specifications & standards

- [OMG SysML Specification](https://www.omg.org/spec/SysML/) - Canonical OMG SysML spec page; now defaults to v2.0 \(2025\), with v1.7 the final v1 release `SysML-general` `spec` (2025).
- [INCOSE Systems Engineering Handbook](https://www.incose.org/resources-publications/technical-publications/se-handbook/) - The practitioner reference for SE life-cycle processes, aligned to ISO/IEC/IEEE 15288 `SysML-general` `standard` `paid` (2023).
- [NASA Systems Modeling Handbook \(NASA-HDBK-1009\)](https://standards.nasa.gov/standard/NASA/NASA-HDBK-1009) - Official NASA tool-agnostic guidance on building and using system models `SysML-general` `standard` (2022).
<!-- AUTOGEN:END section=cross-cutting -->

## Find it your way

Prefer to browse by something other than language? The same entries are indexed four ways
— **Openable models**, **By tool**, **By resource type**, and a **Tag legend** — in
**[docs/find-it-your-way.md](docs/find-it-your-way.md)**, generated from the same data.

## The competitive landscape

Why this list exists, with evidence (gathered 2026-06-23). Existing SysML/SE awesome-lists
are either abandoned, narrow, or carry no Cameo / Magic Grid coverage at all:

<!-- AUTOGEN:START section=competitive -->
| List                                                                                                      | Stars | Last update      | MBSE coverage                                                                                                |
| --------------------------------------------------------------------------------------------------------- | ----- | ---------------- | ------------------------------------------------------------------------------------------------------------ |
| [mycr0ft/awesome-sysml](https://github.com/mycr0ft/awesome-sysml)                                         | ~2    | 2026-06 (active) | Narrow: SysML v2 textual tooling only; ~3 Cameo mentions, **0 MagicDraw / Magic Grid**, no methods/libraries |
| [kktse/awesome-systems-engineering](https://github.com/kktse/awesome-systems-engineering)                 | ~11   | 2021 (abandoned) | Broad SE links, **no MBSE depth**, stale                                                                     |
| [rolling-robot/awesome-systems-engineering](https://github.com/rolling-robot/awesome-systems-engineering) | ~1    | 2024 (stagnant)  | **None**                                                                                                     |
<!-- AUTOGEN:END section=competitive -->

No actively-maintained `awesome-mbse` with this breadth existed before this list. The
differentiator is **scope** — SysML v1/v2 + methods + tooling + reusable libraries +
openable models, with **Magic Grid / Cameo** depth no other list has — plus freshness.

## Contributing

Contributions welcome — see [CONTRIBUTING.md](CONTRIBUTING.md) for the inclusion bar,
the `data/entries.yaml` record format, and the tag vocabulary. **Don't edit `README.md`
directly** — it is generated from the data. Suggest a resource via the
[issue form](../../issues/new/choose) or open a pull request editing the data files.

## Support & security

Questions or a problem with a linked resource? Open an issue using the suggest-a-resource
form (linked in the Contributing section above). To report a malicious or compromised link
privately, email **support@jgsystemsconsulting.com** — see [SECURITY.md](SECURITY.md).

---

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the maintainers have waived all copyright and related
or neighboring rights to this work — released under CC0 1.0 Universal. See [LICENSE](LICENSE).
