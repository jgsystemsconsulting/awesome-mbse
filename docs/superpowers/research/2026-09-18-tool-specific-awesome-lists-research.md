# Research: Tool-specific awesome lists alongside awesome-mbse

Date: 2026-09-18
Status: converged (Track 3 brief-covered; SC6 trademarks remain PROVISIONAL)

## Research brief

### Primary question

Which commercial/open MBSE-adjacent tools warrant dedicated "awesome-*" spoke repositories alongside the awesome-mbse hub (similar to awesome-capella), and what already exists on GitHub or elsewhere for those tools?

### Sub-questions

1. Does a public curated awesome list already exist for Sparx Systems Enterprise Architect (EA)?
2. Does a public curated awesome list already exist for Cameo Systems Modeler / CATIA Magic / MagicDraw beyond the hub section and the planned awesome-magic-grid spoke?
3. What is the state of the existing awesome-capella spoke and any external Capella lists?
4. Are there curated lists (awesome or equivalent) for MathWorks Simulink / System Composer, Rhapsody, PTC Integrity Modeler / Windchill Modeler, Ansys SCADE, IBM Engineering Systems Design Rhapsody, OpenMBEE, Eclipse Papyrus/SysON, or similar?
5. For each candidate tool, what is the rough size of the public GitHub ecosystem (plugins, scripts, example models, tutorials, API wrappers) that would stock a spoke?
6. Which candidates are best placed for a new family spoke given: (a) ecosystem mass, (b) gap vs existing lists, (c) fit with the hub's MBSE practitioner audience, (d) non-overlap with live family spokes?

### Success criteria (decisions this research must support)

- SC1: Name whether Enterprise Architect already has a credible public awesome/curated list; if yes, URL and maintainer; if no, state gap with evidence.
- SC2: Name whether Cameo/MagicDraw/CATIA Magic already has a dedicated public awesome list outside this family's hub/planned spoke; if yes, URL; if no, state gap.
- SC3: Confirm Capella list landscape (family spoke + any external lists) so Capella is not re-proposed as net-new.
- SC4: Produce a short ranked shortlist (top 3–5) of tool-specific spoke candidates with one-line rationale each, grounded in GitHub/web evidence of ecosystem mass and list gaps.
- SC5: Flag tools that look attractive but should stay hub sections only (thin public corpus, pure proprietary lock-in with no openable artifacts, or out of MBSE scope).
- SC6: Note any naming/branding landmines (trademark, vendor "awesome" pages that are marketing not lists).

### Out of scope

- Implementing or scaffolding any new spoke repo.
- Full seed inventories or link audits for a chosen spoke.
- SysML v2 language lists (already covered by awesome-sysml-v2).
- ArchiMate / STPA / requirements / digital-engineering spokes (already family-owned).
- Pricing, license negotiation, or vendor partnership advice.

### Budget

- Max 3 research rounds (used 2; Round 3 skipped under Track 3 brief-covered).
- Prefer primary sources: GitHub search/API, vendor docs, existing family FAMILY.md/README, sindresorhus/awesome and related indexes.

### Family context (internal)

Hub family already Live or planned (do not re-discover as external gap-fill):

- awesome-mbse (hub; deep Magic Grid / Cameo section; **private** as of 2026-09-18)
- awesome-sysml-v2 (Live, public)
- awesome-magic-grid (In development; Cameo practice; no GitHub repo yet)
- awesome-archimate (Live, public)
- awesome-capella (Live, public)
- awesome-requirements-engineering (private Live)
- awesome-digital-engineering (Live seed; still under ~40 bar at last inventory)
- awesome-stpa (Live, public)

User interest named explicitly: Enterprise Architect; Cameo / Magic System of Systems Architect; plus related Capella, Simulink/MathWorks, and similar domain tools.

## Findings

### SC1 — Sparx Enterprise Architect awesome list

**Finding (ESTABLISHED gap):** No credible public awesome list for Sparx Systems Enterprise Architect was found.

