# List family private structure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the awesome-mbse list family visible inside the private hub: FAMILY.md becomes the private-mode operating manual, the hub README shows the whole family with honest statuses and gap callouts, the local magic-grid sibling gets an honest STATUS.md, and the public sysml-v2 spoke gets a link-free family pointer.

**Architecture:** Docs-only reshape across three existing repos (hub, local sibling, public spoke). FAMILY.md gains a Visibility column, a Private mode section, an external-lists and namespace registry, and per-spoke checklists; the hub README mirrors the registry in a List family table and converts the competitive-landscape table into an External awesome lists section in family entry format. Every missing piece is an explicit GAP or TODO marker; no repos, directories, or visibility states change.

**Tech Stack:** Markdown, ripgrep (`rg`), awk/grep for content counts, `npx awesome-lint`, git (local commits only, never push).

**Spec:** docs/superpowers/specs/2026-09-17-list-family-private-structure.md

## Global Constraints

Locked decisions and vocabulary, verbatim from the spec. Every task implicitly includes these.

- D1: Structure lives in hub README and FAMILY.md. Allowed sibling edits only: `../awesome-magic-grid/STATUS.md` (create) and one pointer line in `../awesome-sysml-v2/README.md`. No new repos, no new directories under the hub.
- D2: awesome-magic-grid gets a status note file only; content re-scope stays TODO.
- D3: awesome-sysml-v2 gets one text family pointer, no hyperlink to the private hub. If awesome-lint rejects the line, drop it and record the pointer as TODO under the live-spoke checklist in FAMILY.md; that path still passes acceptance.
- D4: Planned spokes exist as stub rows and FAMILY checklists, never as links or empty repos.
- D5: All edits stay local. No visibility changes. No pushes; the user orders pushes.
- Status vocabulary (registry Status column only): `Live` | `In development` | `Planned`. Visibility never appears inside Status cells.
- Visibility vocabulary: `public` | `private` | `local only` | `none yet`.
- Marker vocabulary: `GAP` means the niche has no adequate hub home today. `TODO` means a concrete next action is pending (create repo, re-check namespace, re-scope).
- Namespace result vocabulary: `empty` | `incumbent found` | `TODO re-check`. Map "empty-ish" to `empty`.
- Zero new em dashes in changed prose (hub README, FAMILY.md, STATUS.md, spoke README).
- Hub deep content (Magic Grid and Cameo, Model Gallery, Broader SysML / MBSE Context) is untouched: the hub shrinks a niche only when the spoke repo is real.
- sindresorhus submission is deferred to the future public-release runbook; no submission files or PRs in this work.

Repo roots used by every command in this plan:

- Hub: `C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse` (HEAD at plan time: `4f7c0a6`)
- Magic-grid sibling: `C:/Users/gower/OneDrive/Documents/GitHub/awesome-magic-grid` (local git repo)
- Public spoke: `C:/Users/gower/OneDrive/Documents/GitHub/awesome-sysml-v2` (public git repo)

## Research

Patterns this plan copies. Full findings: `docs/superpowers/research/2026-09-17-list-family-private-structure-research.md`.

- https://github.com/sindresorhus/awesome (canonical meta-list pattern: category-grouped links, Contents section, badge ecosystem)
- https://github.com/sindresorhus/awesome/blob/main/create-list.md (creation bar behind the roughly-40-entry rule)
- https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md (submission bar, deferred)
- https://github.com/sindresorhus/awesome-lint (lint rules that decide the spoke pointer fallback in Task 4)
- https://github.com/mycr0ft/awesome-sysml (external SysML list; first row of the external registry)
- https://github.com/topics/awesome (topic scale)
- https://github.com/search?q=awesome-archimate&type=repositories (namespace check, 2026-09: empty-ish, mapped to `empty`)
- https://awesome.re (badge ecosystem)

## Codebase context

From `docs/superpowers/context/2026-09-17-list-family-private-structure-context.md`, confirmed against the working tree:

