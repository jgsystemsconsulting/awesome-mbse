# Research: awesome-archimate canonical sources

## Research brief

**Primary question:** What durable official and community URLs, versions, and resources should seed an `awesome-archimate` curated list (ArchiMate 3.x, Archi tool, EA modeling practice)?

**Sub-questions:**
1. Spec & certification: ArchiMate 3.2 (Open Group / OMG relationship), Open Group certification, TOGAF alignment pages
2. Tools: Archi (archimatetool) official site, GitHub org/repos, plugins, model collaboration/repos
3. Learning: Marc Høsgen video course, Gerben Wierda Mastering ArchiMate, other high-signal tutorials
4. Example models: Archi official collection and other open models
5. Incumbent awesome lists / namespace collision on GitHub for `awesome-archimate` or close names
6. Enough depth (~40 candidate entry types) to justify a spoke per FAMILY.md bar

**Success criteria:**
- R1: Canonical https URLs for ArchiMate 3.2 spec and related Open Group pages with version identity
- R2: Canonical Archi tool home, GitHub, and plugin/extension discovery paths
- R3: Confirmed links for Høsgen tutorials and Wierda Mastering ArchiMate (edition/year if findable)
- R4: Example model collection URLs
- R5: Namespace check result for awesome-archimate / similar lists
- R6: TOGAF–ArchiMate relationship primary page(s)

**Out of scope:** Writing list prose; hub FAMILY edits; commercial tool sales copy without a durable product page.

**Budget:** light tier. Retrieved_at: 2026-09-17.

## Findings

### Spec and Open Group identity (R1)

- ArchiMate is a standard of **The Open Group**, not OMG. Spec store titles: "ArchiMate® 3.2 Specification" and "ArchiMate® 4 Specification".
- ArchiMate 3.2: document C226, published 2022-10-19, https://publications.opengroup.org/c226
- ArchiMate 4: document C260, published 2026-04-27, https://publications.opengroup.org/c260 (supersedes 3.2 path in the catalog narrative)
- Personal certification (Foundation/Practitioner, program covers 3.2): https://www.opengroup.org/certifications/archimate
- Tool certification: https://www.opengroup.org/certifications/archimate/tools
- Model Exchange File Format: https://www.opengroup.org/open-group-archimate-model-exchange-file-format

### Archi tool and plugins (R2)

- Home: https://www.archimatetool.com/ — title "Open Source ArchiMate Modelling"; site states support for ArchiMate 3.2 and alignment with TOGAF / Open Group.
- Source: https://github.com/archimatetool/archi (MIT, 1271 stars as of 2026-09-17 via GitHub API)
- Plugins hub: https://www.archimatetool.com/plugins/
- jArchi: https://github.com/archimatetool/archi-scripting-plugin
- coArchi: https://github.com/archimatetool/archi-modelrepository-plugin
- coArchi2: https://github.com/archimatetool/archi-modelrepository-plugin2
- Forum: https://forum.archimatetool.com/
- Wiki: https://github.com/archimatetool/archi/wiki

### Learning (R3)

- Gerben Wierda site https://ea.rna.nl/ (masteringarchimate.com 301s here). Site surfaces **Mastering ArchiMate – Edition 3.2** and free ArchiMate 3.2 overview PDFs. Treat ea.rna.nl as the durable author home; exact shop SKU URL may move under that domain.
- Marc Høsgen video course: **not confirmed** in this research window (search engines challenge-walled; no stable primary URL locked). Spec/plan must list it as a seed candidate only if a live URL is verified at execute time, or omit until verified.

### Example models (R4)

- Official historical collection https://github.com/archimatetool/ArchiModels (170 stars) is **archived**; README redirects maintainers to Open Group ArchiMate User Community: https://community.opengroup.org/archimate-user-community
- Community ArchiSurance practice models remain useful seeds, e.g. https://github.com/yasenstar/ArchiSurance_Practice (57 stars), https://github.com/archimate-models/archisurance (34 stars)
- Exchange format examples referenced from Open Group exchange page (xsd/archimate resources)

### Namespace (R5)

- GitHub search `awesome-archimate`: **0** repositories (2026-09-17, `gh api search/repositories`)
- `jgsystemsconsulting/awesome-archimate` does not exist yet
- No incumbent list of substance under that name; FAMILY empty-namespace claim holds on recheck

### TOGAF relationship (R6)

- Archi site states ArchiMate is hosted by The Open Group and fully aligned with TOGAF
- Open Group TOGAF hub https://www.opengroup.org/togaf links ArchiMate certification and cites ArchiMate 3.2 Specification in page content
- TOGAF certification portfolio: https://www.opengroup.org/certifications/togaf (redirects into certification portfolio path)

### Depth note

Seed surface already includes specs (2+), cert (2), exchange format, Archi + plugins (5+), forum/wiki, model collections (3+), books/overviews, TOGAF hubs, community models, and room for commercial EA tools with ArchiMate support. Spoke depth bar is reachable without inventing entries.

## Synthesis

**Use Open Group branding everywhere; do not label the language "OMG ArchiMate".** List both 3.2 (current tool support on Archi site) and 4 (latest Open Group specification) under Specifications.

**Canonical tool spine:** archimatetool.com + github.com/archimatetool/{archi, archi-scripting-plugin, archi-modelrepository-plugin, archi-modelrepository-plugin2, ArchiModels}.

**Models:** prefer User Community + live community models; mark ArchiModels as archived historical.

**Wierda:** Mastering ArchiMate Edition 3.2 via ea.rna.nl. **Høsgen:** verify URL at execute or drop.

**Namespace clear** for creating `jgsystemsconsulting/awesome-archimate`.

**Provisional:** Høsgen URL; exact Wierda purchase deep-link; bot-gated ArchiMate User Community browse contents.

## Sources

| URL | Role |
|-----|------|
| https://publications.opengroup.org/c226 | ArchiMate 3.2 spec C226 |
| https://publications.opengroup.org/c260 | ArchiMate 4 spec C260 |
| https://www.opengroup.org/certifications/archimate | Personal certification |
| https://www.opengroup.org/certifications/archimate/tools | Tool certification |
| https://www.opengroup.org/open-group-archimate-model-exchange-file-format | Exchange file format |
| https://www.opengroup.org/togaf | TOGAF hub (ArchiMate mentions) |
| https://www.opengroup.org/certifications/togaf | TOGAF cert portfolio entry |
| https://www.archimatetool.com/ | Archi home |
| https://www.archimatetool.com/plugins/ | Plugins |
| https://github.com/archimatetool/archi | Archi source |
| https://github.com/archimatetool/archi-scripting-plugin | jArchi |
| https://github.com/archimatetool/archi-modelrepository-plugin | coArchi |
| https://github.com/archimatetool/archi-modelrepository-plugin2 | coArchi2 |
| https://github.com/archimatetool/ArchiModels | Archived example models |
| https://github.com/archimatetool/archi/wiki | Archi wiki |
| https://forum.archimatetool.com/ | Forum |
| https://community.opengroup.org/archimate-user-community | User community (models successor) |
| https://ea.rna.nl/ | Wierda / Mastering ArchiMate 3.2 |
| https://github.com/yasenstar/ArchiSurance_Practice | Community ArchiSurance practice |
| https://github.com/archimate-models/archisurance | Community ArchiSurance |
| https://github.com/search?q=awesome-archimate&type=repositories | Namespace check |
