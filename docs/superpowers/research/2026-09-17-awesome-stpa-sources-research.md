# Research: awesome-stpa sources and namespace

## Research brief

**Primary question:** Is `awesome-stpa` clear to build, and what live STAMP/STPA resources seed a ~40+ entry curated list under the family standard?

**Sub-questions:**
1. GitHub namespace: any incumbent `awesome-stpa`, `awesome-stamp`, or substantial STPA resource lists?
2. Candidate inventory across foundations, tools, standards, cases, courses, software, papers.
3. Awesome-list skeleton best practice matching the jgsystemsconsulting family.
4. Tag vocabulary values for the STPA niche.

**Success criteria:** SC1 namespace; SC2 ~40 candidates with URLs; SC3 skeleton/CI notes; SC4 tag values.

**Out of scope:** Implementing the repo; pure FMEA/FTA catalogs; ArchiMate spoke.

**Budget:** 1–3 rounds. Retrieved_at: 2026-09-17.

## Findings

### SC1 Namespace (PROVISIONAL → parent-corroborated)

- No repository named `awesome-stpa` or dedicated STPA curated awesome list found on GitHub topics (`stpa`) or family registry (Planned, empty as of 2026-09).
- `gh api search/repositories?q=awesome-stpa+OR+awesome-stamp` returned unrelated hits (e.g. Gitcoin Passport "Stamp" implementations), not STPA safety lists.
- sindresorhus/awesome has no STPA/STAMP safety list category entry (scout R1).
- **Decision:** namespace clear for `awesome-stpa` under `jgsystemsconsulting`. Re-check the day the remote is created (FAMILY rule).

### SC2 Candidate pool (≥40 with URL + role)

Foundations / learning hubs:

1. MIT PSAS home — https://psas.scripts.mit.edu/home/ — central STAMP/STPA hub
2. STPA Handbook (Leveson & Thomas) — https://psas.scripts.mit.edu/home/get_file.php?name=STPA_Handbook.pdf — free process handbook (HTTP 200)
3. CAST Handbook — https://psas.scripts.mit.edu/home/get_file4.php?name=CAST_Handbook.pdf — free CAST guide
4. Books and handbooks index — https://psas.scripts.mit.edu/home/books-and-handbooks/
5. Materials index — https://psas.scripts.mit.edu/home/materials/
6. Engineering a Safer World (Leveson) — https://direct.mit.edu/books/oa-monograph/2908/Engineering-a-Safer-WorldSystems-Thinking-Applied — OA monograph (catalog 403 from some clients; keep canonical OA URL)
7. Introduction to System Safety Engineering — https://mitpress.mit.edu/9780262546881/
8. Safety-III paper PDF — http://sunnyday.mit.edu/safety-3.pdf — host flaky (000 this session); prefer alternate if dead at ship
9. Publications search — https://psas.scripts.mit.edu/home/publications/
10. Online education — https://psas.scripts.mit.edu/home/online-education/

Tools (open + commercial; PSAS catalog + verified):

11. XSTAMPP — https://github.com/SE-Stuttgart/XSTAMPP — open STAMP platform STPA/CAST (HTTP 200)
12. MicroSTAMP — https://github.com/Micro-STAMP/microstamp — open microservices STPA (HTTP 200)
13. PASTA VS Code — https://marketplace.visualstudio.com/items?itemName=kieler.pasta — STPA DSL extension
14. PASTA source — https://github.com/kieler/pasta (or kieler/stpa per PSAS) — HTTP 200 on pasta
15. stpa-capella — https://github.com/labs4capella/stpa-capella — Capella STPA viewpoint (HTTP 200)
16. CAIRIS — https://github.com/cairis-platform/cairis — secure systems modeling with STPA docs
17. CAIRIS STPA docs — https://cairis.readthedocs.io/en/latest/stpa.html
18. STAMP Workbench (IPA) — https://www.ipa.go.jp/en/digital/complex_systems/stamp_workbench.html (alt english/sec path)
19. TRACEIT — https://en.vwaycorp.com/traceit — commercial STPA tooling
20. VisualPro SA — https://en.vwaycorp.com/visualpro
21. RM Studio STPA — https://www.riskmanagementstudio.com/stpa-software-solution/
22. STPAmaster — https://stpamaster.com/
23. Depict — https://depict.systems — control-structure diagrams
24. STPA Safety-based Testing Plugin — https://github.com/SE-Stuttgart/STPA-Safety-based-Testing-Plugin
25. PSAS stamp-tools catalog — https://psas.scripts.mit.edu/home/stamp-tools/ — awareness list (not endorsement)

Standards (link catalog pages; do not claim STPA is mandated):

26. ISO 26262 overview — https://www.iso.org/standard/68383.html — automotive FS (paywalled text)
27. SAE ARP4761A — https://www.sae.org/standards/content/arp4761a/ — aerospace safety assessment (HTTP 200)
28. Note for list prose: SAE J3187 / AIR6913 cited by Capella STPA README as automotive/aero STPA-related SAE docs — verify URLs at execute

Cases / agency:

