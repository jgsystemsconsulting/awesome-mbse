# awesome-digital-engineering spoke launch Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create `jgsystemsconsulting/awesome-digital-engineering` as a public sibling git repo built to the FAMILY shared standard, launched in skeleton-plus-verified-seed mode with CI green on day one, seed inventory tracked outside the repo, and the hub registry plus hub README updated.

**Architecture:** Local git skeleton at `C:\Users\gower\OneDrive\Documents\GitHub\awesome-digital-engineering` (12 template files copied/adapted from the hub repo), then a README populated only with URLs that pass a live verification gate recorded in a seed inventory outside the spoke, then GitHub repo creation via `gh`, CI proof on a launch PR (lychee + awesome-lint, hub filenames), remaining inventory rows converted to `seed-inventory` issues, and hub integration (FAMILY.md row to Live, hub README spoke link).

**Tech Stack:** git, GitHub CLI (`gh`, authenticated as `jgsystemsconsulting`), GitHub Actions (lychee v0.24.2 via lychee-action, awesome-lint on Node 20), `curl` plus web-reader fetch for URL verification, plain markdown, Python 3 for a local anchor check.

**Spec:** `C:\Users\gower\OneDrive\Documents\GitHub\awesome-mbse\docs\superpowers\specs\2026-09-17-awesome-digital-engineering.md` (the plan argues from the spec; executors read both)

## Global Constraints

Every task implicitly includes these. Values are copied verbatim from the spec.

- Repo: `jgsystemsconsulting/awesome-digital-engineering`, public, default branch `main`, its own git root. Local clone: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-digital-engineering` (sibling of the hub clone, never a hub subdirectory).
- Exactly 13 files at launch (spec File inventory): `README.md`, `CONTRIBUTING.md` (uppercase), `LICENSE`, `NOTICE`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `CHANGELOG.md`, `.github/workflows/link-check-pr.yml`, `.github/workflows/link-check-schedule.yml`, `.github/ISSUE_TEMPLATE/suggest-resource.yml`, `.github/PULL_REQUEST_TEMPLATE.md`, `.lycheeignore`, `.gitignore`. No other files. No CITATION.cff. `docs/` stays empty.
- Template source is the hub repo `awesome-mbse` working tree (plan-time HEAD `8d362e7`): FAMILY.md, CONTRIBUTING.md, the two CI workflows, `.lycheeignore`, templates, NOTICE. awesome-sysml-v2 is an existence proof only; never copy its layout, filenames, or entry style.
- Verified-only seed: every entry URL must return HTTP 200-299 during execute verification before it lands in the README. HTTP 429 alone is not verified. No invented URLs. Provisional/blocked hosts: `acq.osd.mil`, `media.defense.gov`, `iso.org`, `incose.org`, `ndia.org`, `sebokwiki.org`, `ntrs.nasa.gov`, plus hub-known blocks (researchgate.net, Wiley/INCOSE library). Each README hit on these hosts needs an active `.lycheeignore` pattern with a trailing `# browser-verified YYYY-MM-DD: <reason>` comment, or the entry is omitted.
- No markdownlint job in v1 (locked; hub actual is lychee + awesome-lint only).
- Launch under 40 entries is acceptable with the exact honest label: README scope block and CHANGELOG launch entry both carry the phrase "initial seed; growth in progress". Live = public repo + green CI + honest label; the FAMILY ~40 bar is explicitly overridden for this launch.
- Seed inventory lives OUTSIDE the spoke: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-mbse\docs\superpowers\seed-inventory-awesome-digital-engineering.md` (untracked workspace file; `docs/` is untracked in the hub repo, so no hub commit is caused).
- Entry format (hub verbatim): `- [Resource Name](url) - One-line factual description `tag` `tag` (YYYY).` Hyphen separator, never en/em dash. Description at most 140 characters, measured from the first non-space character after ` - ` through the character before the first tag backtick. Tags are inline code spans before the terminal period. Year `(YYYY)` is the last token.
- Tag axes and cardinality: `domain -> method -> tool -> has-model -> type -> spec/standard -> paid -> year`. `domain` is exactly 1 (values `DE-general`, `digital-thread`, `MBD`; this renames the family `language` axis, documented in CONTRIBUTING). `method` 0-1 (`MBE`, `GD&T`). `tool` 0+ (`other-tool` only in v1; graduates at 3+ entries in one PR). `has-model` 0-1, only when the primary URL is the downloadable `.step`/`.stp`/`.p21`, `.qif`, or `.jt` file; never on a tool repo homepage. `type` exactly 1 (`tutorial`, `course`, `book`, `paper`, `report`, `blog`, `video`, `tool`, `plugin`; `mcp` omitted). Standards/storefront/policy/program pages use type `report`. `spec`/`standard` 0-1 and only with type `report`/`book`/`paper` (prefer `report` for storefronts). `paid` 0-1. Year exactly 1; omit the entry if the year is unknown.
- README: Awesome badge; one-line scope; sweep badge dated `2026-09`; family pointer as an ABSOLUTE URL to `https://github.com/jgsystemsconsulting/awesome-mbse/blob/main/FAMILY.md`; maintained-by line linking JG Systems Consulting and the CONTRIBUTING neutrality section; flat hand-maintained ToC; all eight section H2s in order (Policy and strategy, Standards, Digital thread and interoperability, Model-based definition and PMI, Government and consortia programs, Open tools and reference implementations, Learning and reports, Commercial platforms). Empty sections keep the H2 plus the stub line `_No verified entries yet._`
- Section to default domain: 1 `DE-general`; 2 `digital-thread` (STEP/thread exchange) or `MBD` (Y14.41/PMI/QIF/metrology), never `DE-general`; 3 `digital-thread`; 4 `MBD` (plus method `GD&T` when primarily GD&T); 5 `DE-general` unless the page is only about one standard family; 6 `digital-thread` or `MBD` by file/tool focus, type usually `tool`; 7 `DE-general` unless topic-locked; 8 matches the product's primary claim, always `paid`. `DE-general` only when neither specialized domain fits.
- LICENSE is CC0-1.0 full legal text; NOTICE follows the hub pattern with the trademark line adapted to DE (reference standards by number and name, no endorsement implied).
- CI proof (AC6): after workflows land on `main`, a launch PR that touches list content must run `link-check (PR)` green (both jobs), and `link-check-schedule.yml` must run once via `workflow_dispatch`. A direct push alone does not satisfy AC6.
- No file in the repo re-hosts third-party content. Link, never redistribute.
- Execution host is Windows Git Bash; use quoted forward-slash paths (for example `"C:/Users/gower/OneDrive/Documents/GitHub/..."`) in bash commands.
- `gh` was authenticated as `jgsystemsconsulting` on 2026-09-17 with `repo` and `workflow` scopes; Task 4 still carries the web-UI fallback in case auth or org permission fails at execute time.
- Hub integration edits only DE-routed content; no general hub reorganization, no awesome-archimate work, no sindresorhus/awesome submission.
- New durable prose in the spoke files uses the Written Prose Standard (no em dashes in prose; verbatim hub ports stay byte-identical to the hub source).

