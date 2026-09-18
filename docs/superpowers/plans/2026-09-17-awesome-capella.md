# awesome-capella spoke Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create the `jgsystemsconsulting/awesome-capella` spoke repo to the awesome-mbse family standard, seed it with verified Capella/Arcadia entries toward the 40-entry depth bar, wire the full CI triad, and flip hub records only when the bar is met.

**Architecture:** One new public repo cloned as a sibling of the hub at `C:\Users\gower\OneDrive\Documents\GitHub\awesome-capella`. Editorial rules port from hub CONTRIBUTING.md (tagged entries with year); CI assembles the FAMILY triad (hub strict lychee + awesome-lint, sysml-v2-style markdownlint). A namespace recheck gates repo creation; a seed-pass count gates hub edits. Everything else in the hub stays untouched.

**Tech Stack:** Markdown, GitHub Actions (lycheeverse/lychee-action with lychee v0.24.2, awesome-lint@2.3.0, markdownlint-cli2), `gh` CLI, dockerized lychee for local checks, Python 3 for the entry-format checker.

**Spec:** `docs/superpowers/specs/2026-09-17-awesome-capella.md` (normative). Research: `docs/superpowers/research/2026-09-17-awesome-capella-sources-research.md`. Context: `docs/superpowers/context/2026-09-17-awesome-capella-pattern-context.md`.

## Global Constraints

Every task implicitly includes these, copied from the spec:

- Repo: `jgsystemsconsulting/awesome-capella`, public (M1), local clone as hub sibling at `C:\Users\gower\OneDrive\Documents\GitHub\awesome-capella`.
- Depth bar: 40 or more verified entries flips the hub; under 40, the spoke ships alone, FAMILY status stays Planned, hub untouched, count documented (M8, decision 4). Never pad.
- Entry format (M4): `- [Name](url) - Description `tag` `tag` (YYYY).` Hyphen separator, never en/em dash. Tags as inline code spans before the terminal period, axis order `language → method → tool → has-model → type → spec/standard → paid → year`. Exactly one language, exactly one type, exactly one `(YYYY)` last token. Description at most 140 characters, measured after ` - ` to before the first tag.
- Language tag values: `Capella`, `UAF` (UAF/UPDM through a Capella addon), `SysML-general` (Capella/Arcadia positioned against SysML). Method: `Arcadia` (0 or 1). Tool: `python4capella`, `py-capellambse`, `Capella-Studio`, `other-tool` (graduates at 3+ shared entries, CONTRIBUTING updated in same change). Type: `tutorial`, `course`, `book`, `paper`, `blog`, `video`, `tool`, `plugin`, `docs`, `case-study` (exactly 1). `standard` only after seed verifies the Arcadia standard id (AFNOR Z67-140). `paid` for Elsevier books and commercial training.
- Year rule (hub §5, frozen): paper → publication year; repo → latest tagged release, else latest default-branch commit; course → current cohort year. Trivial edits do not count. Capella release `v7.1.0 (03 Aug 2026)` is provisional; verify the tag before stamping any year derived from it.
- Canonical URLs (decision 7): `mbse-capella.org` wins over eclipse.org redirects. Banned href patterns: `arcadia-method.com`, `capella.polarsys.org` (grep token `polarsys`), `projects.eclipse.org/projects/modeling.capella`, `eclipse.org/capella`, `eclipse.dev/capella`, and any host that only 302s to mbse-capella.org for the same Capella page. AC4 grep for `eclipse.org/capella` does **not** match `download.eclipse.org/capella/...` (different host). Prefer mbse-capella.org when a resource also lives there; `download.eclipse.org` PDFs remain listable if they pass the inclusion bar.
- Five-point inclusion bar (M6): on-topic (Capella or Arcadia, not general MBSE), substantive, live, not duplicative (canonical-URL rule), legally linkable. We link, we never re-host (M10).
- CI triad (M5): strict lychee `--include-fragments=anchor-only --max-concurrency 4 --accept 200..=299,429 --no-progress README.md`, lychee v0.24.2, `fail: true` on the PR workflow, GITHUB_TOKEN passed; awesome-lint pinned `2.3.0` (sysml-v2 pin; hub currently runs unpinned `npx -y awesome-lint`); markdownlint-cli2 on `README.md` and `CONTRIBUTING.md`. Schedule workflow is report-only (`fail: false` plus link-rot issue). Schedule-only green does not satisfy M5.
- Files: `LICENSE` CC0-1.0, `CONTRIBUTING.md` uppercase filename with year rule, canonical-URL rule, neutrality section (M9). `.lycheeignore` starts empty; never add a banned host to hide failures (S3).
- Collab product (decision 5): resolve the Team for Capella durable URL during seed; no durable page means omit that product entry only; the Collaboration section may ship thin (for example `labs4capella/mms-capella`).
- Namespace (decision 8): recheck GitHub for `awesome-capella` and `awesome-arcadia` incumbents on create day before `gh repo create`. A live incumbent (roughly 100+ stars or updated within the last year) aborts creation per FAMILY step 1.
- Hub touch list when bar met (decision 6): FAMILY.md registry status Planned to Live, hub README spoke link plus Capella/Arcadia shrink. Nothing else. No sindresorhus/awesome submission, no Model Gallery, no sibling spokes, no content re-hosting.

## Codebase context

From `docs/superpowers/context/2026-09-17-awesome-capella-pattern-context.md`:

- Shared standard (S1): README with Awesome badge, one-line scope, Last full sweep badge, family pointer, flat hand-maintained ToC; LICENSE CC0-1.0; CONTRIBUTING.md; CODE_OF_CONDUCT.md; SECURITY.md; CHANGELOG.md.
- Entry format (S2): hub/FAMILY tagged form, not the sysml-v2 untagged form. Copy hub CONTRIBUTING §5 (year), §6 (dedupe), §7 (neutrality). awesome-sysml-v2 is the workflow existence proof and markdownlint reference only.
- CI (S3): full FAMILY triad, assembled: hub lychee flags + hub awesome-lint + sysml-v2-style markdownlint. Not a pure clone of either repo.
- Registry row and scope text already exist in FAMILY.md and hub README (S4); no scope invention needed.
- Hub go-live work (S5): status flip, spoke link near top, shrink hub Capella/Arcadia to pointer plus cross-cutting.
- Location (S6): sibling of the hub at `../awesome-capella`. Uppercase `CONTRIBUTING.md`; CI globs pin the exact filename.

## Research

Seed pillars and canonical sources (full table in the research file):

