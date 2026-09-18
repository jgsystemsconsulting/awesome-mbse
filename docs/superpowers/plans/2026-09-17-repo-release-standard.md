# Repo Release Standard Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Give the awesome-mbse list family one durable public-release runbook (`docs/runbooks/family-public-release.md`), amend the FAMILY.md Private mode section to point at it and ship a text-only skeleton pointer, fix the live 404 family pointer in awesome-digital-engineering, and close or annotate the two backlog rows the spec names.

**Architecture:** Docs-only change set across two repos. The public DE spoke gets a one-line pointer fix through its protected-branch PR first, so the runbook can record it as applied. The hub (awesome-mbse) then gets the new runbook (Checklists A/B/C, pointer class grammar, decision-issue template, standing fixes), the FAMILY.md Private mode amendment, and the backlog edits. No visibility flips, no CI changes, no spoke list edits, no RR-B files.

**Tech Stack:** Markdown, git, gh CLI, grep, curl.

**Spec:** `docs/superpowers/specs/2026-09-17-repo-release-standard.md` (the plan argues from the spec; executors read both)

## Global Constraints

- **Idempotent execution.** If a task target already matches the desired end state (runbook exists, DE pointer fixed, FAMILY amended, backlog annotated), verify with the task's Expected checks and skip the write. Do not fail closed on missing old_string.
- **No visibility flips in this run.** Never run `gh repo edit --visibility` or any `--visibility public` command. Those commands appear in the runbook as documented human steps only; execution is always a later, per-repo, human decision recorded via a `Public release decision <YYYY-MM-DD>` issue.
- Docs and pointer edits only. No RR-B artifacts (`audit.py`, marketplace files, landing page), no CI workflow changes, no new spokes, no hub README body edits.
- No `sindresorhus/awesome` work beyond documenting Checklist C in the runbook. The runbook links the live PR template (`https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md`); it never forks their guidelines into this repo.
- **DE spoke branch protection:** `main` on `jgsystemsconsulting/awesome-digital-engineering` is protected (verified `true` via `gh api repos/jgsystemsconsulting/awesome-digital-engineering/branches/main --jq .protected` on 2026-09-17). DE changes go through a PR gated on the validate, lychee link-check, and awesome-lint workflows.
- **Hub main unprotected:** `main` on `jgsystemsconsulting/awesome-mbse` takes docs commits directly (verified `false` on 2026-09-17). Re-check with the same one-liner before each hub commit; if protection appears, use a branch, PR, and `gh pr checks --watch` instead of the direct commit.
- awesome-lint on DE must keep passing: Contents first, no Licence H2, no duplicate links. The Task 1 edit is one line above Contents and must not disturb those properties.
- **Runbook path is locked:** `docs/runbooks/family-public-release.md` in the hub repo. Not `docs/superpowers/` (durable maintainer documentation, not a process artifact).
- Preferred pointer strings are verbatim, everywhere they appear:
  - hub-private: `Part of the awesome-mbse list family (hub repository currently private).`
  - hub-public: `Part of the [awesome-mbse list family](https://github.com/jgsystemsconsulting/awesome-mbse/blob/main/FAMILY.md).`
- Registry vocabulary: Status is only `Live` | `In development` | `Planned`; Visibility is only `public` | `private` | `local only` | `none yet`. Never invent a fifth Visibility token.
- The DE fix lands in the sibling repo as its own branch, commit, and PR. Hub edits commit in the hub repo. Never mix the two in one commit.
- New prose carries no em dashes. The single exception is the exception-row format quoted verbatim from the reviewed spec (`Exception: <repo> remains private — <reason> — <YYYY-MM-DD>`), which is data format, not prose.
- Commit style: conventional prefixes (`docs:`, `fix:`), matching both repos' existing logs.

## Codebase context

Context doc: `docs/superpowers/context/2026-09-17-repo-release-standard-context.md`. Facts this plan relies on, verified in the workspace on 2026-09-17:

- FAMILY.md already carries the Private mode rules this plan amends (default private, text-only pointers while hub private, sindresorhus deferred, sweep unchanged by privacy). The registry Visibility column is the source of truth for the live mix: hub private; sysml-v2, archimate, capella, DE public; RE and stpa Live but private; magic-grid local only.
- Pointer audit of local checkouts (grep-verified): sysml-v2, capella, archimate, RE, stpa, and DE are text-only / preferred hub-private class (DE fixed). The violation's generator was the README skeleton in FAMILY.md; Task 2 fixes the skeleton. If a task's exact-replace old_string is already gone, treat that step as done and continue.
- Sibling checkouts present: sysml-v2, archimate, capella, DE, magic-grid, RE, stpa, plus stray `awesome-*;C` / `;D` directories with no README (the recurring grep glob skips them).
- The user-scope `release-repo-standard` skill is the RR-B product-repo standard (legal, marketplace, landing page, audit tooling). Pure CC0 link lists take none of it; this plan grows no RR-B files.
- DE has CI (`link-check-pr.yml`, `link-check-schedule.yml`, `validate.yml`), so a PR runs real checks before the fix lands. Hub verification is grep-based (no root markdownlint). If `docs/runbooks/family-public-release.md` already exists and matches the embed, Task 1 is verify-only.
- Backlog rows `list-family-private-structure-4` (line 11) and `awesome-requirements-engineering-1` (line 18) in `docs/superpowers/backlog.md` are the open items this plan closes or annotates. The table has 5 columns (`id | title | source | status | evidence`); observed statuses are `open` and `needs-info`; this plan introduces `done` as the terminal status for a closed row.

## Research

Research doc: `docs/superpowers/research/2026-09-17-repo-release-standard-research.md`

- https://github.com/sindresorhus/awesome (list-of-lists submission target, post-hub-public only, documented in Checklist C)
- https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md (live submission template; linked, never forked)
- Confirmed in research: public spokes resolve without auth; the FAMILY.md URL on the private hub 404s for anonymous readers, which is the basis for the text-only rule.

research: internal-primary + sindresorhus/awesome pointers (see research doc and URLs above).

---

### Task 1: Fix the awesome-digital-engineering family pointer (sibling repo, protected PR)

**Files:**
- Modify: `../awesome-digital-engineering/README.md` line 8 (grep-verified as the only `awesome-mbse/blob` hit in any sibling README)

**Interfaces:**
- Consumes: the preferred hub-private string from Global Constraints.
- Produces: zero FAMILY.md hyperlinks from public spokes while the hub is private; the standing fix the Task 2 runbook records as applied 2026-09-17.

**Model:** flash

Note: the spec's touch list says "two pointer lines to text-only". The DE README carries the hyperlink on one physical line 8; the second hyperlinked pointer line the spec counts is the FAMILY.md README skeleton, fixed in Task 3. Do not hunt for a second DE line; fix line 8 and verify nothing else matches.