- `FAMILY.md` (129 lines) is the family contract: Model (line 9), Registry (line 31, table 33-42), Scope boundaries (line 47), Shared standard (line 66), Starting a new list (line 93), README skeleton (line 106). Registry Status cells currently mix vocabulary with dates ("Planned. Namespace empty as of 2026-09"); Task 1 moves the dates into a namespace table so Status becomes pure vocabulary.
- Hub `README.md`: maintainer blockquote lines 15-18; the `**List family:**` pointer paragraph lines 20-21 (deleted in Task 2, not duplicated); Contents lines 23-29; Magic Grid section lines 31-111 with 35 `- [` entry lines; Model Gallery lines 113-145 with 24 table rows; Broader Context line 147; The competitive landscape lines 235-248 (replaced in Task 2); Contributing line 250; Support & security line 256.
- Hub CI: `.github/workflows/link-check-pr.yml` plus a scheduled lychee sweep with `--include-fragments=anchor-only`; awesome-lint active. markdownlint is listed in FAMILY but absent from hub CI (known drift, not fixed here). The only new outbound URL this work adds is the already-live awesome-sysml-v2 link, so no CI config changes.
- `../awesome-magic-grid`: local git repo. README is titled Awesome MBSE and is generated output (`scripts/generate.py` over `data/entries.yaml`, AUTOGEN markers). No STATUS.md exists today.
- `../awesome-sysml-v2`: public repo, flat entry format without tags or years, no family pointer, no sweep badge. `.github/workflows/lint.yml` runs `npx awesome-lint@2.3.0 README.md` plus markdownlint-cli2 on push and PR to main.
- Acceptance 5 nuance: the spoke repo contains two untracked local working notes under `docs/superpowers/` (research and spec files) that mention `jgsystemsconsulting/awesome-mbse` in prose. They are not part of the published repo. Verification therefore checks tracked content with `git grep` (must be empty) and scopes `rg` to `README.md`; a repo-wide raw `rg` over untracked notes is not the public surface and is not the acceptance target.

---

### Task 1: FAMILY.md becomes the private-mode operating manual

**Files:**
- Modify: `FAMILY.md` (Registry table lines 33-45; new section after `## Model`; new section after `## Scope boundaries`; checklist subsections appended inside `## Starting a new list`)

**Interfaces:**
- Produces: pure Status vocabulary (`Live` / `In development` / `Planned`) that Task 2's hub table copies exactly.
- Produces: the `### awesome-sysml-v2 live-spoke alignment` checklist whose first box Task 4 rewrites verbatim in the lint-fallback path.
- Produces: the checkbox inventory Task 5 counts (`rg -c "^- \[ \]" FAMILY.md` returns 34: 5 template + 25 create + 4 alignment).

**Model:** flash

- [ ] **Step 1: Replace the Registry table and its trailing rules**

Replace everything from the header row `| Repo | Owns | Status |` through `Update the Status column when a repo goes live.` with:

```markdown
| Repo | Owns | Status | Visibility |
|------|------|--------|------------|
| [awesome-mbse](https://github.com/jgsystemsconsulting/awesome-mbse) | Hub. Cross-cutting MBSE: methods, tool landscape, openable models, Magic Grid / Cameo | Live | private |
| [awesome-sysml-v2](https://github.com/jgsystemsconsulting/awesome-sysml-v2) | SysML v2 the language: spec, parsers, editors, API clients, example models | Live | public |
| awesome-magic-grid | Magic Grid method and Cameo practice | In development | local only. No GitHub repo exists; the local working copy is a hub fork pending re-scope, not a niche spoke |
| awesome-archimate | ArchiMate 3.x, the Archi tool, EA modeling practice | Planned | none yet |
| awesome-capella | Capella tool and the Arcadia method | Planned | none yet |
| awesome-requirements-engineering | Requirements as a discipline: EARS, KAOS, ReqIF, tooling, papers | Planned | none yet |
| awesome-digital-engineering | Digital thread, model-based definition, digital engineering transformation | Planned | none yet |
| awesome-stpa | STAMP / STPA and hazard analysis; functional safety methods | Planned | none yet |

Status is only `Live` | `In development` | `Planned`. Visibility is only `public` |
`private` | `local only` | `none yet`, and never appears inside Status cells. Namespace
check dates live in the namespace table under External lists and namespaces.

Do not add a registry row until the GitHub namespace has been checked again that day.
Update the Status column when a repo goes live.
```