## Known deviation (documented, needed for AC6)

The hub repo is private. The spec requires the README family pointer as an absolute URL to the hub's FAMILY.md, but that URL returns 404 to the spoke's CI (`GITHUB_TOKEN` in the spoke can only read the spoke) and to anonymous checkers, so a literal lychee run fails. Resolution: ship the absolute URL (AC3 satisfied) and carry one active `.lycheeignore` pattern for it from launch, commented as access-controlled until the family public release. This exemption is access control, not bot-blocking; remove the line when `awesome-mbse` goes public. It is called out again in Task 2 so no executor "fixes" it away.

## Codebase context

- Hub root: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-mbse`. Port sources: `FAMILY.md` (README skeleton at lines 227-249, registry at lines 44-62, per-spoke checklist at lines 187-196), `CONTRIBUTING.md` (entry format section 3, tag table section 4, year rule section 5 and canonical-URL rule section 6 to be ported verbatim), `LICENSE`, `NOTICE`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `CHANGELOG.md` (style), `.gitignore`, `.github/workflows/link-check-pr.yml`, `.github/workflows/link-check-schedule.yml`, `.github/ISSUE_TEMPLATE/suggest-resource.yml`, `.github/PULL_REQUEST_TEMPLATE.md`, `.lycheeignore` (header comment style).
- Hub files read at plan time: hub `README.md` line 33 carries the DE row in the List family table; lines 36-39 carry the gaps snapshot sentence that names digital engineering as absent. Both are edited in Task 7.
- `docs/superpowers/` in the hub workspace holds spec, research, context, and this plan; it is untracked in hub git. The seed inventory (Task 1) joins it and is never committed to either repo.
- `gh api repos/jgsystemsconsulting/awesome-digital-engineering` returned 404 on 2026-09-17; FAMILY requires the same-day namespace re-check at create time (Task 4 step 1).

---

### Task 1: Seed inventory and URL verification gate

**Files:**
- Create: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-mbse\docs\superpowers\seed-inventory-awesome-digital-engineering.md`

**Interfaces:**
- Consumes: research gate `docs/superpowers/research/2026-09-17-awesome-digital-engineering-research.md` (candidate URLs and grades).
- Produces: inventory file with one row per candidate (verdict: `verified` / `omit` / `issue`), and a final "Verified set" section listing exact README-ready entry lines (name, URL, description, tags in axis order, year, target section). Tasks 3 and 6 consume only this.

**Model:** standard

- [ ] **Step 1: Create the inventory file with the table skeleton and initial candidate rows**

Write the file with this exact table header, then one row per candidate below (rows 1-9 come straight from the research gate; never add a URL row without a source):

```markdown
# Seed inventory: awesome-digital-engineering

Working ledger for the launch. Not committed to any repo. Verdict vocabulary:
`verified` (entry ships) / `omit` (fails the bar or never verified) / `issue`
(ships as a seed-inventory issue after launch).

| # | Candidate | URL | Host class | Research grade | Verify method | HTTP result | Browser result | Inclusion bar | Section / tags / year | Verdict | Notes |
|---|-----------|-----|-----------|----------------|---------------|-------------|----------------|---------------|----------------------|---------|-------|
```

Initial candidate rows (fill columns as you verify):

1. ASME Y14.41 storefront, `https://www.asme.org/codes-standards/find-codes-standards/y14-41-digital-product-definition-data-practices`, standard host, ESTABLISHED (still must pass the live check), section 2 Standards, tags `MBD` `report` `standard` `paid`, year from the page (spec example says 2026; use what the page shows).
2. DMSC / QIF, `https://qifstandards.org/about-dmsc/`, standard host, PROVISIONAL, section 5, domain `DE-general` (page covers QIF and DMIS, two families).
3. LOTAR International, `https://lotar-international.org/`, standard host, PROVISIONAL, section 5, domain by the DE-general rule on the page content.
4. Wikipedia ISO 10303, `https://en.wikipedia.org/wiki/ISO_10303`, standard host, PROVISIONAL fallback (allowed only if no better live STEP link verifies), section 2, domain `digital-thread`.
5. DoD Digital Engineering Strategy (2018), candidate URLs from research section SOURCE-ROT (`https://www.acq.osd.mil/se/docs/2018-Digital-Engineering-Strategy.pdf`, `https://media.defense.gov/2018/Jun/15/2001931999/-1/-1/0/20180614_DIGITAL_ENGINEERING_STRATEGY_FINAL.PDF`), blocked host, PROVISIONAL, section 1, domain `DE-general`. Verify or omit; never invent a third URL. A local file hash may go in Notes but is not a README substitute.
6. NDIA digital thread / DE working group pages (`ndia.org`), blocked host, PROVISIONAL, section 5. Browser-verify or omit.
7. INCOSE DE working group pages (`incose.org`, plus `incose.onlinelibrary.wiley.com` known block), blocked host, PROVISIONAL, section 5. Browser-verify or omit.
8. SEBoK Digital Engineering article (`https://sebokwiki.org/wiki/Digital_Engineering`), blocked host, PROVISIONAL, section 7. Browser-verify or omit.
9. ISO catalog pages for STEP parts, ISO 23952 (QIF), ISO 22093 (DMIS), ISO 14721 (OAIS) on `iso.org`, blocked host, PROVISIONAL, section 2, tags `report` `standard` `paid`. Browser-verify or omit; no invented catalog IDs.

- [ ] **Step 2: Mine additional candidates with concrete searches (no URL invention)**

