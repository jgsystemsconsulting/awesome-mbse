# Design: Generator-driven `awesome-mbse`, restructured by language

**Date:** 2026-06-24
**Status:** Approved (brainstorming) + hardened (spec-review converged in 4 rounds) — ready for implementation plan
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
README.template.md       # narrative prose + AUTOGEN marker blocks the generator fills
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

**Reproducibility (pinned).** The generator must produce byte-identical output on any
machine, or `--check` (below) is unreliable. Therefore:
- Python version is pinned (`.python-version` / documented minimum, e.g. 3.11) and CI
  uses the same version.
- The single yaml dependency is pinned in `requirements.txt` (e.g. `PyYAML==6.0.x`) and
  CI installs from it. The generator imports nothing outside stdlib + that pin.
- Output is normalised: LF line endings only, no trailing whitespace, exactly one
  trailing newline, UTF-8 no BOM. Entry/view ordering is deterministic (see "Ordering").

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
- `tags` (list): display tags drawn from the controlled vocabulary (below) that drive the
  cross-views.
- `date` (year int): rendered as `(YYYY)`, matching current convention.

**Tag vocabulary (one authoritative definition).** Alongside the entries, the data carries
a `tags` legend block — a mapping of `tag → one-line meaning` — that is the single source
for the controlled tag vocabulary. It can live as a top-level key in `entries.yaml` or a
sibling `data/tags.yaml`; either way it is the authority the Tag-legend view renders and the
validator checks records against (every used tag must be defined here; the tool-token set is
a subset of it). The controlled subset includes the notation tags (`SysMLv1`, `SysMLv2`, …),
tool tags (`Cameo`, `Papyrus`, …), and resource tags (`paper`, `tool`, `mcp`, …).

`lang` + `type` derive an entry's home in the spine. `lang: cross-cutting` is an explicit
value meaning "language-general — belongs to no single notation" (e.g. the INCOSE
handbook, OOSEM, SYSMOD); such entries render only in the Cross-cutting section. Every
entry has **exactly one** `lang` home; multi-axis discoverability comes from the views
(by tool, by type, openable-models), not from multi-homing entries in the spine.

Anchors are generated deterministically from the title via a single slug function; the
generator emits the Contents and every view back-link using that same function — which
also resolves the ToC/anchor slug mismatches CI has previously fought (single- vs
double-hyphen slugs). **Slug algorithm (matches GitHub's exactly — do NOT "tidy" it):** lowercase; strip every
character that is not a letter, number, underscore, hyphen, or space; replace each space
with a hyphen. Critically it does **not** collapse consecutive hyphens and does **not**
strip leading/trailing hyphens — so `Magic Grid & Cameo / CATIA Magic` →
`magic-grid--cameo--catia-magic` (double hyphens where `&`/`/` were removed between spaces).
Matching this byte-for-byte is what makes the generated ToC links resolve against GitHub's
own heading anchors; "tidying" the slug is the exact historical bug. This is the single
authoritative definition; the validator's slug-uniqueness check and the renderer both call
it.

### Validation rules (generator fails closed)

Before rendering, `generate.py` validates `entries.yaml` and **exits non-zero** with a
clear message on any violation — invalid data must never silently produce a broken README:

- **Required fields present:** `title`, `url`, `desc`, `date`, `lang`, `type`. Missing →
  error naming the offending entry.
- **Enum membership:** `lang` and `type` must be in their controlled sets above. Unknown
  value → error (catches typos like `sysmlv2` vs `sysml-v2`).
- **`flagship` constraint:** `flagship: true` is only valid when `lang: sysml-v1`;
  anywhere else → error.
- **URL scheme allowlist:** `url` must start with `https://` or `http://` (https
  preferred). Any other scheme (`javascript:`, `data:`, `vbscript:`, `file:`, …) →
  error. This is a security control, not a style rule (see "Security & input handling").
- **`date` sanity:** integer year within `[1990, current_year + 1]`; out of range → error.
- **Slug uniqueness:** the slug of every entry title must be unique across the whole list;
  a collision → error (prevents silent anchor clobbering). Note this catches *near*
  collisions too — two titles differing only in punctuation/case slug to the same value.
  Resolution is to disambiguate the title in data, not to auto-suffix.
- **Tag-legend coverage:** every value appearing in any record's `tags` must have a
  definition in the `tags` legend block → otherwise error (a typo'd tag must not render a
  legend-less tag). A legend entry used by zero records is a warning, not an error.
- **Tool-token subset:** the controlled tool-token set (used by the By-tool view) must be a
  strict subset of the controlled tag vocabulary → a tool token absent from the legend is
  an error. This keeps the By-tool grouping and the tag legend reconciled.
- **Template integrity:** `README.template.md` must exist and contain each expected
  AUTOGEN marker exactly once as a matched START/END pair (see AUTOGEN markers); a missing
  template file or a missing/duplicated/unmatched marker → error.
- **Notation blurb presence:** for each `##` notation section, the template text between the
  section heading and that section's `AUTOGEN:START` must be non-empty prose (the mandatory
  "Use this when…" blurb). An empty/whitespace-only blurb → error. This makes the
  "which fits whom" requirement machine-enforced, so a deleted blurb fails `generate-check`
  rather than silently shipping. (The ≥2-sentence target is editorial guidance; the hard
  gate is non-empty.)

