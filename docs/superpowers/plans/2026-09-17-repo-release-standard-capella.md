# Awesome Capella Release Repo Standard Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bring `jgsystemsconsulting/awesome-capella` to Release Repo Standard v1.14 RR-B Base: audit exits 0, release identity v0.1.0 end to end, release-gate CI, Pages landing live, About/homepage/protection applied.

**Architecture:** One spoke-local change set on a single branch: legal and identity files, Keep-a-Changelog version 0.1.0, SECURITY advisory route, README Install/Usage/Licence/Support/Version sections, `scripts/check_release.py` gate plus `validate.yml`, list-adapted issue forms, self-contained `docs/index.html` Pages landing, and `docs/DISTRIBUTION.md` ledger. All files merge in one PR, then fixed-order platform steps run against main HEAD: merge, Pages enable, About plus homepage, tag v0.1.0 plus GitHub Release, branch protection.

**Tech Stack:** Python 3 stdlib (gate script), GitHub Actions (`actions/checkout@v4`, `actions/setup-python@v5`), `gh` CLI for Pages/About/Release/protection API calls, Git Bash on Windows.

**Spec:** `docs/superpowers/specs/2026-09-17-repo-release-standard-capella.md` (normative; locked decisions D1-D11, acceptance criteria AC1-9)

## Global Constraints

Every task implicitly includes these. Values are verbatim from the spec.

- Target repo: `C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella`, branch `main`, remote `https://github.com/jgsystemsconsulting/awesome-capella`. All file work is spoke-local; the hub `awesome-mbse` is not touched (this plan file is the only hub artifact).
- Profile RR-B Base only (D1). No MCP/skills/research rows. Licence stays CC0-1.0, unchanged (D2). Standalone build model (RR-B-15).
- Version **0.1.0**, dated **2026-09-17**, sourced from the CHANGELOG top entry `## [0.1.0] - 2026-09-17`, propagated to RELEASE-INFO.txt, CITATION.cff, tag `v0.1.0`, GitHub Release (D4).
- About description exactly: `Curated Capella tool and Arcadia method resources for MBSE practitioners`. Topics: `capella`, `arcadia`, `mbse`, `awesome-list`, `model-based-systems-engineering`, keep existing `awesome` (6 total; the auditor requires at least 6) (D10).
- Pages URL (homepage value): `https://jgsystemsconsulting.github.io/awesome-capella/`.
- Licence-enquiry URL everywhere required: `https://labs.jgsystemsconsulting.com/licensing.html` (README Licence, landing page, Release notes) (D5, D10).
- SECURITY.md: private advisory route only, `We aim to acknowledge reports within 7 days`, no email address anywhere, no em dash (D9).
- Release notes footer line exactly: `Licence enquiries: https://labs.jgsystemsconsulting.com/licensing.html` (D10).
- `scripts/check_release.py` REQUIRED list (RR-B-15): `README.md`, `LICENSE`, `COPYRIGHT`, `NOTICE`, `CHANGELOG.md`, `SECURITY.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `RELEASE-INFO.txt`, `CITATION.cff`, `docs/DISTRIBUTION.md`, `docs/index.html`, `scripts/check_entries.py`, `scripts/check_release.py`; header sentinel `Copyright (c) 2026 JG Systems Consulting Ltd`; gate prints a scanned-file count of at least 1.
- Platform order is fixed (D10): merge release commit to main, enable Pages, set About plus homepageUrl only after Pages serves, tag v0.1.0 on that main HEAD SHA and publish the Release, then branch protection.
- README: the 73 entry bullets, their ordering, tags, and the flat `## Contents` block stay byte-identical. New sections append below `## Commercial offers` only.
- Family triad workflows (`link-check-pr.yml`, `link-check-schedule.yml`) stay untouched. `suggest-resource.yml` stays as the improvement channel; renaming or duplicating it is rejected (D8). The audit's `RR-B-32` improvement-form WARN is accepted.
- Family pointer stays text-only; no hub FAMILY.md hyperlink (D11).
- No em dash in README.md, SECURITY.md, CHANGELOG.md, docs/DISTRIBUTION.md, docs/index.html (AC7). No machine-local paths in any new file. New YAML/CFF written as plain UTF-8 without BOM.
- All commits use the repo's configured noreply identity `245595077+jgsystemsconsulting@users.noreply.github.com` (already set; RR-B-27).
- Auditor: `python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base [--gh] [--links]`, run from the spoke root. It imports `landing_taste` from its own directory, so the path works from anywhere.

## Codebase context

The spoke ships: README with 73 verified entries in nine sections plus a flat hand-maintained `## Contents`, CC0-1.0 LICENSE, CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md (has one em dash and an email address today), CHANGELOG.md (date-headed, not semver), `scripts/check_entries.py` (prints `entries: 73`, exits 0), two family link-check workflows, one issue form `suggest-resource.yml`, a PR template, `.markdownlint-cli2.jsonc`, empty `.lycheeignore`. Missing relative to the standard: everything in the spec's file inventory. The GitHub About description and five topics (`arcadia`, `awesome`, `awesome-list`, `capella`, `mbse`) are already set; homepageUrl is empty. Sibling `awesome-sysml-v2` ships the CITATION.cff shape this plan copies (entity `JG Systems Consulting Ltd`, year 2026); its MIT licence is not copied.

## Research

- https://github.com/jgsystemsconsulting/awesome-capella (target spoke; About/topics state verified 2026-09-17 via `gh repo view`)
- https://github.com/jgsystemsconsulting/awesome-sysml-v2 (CITATION.cff shape reference)
- `docs/superpowers/research/2026-09-17-repo-release-standard-capella-research.md` (14 FAIL, 2 WARN, 8 PASS baseline; list-product interpretation notes)
- `docs/superpowers/context/2026-09-17-repo-release-standard-capella-context.md` (spoke inventory, family constraints, baseline porcelain sha256 `0933b130d260f82993853e7b62552af5ff0dccda8cd3a8192496cf60092999d2`)
- Standard: `C:/Users/gower/.zcode/skills/release-repo-standard/references/release-repo-standard.md` (v1.14); auditor and templates under the same skill tree

---

### Task 1: Legal, identity, and hygiene files