- [ ] **Step 1: Sync DE main and branch**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-digital-engineering"
git checkout main
git pull origin main
git checkout -b fix/family-pointer-text-only
```

Expected: main up to date, clean tree, new branch created.

- [ ] **Step 2: Edit the pointer line**

In `README.md`, replace:

```markdown
Part of the [awesome-mbse list family](https://github.com/jgsystemsconsulting/awesome-mbse/blob/main/FAMILY.md).
```

with:

```markdown
Part of the awesome-mbse list family (hub repository currently private).
```

- [ ] **Step 3: Verify locally before pushing**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-digital-engineering"
grep -c "awesome-mbse/blob" README.md
grep -n "awesome-mbse list family" README.md
npx --yes awesome-lint README.md
```

Expected: `0` blob-URL hits; exactly one text-only pointer line; awesome-lint passes (Contents first, no Licence H2, no duplicate links; all preserved by a one-line swap above Contents).

- [ ] **Step 4: Commit, push, open PR, let CI run**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-digital-engineering"
git add README.md
git commit -m "fix: family pointer text-only while hub repository is private"
git push -u origin fix/family-pointer-text-only
gh pr create -R jgsystemsconsulting/awesome-digital-engineering \
  -t "Family pointer: text-only while hub is private" \
  -b "Removes a live 404 for anonymous readers: the family pointer hyperlinked the private hub's FAMILY.md blob, which resolves only for authenticated org members. Text-only pointer per the hub family standard (FAMILY.md Private mode, jgsystemsconsulting/awesome-mbse). Standing fix, applied at runbook creation."
gh pr checks --watch
```

Expected: link-check-pr and validate workflows pass on the PR.

- [ ] **Step 5: Merge and sync**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-digital-engineering"
gh pr merge --squash --delete-branch
git checkout main
git pull
grep -c "awesome-mbse/blob" README.md
curl -s -o /dev/null -w "%{http_code}\n" https://github.com/jgsystemsconsulting/awesome-digital-engineering
```

Expected: PR merged; local main matches origin; `0` blob-URL hits on main; curl prints `200`. If push or PR creation fails on permissions, stop and report to the maintainer; do not commit directly to a protected main as a workaround.

### Task 2: Create the family public-release runbook

**Files:**
- Create: `docs/runbooks/family-public-release.md` (directory `docs/runbooks/` does not exist yet)

**Interfaces:**
- Produces: the runbook path `docs/runbooks/family-public-release.md`, consumed by Task 3 (FAMILY.md link), Task 4 (backlog evidence cells), and every future release.

**Model:** flash

- [ ] **Step 1: Write the runbook**

Create `docs/runbooks/family-public-release.md` with exactly this content:

````markdown
# Family public release runbook

This runbook takes awesome-mbse family repos from private to public: one spoke at a
time, the hub itself, and the sindresorhus/awesome submission that follows a hub
release. It exists so a release is a checklist execution instead of a re-derivation of
rules that used to live in chat.

Two gates run through everything:

- **Spoke-public gate (Checklist A):** one family repo's own visibility flip, private
  to public.
- **Hub-public gate (Checklist B):** the hub's flip, which is also the unlock that
  lets public spokes hyperlink `FAMILY.md` instead of using a text-only family
  pointer.

Every visibility flip in this runbook is a human decision executed by hand. No command
below is automated, batched, or wired into CI.

## Pointer class grammar

A spoke's family pointer line is one of two classes. The class is what greps enforce;
the preferred string is what new writes use.

**Class hub-private (text-only):** no `FAMILY.md` URL and no `awesome-mbse/blob`
hyperlink. Preferred line:

```
Part of the awesome-mbse list family (hub repository currently private).
```

Existing text-only variants that name the hub without a URL (awesome-sysml-v2,
awesome-capella, awesome-archimate, awesome-requirements-engineering) stay compliant
until the next edit to that spoke, then normalize to the preferred line. Hyperlinks to
the private hub are non-compliant.

**Class hub-public (hyperlink):** preferred line:

```
Part of the [awesome-mbse list family](https://github.com/jgsystemsconsulting/awesome-mbse/blob/main/FAMILY.md).
```

Mapping: while hub Visibility is `private`, every **public** spoke must be class
hub-private. After the hub goes public, every **public** spoke must be class
hub-public. Private spokes may keep a text-only line until they themselves go public
(Checklist A then picks the class from current hub visibility).

## Decision issue template

Before any `gh repo edit --visibility` command (DOC-ONLY in this plan; human later), open a GitHub issue in the repo being
flipped. Title: `Public release decision <YYYY-MM-DD>`. Body:

```markdown
- Decision: public
- Decision date: YYYY-MM-DD
- Decision maker: <github-login>
- Reason: <one line>
```

Command, with the date and repo filled in:

```bash
gh issue create -R jgsystemsconsulting/<repo> \
  -t "Public release decision <YYYY-MM-DD>" \
  -b "- Decision: public
- Decision date: <YYYY-MM-DD>
- Decision maker: <github-login>
- Reason: <one line>"
```

Keep the issue open until the flip and the hub registry/README edits land, then close
it. Each flip also gets a CHANGELOG note in the repo that flipped. If gh rejects the
`--accept-visibility-change-consequences` flag below, check `gh repo edit --help` for
the current flag name before running anything.

## Checklist A: spoke public release

Example in flight: awesome-requirements-engineering (Live, private, 40 entries as of
2026-09-17). Run top to bottom; do not flip until every box above the flip is ticked.

- [ ] CI green on default branch: link check, scheduled sweep, markdown lint,
      awesome-lint (`gh run list --limit 5` in the spoke checkout).
- [ ] Every entry link passes the public-availability bar; no private-only resources
      anywhere in the list (the jgs-magic-sysmlv2-mcp CHANGELOG removal is the
      precedent).
- [ ] README matches the family skeleton: Awesome badge, sweep badge, one-line scope,
      table of contents.
- [ ] Family pointer class matches current hub visibility. Hub still private: class
      hub-private (preferred string or a compliant text-only variant; no FAMILY.md
      URL). Hub already public: class hub-public (preferred hyperlink). Fix any
      wrong-class pointer before the flip.
- [ ] No machine-local paths, maintainer-only draft notes, or untracked dumps in
      tracked files:

  ```bash
  git grep -nIE "C:\\\\Users|/Users/|OneDrive" -- .
  git grep -nwIE "TODO|WIP" -- .
  git status --porcelain
  ```

  Fail the check if any appear in tracked files. Expected: no output from either
  grep and no unexpected untracked files.
- [ ] Decision issue filed (template above), then, by hand:

  ```bash
  gh repo edit jgsystemsconsulting/awesome-<niche> --visibility public --accept-visibility-change-consequences
  ```
- [ ] Anonymous access verified: the repo URL and every README link resolve logged
      out.

  ```bash
  curl -s -o /dev/null -w "%{http_code}\n" https://github.com/jgsystemsconsulting/awesome-<niche>
  ```

  Expect 200. A 404 means the flip did not take; README links are covered by the CI
  lychee job on the default branch.
- [ ] Hub edits: FAMILY.md registry Visibility cell private to public; hub README
      family table row gains the spoke URL (was name-only with a location note).
      Status stays `Live`.
- [ ] CHANGELOG note in the spoke recording the release date; close the decision
      issue (`gh issue close <number> -R jgsystemsconsulting/awesome-<niche> -c "Released <YYYY-MM-DD>."`).

## Checklist B: hub public release plus pointer unlock

Gate, then flip, then unlock.

- [ ] Coherence bar met: every registry row with Status `Live` has Visibility
      `public`, or a Live private row is listed under a registry footnote or the
      planned-spoke note block as `Exception: <repo> remains private — <reason> — <YYYY-MM-DD>`
      (Visibility cell stays `private`; never invent a fifth Visibility token). A hub
      that 404s its own family table from an anonymous browser is not coherent.
      `In development` and `Planned` rows stay name-only and do not block.
- [ ] Hub README family table consistent: public spokes linked, private exceptions
      name-only, `In development` / `Planned` rows name-only.
- [ ] Hub CI green; sweep badge current; no private-only entries in hub list bodies.
- [ ] Decision issue filed in the hub (template above), then, by hand:

  ```bash
  gh repo edit jgsystemsconsulting/awesome-mbse --visibility public --accept-visibility-change-consequences
  ```
- [ ] FAMILY.md resolves logged out:

  ```bash
  curl -s -o /dev/null -w "%{http_code}\n" https://github.com/jgsystemsconsulting/awesome-mbse/blob/main/FAMILY.md
  ```

  Expect 200.
- [ ] Pointer unlock sweep: in every **public** spoke README, set the class
      hub-public preferred hyperlink. One commit per spoke, same day. Private spokes
      unchanged.
- [ ] Registry: hub row Visibility private to public. CHANGELOG note in the hub;
      close the decision issue.
- [ ] Close backlog row `list-family-private-structure-4` in
      `docs/superpowers/backlog.md` (status to `done`).

## Checklist C: sindresorhus/awesome submission (per list, after hub public)

- [ ] Prerequisites: hub public, public-spoke pointer unlock done, the list stable:
      last full sweep badge current, CI green, and either at least 40 inclusion-bar
      entries (the family Starting-a-new-list bar) or the README carries the honest
      growth label line exactly:

  ```
  > Initial seed; growth in progress. Entry count is under the family 40+ bar on purpose.
  ```

  placed immediately under the family pointer. The maintainer sets it; remove it when
  the count clears 40.
- [ ] Submit per the live PR template:
      https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md
      (link the template; never fork their guidelines into this repo).
- [ ] Target: https://github.com/sindresorhus/awesome
- [ ] Record the submission (date, PR link) in the spoke CHANGELOG.

## Standing fixes

- **DE drift fix (applied 2026-09-17, before any flip):**
  `awesome-digital-engineering/README.md` hyperlinked the private hub's FAMILY.md,
  which 404s for anonymous readers. Replaced with the preferred class hub-private
  text-only line.
- **Recurring check (run at each sweep):** from a workspace that has the hub plus
  sibling spoke checkouts (`../awesome-*/`):

  ```bash
  grep -rn "FAMILY.md\|awesome-mbse/blob\|awesome-mbse list family" ../awesome-*/README.md
  ```

  Confirm every public spoke is the correct class for current hub visibility: no
  private-hub URL while the hub is private; the preferred hyperlink after the hub is
  public. If sibling checkouts are missing, clone each Live public spoke shallow once
  (`git clone --depth 1 https://github.com/jgsystemsconsulting/<repo>`), then run the
  same grep.
````

- [ ] **Step 2: Verify the runbook content**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
grep -c "^## Checklist" docs/runbooks/family-public-release.md
grep -n "Pointer class grammar\|Decision issue template\|Standing fixes" docs/runbooks/family-public-release.md
grep -c "Part of the awesome-mbse list family (hub repository currently private)." docs/runbooks/family-public-release.md
grep -c "Initial seed; growth in progress. Entry count is under the family 40+ bar on purpose." docs/runbooks/family-public-release.md
grep -n "human decision executed by hand" docs/runbooks/family-public-release.md
grep -n "—" docs/runbooks/family-public-release.md
```

Expected: `3` checklists; one match line each for the three section headers; at least
`1` for the hub-private preferred string; `1` for the growth label; one hit for the
human-decision sentence; the em-dash grep shows only the exception-row line from
Checklist B (spec-quoted data format).

- [ ] **Step 3: Commit**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
gh api repos/jgsystemsconsulting/awesome-mbse/branches/main --jq .protected
git add docs/runbooks/family-public-release.md
git commit -m "docs: add family public-release runbook (spoke, hub, sindresorhus checklists)"
git push origin main
```

Expected from the protection check: `false`, so the direct commit lands. If it prints
`true`, stop before committing: branch `docs/family-release-runbook`, push, `gh pr create --fill`,
`gh pr checks --watch`, `gh pr merge --squash --delete-branch`.

### Task 3: Amend FAMILY.md Private mode and the README skeleton

**Files:**
- Modify: `FAMILY.md` (Private mode section, lines 31-42; README skeleton family pointer, lines 241-242)

**Interfaces:**
- Consumes: `docs/runbooks/family-public-release.md` from Task 2 (link target must exist before this commit lands).
- Produces: FAMILY.md as the family's pointer to the runbook; the skeleton that ships text-only by default, so new spokes cannot reproduce the DE violation.

**Model:** flash

- [ ] **Step 1: Point the sindresorhus bullet at the runbook and add the Status/Visibility and gates additions**

In `FAMILY.md`, replace this exact block:

```markdown
- The `sindresorhus/awesome` submission step is deferred to the future public-release
  runbook; it is not part of private-structure work.
- Sweep badges, CI, and cadence are unchanged by privacy.
```

with:

```markdown
- The `sindresorhus/awesome` submission step is deferred to the public-release runbook
  (`docs/runbooks/family-public-release.md`, Checklist C); it is not part of
  private-structure work.
- Sweep badges, CI, and cadence are unchanged by privacy.
- Status is content maturity (`Live` / `In development` / `Planned`); Visibility is who
  can open the repo (`public` / `private` / `local only` / `none yet`). They flip
  independently; a spoke going public does not move the hub.
- Two gates govern release, and the full procedure lives in
  `docs/runbooks/family-public-release.md`: spoke-public (Checklist A) is one repo's
  own private-to-public flip; hub-public (Checklist B) flips the hub and also unlocks
  `FAMILY.md` hyperlinks in public spokes.
```

- [ ] **Step 2: Fix the skeleton family pointer**

In the same file's README skeleton, replace:

```markdown
Part of the [awesome-mbse list
family](https://github.com/jgsystemsconsulting/awesome-mbse/blob/main/FAMILY.md).
```

with:

```markdown
Part of the awesome-mbse list family (hub repository currently private).
<!-- Hub public unlock: replace the line above with
     Part of the [awesome-mbse list family](https://github.com/jgsystemsconsulting/awesome-mbse/blob/main/FAMILY.md). -->
```

New spokes created while the hub is private now get the compliant text-only default,
with the post-unlock hyperlink preserved as a comment.

- [ ] **Step 3: Verify the edits**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
grep -c "runbooks/family-public-release" FAMILY.md
grep -n "Status is content maturity" FAMILY.md
grep -c "Spoke-public gate\|spoke-public (Checklist A)" FAMILY.md
grep -n "awesome-mbse/blob/main/FAMILY.md" FAMILY.md
grep -n "future public-release" FAMILY.md
```

Expected: two `runbooks/family-public-release.md` references (sindresorhus bullet and
gates bullet); one Status/Visibility line; at least one gate mention; exactly one
`awesome-mbse/blob/main/FAMILY.md` hit, inside the skeleton HTML comment; zero
`future public-release` hits.

- [ ] **Step 4: Commit**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
gh api repos/jgsystemsconsulting/awesome-mbse/branches/main --jq .protected
git add FAMILY.md
git commit -m "docs: amend private mode for release gates and text-only skeleton pointer"
git push origin main
```

Expected: protection check `false`; direct commit lands. If `true`, use the PR flow
from Task 2 Step 3.

### Task 4: Close and annotate the backlog rows

**Files:**
- Modify: `docs/superpowers/backlog.md` (rows `list-family-private-structure-4` at line 11 and `awesome-requirements-engineering-1` at line 18)

**Interfaces:**
- Consumes: the runbook path from Task 2 (evidence cells point at it).

**Model:** flash

- [ ] **Step 1: Annotate `list-family-private-structure-4`**

Replace:

```markdown
| list-family-private-structure-4 | Make hub public when family coherent; then allow FAMILY URL from public spokes | list-family-private-structure | open | FAMILY.md Private mode |
```

with:

```markdown
| list-family-private-structure-4 | Make hub public when family coherent; then allow FAMILY URL from public spokes | list-family-private-structure | open | Runbook ready: docs/runbooks/family-public-release.md (Checklist B); flip pending human decision |
```

The row stays `open`: it closes only when the hub flip actually happens (Checklist B,
last box).

- [ ] **Step 2: Close `awesome-requirements-engineering-1`**

Replace:

```markdown
| awesome-requirements-engineering-1 | Public-release runbook for private RE spoke (FAMILY public flip) | awesome-requirements-engineering | open | FAMILY.md private-mode; plan deferred public |
```

with:

```markdown
| awesome-requirements-engineering-1 | Public-release runbook for private RE spoke (FAMILY public flip) | awesome-requirements-engineering | done | docs/runbooks/family-public-release.md (closed 2026-09-17 by repo-release-standard; Checklist A is the RE public-release path) |
```

- [ ] **Step 3: Verify and commit**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
grep -n "list-family-private-structure-4\|awesome-requirements-engineering-1" docs/superpowers/backlog.md
gh api repos/jgsystemsconsulting/awesome-mbse/branches/main --jq .protected
git add docs/superpowers/backlog.md
git commit -m "docs: close RE public-release runbook row; annotate hub-public row runbook-ready"
git push origin main
```

Expected: row 4 shows `open` with the runbook evidence; RE row shows `done`;
protection check `false` (else PR flow from Task 2 Step 3).

### Task 5: Verification sweep from the hub workspace

**Files:** none edited (Step 5 wording fixes are the only permitted edits)

**Interfaces:**
- Consumes: Tasks 1-4 complete.

**Model:** standard

- [ ] **Step 1: Run the recurring pointer grep**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
grep -rn "FAMILY.md\|awesome-mbse/blob\|awesome-mbse list family" ../awesome-*/README.md
```

Expected while the hub is private (state verified 2026-09-17):

| Repo checkout | Expected matches |
|---|---|
| awesome-sysml-v2 | line 5, text-only blockquote variant |
| awesome-capella | lines 7-9, text-only with Private mode citation |
| awesome-archimate | lines 8-9, text-only naming the hub repo |
| awesome-requirements-engineering | line 7, text-only variant |
| awesome-digital-engineering | line 8, now the preferred text-only line (Task 1 landed) |
| awesome-stpa | line 9, text-only (Live private spoke; no FAMILY.md blob URL; no action while private) |
| awesome-magic-grid | prose mention only, no family pointer (local only) |
| `awesome-*;C` / `;D` stray directories | no README, no match |

Zero `awesome-mbse/blob` hits anywhere. Any blob-URL hit in a public spoke is a
regression of the DE drift; fix it with the Task 1 procedure in that repo.

- [ ] **Step 2: Confirm no public spoke hyperlinks FAMILY.md**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
grep -rln "awesome-mbse/blob" ../awesome-*/README.md
```

Expected: no output. This is the spec's acceptance check for the DE fix.

- [ ] **Step 3: Confirm the hub wiring**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
grep -n "runbooks/family-public-release" FAMILY.md docs/superpowers/backlog.md
grep -n "awesome-requirements-engineering-1.*done" docs/superpowers/backlog.md
ls docs/runbooks/family-public-release.md
```

Expected: FAMILY.md two references; backlog rows 4 (evidence) and 18 (done); the
runbook file exists.

- [ ] **Step 4: Check registry, hub README table, and actual visibility agree**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
for r in awesome-mbse awesome-sysml-v2 awesome-archimate awesome-capella awesome-requirements-engineering awesome-digital-engineering awesome-stpa; do printf "%s: " "$r"; gh repo view "jgsystemsconsulting/$r" --json visibility -q .visibility; done
```

Expected: `awesome-mbse` PRIVATE; `awesome-sysml-v2`, `awesome-archimate`,
`awesome-capella`, `awesome-digital-engineering` PUBLIC;
`awesome-requirements-engineering` and `awesome-stpa` PRIVATE. Compare against the FAMILY.md registry
Visibility column and the hub README family table. Read-only: report any disagreement
to the maintainer rather than editing or flipping; a stale cell is drift for a future
pass, not this plan's scope.

- [ ] **Step 5: Fresh-reader pass on Checklist A**

Read `docs/runbooks/family-public-release.md` Checklist A end to end as someone who has
never seen the spec, imagining the RE spoke as the target. Confirm every box is clear
enough to execute later. **Dry-read only: do not run any `gh repo edit --visibility`
command or open a public-release decision issue in this plan.** Every box must be executable
from the runbook plus FAMILY.md alone, by command or by reading a named file. Fix
wording gaps found (small edits, then commit with `docs: runbook clarity fixes` after
the protection check); if a gap needs new content beyond wording, stop and report it
instead of growing the runbook past the spec.

## Out of scope reminders for executors

- Do not run `gh repo edit --visibility` on any repo. Those commands exist only as runbook text.
- Do not touch `../awesome-requirements-engineering`, `../awesome-sysml-v2`, `../awesome-capella`, `../awesome-archimate`, `../awesome-stpa`, or `../awesome-magic-grid`. They are compliant or out of scope.
- Do not add RR-B artifacts (audit scripts, marketplace metadata, landing pages) anywhere.
- Do not fork the sindresorhus PR template into this repo.
- Do not submit anything to sindresorhus/awesome. The hub is private; Checklist C documents the step for later.