- https://mbse-capella.org/ (product home, canonical)
- https://mbse-capella.org/arcadia.html (Arcadia method page)
- https://mbse-capella.org/addons.html (official addons catalog)
- https://mbse-capella.org/resources.html (resources and case studies)
- https://mbse-capella.org/capella_days_2026.html (Capella Days hub)
- https://github.com/eclipse-capella/capella (core repo)
- https://github.com/eclipse-capella (org: addon repos)
- https://github.com/labs4capella/python4capella (scripting)
- https://github.com/dbinfrago/py-capellambse (headless Python)
- https://shop.elsevier.com/books/model-based-system-and-architecture-engineering-with-the-arcadia-method/voirin/978-1-78548-169-7 (Voirin, 2017)
- https://shop.elsevier.com/books/systems-architecture-modeling-with-the-arcadia-method/roques/978-1-78548-168-0 (Roques, 2017)
- https://www.obeosoft.com/en/capella-professional-offer#coaching (training pointer, confirm on seed, strip fragment per canonical rule)

Open items carried into seed: R4 (Team for Capella URL) and R8 (depth count). Dead hosts never listed: arcadia-method.com, capella.polarsys.org, projects.eclipse.org/projects/modeling.capella, legacy eclipse.org/capella and eclipse.dev/capella redirect paths.

## File map

Also: `scripts/check_entries.py` (Task 7, committed; AC5).


New repo (`C:\Users\gower\OneDrive\Documents\GitHub\awesome-capella`):

| File | Source | Task |
|------|--------|------|
| `README.md` | new, spec skeleton + seeded entries | 3, 6 |
| `LICENSE` | hub copy (CC0-1.0) | 3 |
| `CODE_OF_CONDUCT.md` | hub copy | 3 |
| `SECURITY.md` | hub copy | 3 |
| `CHANGELOG.md` | new | 3, 6 |
| `CONTRIBUTING.md` | new, ported from hub | 4 |
| `.github/workflows/link-check-pr.yml` | hub port + markdownlint job | 5 |
| `.github/workflows/link-check-schedule.yml` | hub verbatim copy | 5 |
| `.markdownlint-cli2.jsonc` | sysml-v2 copy | 5 |
| `.lycheeignore` | new, empty | 3 |
| `.github/ISSUE_TEMPLATE/suggest-resource.yml` (S1) | hub, adapted | 5 (optional) |
| `.github/PULL_REQUEST_TEMPLATE.md` (S2) | hub, adapted | 5 (optional) |

Hub edits (conditional, Task 9): `FAMILY.md` registry row, `README.md` list-family row, gaps sentence, Broader Context Capella entries.

---

### Task 1: Namespace recheck on create day (hard gate)

**Files:** none created. Output feeds Task 2 (abort/proceed) and Task 3 (CHANGELOG first entry).

**Interfaces:**
- Produces: a recheck verdict string, either `empty` (proceed) or `incumbent found: <repo, stars, last push>` (abort).

**Model:** flash

- [ ] **Step 1: Search GitHub for incumbents**

Run:

```bash
gh search repos "awesome-capella" --limit 20 --json fullName,stargazersCount,pushedAt,description
gh search repos "awesome-arcadia" --limit 20 --json fullName,stargazersCount,pushedAt,description
gh api repos/awesome-capella/awesome-capella 2>&1 | head -1
```

Expected baseline: the 2026-09-17 research probe found the namespace empty but rate-limited mid-search, so this recheck is the authoritative one.

- [ ] **Step 2: Apply the FAMILY step-1 rule**

A live incumbent of substance aborts creation (FAMILY step 1 working test across the family: roughly 100+ stars or updated in the last year; same maintainer judgment as the hub). If aborted: stop the whole plan, report the incumbent, and fall back to growing the hub Capella/Arcadia section (spec decision 8). No repo, no hub flips.

- [ ] **Step 3: Keep the verdict for the CHANGELOG**

Hold the raw search output and the verdict. Task 3 writes it into the spoke CHANGELOG as the first entry (M7).

**Done when:** search output captured, verdict decided (`empty` proceeds; an incumbent stops everything).

### Task 2: Create the repo and sibling clone

**Files:** none in the hub. Creates the GitHub repo and the local clone at `C:\Users\gower\OneDrive\Documents\GitHub\awesome-capella`.

**Interfaces:**
- Consumes: Task 1 verdict `empty`.
- Produces: empty public repo on `main`, local sibling clone with origin set.

**Model:** flash

- [ ] **Step 1: Create the repo**

```bash
gh repo create jgsystemsconsulting/awesome-capella --public --description "Curated Capella tool and Arcadia method resources for MBSE practitioners"
```

Note: the spec (M1, reviewed) says public. FAMILY's private-by-default rule is overridden by the spec here; the public spoke then follows the FAMILY private-mode text rules via the family pointer line already in the skeleton.

- [ ] **Step 2: Clone as hub sibling**

```bash
git clone https://github.com/jgsystemsconsulting/awesome-capella.git "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
```

- [ ] **Step 3: Verify (AC1 shape)**

```bash
gh repo view jgsystemsconsulting/awesome-capella --json visibility,defaultBranchRef --jq '.visibility + " " + .defaultBranchRef.name'
git -C "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella" remote -v
git -C "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella" status
```

Expected: `PUBLIC main`, origin points at the repo, working tree clean. An empty repo has no commits yet; `git status` may report "No commits yet", which is fine.

**Done when:** `gh repo view` succeeds, visibility PUBLIC, default branch main, sibling clone exists next to `awesome-mbse`.

### Task 3: Must-inventory scaffold, README skeleton, CHANGELOG first entry

**Files (all inside the spoke clone):**
- Create: `README.md`
- Create: `.lycheeignore` (empty)
- Create: `CHANGELOG.md`
- Copy: `LICENSE`, `CODE_OF_CONDUCT.md`, `SECURITY.md` from the hub

**Interfaces:**
- Consumes: Task 1 verdict (goes into CHANGELOG).
- Produces: README skeleton with the nine fixed section titles that Task 6 fills; `.lycheeignore` placeholder for Task 5's lychee runs; CHANGELOG with the M7 recheck record.

**Model:** flash

- [ ] **Step 1: Copy the three family files, create the empty ignore file**

```bash
HUB="C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
SPOKE="C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
cp "$HUB/LICENSE" "$SPOKE/LICENSE"
cp "$HUB/CODE_OF_CONDUCT.md" "$SPOKE/CODE_OF_CONDUCT.md"
cp "$HUB/SECURITY.md" "$SPOKE/SECURITY.md"
touch "$SPOKE/.lycheeignore"
```

Read the three copies. Fix any hub-specific references (repo names, file links that only exist in the hub) so they make sense in the spoke. Leave the CC0 text untouched.

- [ ] **Step 2: Write the README skeleton (spec decision 3, literal)**

