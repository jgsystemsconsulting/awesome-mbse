# Landing Truth Gate Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Wire the existing release gate (`scripts/check_release.py`) into CI and document the landing page's gate inputs so a hub page that lies cannot merge green.

**Architecture:** One new GitHub Actions workflow runs the stdlib-only gate on every push and PR against main. One checkbox in the PR template and one new CONTRIBUTING.md section tell contributors, before the first red run, exactly which landing-page bits are gate inputs. The gate script itself is never touched.

**Tech Stack:** GitHub Actions (pinned SHAs), Python 3.12, stdlib only. No dependency install anywhere in the new workflow.

**Spec:** `docs/superpowers/specs/2026-09-18-landing-truth-gate.md`

**Research:** research: skipped (internal CI workflow wire-up and maintainer write-path note; no external API or version-sensitive library choice)

## Global Constraints

- No changes to `scripts/check_release.py` logic, ever (spec non-goal and acceptance criterion 5). It is byte-identical at the end of this work to its state at the start.
- No changes to `.github/workflows/link-check-pr.yml`, `.github/workflows/link-check-schedule.yml`, or lychee configuration (spec non-goal).
- Action pins are copied verbatim, SHA plus version comment: `actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4` and `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065 # v5`. Manual bumps only; no Dependabot.
- The workflow job check-run name must be exactly `validate`; branch protection will match that string later (repo settings act, out of scope for files).
- Chip `<dt>` names are matched exactly by the gate: `version`, `sweep`, `entries`. Never renamed in docs.
- Six section-index fragments in fixed order: `list-family`, `magic-grid--cameo--catia-magic`, `model-gallery`, `broader-sysml--mbse-context`, `external-awesome-lists`, `support--security`.
- Repo state note: at plan time `docs/index.html` and `scripts/check_release.py` are untracked files on branch `feat/pages-landing-and-packages` (in-flight package work). The break test in Task 4 must revert `docs/index.html` by exact text edit, never `git checkout` (there is no committed baseline to restore from).
- Written prose standard applies to the CONTRIBUTING.md section: no em dashes.

---

### Task 1: Baseline hash and new CI workflow `.github/workflows/validate.yml`

**Files:**
- Create: `.github/workflows/validate.yml`
- Read-only: `scripts/check_release.py` (hash recorded, never edited)

**Interfaces:**
- Consumes: `scripts/check_release.py` (already on disk, passes locally today as `release gate: PASS`).
- Produces: a `validate` check run on every push and PR against main. Task 4 relies on this workflow existing when the CI-level break test is run later.

**Model:** flash

- [ ] **Step 1: Record the baseline hash of the gate script**

Run from the repo root:

```bash
python -c "import hashlib; print(hashlib.sha256(open('scripts/check_release.py','rb').read()).hexdigest())"
```

Copy the printed hex digest into the task notes (or the PR description). Task 5 compares against this value to prove the script was never touched.

Also confirm the gate is green before starting:

```bash
python scripts/check_release.py
```

Expected: `release gate: PASS (scanned N files)` and exit code 0. If it fails, stop: the baseline is broken and the spec's premises do not hold.

- [ ] **Step 2: Create `.github/workflows/validate.yml` with exactly this content**

```yaml
name: validate

# Landing truth gate: the chips in docs/index.html (version, sweep, entries)
# and the six-link section index must match their sources (RELEASE-INFO.txt,
# README.md). See CONTRIBUTING.md section 11. Spec: landing truth gate.

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: read

jobs:
  validate:
    # The check-run name branch protection must match. Setting both the job id
    # and name: keeps the run named "validate" regardless of job-key display.
    name: validate
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4
      - uses: actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065 # v5
        with:
          python-version: "3.12"
      - name: Release gate
        run: python scripts/check_release.py
```

- [ ] **Step 3: Verify the YAML parses and the triggers, pins, and run step are present**

Run:

```bash
python -c "import yaml; yaml.safe_load(open('.github/workflows/validate.yml')); print('yaml ok')"
grep -c "11d5960a326750d5838078e36cf38b85af677262\|a26af69be951a213d495a4c3e4e4022e16d87065" .github/workflows/validate.yml
grep -n "python-version: \"3.12\"\|python scripts/check_release.py\|workflow_dispatch\|contents: read" .github/workflows/validate.yml
```