Run these and add rows for plausible hits; each row still needs its own verification:

```bash
# NASA NTRS public-distribution reports on "digital engineering"
curl -s "https://ntrs.nasa.gov/api/citations/search/?q=%22digital%20engineering%22&page.size=25" -o /tmp/ntrs.json
python -c "import json;d=json.load(open('/tmp/ntrs.json'));print(d.get('total',d.keys()))"
# pick 3-5 individual public-distribution records; citation URL form:
# https://ntrs.nasa.gov/citations/<recordId>  (ntrs.nasa.gov is a provisional host: verify each)

# Open-source STEP / QIF / JT tooling on GitHub
gh api -X GET "search/repositories?q=step+file+converter&per_page=10" --jq '.items[] | "\(.html_url) \(.stargazers_count) \(.pushed_at)"'
gh api -X GET "search/repositories?q=iso+10303&per_page=10"            --jq '.items[] | "\(.html_url) \(.stargazers_count) \(.pushed_at)"'
gh api -X GET "search/repositories?q=QIF+metrology&per_page=10"        --jq '.items[] | "\(.html_url) \(.stargazers_count) \(.pushed_at)"'
gh api -X GET "search/repositories?q=JT+file+format&per_page=10"       --jq '.items[] | "\(.html_url) \(.stargazers_count) \(.pushed_at)"'
```

- [ ] **Step 3: Verify every candidate URL (200-299 required)**

For each row, standard hosts first:

```bash
curl -sS -o /dev/null -w "%{http_code}" -L --max-time 30 "<URL>"
```

Rules: `200-299` marks the row **verified**. `429` alone is NOT verified: set verdict **`issue`** (viable post-launch; do not omit solely for rate limit). `403`, 5xx, TLS or DNS failures on provisional hosts move the row to the browser step: fetch the exact URL with the agent browser/web-reader tool (or a human browser if the agent cannot); if it renders the real page with a 200-class result, mark Browser result **verified** and record the reason for the `.lycheeignore` line. If browser also fails and the candidate is still on-topic and worth retry later, verdict **`issue`**; only true out-of-scope, dead, or junk candidates get **`omit`**. Record the check date (2026-09-17 or execute date) in Notes.

- [ ] **Step 4: Draft the README-ready entry line for every verified row**