Write `README.md` exactly:

````markdown
# Awesome Capella [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Curated Capella tool and Arcadia method resources for MBSE practitioners.

![Last full sweep: 2026-09](https://img.shields.io/badge/last%20full%20sweep-2026--09-brightgreen)

Part of the awesome-mbse list family (hub: jgsystemsconsulting/awesome-mbse).
Text-only family pointer while the hub is private (FAMILY Private mode: no
FAMILY.md hyperlinks from public spokes).

Maintained by [JG Systems Consulting Ltd.](https://github.com/jgsystemsconsulting).
See [Editorial neutrality](CONTRIBUTING.md#editorial-neutrality).

## Contents

- [Arcadia method](#arcadia-method)
- [Capella core](#capella-core)
- [Addons and extensions](#addons-and-extensions)
- [Scripting and automation](#scripting-and-automation)
- [Collaboration and model management](#collaboration-and-model-management)
- [Books, courses, and training](#books-courses-and-training)
- [Community and events](#community-and-events)
- [Example models and case studies](#example-models-and-case-studies)
- [Commercial offers](#commercial-offers)

## Arcadia method

## Capella core

## Addons and extensions

## Scripting and automation

## Collaboration and model management

## Books, courses, and training

## Community and events

## Example models and case studies

## Commercial offers
````

Deviations from the spec skeleton, deliberate: (1) family pointer is text-only
while the hub is private (FAMILY Private mode), not a FAMILY.md blob URL;
(2) neutrality anchor is CONTRIBUTING.md#editorial-neutrality matching the
spec skeleton. Task 4 uses heading `## Editorial neutrality` so the GitHub slug matches.

- [ ] **Step 3: Write CHANGELOG.md with the recheck record (M7)**

Write `CHANGELOG.md`, substituting the Task 1 verdict:

```markdown
# Changelog

## 2026-09-17

- Created `jgsystemsconsulting/awesome-capella` (public) as the Capella and Arcadia
  spoke of the awesome-mbse list family.
- Namespace recheck on create day (2026-09-17): <Task 1 verdict, for example
  "empty; no live awesome-capella or awesome-arcadia incumbent at 2026-09-17">.
  Supersedes the rate-limited 2026-09-17 research probe (R7).
- Verified seed count: finalized during the seed pass below (depth bar 40).
```

- [ ] **Step 4: Commit and push**

```bash
git -C "$SPOKE" add -A
git -C "$SPOKE" commit -m "chore: scaffold family must-inventory and README skeleton"
git -C "$SPOKE" push origin main
```

**Done when:** all six Must-inventory files created so far exist on origin `main`, README matches the block above, `.lycheeignore` is empty, CHANGELOG carries the recheck verdict.

### Task 4: CONTRIBUTING.md port with frozen rules

**Files:**
- Create: `CONTRIBUTING.md` (uppercase filename, M9)

**Interfaces:**
- Produces: the tag vocabulary Task 6 applies, the neutrality section the README links, the heading `## Editorial neutrality` (slug `#editorial-neutrality`) that the README anchor targets.

**Model:** flash

- [ ] **Step 1: Write CONTRIBUTING.md**

Port of hub CONTRIBUTING.md with the spec's frozen deltas: on-topic reworded to Capella/Arcadia, Capella tag table, Model Gallery section omitted, numbering shifted (hub §9 becomes §8, hub §10 becomes §9). Write the file exactly:

````markdown
# Contributing

Thanks for helping keep this the best-curated Capella / Arcadia index anywhere. Read
this before opening a PR: the CI gates enforce most of it.

The fastest path: open an issue using the "Suggest a resource" form, or open a pull
request that edits `README.md` directly.

## 1. How to suggest a resource

- **Issue:** use the *Suggest a resource* form. Good for "I found this, you decide."
- **PR:** edit `README.md`, follow the entry format below, tick the PR checklist. CI
  link-checks your entry and lints the list.

## 2. Inclusion bar

An entry is accepted only if **all** hold:

1. **On-topic**: genuinely about Capella or the Arcadia method (not general MBSE only).
2. **Substantive**: it teaches, demonstrates, specifies, or provides something usable.
   Not a stub. Not pure vendor marketing.
3. **Live**: the link resolves right now.
4. **Not duplicative**: not already listed (see the canonical-URL rule, §6).
5. **Legally linkable**: publicly accessible. We **link**, we never re-host model files,
   PDFs, or proprietary content.

Tie-breakers (nice-to-have, not gates): has a real openable model (`has-model`),
recently updated, from a recognized source (Eclipse, Thales/Obeo, DLR, a university, an
established practitioner).

## 3. Entry format

One line per entry, **hyphen separator** (` - `, never an en/em dash: awesome-lint
rejects those), tags as **inline code spans inside the sentence before the terminal
period**, year parenthesized as the last token:

```
- [Resource Name](https://example.com) - One-line factual description `Capella` `Arcadia` `tool` (2026).
```

- **Description:** factual, one line, **≤ 140 characters** (measured from the first
  character after ` - ` to the last character before the first tag, excluding the link
  markup and tags). No hype.
- **`has-model`** means: a **directly downloadable, non-paywalled** Capella model (an
  Eclipse model project with `.aird`) that opens in Capella. Screenshots, papers
  *describing* a model, and access-gated / request-only files **do not** qualify.

## 4. Tag vocabulary, cardinality & order

Tags appear in this fixed order, drawn **only** from this vocabulary:

`language → method → tool → has-model → type → spec/standard → paid → year`

| Axis | Cardinality | Values |
|------|-------------|--------|
| language | exactly 1 | `Capella` (native Capella viewpoints/metamodel, and Arcadia-method-only resources whose home is Capella) · `UAF` (UAF/UPDM through a Capella addon) · `SysML-general` (resources that primarily position Capella or Arcadia against SysML) |
| method | 0 or 1 | `Arcadia` |
| tool | 0 or more | `python4capella` · `py-capellambse` · `Capella-Studio` · `other-tool` |
| has-model | 0 or 1 | `has-model` |
| type | exactly 1 (dominant form) | `tutorial` · `course` · `book` · `paper` · `blog` · `video` · `tool` · `plugin` · `docs` · `case-study` |
| spec/standard | 0 or 1 | `standard` (use only after seed verifies the Arcadia standard id, e.g. AFNOR Z67-140, on the method page) |
| paid | 0 or 1 | `paid` |
| year | exactly 1 | `(YYYY)` (see §5) |

- `other-tool` graduates to its own tag only once ≥ 3 entries share it; update this
  table in the same change.
- For a normative standard document use `standard` and omit `paper`.

## 5. The year rule (`YYYY`)

`(YYYY)` = the year of the resource's **most recent author-published version**:

- a paper → its publication year;
- a repo → its latest tagged release, or the latest default-branch commit if untagged;
- a course → its current cohort year.

**Trivial edits (typo fixes) don't count.** Examples:

- A 2019 paper with a 2024 typo-fix commit → `(2019)`.
- A repo whose latest release tag is `v2.1` from 2023 → `(2023)`.

## 6. Canonical-URL rule (dedupe)

Before deciding "is this a duplicate", canonicalize both URLs: force `https`, lowercase
the host, strip a trailing slash, drop the query string and fragment unless they're
semantically required. If the canonical forms match, it's a duplicate.

Canonical hosts for official Capella material: `mbse-capella.org` (product home, Arcadia
method page, addons catalog, resources, Capella Days) and the `eclipse-capella` and
`labs4capella` GitHub orgs. Never list `arcadia-method.com` (DNS dead),
`capella.polarsys.org`, `projects.eclipse.org/projects/modeling.capella`, or the legacy
`eclipse.org/capella` / `eclipse.dev/capella` redirect paths.

## Editorial neutrality

This list is maintained by JG Systems Consulting Ltd., which sells commercial MBSE
consulting services, including Capella and Arcadia engagements. To keep it trustworthy:

- JGS-adjacent entries are listed by the **same inclusion bar** as everything else.
- Every JGS-adjacent entry sits next to **≥ 1 genuine competing/alternative entry**.
- **A superior competing resource is listed above a JGS-adjacent one.** Neutrality is
  enforced by this rule, not by tone.

> **Table of Contents:** the `## Contents` ToC is hand-maintained and lists only the
> top-level sections (a flat ToC keeps awesome-lint happy). If you add or rename a
> **top-level** section, update the ToC by hand; sub-sections are not listed. CI
> validates every ToC anchor resolves (lychee `--include-fragments anchor-only`).

## 8. Local link-check

No install needed. Check your changed links with Docker:

```sh
docker run --rm -v "$PWD:/d" -w /d lycheeverse/lychee --include-fragments anchor-only README.md
```

Or open a **draft PR** and let CI check it for you.

## 9. Maintenance cadence

The maintainers run a **quarterly sweep** (add new resources, prune rot), logged in
`CHANGELOG.md` with the date, and update the *Last full sweep* badge at the top of the
README each time. If it's been **> 6 months** since the last sweep, the badge flips to
"maintenance lapsed"; call it out in an issue.
````

- [ ] **Step 2: Verify the frozen content landed**

```bash
SPOKE="C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
grep -c "## 5. The year rule" "$SPOKE/CONTRIBUTING.md"          # expect 1
grep -c "## 6. Canonical-URL rule" "$SPOKE/CONTRIBUTING.md"     # expect 1
grep -c "## Editorial neutrality" "$SPOKE/CONTRIBUTING.md"   # expect 1
grep -c "has-model" "$SPOKE/CONTRIBUTING.md"                    # >= 3
test "$(basename "$SPOKE"/CONTRIBUTING.md)" = "CONTRIBUTING.md" && echo uppercase-ok
```

- [ ] **Step 3: Commit and push**

```bash
git -C "$SPOKE" add CONTRIBUTING.md
git -C "$SPOKE" commit -m "docs: port hub contributing rules with Capella tag vocabulary"
git -C "$SPOKE" push origin main
```

**Done when:** uppercase `CONTRIBUTING.md` on origin `main` with the year rule, canonical-URL rule, and neutrality section (AC6 shape); grep checks above pass.

### Task 5: CI triad workflows, markdownlint config, contributor templates

**Files:**
- Create: `.github/workflows/link-check-pr.yml`
- Create: `.github/workflows/link-check-schedule.yml`
- Create: `.markdownlint-cli2.jsonc`
- Create (S1, optional): `.github/ISSUE_TEMPLATE/suggest-resource.yml`
- Create (S2, optional): `.github/PULL_REQUEST_TEMPLATE.md`

**Interfaces:**
- Produces: the workflow names `link-check (PR)` and `link-check (weekly)` that Task 8 dispatches and Task 10 reads.

**Model:** flash

- [ ] **Step 1: Copy the schedule workflow and markdownlint config verbatim**

```bash
HUB="C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
SPOKE="C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
mkdir -p "$SPOKE/.github/workflows"
cp "$HUB/.github/workflows/link-check-schedule.yml" "$SPOKE/.github/workflows/link-check-schedule.yml"
cp "C:/Users/gower/OneDrive/Documents/GitHub/awesome-sysml-v2/.markdownlint-cli2.jsonc" "$SPOKE/.markdownlint-cli2.jsonc"
cat "$SPOKE/.markdownlint-cli2.jsonc"
```

Expected config content: `{ "config": { "MD013": false } }`. That is the minimal allowlist that accepts hub-style tagged list lines (long lines, inline code spans). The schedule copy already has the right lychee args, `fail: false`, and the link-rot issue flow.

- [ ] **Step 2: Write the PR workflow (hub port + markdownlint job)**

Write `.github/workflows/link-check-pr.yml` exactly:

```yaml
name: link-check (PR)

# Gate on contributions: a dead new link fails the PR, and the README must stay
# awesome-lint and markdownlint conformant (FAMILY CI triad: hub lychee + awesome-lint,
# sysml-v2-style markdownlint). workflow_dispatch lets the maintainer produce a green
# triad run on main after a direct push (AC2).

on:
  pull_request:
    paths:
      - "README.md"
      - "CONTRIBUTING.md"
      - "scripts/**"
      - ".lycheeignore"
      - ".github/workflows/link-check-pr.yml"
  workflow_dispatch: {}

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
          # --include-fragments=anchor-only validates the hand-maintained flat
          # Contents ToC. GITHUB_TOKEN makes the many github.com links check
          # authenticated, avoiding the 60 req/hr anonymous rate limit that
          # reports live links as dead.
          lycheeVersion: v0.24.2
          args: >-
            --include-fragments=anchor-only
            --max-concurrency 4
            --accept 200..=299,429
            --no-progress
            README.md
          fail: true
          token: ${{ secrets.GITHUB_TOKEN }}

  awesome-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: "20"
      - name: Awesome-list manifest conformance
        run: npx -y awesome-lint@2.3.0 README.md

  markdownlint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: "20"
      - name: Markdown lint
        run: npx -y markdownlint-cli2 "README.md" "CONTRIBUTING.md"
```

Two documented deltas from the hub file, both required by the spec: `workflow_dispatch` added so a direct push to main can still produce the green triad run AC2 needs, and awesome-lint pinned `@2.3.0` (the spec's stated pin; the hub PR workflow line is currently unpinned, the sysml-v2 lint.yml line pins `awesome-lint@2.3.0`).

- [ ] **Step 3: Adapt the S1/S2 templates (optional, spec Should)**

Copy and adapt:

```bash
mkdir -p "$SPOKE/.github/ISSUE_TEMPLATE"
cp "$HUB/.github/ISSUE_TEMPLATE/suggest-resource.yml" "$SPOKE/.github/ISSUE_TEMPLATE/suggest-resource.yml"
cp "$HUB/.github/PULL_REQUEST_TEMPLATE.md" "$SPOKE/.github/PULL_REQUEST_TEMPLATE.md"
```

Read both copies. Replace MBSE/SysML/Cameo wording with Capella/Arcadia wording, and update the checklist items to the spoke rules (entry format per CONTRIBUTING §3, tags per §4, canonical URL per §6, no banned hosts). Do not restructure the forms.

- [ ] **Step 4: Local sanity run of the two npx linters**

```bash
cd "$SPOKE" && npx -y markdownlint-cli2 "README.md" "CONTRIBUTING.md" && echo markdownlint-ok
cd "$SPOKE" && npx -y awesome-lint@2.3.0 README.md && echo awesome-lint-ok
```

awesome-lint talks to the GitHub API for the public repo, so this works after Task 2. Expected: both pass on the skeleton (empty sections are fine; entries arrive in Task 6).

- [ ] **Step 5: Commit and push**

```bash
git -C "$SPOKE" add -A
git -C "$SPOKE" commit -m "ci: wire family link-check triad (lychee strict, awesome-lint, markdownlint)"
git -C "$SPOKE" push origin main
```

**Done when:** three CI/config files on origin `main`, both local linters pass on the skeleton, schedule workflow is a byte-identical hub copy.

### Task 6: Seed pass to 40+ verified entries

**Files:**
- Modify: `README.md` (fill the nine sections)
- Modify: `CHANGELOG.md` (final verified count)

**Interfaces:**
- Consumes: README skeleton and section titles from Task 3, tag vocabulary and rules from Task 4.
- Produces: the verified entry count (integer) that gates Task 9, and the CHANGELOG count line for AC3.

**Model:** deep

This is the judgment task. Work section by section. Every candidate goes through the same loop: fetch it, apply the five-point bar, canonicalize the URL, check the banned-host list, assign tags in axis order, stamp the year with evidence. A candidate that fails any check is dropped, not squeezed. Quality gates the count; the count never gates quality.

- [ ] **Step 1: Pin the version identity**

```bash
gh api repos/eclipse-capella/capella/releases --jq '.[0] | .tag_name + " " + .published_at'
```

Research reported v7.1.0 (03 Aug 2026) as provisional because the tag URL 404'd. Record the actual latest tag and date; use that year for Capella repo year stamps. If the API disagrees with the research, the API wins.

- [ ] **Step 2: Harvest candidates per pillar**

Pillar targets sum past 40 (5+12+4+4+3+4+6+3 = 41, plus collaboration) so a few failures do not sink the bar. Named candidates come from the research; the fill-from column is the discovery source for the rest.

| Pillar (target) | Named candidates, verify each live | Fill remaining from |
|---|---|---|
| Capella core (5) | `https://mbse-capella.org/`, `https://github.com/eclipse-capella/capella`, `https://github.com/eclipse-capella/capella/releases` | Docs and Download pages linked from the product home nav; fetch the home page and follow the nav links, verify each |
| Addons and extensions (12) | `https://mbse-capella.org/addons.html`; `https://github.com/eclipse-capella/capella-requirements-vp`, `capella-cybersecurity`, `capella-xhtml-docgen`, `capella-sss-transition`, `capella-studio`; `https://github.com/labs4capella/stpa-capella`, `DSM4Capella`, `bridge-capella-ea` | The addons catalog page: enumerate its entries, verify each repo or page live |
| Scripting and automation (4) | `https://github.com/labs4capella/python4capella`, `https://github.com/dbinfrago/py-capellambse` | eclipse-capella and labs4capella org repo lists, the addons catalog |
| Arcadia method (4) | `https://mbse-capella.org/arcadia.html` | Method publications under `https://mbse-capella.org/resources.html`. Never `arcadia-method.com` (DNS dead). `download.eclipse.org` primers allowed only if they pass the bar; prefer mbse-capella.org when both exist |
| Books, courses, training (3) | Voirin Elsevier 2017 (`978-1-78548-169-7`), Roques Elsevier 2017 (`978-1-78548-168-0`), both `paid` | Book or training listings under resources.html |
| Community and events (4) | `https://mbse-capella.org/capella_days_2026.html` | Prior-edition pages actually linked from the Days page; do not invent replay playlists. Forum or community links from the home nav |
| Example models and case studies (6) | Case-study PDFs under `https://mbse-capella.org/resources.html` (Rolls-Royce, ArianeGroup, CNES); the IFE example model referenced from addons/resources | The resources page model and case-study sections |
| Commercial offers (3) | `https://www.obeosoft.com/en/capella-professional-offer` (strip the `#coaching` fragment per the canonical rule) | Obeo site training and services pages |
| Collaboration and model management (1+) | `https://github.com/labs4capella/mms-capella` | The Team for Capella product entry, only if Step 3 resolves it |

- [ ] **Step 3: Resolve Team for Capella or omit (decision 5)**

Search the web for the current Obeo or Thales product page ("Team for Capella", "Capella Collaboration Manager"). Research R4 found no durable public URL; candidate ObeoNetwork and eclipse-capella GitHub paths 404. Probe each candidate:

```bash
curl -sIL -o /dev/null -w "%{http_code}\n" "<candidate URL>"
```

A durable, live product page earns one entry under Collaboration and model management. No durable page means omit that product entry entirely and ship the section with mms-capella and anything else that passes the bar. Never guess a URL.

- [ ] **Step 4: Verify liveness of every candidate URL**

```bash
curl -sIL -o /dev/null -w "%{http_code} %{url_effective}\n" "<url>"
```

Accept 2xx. 429 means retry later, it is rate limiting, not death. Watch the `%{url_effective}` column: if the final URL landed on a different host after redirects, list the final canonical URL, and drop candidates whose final host is banned.

- [ ] **Step 5: Tag and stamp each surviving entry**

For each entry: language (exactly one), optional `Arcadia`, optional tool tags, optional `has-model` (directly downloadable `.aird` model project only), exactly one type, `standard` only if the AFNOR Z67-140 id was verified on the method page this run, `paid` for Elsevier books and commercial training, then `(YYYY)`.

Year evidence commands (repo object has no `tag_name`; use releases/tags):

```bash
gh api repos/<owner>/<repo>/releases/latest --jq '.tag_name + " " + (.published_at // .created_at)' 2>/dev/null
gh api repos/<owner>/<repo>/tags --jq '.[0].name' 2>/dev/null
gh api repos/<owner>/<repo> --jq '.pushed_at'
```

Papers and books: publication year (both Elsevier books are 2017). Product and method pages: the latest visible version or copyright year on the page; note the basis when it is ambiguous.

Format reference (shape, not copy-paste text; write factual descriptions from the actual resource):

```markdown
- [Eclipse Capella](https://mbse-capella.org/) - Official home of the open-source Capella MBSE tool implementing the Arcadia method `Capella` `tool` (2026).
- [The Arcadia method](https://mbse-capella.org/arcadia.html) - Official page for the Arcadia method (AFNOR Z67-140) and its perspectives `Capella` `Arcadia` `docs` (2026).
- [python4capella](https://github.com/labs4capella/python4capella) - Python API and scripting library to interact with Capella models and the Capella tool `Capella` `python4capella` `tool` (2026).
- [Model-based System and Architecture Engineering with the Arcadia Method (Voirin)](https://shop.elsevier.com/books/model-based-system-and-architecture-engineering-with-the-arcadia-method/voirin/978-1-78548-169-7) - Elsevier book by Jean-Luc Voirin on the Arcadia method and its engineering perspectives `Capella` `Arcadia` `book` `paid` (2017).
```

Placement per the spec: product home, source repo, docs, download, releases in Capella core; the addons catalog page heads Addons; python4capella and py-capellambse in Scripting; the Days hub in Community and events; the Obeo professional offer heads Commercial offers, competing training vendors after it.

- [ ] **Step 6: Count and decide the depth bar**

```bash
SPOKE="C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
grep -cE '^- \[[^]]+\]\(http' "$SPOKE/README.md"
```

Contents lines link to `#` anchors so they do not match; this counts section entries only, which matches the spec's verified-entry definition once Task 7's format check also passes. If the count is 40 or more, the depth bar is met and Task 9 runs. If under 40: stop adding, do not pad, keep every entry that honestly passed, and record the exact count in Step 7; Task 9 is then skipped and FAMILY stays Planned.

- [ ] **Step 7: Finalize the CHANGELOG count and commit locally (no push yet)**

Edit the CHANGELOG count line to the measured number and the outcome, for example `Verified seed count: 43 entries; depth bar met.` or `Verified seed count: 34 entries; depth bar unmet, FAMILY status stays Planned.` Then:

```bash
git -C "$SPOKE" add README.md CHANGELOG.md
git -C "$SPOKE" commit -m "feat: seed Capella/Arcadia entries from research pillars (verified pass)"
```

**Done when:** every listed entry passed the five checks with a live URL and clean canonical form, entries sit in the right sections with axis-ordered tags, the count is measured and recorded, the commit is local and unpushed.

### Task 7: Local verification gate before push

**Files:** `scripts/check_entries.py` (committed; support script for AC5 and the local gate).

**Interfaces:**
- Consumes: the seeded README (Task 6), CONTRIBUTING and CI config (Tasks 4-5).
- Produces: a green local gate: format checker exit 0, banned-host checks empty (host-path aware), count recorded, three linters pass, lychee exit 0, scripts/check_entries.py committed.

**Model:** standard

- [ ] **Step 1: Run the entry-format checker (AC5, full pass, not a spot check)**

Write `scripts/check_entries.py` (content below; `mkdir -p scripts` first). Do not delete it; AC5 re-runs this path after push. Commit it in Step 1b before Task 8 push:

- [ ] **Step 1b: Commit the checker and any README fixes from the gate**

```bash
mkdir -p "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella/scripts"
# after writing scripts/check_entries.py and any README fixes from Step 1 failures:
git -C "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella" add scripts/check_entries.py README.md CHANGELOG.md
git -C "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella" status
git -C "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella" commit -m "chore: add entry format checker and gate fixes"
```

If there is nothing to commit (already committed), `git status` is clean and this step is a no-op.

Script body:

```python
import re
import sys
from urllib.parse import urlsplit

readme = open("README.md", encoding="utf-8").read()
LANG = {"Capella", "UAF", "SysML-general"}
TYPE = {"tutorial", "course", "book", "paper", "blog", "video", "tool", "plugin", "docs", "case-study"}
BANNED_SUBSTR = (
    "arcadia-method.com",
    "polarsys",
    "projects.eclipse.org/projects/modeling.capella",
)
# Host-path bans: match netloc+path, not raw substring (download.eclipse.org/capella is allowed)
BANNED_HOST_PATH = (
    ("eclipse.org", "/capella"),
    ("www.eclipse.org", "/capella"),
    ("eclipse.dev", "/capella"),
)
entry = re.compile(r"^- \[([^\]]+)\]\((https?://[^)\s]+)\) - (.*)$")
errors, canonical, n = [], {}, 0
for ln, line in enumerate(readme.splitlines(), 1):
    if not line.startswith("- ["):
        continue
    m = entry.match(line)
    if not m:
        if "](#" not in line:  # Contents lines link to in-page anchors, skip them
            errors.append(f"{ln}: malformed entry line")
        continue
    name, url, rest = m.groups()
    n += 1
    parts = urlsplit(url)
    host = (parts.hostname or "").lower()
    path = parts.path or ""
    for tok in BANNED_SUBSTR:
        if tok in url:
            errors.append(f"{name}: banned host token {tok}")
    for bh, bp in BANNED_HOST_PATH:
        if host == bh or host.endswith("." + bh):
            if path == bp or path.startswith(bp + "/"):
                errors.append(f"{name}: banned host path {bh}{bp}")
    key = (parts.scheme, parts.netloc.lower(), parts.path.rstrip("/"))
    if key in canonical:
        errors.append(f"{ln}: canonical duplicate of line {canonical[key]}: {url}")
    canonical[key] = ln
    if not rest.endswith(")."):
        errors.append(f"{ln}: must end with '(YYYY).'")
        continue
    body, year = rest[:-2].rsplit("(", 1)
    if not re.fullmatch(r"\d{4}", year):
        errors.append(f"{ln}: year token not YYYY: ({year})")
    tags = re.findall(r"`([^`]+)`", body)
    desc = re.sub(r"`[^`]+`", "", body).strip()
    if len(desc) > 140:
        errors.append(f"{ln}: description {len(desc)} chars (> 140)")
    if not tags or tags[0] not in LANG:
        errors.append(f"{ln}: first tag must be a language from {sorted(LANG)}, got {tags[:1]}")
    if len([t for t in tags if t in LANG]) != 1:
        errors.append(f"{ln}: language cardinality must be exactly 1")
    type_tags = [t for t in tags if t in TYPE]
    if len(type_tags) != 1:
        errors.append(f"{ln}: type cardinality must be exactly 1, got {type_tags}")
    if any(re.fullmatch(r"\d{4}", t) for t in tags):
        errors.append(f"{ln}: year must be the parenthetical token, not a backtick tag")
print(f"entries: {n}")
print("\n".join(errors) if errors else "format: OK")
sys.exit(1 if errors else 0)
```

Run:

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella" && python scripts/check_entries.py
```

Expected: `format: OK`, zero exit. Fix every finding in README.md and rerun until clean.

- [ ] **Step 2: Banned-host grep (AC4)**

```bash
# Host-aware banned-host proof: prefer scripts/check_entries.py (excludes download.eclipse.org).
# Additional string scan (do not treat download.eclipse.org as a hit):
grep -nE 'arcadia-method\.com|polarsys|projects\.eclipse\.org/projects/modeling\.capella' "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella/README.md" || true
python - <<'PY2'
from urllib.parse import urlsplit
import re
text=open("C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella/README.md",encoding="utf-8").read()
for m in re.finditer(r"\((https?://[^)]+)\)", text):
    u=m.group(1); h=(urlsplit(u).hostname or "").lower(); path=urlsplit(u).path or ""
    if h in {"eclipse.org","www.eclipse.org","eclipse.dev"} and (path=="/capella" or path.startswith("/capella/")):
        raise SystemExit(f"banned href {u}")
print("eclipse host-path bans: OK")
PY2 "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella/README.md"
```

Expected: no matches (grep exit 1). Official Capella pages use mbse-capella.org. If a match appears, fix the entry to the canonical mbse-capella.org URL or drop it. Never solve a match by adding the host to `.lycheeignore` (spec S3).

- [ ] **Step 3: Depth-bar count cross-check**

```bash
grep -cE '^- \[[^]]+\]\(http' "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella/README.md"
```

Confirm the number matches Task 6 Step 6 and the CHANGELOG line.

- [ ] **Step 4: Run the two npx linters locally**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella" && npx -y markdownlint-cli2 "README.md" "CONTRIBUTING.md" && echo markdownlint-ok
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella" && npx -y awesome-lint@2.3.0 README.md && echo awesome-lint-ok
```

Expected: both pass. awesome-lint failure modes to expect and fix in the README, not in the linter: title or badge order drift from the skeleton, entries written with an en/em dash instead of ` - `.

- [ ] **Step 5: Local strict lychee with anchor-only fragments (AC7 shape)**

```bash
docker run --rm -v "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella:/d" -w /d lycheeverse/lychee --include-fragments=anchor-only --max-concurrency 4 --accept 200..=299,429 --no-progress README.md
```

Expected: exit 0, every Contents anchor and entry URL resolves. If docker is unavailable on this machine, substitute a draft PR and let CI run lychee (the Task 8 dispatch run also proves AC7), but run Steps 1-4 locally regardless. Fix any dead link by repairing or dropping the entry; never by ignoring the host.

**Done when:** checker exit 0 with the recorded count, banned grep empty, markdownlint and awesome-lint pass locally, lychee anchor-only run passes locally or a draft PR proves it green.

### Task 8: Push and prove the CI triad green on main

**Files:** none new. Pushes Task 6-7 work and produces the AC2 run.

**Interfaces:**
- Consumes: green Task 7 gate.
- Produces: the green `link-check (PR)` run on main that AC2 and Task 10 read.

**Model:** standard

- [ ] **Step 1: Push the seeded README**

```bash
git -C "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella" push origin main
```

- [ ] **Step 2: Dispatch the PR workflow on main**

The workflow triggers on pull_request by design, so a direct push to main does not run it. The `workflow_dispatch` trigger added in Task 5 covers the AC2 gap:

```bash
gh workflow run "link-check (PR)" --repo jgsystemsconsulting/awesome-capella --ref main
sleep 10
gh run list --repo jgsystemsconsulting/awesome-capella --workflow "link-check (PR)" --limit 1
```

- [ ] **Step 3: Watch the run to green**

```bash
RUN_ID=$(gh run list --repo jgsystemsconsulting/awesome-capella --workflow "link-check (PR)" --limit 1 --json databaseId --jq '.[0].databaseId')
gh run watch "$RUN_ID" --repo jgsystemsconsulting/awesome-capella --exit-status
gh run view "$RUN_ID" --repo jgsystemsconsulting/awesome-capella --json jobs --jq '.jobs[] | .name + " " + .conclusion'
```

Expected: three jobs, all `success`: lychee, awesome-lint, markdownlint. If lychee reports a dead link that local checks missed, fix the entry, push, re-dispatch, re-watch. If awesome-lint or markdownlint fails, fix and repeat. Iterate until green; a first-run failure here is normal, a padded entry is not.

- [ ] **Step 4: Smoke the schedule workflow once (optional but cheap)**

```bash
gh workflow run "link-check (weekly)" --repo jgsystemsconsulting/awesome-capella
```

Then confirm it created exactly one `link-rot` report issue. This validates the report-only path before the first real cron Monday. Note: M5 is satisfied by the PR workflow run in Step 3; this step is extra assurance.

**Done when:** latest `link-check (PR)` run on main is green across lychee (`fail: true`, anchor-only), awesome-lint, and markdownlint (AC2).

### Task 9: Conditional hub updates, only when the depth bar is met

**Files (hub repo, `C:\Users\gower\OneDrive\Documents\GitHub\awesome-mbse`):**
- Modify: `FAMILY.md` (registry row)
- Modify: `README.md` (list-family row, gaps sentence, Broader Context shrink)

**Interfaces:**
- Consumes: verified count 40 or more from Tasks 6-7, and the green main from Task 8.
- Produces: the hub-side half of AC3.

**Model:** standard

Gate: if the verified count is under 40, skip this task entirely. The spoke shipped in Task 8; FAMILY stays Planned; the hub stays untouched; the CHANGELOG shortfall already documents it (decision 4, M8).

- [ ] **Step 1: Flip the FAMILY.md registry row**

In `FAMILY.md`, change the row from:

```markdown
| awesome-capella | Capella tool and the Arcadia method | Planned | none yet |
```

to:

```markdown
| [awesome-capella](https://github.com/jgsystemsconsulting/awesome-capella) | Capella tool and the Arcadia method | Live | public |
```

Visibility becomes `public` to match the row format the Live spokes use (awesome-sysml-v2 reads `Live | public`). Leave the namespace table row and every other FAMILY line untouched; the spec's hub touch list says nothing else.

- [ ] **Step 2: Update the hub README list-family row**

In the hub `README.md`, change:

```markdown
| awesome-capella | Capella tool and the Arcadia method | Planned | Broader Context Capella/Arcadia entries (thin) |
```

to:

```markdown
| [awesome-capella](https://github.com/jgsystemsconsulting/awesome-capella) | Capella tool and the Arcadia method | Live | Linked public spoke |
```

- [ ] **Step 3: Update the gaps sentence**

In the same README, the snapshot sentence currently ends:

```markdown
Capella is four entries (the Arcadia
method page, the Arcadia primer, py-capellambse, Eclipse Capella).
```

Change that clause to:

```markdown
Capella moved to the awesome-capella spoke (the hub keeps only the cross-cutting
methodology directory entry).
```

- [ ] **Step 4: Shrink Broader Context Capella/Arcadia material**

Remove these four entries, whose primary subject is Capella or Arcadia alone:

- `[Arcadia Method (official)](https://mbse-capella.org/arcadia.html)` (under Methodology & method references)
- `[An Introduction to Arcadia (Voirin)](https://download.eclipse.org/capella/publis/An_Introduction_to_Arcadia_20150115.pdf)` (same subsection)
- `[Eclipse Capella](https://mbse-capella.org/)` (under Other MBSE tools)
- `[py-capellambse](https://github.com/DSD-DBS/py-capellambse)` (under Other MBSE tools; hub href as of plan write; spoke seeds https://github.com/dbinfrago/py-capellambse)

Keep `[OMG MBSE Wiki — Methodology Directory](https://www.omgwiki.org/MBSE/doku.php?id=mbse:methodology)`: it lists Arcadia among many methods, so it is cross-cutting (spec decision 6 names it as the keep example).

Add this pointer line directly under the "Cross-tool MBSE methods" intro sentence in Methodology & method references:

```markdown
> Capella and Arcadia-specific resources live in the family spoke
> [awesome-capella](https://github.com/jgsystemsconsulting/awesome-capella).
```

Do not touch the External awesome lists TODO paragraph, the scope table, or anything else; the spec's hub touch list is exhaustive.

- [ ] **Step 5: Commit and push the hub**

```bash
git -C "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse" add FAMILY.md README.md
git -C "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse" commit -m "feat: awesome-capella spoke live; shrink hub Capella/Arcadia to cross-cutting"
git -C "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse" push origin main
```

**Done when:** FAMILY row reads `Live | public` with the spoke URL, hub README links the spoke near the top, the four Capella-primary entries are gone, the methodology directory entry and the pointer remain, hub pushed.

### Task 10: Acceptance checklist, AC1 through AC7

**Files:** none. Final verification pass over both repos.

**Model:** flash

Run each check; record pass or fail. All seven must pass before the effort is reported done.

- [ ] **AC1. Repo and sibling clone exist**

```bash
gh repo view jgsystemsconsulting/awesome-capella --json visibility --jq .visibility
test -d "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella/.git" && echo sibling-ok
```

Expected: `PUBLIC`, `sibling-ok`.

- [ ] **AC2. Latest PR link-check run on main green across the triad**

```bash
gh run list --repo jgsystemsconsulting/awesome-capella --workflow "link-check (PR)" --limit 1
gh run view $(gh run list --repo jgsystemsconsulting/awesome-capella --workflow "link-check (PR)" --limit 1 --json databaseId --jq '.[0].databaseId') --repo jgsystemsconsulting/awesome-capella --json jobs --jq '.jobs[] | .name + " " + .conclusion'
```

Expected: run on `main` refs/heads/main, jobs lychee + awesome-lint + markdownlint all `success`. Schedule-only green does not count.

- [ ] **AC3. Depth-bar rule applied correctly**

```bash
grep -cE '^- \[[^]]+\]\(http' "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella/README.md"
grep -n "Verified seed count" "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella/CHANGELOG.md"
grep -nE "\[?awesome-capella(\]\([^)]+\))?[^|]*\|[^|]*\| *Live" "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse/FAMILY.md"
```

Expected: count matches CHANGELOG. If count ≥ 40, the FAMILY grep finds the Live row and Task 9 ran. If under 40, the FAMILY row still reads Planned and Task 9 was skipped.

- [ ] **AC4. Zero banned or redirect hosts**

```bash
# Host-aware banned-host proof: prefer scripts/check_entries.py (excludes download.eclipse.org).
# Additional string scan (do not treat download.eclipse.org as a hit):
grep -nE 'arcadia-method\.com|polarsys|projects\.eclipse\.org/projects/modeling\.capella' "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella/README.md" || true
python - <<'PY2'
from urllib.parse import urlsplit
import re
text=open("C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella/README.md",encoding="utf-8").read()
for m in re.finditer(r"\((https?://[^)]+)\)", text):
    u=m.group(1); h=(urlsplit(u).hostname or "").lower(); path=urlsplit(u).path or ""
    if h in {"eclipse.org","www.eclipse.org","eclipse.dev"} and (path=="/capella" or path.startswith("/capella/")):
        raise SystemExit(f"banned href {u}")
print("eclipse host-path bans: OK")
PY2 "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella/README.md"
```

Expected: no output. Official Capella pages use mbse-capella.org:

```bash
grep -c 'https://mbse-capella\.org' "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella/README.md"
```

Expected: 1 or more.

- [ ] **AC5. Every entry matches the tagged format and cardinalities**

Re-run the Task 7 checker against the pushed state:

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella" && python scripts/check_entries.py
```

Expected: `format: OK` with the recorded count, exit 0. The script proves language/type/year/banned-host/desc length. Axis order and optional-tag membership still need a full manual pass of every entry (or an extended checker). Spot check alone is not enough for ship.

- [ ] **AC6. CONTRIBUTING.md with the frozen rules**

```bash
test -f "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella/CONTRIBUTING.md" && echo uppercase-ok
grep -cE "## 5. The year rule|## 6. Canonical-URL rule|## Editorial neutrality" "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella/CONTRIBUTING.md"
```

Expected: `uppercase-ok`, count 3.

- [ ] **AC7. Anchor-only lychee proves every Contents anchor resolves**

Evidence: the green lychee job in the AC2 run (and/or the Task 7 local docker run). Confirm the workflow args contained `--include-fragments=anchor-only`:

```bash
grep -n "include-fragments=anchor-only" "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella/.github/workflows/link-check-pr.yml"
```

Expected: match found, job conclusion `success` from AC2.

**Done when:** all seven checks pass, or a failing check sends the work back to the owning task (6, 7, 8, or 9), never waved through.
