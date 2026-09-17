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

## Registry

| Repo | Owns | Status |
|------|------|--------|
| [awesome-mbse](https://github.com/jgsystemsconsulting/awesome-mbse) | Hub. Cross-cutting MBSE: methods, tool landscape, openable models, Magic Grid / Cameo | Live |
| [awesome-sysml-v2](https://github.com/jgsystemsconsulting/awesome-sysml-v2) | SysML v2 the language: spec, parsers, editors, API clients, example models | Live |
| awesome-magic-grid | Magic Grid method and Cameo practice, split out of the hub | In development |
| awesome-archimate | ArchiMate 3.x, the Archi tool, EA modeling practice | Planned. Namespace empty as of 2026-09 |
| awesome-capella | Capella tool and the Arcadia method | Planned. Namespace empty as of 2026-09 |
| awesome-requirements-engineering | Requirements as a discipline: EARS, KAOS, ReqIF, tooling, papers | Planned. Namespace empty as of 2026-09 |
| awesome-digital-engineering | Digital thread, model-based definition, digital engineering transformation | Planned. Namespace empty as of 2026-09 |
| awesome-stpa | STAMP / STPA and hazard analysis; functional safety methods | Planned. Namespace empty as of 2026-09 |

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
