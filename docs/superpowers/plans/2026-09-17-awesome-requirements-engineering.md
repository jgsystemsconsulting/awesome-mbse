# Awesome Requirements Engineering Spoke Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create `jgsystemsconsulting/awesome-requirements-engineering`, a private sibling spoke of the awesome-mbse family (FAMILY private-mode default until an explicit public release), with a FAMILY-conformant README carrying at least 40 tagged, year-stamped entries, blocking CI, and the two hub-side go-live edits.

**Architecture:** New sibling repo beside the hub (`../awesome-requirements-engineering`), bootstrapped with LICENSE plus a minimal README so the default branch exists, then populated with governance files, CONTRIBUTING.md, three workflows, and a 40-entry README. CI runs blocking lychee plus awesome-lint on PRs, a weekly single-issue link-rot sweep, and markdownlint. Hub FAMILY/README edits land in their own PR only after the spoke's population PR is green and the scheduled workflow has been proven by dispatch. While the hub is private, the spoke family pointer is text-only (no hyperlink to hub FAMILY.md).

**Tech Stack:** Git + `gh` CLI, GitHub Actions (lychee-action v0.24.2, awesome-lint via npx, markdownlint-cli2-action), CC0-1.0, plain markdown. No code beyond a local throwaway checker script.

**Spec:** `docs/superpowers/specs/2026-09-17-awesome-requirements-engineering.md`

## Global Constraints

Every task implicitly includes these. Values are verbatim from the spec.

- Repo: `jgsystemsconsulting/awesome-requirements-engineering`, **private** on create (FAMILY private-mode default), default branch `main`. Sibling checkout at `C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering`. Never nested inside the hub. Public release is a later runbook step, not this plan.
- Entry format: ``- [Resource Name](url) - One-line factual description `tags` (YYYY).`` Hyphen separator, never an en/em dash. Description at most 140 characters. Tags as inline code spans before the terminal period.
- Tag order: `language → method → tool → has-model → type → spec/standard → paid → year`.
- Minimum 40 entries after the inclusion bar. The 12 required URLs (Task 5) must appear in their assigned sections.
- `CONTRIBUTING.md` uppercase. LICENSE is CC0-1.0 copied from the hub.
- CI: `link-check-pr.yml` with lychee `fail: true`, `--include-fragments=anchor-only`, `--accept 200..=299,429`, `GITHUB_TOKEN` passed, plus an awesome-lint job. `link-check-schedule.yml` cron `0 6 * * 1` plus `workflow_dispatch`, lychee `fail: false`, exactly one open `link-rot` issue. `lint.yml` runs markdownlint-cli2 on `README.md` and `CONTRIBUTING.md`, action refs pinned to commit SHAs.
- Hub changes are limited to exactly two edits (FAMILY registry status, README spoke link) in one separate PR, opened only after the spoke's population CI is green and the weekly workflow has been proven via `workflow_dispatch`.
- No `awesome-archimate` work. No sindresorhus/awesome submission. No paid-content re-hosting. No entry text copied from the hub, awesome-sysml-v2, or `awesome-requirements-writer`.
- Sweep date: 2026-09. The README badge and the CHANGELOG initial entry must both say 2026-09.
- Entry text is written fresh for this spoke; research URLs are the inputs, not copied lines.

## Codebase context

Pattern document: `docs/superpowers/context/2026-09-17-awesome-requirements-engineering-pattern-context.md` (SC1-SC6 met against hub HEAD `4f7c0a6`).

Decisions this plan inherits:

- Sibling repo under the org, never nested in the hub; the live exemplar is `../awesome-sysml-v2`.
- Hub `FAMILY.md` and hub `CONTRIBUTING.md` are the format source of truth. The sysml-v2 checkout is a structure and config analog only: its untagged entry format, lowercase `contributing.md`, and advisory PR lychee (`fail: false` in `links.yml`) are deliberately not copied. The hub's blocking `link-check-pr.yml` is the gate pattern.
- Port sources, all read at planning time: hub `FAMILY.md`, hub `CONTRIBUTING.md`, hub `.github/workflows/link-check-pr.yml`, hub `.github/workflows/link-check-schedule.yml`, hub `.github/PULL_REQUEST_TEMPLATE.md`, hub `.github/ISSUE_TEMPLATE/suggest-resource.yml`, hub `LICENSE` (CC0), hub `CODE_OF_CONDUCT.md`, hub `SECURITY.md`, sysml-v2 `.github/workflows/lint.yml`, sysml-v2 `.markdownlint-cli2.jsonc`.
- Ignore `docs/superpowers/*awesome-archimate*` artifacts as stem sources.

## Research

Findings document (SC1-SC4 complete, retrieved 2026-09-17, 40+ live candidates, namespace free, seven-section clustering): `docs/superpowers/research/2026-09-17-awesome-requirements-engineering-sources-research.md`

research: docs/superpowers/research/2026-09-17-awesome-requirements-engineering-sources-research.md

Key source URLs behind the anchors:

- https://ieeexplore.ieee.org/document/6170935 (ISO/IEC/IEEE 29148)
- https://www.omg.org/spec/ReqIF/1.2/ (ReqIF 1.2)
- https://alistairmavin.com/ears/ (EARS) and https://doi.org/10.1109/RE.2009.9 (EARS paper)
- https://webperso.info.ucl.ac.be/~avl/ (KAOS)
- https://eclipse.dev/rmf/ , https://github.com/doorstop-dev/doorstop , https://github.com/strictdoc-project/strictdoc
- Top-up URLs verified live during this planning run (2026-09-17): https://dl.acm.org/doi/10.1145/336512.336523 (Nuseibeh and Easterbrook roadmap), https://dl.acm.org/doi/10.1145/237432.237434 (Zave and Jackson, Four Dark Corners), https://rockynook.com/product/requirements-engineering-fundamentals-2nd-edition/ (Pohl and Rupp), https://link.springer.com/book/10.1007/978-1-84996-405-0 (Hull, Jackson, Dick), https://www.computer.org/education/bodies-of-knowledge/software-engineering (SWEBOK V4), https://conf.researchr.org/home/refsq-2026 (REFSQ), https://cpre.ireb.org/en/downloads-and-resources/recommended-reading (IREB reading list).
- Rejected during planning: https://link.springer.com/journal/11507 (Springer IDP cookie wall), https://open-services.net/spec/rm/ (404; the open-services.net root is used instead), https://cpre.ireb.org/en/glossary/ (404).

## File structure

New repo `C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering` (created in Task 1):

| File | Responsibility | Task |
|------|----------------|------|
| `LICENSE` | CC0-1.0, copied from hub | 1 |
| `README.md` | FAMILY skeleton, seven sections, 40+ entries | 1 (stub), 5 (full) |
| `CODE_OF_CONDUCT.md` | Verbatim port from hub | 2 |
| `SECURITY.md` | Verbatim port from hub | 2 |
| `CHANGELOG.md` | Initial sweep entry, 2026-09 | 2 |
| `.github/PULL_REQUEST_TEMPLATE.md` | RE-adapted checklist | 2 |
| `.github/ISSUE_TEMPLATE/suggest-resource.yml` | RE-adapted issue form | 2 |
| `CONTRIBUTING.md` | Inclusion bar, entry format, RE tag vocabulary, year and dedupe rules, neutrality, cadence | 3 |
| `.markdownlint-cli2.jsonc` | MD013 off | 3 |
| `.github/workflows/link-check-pr.yml` | Blocking lychee plus awesome-lint on PR | 4 |
| `.github/workflows/link-check-schedule.yml` | Weekly sweep, single `link-rot` issue | 4 |
| `.github/workflows/lint.yml` | markdownlint-cli2, SHA-pinned actions | 4 |
| `.gitignore` | Ignores the `lychee/` report dir | 4 |
| `.lycheeignore` | Only justified bot-blocked domains | 6 (conditional) |

