# Seed inventory: awesome-digital-engineering

Working ledger for the launch. Not committed to any repo. Verdict vocabulary:
`verified` (entry ships) / `omit` (fails the bar or never verified) / `issue`
(ships as a seed-inventory issue after launch).

| # | Candidate | URL | Host class | Research grade | Verify method | HTTP result | Browser result | Inclusion bar | Section / tags / year | Verdict | Notes |
|---|-----------|-----|-----------|----------------|---------------|-------------|----------------|---------------|----------------------|---------|-------|
| 1 | ASME Y14.41 storefront | https://www.asme.org/codes-standards/find-codes-standards/y14-41-digital-product-definition-data-practices | standard | ESTABLISHED | curl | 200 | n/a | pass | 2 / `MBD` `report` `standard` `paid` / 2026 | verified | 2026-09-17 |
| 2 | DMSC about (QIF/DMIS) | https://qifstandards.org/about-dmsc/ | standard | PROVISIONAL | curl | 200 | n/a | pass | 5 / `DE-general` `report` / 2020 | verified | ISO 23952:2020 context |
| 3 | LOTAR International | https://lotar-international.org/ | standard | PROVISIONAL | curl | 200 | n/a | pass | 5 / `DE-general` `report` / 2024 | verified | EN/NAS 9300 / OAIS |
| 4 | Wikipedia ISO 10303 | https://en.wikipedia.org/wiki/ISO_10303 | standard | PROVISIONAL | curl | 200 | n/a | pass | 2 / `digital-thread` `report` / 2024 | verified | fallback STEP narrative; prefer primary later |
| 5a | DoD DE Strategy PDF acq.osd.mil | https://www.acq.osd.mil/se/docs/2018-Digital-Engineering-Strategy.pdf | blocked | PROVISIONAL | curl | 404 | not attempted | fail | 1 | omit | dead path |
| 5b | DoD DE Strategy media.defense.gov | https://media.defense.gov/2018/Jun/15/2001931999/-1/-1/0/20180614_DIGITAL_ENGINEERING_STRATEGY_FINAL.PDF | blocked | PROVISIONAL | curl | 403 | not attempted | fail live | 1 | issue | viable retry; no browser 200 this session |
| 6 | NDIA SE division | (no stable URL this session) | blocked | — | — | — | — | — | 5 | omit | no URL without invention |
| 7 | INCOSE DE WG | (no stable URL this session) | blocked | — | — | — | — | — | 5 | omit | no URL without invention |
| 8 | SEBoK Digital Engineering | https://sebokwiki.org/wiki/Digital_Engineering | blocked | PROVISIONAL | curl | 403 | not attempted | fail live | 7 | issue | viable browser retry |
| 9 | QIF standards home | https://qifstandards.org/ | standard | PROVISIONAL | curl | 200 | n/a | pass | 5 / `DE-general` `report` / 2024 | verified | org home |
| 10 | STEP-file-parser (AlexFemec) | https://github.com/AlexFemec/STEP-file-parser | standard | — | curl | 200 | n/a | pass | 6 / `digital-thread` `tool` `other-tool` / 2024 | verified | ISO 10303-21 parser |
| 11 | step-file-parser (IfcOpenShell) | https://github.com/IfcOpenShell/step-file-parser | standard | — | curl | 200 | n/a | pass | 6 / `digital-thread` `tool` `other-tool` / 2024 | verified | pure Python STEP parser |
| 12 | NIST EL Systems Integration Division | https://www.nist.gov/el/systems-integration-division | standard | — | curl | 200 | n/a | pass | 5 / `DE-general` `report` / 2024 | verified | MBE-related org page |
| 13 | NTRS ExMC Digital Engineering | https://ntrs.nasa.gov/citations/20250000093 | provisional | PROVISIONAL | ntrs API 200 | API ok | citation not curl-checked | pass topic | 7 / `DE-general` `report` / 2025 | issue | add after citation page 200 |
| 14 | NTRS NASA Digital Engineering Transformation | https://ntrs.nasa.gov/citations/20240006148 | provisional | PROVISIONAL | ntrs API 200 | API ok | citation not curl-checked | pass topic | 7 / `DE-general` `report` / 2024 | issue | add after citation page 200 |
| 15 | NTRS Digital Engineering Strategy Overview | https://ntrs.nasa.gov/citations/20230012351 | provisional | PROVISIONAL | ntrs API 200 | API ok | citation not curl-checked | pass topic | 1 / `DE-general` `report` / 2023 | issue | add after citation page 200 |

## Gate summary

- Verified ship rows: 8 (ASME, DMSC about, LOTAR, Wikipedia ISO 10303, QIF home, two STEP parsers, NIST SID)
- Omitted: DoD acq path 404; NDIA/INCOSE no URL without invention
- Issue (post-launch): media.defense.gov DoD PDF 403; SEBoK 403; three NTRS citations pending page verify
- Under-40 launch: yes (honest label required)

## Verified set

### Policy and strategy

_No verified entries yet._

### Standards

- [ASME Y14.41](https://www.asme.org/codes-standards/find-codes-standards/y14-41-digital-product-definition-data-practices) - Digital product definition data practices for annotated model-based 3D datasets `MBD` `report` `standard` `paid` (2026).
- [ISO 10303 (STEP) overview](https://en.wikipedia.org/wiki/ISO_10303) - Product data representation and exchange family for CAD/PMI interoperability `digital-thread` `report` (2024).

### Digital thread and interoperability

_No verified entries yet._

### Model-based definition and PMI

_No verified entries yet._

### Government and consortia programs

- [DMSC / QIF](https://qifstandards.org/about-dmsc/) - Digital Metrology Standards Consortium; QIF (ISO 23952) and DMIS overview `DE-general` `report` (2020).
- [QIF Standards](https://qifstandards.org/) - Quality Information Framework home and digital metrology resources `DE-general` `report` (2024).
- [LOTAR International](https://lotar-international.org/) - Long-term archiving EN/NAS 9300 family based on OAIS `DE-general` `report` (2024).
- [NIST Systems Integration Division](https://www.nist.gov/el/systems-integration-division) - NIST EL division covering systems integration and MBE-related work `DE-general` `report` (2024).

### Open tools and reference implementations

- [AlexFemec/STEP-file-parser](https://github.com/AlexFemec/STEP-file-parser) - Basic parser for ISO 10303-21 STEP files `digital-thread` `tool` `other-tool` (2024).
- [IfcOpenShell/step-file-parser](https://github.com/IfcOpenShell/step-file-parser) - Pure Python ISO 10303-21 STEP physical file parser `digital-thread` `tool` `other-tool` (2024).

### Learning and reports

_No verified entries yet._

### Commercial platforms

_No verified entries yet._


## Update 2026-09-17 v0.1.1

Spoke README ships **31 verified entries** (merged PR #8). Still under FAMILY ~40 bar; honest growth label remains. DoD/SEBoK/NTRS remain seed-inventory issues on the spoke.
