# Design: Generator-driven `awesome-mbse`, restructured by language

**Date:** 2026-06-24
**Status:** Approved (brainstorming) — ready for implementation plan
**Repo:** `awesome-mbse` (formerly awesome-magic-grid)

## Problem

The list categorises content along two mixed axes — *resource type* (methodology /
tutorials / courses / books / models / tools / communities) nested under two *scope
buckets* (Magic Grid–Cameo flagship vs. Broader SysML/MBSE context). Rich inline tags
exist (`SysMLv1`, `SysMLv2`, `MagicGrid`, `Cameo`, `has-model`, `paper`, `tool`…) but
they are decorative: there is no way to navigate *by* them.

A reader who thinks "I model in SysML v2 — show me everything for it" or "I just want
an openable model" or "what here runs in Cameo?" cannot get there. The goal is to make
the list both **navigable by modelling language** and **self-explaining about which
notation fits whom**, plus expose the tags as real navigation.

## Decisions (from brainstorming)

1. **Primary navigation axis:** modelling language / notation.
2. **Change scope:** full restructure of the README around language (not just an added
   index layer).
3. **Spine buckets:** one section per notation, with thin notations grouped.
4. **Cross-cutting content:** a shared "language-general" section *after* the language
   buckets.
5. **Model Gallery:** dissolved from the spine — each language bucket carries its own
   `Example models`; a cross-language openable-models *view* is restored as a generated
   index (decision 7).
6. **Source of truth:** a structured data file. The generator emits the README body and
   the views from it.
7. **Generated cross-views (all four):** openable-models index, tool index,
   resource-type index, and a tag legend.

## Architecture

The README stops being hand-edited and becomes a **build artifact**. Three new pieces:

```
data/entries.yaml        # single source of truth — every link lives here
README.template.md       # narrative prose + {{placeholders}} for generated blocks
scripts/generate.py      # entries.yaml + template -> README.md  (--check mode for CI)
```

`README.md` stays committed (GitHub renders it) but is regenerated, never hand-edited.
Narrative prose (intros, the competitive-landscape narrative, section blurbs, maintainer
note) lives in `README.template.md` as real markdown. Only the *mechanical* parts —
entry lists, Contents, the four views, and entry anchors — are filled by the generator.
This satisfies "generate the body" without burying paragraphs in YAML.

**Generator language:** Python (cleanest YAML→markdown transform; stdlib + one yaml
dependency). The repo's CI already uses Node for awesome-lint; Python adds one runtime in
one CI job. (If single-runtime is later preferred, a Node port is acceptable — same
design.)

## Data model — `data/entries.yaml`

Each entry is one record:

```yaml
- title: MagicGrid Book of Knowledge
  url: https://discover.3ds.com/magicgrid-book-of-knowledge
  desc: The definitive practitioner guide to the MagicGrid method, by Aleksandraviciene & Morkevicius.
  date: 2021
  lang: sysml-v1            # spine bucket
  type: methodology         # subsection within a bucket
  flagship: true            # optional — pulls v1 entries into the Magic Grid/Cameo marquee
  tags: [MagicGrid, Cameo, book]
```

**Field vocabulary:**

- `lang` (exactly one): `sysml-v1` | `sysml-v2` | `uaf` | `arcadia` | `opm` | `oml` |
  `cross-cutting`
- `type` (exactly one): `methodology` | `tutorial` | `course` | `book-paper` | `model` |
  `tool` | `community` | `spec` | `api`
- `flagship` (optional bool, only meaningful when `lang: sysml-v1`): places the entry in
  the marquee "Magic Grid & Cameo / CATIA Magic" subsection at the top of the SysML v1
  section.
- `tags` (list): free-form display tags that drive the cross-views. The tag legend view
  documents the controlled subset.
- `date` (year int): rendered as `(YYYY)`, matching current convention.

`lang` + `type` derive an entry's home in the spine. Anchors are generated
deterministically from the title via a single slug function; the generator emits the
Contents and every view back-link using that same function — which also resolves the
ToC/anchor slug mismatches CI has previously fought (single- vs double-hyphen slugs).

## README structure (generated output)

```
Intro + maintainer note                         (template prose)
Contents                                         (generated)

## SysML v1
   ### Magic Grid & Cameo / CATIA Magic          (flagship entries, marquee position)
   ### Methodology & guides
   ### Tutorials
   ### Courses & learning paths
   ### Books & papers
   ### Example models
   ### Tools, plugins & automation
   ### Communities & blogs
## SysML v2
   ### ... (incl. libraries, APIs & automation)
## UAF & architecture frameworks                 (UAF, UPDM, NAF, DoDAF, MODAF)
## Adjacent & non-SysML notations
   ### Arcadia / Capella
   ### OPM
   ### OML
## Cross-cutting (language-general)
   ### Methods (OOSEM, SYSMOD, Harmony, FAS)
   ### Systems-engineering standards
   ### Communities & blogs

## Find it your way                              (the four generated views)
   ### Openable models       (every entry tagged has-model, one cross-language table)
   ### By tool               (grouped by tool tag: Cameo, Papyrus, Rhapsody, SysON, ...)
   ### By resource type      (grouped by type across all notations)
   ### Tag legend            (every controlled tag + its meaning)

## The competitive landscape                     (template prose)
## Contributing                                  (template prose)
## Support & security                            (template prose)
```

- Resource-type subsections render only when non-empty (no sparse headings).
- The four views live **in the README** (single page = maximum discoverability), each
  emitted between `<!-- AUTOGEN:view-* -->` markers.
- Magic Grid / Cameo retains marquee position so the flagship differentiator is not
  buried by the restructure.

## Generator + CI

`scripts/generate.py`:

- **default:** read `data/entries.yaml` + `README.template.md`, write `README.md`.
- **`--check`:** regenerate in memory, diff against committed `README.md`, exit non-zero
  on drift.

**New CI job `generate-check`** (PRs): fails if `README.md` does not match
`data/entries.yaml`, preventing stale committed READMEs. Runs *before* lychee. Existing
lychee link + `--include-fragments=anchor-only` checks run unchanged on the generated
output, so the generated ToC/view back-links are still validated against generated
anchors.

**Self-check:** the generator ships one runnable assert-based check (the slug function
plus a tiny fixture entry set rendering to expected markdown). No test framework.

## Contribution workflow change

Contributors edit `data/entries.yaml` and run `python scripts/generate.py`, committing
both `entries.yaml` and the regenerated `README.md`. `CONTRIBUTING.md` and the
suggest-a-resource issue form are updated to describe the YAML record format and the tag
vocabulary instead of the raw markdown line format. This is the one real cost of the
generated-views approach and was accepted as the trade-off.

## Migration

All ~80 existing README entries are transcribed into `data/entries.yaml` with `lang`,
`type`, `flagship`, `tags`, and `date` assigned from their current section and inline
tags. The first generated `README.md` must be diffed against the current one to confirm
no entry is lost and the flagship content is intact before merge.

## Out of scope (YAGNI)

- No separate per-view files or a static-site build — views stay inline in the README.
- No search UI, no JSON API, no database.
- No automated tag inference — tags are authored in YAML.
- No reorganisation of CONTRIBUTING beyond the entry-format and tag-vocabulary changes
  the new workflow requires.

## Success criteria

- A reader can land on the README and jump straight to their notation from the Contents.
- The four views are present, correct, and regenerate deterministically from
  `entries.yaml`.
- Magic Grid / Cameo flagship depth is preserved in marquee position.
- `generate.py --check` is green in CI; lychee link + anchor checks pass on generated
  output.
- No existing entry is dropped in migration.
```
