# Awesome STPA Spoke Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship `jgsystemsconsulting/awesome-stpa` v1 (private) to the FAMILY shared standard with at least 40 live, format-conformant entries, then flip the hub registry and README to Live.

**Architecture:** New sibling repo next to `awesome-mbse` and `awesome-sysml-v2`, built from the hub CONTRIBUTING rules plus the hub lychee workflows, hardened per the spec (SHA pins, blocking PR check, uppercase CONTRIBUTING). Entry population uses the research gate's 42-candidate inventory. Hub edits are the closing change set, only after spoke CI is green on main.

**Tech Stack:** Markdown, GitHub Actions (lychee, awesome-lint, markdownlint-cli2), `gh` CLI, Docker (local link check), CC0-1.0.

**Spec:** docs/superpowers/specs/2026-09-17-awesome-stpa.md

## Global Constraints

Values below are copied from the spec and FAMILY.md. Every task inherits this section.

- Repo: `jgsystemsconsulting/awesome-stpa`. Namespace re-checked the day the remote is created (FAMILY rule). Default branch `main`.
- Local path: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-stpa` (Git Bash: `/c/Users/gower/OneDrive/Documents/GitHub/awesome-stpa`), sibling of the hub.
- Repo description (exact): `Curated list of STAMP/STPA and hazard analysis resources`. Topics (exact): `stpa`, `stamp`, `safety`, `hazard-analysis`, `awesome-list`, `awesome`.
- Private first (FAMILY Private mode). Public release is a separate later decision; v1 acceptance may complete while private.
- License CC0-1.0. No MIT license text or license metadata anywhere. Nominative use of "MIT" in entry names and descriptions (MIT PSAS, MIT Press, MIT STAMP workshop) is required and allowed.
- Entry format: `- [Name](url) - Description `tags` (YYYY).` Hyphen separator, description at most 140 characters, tags as inline code spans before the terminal period, year as the last token.
- `CONTRIBUTING.md` uppercase filename. Hub CONTRIBUTING.md section 5 (year rule) and section 6 (canonical-URL rule) copied verbatim; PSAS `get_file.php?name=` query strings called out as semantically required.
- Family pointer is text only while the hub is private: `Part of the awesome-mbse list family (hub repository currently private).` No FAMILY.md hyperlink.
- CI: `link-check-pr.yml` blocking (lychee `--include-fragments=anchor-only --max-retries 3 --accept 200..=299,429 --max-concurrency 4`, `fail: true`, token passed, triggers `pull_request` and `push` to main); `link-check-schedule.yml` cron-only weekly, opens or replaces the `link-rot` report issue; `lint.yml` runs awesome-lint plus markdownlint on `README.md` and `CONTRIBUTING.md`. Every action ref pinned to a full commit SHA.
- At least 40 full-format entries. Quarantined hosts (CONTRIBUTING known-rot appendix) never appear as live entry URLs. `.lycheeignore` ships comment-only; entries only after CI fails a browser-verifiable URL, with a dated comment.
- J3187 and AIR6913 enter only after a live SAE catalog URL verifies at execute; not required for the 40 floor.
- No ArchiMate content. No claim that ISO 26262, ARP4761A, or IEC 61508 mandates STPA. No re-hosting content. Deferred past v1: CITATION.cff, `docs/` site, `stale.yml`, issue forms, social card, sindresorhus/awesome submission.
- Hub edits land LAST, only after the spoke's push workflows are green (spec order of work, AC13).
- Order of work: repo, skeleton, CONTRIBUTING, workflows, README entries, CHANGELOG and push with CI green, hub edits, acceptance pass.

## Codebase context

- `FAMILY.md` (hub) is the constitution. Relevant lines at HEAD `4f7c0a63`: Registry table row for awesome-stpa (line 55), namespace table row (line 100), Shared standard (line 104), Starting a new list (line 131), awesome-stpa create checklist (lines 198-207), README skeleton (line 227).
- Hub `CONTRIBUTING.md`: section 5 (lines 71-83) and section 6 (lines 84-88) are the verbatim port sources. Section 7 is the neutrality model.
- Hub `.github/workflows/link-check-pr.yml` is the blocking lychee reference (anchor-only fragments, accept 200..299 and 429, `fail: true`, token). Hub `.github/workflows/link-check-schedule.yml` is the weekly report reference (close-then-create, `link-rot` label, title `Weekly link-rot report`). Hub still floats `actions/checkout@v4` and `peter-evans/create-issue-from-file@v5`; this spoke pins every ref.
- Sibling `awesome-sysml-v2` supplies the SHA-pin discipline and config shapes: `.github/workflows/lint.yml` (pinned checkout `11d5960a326750d5838078e36cf38b85af677262`, setup-node `49933ea5288caeca8642d1e84afbd3f7d6820020`, markdownlint-cli2-action `21c1be1b93ad9ed58fa840aacc3f279cde2a72ff`), `.markdownlint-cli2.jsonc`. Do not copy its drift: bare entries, lowercase `contributing.md`, advisory lychee without fragments, missing sweep badge, MIT citation. It has no NOTICE; the hub NOTICE is the port source.
- Hub README family table (lines 25-34) and the gaps snapshot paragraph (lines 36-39) are the hub-chrome edit targets in Task 7.

## Research

Gate files (retrieved 2026-09-17):

- research: docs/superpowers/research/2026-09-17-awesome-stpa-sources-research.md (SC1 namespace provisional-clear, SC2 42-candidate inventory plus exclusion list, SC3 skeleton, SC4 tag values; the spec rejects SC4's `domain` axis)
- context: docs/superpowers/context/2026-09-17-awesome-stpa-pattern-context.md (FAMILY findings, sysml-v2 drift list, HEAD `4f7c0a63`)

Primary URLs this plan builds from:

- https://psas.scripts.mit.edu/home/
- https://psas.scripts.mit.edu/home/get_file.php?name=STPA_Handbook.pdf
- https://psas.scripts.mit.edu/home/get_file4.php?name=CAST_Handbook.pdf
- https://direct.mit.edu/books/oa-monograph/2908/Engineering-a-Safer-WorldSystems-Thinking-Applied
- https://github.com/SE-Stuttgart/XSTAMPP
- https://github.com/labs4capella/stpa-capella
- https://www.sae.org/standards/content/arp4761a/
- https://www.iso.org/standard/68383.html
- https://rosap.ntl.bts.gov/view/dot/78914/dot_78914_DS1.pdf
- https://github.com/sindresorhus/awesome
- https://awesome.re/badge.svg

## File structure

New repo `C:\Users\gower\OneDrive\Documents\GitHub\awesome-stpa`:

| File | Responsibility |
|------|----------------|
| `README.md` | The list: chrome (badge, scope, sweep badge, text-only family pointer, maintainer line), flat ToC, seven content sections, 43 entries |
| `LICENSE` | CC0-1.0 full text, hub copy with the repo name swapped on line 1 |
| `CONTRIBUTING.md` | Rules: suggest path, inclusion bar, entry format, STPA tag vocabulary, verbatim hub sections 5 and 6, neutrality, local link check, cadence, known-rot appendix |
| `CODE_OF_CONDUCT.md` | Verbatim hub copy |
| `SECURITY.md` | Verbatim hub copy (no repo name inside, so nothing to adjust) |
| `NOTICE` | CC0 waiver and nominative-use note, adapted from hub (no Dassault/OMG text) |
| `CHANGELOG.md` | Initial release entry; its month is the sweep badge month |
| `.gitignore` | Verbatim hub copy (OS, editor, lychee output, node) |
| `.lycheeignore` | Comment-only policy at ship; dated entries only after CI failures |
| `.markdownlint-cli2.jsonc` | Sysml-v2 copy unchanged (`MD013: false`) |
| `.github/PULL_REQUEST_TEMPLATE.md` | Format and inclusion checklist |
| `.github/workflows/link-check-pr.yml` | Blocking lychee, PR and push to main |
| `.github/workflows/link-check-schedule.yml` | Cron-only weekly link-rot report issue |
| `.github/workflows/lint.yml` | awesome-lint plus markdownlint, SHA-pinned, node 20 |

Hub edits (Task 7, in `C:\Users\gower\OneDrive\Documents\GitHub\awesome-mbse`): `FAMILY.md` (registry row, namespace row, awesome-stpa checklist), `README.md` (family table rows, gaps sentence, namespace re-check paragraph).

Action ref pins used in Task 4 (verified sources noted):

| Action | Ref |
|--------|-----|
| actions/checkout | `11d5960a326750d5838078e36cf38b85af677262` (v4, from awesome-sysml-v2 lint.yml and links.yml) |
| actions/setup-node | `49933ea5288caeca8642d1e84afbd3f7d6820020` (v4, from awesome-sysml-v2 lint.yml) |
| lycheeverse/lychee-action | `e7477775783ea5526144ba13e8db5eec57747ce8` (hub and sysml-v2, run with `lycheeVersion: v0.24.2`) |
| DavidAnson/markdownlint-cli2-action | `21c1be1b93ad9ed58fa840aacc3f279cde2a72ff` (v24, from awesome-sysml-v2 lint.yml) |
| peter-evans/create-issue-from-file | `e8ef132d6df98ed982188e460ebb3b5d4ef3a9cd` (v5, resolved from the GitHub API on 2026-09-17) |

---

### Task 1: Namespace recheck, private repo create, sibling clone

**Files:** none on disk yet (GitHub remote plus empty clone).

**Interfaces:** Produces the repo, the local clone path, and the create-day date string used by Tasks 5 to 7.

**Model:** flash

- [ ] **Step 1: Confirm auth and org access**

```bash
gh auth status
gh api user --jq .login
gh api orgs/jgsystemsconsulting/members/"$(gh api user --jq .login)" --include 2>&1 | head -1
```

Expected: authenticated, and the org membership call returns HTTP 204. If you cannot create repos in the org, stop and ask the maintainer. Do not create the repo under a personal account as a fallback.

- [ ] **Step 2: Re-check the namespace (FAMILY rule: same day as create)**

```bash
gh api -X GET "search/repositories?q=awesome-stpa%20in:name" --jq '.total_count, (.items[].full_name)'
gh api -X GET "search/repositories?q=awesome-stamp%20in:name" --jq '.total_count, (.items[].full_name)'
```

Decision rule (FAMILY Model rule 2): if any hit is a curated STAMP/STPA list with 100+ stars or updated within the last year, stop and report; do not create. Expected 2026-09 result: no such incumbent (research SC1 found only unrelated "Stamp" hits). Record the result: `empty` or the incumbent names, plus today's date. This string feeds Task 7.

- [ ] **Step 3: Create the private repo and clone it as a sibling**

```bash
cd "/c/Users/gower/OneDrive/Documents/GitHub"
gh repo create jgsystemsconsulting/awesome-stpa \
  --private \
  --description "Curated list of STAMP/STPA and hazard analysis resources" \
  --clone