Evidence:

- Exact-name GitHub search `awesome-enterprise-architect` and `awesome-sparx`: `total_count` 0 (gh API, 2026-09-18).
- Fuzzy search `awesome` + enterprise architect returns unrelated lists (MCP enterprise, 1C Enterprise, social enterprise, Terraform Enterprise), not Sparx EA.
- GitHub topic `enterprise-architect`: about 49–50 public repos; a minority are clearly Sparx-related (add-ins, MDG, ReqIF). No curated awesome among them.
- Phrase search `"enterprise architect" sparx`: about 89 repos. Broader `sparxsystems|sparx-ea|ea-addin`: about 205 (noisy; includes non-EA hits).
- sindresorhus/awesome index: no MBSE / Sparx / EA modeling-tool section in available README fetch.

**Not the same as "no ecosystem."** Public add-ins exist (examples seen in search: ReqIF add-in, RAML/JSON API add-in, JHipster MDG, Sparx-EA model packs). That is thin, not Capella-scale.

### SC2 — Cameo / MagicDraw / CATIA Magic awesome list outside the family

**Finding (ESTABLISHED gap externally; family already owns the niche):** No external dedicated `awesome-cameo`, `awesome-magicdraw`, `awesome-catia-magic`, or `awesome-magic-grid` repo was found (`total_count` 0 on exact and combined name searches, gh API 2026-09-18).

Family already covers this niche:

- Hub README positions Magic Grid / Cameo / CATIA Magic as the flagship section ("deepest … coverage anywhere").
- FAMILY.md routes "Magic Grid method, Cameo / CATIA Magic how-tos" to **awesome-magic-grid** (Status: In development; Visibility: local only; no public GitHub repo yet; working copy is a hub fork pending re-scope).
- Noisy search `magicdraw|"cameo systems"|nomagic`: about 252 repos. Notable public artifacts include Cameo plugins and samples (for example Open-MBEE `exec-cameo-mdk`, GfSE SAF Cameo profile, community MCP bridges). Openable `.mdzip` gallery on the open web remains small (hub notes proprietary binary; changelog once recorded corpus growth 3 → 9).

**Conclusion:** Creating a second public `awesome-cameo` would split ownership with the planned magic-grid spoke and the hub flagship. Gap is "finish the planned spoke," not "invent a new Cameo list."

### SC3 — Capella landscape

**Finding (ESTABLISHED):** Capella already has a family spoke. Do not re-propose as net-new.