**Files:**
- Create: `COPYRIGHT`
- Create: `NOTICE`
- Create: `CITATION.cff`
- Create: `.gitignore`
- Modify: `scripts/check_entries.py` (two header lines at the top only)

**Interfaces:**
- Consumes: nothing.
- Produces: `COPYRIGHT`, `NOTICE`, `CITATION.cff` with version `0.1.0`; the SPDX header on `check_entries.py` that `check_release.py` (Task 3) later requires. Task 2 and Task 3 rely on the version string `0.1.0` and the header sentinel exact text.

**Model:** flash

- [ ] **Step 1: Record the baseline and the licence detector state**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
git status --porcelain   # expect empty; if not, stop and report
gh api repos/jgsystemsconsulting/awesome-capella/license --jq .license.spdx_id
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base
```

Expected: spdx_id `CC0-1.0` (AC9 pre-check); audit prints the 2026-09-17 baseline shape (14 FAIL, 2 WARN, 8 PASS). If spdx_id is `NOASSERTION`, replace LICENSE with the canonical CC0-1.0 Universal text GitHub licensee accepts, keeping any required org/copyright identification in COPYRIGHT/NOTICE (and only in LICENSE if audit.py RR-B-01 still requires an org string in-file). Do not invent a 'Creative Commons Legal Code' header. Re-check `gh api ... license.spdx_id`.

- [ ] **Step 2: Create the branch**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
git checkout main && git pull origin main
git checkout -b release/0.1.0-standard
```

- [ ] **Step 3: Write `COPYRIGHT`** (single line, exactly):

```
Copyright (c) 2026 JG Systems Consulting Ltd. All rights reserved.
```

- [ ] **Step 4: Write `NOTICE`** (filled template, no-third-party-code variant per D2; no trailing comment lines):

```
Awesome Capella
Copyright (c) 2026 JG Systems Consulting Ltd.

No third-party code is distributed with this repository. The list is a
curated index of links; each linked resource remains under its own licence
and is served from its upstream source.
```

- [ ] **Step 5: Write `CITATION.cff`** (sysml-v2 shape plus version and date; plain UTF-8, no BOM):

```yaml
cff-version: 1.2.0
message: "If you use this list in your work, please cite it using this metadata."
title: Awesome Capella
version: "0.1.0"
date-released: "2026-09-17"
authors:
  - entity:
      name: "JG Systems Consulting Ltd"
license: CC0-1.0
repository-code: https://github.com/jgsystemsconsulting/awesome-capella
url: https://github.com/jgsystemsconsulting/awesome-capella
```

- [ ] **Step 6: Write `.gitignore`**

```
__pycache__/
*.pyc
.venv/
.lycheecache
.playwright-mcp/
*.bak
.DS_Store
Thumbs.db
```

- [ ] **Step 7: Prepend the two header lines to `scripts/check_entries.py`**

The file currently starts with `import re`. Make the first three lines:

```python
# Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE.
# SPDX-License-Identifier: CC0-1.0
import re
```

Change nothing else in the file.

- [ ] **Step 8: Verify**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
python scripts/check_entries.py
python -c "from pathlib import Path; p=Path('CITATION.cff'); print(p.read_bytes()[:3]); assert p.read_bytes()[:3] != b'\xef\xbb\xbf'"
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base | grep -E "RR-B-01|RR-B-02|RR-B-03|RR-B-04|RR-B-09|RR-B-13|RR-B-27|RR-B-31|RR-B-33|TMPL"
```

Expected: `entries: 73` and `format: OK`; BOM bytes are not `efbbbf`; in the grep output, RR-B-01, RR-B-02 (x2), RR-B-03, RR-B-04, RR-B-09, RR-B-13, RR-B-27, RR-B-31, RR-B-33, and TMPL all read PASS (RR-B-09 passes here with CITATION.cff as the only version-bearing file; RR-B-18 still FAIL until Task 6, which is expected).

- [ ] **Step 9: Commit**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
git add COPYRIGHT NOTICE CITATION.cff .gitignore scripts/check_entries.py
git commit -m "chore: add legal identity files and SPDX header (RR-B-01..04,13,31)"
```

Done when: the targeted audit rows PASS with no FAIL among them, the checker still counts 73 entries, CITATION.cff has no BOM, and the commit is on `release/0.1.0-standard`.

### Task 2: Version alignment, security route, README sections

**Files:**
- Modify: `CHANGELOG.md` (full rewrite to Keep a Changelog shape)
- Create: `RELEASE-INFO.txt`
- Modify: `SECURITY.md` (full rewrite)
- Modify: `README.md` (append five sections after `## Commercial offers`; entries and Contents untouched)

**Interfaces:**
- Consumes: version `0.1.0` and org name from Task 1.
- Produces: `CHANGELOG.md` top entry `## [0.1.0] - 2026-09-17` (the version source, D4); `RELEASE-INFO.txt` with `Tag: v0.1.0` (auditor RR-B-10 row); README sections and URLs that Task 4's landing page and Task 6's Release notes mirror.

**Model:** standard

- [ ] **Step 1: Rewrite `CHANGELOG.md`** (entire file becomes):

```markdown
# Changelog

All notable changes to this list are documented here. The format follows
Keep a Changelog and versions follow Semantic Versioning.

## [0.1.0] - 2026-09-17

### Added

- Created `jgsystemsconsulting/awesome-capella` (public) as the Capella and
  Arcadia spoke of the awesome-mbse list family.
- Namespace recheck on create day (2026-09-17): empty; no live awesome-capella
  or awesome-arcadia incumbent at 2026-09-17. Supersedes the rate-limited
  2026-09-17 research probe (R7).
- Verified seed count: 73 entries; depth bar met.

### Notes

- Release-standard pass (Release Repo Standard v1.14, RR-B Base): COPYRIGHT,
  NOTICE, CITATION.cff, RELEASE-INFO.txt, release gate CI, Pages landing,
  issue forms, and the distribution ledger.
```