Hub repo `C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse` (Task 9 only): `FAMILY.md` registry row status, `README.md` spoke link.

---

### Task 1: Create local repo, remote, and bootstrap main

**Files:**
- Create: `C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering/LICENSE`
- Create: `C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering/README.md` (stub, replaced in Task 5)

**Interfaces:**
- Produces: remote `origin` pointing at `jgsystemsconsulting/awesome-requirements-engineering`, default branch `main` with one bootstrap commit. Later tasks commit on a `population` branch off this.

**Model:** flash

- [ ] **Step 1: Preflight checks**

```bash
gh auth status
gh repo view jgsystemsconsulting/awesome-requirements-engineering --json name
```

Expected: authenticated as a member/owner able to create org repos. The `gh repo view` call must fail with NotFound (namespace empty). FAMILY requires the namespace re-checked the same day as creation. If it exists, stop and report.

- [ ] **Step 2: Create the local sibling checkout**

```bash
mkdir -p "C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering"
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering"
git init -b main
cp "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse/LICENSE" LICENSE
head -3 LICENSE
```

Expected: `head -3` shows the CC0 dedication lines copied from the hub.

- [ ] **Step 3: Write the stub README**

Create `README.md` with exactly:

```markdown
# Awesome Requirements Engineering [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Curated list of requirements engineering resources: standards, methods, interchange formats, tools, books, and community.

Bootstrap commit; population in progress.
```

- [ ] **Step 4: Commit, create the remote, push**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering"
git add LICENSE README.md
git commit -m "chore: bootstrap repo with CC0 license and README stub"
gh repo create jgsystemsconsulting/awesome-requirements-engineering --private --description "Curated list of requirements engineering resources: standards, methods, interchange formats, tools, books, and community. A spoke of the awesome-mbse family."
git remote add origin https://github.com/jgsystemsconsulting/awesome-requirements-engineering.git
git push -u origin main
```

- [ ] **Step 5: Verify the remote shape**

```bash
gh repo view jgsystemsconsulting/awesome-requirements-engineering --json visibility,defaultBranchRef
git ls-remote origin main
```

Expected: `visibility` is `PRIVATE`. Default branch is `main`.

Expected: visibility `PRIVATE`, default branch `main`, and a non-empty HEAD sha. GitHub cannot open PRs against an empty repo, which is why the bootstrap lands on `main` before anything else.

---

### Task 2: Port governance files and templates

**Files:**
- Create: `CODE_OF_CONDUCT.md`, `SECURITY.md`, `CHANGELOG.md`, `.github/PULL_REQUEST_TEMPLATE.md`, `.github/ISSUE_TEMPLATE/suggest-resource.yml` (all under the spoke repo root)

**Interfaces:**
- Produces: `.github/PULL_REQUEST_TEMPLATE.md` referenced by every later PR; the issue form's dropdown lists the seven README section names that Task 5 creates.
- Consumes: hub `CODE_OF_CONDUCT.md` and `SECURITY.md` at `C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse/`.

**Model:** flash

- [ ] **Step 1: Start the population branch**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering"
git checkout -b population
```

All remaining spoke work commits here. Task 7 opens the PR.

- [ ] **Step 2: Copy CoC and SECURITY verbatim**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering"
cp "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse/CODE_OF_CONDUCT.md" CODE_OF_CONDUCT.md
cp "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse/SECURITY.md" SECURITY.md
grep -F "support@jgsystemsconsulting.com" SECURITY.md
```

Expected: the grep finds the malicious-link reporting address. That path must stay intact.

- [ ] **Step 3: Create CHANGELOG.md**

Create `CHANGELOG.md` with exactly:

```markdown
# Changelog

Maintenance sweeps and notable changes. The "Last full sweep" badge in the README
tracks the most recent dated entry here.

## 2026-09: initial release and first full sweep

- List created as a requirements engineering spoke of the
  awesome-mbse list family (hub private; text-only pointer).
- First full sweep completed 2026-09: 40 entries across seven sections.
- CI enabled: blocking link check and awesome-lint on PRs, weekly link-rot sweep,
  markdownlint on README and CONTRIBUTING.
```

Task 5's checker prints the final entry count; if it is not 40, update the count line in this file before Task 7 opens the PR.

- [ ] **Step 4: Create the PR template**

Create `.github/PULL_REQUEST_TEMPLATE.md` with exactly:

```markdown
<!-- Thanks for contributing! Check every box; CI enforces most of these. -->

## What I'm adding / changing

<!-- one line -->

## Inclusion bar (CONTRIBUTING.md §2)

- [ ] On-topic for requirements engineering as a discipline
- [ ] Substantive: not pure marketing
- [ ] Link is live (CI link-checks it; you can pre-check with the Docker one-liner in CONTRIBUTING.md)
- [ ] Not a duplicate (canonical-URL rule, CONTRIBUTING.md §6)
- [ ] Publicly accessible: linked, not re-hosted

## Entry format (CONTRIBUTING.md §3 and §4)

- [ ] `- [Name](url) - Description ` plus inline-code tags plus `(YYYY).` with the hyphen separator, **not** an en/em-dash
- [ ] Description ≤ 140 characters
- [ ] Tags drawn only from the vocabulary, in the fixed order (language → method → tool → has-model → type → spec/standard → paid → year)
- [ ] `(YYYY)` is the resource's most recent author-published version
- [ ] If `has-model`/`has-template`: directly downloadable, non-paywalled file (CONTRIBUTING.md §3)

## Housekeeping

- [ ] If a **top-level** section was added/renamed, updated the hand-maintained `## Contents` ToC
- [ ] (If a JGS product) it sits next to at least 1 competing/alternative entry (CONTRIBUTING.md §7)
```

- [ ] **Step 5: Create the issue form**

Create `.github/ISSUE_TEMPLATE/suggest-resource.yml` with exactly:

```yaml
name: Suggest a resource
description: Suggest a requirements engineering resource to add to the list
title: "[Suggestion] <resource name>"
labels: ["suggestion"]
body:
  - type: input
    id: name
    attributes:
      label: Resource name
      placeholder: e.g. EARS
    validations:
      required: true
  - type: input
    id: url
    attributes:
      label: URL
      placeholder: https://...
    validations:
      required: true
  - type: textarea
    id: description
    attributes:
      label: One-line description (≤ 140 characters, factual, no hype)
    validations:
      required: true
  - type: dropdown
    id: section
    attributes:
      label: Which section does it belong in?
      options:
        - Standards and guides
        - Interchange and integration
        - Methods and notation
        - Books and foundational papers
        - Open-source tools
        - Commercial tools
        - Learning, certification, and community
    validations:
      required: true
  - type: checkboxes
    id: bar
    attributes:
      label: Inclusion bar (see CONTRIBUTING.md)
      options:
        - label: On-topic for requirements engineering as a discipline
          required: true
        - label: Substantive (teaches, demonstrates, specifies, or provides something usable; not pure marketing)
          required: true
        - label: The link is live right now
          required: true
        - label: It isn't already in the list
          required: true
        - label: Publicly accessible (we link, we never re-host)
          required: true