- [ ] **Step 2: Insert `## Private mode` after `## Model`**

Insert between the end of `## Model` (after "...genuinely cross-cutting.") and `## Registry`:

```markdown
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
```

- [ ] **Step 3: Insert `## External lists and namespaces` after `## Scope boundaries`**

Insert between the end of `## Scope boundaries` (after "...get a cross-link from the other.") and `## Shared standard`:

```markdown
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
| awesome-archimate | 2026-09-17 | empty | Re-check on create day |
| awesome-capella | - | TODO re-check | Re-check on launch day (rate-limited on the 2026-09-17 list-family pass) |
| awesome-stpa | - | TODO re-check | Re-check on launch day (rate-limited on the 2026-09-17 list-family pass) |
| awesome-requirements-engineering | 2026-06 | empty | Re-check on create day (niche research: namespace free or thin incumbents) |
| awesome-digital-engineering | 2026-06 | empty | Re-check on create day (niche research: namespace free or thin incumbents) |
```

- [ ] **Step 4: Append checklist subsections inside `## Starting a new list`**

Insert after existing step 6 (the sindresorhus submission step) and before `## README skeleton`:

```markdown
### Per-spoke create checklist template

Copy per planned spoke. The checklists are the structure; do not create the repo first.

- [ ] Namespace re-checked on YYYY-MM-DD (result: empty / incumbent found)
- [ ] Roughly 40 candidate entries gathered, all passing the inclusion bar
- [ ] Repo created (private) from the README skeleton
- [ ] Hub README family table row updated with the URL
- [ ] Registry status flipped to Live

### awesome-archimate

Planned. Hub GAP: no dedicated ArchiMate section. Namespace empty on 2026-09-17.

- [ ] Namespace re-checked on YYYY-MM-DD (result: empty / incumbent found)
- [ ] Roughly 40 candidate entries gathered, all passing the inclusion bar
- [ ] Repo created (private) from the README skeleton
- [ ] Hub README family table row updated with the URL
- [ ] Registry status flipped to Live

### awesome-capella

Planned. Hub carries Capella/Arcadia thinly: four Broader Context entries (Arcadia
method page, Arcadia primer, py-capellambse, Eclipse Capella). Namespace TODO re-check
(rate-limited on the 2026-09-17 list-family pass).

- [ ] Namespace re-checked on YYYY-MM-DD (result: empty / incumbent found)
- [ ] Roughly 40 candidate entries gathered, all passing the inclusion bar
- [ ] Repo created (private) from the README skeleton
- [ ] Hub README family table row updated with the URL
- [ ] Registry status flipped to Live

### awesome-requirements-engineering

Planned. Hub GAP: requirements engineering is absent from the hub. Namespace empty per
niche research; re-check on create day.

- [ ] Namespace re-checked on YYYY-MM-DD (result: empty / incumbent found)
- [ ] Roughly 40 candidate entries gathered, all passing the inclusion bar
- [ ] Repo created (private) from the README skeleton
- [ ] Hub README family table row updated with the URL
- [ ] Registry status flipped to Live

### awesome-digital-engineering

Planned. Hub GAP: digital engineering is absent from the hub. Namespace empty per
niche research; re-check on create day.

- [ ] Namespace re-checked on YYYY-MM-DD (result: empty / incumbent found)
- [ ] Roughly 40 candidate entries gathered, all passing the inclusion bar
- [ ] Repo created (private) from the README skeleton
- [ ] Hub README family table row updated with the URL
- [ ] Registry status flipped to Live

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
```

- [ ] **Step 5: Verify**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
rg -n "^## (Private mode|External lists and namespaces)$" FAMILY.md    # expect 2 hits
rg -n "Namespace empty as of" FAMILY.md                                # expect no output
rg -n "awesome-(archimate|capella|requirements-engineering|digital-engineering|stpa|magic-grid)" FAMILY.md | rg "\]\(https://github\.com/"
                                                                       # expect no output (planned/magic-grid names never link out)