- [jgsystemsconsulting/awesome-capella](https://github.com/jgsystemsconsulting/awesome-capella): public, description "Curated Capella tool and Arcadia method resources for MBSE practitioners," family pointer in README, 0 stars / 0 forks at check time.
- Primary tool mass is open source: [eclipse-capella/capella](https://github.com/eclipse-capella/capella) (~343 stars); eclipse-capella org ~24 repos. Broader Capella/Arcadia search is large but name-collides with unrelated "Capella" projects.
- Capella is a poor analogy for proprietary tool spokes: seed research and spoke design lean on EPL tool source, public add-on catalogs, and open method materials. Sparx EA and commercial Cameo do not offer the same open gallery pattern.

No competing external `awesome-capella` incumbent was found outside the family.

### SC4 — Ranked shortlist (decision support)

Rank is **what to do next**, not "which vendor is biggest." Family bar from FAMILY.md: a spoke earns a repo only with roughly **40+** live inclusion-bar entries and no incumbent of substance.

| Rank | Candidate | Action | One-line rationale |
|------|-----------|--------|--------------------|
| 1 | **awesome-magic-grid** (Cameo / CATIA Magic practice) | **Finish existing plan** | Namespace empty externally; family already routes Cameo how-tos here; hub already deep; unfinished spoke is open maintainer debt (hub-fork + generator vs hand-TOC conflict). Highest value Cameo path without a second repo name. |
| 2 | **OpenMBEE** (platform, not one desktop tool) | **Watch / hub or DE section first** | Open-MBEE org ~150–167 public repos (MDK, MMS, sample models). Real mass. Already appears under hub Cameo samples and overlaps digital-thread routing to awesome-digital-engineering. Separate `awesome-openmbee` only after DE and magic-grid debt clear and a seed inventory clears 40+. |
| 3 | **Sparx Enterprise Architect** | **Hub section + seed inventory, not spoke yet** | No incumbent awesome list; exact name free. Ecosystem real but thin vs Capella (tens of clear Sparx repos, not hundreds of openable models). `.eap` not in hub recognized `has-model` formats. Name collides with "enterprise architecture" / awesome-archimate. Prove 40+ quality entries before any repo. Prefer name `awesome-sparx-ea` if ever spun. |
| 4 | **MathWorks Simulink / System Composer** | **Do not create family spoke** | MathWorks already publishes large awesome lists (students 742★, robotics 1714★). MBSE-specific System Composer public GitHub mass is tiny (~2 clear repos in targeted search). Scope trap: Simulink is controls/DSP/robotics first, MBSE second. |
| 5 | **Modelica / FMI** | **Neighbor only** | External incumbents exist: [ORNL-Modelica/awesome-modelica](https://github.com/ORNL-Modelica/awesome-modelica) (~29★), [traversaro/awesome-fmi](https://github.com/traversaro/awesome-fmi) (~183★). Out of family scope unless DE thread explicitly absorbs co-simulation. |

**Not ranked as new spokes:** Rhapsody, Papyrus, SysON, SCADE, Cradle, GENESYS. Either hub-tagged already with thin dedicated mass, covered by awesome-sysml-v2 (SysON), or no public awesome + weak open corpus.

### SC5 — Stay hub-only (or external neighbor)

| Tool / niche | Why hub-only or skip |
|--------------|----------------------|
| **Cameo as a second public repo name** | Duplicates hub flagship + planned magic-grid; small open `.mdzip` gallery. |
| **Sparx EA (for now)** | Empty namespace is not the 40+ bar; proprietary models; ArchiMate name collision; vendor WAF 403 on resource pages. |
| **Simulink-wide** | Vendor and community MATLAB/Simulink awesomes already dominate; not MBSE-shaped. |
| **System Composer alone** | Conceptually right for MBSE, empirically too thin on public GitHub to stock a spoke. |
| **IBM Rhapsody** | Hub already lists tool + Harmony deskbook; no awesome-*; commercial depth, thin open gallery. |
| **Eclipse Papyrus** | Hub-tagged; UAF-for-Papyrus etc. exist; mass is Eclipse modeling, not a missing awesome crisis. |
| **SysON** | Belongs with SysML v2 spoke / hub v2 tooling, not a separate vendor-tool list. |
| **Ansys SCADE / Twin Builder** | No awesome-*; little public MBSE list mass found. |
| **Modelica / FMI** | Incumbent awesomes exist; physics/co-sim neighbor, not MBSE hub core. |

### SC6 — Naming and branding landmines

| Issue | Status | Note |
|-------|--------|------|
| `awesome-enterprise-architect` | **Landmine** | Reads as enterprise-architecture (TOGAF/ArchiMate), which **awesome-archimate** already owns ("EA modeling practice"). Sparx product is also "Enterprise Architect." High confusion inside one family. |
| `awesome-ea` | **Landmine** | Fuzzy GitHub name space polluted (earth-observation and other "EA" expansions). |
| `awesome-sparx-ea` / `awesome-sparx-systems` | **Cleaner if ever needed** | Exact `awesome-sparx` was empty at check; still use product-disambiguating form. |
| `awesome-cameo` / `awesome-magicdraw` | **Empty but family-owned** | Do not take the public name until magic-grid scope is settled; avoid two Cameo homes. |
| `awesome-simulink` | **Crowded / wrong owner** | MathWorks and community MATLAB/Simulink lists already exist; family would look like a late thin duplicate. |
| Vendor trademarks (Sparx, Dassault, MathWorks) | **PROVISIONAL** | Official trademark guideline pages returned HTTP 403/404 to automated fetch this run. No quote-level ToS on third-party "awesome-*" naming. Practical risk remains: product names in third-party list titles need normal trademark attribution, not endorsement claims. |
| Vendor doc URLs | **ESTABLISHED maintenance tax** | Sparx and MathWorks sites 403 to bots; hub already maintains lychee ignore patterns for live-but-403 vendor/WAF URLs. Any Sparx/MathWorks-heavy spoke inherits chronic checker noise. |

### Ecosystem mass snapshot (gh API / topic, 2026-09-18)

Rough public GitHub scale for decisioning (noisy searches over-count; treat as order-of-magnitude):

| Ecosystem | Approx public signal | Awesome list today |
|-----------|----------------------|--------------------|
| Capella (eclipse-capella + community) | Tool 343★; org ~24 repos; large fuzzy Capella hits | **Family spoke Live** |
| Open-MBEE | Org ~150–167 repos; MDK 63★; sample models | None dedicated; fragments in hub |
| Cameo / MagicDraw / NoMagic (noisy) | ~252 repos matching keywords; topics cameo ~20, magicdraw ~27 | None external; **hub + planned magic-grid** |
| Sparx EA | Topic ~50; sparx phrase ~89; add-in-ish ~205 noisy | **None** |
| System Composer / Simulink MBSE slice | ~2 clear targeted repos | None MBSE-specific; **MATLAB/Simulink awesomes exist** (vendor) |
| Modelica / FMI | Language ecosystems large | **awesome-modelica**, **awesome-fmi** |
| Rhapsody / SCADE / Papyrus awesome-* names | Exact awesome-* 0 | Hub entries only |

### Family policy constraints that change the answer

From FAMILY.md (primary, this workspace):

1. Spoke needs ~**40+** live inclusion-bar entries; else hub section only.
2. **One canonical home** per resource; siblings link, do not copy.
3. Hub is **private** until release runbook; public spokes must not hyperlink private hub FAMILY.md.
4. awesome-magic-grid is **not** a clean niche spoke yet (local hub fork, generator vs hand-maintained TOC conflict).
5. awesome-digital-engineering was still under the 40 bar at last seed inventory (maintenance debt).
6. CONTRIBUTING recognized `has-model` formats: `.mdzip`, `.mdxml`, `.sysml`, `.uml`, Eclipse model project. **`.eap` / `.eapx` are not listed**, so Sparx openable-gallery spokes fight the bar Capella/Archi-style lists use.
7. Hub tool tags today: `Cameo`, `CATIA-Magic`, `Papyrus`, `Rhapsody`, `SysON`, `other-tool`. Sparx EA and Simulink are not first-class tags yet.

## Synthesis

**Bottom line:** The tooling-spoke idea is sound for **open ecosystems with public models and empty namespaces**. It is a weak default for **proprietary desktop tools** with binary model formats and vendor-hosted forums. Capella worked because Eclipse + Arcadia give you open source, add-ons, and linkable artifacts. Cameo is already the hub flagship and is queued as **awesome-magic-grid**, not as a missing blank. Sparx EA has a real list gap and a free exact namespace, but fails several family gates until someone proves a 40+ seed inventory and fixes the naming collision with ArchiMate "EA." Simulink does not need a family spoke; MathWorks already flooded that niche with non-MBSE awesome lists, and System Composer public mass is tiny.

**Best-placed moves (recommended order):**

1. **Ship / re-scope awesome-magic-grid** as the Cameo / Magic System of Systems Architect / CATIA Magic practice spoke. That is the correct answer to "Cameo awesome list," not a new `awesome-cameo`.
2. **Do not spin Capella again.** Point people at awesome-capella.
3. **If Sparx is strategic:** start with a **hub section** (or private seed inventory), disambiguate naming to Sparx, extend `has-model` policy only if you accept licensed-tool openability, then re-evaluate the 40 bar. Do not create the repo on empty-namespace optimism alone.
4. **OpenMBEE:** treat as platform mass for hub cross-links and possible future spoke after DE and magic-grid stabilize; do not rush `awesome-openmbee` while DE is still growing past 40.
5. **Simulink / System Composer:** hub "other-tool" pointers to MathWorks lists and a few System Composer trainings; no family awesome-simulink.
6. **Rhapsody, Papyrus, SCADE, SysON:** leave as hub (or sysml-v2) entries.

**What "exists out there" in one sentence:** Outside this family, the MBSE tool awesome niche is almost empty (sindresorhus has nothing; no Sparx/Cameo/Capella/Rhapsody awesomes found); Capella and the wider family are the main structured play; MATLAB/Simulink and Modelica/FMI already have non-MBSE or adjacent awesomes that should be treated as neighbors, not gaps to fill.

**Open provisionals (honest):**

- Vendor trademark guideline text not quote-verified (HTTP 403/404).
- Exact count of Sparx resources that would pass the family's inclusion bar is unproven (no full seed inventory this research).
- Open-MBEE public repo count reported as 150 (search) vs 167 (org page); order-of-magnitude only.
- awesome-mbse remains private; external readers still see hub 404 by design.

## Sources

| URL | Role |
|-----|------|
| https://github.com/jgsystemsconsulting/awesome-capella | Family Capella spoke (public) |
| https://github.com/jgsystemsconsulting/awesome-mbse | Family hub (private; gh API visibility) |
| https://github.com/jgsystemsconsulting | Org profile |
| https://github.com/eclipse-capella/capella | Capella OSS primary tool |
| https://github.com/Open-MBEE | OpenMBEE org / ecosystem mass |
| https://github.com/Open-MBEE/exec-cameo-mdk | Cameo MDK plugin sample |
| https://github.com/mathworks/awesome-matlab-students | Vendor MATLAB/Simulink student awesome |
| https://github.com/mathworks-robotics/awesome-matlab-robotics | Vendor MATLAB/Simulink robotics awesome |
| https://github.com/ORNL-Modelica/awesome-modelica | External Modelica awesome |
| https://github.com/traversaro/awesome-fmi | External FMI awesome |
| https://github.com/mycr0ft/awesome-sysml | External thin SysML awesome (neighbor) |
| https://github.com/sindresorhus/awesome | Meta awesome index (no MBSE section found) |
| https://github.com/topics/enterprise-architect | EA topic census |
| https://github.com/topics/magicdraw | MagicDraw topic census |
| https://github.com/topics/sysml | SysML topic census |
| https://github.com/GfSE/SAF-Cameo-Profile | Cameo public profile/samples |
| FAMILY.md (this repo) | Spoke bar, routing, registry, private mode |
| README.md (this repo) | Hub Cameo flagship, model gallery, tool entries |
| CONTRIBUTING.md (this repo) | has-model formats, tool tags |
| CHANGELOG.md (this repo) | mdzip corpus note; 403 lychee ignores |
| docs/superpowers/research/2026-09-17-awesome-capella-sources-research.md | Prior Capella OSS seed evidence |
| docs/superpowers/seed-inventory-awesome-digital-engineering.md | DE under-40 maintenance context |
| docs/superpowers/backlog.md | magic-grid re-scope already queued |
| gh API search snapshots 2026-09-18 | Exact-name totals, star counts, org sizes |

## Converged

Track 3: brief-covered after Round 2. Decision-bearing claims for SC1–SC5 are grounded in primary GitHub API/repo pages plus family primary docs. SC6 trademark prose remains PROVISIONAL (fetch blocked). No unresolved CONTRADICTED claims that block the shortlist recommendation above.
