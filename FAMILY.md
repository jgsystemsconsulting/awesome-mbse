# The awesome-mbse list family

This repository is the hub of a family of curated lists, each owning one niche of the
systems-engineering modeling world. This file defines how the family works: who owns
what, the standard every list follows, and the steps for adding the next one. It is
written for the maintainer starting a new list; a contributor to one list only needs
that list's CONTRIBUTING.md.

## Model

One hub, many spokes.

- **awesome-mbse (the hub):** the broad MBSE index, organized by modeling language,
  with the deepest Magic Grid / Cameo / CATIA Magic coverage anywhere. The hub keeps
  general and cross-cutting material: methodology comparisons, multi-language books and
  courses, tool landscapes, and openable models that span languages. The hub README
  links every spoke near the top.
- **Spokes:** one niche each, covered deeper than the hub would ever carry it.

Two rules hold across the family:

1. **One canonical home per resource.** Route by primary subject (table below). A
   sibling list may link to the canonical entry, but never copy the entry text.
2. **A spoke earns its repo only when** the niche has enough live resources to sustain
   roughly 40+ entries and no incumbent list of substance (checked on GitHub first).
   Below that, the hub carries the niche in a section.

When a spoke splits out of the hub, the hub's section for that niche shrinks to a short
pointer plus the few entries that are genuinely cross-cutting.

## Private mode

The default state of every family repo is private until it is explicitly released.

- Entry links still pass the public-availability inclusion bar. A private repo linking
  private resources violates the bar all the same; the CHANGELOG 2026-06 removal of
  jgs-magic-sysmlv2-mcp is the precedent.
- While the hub is private, public spokes reference the family in text only. No
  FAMILY.md hyperlinks from public repos: they 404 for outside readers.
- The `sindresorhus/awesome` submission step is deferred to the future public-release
  runbook; it is not part of private-structure work.
- Sweep badges, CI, and cadence are unchanged by privacy.

## Registry