Expected: `yaml ok`; grep count `2` (both SHAs); the second grep shows all four lines. If PyYAML is missing in the execution environment, skip that one command; the push-time syntax check in Step 5 covers it.

- [ ] **Step 4: Run the local gate once more (the new file must not disturb it)**

Run: `python scripts/check_release.py`
Expected: `release gate: PASS (scanned N files)`, exit 0.

- [ ] **Step 5: Commit**

```bash
git add .github/workflows/validate.yml
git commit -m "ci: add validate workflow running the release gate on main"
```

After push, the Actions tab shows the workflow running green on the PR that introduces it (spec acceptance criterion 2). If the run fails for a workflow-syntax reason, fix `validate.yml` only; do not touch the gate script.

---

### Task 2: PR template Housekeeping checkbox

**Files:**
- Modify: `.github/PULL_REQUEST_TEMPLATE.md` (Housekeeping section, currently the last section, lines 28-31)

**Interfaces:**
- Consumes: nothing from Task 1 at runtime; the checkbox text references CONTRIBUTING.md section 11, which Task 3 creates. Land Task 3 in the same PR so the reference resolves.
- Produces: contributor-facing warning that chip/heading/count changes must be mirrored in `docs/index.html`.

**Model:** flash

- [ ] **Step 1: Add one checkbox to the Housekeeping list**

The section currently ends with:

```markdown
## Housekeeping

- [ ] If a **top-level** section was added/renamed, updated the hand-maintained `## Contents` ToC
- [ ] (If a JGS product) it sits next to ≥1 competing/alternative entry (CONTRIBUTING.md §7)
```

Append after the last item:

```markdown
- [ ] If a chip value, section heading, or entry count changed, updated `docs/index.html` to match (CI runs `scripts/check_release.py`; see CONTRIBUTING.md §11)
```

- [ ] **Step 2: Verify the checkbox landed in the right list**

Run: `grep -n "check_release" .github/PULL_REQUEST_TEMPLATE.md`
Expected: exactly one hit, inside the `## Housekeeping` section, and it is the file's only mention of the script.

- [ ] **Step 3: Commit**

```bash
git add .github/PULL_REQUEST_TEMPLATE.md
git commit -m "docs: add landing-truth checkbox to PR template Housekeeping"
```

---

### Task 3: CONTRIBUTING.md section 11 "Landing page truth"

**Files:**
- Modify: `CONTRIBUTING.md` (append after section 10 "Maintenance cadence", currently the final section)

**Interfaces:**
- Consumes: the exact gate inputs read from `scripts/check_release.py` (already merged into the branch) and the checkbox from Task 2 that points here.
- Produces: the maintainer write-path note the spec requires; the PR template references `§11`.

**Model:** flash

- [ ] **Step 1: Append the section verbatim after section 10**

```markdown
## 11. Landing page truth

`docs/index.html` makes claims the CI `validate` workflow checks on every PR
(`python scripts/check_release.py`). Know the inputs before you edit.

**Chips.** The three `<dt>` names `version`, `sweep`, and `entries` are matched
exactly by the gate. Do not rename them. Their `<dd>` values are compared against
fixed sources:

- `version` vs the `Version:` line in `RELEASE-INFO.txt`
- `sweep` vs the README `![Last full sweep: YYYY-MM]` badge
- `entries` vs the count of grammar-valid curated bullets

Curated bullets counted for the entries chip live only under these three README
`##` sections: *Magic Grid & Cameo / CATIA Magic*, *Broader SysML / MBSE Context*,
*External awesome lists*. The Model Gallery is a pointer table and is not counted.

**Section index.** The landing page's `<ul class="section-index">` must contain
exactly six links whose href fragments equal the GitHub slugs of the six
product-section README headings, in this fixed order:

1. `#list-family` (List family)
2. `#magic-grid--cameo--catia-magic` (Magic Grid & Cameo / CATIA Magic)
3. `#model-gallery` (Model Gallery)
4. `#broader-sysml--mbse-context` (Broader SysML / MBSE Context)
5. `#external-awesome-lists` (External awesome lists)
6. `#support--security` (Support & security)

Renaming one of these README headings fails the gate by design. If you must
rename, update `docs/index.html` in the same PR; for indexed headings, keeping
the title stable is usually the better fix.