### Ordering (deterministic)

Within every spine subsection and every view, entries sort by **`date` descending, then
`title` ascending (case-insensitive)**. Ties beyond that are impossible because slugs are
unique. This makes output stable regardless of `entries.yaml` record order, so reordering
the YAML never changes the README.

## Security & input handling

`entries.yaml` is community-submitted via PRs; its content is **untrusted** and flows into
markdown rendered on GitHub. The generator treats all entry fields as hostile:

- **YAML parsing:** `yaml.safe_load` only — never `yaml.load`. (`yaml.load` with PyYAML
  can execute arbitrary Python via `!!python/…` tags.)
- **URL allowlist (normalised before check):** the validator first strips leading/trailing
  whitespace and control characters from `url` and lowercases the scheme portion, *then*
  requires it to start `https://` or `http://`. This defeats ` javascript:`,
  `JAVASCRIPT:`, and entity/whitespace-obfuscated bypasses. The check runs on the decoded,
  normalised string, not the raw bytes. Only `http(s)` URLs become links.
- **Markdown/HTML escaping:** `title` and `desc` are escaped before interpolation so they
  cannot break out of `[title](url)` link syntax, table cells, or inject markup. Escape
  the full set `[ ] ( ) ! | < > backtick` (the `!`/`(`/`)` defeat image-syntax `![](…)`
  and link breakout; `|` protects markdown table cells in the view tables). A `desc` is
  rendered as plain text, never as raw HTML; reference-style/autolink forms are neutralised
  by escaping `[ ] < >`.
- **CI trust boundary:** the `generate-check` CI job runs contributor-supplied
  `scripts/generate.py` and `README.template.md`. It therefore runs on `pull_request`
  (fork PRs get a read-only token and no repo secrets), declares
  `permissions: contents: read`, and **requires no secrets/token at all** (it only reads
  files, regenerates in memory, and diffs). The `lychee` job is what holds `GITHUB_TOKEN`
  for authenticated link checks; lychee does **not** execute repo scripts, so the token is
  never exposed to contributor-controlled code. The only privileged job that runs the
  generator — the maintainer-rescue job (write token) — sources all *code* from the base
  branch and only *data* from the PR, so contributor code never executes with a token (see
  CI → Maintainer rescue path). These jobs are independent (see CI).

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
   ### Openable models       (every entry with type==model, one cross-language table)
   ### By tool               (grouped by tool tag: Cameo, Papyrus, Rhapsody, SysON, ...)
   ### By resource type      (grouped by type across all notations)
   ### Tag legend            (every controlled tag + its meaning)

