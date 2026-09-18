# Spec: awesome-archimate, a spoke list in the awesome-mbse family

- Date: 2026-09-17
- Status: ready for plan authoring
- New repo: `jgsystemsconsulting/awesome-archimate` (public)
- Family contract: `awesome-mbse/FAMILY.md`
- Structural reference: `jgsystemsconsulting/awesome-sysml-v2`
- Research gate: `docs/superpowers/research/2026-09-17-awesome-archimate-sources-research.md`
- Context gate: `docs/superpowers/context/2026-09-17-awesome-archimate-pattern-context.md`

## Goal

Create a new public GitHub repository under jgsystemsconsulting named `awesome-archimate`, as a spoke of the awesome-mbse list family. The list owns one niche: ArchiMate, the enterprise architecture modeling language of The Open Group, the open-source Archi tool and its plugins, and enterprise architecture modeling practice around them. It follows the FAMILY.md shared standard in full and borrows repository structure and CI from the live sibling `awesome-sysml-v2`.

Brand correction locked by research: ArchiMate is a standard of The Open Group, not OMG. User-facing prose (README entries, CONTRIBUTING, CHANGELOG, SECURITY) uses Open Group branding. Machine files (LICENSE, workflow YAML, lint config) are exempt. The list carries both the ArchiMate 3.2 specification (document C226, 2022) and ArchiMate 4 (document C260, 2026).

Success at the end of this effort: the spoke repo exists with the shared-standard file set, lint CI is green, a maintainer-run lychee check on README exits 0 at launch (even though PR link CI stays advisory), at least 15 verified entries are listed in FAMILY entry format, the FAMILY registry row reads Live, and the hub README links the new spoke.

## Non-goals

- No submission to `sindresorhus/awesome` in this effort. That is FAMILY step 6, run later once the list is stable, following the submission runbook used for awesome-sysml-v2.
- No hub content moves. The hub README has no ArchiMate section today, so nothing shrinks to a pointer.
- No work on the other planned spokes (awesome-magic-grid, awesome-capella, and the rest).
- No re-hosting of content. The list links; it never copies model files or PDFs into the repo.
- No ArchiMate 4 migration material beyond linking the C260 specification. Tool support for version 4 is unverified at spec time; entries claiming 4 support need verification at execute.
- No commercial tool entries at launch unless a durable product page verifies during execute. The candidate hunt list lives in this spec only.
- No invented seeds. Every listed URL must resolve at execute time.

## Deliverable shape