**Display text is free.** The gate reads names, values, and href fragments only.
The visible labels around chip values and the section-index link text can be
edited without touching the gate.
```

- [ ] **Step 2: Verify structure and the em-dash bar**

Run:

```bash
grep -n "^## " CONTRIBUTING.md
grep -n "—" CONTRIBUTING.md | sed -n '1,40p'
```

Expected: `## 11. Landing page truth` is the last `##` heading; the em-dash grep shows no hits introduced inside section 11 (pre-existing em dashes elsewhere in the file are out of scope for this task).

- [ ] **Step 3: Commit**

```bash
git add CONTRIBUTING.md
git commit -m "docs: add CONTRIBUTING section 11 landing page truth"
```

---

### Task 4: Local break test proving the gate bites

**Files:**
- Modify temporarily: `docs/index.html` (line ~441, `<dd>85</dd>` under `<dt>entries</dt>`), then revert

**Interfaces:**
- Consumes: the gate from `scripts/check_release.py` and the current entries chip value `85` (curated count is also 85 today, verified by the passing baseline in Task 1).
- Produces: recorded evidence (command output) that a chip drift yields exit 1 with the expected line, and that revert restores exit 0. Covers spec acceptance criteria 3 (local equivalent) and 6.

**Model:** flash

- [ ] **Step 1: Sanity-check the baseline before breaking**

Run: `python scripts/check_release.py`
Expected: `release gate: PASS (scanned N files)`, exit 0. If this fails, stop and fix the baseline first; a break test against a red baseline proves nothing.

- [ ] **Step 2: Break the entries chip from 85 to 84**

Edit `docs/index.html`: replace the exact string

```html
<dt>entries</dt>
            <dd>85</dd>
```

with the same lines but `<dd>84</dd>`. Use the editor's exact-match replace; the whitespace between the `</dt>` and `<dd>` line is whatever the file already has.

- [ ] **Step 3: Run the gate and verify it exits 1 with the expected line**

Run:

```bash
python scripts/check_release.py; echo "exit=$?"
```

Expected: exit code 1, and output containing exactly:

```text
  - landing entries chip 84 != curated count 85
```

Save this output in the PR description as break-test evidence.

- [ ] **Step 4: Revert by exact text edit (never git checkout; the file is untracked)**

Edit `docs/index.html` back: `<dd>84</dd>` to `<dd>85</dd>`.

Then verify the revert:

```bash
grep -n "<dd>85</dd>" docs/index.html
python scripts/check_release.py; echo "exit=$?"
```

Expected: the `<dd>85</dd>` line present again under the entries chip; `release gate: PASS (scanned N files)`; exit 0.

- [ ] **Step 5: Confirm nothing from this task is left to commit**

Run: `git status --porcelain -- docs/index.html`
Expected: `?? docs/index.html` (still untracked, as before) and no diff to revert. No commit for this task; it produces evidence only.

Note for the CI-level proof (spec acceptance criterion 3, full form): after this PR opens, push a follow-up commit changing the chip to 84 on the PR branch, let the `validate` run fail with the same line (or use workflow_dispatch on that commit), then push the revert and watch it go green. The local test above is the required minimum; the CI run is the belt-and-braces confirmation.

---

### Task 5: Gate script immutability and final green run

**Files:**
- Read-only: `scripts/check_release.py`

**Interfaces:**
- Consumes: the baseline hex digest recorded in Task 1 Step 1.
- Produces: evidence for spec acceptance criteria 5 and 6.

**Model:** flash

- [ ] **Step 1: Recompute the hash and compare to the Task 1 baseline**

```bash
python -c "import hashlib; print(hashlib.sha256(open('scripts/check_release.py','rb').read()).hexdigest())"
```

Expected: the same hex digest recorded in Task 1. Different digest means someone edited the gate; restore the original bytes and investigate before proceeding.

- [ ] **Step 2: Cross-check via git (valid once the file is tracked)**

Run: `git status --porcelain -- scripts/check_release.py` and, if the file has been committed by the package work at execution time, also `git diff -- scripts/check_release.py`.

Expected: no modifications attributable to this plan. While the file is untracked this check is vacuous (that is why the hash comparison in Step 1 is the primary evidence); once tracked, the diff must stay empty.

- [ ] **Step 3: Final local gate run**

Run: `python scripts/check_release.py`
Expected: `release gate: PASS (scanned N files)`, exit 0. This is spec acceptance criterion 6.

- [ ] **Step 4: Record completion**

Confirm in the PR description: baseline digest matches, break test line captured in Task 4, all three commits from Tasks 1-3 present. No commit for this task.
