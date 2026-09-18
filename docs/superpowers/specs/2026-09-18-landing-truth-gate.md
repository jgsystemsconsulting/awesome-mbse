# Landing Truth Gate for the awesome-mbse Hub

- Date: 2026-09-18
- Branch: feat/pages-landing-and-packages
- Status: decisions locked in dispatch; no open forks

## Problem

The landing page (docs/index.html) makes three testable claims: a version chip, a sweep-date chip, and a curated-entry-count chip. It also makes one structural claim: a section index of six links pointing at README anchors. `scripts/check_release.py` already verifies all of it and exits 1 on drift. It passes locally today.

Nothing runs that script in CI. The repo's only workflows are link checks (`link-check-pr.yml`, `link-check-schedule.yml`). So a maintainer edit that changes a chip value, renames a chip key, or reshuffles the section index can merge green while the hub page lies. Nothing in the contributor path (PR template, CONTRIBUTING.md) says which parts of the landing page are gate inputs either, so the first offender gets surprised by a red run instead of a checklist warning.

This spec wires the existing gate into CI and documents the write path. It does not touch the gate logic.

## Research

research: skipped (internal CI workflow wire-up and maintainer write-path note; no external API or version-sensitive library choice)

## Codebase context

- `scripts/check_release.py`: stdlib-only release gate. Its landing-truth section matches exact `<dt>version|sweep|entries</dt>` followed by `<dd>value</dd>` in docs/index.html, compares the values against the `Version:` line in RELEASE-INFO.txt, the README `Last full sweep: YYYY-MM` badge, and the count of grammar-valid curated bullets. It also requires exactly one `<ul class="section-index">` block with exactly six `<li>`, each containing a single href whose fragment equals the GitHub slug of its README section title (the `SECTION_INDEX` tuple in the script, order fixed).
- `docs/index.html`: chips currently read version 1.0.0, sweep 2026-06, entries 85.
- `.github/workflows/` holds the two link-check workflows only. `validate.yml` is missing.
- `.github/PULL_REQUEST_TEMPLATE.md` and `CONTRIBUTING.md` (ten numbered sections) already exist. Both are edit targets, not new files.
- Local gate run today: `python scripts/check_release.py` prints `release gate: PASS (scanned 148 files)`.

## Goal

A push or PR against main cannot move the landing page's claims away from their sources, or break the section-index structure, without a red CI run. Contributors learn which landing-page bits are gate inputs at PR time (template + CONTRIBUTING), not only from a failure email.

## Non-goals

- No changes to `scripts/check_release.py` logic.
- No changes to the link-check workflows or lychee configuration.
- No Labs page, sindresorhus badge compliance, visitor copy, or GitHub Pages enablement.

## Approach

One new file, two small edits, all serving the same gate.

### 1. New workflow: .github/workflows/validate.yml

Shape matches the awesome-archimate validate workflow:

- Triggers: `push` (branches: main), `pull_request` (branches: main), `workflow_dispatch`.
- `permissions: contents: read`. No secrets, no dependency install.
- One job, `name: validate` (this is the check-run name branch protection must match), on `ubuntu-latest`, three steps:
  1. `actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4`
  2. `actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065 # v5` with `python-version: "3.12"`
  3. `run: python scripts/check_release.py`

Rationale: the script is stdlib only, so no install step exists to skip. Default shallow checkout is fine; the script's only git use is `git ls-files` on the checked-out tree. The pull_request trigger puts the gate on contributor PRs before merge; the push trigger covers direct main pushes; workflow_dispatch allows a manual re-run without a null commit.

### 2. PR template: one new Housekeeping checkbox

Add to the existing Housekeeping list in `.github/PULL_REQUEST_TEMPLATE.md`:

- `[ ]` If a chip value, section heading, or entry count changed, updated `docs/index.html` to match (CI runs `scripts/check_release.py`; see CONTRIBUTING.md section 11)

Exact wording can flex in implementation. The meaning cannot.

### 3. CONTRIBUTING.md: new short section "11. Landing page truth"

A short section after section 10, naming the gate inputs:

- The three chip `<dt>` names (version, sweep, entries) are matched exactly by the gate. Do not rename them. Their `<dd>` values are compared against the RELEASE-INFO.txt `Version:` field, the README sweep badge, and the curated bullet count. Curated bullets counted for the entries chip live only under these three README `##` sections: Magic Grid & Cameo / CATIA Magic, Broader SysML / MBSE Context, External awesome lists (Model Gallery is a pointer table and is not counted).
- The six section-index `<li>` href fragments must equal the GitHub slugs of the six product-section README headings, in fixed order: List family, Magic Grid & Cameo / CATIA Magic, Model Gallery, Broader SysML / MBSE Context, External awesome lists, Support & security. Fragments today: `#list-family`, `#magic-grid--cameo--catia-magic`, `#model-gallery`, `#broader-sysml--mbse-context`, `#external-awesome-lists`, `#support--security` (GitHub slug: lower-case, strip punctuation other than hyphen, spaces to hyphens).
- Visible display text (the labels around chip values, section-index link text) is free to change. The gate reads names, values, and fragments only.

### Notes

- Making `validate` a required status check on main is a repo-settings act for the maintainer, not a file in this repo. Recommended follow-up after merge; not an acceptance criterion here.
- The action SHAs carry version comments from the awesome-archimate reference. Bumps are manual, deliberate commits. No Dependabot in this repo and adding one is out of scope.

## Acceptance criteria

1. `.github/workflows/validate.yml` exists with the triggers, pins, Python version, and run step exactly as specified above.
2. The workflow runs green on the PR that introduces it, and green on a push to main after merge.
3. Break test proves the gate bites: change the entries `<dd>` in docs/index.html from 85 to 84 on a branch with an open PR against main (or run via workflow_dispatch on that commit), observe the run fail with the "landing entries chip 84 != curated count 85" failure line. Revert, observe green. Local equivalent also counts: `python scripts/check_release.py` must exit 1 with that line before revert.
4. The PR template carries the new Housekeeping item, and CONTRIBUTING.md carries the new section naming the three dt names, their comparison sources, and the six section-index fragments as gate inputs, with the display-text carve-out.
5. `scripts/check_release.py` is unchanged: byte-identical to its state on feat/pages-landing-and-packages before this work.
6. Local run `python scripts/check_release.py` exits 0 at the end of the work.

## Risks

- Renaming one of the curated or indexed README headings fails the gate by design. The fix belongs in the same PR as the rename: update docs/index.html (or, for indexed headings, keep the title stable). Section 11 documents this so it is not a surprise.
- Chip values duplicate data already present in RELEASE-INFO.txt and README.md. That is intentional; check_release.py is the single referee, so there is no second source of truth to reconcile.

## Open questions

None. Workflow shape, pin SHAs, Python version, and note placement were all fixed before this spec was written.
