# Awesome ArchiMate Spoke Launch Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create the public spoke repository `jgsystemsconsulting/awesome-archimate` per the family standard (FAMILY.md), seed it with verified ArchiMate entries, turn on CI, and flip the hub registry and README to Live.

**Architecture:** A standalone Markdown list repo modeled on the live sibling `jgsystemsconsulting/awesome-sysml-v2` (three GitHub Actions workflows, awesome-lint pin, CC0 license), patched to close the gaps FAMILY.md requires over the sibling: `CONTRIBUTING.md` casing, tagged-and-dated entries, sweep badge, family pointer, lychee fragment checking, and year/dedupe/neutrality rules. Hub edits (registry flip, README spoke link, CHANGELOG entry) land in `awesome-mbse` in the same effort.

**Tech Stack:** git, GitHub CLI (`gh`), Markdown, GitHub Actions (lychee-action, awesome-lint@2.3.0, markdownlint-cli2-action), CC0-1.0 license.

**Spec:** `C:\Users\gower\OneDrive\Documents\GitHub\awesome-mbse\docs\superpowers\specs\2026-09-17-awesome-archimate.md`

**Model scope note:** tasks marked `flash` carry complete file content or exact copy-and-patch strings (transcription work). Tasks marked `standard` involve live-page verification, push/CI watching, or failure triage.

## Research

Gate: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-mbse\docs\superpowers\research\2026-09-17-awesome-archimate-sources-research.md` (retrieved 2026-09-17). Marker: research-gate path plus the key URLs below.

Key verified sources behind the seed entries:

- https://publications.opengroup.org/c226 - ArchiMate 3.2 Specification, document C226, published 2022-10-19.
- https://publications.opengroup.org/c260 - ArchiMate 4 Specification, document C260, published 2026-04-27.
- https://www.opengroup.org/certifications/archimate - personal certification program.
- https://www.opengroup.org/certifications/archimate/tools - tool certification program.
- https://www.opengroup.org/open-group-archimate-model-exchange-file-format - exchange file format.
- https://www.opengroup.org/togaf - TOGAF hub.
- https://www.archimatetool.com/plugins/ - Archi plugins catalog.
- https://github.com/archimatetool/archi - Archi source (MIT).
- https://github.com/archimatetool/archi-scripting-plugin - jArchi.
- https://github.com/archimatetool/archi-modelrepository-plugin - coArchi.
- https://github.com/archimatetool/archi-modelrepository-plugin2 - coArchi 2.
- https://github.com/archimatetool/archi/wiki - Archi wiki.
- https://github.com/archimatetool/ArchiModels - archived example model collection.
- https://github.com/yasenstar/ArchiSurance_Practice - community ArchiSurance practice models.
- https://github.com/archimate-models/archisurance - community ArchiSurance model.
- https://forum.archimatetool.com/ - Archi forum.
- https://community.opengroup.org/archimate-user-community - ArchiMate User Community (provisional: verify browsable at execute, drop if bot-gated).
- https://ea.rna.nl/ - Gerben Wierda, Mastering ArchiMate Edition 3.2.
- https://github.com/search?q=awesome-archimate&type=repositories - namespace check: 0 results on 2026-09-17.

Research corrections carried into this plan: ArchiMate is a standard of The Open Group, never labeled "OMG ArchiMate" in user-facing prose. Marc Hosgen's video course has no confirmed stable URL; it ships only if a live URL verifies at execute, otherwise it and the Tutorials section are omitted.

## Codebase context

Gate: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-mbse\docs\superpowers\context\2026-09-17-awesome-archimate-pattern-context.md`.

- FAMILY.md (`awesome-mbse/FAMILY.md`) is the normative standard: badges, entry format with tags and `(YYYY)` year, required files, CI with `--include-fragments anchor-only`, quarterly sweep cadence.
- `awesome-sysml-v2` is a partial template only: three workflows and `awesome-lint@2.3.0` are reusable, but it has lowercase `contributing.md`, no tags or years, no sweep badge, no family pointer, no fragment check.
- The hub registry lists `awesome-archimate` as Planned with an empty-namespace note dated 2026-09-17; the scope boundary routes ArchiMate viewpoints, the Archi tool, and TOGAF-aligned modeling to this spoke.
- The hub README's "List family" paragraph points only at FAMILY.md today; adding the live-spoke sentence is launch step 5 of the family process.
- Hub CONTRIBUTING.md sections 5 (year rule) and 6 (canonical-URL rule) are copied verbatim into spoke CONTRIBUTING.md. A separate spoke-only addendum covers undated web pages (verification year). Section 7 (neutrality) is adapted, not copied blind.

## Global Constraints