## The competitive landscape                     (template prose)
## Contributing                                  (template prose)
## Support & security                            (template prose)
```

- Resource-type subsections render only when non-empty — i.e. at least one record matches
  the section's `lang`+`type` predicate; an empty subsection emits no heading.
- Magic Grid / Cameo retains marquee position so the flagship differentiator is not
  buried by the restructure.

### Notation guidance — the "which fits whom" half (mandatory)

The stated problem has two halves: *navigate by notation* (the spine, above) **and**
*self-explain which notation fits whom*. The spine alone delivers only the first. So the
design mandates two pieces of guidance prose, authored in `README.template.md` (not
generated, but required to exist):

1. **A "Choosing a notation" mini-chooser** in the intro, before Contents — 4–6 lines
   mapping situation → section (e.g. "Cameo shop / programme today → SysML v1 · Magic
   Grid; greenfield, text-friendly, tool-flexible → SysML v2; defence/enterprise
   architecture → UAF; non-SysML / Eclipse → Adjacent notations").
2. **A 2–4 sentence "Use this when…" blurb** opening every `##` notation section,
   describing when to prefer that notation. These live in the template prose *above* each
   section's AUTOGEN block, so they are never clobbered by regeneration.

This is the half of the user's goal that structure-only would have dropped; it is a
spec requirement, verified in Success criteria.

### AUTOGEN markers (exact contract)

Generated blocks in `README.template.md` are bounded by paired HTML-comment markers:

```
<!-- AUTOGEN:START section=sysml-v1 -->
<!-- AUTOGEN:END section=sysml-v1 -->
```

Marker names are drawn from a fixed, enumerated set. The spine section id **is the `lang`
value** (`sysml-v1`, `sysml-v2`, `uaf`, `arcadia`, `opm`, `oml`, `cross-cutting`), giving
this exact marker set:

| Marker `section=` | Fills |
|---|---|
| `contents` | the generated ToC |
| `sysml-v1` … `cross-cutting` | each notation section's entry lists (incl. its resource-type subsections; for `sysml-v1`, the Magic Grid/Cameo marquee first) |
| `view-openable-models` | Openable models table |
| `view-by-tool` | By tool view |
| `view-by-type` | By resource type view |
| `view-tag-legend` | Tag legend table |

**Each `lang` value is its own marker — including `arcadia`, `opm`, `oml`.** The
"Adjacent & non-SysML notations" `##` heading is template prose; the three notations under
it are three separate H3 blocks, each its own `section=arcadia` / `=opm` / `=oml` marker
pair. This keeps the "section id = lang value" rule exact with no combined-section
exception.

On every run the generator **asserts each marker in this set appears exactly once as a
matched START/END pair** (and no unknown marker appears); missing, duplicated, or
unmatched → error. The generator only rewrites text *between* a pair, never the prose
outside markers, so the hand-edited narrative and the "Use this when…" blurbs are safe.

### View filter definitions (in real data-model fields)

Each view is a pure function of `entries.yaml` fields — no hidden derived flags:

- **Openable models** — all entries where `type == model`, one cross-language table
  (columns: model, home section link, tags). (Supersedes the old `has-model` tag as the
  selection rule.)
- **By tool** — entries grouped by each tool token present in `tags` from the controlled
  tool set (`Cameo`, `CATIA-Magic`, `Papyrus`, `Rhapsody`, `SysON`, `SysIDE`, `Capella`,
  `Modelio`, `Gaphor`, …), which is a strict subset of the tag vocabulary (enforced in
  validation). An entry with two tool tags appears under both groups — this duplication is
  intentional. It does not affect the count invariant, which counts spine placement
  (by `lang`/`type`) and never view rows; view-level duplication is checked separately (see
  the view-consistency assertion).
- **By resource type** — entries grouped by `type`.
- **Tag legend** — a static-from-data table of every controlled tag and its one-line
  meaning, sourced from a `tags` definition block in the data (so the vocabulary has one
  authoritative definition).

### awesome-lint conformance (generator responsibility)

The generated `README.md` must pass `awesome-lint`, so the generator/template guarantees
its structural rules rather than relying on hand-discipline:

- Title line is `# Awesome MBSE` followed by the Awesome badge, as the very first content.
- A `## Contents` section (the generated ToC) immediately follows the intro, before the
  first list section.
- ToC links use the same slug function as the headings they point to (the historical
  failure mode — fixed by single-source slugging).