cd awesome-stpa
git symbolic-ref HEAD refs/heads/main
```

Expected: empty clone at `/c/Users/gower/OneDrive/Documents/GitHub/awesome-stpa`; `git status` on unborn branch `main`.

- [ ] **Step 4: Set topics**

```bash
gh repo edit jgsystemsconsulting/awesome-stpa \
  --add-topic stpa --add-topic stamp --add-topic safety \
  --add-topic hazard-analysis --add-topic awesome-list --add-topic awesome
```

- [ ] **Step 5: Verify**

```bash
gh repo view jgsystemsconsulting/awesome-stpa --json visibility,description,repositoryTopics
```

Expected: `visibility: PRIVATE`, description matches the constraint string, six topics. `defaultBranchRef` may be null until the first push (Task 6 creates `main`).

---

### Task 2: Skeleton files

**Files:**
- Create: `LICENSE`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `NOTICE`, `.gitignore`, `.lycheeignore`, `.markdownlint-cli2.jsonc`, `.github/PULL_REQUEST_TEMPLATE.md`

**Interfaces:** Consumes the hub copies at `../awesome-mbse/`. Produces the lint config the Task 3 and Task 4 linters read, and the PR template AC6 relies on.

**Model:** flash

- [ ] **Step 1: Copy the verbatim family files**

```bash
cd "/c/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
sed '1s/awesome-mbse/awesome-stpa/' "../awesome-mbse/LICENSE" > LICENSE
cp "../awesome-mbse/CODE_OF_CONDUCT.md" CODE_OF_CONDUCT.md
cp "../awesome-mbse/SECURITY.md" SECURITY.md
cp "../awesome-mbse/.gitignore" .gitignore
cp "../awesome-sysml-v2/.markdownlint-cli2.jsonc" .markdownlint-cli2.jsonc
mkdir -p .github .github/workflows
```

The sed only rewrites the repo name on line 1 of LICENSE; the CC0 legal text stays verbatim. (License text is a verbatim family port, so the hub's line-1 punctuation is kept as is.)

- [ ] **Step 2: Write NOTICE**

Create `NOTICE` with exactly:

```text
awesome-stpa

Maintained by JG Systems Consulting Ltd.