- Repo: `jgsystemsconsulting/awesome-archimate`, public, default branch `main`. Local clone: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-archimate`.
- Minimum 15 live entries at open; 18 seeds targeted. Depth waiver 2026-09-17: the roughly-40-entry bar is deferred to the first full sweep, not a create blocker.
- Entry format (FAMILY normative): `- [Resource Name](url) - One-line factual description \`tags\` (YYYY).` Hyphen separator (` - `) only, never an en or em dash. Description at most 140 characters, measured from the first character after ` - ` to the last character before the first tag. Tags are inline code spans in the axis order `language` -> `method` -> `tool` -> `has-model` -> `type` -> `spec/standard` -> `paid`. The year suffix `(YYYY)` comes last and is not a code span.
- Tag values: language exactly one of `ArchiMate3` / `ArchiMate4` / `ArchiMate-general`; method 0-1 of `TOGAF`; tool 0+ of `Archi` / `other-tool`; has-model 0-1; type 0-1 (required unless `spec` or `standard` present); spec/standard 0-1 of `spec` / `standard`; paid 0-1.
- Open Group branding in all user-facing prose. The string "OMG ArchiMate" appears nowhere in README.md, CONTRIBUTING.md, SECURITY.md, or CHANGELOG.md (LICENSE and workflow YAML are exempt).
- The list links; it never re-hosts model files or PDFs.
- LICENSE is CC0-1.0.
- PR link check is advisory (`fail: false`), matching awesome-sysml-v2. Scheduled and manual link runs open a report issue on failure. Lint gates block merge.
- `awesome-lint@2.3.0` pin exact. All `uses:` action refs pinned to full-length 40-character commit SHAs (copied verbatim from the sibling).
- README: Awesome badge, one-line scope, Last full sweep badge (2026-09), family pointer, maintainer line, flat hand-maintained ToC listing only sections that ship at least one entry. No empty sections.
- Family pointer rule: while the hub repo `jgsystemsconsulting/awesome-mbse` is private, the spoke carries the family pointer as text only, no hyperlink (FAMILY.md private mode; the sibling's live-spoke alignment checklist confirms this practice). The hyperlinked pointer from the spec header block is used only if `gh repo view jgsystemsconsulting/awesome-mbse --json visibility` reports PUBLIC at execute. Text-only is the default.
- No submission to `sindresorhus/awesome` in this effort. No hub content moves. No commercial tool entries unless a durable product page verifies at execute (none are seeded).
- CI workflows run on Node 20 in CI; local lint needs Node/npx on PATH. `gh` must be authenticated as `jgsystemsconsulting`.

## File structure

New repo `awesome-archimate` at launch:

| File | Source |
|---|---|
| `README.md` | New, written in Task 4 (FAMILY skeleton + spec header block + 18 seed entries) |
| `CONTRIBUTING.md` | New, written in Task 3 (hub sections 5 and 6 verbatim, spoke undated-page addendum, adapted bar and neutrality, spoke tag table) |
| `LICENSE` | Copied from `awesome-sysml-v2/LICENSE` (CC0-1.0) |
| `CODE_OF_CONDUCT.md` | Copied from `awesome-sysml-v2/CODE_OF_CONDUCT.md` (already names jgsystemsconsulting; no edits needed) |
| `SECURITY.md` | New, hub text verbatim (curated-list scope, support@jgsystemsconsulting.com) |
| `CHANGELOG.md` | New, Keep a Changelog format like the sibling, with the launch entry |
| `.markdownlint-cli2.jsonc` | Copied as-is from the sibling |
| `.github/workflows/links.yml` | Copied from sibling, one arg added (`--include-fragments anchor-only`) |
| `.github/workflows/lint.yml` | Copied from sibling, glob `contributing.md` changed to `CONTRIBUTING.md` |
| `.github/workflows/stale.yml` | Copied from sibling, report message reworded to the spoke inclusion bar |

Hub repo edits (Task 7): `awesome-mbse/FAMILY.md`, `awesome-mbse/README.md`, `awesome-mbse/CHANGELOG.md`.

Optional additions only on evidence at execute: `CITATION.cff`, `.lycheeignore` (add `.lycheeignore` only if a URL is live in a browser but blocks automated checkers, then list it there).

---

### Task 1: Namespace recheck, repo create, sibling clone

**Files:**

- Create: GitHub repo `jgsystemsconsulting/awesome-archimate` (public)
- Create: local clone `C:\Users\gower\OneDrive\Documents\GitHub\awesome-archimate`

**Interfaces:**

- Produces: local clone with `origin` set to `https://github.com/jgsystemsconsulting/awesome-archimate.git`; later tasks work inside this clone.

**Model:** flash

- [ ] **Step 1: Preconditions**

```bash
gh auth status
node --version
test -d "/c/Users/gower/OneDrive/Documents/GitHub/awesome-sysml-v2"
test -f "/c/Users/gower/OneDrive/Documents/GitHub/awesome-sysml-v2/.github/workflows/links.yml"
test -f "/c/Users/gower/OneDrive/Documents/GitHub/awesome-mbse/SECURITY.md"
```

Expected: logged in as `jgsystemsconsulting`; Node 18+ present (CI uses Node 20); sibling `awesome-sysml-v2` clone present with workflows (Task 2 copies from it); hub `SECURITY.md` present.

- [ ] **Step 2: Namespace recheck, same day as creation**

```bash
gh api "search/repositories?q=awesome-archimate+in:name" --jq '.total_count'
```

Expected output: `0`. If nonzero, inspect:

```bash
gh api "search/repositories?q=awesome-archimate+in:name" --jq '.items[] | {full_name, stargazers_count, pushed_at}'
```

An incumbent of substance (100+ stars, or updated within the last year) means STOP: do not create the repo, report the incumbent instead.

- [ ] **Step 3: Create the public repo and clone it as a sibling**

```bash
cd "/c/Users/gower/OneDrive/Documents/GitHub"
gh repo create jgsystemsconsulting/awesome-archimate --public \
  --description "Curated, vetted, dated list of ArchiMate resources: Open Group specifications and certification, the Archi tool and its plugins, books, and openable example models." \
  --clone
```

- [ ] **Step 4: Verify**

```bash
cd "/c/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
git remote -v
gh repo view jgsystemsconsulting/awesome-archimate --json visibility,isPrivate
```

Expected: `origin` points at the new repo; visibility `PUBLIC`. The working tree is empty (no commits yet; the default branch becomes `main` at the first push in Task 6).

No commit (nothing to commit yet).

---

### Task 2: Port static files from the sibling and hub

**Files:**

- Create: `LICENSE`, `CODE_OF_CONDUCT.md`, `.markdownlint-cli2.jsonc` (copied)
- Create: `.github/workflows/links.yml`, `.github/workflows/lint.yml`, `.github/workflows/stale.yml` (copied, then patched in Task 5)
- Create: `SECURITY.md`, `CHANGELOG.md` (new content below)

**Interfaces:**

- Consumes: sibling clone at `C:\Users\gower\OneDrive\Documents\GitHub\awesome-sysml-v2`.
- Produces: `SECURITY.md` and `CHANGELOG.md` content final; `SECURITY.md` mentions `support@jgsystemsconsulting.com` (hub pattern, not the sibling's GitHub-only reporting).

**Model:** flash

- [ ] **Step 1: Copy the verbatim files**

```bash
cd "/c/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
mkdir -p .github/workflows
cp "/c/Users/gower/OneDrive/Documents/GitHub/awesome-sysml-v2/LICENSE" LICENSE
cp "/c/Users/gower/OneDrive/Documents/GitHub/awesome-sysml-v2/CODE_OF_CONDUCT.md" CODE_OF_CONDUCT.md
cp "/c/Users/gower/OneDrive/Documents/GitHub/awesome-sysml-v2/.markdownlint-cli2.jsonc" .markdownlint-cli2.jsonc
cp "/c/Users/gower/OneDrive/Documents/GitHub/awesome-sysml-v2/.github/workflows/links.yml" .github/workflows/links.yml
cp "/c/Users/gower/OneDrive/Documents/GitHub/awesome-sysml-v2/.github/workflows/lint.yml" .github/workflows/lint.yml
cp "/c/Users/gower/OneDrive/Documents/GitHub/awesome-sysml-v2/.github/workflows/stale.yml" .github/workflows/stale.yml
```

- [ ] **Step 2: Write SECURITY.md (hub text verbatim)**

Create `SECURITY.md` with exactly this content:

```markdown
# Security Policy

This repository is a curated index of links — it ships no executable product. The main
security surface is the links it points to and the CI workflows.

## Reporting

If you find a malicious, hijacked, or compromised linked resource, or an issue with the
repository's automation, report it privately to **support@jgsystemsconsulting.com**.

Please do not open a public issue for a suspected malicious link until it has been
reviewed. We aim to acknowledge reports within a few business days.
```

(The em dash in line 3 is quoted from the hub original; files copied or quoted verbatim from the hub keep their punctuation. Do not introduce new em dashes in any other file.)

- [ ] **Step 3: Write CHANGELOG.md**

Create `CHANGELOG.md` with exactly this content:

```markdown
# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- Initial launch of Awesome ArchiMate: 18 entries across eight content sections, all links
  verified at open (launch lychee run exit 0).
- Family-standard files: README, CONTRIBUTING, LICENSE (CC0-1.0), CODE_OF_CONDUCT,
  SECURITY, and three CI workflows (links, lint, freshness).
```

If the link check in Task 6 trims entries, update the count in the first bullet to the number of entries actually shipped before the Task 6 push. If Books (or any content section) is removed, also rewrite "eight content sections" to the shipped content-section count.

- [ ] **Step 4: Verify the copies**

```bash
cd "/c/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
head -3 LICENSE
grep -n "support@jgsystemsconsulting.com" SECURITY.md
ls -A
```

Expected: LICENSE shows CC0 1.0 Universal; SECURITY.md shows the email; the tree lists at least LICENSE, CODE_OF_CONDUCT.md, SECURITY.md, CHANGELOG.md, `.markdownlint-cli2.jsonc`, and `.github` (README and CONTRIBUTING arrive in later tasks).

- [ ] **Step 5: Commit**

```bash
cd "/c/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
git add -A
git commit -m "chore: port family-standard files from awesome-sysml-v2 and awesome-mbse"
git branch -M main
```

---

### Task 3: Write CONTRIBUTING.md

**Files:**

- Create: `CONTRIBUTING.md`

**Interfaces:**

- Produces: anchors `#inclusion-bar` and `#editorial-neutrality` (the README links `CONTRIBUTING.md#editorial-neutrality`; Task 5's `stale.yml` message cites criterion 4 of the Inclusion bar).

**Model:** flash

- [ ] **Step 1: Write the file**

Create `CONTRIBUTING.md` with exactly this content. Inside it, the year-rule body and the canonical-URL rule body match hub CONTRIBUTING.md sections 5 and 6 verbatim. The undated-page paragraph is a spoke-only addendum in its own heading, not part of the hub year-rule text.

````markdown
# Contributing to Awesome ArchiMate

Thanks for helping keep this the best-curated ArchiMate index anywhere. Read this
before opening a PR: CI gates enforce most of it.

The fastest path: open an issue, or open a pull request that edits `README.md` directly.

## Inclusion bar

An entry is accepted only if **all** hold:

1. **On-topic**: genuinely about ArchiMate (any version), the Archi tool and its
   plugins, or enterprise architecture modeling practice around them.
2. **Substantive**: it teaches, demonstrates, specifies, or provides something usable.
   Not a stub. Not pure vendor marketing.
3. **Live**: the link resolves right now.
4. **Active or foundational**: maintained (commit within 24 months) or foundational
   value: a formal specification, certification program, or other canonical reference
   whose value does not depend on recent commits.
5. **Not duplicative**: not already listed (see the canonical-URL rule below).
6. **Legally linkable**: publicly accessible. We link, we never re-host model files,
   PDFs, or proprietary content.

Tie-breakers (nice-to-have, not gates): has a real openable model (`has-model`),
recently updated, from a recognized source (The Open Group, a university, an
established practitioner).

## Entry format

One line per entry, **hyphen separator** (` - `, never an en/em dash: awesome-lint
rejects those), tags as **inline code spans inside the sentence before the year
token**, year parenthesized as the last token:

```markdown
- [Resource Name](https://example.com) - One-line factual description `ArchiMate3` `Archi` `has-model` `tutorial` (2024).
```

- **Description:** factual, one line, **at most 140 characters** (measured from the
  first character after ` - ` to the last character before the first tag, excluding
  the link markup and tags). No hype.
- **`has-model`** means: a directly downloadable, non-paywalled `.archimate` file or
  ArchiMate Exchange Format model that opens in a named tool, or a repository or
  collection whose documented contents include at least one such file. Screenshots,
  papers describing a model, and access-gated or request-only files do not qualify.

## Tag vocabulary, cardinality and order

Tags appear in this fixed order, drawn **only** from this vocabulary:

`language -> method -> tool -> has-model -> type -> spec/standard -> paid -> year`

| Axis | Cardinality | Values |
|------|-------------|--------|
| language | exactly 1 | `ArchiMate3` (3.x, including 3.2) · `ArchiMate4` · `ArchiMate-general` (version-agnostic: methodology, books, both-version docs; not a lazy default) |
| method | 0 or 1 | `TOGAF` |
| tool | 0 or more | `Archi` · `other-tool` |
| has-model | 0 or 1 | `has-model` |
| type | 0 or 1 | `tutorial` · `course` · `book` · `paper` · `blog` · `docs` · `video` · `tool` · `plugin` · `certification` · `example` · `community` · `mcp` |
| spec/standard | 0 or 1 | `spec` · `standard` |
| paid | 0 or 1 | `paid` |
| year | exactly 1 | `(YYYY)` after the tags, not a code span (see The year rule) |

- `other-tool` graduates to its own tag once 3 or more entries share it.
- The type tag is **required unless `spec` or `standard` is present**: a pure
  specification row carries its language tag plus `spec` or `standard` only.
- Type value notes: `certification` marks a certification program or registry page;
  `example` marks a collection or repository of example models; `community` marks a
  forum or community hub; `docs` marks a wiki or documentation home, not a single
  blog post.
- For an Open Group normative document use `spec` or `standard` and omit `paper`.

## The year rule (`YYYY`)

`(YYYY)` = the year of the resource's **most recent author-published version**:

- a paper → its publication year;
- a repo → its latest tagged release, or the latest default-branch commit if untagged;
- a course → its current cohort year.

**Trivial edits (typo fixes) don't count.** Examples:

- A 2019 paper with a 2024 typo-fix commit → `(2019)`.
- A repo whose latest release tag is `v2.1` from 2023 → `(2023)`.

### Spoke addendum: undated pages

A web page with no visible publication or revision date takes the year it was last
verified during a sweep. This sentence is spoke-only; it is not part of the hub year rule.

## Canonical-URL rule (dedupe)

Before deciding "is this a duplicate", canonicalize both URLs: force `https`, lowercase
the host, strip a trailing slash, drop the query string and fragment unless they're
semantically required. If the canonical forms match, it's a duplicate.

## Editorial neutrality

This list is maintained by JG Systems Consulting Ltd. Current position: JGS sells no
ArchiMate-niche product, so no product disclosure applies today. The rules that hold:

- JGS products are listed by the **same inclusion bar** as everything else.
- Every JGS entry sits next to **at least 1 genuine competing or alternative entry**.
- **A superior competing tool is listed above a JGS one.** Neutrality is enforced by
  this rule, not by tone.

If JGS ships an ArchiMate-niche product, this section gains the product disclosure
before any JGS entry is listed.

## Local checks

Run from the repository root before opening a PR:

```bash
npx awesome-lint@2.3.0 README.md
npx markdownlint-cli2 "README.md" "CONTRIBUTING.md"
```

### Link check

`lychee` is a native binary, not an npm package. Install it once with your platform
package manager (`scoop`, `winget`, or `choco` on Windows, `brew` on macOS, `pacman`,
`zypper`, `snap`, or `apk` on Linux), then run from the repository root:

```bash
lychee --no-progress --max-retries 3 --include-fragments anchor-only README.md
```

Export `GITHUB_TOKEN` (for example `GITHUB_TOKEN=$(gh auth token)`) to avoid GitHub
rate limiting on `github.com` links. Third-party sites sometimes return transient
timeouts or 429s; retry before treating a failure as a broken link.

## Maintenance

Three workflows in `.github/workflows/` run on a fixed cadence. This section states
what each does.

### Link scan (weekly)

`links.yml` runs lychee every Monday at 18:00 UTC, on every pull request, and on
manual dispatch. PR runs are advisory: a PR with broken links gets a warning but is
never blocked by it. Scheduled and manual runs create or update a "Link Checker
Report" issue when the check exits nonzero; a clean run leaves that issue untouched.
Fragment checking (`--include-fragments anchor-only`) validates that every
table-of-contents anchor resolves.

### Freshness report (monthly)

`stale.yml` runs on the first day of each month at 06:00 UTC, or on manual dispatch.
It collects the `github.com` repository URLs from README.md and lists repos with no
push in the last 24 months. The report is advisory: an entry past the window can
still be valid under the foundational-value exception (criterion 4 of the Inclusion
bar). The "Freshness report" issue is refreshed on every run, including months with
no stale entries.

### Lint gates (every PR and push to main)

`lint.yml` runs `awesome-lint@2.3.0` on README.md, and `markdownlint` on README.md
and CONTRIBUTING.md, on every pull request targeting main and every push to main.
These gates block merge on failure. The local markdownlint command above installs an
unpinned npx package and may differ from the version CI runs; the pinned
`awesome-lint@2.3.0` matches CI exactly.
````

- [ ] **Step 2: Verify anchors and lint**

```bash
cd "/c/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
grep -n "^## Inclusion bar" CONTRIBUTING.md
grep -n "^## Editorial neutrality" CONTRIBUTING.md
grep -c "\-\-" CONTRIBUTING.md || true
```

Expected: both headings present. The third check is informational; the only double-hyphen occurrences allowed are the ` - ` separators inside the entry-format examples and `--include-fragments` flags.

- [ ] **Step 3: Commit**

```bash
cd "/c/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
git add CONTRIBUTING.md
git commit -m "docs: add CONTRIBUTING with inclusion bar, tag vocabulary, year and dedupe rules"
```

---

### Task 4: Write README.md with the seed entries

**Files:**

- Create: `README.md`

**Interfaces:**

- Consumes: `CONTRIBUTING.md#editorial-neutrality` anchor from Task 3.
- Produces: 18 entries in FAMILY format; the ToC anchors that Task 5's lychee fragment check validates.

**Model:** standard

Year evidence (looked up 2026-09-17; re-verify in Step 1 and adjust if changed):

| Entry | Year | Basis and evidence |
|---|---|---|
| ArchiMate 3.2 Specification | 2022 | document C226, published 2022-10-19 |
| ArchiMate 4 Specification | 2026 | document C260, published 2026-04-27 |
| Exchange format, certifications (2), plugins page, TOGAF, forum, User Community | 2026 | undated pages: spoke addendum under The year rule (not hub §5) assigns the verification year; launch verification year is 2026 |
| Archi | 2026 | latest tag `release_5.10.0`, tag commit 2026-09-03 |
| Archi Wiki | 2026 | wiki git last edit 2026-09-15 |
| jArchi | 2026 | latest tag `v1.12.0`, tag commit 2026-04-05 |
| coArchi | 2026 | latest tag `0.9.7`, tag commit 2026-08-21 |
| coArchi 2 | 2026 | latest tag `v1.3.4`, tag commit 2026-06-15 |
| Mastering ArchiMate | 2022 | research marks Edition 3.2 on ea.rna.nl as provisional; use (2022) only if Step 1 browser check finds an explicit edition or publication year on the page (or a durable subpage). If no year is stated, drop the book entry rather than invent a ship date |
| ArchiModels | 2021 | last push 2021-02-11 (repo archived) |
| ArchiSurance Practice | 2026 | last push 2026-01-26 |
| ArchiSurance (archimate-models) | 2017 | last push 2017-05-22 |

- [ ] **Step 1: Re-verify the year inputs (spot check, do not skip)**

```bash
gh api "repos/archimatetool/archi/tags?per_page=1" --jq '.[0].name'
gh api "repos/archimatetool/archi/commits/release_5.10.0" --jq '.commit.committer.date'
gh api "repos/archimatetool/ArchiModels" --jq '.pushed_at'
gh api "repos/yasenstar/ArchiSurance_Practice" --jq '.pushed_at'
gh api "repos/archimate-models/archisurance" --jq '.pushed_at'
gh api "repos/archimatetool/archi-scripting-plugin/commits/v1.12.0" --jq '.commit.committer.date'
gh api "repos/archimatetool/archi-modelrepository-plugin/commits/0.9.7" --jq '.commit.committer.date'
gh api "repos/archimatetool/archi-modelrepository-plugin2/commits/v1.3.4" --jq '.commit.committer.date'
```

Expected: the tag names and dates match the table above. If any moved to a later year, update that entry's year token. Check https://ea.rna.nl/ and any Mastering ArchiMate Edition 3.2 subpage for an explicit edition or publication year; keep (2022) only when the page states it, otherwise omit the book entry **and** remove the `## Books` heading, the Books ToC bullet, and any CHANGELOG claim that lists a Books section or "eight content sections"; then recount shipped entries and content sections. Check https://forum.archimatetool.com/ shows activity in 2026 (else use the visible activity year).

- [ ] **Step 2: Write the README**

Create `README.md` with exactly this content:

```markdown
# Awesome ArchiMate [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated, vetted, dated list of ArchiMate resources: Open Group specifications and
> certification, the Archi tool and its plugins, books, and openable example models.

![Last full sweep: 2026-09](https://img.shields.io/badge/last%20full%20sweep-2026--09-brightgreen)

Part of the awesome-mbse list family; the registry and family rules live in FAMILY.md
in the jgsystemsconsulting/awesome-mbse repository.

Maintained by [JG Systems Consulting Ltd.](https://github.com/jgsystemsconsulting).
See [Editorial neutrality](CONTRIBUTING.md#editorial-neutrality).

## Contents

- [Specifications and standards](#specifications-and-standards)
- [Certification](#certification)
- [The Archi tool](#the-archi-tool)
- [Plugins and collaboration](#plugins-and-collaboration)
- [Books](#books)
- [Example models](#example-models)
- [TOGAF alignment](#togaf-alignment)
- [Communities](#communities)
- [Contributing](#contributing)

## Specifications and standards

- [ArchiMate 3.2 Specification](https://publications.opengroup.org/c226) - The Open Group standard defining the ArchiMate 3.2 modeling language, document C226 `ArchiMate3` `spec` (2022).
- [ArchiMate 4 Specification](https://publications.opengroup.org/c260) - The Open Group standard defining the ArchiMate 4 modeling language, document C260, published April 2026 `ArchiMate4` `spec` (2026).
- [ArchiMate Model Exchange File Format](https://www.opengroup.org/open-group-archimate-model-exchange-file-format) - The Open Group specification for the XML-based interchange format for ArchiMate models `ArchiMate-general` `spec` (2026).

## Certification

- [ArchiMate Certification](https://www.opengroup.org/certifications/archimate) - The Open Group certification program for individuals: Foundation and Practitioner levels `ArchiMate-general` `certification` (2026).
- [ArchiMate Tool Certification](https://www.opengroup.org/certifications/archimate/tools) - The Open Group certification program for ArchiMate modeling tools `ArchiMate-general` `certification` (2026).

## The Archi tool

- [Archi](https://github.com/archimatetool/archi) - Open-source ArchiMate modeling tool for Windows, macOS, and Linux, with full ArchiMate 3.2 support `ArchiMate3` `Archi` `tool` (2026).
- [Archi Wiki](https://github.com/archimatetool/archi/wiki) - Official Archi wiki: user guides, how-tos, and plugin documentation `ArchiMate-general` `Archi` `docs` (2026).

## Plugins and collaboration

- [Archi plugins](https://www.archimatetool.com/plugins/) - Catalog of official Archi plugins: jArchi scripting, coArchi collaboration, visualization, and more `ArchiMate-general` `Archi` `plugin` (2026).
- [jArchi](https://github.com/archimatetool/archi-scripting-plugin) - Official Archi scripting plugin: automate model queries, reports, and content generation with JavaScript `ArchiMate-general` `Archi` `plugin` (2026).
- [coArchi](https://github.com/archimatetool/archi-modelrepository-plugin) - Archi plugin adding Git-based model collaboration: shared repositories, commits, and compare `ArchiMate-general` `Archi` `plugin` (2026).
- [coArchi 2](https://github.com/archimatetool/archi-modelrepository-plugin2) - Second-generation coArchi plugin for Git-based shared model repositories in Archi `ArchiMate-general` `Archi` `plugin` (2026).

## Books

- [Mastering ArchiMate](https://ea.rna.nl/) - Gerben Wierda's practitioner book on ArchiMate, Edition 3.2, with free ArchiMate overview PDFs `ArchiMate3` `book` (2022).

## Example models

- [ArchiModels](https://github.com/archimatetool/ArchiModels) - Archived official collection of example ArchiMate models that open in Archi; kept as reference material `ArchiMate3` `Archi` `has-model` `example` (2021).
- [ArchiSurance Practice](https://github.com/yasenstar/ArchiSurance_Practice) - Community practice models recreating the ArchiSurance case study in Archi `ArchiMate3` `Archi` `has-model` `example` (2026).
- [ArchiSurance (archimate-models)](https://github.com/archimate-models/archisurance) - The ArchiSurance example model from the ArchiMate specification, packaged for Archi `ArchiMate3` `Archi` `has-model` `example` (2017).

## TOGAF alignment

- [TOGAF](https://www.opengroup.org/togaf) - The Open Group TOGAF standard hub; TOGAF is the enterprise architecture method ArchiMate viewpoints serve `ArchiMate-general` `TOGAF` `standard` (2026).

## Communities

- [Archi forum](https://forum.archimatetool.com/) - Community support forum for Archi users: troubleshooting, plugin discussion, and scripting help `ArchiMate-general` `Archi` `community` (2026).
- [Open Group ArchiMate User Community](https://community.opengroup.org/archimate-user-community) - The Open Group hub for the ArchiMate User Community: shared models and working groups `ArchiMate-general` `community` (2026).

## Contributing

Contributions welcome: see [CONTRIBUTING.md](CONTRIBUTING.md) for the inclusion bar,
entry format, and tag vocabulary.
```

Family pointer note: the block above uses the text-only pointer because the hub registry lists `awesome-mbse` as private, and a hyperlinked private-repo URL would fail the launch lychee gate and 404 for outside readers. Before writing the file, run:

```bash
gh repo view jgsystemsconsulting/awesome-mbse --json visibility --jq .visibility
```

If the output is `PUBLIC` (hub released), replace the pointer paragraph with the spec's hyperlinked form:

```markdown
Part of the [awesome-mbse list
family](https://github.com/jgsystemsconsulting/awesome-mbse/blob/main/FAMILY.md).
```

- [ ] **Step 3: Verify the two provisional entries**

1. Open https://community.opengroup.org/archimate-user-community in a browser. If it is browsable (no bot gate beyond normal use), keep the entry. If it is bot-gated or unreachable, delete that entry line (the Communities section still ships the forum, so no empty section).
2. Marc Hosgen's course: search once more for a stable primary URL (his site, YouTube channel, or The Open Group education pages). Only if a URL verifies live, add a `Tutorials and courses` section between `Books` and `Example models` plus the matching ToC line, with one entry following the entry format (`ArchiMate-general` or `ArchiMate3` language tag, `course` type). Absent a verified URL, ship nothing for it; the default is omission.

- [ ] **Step 4: Run the entry-format check**

```bash
cd "/c/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
python - <<'PY'
import re, sys
text = open("README.md", encoding="utf-8").read()
# Real entries only: markdown link with http(s) URL and " - " description separator.
# ToC lines are `- [Label](#anchor)` and must not be counted.
entry_re = re.compile(r"^- \[[^]]+\]\((https?://[^)]+)\) - (.*)$")
lines = [l for l in text.splitlines() if entry_re.match(l)]
bad = []
for line in lines:
    m = entry_re.match(line)
    desc = m.group(2).split("`")[0].rstrip()
    if len(desc) > 140:
        bad.append((f"len {len(desc)}", line[:60]))
    if not re.search(r"` \(20\d{2}\)\.$", line):
        bad.append(("year-last", line[:60]))
    tags = re.findall(r"`([^`]+)`", m.group(2))
    if not tags or not tags[0].startswith("ArchiMate"):
        bad.append(("language-tag", line[:60]))
    if any(c in line for c in ("\u2013", "\u2014")):
        bad.append(("dash", line[:60]))
print(f"{len(lines)} entries checked")
for b in bad:
    print("FAIL", b)
sys.exit(1 if bad or len(lines) < 15 else 0)
PY
```

Expected: `18 entries checked` (or fewer if provisionals dropped, still >= 15), no FAIL lines, exit 0. ToC lines are ignored.

- [ ] **Step 5: Run the lint gates**

```bash
cd "/c/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
npx awesome-lint@2.3.0 README.md
npx markdownlint-cli2 "README.md" "CONTRIBUTING.md"
```

Expected: both exit 0 with no reported problems. awesome-lint validates the Awesome badge, the `## Contents` ToC against the headings, and the entry lines. If awesome-lint reports a ToC mismatch, a section was renamed or dropped without updating the ToC; fix the ToC.

- [ ] **Step 6: Commit**

```bash
cd "/c/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
git add README.md
git commit -m "docs: add README with 18 seed entries in family entry format"
```

(Adjust the message count if the User Community entry was dropped.)

---

### Task 5: Patch the three workflows

**Files:**

- Modify: `.github/workflows/links.yml`
- Modify: `.github/workflows/lint.yml`
- Modify: `.github/workflows/stale.yml`

**Interfaces:**

- Consumes: sibling workflow files copied in Task 2; the CONTRIBUTING.md headings from Task 3.
- Produces: lychee args with `--include-fragments anchor-only` (launch gate and ToC validation), `CONTRIBUTING.md` glob in lint, stale.yml message citing the spoke inclusion bar.

**Model:** flash

- [ ] **Step 1: Patch links.yml**

In `.github/workflows/links.yml`, change the `args:` line:

From:

```yaml
          args: --no-progress --max-retries 3 README.md
```

To:

```yaml
          args: --no-progress --max-retries 3 --include-fragments anchor-only README.md
```

Leave the `fail: false` line and both pinned SHAs untouched.

- [ ] **Step 2: Patch lint.yml**

In `.github/workflows/lint.yml`, change the globs block:

From:

```yaml
          globs: |
            README.md
            contributing.md
```

To:

```yaml
          globs: |
            README.md
            CONTRIBUTING.md
```

Leave `npx awesome-lint@2.3.0 README.md` and all pinned SHAs untouched.

- [ ] **Step 3: Patch stale.yml**

In `.github/workflows/stale.yml`, change the report-header echo line inside the "Build freshness report" step:

From:

```bash
            echo "Entries with no push in over 24 months (as of $(date -u +%Y-%m-%d)). Advisory only: entries meeting the foundational-value exception (contributing.md criterion 4) are still valid."
```

To:

```bash
            echo "Entries with no push in over 24 months (as of $(date -u +%Y-%m-%d)). Advisory only: entries meeting the foundational-value exception (criterion 4 of the Inclusion bar in CONTRIBUTING.md) are still valid."
```

- [ ] **Step 4: Verify the patches**

```bash
cd "/c/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
grep -n "anchor-only" .github/workflows/links.yml
grep -n "fail: false" .github/workflows/links.yml
grep -n "awesome-lint@2.3.0" .github/workflows/lint.yml
grep -n "CONTRIBUTING.md" .github/workflows/lint.yml
grep -n "Inclusion bar" .github/workflows/stale.yml
grep -cE "uses: .*@[0-9a-f]{40}" .github/workflows/*.yml
```

Expected: one `anchor-only` hit and one `fail: false` in links.yml; the awesome-lint pin and CONTRIBUTING.md glob in lint.yml; the Inclusion bar citation in stale.yml; SHA-pin counts of 2 (links), 3 (lint), 1 (stale).

- [ ] **Step 5: Commit**

```bash
cd "/c/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
git add .github/workflows
git commit -m "ci: fragment checking, CONTRIBUTING glob, and inclusion-bar citation per family standard"
```

---

### Task 6: Launch gate (lychee exit 0), push, and CI green

**Files:**

- No new files. Pushes the four commits from Tasks 2 through 5 to `origin/main`.

**Interfaces:**

- Consumes: the full working tree from Tasks 2 through 5.
- Produces: the public repo state that Task 7 links from the hub; CI runs on `main`.

**Model:** standard

- [ ] **Step 1: Run the launch lychee gate locally (ship gate: must exit 0)**

```bash
cd "/c/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
export GITHUB_TOKEN=$(gh auth token)
lychee --no-progress --max-retries 3 --include-fragments anchor-only README.md
echo "exit=$?"
```

Expected: summary shows 0 errors, `exit=0`. This is the maintainer-run launch check the spec names as the ship gate.

If lychee is not installed: `scoop install lychee` (or `winget install lycheeverse.lychee`), then rerun. Docker fallback (Windows Git Bash):

```bash
docker run --rm -e GITHUB_TOKEN -v "$(pwd -W):/d" -w /d lycheeverse/lychee --no-progress --max-retries 3 --include-fragments anchor-only README.md
```

(`GITHUB_TOKEN` must already be exported in the host shell so Docker receives it; without it, GitHub rate limits can false-fail seed URLs.)

On failures: retry once (transient 429/timeouts are expected on third-party sites). A persistent failure means the entry drops or gets corrected; apply the fix, update CHANGELOG entry count if it changed, remove any section that became empty (heading + ToC bullet), rerun the lint gates from Task 4 Step 5, amend the README commit or add a fix commit, and rerun the gate until exit 0. If the User Community page is the failure, delete that entry and its fix-up per Task 4 Step 3. If drops would leave fewer than 15 live entries, stop and report; do not invent replacement seeds in this effort.

- [ ] **Step 2: Push**

```bash
cd "/c/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
git push -u origin main
```

- [ ] **Step 3: Verify default branch and lint CI**

```bash
gh repo view jgsystemsconsulting/awesome-archimate --json defaultBranchRef --jq .defaultBranchRef.name
gh run list --repo jgsystemsconsulting/awesome-archimate --workflow=lint.yml --limit 1
```

Expected: `main`; the push-triggered Lint run exists. Watch it to completion:

```bash
gh run watch --repo jgsystemsconsulting/awesome-archimate $(gh run list --repo jgsystemsconsulting/awesome-archimate --workflow=lint.yml --limit 1 --json databaseId --jq '.[0].databaseId') --exit-status
```

Expected: conclusion `success` (awesome-lint and markdownlint both pass in CI).

- [ ] **Step 4: Exercise the links workflow by manual dispatch**

```bash
gh workflow run links.yml --repo jgsystemsconsulting/awesome-archimate
sleep 15
gh run watch --repo jgsystemsconsulting/awesome-archimate $(gh run list --repo jgsystemsconsulting/awesome-archimate --workflow=links.yml --limit 1 --json databaseId --jq '.[0].databaseId') --exit-status
```

Expected: conclusion `success`; no "Link Checker Report" issue was created (issue creation only fires on nonzero exit). This also validates the `--include-fragments anchor-only` flag inside CI.

No commit in this task.

---

### Task 7: Hub updates in awesome-mbse

**Files:**

- Modify: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-mbse\FAMILY.md`
- Modify: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-mbse\README.md`
- Modify: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-mbse\CHANGELOG.md`

**Interfaces:**

- Consumes: the live repo from Task 6.
- Produces: registry row `Live` with the scope text the acceptance check greps for.

**Model:** flash

- [ ] **Step 1: Flip the FAMILY.md registry row**

In `FAMILY.md`, the registry row:

From:

```markdown
| awesome-archimate | ArchiMate 3.x, the Archi tool, EA modeling practice | Planned | none yet |
```

To:

```markdown
| [awesome-archimate](https://github.com/jgsystemsconsulting/awesome-archimate) | ArchiMate 3.x and 4, the Archi tool, EA modeling practice | Live | public |
```

- [ ] **Step 2: Update the FAMILY.md namespace table row**

From:

```markdown
| awesome-archimate | 2026-09-17 | empty | Re-check on create day |
```

To (insert the actual creation-day date in `Checked`, which is the same day Task 1 ran):

```markdown
| awesome-archimate | 2026-09-17 (create-day re-check: empty) | empty | None; repo created |
```

- [ ] **Step 3: Tick the FAMILY.md per-spoke checklist**

The `### awesome-archimate` checklist block:

From:

```markdown
### awesome-archimate

Planned. Hub GAP: no dedicated ArchiMate section. Namespace empty on 2026-09-17.

- [ ] Namespace re-checked on YYYY-MM-DD (result: empty / incumbent found)
- [ ] Roughly 40 candidate entries gathered, all passing the inclusion bar
- [ ] Repo created (private) from the README skeleton
- [ ] Hub README family table row updated with the URL
- [ ] Registry status flipped to Live
```

To (fill the date from Task 1):

```markdown
### awesome-archimate

Live. Hub GAP: no dedicated ArchiMate section. Namespace empty on 2026-09-17 and on
the create-day re-check. Launched with 18 verified seeds under the depth waiver
(2026-09-17, owner: spoke maintainer); the ~40-entry bar is the target for the first
full sweep, logged in the spoke CHANGELOG.

- [x] Namespace re-checked on <CREATE-DATE> (result: empty)
- [x] Depth waiver applied: opened with 18 verified seeds (minimum 15 live) per the 2026-09-17 waiver
- [x] Repo created (public, matching awesome-sysml-v2) from the README skeleton
- [x] Hub README family table row updated with the URL
- [x] Registry status flipped to Live
```

- [ ] **Step 4: Add the live-spoke sentence to the hub README**

In `README.md`, the List family paragraph:

From:

```markdown
This repo is the hub of a family of lists; the registry and family rules live in
[FAMILY.md](FAMILY.md).
```

To:

```markdown
This repo is the hub of a family of lists; the registry and family rules live in
[FAMILY.md](FAMILY.md). The live spokes are
[awesome-sysml-v2](https://github.com/jgsystemsconsulting/awesome-sysml-v2),
[awesome-digital-engineering](https://github.com/jgsystemsconsulting/awesome-digital-engineering),
and [awesome-archimate](https://github.com/jgsystemsconsulting/awesome-archimate).
```

- [ ] **Step 5: Update the two mirror-table rows in the hub README**

The awesome-sysml-v2 row (only if it still carries the stale "only existing live spoke" note; current hub may already say `Linked public spoke` only, in which case skip this From/To):

From (stale variant, if present):

```markdown
| [awesome-sysml-v2](https://github.com/jgsystemsconsulting/awesome-sysml-v2) | SysML v2 the language: spec, parsers, editors, API clients, example models | Live | Linked public spoke; the only existing live spoke |
```

To:

```markdown
| [awesome-sysml-v2](https://github.com/jgsystemsconsulting/awesome-sysml-v2) | SysML v2 the language: spec, parsers, editors, API clients, example models | Live | Linked public spoke |
```

The awesome-archimate row:

From:

```markdown
| awesome-archimate | ArchiMate 3.x, the Archi tool, EA modeling practice | Planned | GAP (no dedicated hub section) |
```

To:

```markdown
| [awesome-archimate](https://github.com/jgsystemsconsulting/awesome-archimate) | ArchiMate 3.x and 4, the Archi tool, EA modeling practice | Live | Linked public spoke |
```

- [ ] **Step 6: Add the hub CHANGELOG entry**

In `CHANGELOG.md`, insert directly after the line `tracks the most recent dated entry here.` and its blank line, so the new section is the first dated entry:

```markdown
## 2026-09 - Spoke launch: awesome-archimate

- **Launched [awesome-archimate](https://github.com/jgsystemsconsulting/awesome-archimate)**
  (public) as an additional live spoke (third Live spoke after awesome-sysml-v2 and
  awesome-digital-engineering): ArchiMate 3.x and 4, the Archi tool, EA modeling
  practice. Opened with 18 verified seed entries under the depth waiver.
- **FAMILY.md registry**: awesome-archimate flipped Planned -> Live, repo link added,
  scope text updated to "ArchiMate 3.x and 4, the Archi tool, EA modeling practice".
- **Hub README**: the List family paragraph now names the live spokes (sysml-v2, digital-engineering, archimate); the
  registry-mirror table rows for awesome-sysml-v2 and awesome-archimate updated.
```

- [ ] **Step 7: Verify and push the hub**

```bash
cd "/c/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
grep -n "awesome-archimate" FAMILY.md | head -5
grep -n "awesome-archimate" README.md | head -5
git diff --stat
git add FAMILY.md README.md CHANGELOG.md
git commit -m "docs: flip awesome-archimate spoke to Live and link it from the hub"
git push
```

Expected: the grep hits show the Live registry row, the namespace row, the checklist block, the README sentence, and the mirror row. No content was removed from the hub (no shrink needed; the hub carries no ArchiMate section).

---

### Task 8: Acceptance sweep

**Files:**

- No file changes unless a check fails and forces a fix.

**Model:** standard

Run every check; fix and re-run on failure. Work from `C:\Users\gower\OneDrive\Documents\GitHub\awesome-archimate` unless the command says otherwise.

- [ ] **Check 1: Repo state**

```bash
gh repo view jgsystemsconsulting/awesome-archimate --json visibility,defaultBranchRef --jq '.visibility + " " + .defaultBranchRef.name'
```

Expected: `PUBLIC main`.

- [ ] **Check 2: Shared-standard file set**

```bash
cd "/c/Users/gower/OneDrive/Documents/GitHub/awesome-archimate" && ls -A
```

Expected: `README.md`, `CONTRIBUTING.md`, `LICENSE`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `CHANGELOG.md`, `.markdownlint-cli2.jsonc`, `.github/workflows/links.yml`, `.github/workflows/lint.yml`, `.github/workflows/stale.yml`.

- [ ] **Check 3: Branding**

```bash
grep -ri "OMG ArchiMate" README.md CONTRIBUTING.md SECURITY.md CHANGELOG.md CODE_OF_CONDUCT.md
```

Expected: no matches (exit 1). Both specifications present:

```bash
grep -c "publications.opengroup.org/c226" README.md
grep -c "publications.opengroup.org/c260" README.md
```

Expected: `1` and `1`.

- [ ] **Check 4: Entries and format**

Re-run the Task 4 Step 4 python check (http(s) entries only; ignores ToC). Expected exit 0 and printed count >= 15.

Do not use bare `grep -c "^- \["` as the entry count; that includes ToC lines.

- [ ] **Check 5: CONTRIBUTING content**

```bash
grep -l "foundational" CONTRIBUTING.md
grep -c "canonicalize both URLs" CONTRIBUTING.md
grep -c "most recent author-published version" CONTRIBUTING.md
grep -c "required unless \`spec\` or \`standard\` is present" CONTRIBUTING.md
grep -c "\`docs\`" CONTRIBUTING.md
```

Expected: file found; the year rule and dedupe rule verbatim lines present (1 each); the type-optional-when-spec rule and the `docs` type present.

- [ ] **Check 6: Workflows**

```bash
grep -cE "uses: .*@[0-9a-f]{40}" .github/workflows/*.yml
grep -n "include-fragments anchor-only" .github/workflows/links.yml
grep -n "fail: false" .github/workflows/links.yml
grep -n "awesome-lint@2.3.0" .github/workflows/lint.yml
grep -n "Inclusion bar" .github/workflows/stale.yml
```

Expected: SHA pins 2/3/1; the anchor-only flag and advisory `fail: false` in links.yml; the lint pin in lint.yml; the inclusion-bar citation in stale.yml.

- [ ] **Check 7: Local lint gates still pass**

```bash
cd "/c/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
npx awesome-lint@2.3.0 README.md
npx markdownlint-cli2 "README.md" "CONTRIBUTING.md"
```

Expected: both exit 0.

- [ ] **Check 8: CI green on GitHub**

```bash
gh run list --repo jgsystemsconsulting/awesome-archimate --limit 5
```

Expected: the latest Lint run and the dispatched Links run both show `success` (or a later run triggered by a sweep fix does).

- [ ] **Check 9: Hub state**

```bash
cd "/c/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
grep -n "ArchiMate 3.x and 4" FAMILY.md
grep -n "awesome-archimate" README.md | head -3
grep -n "2026-09" CHANGELOG.md | head -2
```

Expected: the FAMILY registry row reads Live with the repo link and the scope text "ArchiMate 3.x and 4, the Archi tool, EA modeling practice"; the hub README links the spoke near the family paragraph; the CHANGELOG carries the 2026-09 launch entry. The spoke CHANGELOG launch entry was verified in Check 2's tree plus:

```bash
grep -n "Initial launch" "/c/Users/gower/OneDrive/Documents/GitHub/awesome-archimate/CHANGELOG.md"
```

- [ ] **Check 10: No leftover conditionals**

Confirm the Hosgen decision was applied (entry present only if a URL verified in Task 4 Step 3; otherwise absent and no empty Tutorials section exists) and the User Community entry is either present and browsable or removed with no empty Communities section:

```bash
grep -c "^## " README.md
```

Expected: **10** headings when the default eight content sections ship (Contents + 8 content sections + Contributing). If Books was removed after a book drop, expect **9**. If Tutorials and courses was added for Hosgen, expect **11**. Every content section heading that remains must have at least one entry beneath it (Contents and Contributing are exempt).

If any fix changes tracked files anywhere, commit and push, then re-run the affected checks and watch CI again.

---

## Self-review record

Spec coverage: namespace recheck (Task 1), public repo and sibling clone (Task 1), ported files with hub-style SECURITY and sibling CoD (Task 2), CONTRIBUTING with inclusion bar, foundational-value exception, hub year and dedupe rules verbatim plus spoke undated-page addendum, adapted neutrality, tag table with type-optional-when-spec and docs (Task 3), README with badges, family pointer, flat ToC, 18 seeded entries with full tags and years, Open Group branding, both specs (Task 4), patched workflows with SHA pins, fragment checking, advisory PR gate, awesome-lint pin, inclusion-bar citation (Task 5), launch lychee exit 0, push, CI green (Task 6), hub registry flip with scope text, README spoke links, both CHANGELOGs (Task 7), acceptance mapping (Task 8). Non-goals respected: no sindresorhus submission, no hub shrink, no commercial tools, no re-hosting, Hosgen conditional.

Placeholder scan: no TBD or TODO tokens. Execute-determined values all carry their derivation: years come from the evidence table plus a re-verification step, the create-day date is Task 1's date, the entry count in the spoke CHANGELOG is the shipped count, and the hub-privacy branch on the family pointer is resolved by an exact command with both variants provided.

Consistency: `CONTRIBUTING.md#editorial-neutrality` (README link) matches the `## Editorial neutrality` heading; `criterion 4 of the Inclusion bar` (stale.yml, CONTRIBUTING) matches `## Inclusion bar` with foundational value at item 4; ToC anchors match the GitHub slugs of the default ten H2s (Contents + 8 content + Contributing); tag axis order in the README matches the CONTRIBUTING table; the 140-character measurement text matches hub section 3 wording; entry-format check counts http(s) entries only; book drop removes empty Books section.