rg -n "\| (Live|In development|Planned) \|" FAMILY.md | wc -l          # expect 8 (one per registry row)
rg -c "^- \[ \]" FAMILY.md                                             # expect 34
rg -n "—" FAMILY.md                                                    # expect no output
```

- [ ] **Step 6: Commit (local only, never push)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
git add FAMILY.md
git commit -m "docs(family): visibility column, private mode, external lists, spoke checklists"
```

**Done when:** every Step 5 command shows its expected output, the commit exists on the local branch, and `git status` shows nothing new beyond `?? docs/`.

---

### Task 2: Hub README shows the family

**Files:**
- Modify: `README.md` (pointer paragraph lines 20-21; Contents lines 25-29; competitive landscape section lines 235-248)

**Interfaces:**
- Consumes: Task 1's registry Status values (`Live` / `In development` / `Planned`); hub table Status cells must match FAMILY exactly.
- Produces: `## List family` and `## External awesome lists` sections Task 5 greps; deep-content counts (35 entry lines, 24 gallery rows) that must survive unchanged for Task 5.

**Model:** flash

- [ ] **Step 1: Capture baseline counts before editing**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
awk '/^## Magic Grid & Cameo/{f=1;next} /^## /{f=0} f' README.md | grep -c '^- \['   # expect 35
awk '/^## Model Gallery/{f=1;next} /^## /{f=0} f' README.md | grep -c '^| \['        # expect 24
git status --porcelain=v1                                                            # expect " M FAMILY.md" (Task 1) and "?? docs/" only
```

- [ ] **Step 2: Replace the `**List family:**` pointer paragraph with the new section**

Replace these two lines exactly:

```markdown
**List family:** this repo is the hub. See [FAMILY.md](FAMILY.md) for the spoke
registry, scope boundaries, and the shared standard every family list follows.
```

with (the new section replaces the pointer, it is not duplicated):

```markdown
## List family

This repo is the hub of a family of lists; the registry and family rules live in
[FAMILY.md](FAMILY.md).