```

- [ ] **Step 6: Verify and commit**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering"
git ls-files | grep -E "CODE_OF_CONDUCT|SECURITY|CHANGELOG|PULL_REQUEST|suggest-resource"
python -c "import yaml; yaml.safe_load(open('.github/ISSUE_TEMPLATE/suggest-resource.yml', encoding='utf-8'))" || pip install pyyaml
git add CODE_OF_CONDUCT.md SECURITY.md CHANGELOG.md .github/
git commit -m "docs: port governance files from the hub"
```

Expected: all five paths listed, YAML parses clean.

---

### Task 3: CONTRIBUTING.md with the RE tag vocabulary

**Files:**
- Create: `CONTRIBUTING.md`
- Create: `.markdownlint-cli2.jsonc`

**Interfaces:**
- Produces: heading anchors `CONTRIBUTING.md#7-editorial-neutrality` (used by the README in Task 5), the tag vocabulary the Task 5 checker enforces, and the markdownlint config Task 4's workflow relies on.

**Model:** flash

- [ ] **Step 1: Write .markdownlint-cli2.jsonc**

Create `.markdownlint-cli2.jsonc` with exactly (sysml-v2 port):

```jsonc
{
  "config": {
    "MD013": false
  }
}
```

- [ ] **Step 2: Write CONTRIBUTING.md**

Create `CONTRIBUTING.md` with exactly the content below. Port notes: inclusion bar, entry format, tag axes/cardinality/order, year rule, canonical-URL rule, neutrality structure, ToC note, local link-check, and cadence are ported from hub `CONTRIBUTING.md` as FAMILY mandates; the tag values are the RE adaptation from the spec; the hub's Model Gallery section is dropped (no gallery on this spoke) and later sections are renumbered. One spoke addition under §5 defines years for living pages, which the hub rule does not cover.

````markdown
# Contributing

Thanks for helping keep this the best-curated requirements engineering index anywhere.
Read this before opening a PR: the CI gates enforce most of it.

The fastest path: open an [issue using the "Suggest a resource" form](../../issues/new/choose),
or open a pull request that edits `README.md` directly.

## 1. How to suggest a resource

- **Issue:** use the *Suggest a resource* form. Good for "I found this, you decide."
- **PR:** edit `README.md`, follow the entry format below, tick the PR checklist. CI
  link-checks your entry and lints the list.

## 2. Inclusion bar

An entry is accepted only if **all** hold:

1. **On-topic:** genuinely about requirements engineering as a discipline: elicitation,
   writing, management, traceability, interchange, standards, methods, tools, books,
   papers, community. SysML v2 the language lives in
   awesome-sysml-v2 (public spoke); Magic
   Grid and Cameo practice stays with the
   the awesome-mbse hub (private; text name only while hub is private).
2. **Substantive:** it teaches, demonstrates, specifies, or provides something usable.
   Not a stub. Not pure vendor marketing.
3. **Live:** the link resolves right now.
4. **Not duplicative:** not already listed (see the canonical-URL rule, §6).
5. **Legally linkable:** publicly accessible. We **link**, we never re-host model files,
   PDFs, or proprietary content.

Tie-breakers (nice-to-have, not gates): has a downloadable template or ReqIF sample
(`has-template` / `has-model`), recently updated, from a recognized source (ISO, IEEE,
OMG, IREB, Eclipse, a university, an established practitioner).

## 3. Entry format

One line per entry, **hyphen separator** (` - `, never an en/em-dash; awesome-lint
rejects those), tags as **inline code spans inside the sentence before the terminal
period**, year parenthesized as the last token:

```
- [Resource Name](https://example.com) - One-line factual description `textual` `EARS` `tutorial` (2024).
```

- **Description:** factual, one line, **≤ 140 characters** (measured from the first
  character after ` - ` to the last character before the first tag, excluding the link
  markup and tags). No hype.