| Repo | Owns | Status | Visibility |
|------|------|--------|------------|
| [awesome-mbse](https://github.com/jgsystemsconsulting/awesome-mbse) | Hub. Cross-cutting MBSE: methods, tool landscape, openable models, Magic Grid / Cameo | Live | private |
| [awesome-sysml-v2](https://github.com/jgsystemsconsulting/awesome-sysml-v2) | SysML v2 the language: spec, parsers, editors, API clients, example models | Live | public |
| awesome-magic-grid | Magic Grid method and Cameo practice | In development | local only. No GitHub repo exists; the local working copy is a hub fork pending re-scope, not a niche spoke |
| [awesome-archimate](https://github.com/jgsystemsconsulting/awesome-archimate) | ArchiMate 3.x and 4, the Archi tool, EA modeling practice | Live | public |
| [awesome-capella](https://github.com/jgsystemsconsulting/awesome-capella) | Capella tool and the Arcadia method | Live | public |
| awesome-requirements-engineering | Requirements as a discipline: EARS, KAOS, ReqIF, tooling, papers | Live | private |
| [awesome-digital-engineering](https://github.com/jgsystemsconsulting/awesome-digital-engineering) | Digital thread, model-based definition, digital engineering transformation | Live | public |
| awesome-stpa | STAMP / STPA and hazard analysis; functional safety methods | Planned | none yet |

Status is only `Live` | `In development` | `Planned`. Visibility is only `public` |
`private` | `local only` | `none yet`, and never appears inside Status cells. Namespace
check dates live in the namespace table under External lists and namespaces.

Do not add a registry row until the GitHub namespace has been checked again that day.
Update the Status column when a repo goes live.

## Scope boundaries

Route a resource by its primary subject:

| Primary subject | Home |
|-----------------|------|
| SysML v2 syntax, parsers, editors, the v2 API | awesome-sysml-v2 |
| Magic Grid method, Cameo / CATIA Magic how-tos | awesome-magic-grid |
| ArchiMate viewpoints, the Archi tool, TOGAF-aligned modeling | awesome-archimate |
| Capella workbenches, Arcadia method material | awesome-capella |
| Requirements elicitation and management as its own discipline | awesome-requirements-engineering |
| Digital thread, MBD, digital engineering policy and standards | awesome-digital-engineering |
| STAMP / STPA, hazard analysis, functional safety standards | awesome-stpa |
| MBSE in general: methodology surveys, language-agnostic books, tool roundups | awesome-mbse (hub) |

Borderline cases (a SysML v2 paper that applies Magic Grid, an ArchiMate model of a
SysML system) go to the list whose reader would search for the resource by its main
claim, and get a cross-link from the other.

## External lists and namespaces

External lists cover adjacent ground. They are neighbors and competitors, not family.

| List | Coverage note | Last checked |
|------|---------------|--------------|
| [mycr0ft/awesome-sysml](https://github.com/mycr0ft/awesome-sysml) | SysML v2 textual tooling; thin on Magic Grid and openable Cameo models | 2026-06 |
| [kktse/awesome-systems-engineering](https://github.com/kktse/awesome-systems-engineering) | Broad systems-engineering links; no MBSE depth; untouched since 2021 | 2026-06 |
| [rolling-robot/awesome-systems-engineering](https://github.com/rolling-robot/awesome-systems-engineering) | Minimal systems-engineering collection; no MBSE coverage; stagnant since 2024 | 2026-06 |

Namespace checks for the planned spokes. Result vocabulary: `empty` | `incumbent
found` | `TODO re-check`.

| Name | Checked | Result | Next action |
|------|---------|--------|-------------|
| awesome-archimate | 2026-09-17 (create-day re-check: empty) | empty | None; repo created |
| awesome-capella | 2026-09-17 | empty | Live as jgsystemsconsulting/awesome-capella |
| awesome-stpa | - | TODO re-check | Re-check on launch day (rate-limited on the 2026-09-17 list-family pass) |
| awesome-requirements-engineering | 2026-06 | empty | Re-check on create day (niche research: namespace free or thin incumbents) |
| awesome-digital-engineering | 2026-06 | empty | Re-check on create day (niche research: namespace free or thin incumbents) |

## Shared standard

Every family repo has, without exception:

- **README.md** with the Awesome badge, a one-line scope statement, the *Last full
  sweep* badge, a family pointer line, and a flat hand-maintained table of contents
  (top-level sections only).
- **Entry format:** `- [Resource Name](url) - One-line factual description `tags` (YYYY).`
  Hyphen separator (never an en/em dash), description at most 140 characters, tags as
  inline code spans before the terminal period, year in parentheses as the last token.
- **Inclusion bar:** on-topic, substantive (not a stub, not pure vendor marketing),
  live, not duplicative, legally linkable. We link, we never re-host content.
- **Tag vocabulary:** the same axes as awesome-mbse (language, method, tool,
  has-model, type, spec/standard, paid, year) with per-list values. Keep the
  cardinality and ordering rules; define the values in each list's CONTRIBUTING.md.
- **Year rule and canonical-URL dedupe rule** as written in the hub CONTRIBUTING.md
  (sections 5 and 6). Copy them verbatim into each spoke's CONTRIBUTING.md.
- **Editorial neutrality:** the maintainer disclosure and the
  competing-entry-alongside rule, adapted to whatever products JG Systems Consulting
  sells into that niche (or stated as not applicable).
- **Files:** LICENSE (CC0-1.0), CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md,
  CHANGELOG.md.
- **CI:** link check on every PR plus a scheduled sweep (lychee with
  `--include-fragments anchor-only`), markdown lint, awesome-lint.
- **Cadence:** quarterly sweep, logged in CHANGELOG.md, *Last full sweep* badge
  updated. Over six months without a sweep, the badge says maintenance lapsed.

## Starting a new list

1. Check the namespace: search GitHub for `awesome-<niche>`. A live incumbent (roughly
   100+ stars or updated in the last year) means do not build; differentiate or stop.
2. Confirm depth: gather roughly 40 candidate entries that pass the inclusion bar
   before creating anything.
3. Create the repo from the skeleton below, adapt the tag vocabulary values to the
   niche, and port the year, dedupe, and neutrality rules from the hub CONTRIBUTING.md.
4. Populate, link-check, and turn on CI.
5. Add the registry row here and the spoke link in the hub README.
6. When the list is stable, submit it to `sindresorhus/awesome` following the
   submission runbook used for awesome-sysml-v2.

### Per-spoke create checklist template

Copy per planned spoke. The checklists are the structure; do not create the repo first.

- [ ] Namespace re-checked on YYYY-MM-DD (result: empty / incumbent found)
- [ ] Roughly 40 candidate entries gathered, all passing the inclusion bar
- [ ] Repo created (private) from the README skeleton
- [ ] Hub README family table row updated with the URL
- [ ] Registry status flipped to Live

### awesome-archimate

Live. Hub GAP: no dedicated ArchiMate section. Namespace empty on 2026-09-17 and on
the create-day re-check. Launched with 17 verified seeds under the depth waiver
(2026-09-17, owner: spoke maintainer); the ~40-entry bar is the target for the first
full sweep, logged in the spoke CHANGELOG.

- [x] Namespace re-checked on 2026-09-17 (result: empty)
- [x] Depth waiver applied: opened with 17 verified seeds (minimum 15 live) per the 2026-09-17 waiver
- [x] Repo created (public, matching awesome-sysml-v2) from the README skeleton
- [x] Hub README family table row updated with the URL
- [x] Registry status flipped to Live

### awesome-capella

Live. Public spoke at https://github.com/jgsystemsconsulting/awesome-capella (73 verified
entries, 2026-09-17). Hub Capella/Arcadia section shrunk to a pointer plus cross-cutting
entries. Namespace re-check empty on create day.

- [x] Namespace re-checked on 2026-09-17 (result: empty)
- [x] Roughly 40 candidate entries gathered, all passing the inclusion bar (73 shipped)
- [x] Repo created (public, per reviewed spec M1) from the README skeleton
- [x] Hub README family table row updated with the URL
- [x] Registry status flipped to Live

### awesome-requirements-engineering

Live. Private spoke created and populated 2026-09-17 (40 entries). Hub still has no
RE resource section (GAP closed by spoke status, not by hub body copy). Public release
and sindresorhus/awesome submission are later steps.

- [x] Namespace re-checked on 2026-09-17 (result: empty)
- [x] Roughly 40 candidate entries gathered, all passing the inclusion bar
- [x] Repo created (private) from the README skeleton
- [x] Hub README family table row updated with the URL
- [x] Registry status flipped to Live

### awesome-digital-engineering

Live. Public spoke at https://github.com/jgsystemsconsulting/awesome-digital-engineering
(launched 2026-09-17, initial seed under 40 with honest growth label). Hub still has no
DE resource section (GAP closed by spoke, not by hub content).

- [x] Namespace re-checked on 2026-09-17 (result: empty)
- [ ] Roughly 40 candidate entries gathered, all passing the inclusion bar (growth in progress)
- [x] Repo created (public) from the README skeleton
- [x] Hub README family table row updated with the URL
- [x] Registry status flipped to Live

### awesome-stpa

Planned. Hub carries one STPA entry: the Model Gallery DLR-FT STPA library. Namespace
TODO re-check (rate-limited on the 2026-09-17 list-family pass).

- [ ] Namespace re-checked on YYYY-MM-DD (result: empty / incumbent found)
- [ ] Roughly 40 candidate entries gathered, all passing the inclusion bar
- [ ] Repo created (private) from the README skeleton
- [ ] Hub README family table row updated with the URL
- [ ] Registry status flipped to Live

### awesome-magic-grid status note

The local working copy runs a generator pipeline (`scripts/generate.py` over
`data/entries.yaml`) while the family standard mandates a hand-maintained table of
contents. That conflict is surfaced, not solved: it is tracked in
`../awesome-magic-grid/STATUS.md`. Re-scope (prune entries, retitle, decide generator
versus hand maintenance) is a TODO.

### awesome-sysml-v2 live-spoke alignment

Not a create checklist: the repo exists and is public. Alignment with the family
standard, checked on each sweep.

- [ ] Family pointer line present (text only while hub private)
- [ ] Last full sweep badge
- [ ] Entry tags and year tokens per family standard
- [ ] CONTRIBUTING year/dedupe/neutrality rules aligned

## README skeleton

```markdown
# Awesome <Niche> [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> One-line scope statement: what this list covers and who it is for.

![Last full sweep: YYYY-MM](https://img.shields.io/badge/last%20full%20sweep-YYYY--MM-brightgreen)

Part of the [awesome-mbse list
family](https://github.com/jgsystemsconsulting/awesome-mbse/blob/main/FAMILY.md).

Maintained by [JG Systems Consulting Ltd.](https://github.com/jgsystemsconsulting).
See [Editorial neutrality](CONTRIBUTING.md#editorial-neutrality).

## Contents

- [Section one](#section-one)

## Section one

- [Resource Name](https://example.com) - One-line factual description `tag` (2024).
```