- [ ] **Step 2: Write `RELEASE-INFO.txt`** with the real UTC timestamp (D4: Built is the UTC ISO-8601 time at release-commit authoring):

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
printf 'Product: Awesome Capella\nVersion: 0.1.0\nBuilt: %s\nTag: v0.1.0\n' "$TS" > RELEASE-INFO.txt
cat RELEASE-INFO.txt
```

Expected output has all four fields; `Built` matches `YYYY-MM-DDTHH:MM:SSZ`.

- [ ] **Step 3: Rewrite `SECURITY.md`** (entire file becomes; no email, no em dash):

```markdown
# Security Policy

This repository is a curated index of links. It ships no executable product.
The main security surfaces are the links it points to and the CI workflows.

## Reporting a vulnerability

Report sensitive issues privately via a
[GitHub security advisory](https://github.com/jgsystemsconsulting/awesome-capella/security/advisories/new).
Please do not open a public issue for a suspected malicious or hijacked link
until it has been reviewed.

For non-sensitive fixes (a dead or moved link, a CI misbehaviour), open a
pull request with the fix directly.

We aim to acknowledge reports within 7 days.

## Scope notes

- A linked resource that turns out to be malicious, hijacked, or compromised.
- The repository's automation: the link-check workflows and the release gate.
```

- [ ] **Step 4: Append the README sections after the `## Commercial offers` section** (end of file; one blank line before `## Install`; do not touch anything above):

````markdown
## Install

Nothing to install. This list is a curated index: browse it here on GitHub,
or clone it:

```bash
git clone https://github.com/jgsystemsconsulting/awesome-capella.git
```

## Usage

- Browse the sections under [Contents](#contents), or search the page with
  your browser's find function.
- Open any entry's link to reach the upstream resource; the list never
  re-hosts content.
- To suggest a resource, use the
  [Suggest a resource](https://github.com/jgsystemsconsulting/awesome-capella/issues/new?template=suggest-resource.yml)
  issue form.
- To report a wrong or dead entry, use the
  [bug report](https://github.com/jgsystemsconsulting/awesome-capella/issues/new?template=bug_report.yml)
  form (added with this release).

## Licence

Released under the [CC0-1.0](LICENSE) licence (public domain dedication).
Linked resources remain under their own licences.

To request a commercial or academic licence, or if you are unsure which
licence you need: https://labs.jgsystemsconsulting.com/licensing.html

## Support

- Bug or dead link: [bug report form](https://github.com/jgsystemsconsulting/awesome-capella/issues/new?template=bug_report.yml)
- Suggest a resource (the list's improvement channel):
  [suggestion form](https://github.com/jgsystemsconsulting/awesome-capella/issues/new?template=suggest-resource.yml)
- Security issues: [private security advisory](https://github.com/jgsystemsconsulting/awesome-capella/security/advisories/new)
  (see [SECURITY.md](SECURITY.md))
- SysML v2 resource suggestions belong on the sibling list:
  [awesome-sysml-v2 issues](https://github.com/jgsystemsconsulting/awesome-sysml-v2/issues)

## Version

Current release: 0.1.0 (2026-09-17). See [CHANGELOG.md](CHANGELOG.md) and
[RELEASE-INFO.txt](RELEASE-INFO.txt).
````

- [ ] **Step 5: Verify**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
python scripts/check_entries.py
grep -c '^- \[' README.md
grep -n "—" README.md CHANGELOG.md SECURITY.md RELEASE-INFO.txt
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base | grep -E "RR-B-05|RR-B-07|RR-B-08|RR-B-09|RR-B-10|RR-B-28"
npx -y markdownlint-cli2 "README.md" 2>/dev/null || echo "node not available locally; CI triad is the guard"
```

Expected: checker prints `entries: 73` and `format: OK` (AC4); `grep -c` prints `82` (73 entries plus the 9 Contents lines: the entry set is unchanged); the em-dash grep prints nothing (SECURITY.md's old em dash is gone, AC7 partial); audit rows RR-B-05, RR-B-07, RR-B-08, RR-B-09, RR-B-10, RR-B-28 read PASS (RR-B-07 detail must say `no email`). If markdownlint runs and flags the new sections, fix before commit; if node is absent, the triad run in Task 7 is the binding guard.

- [ ] **Step 6: Commit**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
git add CHANGELOG.md RELEASE-INFO.txt SECURITY.md README.md
git commit -m "feat: v0.1.0 changelog, release info, security advisory route, README sections (RR-B-05,07..10,28)"
```

Done when: checker counts 73 entries and exits 0, version rows RR-B-09/10 PASS with value `0.1.0` (RR-B-08 is CHANGELOG present, not a PASS label), RR-B-07 PASS with no email, RR-B-05 PASS, no em dash in the four files, commit on the branch.

### Task 3: Release gate, validate workflow, issue forms

**Files:**
- Create: `scripts/check_release.py`
- Create: `.github/workflows/validate.yml`
- Create: `.github/ISSUE_TEMPLATE/bug_report.yml`
- Create: `.github/ISSUE_TEMPLATE/config.yml`

**Interfaces:**
- Consumes: the REQUIRED file set (RR-B-15) which Tasks 1, 2, and 4 create; header sentinel text `Copyright (c) 2026 JG Systems Consulting Ltd` matching Task 1's headers.
- Produces: gate command `python scripts/check_release.py` (exit 0 when the tree is complete, Task 4 finishes making it pass); workflow `validate.yml` whose job id `validate` becomes the branch-protection required check name in Task 6; `config.yml` contact_links with the two exact URLs from D8.

**Model:** flash

- [ ] **Step 1: Write `scripts/check_release.py`** (adapted from the skill template for this tree: Base REQUIRED list, no src/ layout, real sentinel, scanned-count print):

```python
# Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE.
# SPDX-License-Identifier: CC0-1.0
"""Release gate (RR-B-15): required files, forbidden paths, forbidden
content, headers present. Exits non-zero on any failure.

Adapted for awesome-capella (RR-B Base, standalone model): no src/ layout,
no package install, no unit tests beyond scripts/check_entries.py."""
import pathlib
import re
import subprocess
import sys

fails: list[str] = []

REQUIRED = [
    "README.md", "LICENSE", "COPYRIGHT", "NOTICE", "CHANGELOG.md",
    "SECURITY.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md",
    "RELEASE-INFO.txt", "CITATION.cff",
    "docs/DISTRIBUTION.md", "docs/index.html",
    "scripts/check_entries.py", "scripts/check_release.py",
]
for f in REQUIRED:
    if not pathlib.Path(f).is_file():
        fails.append(f"required file missing: {f}")

tracked = subprocess.run(["git", "ls-files"], capture_output=True, text=True,
                         check=True).stdout.splitlines()
FORBIDDEN_PATH_PARTS = ["__pycache__", ".venv", ".worktrees", ".pytest_cache",
                        ".ruff_cache", ".bak"]
for f in tracked:
    if any(part in f for part in FORBIDDEN_PATH_PARTS):
        fails.append(f"forbidden tracked path: {f}")

FORBIDDEN_CONTENT = [re.compile(r"BEGIN [A-Z ]*PRIVATE KEY"),
                     re.compile(r"CONFIDENTIAL\s+[-—]\s+Not for external distribution")]
SCAN_GLOBS = ["scripts/*.py", "*.md", "docs/*.md", "docs/*.html",
              "RELEASE-INFO.txt", "CITATION.cff"]
scanned: set[pathlib.Path] = set()
for g in SCAN_GLOBS:
    for path in pathlib.Path(".").glob(g):
        scanned.add(path)
        text = path.read_text(encoding="utf-8", errors="ignore")
        for rx in FORBIDDEN_CONTENT:
            if rx.search(text):
                fails.append(f"forbidden content in {path}: {rx.pattern}")

HEADER_SENTINEL = "Copyright (c) 2026 JG Systems Consulting Ltd"
for g in ["scripts/*.py"]:
    for path in pathlib.Path(".").glob(g):
        scanned.add(path)
        if HEADER_SENTINEL not in path.read_text(encoding="utf-8", errors="ignore")[:600]:
            fails.append(f"header missing: {path}")

if fails:
    print("RELEASE GATE FAILED:")
    for f in fails:
        print(f"  - {f}")
    sys.exit(1)
assert scanned, "scan globs matched nothing; fix SCAN_GLOBS"
print(f"release gate: PASS (scanned {len(scanned)} files)")
```

- [ ] **Step 2: Run the gate and prove it fails for the right reason** (Task 4 has not run yet, so the docs files are the expected misses):

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
python scripts/check_release.py; echo "exit=$?"
```

Expected: `exit=1` listing exactly `required file missing: docs/DISTRIBUTION.md` and `required file missing: docs/index.html` and nothing else. Negative probe: `mv CITATION.cff CITATION.cff.hold && python scripts/check_release.py; echo "exit=$?"; mv CITATION.cff.hold CITATION.cff` must add `required file missing: CITATION.cff` to the list (proves the REQUIRED check fires; this is the failing-test cycle for the gate).

- [ ] **Step 3: Write `.github/workflows/validate.yml`** (job id `validate` so the required check name is exactly `validate`; plain English step names; push and pull_request on main; family triad files untouched):

```yaml
name: validate
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
permissions:
  contents: read
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Run release gate
        run: python scripts/check_release.py
```

- [ ] **Step 4: Write `.github/ISSUE_TEMPLATE/bug_report.yml`** (list-adapted per D8's sibling form; affected entry URL, problem type, list version, required hygiene checkbox):

```yaml
name: Bug report
description: Report a dead, wrong, or mislabelled list entry, or a checker defect
labels: [bug]
body:
  - type: input
    id: entry-url
    attributes:
      label: Affected entry URL
      description: The list entry this report is about (paste the URL from README)
    validations:
      required: true
  - type: dropdown
    id: problem-type
    attributes:
      label: Problem type
      options:
        - Dead or moved link
        - Wrong or misleading description
        - Wrong tags or year
        - Checker or CI defect
    validations:
      required: true
  - type: input
    id: version
    attributes:
      label: List version
      description: From RELEASE-INFO.txt or the release notes
    validations:
      required: true
  - type: textarea
    id: detail
    attributes:
      label: What is wrong, and what should it say instead
    validations:
      required: true
  - type: checkboxes
    id: hygiene
    attributes:
      label: Hygiene
      options:
        - label: I confirm this report contains no tokens, keys, or credentials.
          required: true
```

- [ ] **Step 5: Write `.github/ISSUE_TEMPLATE/config.yml`** (exact titles and URLs from D8; `suggest-resource.yml` stays untouched as the improvement channel):

```yaml
blank_issues_enabled: false
contact_links:
  - name: Security advisory
    url: https://github.com/jgsystemsconsulting/awesome-capella/security/advisories/new
    about: Report security issues privately, never as a public issue.
  - name: awesome-sysml-v2 issues
    url: https://github.com/jgsystemsconsulting/awesome-sysml-v2/issues
    about: SysML v2 resource suggestions and defects belong on the sibling list.
```

- [ ] **Step 6: Verify**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
python -c "from pathlib import Path
for f in ['.github/workflows/validate.yml', '.github/ISSUE_TEMPLATE/bug_report.yml', '.github/ISSUE_TEMPLATE/config.yml']:
    b = Path(f).read_bytes()
    assert b[:3] != b'\xef\xbb\xbf', f'BOM in {f}'
print('no BOM')"
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base | grep -E "RR-B-15|RR-B-32|RR-B-33|RR-B-34"
```

Expected: no BOM in the three YAML files; RR-B-15 PASS (`gate script: True, CI workflow: True`); RR-B-32 first row PASS (`issue form + chooser present`) and second row WARN (`no improvement/enhancement form`), which is the accepted D8 WARN; RR-B-33 PASS; RR-B-34 PASS.

- [ ] **Step 7: Commit**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
git add scripts/check_release.py .github/workflows/validate.yml .github/ISSUE_TEMPLATE/bug_report.yml .github/ISSUE_TEMPLATE/config.yml
git commit -m "ci: release gate script, validate workflow, bug report form and chooser (RR-B-15,32)"
```

Done when: the gate exits 1 citing exactly the two not-yet-created docs files (and catches a moved required file in the negative probe), the three YAML files are BOM-free, RR-B-15 PASS, RR-B-32 PASS plus the accepted WARN, commit on the branch.

### Task 4: Pages landing page and distribution ledger

**Files:**
- Create: `docs/index.html`
- Create: `docs/.nojekyll` (empty file)
- Create: `docs/DISTRIBUTION.md`

**Interfaces:**
- Consumes: licence-enquiry URL and repo URL (Global Constraints); version 0.1.0.
- Produces: the two files whose absence made the Task 3 gate red, so `python scripts/check_release.py` now exits 0 (AC2); `docs/index.html` containing the licence-enquiry URL (auditor RR-B-20 file-level row); ledger rows named in the Task 5 PR body (D8, D5, RR-B-19/29/30).

**Model:** flash

- [ ] **Step 1: Write `docs/index.html`** (self-contained: system fonts only, inline CSS, canonical plus OG tags, licence-enquiry link in the footer, focus-visible and reduced-motion rules; no em dash anywhere; version line in the footer, not in a hero):

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Awesome Capella: curated Capella and Arcadia resources for MBSE</title>
<meta name="description" content="A curated, verified list of Eclipse Capella tools, Arcadia method references, case studies, and training for MBSE practitioners. Browse on GitHub or clone the list.">
<link rel="canonical" href="https://jgsystemsconsulting.github.io/awesome-capella/">
<meta property="og:type" content="website">
<meta property="og:title" content="Awesome Capella">
<meta property="og:description" content="Curated Capella tool and Arcadia method resources for MBSE practitioners.">
<meta property="og:url" content="https://jgsystemsconsulting.github.io/awesome-capella/">
<meta name="twitter:card" content="summary">
<style>
:root { --ink:#1f2937; --muted:#4b5563; --accent:#1d4ed8; --line:#e5e7eb; --bg:#ffffff; --soft:#f9fafb; }
* { box-sizing: border-box; }
body { margin:0; font-family: system-ui, -apple-system, "Segoe UI", sans-serif; color:var(--ink); background:var(--bg); line-height:1.6; }
header.site-head { border-bottom:1px solid var(--line); padding:1.5rem 0; }
main, header.site-head > div, footer > div { max-width:46rem; margin:0 auto; padding:0 1.25rem; }
h1 { font-size:1.6rem; margin:0 0 .25rem; }
p.tagline { color:var(--muted); margin:.25rem 0 0; }
section { padding:1.25rem 0; border-bottom:1px solid var(--line); }
h2 { font-size:1.15rem; }
a { color:var(--accent); }
a:focus-visible { outline:2px solid var(--accent); outline-offset:2px; }
ul { padding-left:1.25rem; }
code { background:var(--soft); padding:.1rem .35rem; border-radius:3px; }
footer { padding:1.25rem 0 2.5rem; color:var(--muted); font-size:.9rem; }
@media (prefers-reduced-motion: reduce) { * { transition:none !important; scroll-behavior:auto !important; } }
</style>
</head>
<body>
<header class="site-head">
  <div>
    <h1>Awesome Capella</h1>
    <p class="tagline">Curated Capella tool and Arcadia method resources for MBSE practitioners.</p>
  </div>
</header>
<main>
  <section id="about">
    <h2>What this is</h2>
    <p>A curated, verified index of Eclipse Capella tools, Arcadia method
    references, add-ons, books and courses, community resources, example
    models, and commercial offers. Every entry points at the upstream source;
    nothing is re-hosted. Maintained by JG Systems Consulting Ltd as part of
    the awesome-mbse list family.</p>
  </section>
  <section id="use-the-list">
    <h2>How to use the list</h2>
    <ul>
      <li><a href="https://github.com/jgsystemsconsulting/awesome-capella#readme">Open the list on GitHub</a>
          and browse the nine sections, or search the page in your browser.</li>
      <li>Clone it: <code>git clone https://github.com/jgsystemsconsulting/awesome-capella.git</code></li>
      <li>Each entry carries topic tags and a year, so you can scan for what
          applies to your work.</li>
    </ul>
  </section>
  <section id="contribute">
    <h2>Suggest an entry or report a problem</h2>
    <ul>
      <li>Suggest a resource with the
          <a href="https://github.com/jgsystemsconsulting/awesome-capella/issues/new?template=suggest-resource.yml">suggestion form</a>.</li>
      <li>Report a dead or wrong entry with the
          <a href="https://github.com/jgsystemsconsulting/awesome-capella/issues/new?template=bug_report.yml">bug report form</a>.</li>
      <li>Security issues go through a
          <a href="https://github.com/jgsystemsconsulting/awesome-capella/security/advisories/new">private security advisory</a>.</li>
    </ul>
  </section>
</main>
<footer>
  <div>
    <p><a href="https://github.com/jgsystemsconsulting/awesome-capella">awesome-capella on GitHub</a>
       &middot; Version 0.1.0 (2026-09-17)</p>
    <p>CC0-1.0. To request a commercial or academic licence, or if you are unsure
       which licence you need:
       <a href="https://labs.jgsystemsconsulting.com/licensing.html">https://labs.jgsystemsconsulting.com/licensing.html</a></p>
  </div>
</footer>
</body>
</html>
```

- [ ] **Step 2: Create `docs/.nojekyll`** (empty) and write `docs/DISTRIBUTION.md`:

Create the empty marker file:

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
mkdir -p docs && touch docs/.nojekyll
```

Write `docs/DISTRIBUTION.md` (all nine channel rows from RR-B-36; every non-submitted row carries a decision plus date):

```markdown
<!--
Copyright (c) 2026 JG Systems Consulting Ltd. All Rights Reserved.
See LICENSE for terms.
-->

# Distribution ledger: Awesome Capella

One row per channel this list reaches or could reach (RR-B-36,
release-repo-standard v1.14). A non-submitted row carries its decision and
date so the question stays closed until its premises change. Revisit at
every release: move statuses, re-date reasons whose premises changed, never
drop a row silently.

Last reviewed: 0.1.0 / 2026-09-17

| Channel | Artifact | Status | Decision / reason | Date |
|---|---|---|---|---|
| GitHub repo (public) | jgsystemsconsulting/awesome-capella | live | Canonical home of the list. | 2026-09-17 |
| GitHub Releases | v0.1.0 | submitted | Release v0.1.0 published from the CHANGELOG entry with the licence-enquiry footer. | 2026-09-17 |
| GitHub Pages landing | docs/index.html | live | Served from main /docs; the repo homepage URL points here. | 2026-09-17 |
| GitHub About, topics, homepage | repo settings | applied | Description, six topics, homepage set to the Pages URL. | 2026-09-17 |
| Org catalogue (labs.jgsystemsconsulting.com) | site entry | planned | Add a list entry alongside the other awesome-mbse spokes. | 2026-09-17 |
| sindresorhus/awesome | list PR | deferred | Acceptability gate not passed: membership bar, review bandwidth, and naming conventions need assessment before submitting. | 2026-09-17 |
| In-host agent and IDE marketplaces (Claude Code, Cursor, Codex, Gemini CLI) | n/a | deliberate N/A | A curated list is browsed on GitHub, not installed into an agent host, so no marketplace manifests apply (RR-B-29). | 2026-09-17 |
| MCP directories (awesome-mcp-servers, Glama, Smithery, PulseMCP) | n/a | deliberate N/A | The list speaks no MCP; RR-M rows are out of profile (RR-B Base only). | 2026-09-17 |
| Community MBSE directories and forums | link posts | deferred | Assess each directory's scope and licence bar before posting. | 2026-09-17 |
```

- [ ] **Step 3: Verify**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/landing_taste.py" docs/index.html
python scripts/check_release.py; echo "exit=$?"
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base | grep -E "RR-B-20|RR-B-24|RR-B-28|RR-B-34|RR-B-36"
grep -n "—" docs/index.html docs/DISTRIBUTION.md
```

Expected: `landing_taste.py` prints `PASS` (this is the RR-B-24 mechanical overlay; the taste-skill pre-flight itself is a MANUAL note recorded in the PR per D5); the gate prints `release gate: PASS (scanned N files)` with N at least 1 and exits 0 (AC2); RR-B-20 PASS (`docs/index.html contains licence-enquiry URL`), RR-B-24 PASS, RR-B-28 PASS, RR-B-34 PASS, RR-B-36 PASS; the em-dash grep prints nothing.

- [ ] **Step 4: Commit**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
git add docs/index.html docs/.nojekyll docs/DISTRIBUTION.md
git commit -m "feat: Pages landing page and distribution ledger (RR-B-20,24,30,36)"
```

Done when: landing_taste PASS, gate exit 0 with a scanned count of at least 1, RR-B-20/24/28/34/36 PASS, no em dash in either docs file, commit on the branch.

### Task 5: Full audit snapshot, PR with MANUAL closures, merge

**Files:**
- Modify: none in the tree (PR body and platform records only)

**Interfaces:**
- Consumes: the complete branch from Tasks 1-4; `gh` with `workflow` scope.
- Produces: the merged main HEAD SHA (Task 6 tags this exact SHA); the PR body that closes the spec's MANUAL items (AC6); the recorded `gh auth` workflow-scope fix (AC8).

**Model:** standard

- [ ] **Step 1: Confirm workflow push scope (AC8)**

```bash
gh auth status
```

If the token lacks `workflow` scope, run `gh auth refresh -s workflow` and re-check. The push in Step 4 creates `validate.yml`; without the scope GitHub rejects the whole push.

- [ ] **Step 2: Run the pre-merge audit snapshot and check the keep/drop inventory**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base; echo "exit=$?"
git ls-files | grep -E "^\.planning/|^docs/(eval|evidence|superpowers|specs)/|^GATES\.md$|^scripts/add_headers\.py$" || echo "no maintainer-only candidates tracked"
```

Expected audit shape: the only FAIL row is `RR-B-18` (tag v0.1.0 missing until Task 6, per the spec's risk note; the tag ships on this same change set's merge commit). Every other row is PASS except the accepted RR-B-32 improvement-form WARN. Keep/drop inventory (RR-B-35): the grep prints `no maintainer-only candidates tracked`; this exact phrase goes in the PR.

- [ ] **Step 3: Push and open the PR with the MANUAL closures**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
git push -u origin release/0.1.0-standard
gh pr create --base main --head release/0.1.0-standard \
  --title "Release standard 0.1.0: legal, gate, landing, ledger" \
  --body-file - <<'EOF'
## Summary

Release Repo Standard v1.14 (RR-B Base) packaging for the list. New: COPYRIGHT, NOTICE, CITATION.cff, RELEASE-INFO.txt, .gitignore, scripts/check_release.py, .github/workflows/validate.yml, bug report form + chooser, docs/index.html + docs/.nojekyll, docs/DISTRIBUTION.md. Rewritten: CHANGELOG (Keep a Changelog, [0.1.0]), SECURITY.md (private advisory route, 7-day ack, no email), README Install/Usage/Licence/Support/Version. scripts/check_entries.py gained the copyright + SPDX header. Entries, Contents block, family workflows, and suggest-resource.yml untouched.

## MANUAL items closed

- RR-B-06 (D6): list product; Install says nothing to install (browse or clone); Usage covers browse, search, open links, contribute via forms. Depth carried by README Install+Usage plus CONTRIBUTING.md; no docs/usage.md.
- RR-B-12: CONTRIBUTING.md, CODE_OF_CONDUCT.md, PR template already present (OSS posture); no change.
- RR-B-19: org catalogue row `planned` in docs/DISTRIBUTION.md.
- RR-B-24: landing_taste.py PASS on docs/index.html. MANUAL taste-skill note: page kind is a reference-index landing for MBSE practitioners; vibe minimal and quiet; no hero, no scroll cues, system fonts, single column, footer carries the licence-enquiry link. Design-system precedence applied; no exemptions needed. Playwright 2-breakpoint screenshots are a SHOULD residual if skipped; D5 requires mechanical taste overlay when available plus a MANUAL taste note. 
- RR-B-26: no ASCII diagrams in README; no Mermaid needed for a list; callout/table usage unchanged.
- RR-B-28: new prose written clean; em-dash grep clean across README.md, SECURITY.md, CHANGELOG.md, docs/DISTRIBUTION.md, docs/index.html; old SECURITY.md em dash removed.
- RR-B-29 (D7): whole requirement deliberate N/A (list is not installed into an agent host); ledger row with date.
- RR-B-30 (D5): multi-page assessment done; content walked; outcome: one HTML landing + README deep content; nothing justifies a third page.
- RR-B-35: git ls-files inventory walked: no maintainer-only candidates tracked.
- RR-B-36: ledger at 0.1.0 / 2026-09-17, nine channels, every non-submitted row has decision + date.

## Platform steps after merge (fixed order)

Merge, Pages enable from /docs, About + homepage, tag v0.1.0 on main HEAD, branch protection. Tracked in the session notes; RR-B-18 stays FAIL until the tag exists (expected for this snapshot).
EOF
```

- [ ] **Step 4: Watch the PR checks**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
gh pr checks --watch
```

Expected: `validate` (release gate) green, and the family triad jobs (`lychee`, `awesome-lint`, `markdownlint`, triggered by the README.md path change) green. If `awesome-lint` or `markdownlint` fails on the new README sections, fix the section prose (entries stay untouched), push, and re-watch.

- [ ] **Step 5: Merge and record the release SHA**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
gh pr merge --squash --delete-branch
git checkout main && git pull origin main
git rev-parse HEAD
```

Record the printed SHA: it is the release commit. Task 6 tags exactly this SHA.

Done when: PR checks green (validate plus triad), PR merged with squash, main HEAD SHA recorded, PR body contains the MANUAL closures and the keep/drop phrase.

### Task 6: Platform state in the fixed order (D10)

**Files:**
- Modify: none in the tree (GitHub platform state only; the temporary release-notes file is created and deleted)

**Interfaces:**
- Consumes: merge SHA from Task 5; CHANGELOG notes (Task 2); Pages URL and exact About string (Global Constraints).
- Produces: live Pages site; homepageUrl; local plus pushed tag `v0.1.0`; published Release v0.1.0 with the exact footer line; branch protection with required check `validate`. These make RR-B-18/20/21/22/23 PASS in Task 7's `--gh` audit.

**Model:** deep

- [ ] **Step 1: Enable Pages from /docs and verify it serves**

```bash
gh api -X POST repos/jgsystemsconsulting/awesome-capella/pages \
  -f "source[branch]=main" -f "source[path]=/docs"
gh api repos/jgsystemsconsulting/awesome-capella/pages --jq .html_url
gh api repos/jgsystemsconsulting/awesome-capella/pages/builds/latest --jq .status
curl -fsSL -o /dev/null -w '%{http_code}\n' https://jgsystemsconsulting.github.io/awesome-capella/
```

Expected: `https://jgsystemsconsulting.github.io/awesome-capella/`, build status `built` (re-run the builds call until it flips from `building`; first build can take a minute or two), then HTTP `200`. If the POST returns "already exists", confirm the existing source is `main` `/docs` via the GET call. If curl returns 404 after the build is `built`, re-run the curl once after 30 seconds before investigating.

- [ ] **Step 2: Set About description, topics, and homepage (homepage only now that Pages serves)**

```bash
gh repo edit jgsystemsconsulting/awesome-capella \
  --description "Curated Capella tool and Arcadia method resources for MBSE practitioners" \
  --homepage "https://jgsystemsconsulting.github.io/awesome-capella/"
gh repo edit jgsystemsconsulting/awesome-capella --add-topic model-based-systems-engineering
gh repo view jgsystemsconsulting/awesome-capella --json description,homepageUrl,repositoryTopics
```

Expected JSON: description is the exact string; homepageUrl is the Pages URL; six topics (`arcadia`, `awesome`, `awesome-list`, `capella`, `mbse`, `model-based-systems-engineering`). Six is required: the auditor's RR-B-21 row demands at least 6 topics.

- [ ] **Step 3: Tag v0.1.0 on the main HEAD SHA and push it**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
SHA=$(git rev-parse origin/main)
git tag -a v0.1.0 "$SHA" -m "Awesome Capella 0.1.0"
git push origin v0.1.0
git tag -l v0.1.0
```

Expected: the tag lists locally after push. The tagged SHA must equal the SHA recorded at the end of Task 5.

- [ ] **Step 4: Publish the GitHub Release with the exact footer line**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
cat > release-notes-v0.1.0.md <<'EOF'
# Awesome Capella 0.1.0

First tagged release of the curated Capella and Arcadia resource list.

## Added

- 73 verified entries across nine sections: Arcadia method, Capella core,
  addons and extensions, scripting and automation, collaboration and model
  management, books, courses, and training, community and events, example
  models and case studies, commercial offers.
- Release-standard packaging: CITATION.cff, RELEASE-INFO.txt, COPYRIGHT and
  NOTICE, private security advisory route, bug report form and chooser,
  release gate CI, and a Pages landing page.

## Licence

See LICENSE in the repository (CC0-1.0).

Licence enquiries: https://labs.jgsystemsconsulting.com/licensing.html
EOF
gh release create v0.1.0 -R jgsystemsconsulting/awesome-capella \
  --title "v0.1.0" --notes-file release-notes-v0.1.0.md
rm release-notes-v0.1.0.md
gh release view v0.1.0 -R jgsystemsconsulting/awesome-capella --json body --jq .body | grep -c "https://labs.jgsystemsconsulting.com/licensing.html"
```

Expected: the release is published and the grep count is at least 1 (the exact footer line `Licence enquiries: https://labs.jgsystemsconsulting.com/licensing.html` is present verbatim, D10).

- [ ] **Step 5: Apply branch protection (first-time PUT, solo-maintainer shape)**

```bash
gh api -X PUT repos/jgsystemsconsulting/awesome-capella/branches/main/protection \
  --input - <<'EOF'
{
  "required_status_checks": {"strict": true, "contexts": ["validate"]},
  "enforce_admins": false,
  "required_pull_request_reviews": {"required_approving_review_count": 0},
  "restrictions": null,
  "allow_force_pushes": {"enabled": false},
  "allow_deletions": {"enabled": false}
}
EOF
gh api repos/jgsystemsconsulting/awesome-capella/branches/main/protection \
  --jq '{contexts: .required_status_checks.contexts, force: .allow_force_pushes.enabled, del: .allow_deletions.enabled, admins: .enforce_admins.enabled, reviews: .required_pull_request_reviews.required_approving_review_count}'
```

Expected GET: `contexts` contains `validate`, `force` false, `del` false, `admins` false, `reviews` 0. If the PUT fails on permissions (403/404), do not retry blindly and do not mark RR-B-23 done: record it in the PR as the named maintainer action with this exact command, and continue to Task 7 (the `--gh` audit will then show RR-B-23 WARN, which is reported, not hidden).


- [ ] **Step 6: Amend DISTRIBUTION.md channel statuses after platform success**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
# set Releases, Pages, About/homepage rows from pending to live/submitted/applied with today's date
# edit docs/DISTRIBUTION.md accordingly, then:
git add docs/DISTRIBUTION.md
git commit -m "docs: mark distribution channels live after 0.1.0 platform steps"
git push origin main
```

Expected: ledger rows match actual platform state; no channel still says pending for Releases/Pages/About after success.

Done when: Pages returns 200 from the /docs source, homepageUrl is the Pages URL with six topics, tag v0.1.0 exists locally and on origin on the merge SHA, Release v0.1.0 is published with the exact footer line, and protection GET returns the expected shape (or the failure is recorded as the named maintainer action in the PR).

### Task 7: Acceptance verification (AC1-9)

**Files:**
- Modify: none (verification only; any fix loops back to its source task)

**Interfaces:**
- Consumes: the merged main, the tag and Release from Task 6, the gate and checker scripts.
- Produces: the recorded evidence block for the PR (final audit output, AC1-9 results) that the session notes cite when claiming standard-complete.

**Model:** standard

- [ ] **Step 1: Plain audit exits 0 (AC1)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base; echo "exit=$?"
```

Expected: `0 FAIL, 1 WARN, N PASS` and `exit=0`. The single WARN is the accepted RR-B-32 improvement-form glob row (D8). Any other WARN or any FAIL means a fix loop back to its task, then re-run.

- [ ] **Step 2: Platform and link audit (AC3)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base --gh --links; echo "exit=$?"
```

Expected: `exit=0`; rows RR-B-20 (Pages URL shown), RR-B-21 (description true, topics 6, homepage set), RR-B-22 (Release published with licence-enquiry URL), RR-B-23 (branch protection configured), RR-B-25 (all links resolve) all PASS. If a README issue-template URL 404s under the link check, replace that markdown link with the plain issues URL `https://github.com/jgsystemsconsulting/awesome-capella/issues` (Support and Usage sections only), commit, re-run Steps 5-6 of Task 5's flow through a small follow-up PR, and re-run this step. If RR-B-23 shows WARN because Task 6 Step 5 was blocked, report it as the named maintainer residual rather than looping.

- [ ] **Step 3: Gate and checker (AC2, AC4)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
python scripts/check_release.py; echo "exit=$?"
python scripts/check_entries.py; echo "exit=$?"
```

Expected: gate prints `release gate: PASS (scanned N files)` with N >= 1, exit 0; checker prints `entries: 73` and `format: OK`, exit 0.

- [ ] **Step 4: Family triad on main (AC5)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
gh workflow run link-check-pr.yml --ref main
sleep 10
RUN_ID=$(gh run list --workflow=link-check-pr.yml --limit 1 --json databaseId --jq '.[0].databaseId')
gh run watch "$RUN_ID" --exit-status; echo "triad exit=$?"
```

Expected: the lychee, awesome-lint, and markdownlint jobs all conclude green. A red awesome-lint or markdownlint job means the README section prose needs a fix; entries stay untouched.

- [ ] **Step 5: Em-dash and licence checks (AC7, AC9)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
grep -n "—" README.md SECURITY.md CHANGELOG.md docs/DISTRIBUTION.md docs/index.html
echo "em-dash grep exit=$? (1 means clean)"
gh api repos/jgsystemsconsulting/awesome-capella/license --jq .license.spdx_id
```

Expected: grep finds nothing (exit 1) across the five customer-surface files; the licence API returns `CC0-1.0` (not `NOASSERTION`).

- [ ] **Step 6: Confirm the PR carries the MANUAL closures (AC6) and record the evidence**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella"
gh pr list --state merged --limit 1 --json number,body --jq '.[0].body' | grep -c "MANUAL items closed"
```

Expected: count at least 1. Then post a comment on the merged PR with the final audit outputs from Steps 1-2, the triad run id, and the AC1-9 checklist. AC8 is evidenced by Task 5 Step 1 (workflow scope confirmed or refreshed before the push succeeded). Nothing is committed in this task; the evidence lives in the PR comment and the session notes.

Done when: all nine acceptance criteria have a recorded PASS (or the two named residuals: the accepted RR-B-32 WARN and, only if the PUT was blocked, RR-B-23 as a maintainer action with the exact command), and the evidence comment is on the PR.

## Acceptance criteria coverage

| AC | Where |
|----|-------|
| AC1 plain audit exit 0 | Task 7 Step 1 (tag from Task 6 closes RR-B-18) |
| AC2 gate exit 0 | Task 3 Step 2 (red), Task 4 Step 3 and Task 7 Step 3 (green) |
| AC3 --gh --links rows PASS | Task 6 Steps 1-2, 4-5; Task 7 Step 2 |
| AC4 checker exit 0, 73 entries | Task 1 Step 8, Task 2 Step 5, Task 7 Step 3 |
| AC5 triad green | Task 5 Step 4 (PR), Task 7 Step 4 (main) |
| AC6 MANUAL items in PR | Task 5 Step 3, Task 7 Step 6 |
| AC7 no em dash | Task 2 Step 5, Task 4 Step 3, Task 7 Step 5 |
| AC8 workflow scope | Task 5 Step 1 |
| AC9 licence spdx id | Task 1 Step 1, Task 7 Step 5 |

Locked decisions D1-D11 map onto: D1/D2/D3 (Global Constraints plus Task 1 and Task 3), D4 (Task 2 plus Task 6 Steps 3-4), D5 (Task 4 plus Task 6 Steps 1-2 plus the Task 5 PR body), D6 (Task 2 README sections plus PR body), D7 and D8 (Task 3 Step 5 plus Task 4 ledger plus PR body), D9 (Task 2 SECURITY.md), D10 (Task 6 fixed order), D11 (no hub edits anywhere; family pointer untouched).