- No `## License` section in the body (awesome-lint's `awesome-license` rule): licensing
  stays in the CC0 footer + `LICENSE` file, matching the current README.
- List items follow the awesome convention `[name](url) - Description.` which the entry
  renderer emits verbatim.

## Generator + CI

`scripts/generate.py`:

- **default:** read `data/entries.yaml` + `README.template.md`, validate (see Validation
  rules), write `README.md` with normalised output (LF, no trailing whitespace, single
  trailing newline, UTF-8 no BOM).
- **`--check`:** run validation, regenerate in memory, and compare to the committed
  `README.md`. The comparison is on the **normalised form**: both sides are read and
  written as LF / UTF-8-no-BOM so a contributor's CRLF checkout cannot cause a false
  diff. Exit non-zero on any difference, printing a unified diff.

**Migration / entry-count invariant (every run, not just migration).** The invariant is
defined over **spine placement**, which is unambiguous because every record has exactly one
`lang` home (a `cross-cutting` record renders in the Cross-cutting spine section — itself a
spine section — so it is placed exactly once like any other). The generator asserts:

- Every record is rendered into **exactly one** spine section (its `lang` home). The set of
  distinct records placed into the spine equals the set of records in `entries.yaml` —
  `count(distinct spine-placed records) == count(records)`. No record is dropped or
  double-placed in the spine.
- `count(records rendered in the Magic Grid/Cameo marquee) == count(flagship: true records)`.
- **Views are excluded from this invariant** — they re-present spine records and may
  duplicate (a two-tool entry appears in two By-tool groups). A separate assertion checks
  the views are consistent with the data: an entry with N tool tags appears in exactly N
  By-tool groups, and the Openable-models table row count equals `count(type == model)`.

Any mismatch → error. This converts the one-time "no entry dropped" migration check into a
permanent regression guard with no ambiguity about what is counted.

**CI — three independent jobs on `pull_request`:**

- **`generate-check`** — `permissions: contents: read`, no secrets. Installs the pinned
  Python + PyYAML, runs `python scripts/generate.py --check`. Fails the PR on drift,
  invalid data, or a broken invariant. Because it runs contributor-controlled code, it
  deliberately holds no token. It runs on **every** PR (no GitHub `paths:` filter): a
  path-filtered required check shows as *skipped* on unrelated PRs, and branch protection
  treats "skipped" as not-passing, permanently blocking merge. The job is fast, so it
  always runs and exits 0 quickly when generator inputs are unchanged.
- **`awesome-lint`** (existing/restored) — runs `awesome-lint` on the committed
  `README.md`, enforcing the structural rules the generator targets (above). A named,
  required job so "awesome-lint passes" is verified, not assumed.
- **`lychee`** (existing) — keeps `GITHUB_TOKEN` for authenticated link +
  `--include-fragments=anchor-only` checks, run on the committed `README.md` (which is what
  ships). It does not execute repo scripts.

The jobs are **independent** (none `needs:` another) so one failure doesn't mask another;
the PR must pass all three. The weekly link-rot job is unchanged and assumes the committed
`README.md` is always a valid generator output.

**Maintainer rescue path (web-UI / non-Python contributors).** Most awesome-list
contributions arrive via the issue form or the GitHub web "Edit file" button, where the
contributor cannot run `generate.py`. To avoid a dead-end:

- The **primary** path stays the suggest-a-resource **issue form** — the maintainer adds
  the record to `entries.yaml` and regenerates. Contributors are not expected to run Python.
- For a direct PR that edited only `entries.yaml` and left `README.md` stale, a
  **maintainer-triggered** job (on the `regenerate` label or `workflow_dispatch`) runs
  `generate.py` and commits the regenerated `README.md` to the PR branch. This is a
  deliberate, *maintainer-gated* exception to "CI never commits".

  **Critical trust rule for this job:** because it holds a write token, it must source **all
  code from the base branch only** — `generate.py`, `README.template.md`, and any imported
  module are checked out at the repository default branch (`ref:` pinned to base), and
  **only `data/*.yaml` is taken from the PR branch**, passed through the validator before
  use. It must never execute `generate.py` or a template from the PR head, or a malicious PR
  could run attacker code with the write token. (The unprivileged `generate-check` job, by
  contrast, safely runs PR-head code precisely because it holds no token.)

  **Fork prerequisite:** pushing the regenerated `README.md` to a fork PR branch requires
  the contributor to have enabled "Allow edits by maintainers". The job checks
  `maintainerCanModify` (e.g. `gh pr view --json maintainerCanModify`); if false, it posts a
  PR comment asking the contributor to enable it (or to pull the regenerated file) instead of
  failing silently.

`CONTRIBUTING.md` documents both paths (and the "Allow edits by maintainers" note) so a
failing `generate-check` is never a silent dead-end.

**Pre-commit hook (prevention, not just CI detection).** The repo ships a version-
controlled `.pre-commit-config.yaml` with a local hook that runs `generate.py`, so the
committed `README.md` is regenerated before commit. `CONTRIBUTING.md` documents the
one-time enable command (`pip install pre-commit && pre-commit install`). The hook runs
**locally only — never in CI, never with a token.** This addresses the "forgot to
regenerate" failure mode at the source; `generate-check` remains the backstop for
contributors who skip the hook.

**Rollback.** A bad merge is reverted by reverting the `entries.yaml` (and regenerated
`README.md`) commit, or by editing `entries.yaml` and re-running the generator — there is
no separate state to unwind.

**Self-check:** the generator ships one runnable assert-based check (`__main__`/`demo()`)
over a tiny fixture entry set, exercising the non-trivial logic:
- the slug function (incl. a near-collision: two distinct titles that slug identically must
  raise);
- validation fail-closed cases — a bad URL (` JAVASCRIPT:`), `flagship` on a non-v1
  record, an unknown `lang`, a `tags` value missing from the legend, and a notation section
  with an empty/whitespace-only blurb each must raise;
- determinism — reordering the fixture records produces byte-identical output;
- normalisation — `--check` against a fixture with CRLF/BOM still reports clean;
- empty-subsection — a `lang`+`type` with no records emits no heading.
No test framework.

## Contribution workflow change

Contributors edit `data/entries.yaml` and run `python scripts/generate.py`, committing
both `entries.yaml` and the regenerated `README.md`. `CONTRIBUTING.md` and the
suggest-a-resource issue form are updated to describe the YAML record format and the tag
vocabulary instead of the raw markdown line format, and to state prominently **"never edit
`README.md` directly — it is generated."** Enabling the pre-commit hook (one documented
command) is recommended so regeneration is automatic, and `CONTRIBUTING.md` names Python
3.11 as the canonical version (recommending pyenv/asdf) to avoid "works locally, fails CI"
drift. Contributors who cannot run Python use the issue-form path instead (see Maintainer
rescue path). This raised contribution barrier is the one real cost of the generated-views
approach and was accepted as the trade-off; the local-generate model was kept (over a
CI-generates-and-commits model) specifically so the README change is visible in the PR diff
for review, which an awesome-list depends on.

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

- A reader can land on the README and jump straight to their notation from the Contents —
  CI-verified: lychee's `--include-fragments=anchor-only` check confirms every Contents
  link resolves to a real anchor (the same check already guards the ToC today).
- The "which fits whom" half is delivered: a "Choosing a notation" chooser appears in the
  intro, and every `##` notation section opens with a "Use this when…" blurb whose presence
  is generator-validated (non-empty; ≥2-sentence is editorial guidance) — a deleted blurb
  fails `generate-check`.
- The four views are present, correct, and regenerate deterministically from
  `entries.yaml` (re-running the generator on unchanged data produces a byte-identical
  README — verified by `--check` returning clean immediately after a generate).
- Magic Grid / Cameo flagship depth is preserved in marquee position.
- `generate.py --check` is green in CI; lychee link + anchor checks pass on generated
  output; the generated README passes `awesome-lint`.
- The entry-count and flagship-count invariants hold (no entry dropped, in migration or
  any later run).
- Validation fails closed: a record with an unknown `lang`/`type`, a non-`http(s)` URL,
  `flagship` outside SysML v1, or a duplicate title-slug causes a non-zero exit with a
  clear message (verified by the self-check fixture).
```