- **`has-model`** means: a **directly downloadable, non-paywalled** file in a recognized
  interchange or model format (`.reqif`, `.reqifz`, or a named tool's project file) that
  opens in a named tool. **`has-template`** means: a directly downloadable requirements
  template or pattern sheet. Screenshots and access-gated or request-only files do not
  qualify. If both apply to one resource, split it into two list entries.

## 4. Tag vocabulary, cardinality & order

Tags appear in this fixed order, drawn **only** from this vocabulary:

`language → method → tool → has-model → type → spec/standard → paid → year`

| Axis | Cardinality | Values |
|------|-------------|--------|
| language (requirement notation) | exactly 1 | `textual` · `model-based` · `RE-general` |
| method | 0 or 1 | `EARS` · `KAOS` · `Volere` · `other-method` |
| tool | 0 or more | `DOORS` · `ReqView` · `Jama` · `Visure` · `Polarion` · `other-tool` |
| has-model | 0 or 1 | `has-model` · `has-template` (pick one; a resource with two downloadables gets two entries) |
| type | exactly 1 (dominant form) | `tutorial` · `course` · `book` · `paper` · `blog` · `video` · `tool` · `plugin` · `template` · `standard` · `spec` · `guide` · `community` |
| spec/standard | 0 or 1 | `spec` · `standard` (optional echo of type when type is `spec` or `standard`) |
| paid | 0 or 1 | `paid` |
| year | exactly 1 | `(YYYY)` (see §5) |

Definitions:

- `textual`: natural-language requirement writing (EARS, quality guides, Volere template
  practice). `model-based`: goal-oriented or other model-centric RE (KAOS and kin).
  `RE-general`: the default for tools, interchange, certification, community, and
  discipline-wide standards or books with no notation focus.
- `other-tool` and `other-method` graduate to their own tags only once ≥ 3 entries share
  them.
- Type by source: ISO/IEEE normative documents are `standard`; OMG or consortium
  interchange formats are `spec`; informal practice guides are `guide`; organizations,
  conferences, and magazines are `community`; commercial and open-source products are
  `tool` (plugins are `plugin` unless they are paid commercial products). Never also use
  type `paper` on a normative document.
- Any non-free resource (tool, book, course, certification) carries `paid`. Free
  open-source tools omit it.

## 5. The year rule (`YYYY`)

`(YYYY)` = the year of the resource's **most recent author-published version**:

- a paper → its publication year;
- a repo → its latest tagged release, or the latest default-branch commit if untagged;
- a course → its current cohort year.

**Trivial edits (typo fixes) don't count.** Examples:

- A 2019 paper with a 2024 typo-fix commit → `(2019)`.
- A repo whose latest release tag is `v2.1` from 2023 → `(2023)`.

Spoke addition, for living pages: a vendor product site, organization page, or
documentation home uses the year of its most recent visible dated update; if the page
shows no date, use the year of the sweep that added the entry.

## 6. Canonical-URL rule (dedupe)

Before deciding "is this a duplicate", canonicalize both URLs: force `https`, lowercase
the host, strip a trailing slash, drop the query string and fragment unless they're
semantically required. If the canonical forms match, it's a duplicate.

## 7. Editorial neutrality

This list is maintained by JG Systems Consulting Ltd., which currently sells no
requirements-management product. To keep it trustworthy if that ever changes:

- JGS products would be listed by the **same inclusion bar** as everything else.
- Every JGS entry would sit next to **≥ 1 genuine competing/alternative entry**.
- **A superior competing tool is listed above a JGS one.** Neutrality is enforced by
  this rule, not by tone.

> **Table of Contents:** the `## Contents` ToC is hand-maintained and lists only the
> top-level sections (a flat ToC keeps awesome-lint happy). If you add or rename a
> **top-level** section, update the ToC by hand; sub-sections are not listed. CI validates
> every ToC anchor resolves (lychee `--include-fragments anchor-only`).

## 8. Local link-check

No install needed: check your changed links with Docker.

```sh
docker run --rm -v "$PWD:/d" -w /d lycheeverse/lychee --include-fragments anchor-only README.md
```

Or just open a **draft PR** and let CI check it for you.

## 9. Maintenance cadence

The maintainers run a **quarterly sweep** (add new resources, prune rot), logged in
`CHANGELOG.md` with the date, and update the *Last full sweep* badge at the top of the
README each time. If it's been **> 6 months** since the last sweep, the badge flips to
"maintenance lapsed"; call it out in an issue.
````

- [ ] **Step 3: Verify and commit**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering"
grep -c "RE-general" CONTRIBUTING.md
grep -F "language → method → tool → has-model → type → spec/standard → paid → year" CONTRIBUTING.md
npx -y markdownlint-cli2 "CONTRIBUTING.md"
git add CONTRIBUTING.md .markdownlint-cli2.jsonc
git commit -m "docs: add CONTRIBUTING.md with the RE tag vocabulary"
```

Expected: the tag-order grep matches one line, and markdownlint exits clean. If markdownlint is not installed, `npx` fetches it.

---

### Task 4: CI workflows

**Files:**
- Create: `.github/workflows/link-check-pr.yml`
- Create: `.github/workflows/link-check-schedule.yml`
- Create: `.github/workflows/lint.yml`
- Create: `.gitignore`

**Interfaces:**
- Produces: workflow names `link-check (PR)`, `link-check (weekly)`, `Lint` (Task 7 and Task 8 watch these); the `link-rot` label and `lychee/out.md` output path (Task 8 asserts on both); the `.lycheeignore` path trigger that Task 6 may use.
- Consumes: hub workflow YAML as the semantic source. The two link-check files below are the hub's workflows with the header comments rewritten for this spoke (the hub comments reference hub-internal spec sections and the Model Gallery). `lint.yml` is the sysml-v2 `lint.yml` with the awesome-lint step removed (spec: awesome-lint stays in workflow 1, matching the hub) and globs widened to both markdown files.

**Model:** flash

- [ ] **Step 1: Write .github/workflows/link-check-pr.yml**

Create `.github/workflows/link-check-pr.yml` with exactly:

```yaml
name: link-check (PR)

# Gate on contributions: a dead new link fails the PR, and the README must
# stay awesome-lint conformant (FAMILY.md shared standard).

on:
  pull_request:
    paths:
      - "README.md"
      - ".lycheeignore"
      - ".github/workflows/link-check-pr.yml"

concurrency:
  group: link-check-${{ github.ref }}
  cancel-in-progress: true

permissions:
  contents: read

jobs:
  lychee:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Check links and in-doc anchors
        uses: lycheeverse/lychee-action@e7477775783ea5526144ba13e8db5eec57747ce8 # master w/ nested-tarball install fix (>v2.8.0)
        with:
          # --include-fragments=anchor-only validates the hand-maintained ToC
          # anchors against the section headings. The token is passed so the many
          # github.com links are checked authenticated, avoiding the 60 req/hr
          # anonymous rate limit that reports live links as dead.
          lycheeVersion: v0.24.2
          args: >-
            --include-fragments=anchor-only
            --max-concurrency 4
            --accept 200..=299,429
            --no-progress
            README.md
          fail: true
          token: ${{ secrets.GITHUB_TOKEN }}

  # ToC is hand-maintained (flat, top-level only) to stay awesome-lint clean.

  awesome-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: "20"
      - name: Awesome-list manifest conformance
        run: npx -y awesome-lint
```

- [ ] **Step 2: Write .github/workflows/link-check-schedule.yml**

Create `.github/workflows/link-check-schedule.yml` with exactly:

```yaml
name: link-check (weekly)

# Freshness engine: every week, find rotted links and keep exactly ONE open
# tracking issue. Does not fail noisily: it reports (FAMILY.md shared standard).

on:
  schedule:
    - cron: "0 6 * * 1" # Mondays 06:00 UTC
  workflow_dispatch: {}

permissions:
  contents: read
  issues: write # required for the close + create steps below

jobs:
  link-rot:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Check links (report only, never fail)
        uses: lycheeverse/lychee-action@e7477775783ea5526144ba13e8db5eec57747ce8 # master w/ nested-tarball install fix (>v2.8.0)
        with:
          lycheeVersion: v0.24.2
          args: >-
            --include-fragments=anchor-only
            --max-concurrency 4
            --accept 200..=299,429
            --no-progress
            README.md
          fail: false
          output: ./lychee/out.md
          token: ${{ secrets.GITHUB_TOKEN }}

      # Stock create-issue-from-file does NOT dedupe/update, so we enforce a single
      # open report ourselves: close any existing open link-rot issue first, then
      # create the fresh one. gh needs GH_TOKEN explicitly; the ambient token is not
      # auto-visible to it as auth.
      - name: Close previous link-rot report
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          for n in $(gh issue list --label link-rot --state open --json number --jq '.[].number'); do
            gh issue close "$n" --comment "Superseded by this week's link-rot report."
          done

      - name: Open this week's link-rot report
        uses: peter-evans/create-issue-from-file@v5
        with:
          title: "Weekly link-rot report"
          content-filepath: ./lychee/out.md
          labels: link-rot
```

- [ ] **Step 3: Write .github/workflows/lint.yml**

Create `.github/workflows/lint.yml` with exactly (SHA pins are the sysml-v2 values, already resolved to commit SHAs there):

```yaml
name: Lint
# Action refs are pinned to full-length commit SHAs (supply-chain hardening).
# To bump an action, resolve its tag to a commit SHA, e.g.:
#   curl -s https://api.github.com/repos/<owner>/<repo>/commits/<tag>
# Use the "sha" field (the commit, not a tag object SHA), then update the version
# comment to match.

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

permissions:
  contents: read

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4
        with:
          fetch-depth: 0
      - uses: actions/setup-node@49933ea5288caeca8642d1e84afbd3f7d6820020 # v4
        with:
          node-version: 20
      - name: markdownlint
        uses: DavidAnson/markdownlint-cli2-action@21c1be1b93ad9ed58fa840aacc3f279cde2a72ff # v24
        with:
          globs: |
            README.md
            CONTRIBUTING.md
```

- [ ] **Step 4: Write .gitignore**

Create `.gitignore` with exactly:

```
lychee/
```

- [ ] **Step 5: Verify and commit**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering"
python - <<'EOF'
import yaml
for f in [".github/workflows/link-check-pr.yml", ".github/workflows/link-check-schedule.yml", ".github/workflows/lint.yml"]:
    yaml.safe_load(open(f, encoding="utf-8"))
    print(f, "OK")
EOF
grep -c "fail: true" .github/workflows/link-check-pr.yml
grep -c "fail: false" .github/workflows/link-check-schedule.yml
grep -F "workflow_dispatch" .github/workflows/link-check-schedule.yml
git add .github .gitignore
git commit -m "ci: add PR link check, weekly sweep, and lint workflows"
```

- [ ] **Step 5b: Bootstrap issue labels on the new private repo**

```bash
gh label create link-rot --description "Scheduled lychee link-rot report" --color B60205 || true
gh label create suggestion --description "Resource suggestion" --color 0E8A16 || true
gh label list
```

Expected: `link-rot` and `suggestion` both listed.

Expected: all three YAML files parse; `fail: true` appears once in the PR workflow and `fail: false` once in the schedule workflow. (If `pip install pyyaml` was needed in Task 2, it is already present.)

---

### Task 5: Populate README with 40 entries

**Files:**
- Modify: `README.md` (replace the Task 1 stub)

**Interfaces:**
- Produces: the seven section headings the issue form (Task 2) lists; the anchor `CONTRIBUTING.md#7-editorial-neutrality` target consumed by the README itself; the entry set the Task 6 linters and Task 7 CI validate.
- Consumes: the research findings document (all URLs) and the year-resolution procedure in this task.

**Model:** standard

- [ ] **Step 1: Resolve repo and PyPI years**

The README content in Step 2 carries draft years for seven resources. Run this and replace any draft that differs:

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering"
for r in doorstop-dev/doorstop itsallcode/openfasttrace useblocks/sphinx-needs cairis-platform/cairis strictdoc-project/strictdoc; do
  y=$(gh api "repos/$r/releases/latest" --jq '.published_at' 2>/dev/null | cut -c1-4)
  [ -z "$y" ] && y=$(gh api "repos/$r/commits/HEAD" --jq '.commit.committer.date' | cut -c1-4)
  echo "$r -> $y"
done
curl -s https://pypi.org/pypi/reqif/json | python -c "import json,sys; d=json.load(sys.stdin); print('reqif ->', d['urls'][0]['upload_time'][:4])"
```

Year decisions for the rest, per CONTRIBUTING §5:

| Entry | Source | Draft |
|-------|--------|-------|
| Eclipse RMF | latest release date shown on eclipse.dev/rmf | 2019 |
| Volere | template edition date on volere.org | 2019 |
| Pohl & Rupp | publisher page edition year | 2015 |
| Wiegers quality-requirements article | page's last-modified year, else sweep year | 2026 |
| SEBoK | current edition year on the page | 2026 |
| Living pages (EARS, KAOS UCL, OSLC, IREB x3, both IBM pages, ReqView, JAMA, Visure, Polarion, Codebeamer, Modern Requirements, Objectiver) | no visible date, so sweep year | 2026 |
| RE 2025 conference | edition year | 2025 |
| REFSQ | edition year | 2026 |

Pinned years, already settled: 29148 (2011), ARP4754A (2010), ReqIF 1.2 and hub (2016), EARS paper (2009), Wiegers book (2013), KAOS Wiley book (2009), Nuseibeh/Easterbrook (2000), Zave/Jackson (1997), Hull et al. (2011), SWEBOK (2025, v4.0a).

- [ ] **Step 2: Write the full README**

Replace `README.md` with exactly the content below, substituting any corrected years from Step 1. The scope line is the spec's verbatim scope line.

```markdown
# Awesome Requirements Engineering [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Curated list of requirements engineering resources: standards, methods, interchange formats, tools, books, and community.

![Last full sweep: 2026-09](https://img.shields.io/badge/last%20full%20sweep-2026--09-brightgreen)

Part of the awesome-mbse list family (hub private; family pointer is text-only).

Maintained by [JG Systems Consulting Ltd.](https://github.com/jgsystemsconsulting).
See [Editorial neutrality](CONTRIBUTING.md#7-editorial-neutrality).

## Contents

- [Standards and guides](#standards-and-guides)
- [Interchange and integration](#interchange-and-integration)
- [Methods and notation](#methods-and-notation)
- [Books and foundational papers](#books-and-foundational-papers)
- [Open-source tools](#open-source-tools)
- [Commercial tools](#commercial-tools)
- [Learning, certification, and community](#learning-certification-and-community)

## Standards and guides

- [ISO/IEC/IEEE 29148-2011](https://ieeexplore.ieee.org/document/6170935) - The requirements engineering life-cycle processes standard: elicitation, analysis, specification, and management `RE-general` `standard` `paid` (2011).
- [SAE ARP4754A](https://www.sae.org/standards/content/arp4754a/) - Guidelines for development of civil aircraft and systems, the requirements-driven standard in a regulated domain `RE-general` `standard` `paid` (2010).

## Interchange and integration

- [OMG ReqIF 1.2](https://www.omg.org/spec/ReqIF/1.2/) - The Requirements Interchange Format: tool-neutral XML exchange of requirements between tools and organizations `RE-general` `spec` (2016).
- [OMG ReqIF (all versions)](https://www.omg.org/spec/ReqIF/) - OMG spec hub for ReqIF: version index, formal schemas, and related documents `RE-general` `spec` (2016).
- [Eclipse Requirements Modeling Framework](https://eclipse.dev/rmf/) - Open-source reference implementation of ReqIF, including the ProR requirements editor `RE-general` `other-tool` `tool` (2019).
- [reqif (Python library)](https://pypi.org/project/reqif/) - Python library for parsing and writing ReqIF files `RE-general` `other-tool` `tool` (2025).
- [OSLC](https://open-services.net/) - Open standards for linking lifecycle tool chains, including requirements management integration `RE-general` `community` (2026).

## Methods and notation

- [EARS (Easy Approach to Requirements Syntax)](https://alistairmavin.com/ears/) - Alistair Mavin's constrained natural-language patterns for writing requirements `textual` `EARS` `guide` (2026).
- [KAOS and goal-oriented RE (van Lamsweerde)](https://webperso.info.ucl.ac.be/~avl/) - Axel van Lamsweerde's UCL page: the KAOS goal-oriented modeling language, method, and publications `model-based` `KAOS` `guide` (2026).
- [Volere Requirements Specification Template](https://volere.org/) - The Volere template and companion practice material for structured requirements specification `textual` `Volere` `has-template` `template` (2019).
- [Writing Quality Requirements (Karl Wiegers)](https://www.processimpact.com/articles/qualreqs.html) - Karl Wiegers' practice guide to writing high-quality requirements statements `textual` `guide` (2026).

## Books and foundational papers

- [EARS (IEEE RE 2009 paper)](https://doi.org/10.1109/RE.2009.9) - The IEEE RE 2009 paper by Mavin et al. introducing EARS `textual` `EARS` `paper` `paid` (2009).
- [Software Requirements, 3rd ed. (Wiegers & Beatty)](https://www.microsoftpressstore.com/store/software-requirements-9780735679665) - Microsoft Press' end-to-end practitioner handbook on requirements practices `textual` `book` `paid` (2013).
- [Requirements Engineering: From System Goals to UML Models to Software Specifications (van Lamsweerde)](https://www.wiley.com/en-us/Requirements+Engineering%3A+From+System+Goals+to+UML+Models+to+Software+Specifications-p-9780470012703) - The Wiley synthesis of KAOS goal-oriented requirements engineering `model-based` `KAOS` `book` `paid` (2009).
- [Requirements Engineering: A Roadmap (Nuseibeh & Easterbrook)](https://dl.acm.org/doi/10.1145/336512.336523) - The ICSE 2000 roadmap survey of RE research and practice `RE-general` `paper` `paid` (2000).
- [Four Dark Corners of Requirements Engineering (Zave & Jackson)](https://dl.acm.org/doi/10.1145/237432.237434) - The 1997 TOSEM paper defining the requirements-to-specification relationship `RE-general` `paper` `paid` (1997).
- [Requirements Engineering Fundamentals, 2nd ed. (Pohl & Rupp)](https://rockynook.com/product/requirements-engineering-fundamentals-2nd-edition/) - The IREB CPRE Foundation Level study guide from Rocky Nook `RE-general` `book` `paid` (2015).
- [Requirements Engineering, 3rd ed. (Hull, Jackson & Dick)](https://link.springer.com/book/10.1007/978-1-84996-405-0) - Springer text on the RE process and traceability, with DOORS-based tool support `RE-general` `book` `paid` (2011).

## Open-source tools

- [Doorstop](https://github.com/doorstop-dev/doorstop) - Requirements management stored in version control, with documents and traceability views `textual` `other-tool` `tool` (2025).
- [OpenFastTrace](https://github.com/itsallcode/openfasttrace) - Requirement tracing suite that checks coverage across specifications and code `textual` `other-tool` `tool` (2025).
- [sphinx-needs](https://github.com/useblocks/sphinx-needs) - Sphinx extension for managing, linking, and filtering needs and requirements in docs `textual` `other-tool` `tool` (2026).
- [CAIRIS](https://github.com/cairis-platform/cairis) - Platform for modeling requirements together with the security properties they shape `model-based` `other-tool` `tool` (2025).
- [StrictDoc](https://github.com/strictdoc-project/strictdoc) - Requirements and documentation tool with ReqIF support and traceability `textual` `other-tool` `tool` (2026).

## Commercial tools

- [IBM Engineering Requirements Management DOORS Next](https://www.ibm.com/products/requirements-management-doors-next) - IBM's web-based requirements management for engineering lifecycle traceability `RE-general` `DOORS` `tool` `paid` (2026).
- [IBM DOORS family](https://www.ibm.com/products/engineering-requirements-management-doors-family) - The classic DOORS product family for enterprise requirements management `RE-general` `DOORS` `tool` `paid` (2026).
- [ReqView](https://www.reqview.com/) - Git-powered requirements management tool with offline traceability from Eccam `RE-general` `ReqView` `tool` `paid` (2026).
- [JAMA Connect](https://www.jamasoftware.com/platform/jama-connect/) - Jama's platform for requirements management, review, and engineering traceability `RE-general` `Jama` `tool` `paid` (2026).
- [Visure Requirements](https://visuresolutions.com/) - Requirements and ALM platform aimed at regulated industries and traceability `RE-general` `Visure` `tool` `paid` (2026).
- [Siemens Polarion ALM](https://plm.sw.siemens.com/en-US/polarion/) - Siemens' ALM platform with requirements management and traceability `RE-general` `Polarion` `tool` `paid` (2026).
- [Codebeamer](https://codebeamer.com/) - ALM platform with requirements management for safety-critical development `RE-general` `other-tool` `tool` `paid` (2026).
- [Modern Requirements](https://www.modernrequirements.com/) - Requirements management built natively on Azure DevOps `RE-general` `other-tool` `tool` `paid` (2026).
- [Objectiver](https://www.objectiver.com/) - Requirements tool descended from the KAOS goal-modeling lineage `model-based` `KAOS` `other-tool` `tool` `paid` (2026).

## Learning, certification, and community

- [IREB CPRE](https://cpre.ireb.org/en/) - The Certified Professional for Requirements Engineering program, Foundation through Expert `RE-general` `course` `paid` (2026).
- [IREB](https://www.ireb.org/en/) - The International Requirements Engineering Board: schemes, publications, and news `RE-general` `community` (2026).
- [IREB CPRE Recommended Reading](https://cpre.ireb.org/en/downloads-and-resources/recommended-reading) - IREB's reviewed reading list, including free downloadable CPRE handbooks `RE-general` `guide` (2026).
- [RE Magazine (IREB)](https://re-magazine.ireb.org/) - IREB's practitioner magazine on requirements engineering `RE-general` `community` (2026).
- [IEEE International Requirements Engineering Conference (RE)](https://conf.researchr.org/home/RE-2025) - The flagship IEEE conference series for RE research and industry `RE-general` `community` (2025).
- [REFSQ](https://conf.researchr.org/home/refsq-2026) - Requirements Engineering: Foundation for Software Quality, the annual working conference `RE-general` `community` (2026).
- [SEBoK](https://sebokwiki.org/wiki/Guide_to_the_Systems_Engineering_Body_of_Knowledge_%28SEBoK%29) - The Guide to the Systems Engineering Body of Knowledge, with requirements chapters `RE-general` `guide` (2026).
- [SWEBOK Guide V4](https://www.computer.org/education/bodies-of-knowledge/software-engineering) - IEEE's Software Engineering Body of Knowledge, with a dedicated Requirements knowledge area `RE-general` `guide` (2025).
```

- [ ] **Step 3: Run the entry checker**

Run this throwaway check (not committed):

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering"
python - <<'EOF'
import re

text = open("README.md", encoding="utf-8").read()
ENTRY = re.compile(r"^- \[[^\]]+\]\((https?://[^)]+)\) - (.+) \((\d{4})\)\.$")
lines = [l for l in text.splitlines() if ENTRY.match(l)]
assert len(lines) >= 40, f"only {len(lines)} entries"

LANG = {"textual", "model-based", "RE-general"}
METHOD = {"EARS", "KAOS", "Volere", "other-method"}
TOOL = {"DOORS", "ReqView", "Jama", "Visure", "Polarion", "other-tool"}
HAS = {"has-model", "has-template"}
TYPE = {"tutorial","course","book","paper","blog","video","tool","plugin",
        "template","standard","spec","guide","community"}
SPECSTD = {"spec", "standard"}
ORDER = ["language","method","tool","has-model","type","spec/standard","paid","year"]
SEC_MAP = {
    "ieeexplore.ieee.org/document/6170935": "Standards and guides",
    "www.omg.org/spec/ReqIF/1.2/": "Interchange and integration",
    "www.omg.org/spec/ReqIF/": "Interchange and integration",
    "cpre.ireb.org/en/": "Learning, certification, and community",
    "alistairmavin.com/ears/": "Methods and notation",
    "doi.org/10.1109/RE.2009.9": "Books and foundational papers",
    "webperso.info.ucl.ac.be/~avl/": "Methods and notation",
    "wiley.com/en-us/Requirements+Engineering": "Books and foundational papers",
    "microsoftpressstore.com/store/software-requirements-9780735679665": "Books and foundational papers",
    "www.reqview.com/": "Commercial tools",
    "www.ibm.com/products/requirements-management-doors-next": "Commercial tools",
    "www.jamasoftware.com/platform/jama-connect/": "Commercial tools",
    "visuresolutions.com/": "Commercial tools",
}

section, urls = None, set()
for l in text.splitlines():
    if l.startswith("## "):
        section = l[3:].strip()
    m = ENTRY.match(l)
    if not m:
        continue
    url, body, year = m.groups()
    assert url not in urls, f"duplicate URL: {url}"
    urls.add(url)
    for key, want in SEC_MAP.items():
        if key in url:
            assert section == want, f"{url} in '{section}', expected '{want}'"
    desc = re.split(r" `", body)[0]
    assert len(desc) <= 140, f"{len(desc)} chars: {l[:60]}"
    seen, axis = set(), []
    for t in re.findall(r"`([^`]+)`", body):
        if t in LANG: ax = "language"
        elif t in METHOD: ax = "method"
        elif t in TOOL: ax = "tool"
        elif t in HAS: ax = "has-model"
        elif t in TYPE and "type" not in seen: ax = "type"
        elif t in SPECSTD and "spec/standard" not in seen: ax = "spec/standard"
        elif t == "paid": ax = "paid"
        else: raise AssertionError(f"unknown tag {t!r}: {l}")
        seen.add(ax); axis.append(ax)
    assert axis == sorted(axis, key=ORDER.index), f"tag order: {l}"
    assert axis.count("language") == 1 and axis.count("type") == 1, f"cardinality: {l}"
    assert axis.count("method") <= 1 and axis.count("has-model") <= 1 and axis.count("paid") <= 1, l

print(f"OK: {len(lines)} entries, format, tag order, uniqueness, sections")
EOF
```

Expected: `OK: 40 entries, ...` (or more). If a tag-order or section assertion fails, fix the README line it names and rerun.

- [ ] **Step 4: Verify the 12 spec-required URLs are present**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering"
for u in \
  "https://ieeexplore.ieee.org/document/6170935" \
  "https://www.omg.org/spec/ReqIF/1.2/" \
  "https://cpre.ireb.org/en/" \
  "https://alistairmavin.com/ears/" \
  "https://doi.org/10.1109/RE.2009.9" \
  "https://webperso.info.ucl.ac.be/~avl/" \
  "https://www.wiley.com/en-us/Requirements+Engineering%3A+From+System+Goals+to+UML+Models+to+Software+Specifications-p-9780470012703" \
  "https://www.microsoftpressstore.com/store/software-requirements-9780735679665" \
  "https://www.reqview.com/" \
  "https://www.ibm.com/products/requirements-management-doors-next" \
  "https://www.jamasoftware.com/platform/jama-connect/" \
  "https://visuresolutions.com/" ; do
  grep -qF "($u)" README.md || echo "MISSING: $u"
done
```

Expected: no MISSING lines.

- [ ] **Step 5: Sync the CHANGELOG count and commit**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering"
grep -F "entries across seven sections" CHANGELOG.md
# If the checker count differs from the CHANGELOG line, edit CHANGELOG.md to match.
git add README.md CHANGELOG.md
git commit -m "docs: populate README with 40 vetted entries"
```

---

### Task 6: Local lint and link-check pass

**Files:**
- Create (conditional): `.lycheeignore`

**Interfaces:**
- Consumes: README and CONTRIBUTING from Tasks 3 and 5, `.markdownlint-cli2.jsonc` from Task 3, Docker or a draft PR for lychee.
- Produces: `.lycheeignore` entries if any domain blocks the checker; the workflow's `paths` trigger already watches this file.

**Model:** standard

- [ ] **Step 1: markdownlint and awesome-lint locally**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering"
npx -y markdownlint-cli2 "README.md" "CONTRIBUTING.md"
npx -y awesome-lint
```

Expected: both exit clean. awesome-lint resolves the repo slug from the git remote, which exists since Task 1. Fix any findings before moving on; do not weaken lint rules.

- [ ] **Step 2: Lychee locally (Docker), or defer to CI**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering"
docker run --rm -v "$PWD:/d" -w /d lycheeverse/lychee --include-fragments=anchor-only --max-concurrency 4 --accept 200..=299,429 --no-progress README.md
```

If Docker is unavailable, skip to Step 3 and let the CI gate in Task 7 do the checking; that is acceptable because the gate is blocking.

- [ ] **Step 3: Handle bot-blocked domains**

For every URL that lychee reports dead with 403 or an anti-bot response but that opens fine in a browser, add one justified line to `.lycheeignore`. The likely candidates are `dl.acm.org` and IEEE Explore. Create `.lycheeignore` only if needed, in this shape (hub pattern):

```
# URLs that are live in a browser but return 403/anti-scrape to automated
# checkers. Add a line only after confirming the link is genuinely live in a
# browser. Keep this list short. Re-verify during the quarterly sweep.

# ACM Digital Library blocks automated clients (2026-09)
https://dl\.acm\.org/
```

Every line needs a comment with reason and date. Never ignore a genuinely dead link.

- [ ] **Step 4: Commit if .lycheeignore was created**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering"
[ -f .lycheeignore ] && { git add .lycheeignore; git commit -m "ci: ignore bot-blocked domains with justified entries"; } || echo "no ignore needed"
```

---

### Task 7: Open the population PR and verify CI green

**Files:**
- No new files. Pushes the `population` branch and opens the PR to `main`.

**Interfaces:**
- Consumes: all prior commits on `population`; the workflows from Task 4.
- Produces: a merged population PR with lychee, awesome-lint, and markdownlint green on `main`. This is the gate Task 9 waits on.

**Model:** standard

- [ ] **Step 1: Push and open the PR**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering"
git push -u origin population
gh pr create --base main --title "Populate spoke: governance, CI, and 40 entries" --body "Implements the 2026-09-17 spec. README carries 40 vetted entries in seven sections; CI adds blocking lychee plus awesome-lint on PRs, the weekly link-rot sweep, and markdownlint."
```

- [ ] **Step 2: Watch the checks to green**

```bash
gh pr checks --watch
```

Expected: `link-check (PR)` (lychee plus awesome-lint jobs) and `Lint` all pass. If lychee fails on a bot-blocked domain, apply the Task 6 Step 3 rule, push, and re-watch. If awesome-lint fails, fix the README finding; do not bypass.

- [ ] **Step 3: Merge**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering"
gh pr merge --squash --delete-branch
git checkout main && git pull
gh run list --limit 5
```

Expected: PR merged, `main` up to date, the push-triggered `Lint` run green. Record the PR number; Task 9's PR body references it as the CI-green evidence.

---

### Task 8: Prove the weekly sweep via workflow_dispatch

**Files:**
- No new files. Triggers the schedule workflow manually; acceptance criterion 6 forbids waiting for the Monday cron.

**Interfaces:**
- Consumes: `link-check-schedule.yml` on `main` (must be merged first; `workflow_dispatch` needs the workflow on the default branch).
- Produces: one successful manual run and exactly one open `link-rot` issue. This is the second piece of evidence Task 9 cites.

**Model:** flash

- [ ] **Step 1: Dispatch and watch**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering"
gh workflow run link-check-schedule.yml --ref main
sleep 10
run_id=$(gh run list --workflow=link-check-schedule.yml --limit 1 --json databaseId --jq '.[0].databaseId')
gh run watch "$run_id" --exit-status
```

Expected: the run succeeds (the workflow reports; it never fails on dead links).

- [ ] **Step 2: Assert the single-issue shape**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering"
gh issue list --label link-rot --state open --json number,title
gh issue list --label link-rot --state open --json number --jq 'length'
```

Expected: exactly one open issue titled `Weekly link-rot report`, body generated from `lychee/out.md`. Inspect with `gh issue view <number> --json body`. Leave it open; the next Monday run supersedes it. If an earlier run left a second open issue, the close-then-create steps failed; debug the workflow before proceeding.

---

### Task 9: Hub go-live PR (FAMILY registry and README spoke link)

**Files:**
- Modify: `C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse/FAMILY.md` (registry row, registry table row near L53)
- Modify: `C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse/README.md` (spoke link near the top)

**Interfaces:**
- Consumes: Task 7's merged population PR and Task 8's successful dispatch run. Do not open this PR before both exist; FAMILY step 5 ordering and acceptance criteria 5 and 7 forbid the premature flip.
- Produces: the registry row status `Live` and the hub README List family Status/location row. Nothing else in the hub changes.

**Model:** flash

- [ ] **Step 1: Branch in the hub repo**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
git checkout main && git pull
git checkout -b spoke-requirements-engineering-live
```

- [ ] **Step 2: Flip the FAMILY registry status**

In `FAMILY.md` registry table (four columns: Repo | Owns | Status | Visibility),
change exactly the existing requirements-engineering row (do not add a second row):

Old (live hub shape as of 2026-09-17):

```markdown
| awesome-requirements-engineering | Requirements as a discipline: EARS, KAOS, ReqIF, tooling, papers | Planned | none yet |
```

New:

```markdown
| awesome-requirements-engineering | Requirements as a discipline: EARS, KAOS, ReqIF, tooling, papers | Live | private |
```

If the row text drifted, re-read `FAMILY.md` registry before editing; keep four
columns. Status becomes `Live`; Visibility becomes `private` (spoke created private).

Also update the `### awesome-requirements-engineering` checklist under planned
spokes if present: tick create/populate items this run completed; leave
sindresorhus submission unchecked.

- [ ] **Step 3: Update the hub README List family table**

In `README.md` under `## List family`, change exactly the requirements-engineering
table row (not a deleted two-line blurb):

Old:

```markdown
| awesome-requirements-engineering | Requirements as a discipline: EARS, KAOS, ReqIF, tooling, papers | Planned | GAP (absent) |
```

New:

```markdown
| awesome-requirements-engineering | Requirements as a discipline: EARS, KAOS, ReqIF, tooling, papers | Live | Private spoke (org-visible); hub still GAP for RE body copy |
```

Do not add a public markdown link to the private spoke unless the hub already
links other private org repos the same way. Prefer the Status flip + location
note. Re-read the live table before editing if columns moved.

- [ ] **Step 4: Commit, PR, watch, merge**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
git add FAMILY.md README.md
git commit -m "go live: awesome-requirements-engineering spoke"
git push -u origin spoke-requirements-engineering-live
gh pr create --base main --title "Go live: awesome-requirements-engineering spoke" --body "Spoke CI is green: population PR <population PR number> merged with blocking lychee, awesome-lint, and markdownlint; weekly workflow proven via workflow_dispatch (<run id>). Flips the FAMILY registry row to Live and adds the hub README List family Status/location row, per FAMILY step 5."
gh pr checks --watch
gh pr merge --squash --delete-branch
```

Expected: the hub's `link-check (PR)` fires (README.md changed) and passes. The spoke stays private; hub row notes private spoke without requiring an external public URL. awesome-lint stays green. Merge only on green.

- [ ] **Step 5: Confirm the registry shape**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
grep -c "awesome-requirements-engineering" FAMILY.md
grep -F "Live" FAMILY.md | grep -F "requirements-engineering"
```

Expected: the stem appears in the registry table once plus the scope table once (two matches total for `grep -c` counts lines), and the Live row is the requirements-engineering one.

---

### Task 10: Acceptance sweep (CHANGELOG, badge, all nine criteria)

**Files:**
- Modify: `CHANGELOG.md` in the spoke repo only if the entry count changed after Task 5 (the count line must match reality).

**Interfaces:**
- Consumes: everything. This task is the verification pass against the spec's nine acceptance criteria.

**Model:** standard

- [ ] **Step 1: Repo and file set (criteria 1, 2)**

```bash
gh repo view jgsystemsconsulting/awesome-requirements-engineering --json visibility,defaultBranchRef
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering" && git checkout main && git pull
ls README.md CONTRIBUTING.md LICENSE CODE_OF_CONDUCT.md SECURITY.md CHANGELOG.md .markdownlint-cli2.jsonc .github/workflows/link-check-pr.yml .github/workflows/link-check-schedule.yml .github/workflows/lint.yml .github/PULL_REQUEST_TEMPLATE.md .github/ISSUE_TEMPLATE/suggest-resource.yml
head -3 LICENSE
```

Expected: private visibility, main, every file present, CC0 header. If the count line changed, commit `docs: correct sweep entry count` on a small PR, merge it, and rerun Task 8 once so `main` still shows a proven dispatch run.

- [ ] **Step 2: README skeleton and entries (criteria 3, 4)**

Rerun the Task 5 Step 3 checker verbatim; expected `OK` line. Then:

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering"
grep -F "https://awesome.re/badge.svg" README.md
grep -F "last full sweep-2026--09" README.md
grep -F "awesome-mbse list family" README.md
# Must NOT contain a hyperlink to hub FAMILY.md while hub is private:
grep -F "awesome-mbse/blob/main/FAMILY.md" README.md && exit 1 || true
grep -F "CONTRIBUTING.md#7-editorial-neutrality" README.md
```

Expected: all four match. The checker already proved every ToC anchor's target heading exists structurally; lychee's fragment check in CI proves it end to end.

- [ ] **Step 3: CI and sweep proof (criteria 5, 6)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering"
gh run list --limit 10
gh issue list --label link-rot --state open --json number --jq 'length'
```

Expected: the population PR runs and the push-run on `main` all green (lychee `fail: true`, awesome-lint, markdownlint); one open `link-rot` issue from the Task 8 dispatch.

- [ ] **Step 4: Hub flip (criteria 7)**

```bash
gh pr list --repo jgsystemsconsulting/awesome-mbse --state merged --limit 5
```

Expected: the go-live PR merged, and it contains exactly the two edits from Task 9 (`git show` on the squash commit shows only `FAMILY.md` and `README.md`).

- [ ] **Step 5: CHANGELOG and badge match (criterion 8)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering"
grep -E "^## 2026-09" CHANGELOG.md
grep -F "Last full sweep: 2026-09" README.md
```

Expected: both say 2026-09.

- [ ] **Step 6: No copied entry text (criterion 9)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-requirements-engineering"
comm -12 \
  <(grep -oE 'https://[^) ]+' README.md | sed 's/[).,]*$//' | sort -u) \
  <(grep -oE 'https://[^) ]+' "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse/README.md" | sed 's/[).,]*$//' | sort -u)
```

Expected: no resource URLs in the intersection. Allowed leftovers are infrastructure URLs only: `awesome.re`, `img.shields.io`, and `github.com/jgsystemsconsulting` org/family pointers. Every spoke entry line was written fresh in Task 5; a suspicious overlap means an entry was copied, so rewrite it.

- [ ] **Step 7: Final report**

State each of the nine acceptance criteria with its command output. Any criterion without passing output is a failed run: go back to the owning task, not around it.