This work (the curated index in README.md and the repository's own files) is released
under CC0 1.0 Universal (see LICENSE). To the extent possible under law, the maintainers
have waived all copyright and related rights to it.

Linked resources are the property of their respective owners and are referenced, not
redistributed. "STPA", "STAMP", and "CAST" are used to name the methods the listed
resources teach and apply; method names are used nominatively, with no implication of
endorsement.
```

- [ ] **Step 3: Write the comment-only `.lycheeignore`**

Create `.lycheeignore` with exactly:

```text
# Ignore policy: add a line only after CI reports a URL failed but the URL is
# verifiably live in a browser. Every entry is a hole in the freshness guarantee.
# Format: one regex per line, with a dated comment above it naming the browser
# verification used and the removal condition. Re-verify every entry at each
# quarterly sweep.
#
# Standing candidates (research 2026-09-17), NOT ignored yet: MIT Press book
# pages and iso.org / sae.org catalog pages can 403 automated fetchers. If CI
# reports one, browser-verify it, then add the exact URL with a dated comment.
```

- [ ] **Step 4: Write the PR template**

Create `.github/PULL_REQUEST_TEMPLATE.md` with exactly:

```markdown
<!-- Thanks for contributing! Check every box; CI enforces most of these. -->

## What I'm adding / changing

<!-- one line -->

## Inclusion bar (CONTRIBUTING.md section 2)

- [ ] On-topic for STAMP/STPA/CAST or hazard analysis
- [ ] Substantive: not a stub, not pure vendor marketing
- [ ] Link is live (CI link-checks it; Docker one-liner in CONTRIBUTING.md section 8)
- [ ] Not a duplicate (canonical-URL rule, CONTRIBUTING.md section 6)
- [ ] Publicly accessible: linked, not re-hosted
- [ ] Host is not in the known-rot appendix (CONTRIBUTING.md section 10)

## Entry format (CONTRIBUTING.md sections 3 and 4)

- [ ] `- [Name](url) - Description ` + inline-code tags + `(YYYY).`, hyphen separator, not an en/em dash
- [ ] Description at most 140 characters
- [ ] Exactly one language tag and one type tag; remaining tags from the vocabulary in axis order (language -> method -> tool -> has-model -> type -> spec/standard -> paid -> year)
- [ ] `(YYYY)` is the resource's most recent author-published version (CONTRIBUTING.md section 5)

## Housekeeping

- [ ] If a top-level section was added or renamed, the hand-maintained `## Contents` ToC was updated
```

- [ ] **Step 5: Verify**

```bash
cd "/c/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
head -1 LICENSE
grep -c "CC0 1.0 Universal" LICENSE
grep -rniE "\bMIT\b" LICENSE NOTICE SECURITY.md CODE_OF_CONDUCT.md .gitignore .lycheeignore .markdownlint-cli2.jsonc .github/PULL_REQUEST_TEMPLATE.md
ls CONTRIBUTING.md contributing.md 2>&1 || true
```

Expected: line 1 starts `awesome-stpa`; CC0 count at least 1; the MIT scan prints nothing; `contributing.md` does not exist (uppercase filename only lands in Task 3).

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "chore: family skeleton (LICENSE, CoC, SECURITY, NOTICE, lint config, PR template)"
```

---

### Task 3: CONTRIBUTING.md

**Files:**
- Create: `CONTRIBUTING.md`

**Interfaces:** Produces the section anchors and tag vocabulary that Task 5 (README neutrality link `CONTRIBUTING.md#7-editorial-neutrality`) and the Task 2 PR template reference.

**Model:** standard

- [ ] **Step 1: Write CONTRIBUTING.md**

Create `CONTRIBUTING.md` with exactly the content below. Section numbers are chosen so the ported rules keep their hub numbers (5 and 6), which the spec and PR template reference.

````markdown
# Contributing

Thanks for helping keep this the best-curated STAMP/STPA index anywhere. Read this
before opening a PR; CI gates enforce most of it.

In v1 the only path is a pull request editing `README.md` directly (no issue forms yet).

## 1. How to suggest a resource

Open a pull request that edits `README.md`, follow the entry format below, and tick the
PR checklist. CI link-checks your entry and lints the list.

## 2. Inclusion bar

An entry is accepted only if **all** hold:

1. **On-topic:** genuinely about STAMP, STPA, CAST, hazard analysis, or the
   functional-safety context where those methods are used or discussed.
2. **Substantive:** it teaches, demonstrates, specifies, or provides something usable.
   Not a stub. Not pure vendor marketing.
3. **Live:** the link resolves right now.
4. **Not duplicative:** not already listed (see the canonical-URL rule, section 6).
5. **Legally linkable:** publicly accessible. We **link**, we never re-host PDFs or
   proprietary content.

Tie-breakers (nice-to-have, not gates): has a directly downloadable, tool-openable STPA
case or example (`has-model`), recently updated, from a recognized source (MIT, a
regulator, a university, an established practitioner).

## 3. Entry format

One line per entry, **hyphen separator** (` - `, never an en/em dash; awesome-lint
rejects those), tags as **inline code spans inside the sentence before the terminal
period**, year parenthesized as the last token:

- [STPA Handbook](https://psas.scripts.mit.edu/home/get_file.php?name=STPA_Handbook.pdf) - Free process handbook for System-Theoretic Process Analysis by Leveson and Thomas `STPA` `handbook` (2018).

- **Description:** factual, one line, **at most 140 characters** (measured from the
  first character after ` - ` to the last character before the first tag, excluding the
  link markup and tags). No hype.
- **`has-model`** means: a **directly downloadable, non-paywalled** STPA case or example
  that opens in a named tool. Screenshots, papers *describing* an analysis, and
  access-gated files **do not** qualify.

## 4. Tag vocabulary, cardinality and order

Tags appear in this fixed order, drawn **only** from this vocabulary:

`language -> method -> tool -> has-model -> type -> spec/standard -> paid -> year`

| Axis | Cardinality | Values |
|------|-------------|--------|
| language | exactly 1 | `STPA` (process analysis primary) - `CAST` (accident analysis primary) - `STPA-Sec` (security/threat-model primary) - `STAMP-general` (methodology-wide: books, hubs, related lists, multi-method platforms, standards context) |
| method | 0 or 1 | `HARA` - `FTA` - `FMEA` - `HazOp` (companion technique the resource couples with) |
| tool | 0 or more | `XSTAMPP` - `PASTA` - `stpa-capella` - `MicroSTAMP` - `CAIRIS` - `other-tool` |
| has-model | 0 or 1 | `has-model` |
| type | exactly 1 (dominant form) | `handbook` - `book` - `paper` - `standard` - `tool` - `course` - `video` - `case` - `dataset` - `workshop` - `list` |
| spec/standard | 0 or 1 | `ISO-26262` - `ARP4761A` - `IEC-61508` - `J3187` - `AIR6913` (entry is tied to that normative document) |
| paid | 0 or 1 | `paid`, when the linked URL's primary artifact requires purchase or a paid account. Free catalog/landing pages of paywalled standards are **not** `paid`. |
| year | exactly 1 | `(YYYY)` (see section 5) |

- Multi-method tools take their primary method or `STAMP-general`.
- A `tool` tag is required whenever `has-model` is present.
- `other-tool` graduates to its own tag once 3 or more entries share it (hub rule).
- There is no `domain` tag. Domain belongs in the description prose only.

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

Query strings that are semantically required survive canonicalization. The MIT PSAS
file links are the standing example:
`https://psas.scripts.mit.edu/home/get_file.php?name=STPA_Handbook.pdf` and
`https://psas.scripts.mit.edu/home/get_file4.php?name=CAST_Handbook.pdf` name the file
they serve; strip the query and you point at the wrong resource.

## 7. Editorial neutrality

This list is maintained by JG Systems Consulting Ltd., a commercial vendor of
SysML/Cameo tooling. It has no STPA, CAST, or hazard-analysis product, so no
vendor-conflict applies today. If that ever changes, the family rules bind unchanged:

- JGS products are listed by the **same inclusion bar** as everything else.
- Every JGS entry sits next to **at least 1 genuine competing/alternative entry**.
- **A superior competing entry is listed above a JGS one.** Neutrality is enforced by
  this rule, not by tone.

Tool-listing note: the PSAS stamp-tools catalog is linked as an awareness list, not an
endorsement. Commercial entries must clear the same "not pure vendor marketing" bar:
link product documentation or method pages with substance, not landing pages alone.

## 8. Local link-check

No install needed; check your links with Docker, using the same arguments CI uses:

```sh
docker run --rm -v "$PWD:/d" -w /d lycheeverse/lychee --include-fragments=anchor-only --max-retries 3 --accept 200..=299,429 README.md
```

Or open a **draft PR** and let CI check it for you.

## 9. Maintenance cadence

The maintainers run a **quarterly sweep** (add new resources, prune rot), logged in
`CHANGELOG.md` with the date, and update the *Last full sweep* badge at the top of the
README each time. If more than **6 months** pass since the last sweep, the badge flips
to "maintenance lapsed"; call it out in an issue.

## 10. Known-rot appendix (quarantine)

Hosts below failed live-link checks on the date shown. Quarantined hosts never ship as
live entries, and no entry is added from them without a passing recheck.

| Host | Reason | Checked | Recheck condition |
|------|--------|---------|-------------------|
| sunnyday.mit.edu (and handbook mirrors) | connection timeouts | 2026-09-17 | PSAS announces a new host; use psas.scripts.mit.edu instead |
| stamp-workshop.mit.edu, stamp-workshop.org | DNS resolution failure | 2026-09-17 | each quarterly sweep |
| www.sahra.ch | parked domain | 2026-09-17 | only if a real site returns |
| www.safetbox.de | TLS failure | 2026-09-17 | before listing; list only after a clean TLS check |
| SafetyHAT / Volpe hosts | host timeouts; Volpe landing 403 | 2026-09-17 | when Volpe restores automated access |
| safeware-eng.com (SpecTRM) | expired certificate | 2026-09-17 | after certificate renewal |
| MathWorks File Exchange STPA tool | 403 to some clients | 2026-09-17 | never ship as a live entry until automated fetch returns 2xx without ignore; browser-only access is not enough |
````

- [ ] **Step 2: Verify the verbatim ports and the casing**

```bash
cd "/c/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
sed -n '71,83p' "../awesome-mbse/CONTRIBUTING.md"
sed -n '84,88p' "../awesome-mbse/CONTRIBUTING.md"
grep -c "most recent author-published version" CONTRIBUTING.md
grep -c "semantically required" CONTRIBUTING.md
grep -c "get_file.php?name=STPA_Handbook.pdf" CONTRIBUTING.md
test -f CONTRIBUTING.md && test ! -f contributing.md && echo "uppercase-only OK"
```

Expected: the hub section 5 and section 6 bodies match the spoke sections 5 and 6 line for line (the PSAS callout is additive, after the section 6 rule); the three grep counts are 1, 2, and 1.

- [ ] **Step 3: Lint**

```bash
npx -y markdownlint-cli2 "CONTRIBUTING.md"
```

Expected: no findings. If MD024 (duplicate headings) fires on the ported headers, that indicates a copy mistake, not a lint config change.

- [ ] **Step 4: Commit**

```bash
git add CONTRIBUTING.md
git commit -m "docs: CONTRIBUTING with STPA tag vocabulary and ported hub rules"
```

---

### Task 4: CI workflows

**Files:**
- Create: `.github/workflows/link-check-pr.yml`
- Create: `.github/workflows/link-check-schedule.yml`
- Create: `.github/workflows/lint.yml`

**Interfaces:** Consumes the Task 2 `.lycheeignore` and `.markdownlint-cli2.jsonc`. Produces the three checks AC8 requires; Task 6's push is their first real run.

**Model:** flash

- [ ] **Step 1: Write `link-check-pr.yml`**

Create `.github/workflows/link-check-pr.yml` with exactly:

```yaml
name: link-check (PR)

# Gate on contributions: a dead new link or bad anchor fails the PR, and pushes
# to main are gated too. Ported from the awesome-mbse hub workflow, hardened:
# every action ref is pinned to a full commit SHA, and --max-retries added for
# MIT host flakiness (spec risks).

on:
  pull_request:
    paths:
      - "README.md"
      - ".lycheeignore"
      - ".github/workflows/link-check-pr.yml"
  push:
    branches: [main]

concurrency:
  group: link-check-${{ github.ref }}
  cancel-in-progress: true

permissions:
  contents: read

jobs:
  lychee:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4
      - name: Check links and in-doc anchors
        uses: lycheeverse/lychee-action@e7477775783ea5526144ba13e8db5eec57747ce8 # master w/ nested-tarball install fix (>v2.8.0)
        with:
          # --include-fragments=anchor-only validates the hand-maintained ToC
          # against the section headings. The token lets github.com links be
          # checked authenticated instead of against the anonymous rate limit.
          lycheeVersion: v0.24.2
          args: >-
            --include-fragments=anchor-only
            --max-retries 3
            --max-concurrency 4
            --accept 200..=299,429
            --no-progress
            README.md
          fail: true
          token: ${{ secrets.GITHUB_TOKEN }}
```

- [ ] **Step 2: Write `link-check-schedule.yml`**

Create `.github/workflows/link-check-schedule.yml` with exactly:

```yaml
name: link-check (weekly)

# Freshness engine: every week, find rotted links and keep exactly ONE open
# tracking issue. Cron only per spec; it reports, it never blocks. Ported from
# the awesome-mbse hub (labels link-rot, title "Weekly link-rot report").

on:
  schedule:
    - cron: "0 6 * * 1" # Mondays 06:00 UTC

permissions:
  contents: read
  issues: write # required for the close + create steps below

jobs:
  link-rot:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4

      - name: Check links (report only, never fail)
        uses: lycheeverse/lychee-action@e7477775783ea5526144ba13e8db5eec57747ce8 # master w/ nested-tarball install fix (>v2.8.0)
        with:
          lycheeVersion: v0.24.2
          args: >-
            --include-fragments=anchor-only
            --max-retries 3
            --max-concurrency 4
            --accept 200..=299,429
            --no-progress
            README.md
          fail: false
          output: ./lychee/out.md
          token: ${{ secrets.GITHUB_TOKEN }}

      # Stock create-issue-from-file does NOT dedupe/update, so a single open
      # report is enforced: close the previous link-rot issue, then create the
      # fresh one. gh needs GH_TOKEN explicitly.
      - name: Close previous link-rot report
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          for n in $(gh issue list --label link-rot --state open --json number --jq '.[].number'); do
            gh issue close "$n" --comment "Superseded by this week's link-rot report."
          done

      - name: Open this week's link-rot report
        uses: peter-evans/create-issue-from-file@e8ef132d6df98ed982188e460ebb3b5d4ef3a9cd # v5
        with:
          title: "Weekly link-rot report"
          content-filepath: ./lychee/out.md
          labels: link-rot
```

- [ ] **Step 3: Write `lint.yml`**

Create `.github/workflows/lint.yml` with exactly:

```yaml
name: Lint
# awesome-lint + markdownlint. Action refs are pinned to full-length commit
# SHAs (supply-chain hardening). To bump an action, resolve its tag to a
# commit SHA, e.g.:
#   curl -s https://api.github.com/repos/<owner>/<repo>/commits/<tag>
# Use the "sha" field (the commit, not a tag object SHA), then update the
# version comment to match.

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
      - name: awesome-lint
        run: npx -y awesome-lint
      - name: markdownlint
        uses: DavidAnson/markdownlint-cli2-action@21c1be1b93ad9ed58fa840aacc3f279cde2a72ff # v24
        with:
          globs: |
            README.md
            CONTRIBUTING.md
```

- [ ] **Step 4: Verify pins and triggers**

```bash
cd "/c/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
grep -rn "uses: .*@v" .github/workflows/ ; echo "exit=$?"
grep -c "@[0-9a-f]\{40\}" .github/workflows/link-check-pr.yml .github/workflows/link-check-schedule.yml .github/workflows/lint.yml
grep -n "pull_request\|push" .github/workflows/link-check-schedule.yml ; echo "exit=$?"
grep -n "cron" .github/workflows/link-check-schedule.yml
grep -n "fail: true" .github/workflows/link-check-pr.yml
grep -n "labels: link-rot" .github/workflows/link-check-schedule.yml
```

Expected: no floating `uses: ...@vN` refs (first grep exits 1); SHA counts 2, 3, 3; no pull_request or push trigger in the schedule workflow; cron Mondays 06:00 UTC; `fail: true`; `link-rot` label present.

- [ ] **Step 5: Commit**

```bash
git add .github/workflows
git commit -m "ci: blocking link check, weekly link-rot report, lint (all actions SHA-pinned)"
```

---

### Task 5: README with the entry set

**Files:**
- Create: `README.md`

**Interfaces:** Consumes the Task 3 vocabulary and section numbering. Produces the entry corpus every CI check and the acceptance criteria measure.

**Model:** standard

The full entry set is 43 lines: 8 foundations, 15 tools, 2 standards, 5 cases, 4 learning, 6 datasets, 3 related lists. That clears the 40 floor with a 3-entry buffer. Soft section targets from the spec are not hard quotas; Learning ships 4 seed rows against a soft band of 6–8 (buffer lives in other sections). Every `(YYYY)` is resolved in Step 3 from primary pages or repo metadata; worked-example years in the spec are illustrative only and must be reconfirmed, not copied blindly.

- [ ] **Step 1: Write the README chrome, ToC, section intros, and all 43 entry lines**

Create `README.md` with exactly:

```markdown
# Awesome STPA [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated, dated index of STAMP/STPA, CAST, and hazard-analysis resources:
> handbooks, tools, standards context, case studies, and datasets, for safety and
> systems engineering practitioners.

![Last full sweep: 2026-09](https://img.shields.io/badge/last%20full%20sweep-2026--09-brightgreen)

Part of the awesome-mbse list family (hub repository currently private).

Maintained by [JG Systems Consulting Ltd.](https://github.com/jgsystemsconsulting).
See [Editorial neutrality](CONTRIBUTING.md#7-editorial-neutrality).

## Contents

- [Foundations & Handbooks](#foundations--handbooks)
- [Tools](#tools)
- [Standards & Guidance](#standards--guidance)
- [Case Studies & Agency Reports](#case-studies--agency-reports)
- [Learning & Workshops](#learning--workshops)
- [Datasets & Examples](#datasets--examples)
- [Related lists](#related-lists)

## Foundations & Handbooks

Start here: the free STPA and CAST handbooks, Leveson's books, and the MIT PSAS
indexes that track the STAMP ecosystem.

- [STPA Handbook](https://psas.scripts.mit.edu/home/get_file.php?name=STPA_Handbook.pdf) - Free process handbook for System-Theoretic Process Analysis by Leveson and Thomas `STPA` `handbook` (2018).
- [CAST Handbook](https://psas.scripts.mit.edu/home/get_file4.php?name=CAST_Handbook.pdf) - Free handbook for CAST, the STAMP-based accident analysis method `CAST` `handbook` (YYYY).
- [Engineering a Safer World](https://direct.mit.edu/books/oa-monograph/2908/Engineering-a-Safer-WorldSystems-Thinking-Applied) - Leveson's open-access foundations of STAMP systems thinking `STAMP-general` `book` (2011).
- [Introduction to System Safety Engineering](https://mitpress.mit.edu/9780262546881/) - Leveson's textbook on system safety engineering and management `STAMP-general` `book` (YYYY).
- [MIT PSAS home](https://psas.scripts.mit.edu/home/) - MIT host for STAMP handbooks, the tools catalog, workshops, and publications `STAMP-general` `list` (YYYY).
- [Books and handbooks index](https://psas.scripts.mit.edu/home/books-and-handbooks/) - PSAS index of STAMP books and handbooks, free and commercial `STAMP-general` `list` (YYYY).
- [Materials index](https://psas.scripts.mit.edu/home/materials/) - PSAS index of STAMP/STPA learning materials and references `STAMP-general` `list` (YYYY).
- [Publications search](https://psas.scripts.mit.edu/home/publications/) - PSAS publications index covering STAMP research literature `STAMP-general` `list` (YYYY).

## Tools

Open source first, then commercial. The PSAS stamp-tools catalog is an awareness
list, not an endorsement. Commercial entries clear the same bar as everything else:
documentation with substance, not pure vendor marketing (see
[Editorial neutrality](CONTRIBUTING.md#7-editorial-neutrality)).

- [XSTAMPP](https://github.com/SE-Stuttgart/XSTAMPP) - Open-source Eclipse-based STAMP platform supporting STPA and CAST analyses `STPA` `XSTAMPP` `tool` (2024).
- [MicroSTAMP](https://github.com/Micro-STAMP/microstamp) - Open-source toolchain for STPA of microservice architectures `STPA` `MicroSTAMP` `tool` (YYYY).
- [PASTA for VS Code](https://marketplace.visualstudio.com/items?itemName=kieler.pasta) - VS Code extension providing an STPA DSL and analysis tooling from the KIELER project `STPA` `PASTA` `tool` (YYYY).
- [PASTA source](https://github.com/kieler/pasta) - Source repository for PASTA, the KIELER STPA modeling and analysis tool `STPA` `PASTA` `tool` (YYYY).
- [stpa-capella](https://github.com/labs4capella/stpa-capella) - Capella add-on bringing STPA viewpoints and analyses into Eclipse Capella models `STPA` `stpa-capella` `tool` (YYYY).
- [CAIRIS](https://github.com/cairis-platform/cairis) - Open-source platform for engineering secure and usable systems, with STPA support `STPA-Sec` `CAIRIS` `tool` (YYYY).
- [CAIRIS STPA documentation](https://cairis.readthedocs.io/en/latest/stpa.html) - CAIRIS guide to building STPA models: losses, hazards, constraints, control structures `STPA` `CAIRIS` `handbook` (YYYY).
- [STPA Safety-based Testing Plugin](https://github.com/SE-Stuttgart/STPA-Safety-based-Testing-Plugin) - Plugin deriving safety tests from STPA analysis results `STPA` `other-tool` `tool` (YYYY).
- [STAMP Workbench (IPA)](https://www.ipa.go.jp/en/digital/complex_systems/stamp_workbench.html) - Japan IPA workbench for applying STPA to complex-system safety analysis `STPA` `other-tool` `tool` (YYYY).
- [PSAS stamp-tools catalog](https://psas.scripts.mit.edu/home/stamp-tools/) - Catalog of STAMP and STPA tools across the ecosystem, maintained by MIT PSAS `STAMP-general` `list` (YYYY).
- [TRACEIT](https://en.vwaycorp.com/traceit) - Commercial STPA and requirements-management tooling from VWAY `STPA` `other-tool` `tool` `paid` (YYYY).
- [VisualPro SA](https://en.vwaycorp.com/visualpro) - Commercial safety-analysis tool covering STPA and FHA workflows `STPA` `other-tool` `tool` `paid` (YYYY).
- [RM Studio STPA](https://www.riskmanagementstudio.com/stpa-software-solution/) - Commercial STPA module of the RM Studio risk-management platform `STPA` `other-tool` `tool` `paid` (YYYY).
- [STPAmaster](https://stpamaster.com/) - Commercial tool for building STPA control structures and analyzing scenarios `STPA` `other-tool` `tool` `paid` (YYYY).
- [Depict](https://depict.systems) - Commercial web tool for drawing and analyzing STPA control structures `STPA` `other-tool` `tool` `paid` (YYYY).

## Standards & Guidance

Functional-safety assessment standards and guidance: industry contexts where STPA is
used or discussed. This list does not claim any of them mandates STPA.

- [ISO 26262](https://www.iso.org/standard/68383.html) - ISO catalog page for road vehicles functional safety; the text is paywalled, the catalog page is free `STAMP-general` `standard` `ISO-26262` (YYYY).
- [SAE ARP4761A](https://www.sae.org/standards/content/arp4761a/) - SAE catalog page for the aerospace safety assessment guideline `STAMP-general` `standard` `ARP4761A` (YYYY).

## Case Studies & Agency Reports

Applied STPA and CAST: regulator evaluations and workshop case studies.

- [FAA STPA aviation-safety evaluation](https://rosap.ntl.bts.gov/view/dot/78914/dot_78914_DS1.pdf) - FAA evaluation applying STPA to aviation safety, hosted on ROSAP `STPA` `case` (YYYY).
- [Adopting STPA within the FAA: an eVTOL test case](https://psas.scripts.mit.edu/home/wp-content/uploads/2026/2026-03-24-1340__Adopting_STPA_Within_the_FAA__an_eVTOL_Test_C__PUB.pdf) - FAA eVTOL STPA test case presented at the MIT STAMP workshop `STPA` `case` (2026).
- [Network Rail STPA for resilient systems](PRESENTATION_URL_NetworkRail) - STPA applied to Network Rail resilient systems, MIT STAMP workshop presentation `STPA` `case` (YYYY).
- [Healthcare CAST adverse-event case](PRESENTATION_URL_HealthcareCAST) - CAST analysis of a healthcare adverse event, MIT STAMP workshop presentation `CAST` `case` (YYYY).
- [MIT STAMP workshop presentations archive](https://psas.scripts.mit.edu/home/mit-stamp-workshop-presentations/) - Archive of yearly MIT STAMP workshop presentations `STAMP-general` `workshop` (YYYY).

## Learning & Workshops

Courses, tutorials, and the yearly MIT STAMP workshop.

- [MIT STAMP workshop tutorials](https://psas.scripts.mit.edu/home/mit-stamp-workshop-tutorials/) - Tutorial program of the yearly MIT STAMP workshop `STAMP-general` `workshop` (YYYY).
- [STAMP workshop information](https://psas.scripts.mit.edu/home/stamp-workshop-information/) - Current-year MIT STAMP workshop dates, venue, and registration `STAMP-general` `workshop` (YYYY).
- [PSAS online education](https://psas.scripts.mit.edu/home/online-education/) - Free online STAMP/STPA education material from MIT PSAS `STAMP-general` `course` (YYYY).
- [STAMP Institute training](https://classes.stamp-institute.com/p/home) - Commercial STPA/STAMP training catalog from the STAMP Institute `STAMP-general` `course` `paid` (YYYY).

## Datasets & Examples

Downloadable STPA artifacts, worked examples, and adjacent modeling tools.

- [train-gate STPA control example](https://github.com/adityajeppu/train-gate-STPA-control) - Worked STPA control-structure example on a train-gate system `STPA` `dataset` (YYYY).
- [stpa-step1-dataset](https://github.com/andreyokamura-unicamp/stpa-step1-dataset) - Dataset of STPA step-one artifacts: losses, hazards, constraints `STPA` `dataset` (YYYY).
- [triarchsecurity/stpa](https://github.com/triarchsecurity/stpa) - STPA applied to security threat modeling `STPA-Sec` `dataset` (YYYY).
- [anvil-safety-framework](https://github.com/Dr-AneeshJoseph/anvil-safety-framework) - Safety-analysis framework package including STPA support `STPA` `dataset` (YYYY).
- [ease-2026 replication package](https://github.com/LLM-Mutation/ease-2026-replication-package) - Replication package for an LLM-mutation STPA study (EASE 2026) `STPA` `dataset` (2026).
- [Gaphor](https://github.com/gaphor/gaphor) - Lightweight open-source modeling tool with RAAML templates, STPA-adjacent safety modeling support `STAMP-general` `other-tool` `tool` (YYYY).

## Related lists

Family lists and the awesome meta-index. The hub link resolves for org members while
the hub repository is private.

- [awesome-mbse](https://github.com/jgsystemsconsulting/awesome-mbse) - Hub of this list family: methods, tools, and openable models across MBSE `STAMP-general` `list` (YYYY).
- [awesome-sysml-v2](https://github.com/jgsystemsconsulting/awesome-sysml-v2) - Sibling family list for SysML v2: spec, tools, models `STAMP-general` `list` (YYYY).
- [sindresorhus/awesome](https://github.com/sindresorhus/awesome) - The meta-list of high-quality awesome lists `STAMP-general` `list` (YYYY).

---

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the maintainers have waived all copyright and related
or neighboring rights to this work. Released under CC0 1.0 Universal; see [LICENSE](LICENSE).
```

- [ ] **Step 2: Resolve the two presentation URLs**

Open https://psas.scripts.mit.edu/home/mit-stamp-workshop-presentations/ in a browser. Locate the Network Rail resilient-systems presentation PDF and the healthcare CAST adverse-event presentation PDF. Replace `PRESENTATION_URL_NetworkRail` and `PRESENTATION_URL_HealthcareCAST` with the exact URLs. If either talk has no stable individually linkable PDF, delete that entry; the set stays at 42 or 41, still above 40 (AC7 buffer).

- [ ] **Step 3: Resolve every remaining `(YYYY)` by resource class**

| Class | Entries | Year rule (CONTRIBUTING section 5) | How to resolve |
|-------|---------|------------------------------------|----------------|
| Primary document / named case | STPA Handbook, Engineering a Safer World, CAST Handbook, eVTOL case PDF, ease-2026 package | Publication or event year on the primary | Confirm PDF cover, book front matter, or package year; starter values 2018/2011/2026 are only hints |
| GitHub repo | XSTAMPP, MicroSTAMP, PASTA source, stpa-capella, CAIRIS, testing plugin, train-gate, stpa-step1-dataset, triarchsecurity, anvil, Gaphor, awesome-mbse, awesome-sysml-v2, sindresorhus/awesome | Latest tagged release year, else latest default-branch commit year | `gh api repos/OWNER/REPO/releases/latest --jq .published_at`; if 404, `gh api repos/OWNER/REPO/commits/HEAD --jq .commit.committer.date`; take the YYYY |
| PSAS PDF | CAST Handbook | Publication year on the cover or title page | Open the PDF, read the cover |
| Catalog page | Introduction to System Safety Engineering, ISO 26262, ARP4761A | Edition year shown on the page | Read the page |
| Living web page or index | PSAS home, the three PSAS indexes, stamp-tools, workshop archive, tutorials, workshop info, online education, STAMP Institute, TRACEIT, VisualPro, RM Studio, STPAmaster, Depict | Year of the site's current author-published state | Prefer explicit program/edition year on the page; else footer copyright year; else the ship-year YYYY-MM of this release |

Replace every `(YYYY)` with the resolved year. Do not guess: every replacement traces to one of the sources above.

- [ ] **Step 4: Run the format gate**

```bash
cd "/c/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
grep -c '^- \[' README.md
grep -n '(YYYY)' README.md ; echo "exit=$?"
grep -n 'PRESENTATION_URL' README.md ; echo "exit=$?"
python - <<'EOF'
import re
LANG={'STPA','CAST','STPA-Sec','STAMP-general'}
TYPE={'handbook','book','paper','standard','tool','course','video','case','dataset','workshop','list'}
TOOL={'XSTAMPP','PASTA','stpa-capella','MicroSTAMP','CAIRIS','other-tool'}
STD={'ISO-26262','ARP4761A','IEC-61508','J3187','AIR6913'}
METHOD={'HARA','FTA','FMEA','HazOp'}
def axis(t):
    if t in LANG: return 0
    if t in METHOD: return 1
    if t in TOOL: return 2
    if t=='has-model': return 3
    if t in TYPE: return 4
    if t in STD: return 5
    if t=='paid': return 6
    raise SystemExit(f'unknown tag {t!r}')
n=0
for line in open('README.md',encoding='utf-8'):
    line=line.rstrip('\n')
    if not line.startswith('- ['): continue
    n+=1
    m=re.match(r'^- \[([^]]+)\]\((https?://[^)]+)\) - (.*)$',line)
    assert m, f'bad line: {line}'
    rest=m.group(3)
    # year is OUTSIDE backticks per FAMILY: ... `tags` (YYYY).
    ym=re.search(r'\((\d{4})\)\.\s*$', rest)
    assert ym, f'year not terminal (YYYY).: {line}'
    body=rest[:ym.start()].rstrip()
    i=body.index('`')
    assert len(body[:i].strip())<=140, f'description over 140: {line[:60]}'
    tags=re.findall(r'`([^`]+)`', body)
    assert tags, f'no tags: {line}'
    assert not any(re.fullmatch(r'\(\d{4}\)', t) for t in tags), f'year must not be a backtick tag: {line}'
    idx=[axis(t) for t in tags]
    assert idx==sorted(idx), f'tag order: {line}'
    assert idx.count(0)==1, f'language cardinality: {line}'
    assert idx.count(1)<=1, f'method cardinality: {line}'
    assert idx.count(4)==1, f'type cardinality: {line}'
    assert idx.count(5)<=1, f'spec cardinality: {line}'
    assert idx.count(6)<=1, f'paid cardinality: {line}'
    if 3 in idx:
        assert any(i==2 for i in idx), f'has-model requires tool tag: {line}'
print(f'{n} entries OK')
assert n>=40, f'only {n} entries'
EOF
```

Expected: count is 41 to 43 (43 if both presentations resolved); no `(YYYY)` matches; no `PRESENTATION_URL` matches; the python check prints `N entries OK`.

- [ ] **Step 5: Lint locally**

```bash
npx -y awesome-lint
npx -y markdownlint-cli2 "README.md" "CONTRIBUTING.md"
```

Expected: clean. awesome-lint needs the git remote set (Task 1 did that). If awesome-lint errors on something structural (H1, badge), fix the chrome, not the linter.

- [ ] **Step 6: Link check locally (Docker)**

```bash
docker run --rm -v "$PWD:/d" -w /d lycheeverse/lychee --include-fragments=anchor-only --max-retries 3 --accept 200..=299,429 --no-progress README.md
```

Expected: no failures except (predictably) the private hub URL `https://github.com/jgsystemsconsulting/awesome-mbse`, which 404s for unauthenticated local runs. Leave it; the CI token handles org-internal links differently and Task 6 has the contingency. Any other failure: fix the URL or re-verify in a browser and apply the dated `.lycheeignore` policy (the only sanctioned ignore).

- [ ] **Step 7: Commit**

```bash
git add README.md
git commit -m "feat: initial entry set, seven sections per family standard"
```

- [ ] **Step 7b (optional, only if verified): SAE J3187 and AIR6913 entries**

Search https://www.sae.org for the J3187 and AIR6913 catalog pages. Only if a live catalog URL verifies in a browser, add one line each to Standards & Guidance in the established format, with spec/standard tags `J3187` and `AIR6913` and no `paid` tag (free catalog page). Do not invent URLs; if the search does not produce live pages, skip this step. These are not needed for the 40 floor. If this step adds lines, amend or add a README commit before Task 6 so the four-then-five commit count still holds (README complete before CHANGELOG).

---

### Task 6: CHANGELOG, first push, CI green

**Files:**
- Create: `CHANGELOG.md`
- Modify: `.lycheeignore` (only on the private-hub contingency)

**Interfaces:** Consumes Tasks 2 to 5. Produces the green-on-main state AC9 and AC13 require; Task 7 starts only after this task ends green.

**Model:** standard

- [ ] **Step 1: Write CHANGELOG.md**

Create `CHANGELOG.md` with exactly (replace `N` with the real shipped count from the Task 5 gate, and the dates with the real push dates):

```markdown
# Changelog

Maintenance sweeps and notable changes. The "Last full sweep" badge in the README
tracks the most recent dated entry here.

## 2026-09 - Initial release

- **Shipped v1**: seven sections, N entries (PSAS foundations, open-source tools
  first then commercial, standards context, agency and workshop cases, learning,
  datasets, family related lists), all in family entry format (tags plus year).
- **CI live**: blocking link check on PRs and pushes to main (lychee, anchor-only
  fragments, retries, 429 accepted), weekly link-rot report issue, awesome-lint plus
  markdownlint on README and CONTRIBUTING. All action refs pinned to full commit SHAs.
- **Family standard**: CC0-1.0, CONTRIBUTING.md with the hub year and canonical-URL
  rules ported verbatim (PSAS query strings called out as semantically required), STPA
  tag vocabulary in fixed axis order, known-rot appendix, editorial neutrality. Repo
  created private per FAMILY Private mode.
```

The `2026-09` heading and the README badge month must match (AC14). If the push slips to a later month, change both to the real month.

- [ ] **Step 2: Final pre-push greps**

```bash
cd "/c/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
grep -nEi 'sunnyday\.mit\.edu|stamp-workshop\.(mit\.edu|org)|sahra\.ch|safetbox\.de|safeware-eng\.com|volpe|mathworks' README.md ; echo "exit=$?"
git log --oneline
```

Expected: no quarantined host in the README; four commits so far (skeleton, CONTRIBUTING, workflows, README). CHANGELOG is the fifth commit in the next step.

- [ ] **Step 3: Write CHANGELOG commit and push**

```bash
git add CHANGELOG.md
git commit -m "docs: changelog initial release"
git log --oneline | head -5
git push -u origin main
```

Expected after commit: five commits (skeleton, CONTRIBUTING, workflows, README, CHANGELOG).

- [ ] **Step 4: Watch the first CI run (both push workflows)**

```bash
SHA="$(git rev-parse HEAD)"
gh run list --repo jgsystemsconsulting/awesome-stpa --limit 10
# Wait until BOTH push-triggered jobs are green (names match workflow `name:` fields).
# Pipe JSON to jq; gh --jq does not accept jq --arg flags.
for name in "link-check (PR)" "Lint"; do
  rid=$(gh run list --repo jgsystemsconsulting/awesome-stpa --event push --limit 20 \
    --json databaseId,name,status,conclusion,headSha \
    | jq -r --arg n "$name" --arg sha "$SHA" \
      '.[] | select(.name==$n and .headSha==$sha) | .databaseId' | head -1)
  test -n "$rid" || { echo "missing run for $name on $SHA"; exit 1; }
  gh run watch --repo jgsystemsconsulting/awesome-stpa "$rid" --exit-status
done
gh label create link-rot --repo jgsystemsconsulting/awesome-stpa --color D93F0B --description "Weekly lychee link-rot report" 2>/dev/null || true
```

Expected: the push event triggers `link-check (PR)` and `Lint`; both succeed on the HEAD sha. The weekly workflow does not run on push (AC9 does not require it). `link-rot` label exists for future schedule runs.

- [ ] **Step 5: Private-hub contingency (expected path for the hub URL while hub is private)**

Unauthenticated and spoke-scoped tokens typically 404 the private hub. If lychee fails only on `https://github.com/jgsystemsconsulting/awesome-mbse`, append to `.lycheeignore`, replacing the date with the real verification date:

```text
# Hub repo is private: lychee authenticated as this repo's GITHUB_TOKEN gets a 404.
# Browser-verified live by an org member on YYYY-MM-DD. Remove when the hub goes public.
https://github\.com/jgsystemsconsulting/awesome-mbse
```

Then:

```bash
git add .lycheeignore
git commit -m "chore: lycheeignore entry for private hub link"
git push
```

Re-run the watch command; expected green. Any other failure: fix the URL, or browser-verify and apply the dated ignore policy, then re-push.

---

### Task 7: Hub go-live edits (awesome-mbse)

**Files:**
- Modify: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-mbse\FAMILY.md`
- Modify: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-mbse\README.md`

**Interfaces:** Consumes Task 1's namespace recheck date and result, and Task 6's green CI. Produces the AC13 hub state. Nothing in the spoke depends on this task.

**Model:** flash

- [ ] **Step 0: Sequencing guard**

```bash
gh run list --repo jgsystemsconsulting/awesome-stpa --limit 3
```

Expected: the latest push-triggered `link-check (PR)` and `Lint` runs are `completed/success`. Do not start until they are (spec: hub edits last; AC13).

- [ ] **Step 1: FAMILY.md registry row (line 55)**

Replace:

```markdown
| awesome-stpa | STAMP / STPA and hazard analysis; functional safety methods | Planned | none yet |
```

with:

```markdown
| [awesome-stpa](https://github.com/jgsystemsconsulting/awesome-stpa) | STAMP / STPA and hazard analysis; functional safety methods | Live | private |
```

Use `public` in the Visibility cell only if the maintainer explicitly releases the repo the same day (AC1 records the choice).

- [ ] **Step 2: FAMILY.md namespace table row (line 100)**

Replace:

```markdown
| awesome-stpa | - | TODO re-check | Re-check on launch day (rate-limited on the 2026-09-17 list-family pass) |
```

with (using the real create-day date and result from Task 1):

```markdown
| awesome-stpa | YYYY-MM-DD | empty | Namespace clear; repo created the same day |
```

- [ ] **Step 3: FAMILY.md awesome-stpa checklist (lines 198-207)**

Replace the section intro `Planned. Hub carries one STPA entry: the Model Gallery DLR-FT STPA library. Namespace TODO re-check (rate-limited on the 2026-09-17 list-family pass).` with:

```markdown
Live. Hub keeps the cross-cutting Model Gallery DLR-FT STPA library entry; the niche
spoke carries the deep list. Namespace re-checked empty on YYYY-MM-DD (real date from
Task 1); repo created private the same day.
```

Tick all five checkboxes, filling the real date on the first:

```markdown
- [x] Namespace re-checked on YYYY-MM-DD (result: empty)
- [x] Roughly 40 candidate entries gathered, all passing the inclusion bar
- [x] Repo created (private) from the README skeleton
- [x] Hub README family table row updated with the URL
- [x] Registry status flipped to Live
```

- [ ] **Step 4: Hub README family table (awesome-stpa row)**

Confirm at execute that the awesome-sysml-v2 and awesome-digital-engineering rows already say `Linked public spoke` (no "only live spoke" claim). Do not edit those rows unless HEAD still carries obsolete "only live spoke" text.

awesome-stpa row, replace:

```markdown
| awesome-stpa | STAMP / STPA and hazard analysis; functional safety methods | Planned | Model Gallery DLR-FT STPA library (one entry, thin) |
```

with:

```markdown
| [awesome-stpa](https://github.com/jgsystemsconsulting/awesome-stpa) | STAMP / STPA and hazard analysis; functional safety methods | Live | Dedicated private spoke; hub keeps the DLR-FT STPA library as its one cross-cutting entry |
```

- [ ] **Step 5: Hub README gaps snapshot and re-check paragraph**

In the gaps paragraph (line 36), update the snapshot date to the edit date, and replace the clause `STPA is one entry (the DLR-FT STPA library);` with `STPA has a dedicated spoke (the hub keeps one cross-cutting entry, the DLR-FT STPA library);`.

In the namespace re-check paragraph (line 264), replace:

```markdown
TODO: re-check the `awesome-capella` and `awesome-stpa` namespaces on launch day (both
were rate-limited on the 2026-09-17 list-family pass).
```

with:

```markdown
TODO: re-check the `awesome-capella` namespace on launch day (rate-limited on the
2026-09-17 list-family pass).
```

Leave the second sentence of that paragraph (archimate, requirements-engineering, digital-engineering) unchanged.

- [ ] **Step 6: Verify hub scope and commit**

```bash
cd "/c/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
git diff --stat
grep -n "awesome-stpa" FAMILY.md README.md
grep -nE "^#+ .*STPA" README.md ; echo "exit=$?"
```

Expected: the diff touches only FAMILY.md and README.md; the grep shows the registry row, namespace row, checklist section, family-table row, gaps sentence, and the re-check paragraph, nothing else; no STPA heading was added to the hub README (exit 1, AC13's no-duplicated-section rule). The scope-boundary row is untouched by design.

```bash
git add FAMILY.md README.md
git commit -m "feat(family): awesome-stpa spoke live (private)"
git push
```

---

### Task 8: Acceptance pass (AC1-14)

**Files:** none modified (verification only). Fix-and-re-run if any row fails.

**Model:** flash

- [ ] **Step 1: Run the acceptance table**

| AC | Verify | Expected |
|----|--------|----------|
| AC1 repo, private, main, v1 files | `gh repo view jgsystemsconsulting/awesome-stpa --json visibility,defaultBranchRef` and path checks: `for p in README.md LICENSE CONTRIBUTING.md CODE_OF_CONDUCT.md SECURITY.md CHANGELOG.md NOTICE .gitignore .lycheeignore .markdownlint-cli2.jsonc .github/PULL_REQUEST_TEMPLATE.md .github/workflows/link-check-pr.yml .github/workflows/link-check-schedule.yml .github/workflows/lint.yml; do gh api "repos/jgsystemsconsulting/awesome-stpa/contents/$p" --jq .path; done` | PRIVATE, main; each of the 14 paths returns |
| AC2 CONTRIBUTING content | `grep -c "most recent author-published version" CONTRIBUTING.md; grep -c "semantically required" CONTRIBUTING.md; grep -c "get_file.php?name=STPA_Handbook.pdf" CONTRIBUTING.md; grep -c "Known-rot appendix" CONTRIBUTING.md` | 1, 2, 1, 1; uppercase filename; vocabulary table with cardinalities in axis order |
| AC3 CC0, no MIT *license* text | `grep -c "CC0 1.0 Universal" LICENSE` and `grep -rniE "MIT License|license: MIT|SPDX-License-Identifier: MIT" . --exclude-dir=.git` | LICENSE count ≥1; no MIT license metadata. Nominative MIT (PSAS, MIT Press, workshops) in README/CONTRIBUTING/NOTICE is allowed |
| AC2 extras | `grep -c "Inclusion bar" CONTRIBUTING.md; grep -c "Editorial neutrality" CONTRIBUTING.md; grep -c "STAMP-general" CONTRIBUTING.md` | each ≥1 |
| AC4 README chrome | `head -8 README.md` and `grep -n "FAMILY.md" README.md` | badge, scope, sweep badge, text-only pointer, maintainer line; no FAMILY.md hyperlink |
| AC5 seven sections, flat ToC | `grep -c "^## " README.md` and `sed -n '/## Contents/,/## Foundations/p' README.md` | 8 headings (Contents plus seven); ToC lists exactly the seven content sections |
| AC6 entry format | Task 5 Step 4 python gate | `N entries OK` with N at least 40 |
| AC7 live links, ignore policy | `gh run list` link-check green; `grep -v "^#" .lycheeignore` | every failing-but-live URL listed with a dated comment; quarantined hosts never listed |
| AC8 CI shapes | Task 4 Step 4 greps | SHA pins only; cron-only weekly; `link-rot` label; lint globs README.md and CONTRIBUTING.md |
| AC9 first push green | `gh run list --repo jgsystemsconsulting/awesome-stpa` | `link-check (PR)` and `Lint` success on the push event |
| AC10 no mandate claims | `grep -nEi "mandat" README.md` | only the Standards intro negation sentence; no entry claims a standard mandates STPA |
| AC11 no rehost | review: every URL points at the canonical source (PSAS PDFs are author-published) | no hosted copies |
| AC12 quarantine clean | `grep -nEi 'sunnyday|stamp-workshop\.(mit\.edu|org)|sahra\.ch|safetbox|safeware-eng|volpe|mathworks' README.md` | no output |
| AC13 hub state | Task 7 Step 6 greps plus `git -C ../awesome-mbse log --oneline -1` | registry Live with visibility; hub family table names every Live spoke (sysml-v2, digital-engineering, and stpa at minimum); no hub STPA section |
| AC14 CHANGELOG and badge agree | `grep -n "full sweep" README.md` and `head -8 CHANGELOG.md` | same YYYY-MM |

- [ ] **Step 2: Record and close**

Tick every row. If the maintainer released the spoke public the same day, confirm the FAMILY Visibility cell says `public`, else `private`. Report the AC table result to the parent; the parent owns the exit gate and step 4 review.

---

## Self-review record

- Spec coverage: AC1-14 map one-to-one onto Tasks 1-8 (table in Task 8); the deferred list (CITATION.cff, docs site, stale.yml, issue forms, awesome submission) and the non-goals (ArchiMate, mandate claims, rehosting) are enforced as Global Constraints and verified in AC3, AC10, AC11.
- Placeholder scan: `(YYYY)` and `YYYY-MM-DD` tokens are parameterized values with written resolution rules (Task 5 Step 3, Task 7 dates from Task 1) and hard verification gates that fail while they remain; they are not open content. `PRESENTATION_URL_*` resolves in a dedicated step with a defined fallback (delete the entry; floor stays met).
- Consistency: tag vocabulary, axis order, section names, anchors, workflow titles, labels, and SHAs are identical across Tasks 2 to 8; the Task 8 table reuses the exact grep commands defined in earlier steps.