Under a final heading `## Verified set`, write one block per entry: target section, then the exact line in entry format, then the tag axis check. Example shape (content comes from your verified rows; this one is the spec's own example):

```markdown
### Standards

- [ASME Y14.41](https://www.asme.org/codes-standards/find-codes-standards/y14-41-digital-product-definition-data-practices) - Digital product definition data practices for annotated model-based 3D datasets `MBD` `report` `standard` `paid` (2026).
```

Checklist per line: hyphen separator; description 140 characters or fewer measured from the first character after ` - ` to the character before the first tag backtick; tags in axis order `domain -> method -> tool -> has-model -> type -> spec/standard -> paid -> year`; exactly one `domain` and one `type`; `standard`/`spec` only with type `report`/`book`/`paper`; year last; no URL duplicated in canonical form (force https, lowercase host, strip trailing slash and non-semantic query).

- [ ] **Step 5: Close the gate**

Confirm the inventory answers three questions, and record the answers in a short `## Gate summary` section: how many rows verified, how many omitted and why, how many remain viable as post-launch issues. Ship decision is locked by the spec (launch regardless, honest under-40 label), so no stop decision is needed here; the numbers feed Tasks 3, 6, and 8.

This file is a workspace artifact: do not commit it to any repo.

---

### Task 2: Local skeleton: repo init plus 12 template files

**Files:**
- Create: git repo `C:\Users\gower\OneDrive\Documents\GitHub\awesome-digital-engineering` (branch `main`)
- Create: `CONTRIBUTING.md`, `LICENSE`, `NOTICE`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `CHANGELOG.md`, `.gitignore`, `.lycheeignore`, `.github/workflows/link-check-pr.yml`, `.github/workflows/link-check-schedule.yml`, `.github/ISSUE_TEMPLATE/suggest-resource.yml`, `.github/PULL_REQUEST_TEMPLATE.md`

**Interfaces:**
- Consumes: hub files listed in Codebase context; the deviation note above.
- Produces: 12 of the 13 launch files, byte-copied or adapted as specified; Task 3 adds README.md; Task 4 pushes this tree; Task 5's CI runs these workflows.

**Model:** flash

- [ ] **Step 1: Init the repo**

```bash
mkdir -p "C:/Users/gower/OneDrive/Documents/GitHub/awesome-digital-engineering"
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-digital-engineering"
git init -b main
mkdir -p .github/workflows .github/ISSUE_TEMPLATE
```

- [ ] **Step 2: Copy the byte-identical hub files**

```bash
HUB="C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
REPO="C:/Users/gower/OneDrive/Documents/GitHub/awesome-digital-engineering"
cp "$HUB/.github/workflows/link-check-pr.yml"       "$REPO/.github/workflows/link-check-pr.yml"
cp "$HUB/.github/workflows/link-check-schedule.yml" "$REPO/.github/workflows/link-check-schedule.yml"
cp "$HUB/.gitignore"                                "$REPO/.gitignore"
cp "$HUB/CODE_OF_CONDUCT.md"                        "$REPO/CODE_OF_CONDUCT.md"
cp "$HUB/SECURITY.md"                               "$REPO/SECURITY.md"
```

Verify each copied file has no hub-specific names to swap: `grep -ri "awesome-mbse\|mbse\|sysml" .gitignore CODE_OF_CONDUCT.md SECURITY.md .github/workflows/` must return nothing (plan-time read says all four are clean; if grep finds something, swap the repo name in that spot and note it in the commit message).

- [ ] **Step 3: LICENSE**

Copy the hub `LICENSE` (CC0-1.0 full legal text) and swap only the repo name on line 1: replace the leading `awesome-mbse` with `awesome-digital-engineering`, keep the rest byte-identical.

```bash
cp "$HUB/LICENSE" "$REPO/LICENSE"
# edit line 1 repo name as above
head -1 "$REPO/LICENSE"   # expect: line 1 starts with awesome-digital-engineering and is otherwise unchanged from the hub
```

- [ ] **Step 4: NOTICE (DE-adapted trademark line)**

Write `NOTICE`:

```text
awesome-digital-engineering

Maintained by JG Systems Consulting Ltd.

This work (the curated index in README.md and the repository's own files) is released
under CC0 1.0 Universal; see LICENSE. To the extent possible under law, the maintainers
have waived all copyright and related rights to it.

Linked resources are the property of their respective owners and are referenced, not
redistributed. Standards are referenced by number and name (ASME Y14.41, ISO 10303
(STEP), QIF / ISO 23952, DMIS / ISO 22093, LOTAR EN/NAS 9300, OAIS / ISO 14721). Those
names and acronyms belong to their respective organizations and are used here
nominatively to describe resources, with no implication of endorsement.
```

- [ ] **Step 5: CONTRIBUTING.md (hub port with DE adaptations)**

Port the hub CONTRIBUTING.md section by section. Sections 5 and 6 are copied verbatim from the hub (spec AC2). The full adapted file:

1. Intro paragraph, adapted: "Thanks for helping keep this the best-curated digital engineering index anywhere, covering digital thread, model-based definition and PMI, and DE policy and standards. Read this before opening a PR; the CI gates enforce most of it." Then keep the hub's two bullets (issue via the Suggest a resource form / PR editing README.md) unchanged.
2. Section 1 "How to suggest a resource": hub text verbatim.
3. Section 2 "Inclusion bar": hub's five numbered rules; rewrite rule 1 as "On-topic: genuinely about digital thread, model-based definition or PMI, or digital engineering policy, strategy, standards, or transformation, within this list's scope." Keep rules 2-5 (substantive, live, not duplicative, legally linkable / link never re-host) and the tie-breakers paragraph verbatim.
4. Section 3 "Entry format": hub text verbatim for the format line and the 140-character rule. Replace the `has-model` paragraph with: "`has-model` means: a directly downloadable, non-paywalled file in a recognized product-data format (`.step` / `.stp` / `.p21`, `.qif`, `.jt`) that opens in a named tool. Screenshots, papers describing a model, and access-gated or request-only files do not qualify. A `type=tool` repo homepage never also carries `has-model`."
5. Section 4 "Tag vocabulary, cardinality and order": open with the rename note, then this table, then the rules:

```markdown
Tags appear in this fixed order, drawn **only** from this vocabulary:

`domain → method → tool → has-model → type → spec/standard → paid → year`

The family shared standard names the first axis `language`. This list renames it to
`domain`: digital engineering has no single modeling language to name, and FAMILY
allows per-list values while keeping the axis order and cardinality. This rename is
the documented per-list deviation.

| Axis | Cardinality | Values |
|------|-------------|--------|
| domain | exactly 1 | `DE-general` · `digital-thread` · `MBD` |
| method | 0 or 1 | `MBE` · `GD&T` |
| tool | 0 or more | `other-tool` (graduates to a named tag at 3+ entries, in one PR) |
| has-model | 0 or 1 | `has-model` (see §3) |
| type | exactly 1 | `tutorial` · `course` · `book` · `paper` · `report` · `blog` · `video` · `tool` · `plugin` |
| spec/standard | 0 or 1 | `spec` · `standard` |
| paid | 0 or 1 | `paid` |
| year | exactly 1 | `(YYYY)` (see §5) |

- Section routing sets the default `domain`: Policy and strategy → `DE-general`;
  Standards → `digital-thread` (STEP / thread exchange) or `MBD` (Y14.41 / PMI / QIF /
  metrology), never `DE-general`; Digital thread → `digital-thread`; MBD and PMI →
  `MBD`; Government and consortia → `DE-general` unless the page is only about one
  standard family; Open tools → `digital-thread` or `MBD` by file or tool focus;
  Learning and reports → `DE-general` unless topic-locked; Commercial platforms →
  match the product's primary claim, always `paid`.
- `DE-general` is legal only when the entry's primary subject is neither
  digital-thread nor MBD (strategy surveys, broad DE transformation, multi-topic
  reports). Reviewers reject lazy `DE-general` on standards and pure MBD/thread tools.
- For a normative document use `spec`/`standard`, and then `type` must be `report`,
  `book`, or `paper` (prefer `report` for storefronts). Never `tutorial` or `tool`
  alongside `standard`. Standards, storefront, policy, and program home pages use
  type `report`.
```

6. Section 5 "The year rule (YYYY)": copy hub section 5 verbatim (title through the two examples).
7. Section 6 "Canonical-URL rule (dedupe)": copy hub section 6 verbatim.
8. Section 7 "Editorial neutrality", adapted:

```markdown
## 7. Editorial neutrality

This list is maintained by JG Systems Consulting Ltd., a commercial vendor of
SysML/Cameo tooling. JGS sells no commercial product into the digital engineering
niche today, so no neutrality conflict currently exists in this list. The rules still
bind if that changes: a JGS entry, if ever listed, meets the same inclusion bar as
everything else, sits next to at least one genuine competing or alternative entry,
and a superior competing resource is listed above a JGS one.
```

9. Keep the hub's Table of Contents blockquote note verbatim right after section 7 (it is the flat-ToC rule; it references lychee `--include-fragments anchor-only`).
10. Section 8 "Local link-check": hub section 9 verbatim (the Docker one-liner stays `README.md`).
11. Section 9 "Maintenance cadence": hub section 10 verbatim.
12. Do NOT port hub section 8 (Model Gallery); it is hub-specific.

- [ ] **Step 6: .lycheeignore (header comment plus the one documented exemption)**

```text
# URLs that are live in a browser but return 403/anti-scrape to automated
# checkers (CDN/WAF bot-blocks), plus access-controlled URLs the family
# standard requires in the README. Add a line (regex) only with a documented
# reason below it. Keep this list short: every entry is a hole in the
# freshness guarantee. Re-verify during the quarterly sweep.

# Hub FAMILY.md is private until the family public release. The README carries
# the family pointer as an absolute URL (family standard, spec requirement);
# that URL 404s to unauthenticated checkers and to this repo's CI token.
# Remove this line when awesome-mbse goes public.
https://github\.com/jgsystemsconsulting/awesome-mbse/blob/main/FAMILY\.md
```

Any candidate that passed browser verification on a blocked host (Task 1) gets one more line here, pattern first, then the comment `# browser-verified YYYY-MM-DD: <reason>`.

- [ ] **Step 7: CHANGELOG.md (launch entry)**

```markdown
# Changelog

Maintenance sweeps and notable changes. The "Last full sweep" badge in the README
tracks the most recent dated entry here.

## 2026-09 - Launch (initial seed)

- First public release of the digital engineering spoke of the awesome-mbse list
  family: digital thread, model-based definition and PMI, and DE policy, standards,
  and transformation.
- N verified entries (final count from Task 1); every link checked HTTP 200-299 on
  launch day.
- initial seed; growth in progress. Remaining candidates are tracked in `seed-inventory`
  issues and the next sweep targets the family ~40-entry bar.
- CI on day one: `link-check (PR)` (lychee + awesome-lint) and the weekly
  `link-check (weekly)` link-rot report.
```

Update the entry count N once the README is final (Task 3, step 5).

- [ ] **Step 8: Issue form .github/ISSUE_TEMPLATE/suggest-resource.yml**

```yaml
name: Suggest a resource
description: Suggest a digital engineering / digital thread / MBD resource to add to the list
title: "[Suggestion] <resource name>"
labels: ["suggestion"]
body:
  - type: input
    id: name
    attributes:
      label: Resource name
      placeholder: e.g. DoD Digital Engineering Strategy
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
      label: One-line description (140 characters max, factual, no hype)
    validations:
      required: true
  - type: dropdown
    id: section
    attributes:
      label: Which section does it belong in?
      options:
        - Policy and strategy
        - Standards
        - Digital thread and interoperability
        - Model-based definition and PMI
        - Government and consortia programs
        - Open tools and reference implementations
        - Learning and reports
        - Commercial platforms
    validations:
      required: true
  - type: checkboxes
    id: bar
    attributes:
      label: Inclusion bar (see CONTRIBUTING.md)
      options:
        - label: On-topic for digital thread, MBD, or DE transformation
          required: true
        - label: Substantive (teaches/demonstrates/specifies/provides something usable, not pure marketing)
          required: true
        - label: The link is live right now
          required: true
        - label: It isn't already in the list
          required: true
        - label: Publicly accessible (we link, we never re-host)
          required: true
```

- [ ] **Step 9: PR template .github/PULL_REQUEST_TEMPLATE.md**

```markdown
<!-- Thanks for contributing! Check every box; CI enforces most of these. -->

## What I'm adding / changing

<!-- one line -->

## Inclusion bar (CONTRIBUTING.md section 2)

- [ ] On-topic for digital thread, MBD, or digital engineering transformation
- [ ] Substantive, not pure marketing
- [ ] Link is live (CI link-checks it; you can pre-check with the Docker one-liner in CONTRIBUTING.md)
- [ ] Not a duplicate (canonical-URL rule, CONTRIBUTING.md section 6)
- [ ] Publicly accessible, linked not re-hosted

## Entry format (CONTRIBUTING.md sections 3-4)

- [ ] `- [Name](url) - Description ` plus inline-code tags plus `(YYYY).`; hyphen separator, not an en/em-dash
- [ ] Description at most 140 characters (first character after ` - ` to the character before the first tag backtick)
- [ ] Tags drawn only from the DE vocabulary, in fixed order (domain, method, tool, has-model, type, spec/standard, paid, year)
- [ ] Exactly one `domain` and one `type`; `standard`/`spec` only with type `report`/`book`/`paper`
- [ ] `(YYYY)` is the resource's most recent author-published version
- [ ] If `has-model`: the primary URL is the directly downloadable, non-paywalled model file (CONTRIBUTING.md section 3)

## Housekeeping

- [ ] If a top-level section was added or renamed, updated the hand-maintained `## Contents` ToC
- [ ] (If a JGS product) it sits next to at least 1 competing entry (CONTRIBUTING.md section 7)
```

- [ ] **Step 10: Verify the 12 files and commit**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-digital-engineering"
git status --porcelain   # expect exactly: 4 top-level adapted files, LICENSE, NOTICE, .gitignore, .lycheeignore, 2 workflows, issue template, PR template
grep -c "most recent author-published version" CONTRIBUTING.md   # expect 1 (hub section 5 ported)
grep -c "canonicalize both URLs" CONTRIBUTING.md                 # expect 1 (hub section 6 ported)
grep -c "renames it to" CONTRIBUTING.md                          # expect 1 (domain rename documented)
git add -A
git commit -m "chore: launch skeleton (community files, CI, templates)"
```

---

### Task 3: README.md with verified seed entries

**Files:**
- Create: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-digital-engineering\README.md`

**Interfaces:**
- Consumes: the `## Verified set` blocks from Task 1's inventory; the skeleton files from Task 2.
- Produces: the 13th and final launch file; the URL set that Tasks 5 (CI) and 8 (AC sweep) validate.

**Model:** standard

- [ ] **Step 1: Write the README skeleton**

```markdown
# Awesome Digital Engineering [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated, vetted, dated index of **digital engineering**: digital thread architecture,
> model-based definition and PMI, and the policy and standards behind DE transformation.

![Last full sweep: 2026-09](https://img.shields.io/badge/last%20full%20sweep-2026--09-brightgreen)

Part of the [awesome-mbse list
family](https://github.com/jgsystemsconsulting/awesome-mbse/blob/main/FAMILY.md).

Maintained by [JG Systems Consulting Ltd.](https://github.com/jgsystemsconsulting).
See [Editorial neutrality](CONTRIBUTING.md#7-editorial-neutrality).

initial seed; growth in progress. Every entry below passed a live link check on launch
day; the tracked path to the family ~40-entry bar lives in the `seed-inventory` issues.

## Contents

- [Policy and strategy](#policy-and-strategy)
- [Standards](#standards)
- [Digital thread and interoperability](#digital-thread-and-interoperability)
- [Model-based definition and PMI](#model-based-definition-and-pmi)
- [Government and consortia programs](#government-and-consortia-programs)
- [Open tools and reference implementations](#open-tools-and-reference-implementations)
- [Learning and reports](#learning-and-reports)
- [Commercial platforms](#commercial-platforms)

## Policy and strategy

_No verified entries yet._

## Standards

_No verified entries yet._

## Digital thread and interoperability

_No verified entries yet._

## Model-based definition and PMI

_No verified entries yet._

## Government and consortia programs

_No verified entries yet._

## Open tools and reference implementations

_No verified entries yet._

## Learning and reports

_No verified entries yet._

## Commercial platforms

_No verified entries yet._
```

- [ ] **Step 2: Paste verified entries under their sections**

For every `## Verified set` block in the Task 1 inventory, paste the entry line under its target section H2, one per line, no sub-headers. Delete a section's `_No verified entries yet._` stub only when that section now has at least one entry. Keep stubs for genuinely empty sections. Nothing else changes: the eight H2s always exist in order.

- [ ] **Step 3: Run the local anchor and format checks**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-digital-engineering"
python - <<'EOF'
import re, pathlib
md = pathlib.Path("README.md").read_text(encoding="utf-8")
def slug(h):
    s = h.strip().lower()
    s = re.sub(r"[^a-z0-9 -]", "", s)
    return s.replace(" ", "-")
heads = {slug(h) for h in re.findall(r"^## (.+)$", md, re.M)}
toc = re.findall(r"\]\(#(.+?)\)", md)
missing = [t for t in toc if t not in heads]
print("ToC anchors:", len(toc), "missing:", missing or "none")
assert not missing, missing
lines = [l for l in md.splitlines() if re.match(r"^- \[.+\]\(https?://[^)]+\)", l)]
print("entries:", len(lines))
for l in lines:
    assert " - " in l and l.rstrip().endswith(")."), l
    desc = l.split(" - ", 1)[1]
    desc = desc[:desc.index("`")] if "`" in desc else desc
    assert len(desc.strip()) <= 140, (len(desc.strip()), l[:60])
    assert not re.search(r"[—–]", l), "en/em dash in entry"
print("entry format OK")
EOF
```

Expected: `missing: none`, `entry format OK`.

- [ ] **Step 4: Optional local lint (informational)**

If Docker is available: `docker run --rm -v "$PWD:/d" -w /d lycheeverse/lychee --include-fragments anchor-only --accept 200..=299,429 --no-progress README.md` (expect zero errors). Then `npx -y awesome-lint` (Node 20). The awesome-lint run may complain about the missing GitHub remote before Task 4 creates it; the binding gate is CI in Task 5. Note any findings and fix real ones.

- [ ] **Step 5: Finalize counts and commit**

Set `N verified entries` in CHANGELOG.md (Task 2 step 7) to the actual count. Count H2 sections (must be 8) and ToC lines (must be 8). Then:

```bash
git add README.md CHANGELOG.md
git commit -m "docs: README with verified seed entries"
```

---

### Task 4: Create the GitHub repo and push main

**Files:** none new; pushes Tasks 2-3 output.

**Interfaces:**
- Consumes: local repo at `C:\Users\gower\OneDrive\Documents\GitHub\awesome-digital-engineering` with `main` and two commits.
- Produces: `https://github.com/jgsystemsconsulting/awesome-digital-engineering`, public, default branch `main`, remote `origin`.

**Model:** flash

- [ ] **Step 1: Same-day namespace re-check (FAMILY rule)**

```bash
gh api repos/jgsystemsconsulting/awesome-digital-engineering 2>&1 | head -3
```

Expected: `Not Found` (404). If it unexpectedly exists, STOP and report; do not overwrite.

- [ ] **Step 2: Create and push (preferred path)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-digital-engineering"
gh repo create jgsystemsconsulting/awesome-digital-engineering --public --source . --remote origin --push
```

- [ ] **Step 3: Fallback chain if Step 2 fails on auth or org permission**

```bash
# fallback A: create empty repo via API, then wire the remote by hand
gh repo create jgsystemsconsulting/awesome-digital-engineering --public
git remote add origin https://github.com/jgsystemsconsulting/awesome-digital-engineering.git
git push -u origin main
```

If both `gh` paths fail (auth expired, org restriction), fall back to the web UI: create an empty public repo named `awesome-digital-engineering` under the org with no README, no license, no gitignore (empty repo), then run the `git remote add` and `git push -u origin main` lines from fallback A. Note which path was used in the task result.

- [ ] **Step 4: Verify identity**

```bash
gh repo view jgsystemsconsulting/awesome-digital-engineering --json isPrivate,defaultBranchRef,url
git -C "C:/Users/gower/OneDrive/Documents/GitHub/awesome-digital-engineering" rev-parse --show-toplevel
```

Expected: `isPrivate: false`, `defaultBranchRef.main`, url as above; toplevel is the sibling path (its own git root, not inside the hub tree).

---

### Task 5: CI proof: launch PR green, schedule workflow dispatched

**Files:**
- Modify: `README.md` (one verified reserve entry, on a branch)

**Interfaces:**
- Consumes: Task 1 inventory reserve rows (verified but not yet in the README; if none remain, move one shipped entry's wording tweak through the PR instead, still touching README.md so the path filter triggers).
- Produces: green `link-check (PR)` run on a merged launch PR, one `link-check (weekly)` dispatch run, AC6 evidence.

**Model:** standard

- [ ] **Step 1: Open the launch PR with a real README byte change**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-digital-engineering"
git checkout -b seed/launch-ci-proof
```

Mutate README.md so `git status` is dirty (path filter must fire). Prefer order:

1. Paste one verified reserve entry from Task 1 under its section H2 (replace the stub line).
2. Else tweak one existing entry description by a few characters without breaking the 140-char rule.
3. Else append a single trailing newline or a one-character whitespace-only edit under the scope note (no-op content, still a file change).

Then:

```bash
python - <<'EOF'
import re, pathlib
md = pathlib.Path("README.md").read_text(encoding="utf-8")
print("entries:", len([l for l in md.splitlines() if re.match(r"^- \[.+\]\(https?://[^)]+\)", l)]))
EOF
git add README.md
git status --porcelain   # must show M README.md
git commit -m "readme: launch CI proof"
gh pr create --base main --title "Launch CI proof" --body "Launch PR so link-check (PR) runs before launch is declared. Checklist: on-topic, substantive, link live, not a duplicate, linked not re-hosted; format per CONTRIBUTING sections 3-4."
```

- [ ] **Step 2: Watch both jobs green**

```bash
gh pr checks --watch
gh run list --workflow=link-check-pr.yml --limit 2
```

Expected: `lychee` and `awesome-lint` both pass. If lychee fails, debug in this order: (a) the dead URL is a genuinely unverified entry, fix the entry or omit it; (b) a blocked-host URL lacks its `.lycheeignore` line plus `# browser-verified` comment, add the pair only for URLs that passed browser verification in Task 1; (c) anchor mismatch, rerun the Task 3 step 3 checker. Re-push and re-watch until green.

- [ ] **Step 3: Ensure labels, merge, dispatch schedule workflow**

```bash
gh label create link-rot --repo jgsystemsconsulting/awesome-digital-engineering --color B60205 --description "Scheduled link-check findings" 2>/dev/null || true
gh label create seed-inventory --repo jgsystemsconsulting/awesome-digital-engineering --color 0E8A16 --description "Post-launch seed candidates" 2>/dev/null || true
gh pr merge --squash --delete-branch
git checkout main && git pull
gh workflow run link-check-schedule.yml
sleep 20
gh run list --workflow=link-check-schedule.yml --limit 1
gh issue list --label link-rot
```

Expected: squash merge green; the dispatched run completes (report-only, `fail: false`, so success even with rot findings); zero or one open `link-rot` issue.

- [ ] **Step 4: Negative check: no markdownlint**

```bash
gh workflow list
gh api repos/jgsystemsconsulting/awesome-digital-engineering/contents/.github/workflows --jq '.[].name'
```

Expected: exactly `link-check-pr.yml` and `link-check-schedule.yml`; no markdownlint workflow anywhere.

---

### Task 6: Convert remaining viable inventory rows to seed-inventory issues

**Files:** none in the repo; GitHub issues only.

**Interfaces:**
- Consumes: Task 1 inventory rows with verdict `issue`.
- Produces: the `seed-inventory` label and one issue per viable row; AC9 evidence.

**Model:** flash

- [ ] **Step 1: Create the label (idempotent)**

```bash
gh label create seed-inventory --repo jgsystemsconsulting/awesome-digital-engineering \
  --description "Seed inventory candidate: verify and add toward the ~40-entry bar" \
  --color 0E8A16 || true
```

- [ ] **Step 2: One issue per viable row**

For each inventory row marked `issue` (candidates that plausibly pass the inclusion bar but were not verified, or were 429/503 on launch day):

```bash
gh issue create --repo jgsystemsconsulting/awesome-digital-engineering \
  --label seed-inventory \
  --title "Seed candidate: <candidate name>" \
  --body "URL: <url>
Host: <host> (provisional host: browser-verify or omit per seed policy)
Target section: <section>
Why viable: <one line from inventory>
Next step: verify HTTP 200-299 (429 is not enough), then PR with entry format per CONTRIBUTING sections 3-4."
```

- [ ] **Step 3: Verify**

```bash
gh issue list --repo jgsystemsconsulting/awesome-digital-engineering --label seed-inventory --state open
```

Expected: one line per converted row; every remaining viable inventory row has an issue.

---

### Task 7: Hub integration (awesome-mbse)

**Files:**
- Modify: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-mbse\FAMILY.md` (registry row, per-spoke checklist)
- Modify: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-mbse\README.md` (List family table row, gaps snapshot sentence)

**Interfaces:**
- Consumes: the spoke live and CI-green (Tasks 4-5).
- Produces: AC10. Same-day namespace rule already satisfied by Task 4 step 1.

**Model:** flash

- [ ] **Step 1: Flip the FAMILY.md registry row (line 54)**

Replace:

```markdown
| awesome-digital-engineering | Digital thread, model-based definition, digital engineering transformation | Planned | none yet |
```

with:

```markdown
| [awesome-digital-engineering](https://github.com/jgsystemsconsulting/awesome-digital-engineering) | Digital thread, model-based definition, digital engineering transformation | Live | public |
```

- [ ] **Step 2: Update the FAMILY.md per-spoke checklist (lines 187-196)**

Replace the `### awesome-digital-engineering` block with:

```markdown
### awesome-digital-engineering

Live. Public spoke launched 2026-09-17 under the explicit under-40 override (maintainer
decision: Live = repo + green CI + honest "initial seed; growth in progress" label).
Growth is tracked in the spoke's `seed-inventory` issues.

- [x] Namespace re-checked on 2026-09-17 (result: empty)
- [ ] Roughly 40 candidate entries: NOT met at launch (under-40 override, logged above; inventory ledger in docs/superpowers/seed-inventory-awesome-digital-engineering.md)
- [x] Repo created (public, not private: launch decision) from the README skeleton
- [x] Hub README family table row updated with the URL
- [x] Registry status flipped to Live
```

The unticked second box stays honestly unticked; do not force it green.

- [ ] **Step 3: Update the hub README List family row (line 33)**

Replace:

```markdown
| awesome-digital-engineering | Digital thread, model-based definition, digital engineering transformation | Planned | GAP (absent) |
```

with:

```markdown
| [awesome-digital-engineering](https://github.com/jgsystemsconsulting/awesome-digital-engineering) | Digital thread, model-based definition, digital engineering transformation | Live | Linked public spoke |
```

- [ ] **Step 4: Update the gaps snapshot sentence (hub README lines 36-39)**

In the paragraph beginning `Gaps, snapshot 2026-09-17`, change the clause `requirements engineering and digital engineering are absent from the hub` to `requirements engineering is absent from the hub, and digital engineering now lives in the awesome-digital-engineering spoke (launched 2026-09-17)`, and update the snapshot date to the execute date.

- [ ] **Step 5: Verify there is no DE-routed hub section to shrink (AC10 third clause)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
grep -niE "digital thread|digital engineering|model-based definition" README.md | grep -viE "list family|spoke|awesome-digital-engineering|snapshot"
```

Expected: no output (hub research and the gap snapshot say DE is absent; the only DE-routed hub content is the registry rows just edited). If output appears, evaluate each hit **in this task**: genuinely cross-cutting entries stay; DE-only entries shrink to a short pointer to the spoke (do not leave unshrunk DE-only hub sections). Record the finding either way.

- [ ] **Step 6: Commit and push the hub**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
git add FAMILY.md README.md
git commit -m "docs(family): awesome-digital-engineering spoke goes Live"
git push origin main
git log --oneline -1
```

Note: `docs/` (spec, research, plan, inventory) is untracked and must NOT be committed here.

---

### Task 8: Acceptance sweep (AC1-AC11)

**Files:** none new; read-only verification plus fixes if any check fails.

**Interfaces:**
- Consumes: everything above.
- Produces: the evidence list for the completion report.

**Model:** standard

- [ ] **Step 1: AC1 identity**

```bash
gh repo view jgsystemsconsulting/awesome-digital-engineering --json isPrivate,defaultBranchRef
git -C "C:/Users/gower/OneDrive/Documents/GitHub/awesome-digital-engineering" rev-parse --show-toplevel
```

Public, default `main`, toplevel equals the sibling path.

- [ ] **Step 2: AC2 inventory and CONTRIBUTING content**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-digital-engineering"
git ls-files | sort
grep -c "most recent author-published version" CONTRIBUTING.md      # 1 (hub year rule verbatim)
grep -c "canonicalize both URLs" CONTRIBUTING.md                    # 1 (dedupe rule verbatim)
grep -c "renames it to" CONTRIBUTING.md                             # 1 (domain rename)
grep -c "DE-general" CONTRIBUTING.md                                # >= 3 (value set, routing, rule)
```

Exactly the 13 files; CONTRIBUTING.md uppercase.

- [ ] **Step 3: AC3 and AC4 README structure**

```bash
grep -n "awesome.re/badge\|last%20full%20sweep\|FAMILY.md" README.md | head -5
grep -c "^## " README.md        # 9 (## Contents + 8 sections)
grep -n "initial seed; growth in progress" README.md
python - <<'EOF'
import re, pathlib
md = pathlib.Path("README.md").read_text(encoding="utf-8")
def slug(h):
    s = h.strip().lower(); s = re.sub(r"[^a-z0-9 -]", "", s); return s.replace(" ", "-")
heads = {slug(h) for h in re.findall(r"^## (.+)$", md, re.M)}
assert all(t in heads for t in re.findall(r"\]\(#(.+?)\)", md))
order = [h for h in re.findall(r"^## (.+)$", md, re.M) if h != "Contents"]
assert order == ["Policy and strategy","Standards","Digital thread and interoperability",
 "Model-based definition and PMI","Government and consortia programs",
 "Open tools and reference implementations","Learning and reports","Commercial platforms"], order
print("structure OK, entries:", len([l for l in md.splitlines() if re.match(r"^- \[.+\]\(https?://[^)]+\)", l)]))
EOF
```

Family pointer must be the absolute URL. Anchor integrity is proven by the green lychee run in Task 5.

- [ ] **Step 4: AC5 and AC11 verification trail**

Cross-check: every README entry URL appears in the Task 1 inventory with verdict `verified` and either (a) HTTP 200-299 on curl or (b) Browser verified plus a matching active `.lycheeignore` line with `# browser-verified` (or the single FAMILY.md access-control exemption). Then:

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-digital-engineering"
grep -nE "acq\.osd\.mil|media\.defense\.gov|iso\.org|incose\.org|ndia\.org|sebokwiki\.org|researchgate\.net|ntrs\.nasa\.gov|wiley|onlinelibrary" README.md .lycheeignore
grep -n "CC0\|trademark\|linked resources\|JG Systems" NOTICE | head -10
```

Every README hit on provisional hosts must have a matching `.lycheeignore` pattern with a documented reason comment. No repo file re-hosts third-party content (`git ls-files` shows only the 13 files).

- [ ] **Step 5: AC6, AC7, AC8, AC9, AC10**

```bash
gh run list --repo jgsystemsconsulting/awesome-digital-engineering --limit 5
gh workflow list --repo jgsystemsconsulting/awesome-digital-engineering
head -3 LICENSE
grep -n "initial seed; growth in progress" README.md CHANGELOG.md
gh issue list --repo jgsystemsconsulting/awesome-digital-engineering --label seed-inventory --state open
# AC9: issue count must equal Task 1 rows with verdict=issue (zero is OK when none remain)
grep -n "awesome-digital-engineering" "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse/FAMILY.md" "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse/README.md"
# AC10: hub must not still hold a full DE resource section; pointer or absence only
rg -n "Digital Engineering|digital thread|model-based definition|Y14.41" "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse/README.md" || true
ls "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse/docs/superpowers/seed-inventory-awesome-digital-engineering.md"
```

Expected: a green PR run for `link-check (PR)` and a completed dispatched run for the weekly workflow; exactly the two workflows (no markdownlint); LICENSE starts with CC0 for the new repo name; the under-40 phrase in both files when entry count < 40; seed-inventory open issues equal inventory `issue` rows (may be zero); hub FAMILY row says Live with the URL and hub README links the spoke; Task 7 applied shrink/pointer rule (no unshrunk DE hub section); the inventory file exists outside the spoke.

- [ ] **Step 6: Fix-and-rerun loop**

Any failed check: fix at the task that owns the artifact, rerun that task's verification, then rerun this sweep. Do not declare done with a red check. Finish by reporting the AC1-AC11 evidence list in the task result.

---

## Research

Research gate: `docs/superpowers/research/2026-09-17-awesome-digital-engineering-research.md`
(log: `docs/superpowers/research/2026-09-17-awesome-digital-engineering-research-log.md`).
Context gate: `docs/superpowers/context/2026-09-17-awesome-digital-engineering-context.md`.

URLs established or provisionally identified by the gate, all subject to Task 1 verification:

- https://www.asme.org/codes-standards/find-codes-standards/y14-41-digital-product-definition-data-practices
- https://qifstandards.org/about-dmsc/
- https://lotar-international.org/
- https://ntrs.nasa.gov/api/citations/search/?q=%22digital%20engineering%22&page.size=5
- https://en.wikipedia.org/wiki/ISO_10303
- https://github.com/search?q=awesome-digital-engineering&type=repositories
- https://api.github.com/repos/jgsystemsconsulting/awesome-digital-engineering
- https://github.com/jgsystemsconsulting/awesome-mbse/blob/main/CONTRIBUTING.md
- https://github.com/jgsystemsconsulting/awesome-mbse/blob/main/FAMILY.md

Blocked this session, candidates only until browser-verified in execute: `acq.osd.mil`, `media.defense.gov`, `iso.org`, `incose.org`, `ndia.org`, `sebokwiki.org`.