29. FAA STPA aviation safety eval PDF — https://rosap.ntl.bts.gov/view/dot/78914/dot_78914_DS1.pdf
30. FAA eVTOL STPA test case (2026 workshop) — PSAS wp-content 2026 PDF path from scout
31. Network Rail STPA resilient systems (2024 workshop PDF) — PSAS presentations
32. Healthcare CAST adverse event (2026 workshop PDF) — PSAS presentations
33. STAMP Workshop presentations archive — https://psas.scripts.mit.edu/home/mit-stamp-workshop-presentations/
34. STAMP Workshop 2026 info — http://psas.scripts.mit.edu/home/stamp-workshop-information/

Learning / community:

35. MIT STAMP tutorials — https://psas.scripts.mit.edu/home/mit-stamp-workshop-tutorials/
36. STAMP Institute training — https://classes.stamp-institute.com/p/home
37. gaphor RAAML/STPA-adjacent — https://github.com/gaphor/gaphor
38. train-gate STPA example — https://github.com/adityajeppu/train-gate-STPA-control
39. stpa-step1-dataset — https://github.com/andreyokamura-unicamp/stpa-step1-dataset
40. triarchsecurity/stpa — https://github.com/triarchsecurity/stpa — STPA for threat modeling
41. anvil-safety-framework — https://github.com/Dr-AneeshJoseph/anvil-safety-framework
42. LLM-Mutation ease-2026 replication — https://github.com/LLM-Mutation/ease-2026-replication-package

**Exclusion / rot list (do not ship as live primary without recheck):**

- http://sunnyday.mit.edu/ and handbook mirrors (timeouts)
- https://stamp-workshop.mit.edu / stamp-workshop.org (DNS fail)
- https://www.sahra.ch (parked)
- https://www.safetbox.de (TLS issues this session; may still list with note after recheck)
- SafetyHAT volpe DB host timeouts; Volpe landing 403
- MathWorks File Exchange STPA tool 403 from some clients
- SpecTRM safeware-eng.com cert expired

Workshop presentation PDFs count as case/learning entries only when individually linked; do not bulk-pad 120 slides as 120 list rows.

### SC3 Skeleton (PROVISIONAL, family-local CORROBORATED)

- Awesome badge right of H1: https://awesome.re/badge.svg
- License CC0-1.0 (sindresorhus + FAMILY)
- awesome-lint + lychee CI (FAMILY shared standard; hub blocking PR lychee with `--include-fragments=anchor-only`)
- Template shape: sibling `awesome-sysml-v2` workflows, hardened to FAMILY entry format (tags + year)

### SC4 Tag vocabulary (PROVISIONAL proposal)

Keep hub axes; STPA values:

- **method:** `STPA` `CAST` `STAMP` `STPA-Sec`
- **tool:** tool product slug or `none`
- **type:** `handbook` `book` `paper` `standard` `tool` `course` `video` `case` `dataset` `workshop`
- **standard:** `ISO-26262` `ARP4761A` `IEC-61508` `J3187` `AIR6913` `none`
- **domain:** `aerospace` `automotive` `rail` `healthcare` `cyber` `general`
- **paid:** `paid` when commercial/paywalled primary access
- **year:** `(YYYY)` terminal token per hub rule

## Synthesis

**Build `awesome-stpa`.** Namespace is clear enough under FAMILY rules (no STPA awesome incumbent; false-positive "stamp" hits are unrelated). Depth bar is met: 40+ distinct URL-backed candidates across foundations, tools, standards, cases, and learning, anchored on MIT PSAS plus verified GitHub tools.

**Standards section must stay honest:** ISO 26262 and ARP4761A are functional-safety assessment context where STPA is used or discussed in industry practice; the list must not claim the standards mandate STPA unless a primary quote is verified at execute.

**Link hygiene:** prefer `psas.scripts.mit.edu` over dead `sunnyday.mit.edu` / old workshop hosts. Drop or quarantine TLS/parked tool URLs until recheck. Engineering a Safer World keeps the MIT Press OA canonical URL even if some fetchers get 403.

**Ship path:** new sibling repo (not a folder inside awesome-mbse), FAMILY standard entry format, hub CONTRIBUTING year/dedupe/neutrality ported, sysml-v2 CI shape hardened to hub lychee, registry Planned→Live + hub README spoke link on go-live.

## Sources

| URL | Role |
|-----|------|
| https://psas.scripts.mit.edu/home/ | PSAS hub |
| https://psas.scripts.mit.edu/home/stamp-tools/ | Tools catalog |
| https://psas.scripts.mit.edu/home/books-and-handbooks/ | Handbooks |
| https://psas.scripts.mit.edu/home/get_file.php?name=STPA_Handbook.pdf | STPA Handbook PDF |
| https://github.com/SE-Stuttgart/XSTAMPP | XSTAMPP |
| https://github.com/Micro-STAMP/microstamp | MicroSTAMP |
| https://github.com/kieler/pasta | PASTA |
| https://github.com/labs4capella/stpa-capella | Capella STPA |
| https://www.sae.org/standards/content/arp4761a/ | ARP4761A |
| https://github.com/sindresorhus/awesome | awesome meta |
| https://awesome.re/badge.svg | badge |
| FAMILY.md / CONTRIBUTING.md (hub) | family standard |