| List | Scope | Status | Where the niche lives today |
|------|-------|--------|-----------------------------|
| awesome-mbse | Hub. Cross-cutting MBSE: methods, tool landscape, openable models, Magic Grid / Cameo | Live | This repo (hub and cross-cutting) |
| [awesome-sysml-v2](https://github.com/jgsystemsconsulting/awesome-sysml-v2) | SysML v2 the language: spec, parsers, editors, API clients, example models | Live | Linked public spoke; the only existing live spoke |
| awesome-magic-grid | Magic Grid method and Cameo practice | In development | Hub section Magic Grid and Cameo (no spoke URL) |
| awesome-archimate | ArchiMate 3.x, the Archi tool, EA modeling practice | Planned | GAP (no dedicated hub section) |
| awesome-capella | Capella tool and the Arcadia method | Planned | Broader Context Capella/Arcadia entries (thin) |
| awesome-requirements-engineering | Requirements as a discipline: EARS, KAOS, ReqIF, tooling, papers | Planned | GAP (absent) |
| awesome-digital-engineering | Digital thread, model-based definition, digital engineering transformation | Planned | GAP (absent) |
| awesome-stpa | STAMP / STPA and hazard analysis; functional safety methods | Planned | Model Gallery DLR-FT STPA library (one entry, thin) |

Gaps, snapshot 2026-09-17 (not a permanent census): requirements engineering and
digital engineering are absent from the hub; ArchiMate has no dedicated hub section;
STPA is one entry (the DLR-FT STPA library); Capella is four entries (the Arcadia
method page, the Arcadia primer, py-capellambse, Eclipse Capella).
```

Rules baked into this block: planned spoke names and `awesome-magic-grid` are plain text (never hyperlinked); Status cells use only the three-word vocabulary; visibility appears nowhere.

- [ ] **Step 3: Update the Contents list**

Replace the five Contents bullets with, in this order:

```markdown
- [List family](#list-family)
- [Magic Grid & Cameo / CATIA Magic](#magic-grid--cameo--catia-magic)
- [Model Gallery](#model-gallery)
- [Broader SysML / MBSE Context](#broader-sysml--mbse-context)
- [External awesome lists](#external-awesome-lists)
- [Support & security](#support--security)
```

- [ ] **Step 4: Replace `## The competitive landscape` with `## External awesome lists`**

Replace everything from the heading `## The competitive landscape` up to (not including) `## Contributing` with:

```markdown
## External awesome lists

Why this list exists, with evidence (gathered 2026-06): existing SysML/SE awesome-lists
are either abandoned, narrow, or carry no Cameo / Magic Grid coverage. No actively
maintained `awesome-mbse` with this breadth existed before this list.

- [mycr0ft/awesome-sysml](https://github.com/mycr0ft/awesome-sysml) - Community SysML v2 tools and samples list; thin on Magic Grid and openable Cameo models `SysMLv2` `external-list` (2025).
- [kktse/awesome-systems-engineering](https://github.com/kktse/awesome-systems-engineering) - Broad systems-engineering links, untouched since 2021; no MBSE depth `SE-general` `external-list` (2021).
- [rolling-robot/awesome-systems-engineering](https://github.com/rolling-robot/awesome-systems-engineering) - Minimal systems-engineering collection, stagnant since 2024; no MBSE coverage `SE-general` `external-list` (2024).

TODO: re-check the `awesome-capella` and `awesome-stpa` namespaces on launch day (both
were rate-limited on the 2026-09-17 list-family pass). Re-check `awesome-archimate`
(empty-ish on 2026-09-17), `awesome-requirements-engineering`, and
`awesome-digital-engineering` (probed in niche research) again on each create day.
```

- [ ] **Step 5: Verify**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
rg -n "^## (List family|External awesome lists)$" README.md             # expect 2 hits
rg -n "The competitive landscape|^\*\*List family:\*\*" README.md       # expect no output
rg -n "awesome-(archimate|capella|requirements-engineering|digital-engineering|stpa|magic-grid)" README.md | rg "\]\(https://github\.com/"
                                                                        # expect no output
rg -n "\| (Live|In development|Planned) \|" README.md | wc -l           # expect 8
rg -n "^- \[(List family|External awesome lists)\]" README.md           # expect 2 hits (Contents bullets)
awk '/^## Magic Grid & Cameo/{f=1;next} /^## /{f=0} f' README.md | grep -c '^- \['   # expect 35, unchanged
awk '/^## Model Gallery/{f=1;next} /^## /{f=0} f' README.md | grep -c '^| \['        # expect 24, unchanged
git diff -- README.md | rg "^\+" | rg "—"                               # expect no output (no new em dashes)
```

- [ ] **Step 6: Commit (local only, never push)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
git add README.md
git commit -m "docs(readme): list family table, external awesome lists, gap callouts"
```

**Done when:** Step 5 outputs all match, the counts from Step 1 are unchanged, and the commit exists locally.

---

### Task 3: STATUS.md for the awesome-magic-grid sibling

**Files:**
- Create: `C:/Users/gower/OneDrive/Documents/GitHub/awesome-magic-grid/STATUS.md`

**Interfaces:**
- Consumes: nothing from other tasks.
- Produces: the status note Task 1's magic-grid registry row and status note point to, and Task 5's acceptance 4 target.

**Model:** flash

- [ ] **Step 1: Create the file**

Write exactly:

```markdown
# Status: hub fork, not yet the awesome-magic-grid spoke

This repository is a local fork of the awesome-mbse hub, not the awesome-magic-grid
spoke. The README still carries the hub title and scope because it is generated output
(`scripts/generate.py` over `data/entries.yaml`). The family contract is `FAMILY.md` in
the awesome-mbse hub; nothing here overrides it.

Warning: hand edits to `README.md` are overwritten by the generator. That is why this
note is a separate file instead of a README edit.

TODO:

- [ ] Decide the final list name and re-check the `awesome-magic-grid` namespace on create day
- [ ] Prune `data/entries.yaml` to the Magic Grid niche, or retire the generator for hand maintenance
- [ ] Retitle the generated README to the final list name
- [ ] Create the private GitHub repo
- [ ] Register the spoke in awesome-mbse `FAMILY.md` and the hub README family table

STATUS.md is a private working note outside the family standard's required file list;
delete it at re-scope.
```

No content re-scope happens here: pruning `data/entries.yaml` or retitling is list-building, deferred to the TODOs.

- [ ] **Step 2: Verify**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-magic-grid"
test -f STATUS.md && echo OK                                            # expect OK
rg -n "local fork of the awesome-mbse hub|overwritten by the generator" STATUS.md   # expect 2 hits
rg -c "^- \[ \]" STATUS.md                                              # expect 5
rg -n "—" STATUS.md                                                     # expect no output
```

- [ ] **Step 3: Commit in the sibling repo (local only, never push)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-magic-grid"
git add STATUS.md
git commit -m "docs: add STATUS.md hub-fork note pending re-scope"
```

**Done when:** the file exists with the three required elements (hub-fork state, generator overwrite warning, re-scope TODOs) and the sibling commit exists locally.

---

### Task 4: Family pointer on the awesome-sysml-v2 public spoke

**Files:**
- Modify: `C:/Users/gower/OneDrive/Documents/GitHub/awesome-sysml-v2/README.md` (one blockquote line after the intro sentence)
- Modify (fallback branch only): `FAMILY.md` (first box of the live-spoke alignment checklist)

**Interfaces:**
- Consumes: Task 1's `### awesome-sysml-v2 live-spoke alignment` checklist (exact first-box text below).
- Produces: the acceptance-5 end state; Task 5 verifies whichever branch landed.

**Model:** standard

- [ ] **Step 1: Insert the pointer line**

In `../awesome-sysml-v2/README.md`, after the intro sentence `A curated list of OMG SysML v2 tools, example models, and learning resources.`, insert a blank line then:

```markdown
> Part of the awesome-mbse list family (hub repository currently private).
```

Text only: no URL, no FAMILY.md link. A hyperlink would 404 for public readers while the hub is private.

- [ ] **Step 2: Run the lint gate**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-sysml-v2"
npx awesome-lint@2.3.0 README.md
echo "exit=$?"
```

- [ ] **Step 3a: If the lint gate passed (exit 0), keep the line and commit**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-sysml-v2"
rg -n "jgsystemsconsulting/awesome-mbse" README.md     # expect no output (text-only pointer)
git add README.md
git commit -m "docs: add text-only awesome-mbse family pointer"
```

- [ ] **Step 3b: If the lint gate failed on the pointer line, drop it and record the TODO**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-sysml-v2"
git checkout -- README.md
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
```

Then in `FAMILY.md`, replace the alignment checklist's first box

```markdown
- [ ] Family pointer line present (text only while hub private)
```

with

```markdown
- [ ] TODO: add family pointer line (awesome-lint rejected the text-only line on 2026-09-17; re-add when the hub goes public)
```

and commit:

```bash
git add FAMILY.md
git commit -m "docs(family): record spoke pointer as TODO after awesome-lint rejection"
```

- [ ] **Step 4: Do not push in either branch**

The spoke is public and the user controls pushes. Leave both repos ahead of their remotes.

**Done when:** either the spoke README carries the text-only pointer, lint exits 0, and the spoke has a local commit; or the line is gone and FAMILY's alignment checklist records the pointer as an unchecked TODO.

---

### Task 5: Acceptance sweep against the spec

**Files:** none (read-only verification).

**Interfaces:**
- Consumes: all four prior tasks' outputs.

**Model:** flash

- [ ] **Step 1: Acceptance 1, 2, and 6 (hub README)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
rg -n "^## (List family|External awesome lists)$" README.md             # AC1: 2 hits
rg -n "^\*\*List family:\*\*" README.md                                 # AC1: no output
rg -n "\| (Live|In development|Planned) \|" README.md | wc -l           # AC1: 8, matches FAMILY
rg -n "awesome-(archimate|capella|requirements-engineering|digital-engineering|stpa|magic-grid)" README.md FAMILY.md | rg "\]\(https://github\.com/"
                                                                        # AC2: no output anywhere in either file
awk '/^## Magic Grid & Cameo/{f=1;next} /^## /{f=0} f' README.md | grep -c '^- \['   # AC6: 35, unchanged from baseline
awk '/^## Model Gallery/{f=1;next} /^## /{f=0} f' README.md | grep -c '^| \['        # AC6: 24, unchanged from baseline
```

- [ ] **Step 2: Acceptance 3 (FAMILY.md)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
rg -n "\| (private|public|local only|none yet)" FAMILY.md | wc -l       # expect 8 (one Visibility cell per registry row)
rg -n "^## (Private mode|External lists and namespaces)$" FAMILY.md     # expect 2 hits
rg -n "^### (awesome-(archimate|capella|requirements-engineering|digital-engineering|stpa)|awesome-magic-grid status note|awesome-sysml-v2 live-spoke alignment|Per-spoke create checklist template)" FAMILY.md
                                                                        # expect 8 hits (template + 5 create + status note + alignment)
rg -c "^- \[ \]" FAMILY.md                                              # expect 34 (or 34 with TODO wording if Task 4 fallback ran)
```

- [ ] **Step 3: Acceptance 4 and 5 (siblings)**

```bash
test -f "C:/Users/gower/OneDrive/Documents/GitHub/awesome-magic-grid/STATUS.md" && echo OK    # AC4: OK
rg -n "local fork|generator" "C:/Users/gower/OneDrive/Documents/GitHub/awesome-magic-grid/STATUS.md"   # AC4: hits
rg -n "jgsystemsconsulting/awesome-mbse" "C:/Users/gower/OneDrive/Documents/GitHub/awesome-sysml-v2/README.md"   # AC5: no output
git -C "C:/Users/gower/OneDrive/Documents/GitHub/awesome-sysml-v2" grep -n "jgsystemsconsulting/awesome-mbse"    # AC5: no output (tracked content; the two untracked docs/superpowers notes are not the public surface)
rg -n "Part of the awesome-mbse list family" "C:/Users/gower/OneDrive/Documents/GitHub/awesome-sysml-v2/README.md"
                                                                        # AC5: 1 hit on the keep branch; on the fallback branch expect no output here plus the TODO box in FAMILY (check: rg -n "re-add when the hub goes public" FAMILY.md)
```

- [ ] **Step 4: Acceptance 7 (negatives)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
git diff 4f7c0a6 --stat                                                 # expect README.md and FAMILY.md only (plus Task 4 fallback if it ran); no .github/ files
git status --porcelain=v1                                               # expect only "?? docs/" remaining
```

Process negatives, out of band: `gh repo edit --visibility` was never run; no sindresorhus submission PR was opened; no push command appears anywhere in this plan.

- [ ] **Step 5: Acceptance 8 (markers and em dashes)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
rg -n "GAP" README.md                                                   # hits must include the archimate, requirements-engineering, and digital-engineering rows
rg -c "TODO" README.md FAMILY.md                                        # at least 1 each (namespace re-check TODOs; planned-spoke checklists)
git diff 4f7c0a6 -- README.md FAMILY.md | rg "^\+" | rg "—"             # expect no output (zero new em dashes)
rg -n "—" "C:/Users/gower/OneDrive/Documents/GitHub/awesome-magic-grid/STATUS.md"   # expect no output
git -C "C:/Users/gower/OneDrive/Documents/GitHub/awesome-sysml-v2" diff | rg "^\+" | rg "—"   # expect no output
```

- [ ] **Step 6: Prose check on changed durable files**

```bash
python ~/.zcode/scripts/prose_check.py "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse/README.md" "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse/FAMILY.md" "C:/Users/gower/OneDrive/Documents/GitHub/awesome-magic-grid/STATUS.md"
```

Fix findings or justify them in the delivery note (copyright HTML comment `--` false positives may remain). No commit; nothing changes in this task.

**Done when:** every command shows its expected output. Any miss loops back to the owning task (1 through 4), never patched silently in Task 5.