- A separate GitHub repository, `jgsystemsconsulting/awesome-archimate`. Not a folder inside awesome-mbse.
- Visibility: public, matching awesome-sysml-v2. Nothing in this effort requires private content.
- Default branch: `main`.
- Local clone: sibling directory `awesome-archimate` next to the hub and awesome-sysml-v2 clones (illustrative absolute path on this machine: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-archimate`).
- File set at launch: `README.md`, `CONTRIBUTING.md`, `LICENSE` (CC0-1.0), `CODE_OF_CONDUCT.md`, `SECURITY.md`, `CHANGELOG.md`, `.markdownlint-cli2.jsonc`, and `.github/workflows/links.yml`, `lint.yml`, `stale.yml`. `CITATION.cff` and `.lycheeignore` are optional additions only if a need shows up at execute.
- Creation precondition (FAMILY step 1): recheck the GitHub namespace the same day the repo is created. Research found zero repositories named `awesome-archimate` on 2026-09-17. If an incumbent of substance appeared, stop and report instead of creating.

## Normative standard: FAMILY.md wins over sysml-v2

awesome-sysml-v2 predates parts of the family standard, so it is a structural template only. Where the two disagree, FAMILY.md wins. The new repo closes these gaps:

| Point | awesome-sysml-v2 today | FAMILY.md normative | awesome-archimate does |
|---|---|---|---|
| Contributing file name | `contributing.md` | `CONTRIBUTING.md` | `CONTRIBUTING.md` |
| Entry format | name plus description only | tags in code spans, then `(YYYY)` last | FAMILY format |
| README badges | Awesome badge only | Awesome badge plus Last full sweep badge | both |
| Family pointer | absent | required line to FAMILY.md | included |
| lychee flags | no fragment checking | `--include-fragments anchor-only` | FAMILY flags |
| Year, dedupe, neutrality rules | absent | ported from hub CONTRIBUTING.md sections 5, 6, 7 | ported; sections 5 and 6 verbatim |
| PR link-check gate | advisory (`fail: false`) | unspecified | advisory (`fail: false`), matching awesome-sysml-v2 only; hub PR lychee is blocking (`fail: true`) and is not the pattern |

## Structural borrow from awesome-sysml-v2

Port from the sibling repo, then patch per the table above:

- Three workflows: `links.yml` (weekly lychee sweep plus every PR and manual dispatch, report issue on failure), `lint.yml` (awesome-lint and markdownlint on PRs and pushes to main), `stale.yml` (monthly 24-month freshness report issue). Action references stay pinned to full-length commit SHAs.
- `lint.yml` pins `awesome-lint@2.3.0`; keep that pin exactly. Change the markdownlint globs from `contributing.md` to `CONTRIBUTING.md`.
- `links.yml` lychee args gain `--include-fragments anchor-only`, which makes CI validate that every ToC anchor resolves.
- `stale.yml` echoes a message that cites "contributing.md criterion 4"; reword it to the spoke CONTRIBUTING.md inclusion bar. Foundational-value exception (defined in spoke CONTRIBUTING, ported from hub/sysml practice): an entry may stay listed without a push in the last 24 months when it is a formal specification, certification program, or other canonical reference whose value does not depend on recent commits. The freshness report is advisory; that exception explains why stale repos can remain valid.
- `.markdownlint-cli2.jsonc` ports as-is.
- `LICENSE` is CC0-1.0, copied from the sibling or hub text.
- `CODE_OF_CONDUCT.md` and `CHANGELOG.md` port from the sibling with the repo name adjusted. `SECURITY.md` ports from the hub text: curated-list scope plus private reports to `support@jgsystemsconsulting.com`. Do not copy the sibling SECURITY.md as-is; awesome-sysml-v2 uses GitHub private vulnerability reporting only and does not list that email.

## README shape and contents

Follow the FAMILY README skeleton exactly. Header block at launch:

```markdown
# Awesome ArchiMate [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated, vetted, dated list of ArchiMate resources: Open Group specifications and
> certification, the Archi tool and its plugins, books, and openable example models.

![Last full sweep: 2026-09](https://img.shields.io/badge/last%20full%20sweep-2026--09-brightgreen)

Part of the [awesome-mbse list
family](https://github.com/jgsystemsconsulting/awesome-mbse/blob/main/FAMILY.md).

Maintained by [JG Systems Consulting Ltd.](https://github.com/jgsystemsconsulting).
See [Editorial neutrality](CONTRIBUTING.md#editorial-neutrality).
```

Launch table of contents (flat, top-level sections only):

- Specifications and standards
- Certification
- The Archi tool
- Plugins and collaboration
- Books
- Example models
- TOGAF alignment
- Communities

Deferred sections, added only once a verified entry exists: Tutorials and courses (Hosgen's course if its URL verifies, otherwise the first verified tutorial) and Commercial tools. No empty sections at launch; the ToC is built from the sections that actually ship. A Contributing section at the bottom links `CONTRIBUTING.md`.

## Entry format and tag vocabulary

FAMILY normative format, with this list's tag values:

```
- [Resource Name](https://example.com) - One-line factual description `ArchiMate3` `Archi` `has-model` `tutorial` (2024).
```

Description at most 140 characters, measured as hub CONTRIBUTING.md section 3 defines. Hyphen separator (` - `), never an en or em dash; awesome-lint rejects those. Tags are inline code spans before the year token, in the fixed axis order. Year in parentheses is a terminal suffix after the tags, not a code-span tag.

Tag axis order (code spans only): `language` -> `method` -> `tool` -> `has-model` -> `type` -> `spec/standard` -> `paid`. Then the year suffix `(YYYY)`.

| Axis | Cardinality | Values for this list |
|------|-------------|----------------------|
| language | exactly 1 | `ArchiMate3` (3.x, including 3.2) / `ArchiMate4` / `ArchiMate-general` (version-agnostic) |
| method | 0 or 1 | `TOGAF` |
| tool | 0 or more | `Archi` / `other-tool` (graduates to its own tag once 3 or more entries share it) |
| has-model | 0 or 1 | `has-model`: the linked page is a direct file download, or a repository/collection whose documented contents include at least one downloadable `.archimate` or ArchiMate Exchange Format model that opens in a named tool |
| type | 0 or 1 | `tutorial` / `course` / `book` / `paper` / `blog` / `docs` / `video` / `tool` / `plugin` / `certification` / `example` / `community` / `mcp`. Required unless `spec` or `standard` is present (hub practice: pure specification rows carry language plus `spec`/`standard` only) |
| spec/standard | 0 or 1 | `spec` / `standard` |
| paid | 0 or 1 | `paid` |
| year (suffix) | exactly 1 | `(YYYY)` after tags; not a code span |

Type value notes: `certification` marks a certification program or registry page, `example` marks a collection or repository of example models, `community` marks a forum or community hub, `docs` marks a wiki or documentation home (not a single blog post). The remaining values follow hub usage.

Format examples (year values illustrative; final values follow hub CONTRIBUTING.md section 5 at execute):

- [ArchiMate 3.2 Specification](https://publications.opengroup.org/c226) - The Open Group standard defining the ArchiMate 3.2 modeling language, document C226 `ArchiMate3` `spec` (2022).
- [jArchi](https://github.com/archimatetool/archi-scripting-plugin) - Scripting plugin for Archi that automates model queries and content generation with JavaScript `ArchiMate-general` `Archi` `plugin` (2025).

## Seed entry set

18 candidates from the research gate. Link-check at execute may trim; the minimum to open the list is 15 live entries. The Year basis column states what sets `(YYYY)`; final values are picked at execute under the hub year rule. One-line descriptions are written at execute from the research gate's role notes.

| Section | Entry | URL | Tags | Year basis |
|---|---|---|---|---|
| Specifications and standards | ArchiMate 3.2 Specification | https://publications.opengroup.org/c226 | `ArchiMate3` `spec` | known: 2022 |
| Specifications and standards | ArchiMate 4 Specification | https://publications.opengroup.org/c260 | `ArchiMate4` `spec` | known: 2026 |
| Specifications and standards | ArchiMate Model Exchange File Format | https://www.opengroup.org/open-group-archimate-model-exchange-file-format | `ArchiMate-general` `spec` | page date |
| Certification | ArchiMate Certification | https://www.opengroup.org/certifications/archimate | `ArchiMate-general` `certification` | page date |
| Certification | ArchiMate Tool Certification | https://www.opengroup.org/certifications/archimate/tools | `ArchiMate-general` `certification` | page date |
| The Archi tool | Archi | https://github.com/archimatetool/archi | `ArchiMate3` `Archi` `tool` | latest tagged release |
| The Archi tool | Archi Wiki | https://github.com/archimatetool/archi/wiki | `ArchiMate-general` `Archi` `docs` | latest edit |
| Plugins and collaboration | Archi plugins | https://www.archimatetool.com/plugins/ | `ArchiMate-general` `Archi` `plugin` | page date |
| Plugins and collaboration | jArchi | https://github.com/archimatetool/archi-scripting-plugin | `ArchiMate-general` `Archi` `plugin` | latest tagged release |
| Plugins and collaboration | coArchi | https://github.com/archimatetool/archi-modelrepository-plugin | `ArchiMate-general` `Archi` `plugin` | latest tagged release |
| Plugins and collaboration | coArchi 2 | https://github.com/archimatetool/archi-modelrepository-plugin2 | `ArchiMate-general` `Archi` `plugin` | latest tagged release |
| Books | Mastering ArchiMate (Gerben Wierda) | https://ea.rna.nl/ | `ArchiMate3` `book` | Edition 3.2 publication year |
| Example models | ArchiModels (archived) | https://github.com/archimatetool/ArchiModels | `ArchiMate3` `Archi` `has-model` `example` | last push |
| Example models | ArchiSurance Practice | https://github.com/yasenstar/ArchiSurance_Practice | `ArchiMate3` `Archi` `has-model` `example` | last push |
| Example models | ArchiSurance (archimate-models) | https://github.com/archimate-models/archisurance | `ArchiMate3` `Archi` `has-model` `example` | last push |
| Communities | Archi forum | https://forum.archimatetool.com/ | `ArchiMate-general` `Archi` `community` | current activity year |
| Communities | Open Group ArchiMate User Community | https://community.opengroup.org/archimate-user-community | `ArchiMate-general` `community` | page date |
| TOGAF alignment | TOGAF | https://www.opengroup.org/togaf | `ArchiMate-general` `TOGAF` `standard` | page date |

Provisional items:

- Marc Hosgen's video course: research could not confirm a stable URL. Include it under Tutorials and courses only if a live URL verifies at execute; otherwise omit both the entry and the section. Do not seed it from a search-engine guess.
- The Open Group ArchiMate User Community page was flagged as possibly bot-gated during research. Verify it is browsable at execute; drop the entry if not.
- ArchiModels is archived upstream; keep it with "archived" in the description, since the collection still has reference value and the link resolves.
- The `archimatetool.com` home page is not a separate entry; the repo root is the canonical Archi entry, matching the sibling list's convention.

## Growth path to the 40-entry bar

FAMILY step 2 asks for roughly 40 candidate entries before creation. **Waiver for this launch (2026-09-17):** open with 18 verified seeds (minimum 15 live after link-check), not 40 pre-verified candidates. Rationale: namespace is empty, research shows the surface is reachable, and the depth bar is maintainer policy without CI. Owner: spoke maintainer. The ~40 bar remains the target for the first full sweep logged in CHANGELOG, not a create blocker.

Growth buckets to fill in the first sweeps, each entry verified before listing:

- Commercial EA tools with ArchiMate support: Bizzdesign, Sparx Enterprise Architect, Software AG ARIS, LeanIX, MEGA HOPEX, Orbus iServer, Visual Paradigm. Durable product pages only; `other-tool` until 3 or more entries share a tool tag.
- Tutorials and courses: Hosgen's course, Open Group training pages, vendor tutorials.
- jArchi script collections and model exchange tooling: importers, exporters, validators for the exchange format.
- Open Group and academic papers on ArchiMate practice, viewpoints, and use with TOGAF.
- More community models from the User Community and GitHub.

## Hub updates in the same effort

FAMILY step 5 runs in this effort. Step 6 (sindresorhus submission) does not.

- FAMILY.md registry: flip the awesome-archimate row Status from `Planned. Namespace empty as of 2026-09` to `Live` and add the repo link. Update scope text to: "ArchiMate 3.x and 4, the Archi tool, EA modeling practice" so the registry matches listing C226 and C260. Boundary table row for ArchiMate may keep the shorter "ArchiMate viewpoints, the Archi tool, TOGAF-aligned modeling" wording.
- Hub README: the "List family" paragraph currently points only to FAMILY.md. The FAMILY model section says the hub README links every spoke near the top. Add a sentence there naming the live spokes with links: awesome-sysml-v2 and awesome-archimate.
- Hub `CHANGELOG.md`: add an entry for the family update (registry flip plus README pointer).
- Hub content shrink: not needed. The hub carries no ArchiMate section today. Its UAF and DoDAF framework entries stay hub-side; TOGAF alignment for ArchiMate lives in the spoke per the scope boundary.

## Editorial neutrality for this niche

Hub CONTRIBUTING.md section 7 is adapted, not copied blind. Research did not establish that JG Systems Consulting sells an ArchiMate-niche product. The spoke CONTRIBUTING.md states the current position: JGS products fall under the same inclusion bar as everything else; today JGS lists no ArchiMate-niche product; if that changes, every JGS entry sits next to at least one competing entry and a superior competitor ranks above it. Do not invent a JGS product entry to make the disclosure concrete.

## Acceptance criteria

- [ ] Namespace rechecked on creation day; still no incumbent before `gh repo create`.
- [ ] Repo `jgsystemsconsulting/awesome-archimate` exists, public, default branch `main`.
- [ ] Local clone exists as sibling `awesome-archimate` next to the hub clone (path may vary by machine).
- [ ] Shared-standard file set present: README.md, CONTRIBUTING.md, LICENSE (CC0-1.0), CODE_OF_CONDUCT.md, SECURITY.md (hub-style support@ contact), CHANGELOG.md, `.markdownlint-cli2.jsonc`.
- [ ] README follows the family skeleton: Awesome badge, one-line scope, Last full sweep badge (2026-09), family pointer, maintainer line, flat ToC built only from sections that ship entries, contributing section. No empty sections.
- [ ] The string "OMG ArchiMate" appears nowhere in user-facing prose; Open Group branding in README/CONTRIBUTING/CHANGELOG/SECURITY; both 3.2 (C226) and 4 (C260) listed.
- [ ] Every entry matches FAMILY format: hyphen separator, description 140 characters or fewer, required language tag, type unless `spec`/`standard` present, tags in axis order, year suffix last.
- [ ] At least 15 entries at open whose URLs return success on a maintainer-run lychee of README at launch; the Hosgen entry present only if its URL verified.
- [ ] CONTRIBUTING.md contains inclusion bar, foundational-value exception text, hub year rule and canonical-URL rule verbatim, adapted neutrality, and the spoke tag table (including type-optional-when-spec rule and `docs` type).
- [ ] CI: three workflows on main with full-length SHA pins; `links.yml` lychee args include `--include-fragments anchor-only` and PR `fail: false`; `lint.yml` pins `awesome-lint@2.3.0` and globs README.md and CONTRIBUTING.md; `stale.yml` cites spoke inclusion bar and foundational-value exception.
- [ ] `npx awesome-lint@2.3.0 README.md` passes; `npx markdownlint-cli2 "README.md" "CONTRIBUTING.md"` passes.
- [ ] Maintainer launch lychee exits 0 on README (ship gate). Ongoing PR link CI may remain advisory.
- [ ] FAMILY.md registry row reads Live with the repo link and scope text "ArchiMate 3.x and 4, the Archi tool, EA modeling practice".
- [ ] Hub README links the new spoke near the family paragraph.
- [ ] Both CHANGELOG.md files carry launch entries.

## Open questions

None blocking. Two provisional items resolve at execute: the Hosgen URL (include only if verified) and the Open Group User Community page (drop if bot-gated beyond use).

## Research

Gate: `docs/superpowers/research/2026-09-17-awesome-archimate-sources-research.md`, retrieved 2026-09-17. Key verified sources:

- https://publications.opengroup.org/c226 - ArchiMate 3.2 Specification, document C226, published 2022-10-19.
- https://publications.opengroup.org/c260 - ArchiMate 4 Specification, document C260, published 2026-04-27.
- https://www.opengroup.org/certifications/archimate - personal certification program (Foundation, Practitioner).
- https://www.opengroup.org/open-group-archimate-model-exchange-file-format - model exchange file format.
- https://www.archimatetool.com/ - Archi tool home; site states ArchiMate 3.2 support.
- https://github.com/archimatetool/archi - Archi source, MIT licensed.
- https://github.com/archimatetool/ArchiModels - archived example model collection, succeeded by https://community.opengroup.org/archimate-user-community.
- https://ea.rna.nl/ - Gerben Wierda, Mastering ArchiMate Edition 3.2 and free overview PDFs.
- https://www.opengroup.org/togaf - TOGAF hub, cites ArchiMate 3.2.
- https://github.com/search?q=awesome-archimate&type=repositories - namespace check, 0 results on 2026-09-17.

Corrections carried into this spec: The Open Group owns ArchiMate (not OMG), and both version 3.2 and version 4 are listed. Marc Hosgen's course URL is unconfirmed and stays conditional.

## Codebase context

Gate: `docs/superpowers/context/2026-09-17-awesome-archimate-pattern-context.md`. Findings this spec builds on:

- FAMILY.md is the normative shared standard: badges, entry format with tags and year, required files, CI with anchor-only fragment checking, quarterly sweep cadence.
- awesome-sysml-v2 is a partial template: three workflows, `awesome-lint@2.3.0`, CC0 license, but lowercase `contributing.md`, no tags or years, no sweep badge, no family pointer, no fragment check, advisory link check.
- The registry already lists awesome-archimate as Planned with an empty-namespace note; the scope boundary routes ArchiMate viewpoints, the Archi tool, and TOGAF-aligned modeling to this spoke.
- The hub README links only FAMILY.md today; per-spoke links are part of launch step 5.
- The depth bar (roughly 40 entries, no incumbent) is maintainer policy, not CI.
