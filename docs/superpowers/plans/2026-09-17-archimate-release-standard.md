# Awesome ArchiMate Release Repo Standard Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bring `jgsystemsconsulting/awesome-archimate` to Release Repo Standard v1.14 RR-B Base: audit exits 0, release identity v0.1.0 end to end, release-gate CI, Pages landing live, About/homepage/protection applied, 17-entry seed byte-identical.

**Architecture:** One spoke-local change set on a single branch, cloned from the Capella RR-B close executed the same day: legal and identity files, Keep-a-Changelog version 0.1.0, SECURITY advisory route, README Install/Usage/Licence/Support/Version sections, `scripts/check_release.py` gate plus `validate.yml`, list-adapted issue forms plus a PR template, self-contained `docs/index.html` Pages landing, and `docs/DISTRIBUTION.md` ledger. All files merge in one PR, then fixed-order platform steps run against main HEAD: merge, Pages enable, About plus homepage, tag v0.1.0 plus GitHub Release, branch protection.

**Tech Stack:** Python 3 stdlib (gate script), GitHub Actions (`actions/checkout@11d5960a326750d5838078e36cf38b85af677262`, `actions/setup-python@v5`), `gh` CLI for Pages/About/Release/protection API calls, Git Bash on Windows.

**Spec:** `docs/superpowers/specs/2026-09-17-archimate-release-standard.md` (normative; locked decisions D1-D11, acceptance criteria AC1-9)

## Global Constraints

Every task implicitly includes these. Values are verbatim from the spec.

- Target repo: `C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate`, branch `main`, remote `https://github.com/jgsystemsconsulting/awesome-archimate`. All file work is spoke-local; the hub `awesome-mbse` is not touched (this plan file is the only hub artifact).
- Profile RR-B Base only (D1). No MCP/skills/research rows. Licence stays CC0-1.0, unchanged (D2). Standalone build model (D3).
- Version **0.1.0**, dated **2026-09-17**, sourced from the CHANGELOG top entry `## [0.1.0] - 2026-09-17`, propagated to RELEASE-INFO.txt, CITATION.cff, tag `v0.1.0`, GitHub Release (D4).
- About description exactly: `Curated ArchiMate resources for enterprise architecture and MBSE practitioners`. Topics exactly six: `archimate`, `awesome`, `awesome-list`, `enterprise-architecture`, `mbse`, `togaf` (the first five are already set; `togaf` is the only add; the auditor requires at least 6).
- Pages URL (homepage value): `https://jgsystemsconsulting.github.io/awesome-archimate/`.
- Licence-enquiry URL everywhere required: `https://labs.jgsystemsconsulting.com/licensing.html` (README Licence, landing page, Release notes).
- SECURITY.md: private advisory route only, exact line `We aim to acknowledge reports within 7 days`, no email address anywhere, no em dash (D9).
- Release notes footer line exactly: `Licence enquiries: https://labs.jgsystemsconsulting.com/licensing.html`.
- `scripts/check_release.py` (RR-B-15): REQUIRED list has **no `scripts/check_entries.py`** (archimate ships no entry checker; `lint.yml` awesome-lint plus markdownlint is the format gate). Full REQUIRED list: `LICENSE`, `COPYRIGHT`, `NOTICE`, `README.md`, `CHANGELOG.md`, `RELEASE-INFO.txt`, `CITATION.cff`, `SECURITY.md`, `.gitignore`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `docs/DISTRIBUTION.md`, `docs/index.html`, `scripts/check_release.py`. Header scan scope is `scripts/*.py` with sentinel `Copyright (c) 2026 JG Systems Consulting Ltd` plus `SPDX-License-Identifier: CC0-1.0`. The gate exits 0 and prints a scanned-file count of at least 1.
- `.github/workflows/validate.yml`: job id `validate`, triggers `push` and `pull_request` on `main` plus `workflow_dispatch`, `permissions: contents: read`, checkout pinned to the full SHA used by the **archimate triad** (`actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4`), not Capella's unpinned `@v4`. Use `actions/setup-python@v5` with Python `"3.12"` as Capella does, then run `python scripts/check_release.py`.
- Platform order is fixed (D10): merge release commit to main, enable Pages from `/docs`, set About plus homepageUrl only after Pages serves, tag v0.1.0 on that main HEAD SHA and publish the Release, then branch protection.
- README: the 17 seed-entry bullets, their ordering, tags, and the flat 8-link `## Contents` block stay byte-identical, as does the badge line 1. Freeze is proven by hashing or diffing the 25 `- [` lines (17 entries plus 8 Contents links) against pre-edit `git show origin/main:README.md`; counts alone are not enough. New sections append below `## Contributing` only.
- Family triad workflows `links.yml`, `lint.yml`, `stale.yml` stay untouched. `lint.yml` has no `workflow_dispatch`; its green run comes from the release push to main (AC4/AC5). `links.yml` is run via `workflow_dispatch`.
- `suggest-resource.yml` is ADDED as the improvement channel (D8). The auditor's improvement-form glob matches `improv`/`enhanc` in the filename and will not match, so the RR-B-32 WARN is expected and accepted; do not rename the form to silence the glob.
- Family pointer stays text-only; no hub FAMILY.md hyperlink (D11).
- No em dash in README.md, SECURITY.md, CHANGELOG.md, docs/DISTRIBUTION.md, docs/index.html, and no `support@jgsystemsconsulting.com` occurrence on that surface (AC7). No machine-local paths in any new file (RR-B-34). New YAML/CFF written as plain UTF-8 without BOM (RR-B-33).
- All commits use the repo's configured noreply identity `245595077+jgsystemsconsulting@users.noreply.github.com` (already set; RR-B-27).
- Auditor command (run from the spoke root): `python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base [--gh] [--links]`. Defaults already carry `--org "JG Systems Consulting Ltd"`. This is the spec AC1 command in equivalent form: the hub has no `tools/` directory, so `python tools/audit.py --repo ../awesome-archimate --profile base` from the spec resolves to this skill path.

## Codebase context

The spoke ships 10 tracked files (`git ls-files`): README (17 entries across eight sections: Specifications and standards, Certification, The Archi tool, Plugins and collaboration, Books, Example models, TOGAF alignment, Communities; an 8-link flat `## Contents`; awesome badge on line 1; a text-only family pointer; ends at `## Contributing`), CC0-1.0 LICENSE, CONTRIBUTING.md (inclusion bar, entry format, tag vocabulary, year rule, canonical-URL rule, editorial neutrality, local checks), CODE_OF_CONDUCT.md, SECURITY.md (line 9 publishes `support@jgsystemsconsulting.com`; line 3 has the repo's only customer-surface em dash; must both go), CHANGELOG.md (Keep a Changelog 1.1.0 header, `## [Unreleased]` only), `.markdownlint-cli2.jsonc` (`MD013: false`, so no line-length constraint), and the triad `.github/workflows/links.yml` (lychee, PR plus Monday 18:00 UTC schedule plus `workflow_dispatch`, advisory on PRs), `lint.yml` (awesome-lint@2.3.0 plus markdownlint on PR and push to main only, no dispatch), `stale.yml` (monthly freshness report). Action refs in the triad are pinned to full-length SHAs with `# vN` comments.

GitHub state verified 2026-09-17: license spdx_id already `CC0-1.0`; description is the README tagline; homepageUrl empty; five topics already set (`archimate`, `awesome`, `awesome-list`, `enterprise-architecture`, `mbse`). Missing relative to the standard: everything in the spec's file inventory; there are no scripts, docs, issue forms, or PR template today. Task content clones the executed Capella spoke files at `C:/Users/gower/OneDrive/Documents/GitHub/awesome-capella` (COPYRIGHT, NOTICE, CITATION.cff, RELEASE-INFO.txt shape, SECURITY.md shape, `scripts/check_release.py`, `.github/workflows/validate.yml`, `docs/index.html`, `docs/DISTRIBUTION.md`, issue forms, PR template) with ArchiMate strings.

## Research

- https://github.com/jgsystemsconsulting/awesome-archimate (target spoke; About/topics/license state verified 2026-09-17 via `gh repo view`)
- https://jgsystemsconsulting.github.io/awesome-archimate/ (planned Pages URL; 404 until RR-B-20 enablement)
- https://labs.jgsystemsconsulting.com/licensing.html (licence-enquiry URL)
- https://github.com/jgsystemsconsulting/awesome-archimate/security/advisories/new (private advisory route)
- https://github.com/jgsystemsconsulting/awesome-capella (executed pattern spoke, cloned file shapes)
- Standard: `C:/Users/gower/.zcode/skills/release-repo-standard/references/release-repo-standard.md` (v1.14, normative); auditor and `landing_taste.py` under the same skill's `tools/`
- `docs/superpowers/research/2026-09-17-archimate-release-standard-research.md` (canonical URLs, version facts)
- `docs/superpowers/context/2026-09-17-archimate-release-standard-context.md` (spoke inventory, family constraints, clone-target decision)
- `docs/superpowers/specs/2026-09-17-repo-release-standard-capella.md` (pattern source spec, executed 2026-09-17)

---

### Task 1: Baseline snapshot, legal, identity, and hygiene files

**Files:**
- Create: `COPYRIGHT`
- Create: `NOTICE`
- Create: `CITATION.cff`
- Create: `.gitignore`
- Modify: `LICENSE` (append one trailing line; CC0 body untouched)

**Interfaces:**
- Consumes: nothing.
- Produces: `COPYRIGHT`, `NOTICE`, `CITATION.cff` with version `0.1.0`; LICENSE carrying the org string the auditor greps for; `/tmp/archimate-audit-baseline.txt` (pre-edit audit snapshot) and `/tmp/archimate-entries-before.txt` (the 25 frozen `- [` lines). Task 2 and Task 3 rely on version `0.1.0`, the org string `JG Systems Consulting Ltd`, and the baseline snapshot for the closing diff.

**Model:** flash

- [ ] **Step 1: Record the baseline, the licence detector state, and the entry freeze**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
git status --porcelain   # expect empty; if not, stop and report
gh api repos/jgsystemsconsulting/awesome-archimate/license --jq .license.spdx_id
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base | tee /tmp/archimate-audit-baseline.txt; echo "baseline exit=$?"
git show origin/main:README.md | grep '^- \[' > /tmp/archimate-entries-before.txt
wc -l < /tmp/archimate-entries-before.txt
grep '^- \[' README.md | diff - /tmp/archimate-entries-before.txt && echo "working tree matches origin/main"
grep '^- \[' README.md | sha256sum
```

Expected: spdx_id `CC0-1.0` (AC9 pre-check); porcelain empty; the audit output is saved to `/tmp/archimate-audit-baseline.txt` and its FAIL/WARN/PASS counts are noted verbatim for the PR (this is the first-ever baseline for the spoke; do not quote a count that was not run); `wc -l` prints `25`; the diff is empty; the sha256 of the 25 `- [` lines is recorded for the PR body. Keep both `/tmp` files for Task 7; if the session loses them, regenerate with the same `git show` command (byte-identical while entries stay untouched).

- [ ] **Step 2: Create the branch**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
git checkout main && git pull origin main
git checkout -b release/0.1.0-standard
```

- [ ] **Step 3: Write `COPYRIGHT`** (single line, exactly):

```
Copyright (c) 2026 JG Systems Consulting Ltd. All rights reserved.
```

- [ ] **Step 4: Write `NOTICE`** (no-third-party-code variant per D2):

```
Awesome ArchiMate
Copyright (c) 2026 JG Systems Consulting Ltd.

Third-party components are not distributed with this repository. The list only
links to external resources; each linked resource remains under its own licence.
```

- [ ] **Step 5: Write `CITATION.cff`** (Capella executed shape plus archimate strings; plain UTF-8, no BOM):

```yaml
cff-version: 1.2.0
message: "If you use this list in your work, please cite it using this metadata."
title: "Awesome ArchiMate"
version: "0.1.0"
date-released: "2026-09-17"
authors:
  - entity:
      name: "JG Systems Consulting Ltd"
license: CC0-1.0
repository-code: "https://github.com/jgsystemsconsulting/awesome-archimate"
url: "https://github.com/jgsystemsconsulting/awesome-archimate"
preferred-citation:
  type: generic
  title: "Awesome ArchiMate"
  authors:
    - entity:
        name: "JG Systems Consulting Ltd"
  year: 2026
  version: "0.1.0"
  repository-code: "https://github.com/jgsystemsconsulting/awesome-archimate"
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

- [ ] **Step 7: Append the org line to `LICENSE`**

The CC0-1.0 Universal legal text stays untouched. Append exactly one trailing line (one blank line before it):

```
Copyright (c) 2026 JG Systems Consulting Ltd.
```

Then re-check the GitHub detector (AC9):

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
git diff LICENSE | tail -5
gh api repos/jgsystemsconsulting/awesome-archimate/license --jq .license.spdx_id
```

Expected after this file merges: spdx_id stays `CC0-1.0`. If it flips to `NOASSERTION` (check again after the PR merges in Task 5), restore the canonical CC0 text, keep the org string only in COPYRIGHT/NOTICE, and record the RR-B-01 strategy residual in the PR as the spec's RR-B-01 row directs.

- [ ] **Step 8: Verify**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
python -c "from pathlib import Path; p=Path('CITATION.cff'); print(p.read_bytes()[:3]); assert p.read_bytes()[:3] != b'\xef\xbb\xbf'"
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base | grep -E "RR-B-01|RR-B-02|RR-B-03|RR-B-04|RR-B-09|RR-B-13|RR-B-27|RR-B-31|RR-B-33|TMPL"
```

Expected: the BOM bytes are not `efbbbf`; in the grep output RR-B-01, RR-B-02 (x2), RR-B-03 (`0 .py without header`), RR-B-04, RR-B-09 (`versions agree (0.1.0) across 1 files`, CITATION.cff is the only version-bearing file until Task 2), RR-B-13, RR-B-27, RR-B-31, RR-B-33, and TMPL all read PASS. RR-B-18 shows FAIL (`tag v0.1.0 missing`), which is expected until Task 6.

- [ ] **Step 9: Commit**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
git add COPYRIGHT NOTICE CITATION.cff .gitignore LICENSE
git commit -m "chore: add legal identity files and org line on LICENSE (RR-B-01,02,13,31)"
```

Done when: the targeted audit rows PASS with no FAIL among them, CITATION.cff has no BOM, the baseline and freeze files exist in `/tmp`, and the commit is on `release/0.1.0-standard`.

### Task 2: Version alignment, security route, README sections

**Files:**
- Modify: `CHANGELOG.md` (keep header; add `## [0.1.0] - 2026-09-17`, keep empty `[Unreleased]` above it)
- Create: `RELEASE-INFO.txt`
- Modify: `SECURITY.md` (full rewrite)
- Modify: `README.md` (append five sections after `## Contributing`; the 25 `- [` lines untouched)

**Interfaces:**
- Consumes: version `0.1.0` and the org string from Task 1; `/tmp/archimate-entries-before.txt` for the freeze check.
- Produces: `CHANGELOG.md` top entry `## [0.1.0] - 2026-09-17` (the version source, D4); `RELEASE-INFO.txt` with `Tag: v0.1.0`; README sections and the issue-form URLs that Task 3's forms, Task 4's landing page, and Task 6's Release notes mirror.

**Model:** standard

- [ ] **Step 1: Rewrite `CHANGELOG.md`** (entire file becomes; the two existing seed bullets move under the 0.1.0 entry):

```markdown
# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

## [0.1.0] - 2026-09-17

### Added

- Initial launch of Awesome ArchiMate: 17 entries across eight content sections, all
  links verified at open (launch lychee run exit 0).
- Family-standard files: README, CONTRIBUTING, LICENSE (CC0-1.0), CODE_OF_CONDUCT,
  SECURITY, and three CI workflows (links, lint, freshness).

### Notes

- Release-standard pass (Release Repo Standard v1.14, RR-B Base): COPYRIGHT, NOTICE,
  CITATION.cff, RELEASE-INFO.txt, release gate CI, Pages landing, issue forms, PR
  template, and the distribution ledger.
```

- [ ] **Step 2: Write `RELEASE-INFO.txt`** with the real UTC timestamp (D4: Built is the UTC ISO-8601 time at release-commit authoring):

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
printf 'Product: Awesome ArchiMate\nVersion: 0.1.0\nBuilt: %s\nTag: v0.1.0\n' "$TS" > RELEASE-INFO.txt
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
[GitHub security advisory](https://github.com/jgsystemsconsulting/awesome-archimate/security/advisories/new).
Please do not open a public issue for a suspected malicious or hijacked link
until it has been reviewed.

For non-sensitive fixes (a dead or moved link, a CI misbehavior), open a
pull request with the fix directly.

We aim to acknowledge reports within 7 days.

## Scope notes

- A linked resource that turns out to be malicious, hijacked, or compromised.
- The repository's automation: the link-check, lint, and freshness workflows.

Out of scope: vulnerabilities in the tools and sites the list links to; report
those upstream.
```

- [ ] **Step 4: Append the README sections after the `## Contributing` section** (end of file; one blank line before `## Install`; do not touch anything above):

````markdown
## Install

Nothing to install. This list is a curated index: browse it here on GitHub,
or clone it:

```bash
git clone https://github.com/jgsystemsconsulting/awesome-archimate.git
```

## Usage

- Browse the sections under [Contents](#contents), or search the page with
  your browser's find function.
- Open any entry's link to reach the upstream resource; the list never
  re-hosts content.
- To suggest a resource, use the
  [suggestion form](https://github.com/jgsystemsconsulting/awesome-archimate/issues/new?template=suggest-resource.yml)
  (added with this release).
- To report a wrong or dead entry, use the
  [bug report form](https://github.com/jgsystemsconsulting/awesome-archimate/issues/new?template=bug_report.yml)
  (added with this release).

## Licence

Released under the [CC0-1.0](LICENSE) licence (public domain dedication).
Linked resources remain under their own licences.

To request a commercial or academic licence, or if you are unsure which
licence you need: https://labs.jgsystemsconsulting.com/licensing.html

## Support

- Bug or dead link: [bug report form](https://github.com/jgsystemsconsulting/awesome-archimate/issues/new?template=bug_report.yml)
- Suggest a resource (the list's improvement channel):
  [suggestion form](https://github.com/jgsystemsconsulting/awesome-archimate/issues/new?template=suggest-resource.yml)
- Security issues: [private security advisory](https://github.com/jgsystemsconsulting/awesome-archimate/security/advisories/new)
  (see [SECURITY.md](SECURITY.md))
- Capella and Arcadia resources belong on the sibling list:
  [awesome-capella issues](https://github.com/jgsystemsconsulting/awesome-capella/issues)

## Version

Current release: 0.1.0 (2026-09-17). See [CHANGELOG.md](CHANGELOG.md) and
[RELEASE-INFO.txt](RELEASE-INFO.txt).
````

- [ ] **Step 5: Verify**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
grep '^- \[' README.md | diff - /tmp/archimate-entries-before.txt && echo "25 `- [` lines byte-identical"
grep -c '^- \[' README.md
grep -n $'\u2014' README.md CHANGELOG.md SECURITY.md RELEASE-INFO.txt
grep -n "support@jgsystemsconsulting.com" README.md SECURITY.md CHANGELOG.md
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base | grep -E "RR-B-05|RR-B-07|RR-B-08|RR-B-09|RR-B-10|RR-B-28"
npx -y markdownlint-cli2 "README.md" 2>/dev/null || echo "node not available locally; CI triad is the guard"
```

Expected: the freeze diff is empty and `grep -c` prints `25` (AC4); the em-dash grep finds nothing (the old SECURITY.md em dash is gone; AC7 partial); the email grep finds nothing (the old line 9 is gone); audit rows RR-B-05 PASS (`README sections present and licence-enquiry URL in Licence section`), RR-B-07 PASS (`advisory route documented, no email`), RR-B-09 PASS (`versions agree (0.1.0) across 3 files`), RR-B-10 PASS, RR-B-28 PASS. CHANGELOG presence is required but `audit.py` does not emit a separate RR-B-08 PASS row (only FAILs if the file is missing). If markdownlint runs and flags the new sections, fix the section prose (entries stay untouched) before commit; if node is absent, the triad run in Task 5 Step 4 is the binding guard.

- [ ] **Step 6: Commit**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
git add CHANGELOG.md RELEASE-INFO.txt SECURITY.md README.md
git commit -m "feat: v0.1.0 changelog, release info, security advisory route, README sections (RR-B-05,07..10,28)"
```

Done when: freeze diff clean at 25 lines, version rows RR-B-09/10 PASS with value `0.1.0`, RR-B-07 PASS with no email, RR-B-05 PASS, no em dash and no email in the touched files, commit on the branch.

### Task 3: Release gate, validate workflow, issue forms, PR template

**Files:**
- Create: `scripts/check_release.py`
- Create: `.github/workflows/validate.yml`
- Create: `.github/ISSUE_TEMPLATE/bug_report.yml`
- Create: `.github/ISSUE_TEMPLATE/config.yml`
- Create: `.github/ISSUE_TEMPLATE/suggest-resource.yml` (ADDED per D8)
- Create: `.github/PULL_REQUEST_TEMPLATE.md`

**Interfaces:**
- Consumes: the REQUIRED file set, which Tasks 1, 2, and 4 create; header sentinel text `Copyright (c) 2026 JG Systems Consulting Ltd` matching Task 1's files.
- Produces: gate command `python scripts/check_release.py` (exit 0 once Task 4 lands the two docs files); workflow `validate.yml` whose check name feeds branch protection in Task 6; the three issue-form URLs referenced by the README Support/Usage sections (Task 2) and the landing page (Task 4).

**Model:** flash

- [ ] **Step 1: Write `scripts/check_release.py`** (Capella executed file with one delta: `scripts/check_entries.py` removed from REQUIRED because archimate ships no entry checker):

```python
# Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE.
# SPDX-License-Identifier: CC0-1.0
"""Release gate (RR-B-15) for Awesome ArchiMate (Base + list files)."""
import pathlib
import re
import subprocess
import sys

fails: list[str] = []

REQUIRED = [
    "LICENSE", "COPYRIGHT", "NOTICE", "README.md", "CHANGELOG.md",
    "RELEASE-INFO.txt", "CITATION.cff", "SECURITY.md", ".gitignore",
    "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "docs/DISTRIBUTION.md",
    "docs/index.html", "scripts/check_release.py",
]
for f in REQUIRED:
    if not pathlib.Path(f).is_file():
        fails.append(f"required file missing: {f}")

tracked = subprocess.run(
    ["git", "ls-files"], capture_output=True, text=True, check=True
).stdout.splitlines()
FORBIDDEN_PATH_PARTS = [
    "__pycache__", ".venv", ".worktrees", ".pytest_cache", ".ruff_cache", ".bak",
]
for f in tracked:
    if any(part in f for part in FORBIDDEN_PATH_PARTS):
        fails.append(f"forbidden tracked path: {f}")

FORBIDDEN_CONTENT = [
    re.compile(r"BEGIN [A-Z ]*PRIVATE KEY"),
]
SCAN_GLOBS = ["scripts/*.py", "*.md", "*.txt", "*.cff", "docs/**/*.md", "docs/**/*.html"]
scanned = 0
for g in SCAN_GLOBS:
    for path in pathlib.Path(".").glob(g):
        if not path.is_file():
            continue
        scanned += 1
        text = path.read_text(encoding="utf-8", errors="ignore")
        for rx in FORBIDDEN_CONTENT:
            if rx.search(text):
                fails.append(f"forbidden content in {path}: {rx.pattern}")

HEADER_SENTINEL = "Copyright (c) 2026 JG Systems Consulting Ltd"
for path in pathlib.Path("scripts").glob("*.py"):
    head = path.read_text(encoding="utf-8", errors="ignore")[:400]
    if HEADER_SENTINEL not in head:
        fails.append(f"header missing: {path}")
    if "SPDX-License-Identifier: CC0-1.0" not in head:
        fails.append(f"SPDX missing: {path}")

if scanned < 1:
    fails.append("SCAN_GLOBS matched zero files")

if fails:
    print("RELEASE GATE FAILED:")
    for f in fails:
        print(f"  - {f}")
    sys.exit(1)
print(f"release gate: PASS (scanned {scanned} files)")
```

- [ ] **Step 2: Run the gate and prove it fails for the right reason** (Task 4 has not run yet, so the docs files are the expected misses):

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
python scripts/check_release.py; echo "exit=$?"
mv CITATION.cff CITATION.cff.hold && python scripts/check_release.py; echo "exit=$?"; mv CITATION.cff.hold CITATION.cff
```

Expected: the first run prints `exit=1` listing exactly `required file missing: docs/DISTRIBUTION.md` and `required file missing: docs/index.html` and nothing else. The negative probe adds `required file missing: CITATION.cff` to the list (proves the REQUIRED check fires; this is the failing-test cycle for the gate).

- [ ] **Step 3: Write `.github/workflows/validate.yml`** (job id `validate` so the required check name resolves to `validate`; separate file; triad untouched):

```yaml
name: validate

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Run release gate
        run: python scripts/check_release.py
```

- [ ] **Step 4: Write `.github/ISSUE_TEMPLATE/bug_report.yml`** (Capella executed shape with archimate strings):

```yaml
name: Bug report
description: Report a dead link, wrong entry, or list defect
title: "[bug] "
labels: ["bug"]
body:
  - type: input
    id: entry-url
    attributes:
      label: Affected entry URL (if any)
      description: Canonical URL of the list entry, if this is about one resource
    validations:
      required: false
  - type: dropdown
    id: problem-type
    attributes:
      label: Problem type
      options:
        - Dead or broken link
        - Wrong or misleading description
        - Duplicate entry
        - Wrong tags or year
        - Formatting or CI failure
        - Other
    validations:
      required: true
  - type: input
    id: list-version
    attributes:
      label: List version
      description: From README Version section or git tag (for example 0.1.0)
      placeholder: "0.1.0"
    validations:
      required: true
  - type: textarea
    id: details
    attributes:
      label: Details
      description: What you expected and what you saw
    validations:
      required: true
  - type: checkboxes
    id: hygiene
    attributes:
      label: Checks
      options:
        - label: I searched existing issues for duplicates
          required: true
```

- [ ] **Step 5: Write `.github/ISSUE_TEMPLATE/config.yml`** (exact contact URLs from the spec's RR-B-32 row; `suggest-resource.yml` is the improvement channel, D8):

```yaml
blank_issues_enabled: false
contact_links:
  - name: Security advisory
    url: https://github.com/jgsystemsconsulting/awesome-archimate/security/advisories/new
    about: Report a security issue privately
  - name: awesome-capella issues
    url: https://github.com/jgsystemsconsulting/awesome-capella/issues
    about: Issues about the Capella and Arcadia sibling list
```

- [ ] **Step 6: Write `.github/ISSUE_TEMPLATE/suggest-resource.yml`** (resource name, URL, section, why it fits, licence checkbox; section options are the list's eight sections; inclusion-bar items come from CONTRIBUTING.md):

```yaml
name: Suggest a resource
description: Suggest an ArchiMate or Archi resource to add to the list
title: "[Suggestion] <resource name>"
labels: ["suggestion"]
body:
  - type: input
    id: name
    attributes:
      label: Resource name
      placeholder: e.g. Archi handbook or plugin page
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
    id: why
    attributes:
      label: Why it fits the list
      description: One or two sentences against the inclusion bar in CONTRIBUTING.md (factual, no hype)
    validations:
      required: true
  - type: dropdown
    id: section
    attributes:
      label: Which section does it belong in?
      options:
        - Specifications and standards
        - Certification
        - The Archi tool
        - Plugins and collaboration
        - Books
        - Example models
        - TOGAF alignment
        - Communities
    validations:
      required: true
  - type: checkboxes
    id: bar
    attributes:
      label: Inclusion bar (see CONTRIBUTING.md)
      options:
        - label: Genuinely about ArchiMate, the Archi tool and its plugins, or EA modeling practice around them
          required: true
        - label: Substantive (teaches, demonstrates, specifies, or provides something usable); not pure marketing
          required: true
        - label: The link is live right now
          required: true
        - label: It isn't already in the list (canonical-URL rule, CONTRIBUTING.md)
          required: true
        - label: Licence and access are clean (publicly accessible; we link, we never re-host; not paywalled or request-only)
          required: true
```

- [ ] **Step 7: Write `.github/PULL_REQUEST_TEMPLATE.md`** (guardrails from the spec's RR-B-12 row: entries untouched, links checked, no em dash, version files updated together; format rules mirror CONTRIBUTING.md):

```markdown
<!-- Thanks for contributing! Check every box; CI enforces most of these. -->

## What I'm adding / changing

<!-- one line -->

## Inclusion bar (CONTRIBUTING.md)

- [ ] On-topic for ArchiMate, the Archi tool and its plugins, or EA modeling practice around them
- [ ] Substantive: teaches, demonstrates, specifies, or provides something usable; not pure marketing
- [ ] Link is live right now (lychee CI checks it)
- [ ] Not a duplicate (canonical-URL rule, CONTRIBUTING.md)
- [ ] Publicly accessible; we link, we never re-host; not paywalled or request-only

## Entry format (CONTRIBUTING.md)

- [ ] `- [Name](url) - Description` with inline-code tags before the `(YYYY)` token; hyphen separator, not an en/em dash
- [ ] Description at most 140 characters, factual, no hype
- [ ] Tags drawn only from the vocabulary, in the fixed order (language, method, tool, has-model, type, spec/standard, paid, year)
- [ ] `(YYYY)` is the resource's most recent author-published version (spoke addendum covers undated pages)

## Housekeeping

- [ ] Existing entries and the `## Contents` block are untouched
- [ ] No em dash anywhere in the diff
- [ ] If this changes version-bearing files (CHANGELOG.md, RELEASE-INFO.txt, CITATION.cff), they are updated together
```

- [ ] **Step 8: Verify**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
python -c "from pathlib import Path
for f in ['.github/workflows/validate.yml', '.github/ISSUE_TEMPLATE/bug_report.yml', '.github/ISSUE_TEMPLATE/config.yml', '.github/ISSUE_TEMPLATE/suggest-resource.yml', '.github/PULL_REQUEST_TEMPLATE.md']:
    b = Path(f).read_bytes()
    assert b[:3] != b'\xef\xbb\xbf', f'BOM in {f}'
print('no BOM')"
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base | grep -E "RR-B-15|RR-B-32|RR-B-33|RR-B-34|RR-B-24"
```

Expected: no BOM in any new YAML/markdown file; RR-B-15 PASS (`gate script: True, CI workflow: True`); RR-B-32 first row PASS (`issue form + chooser present`) and second row WARN (`no improvement/enhancement form (SHOULD per RR-B-32)`), which is the accepted D8 WARN; RR-B-33 PASS; RR-B-34 PASS; RR-B-24 still WARN (`no docs/*.html; mechanical taste overlay skipped`) until Task 4.

- [ ] **Step 9: Commit**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
git add scripts/check_release.py .github/workflows/validate.yml .github/ISSUE_TEMPLATE/bug_report.yml .github/ISSUE_TEMPLATE/config.yml .github/ISSUE_TEMPLATE/suggest-resource.yml .github/PULL_REQUEST_TEMPLATE.md
git commit -m "ci: release gate, validate workflow, issue forms, suggestion channel, PR template (RR-B-15,32)"
```

Done when: the gate exits 1 citing exactly the two not-yet-created docs files (and catches the moved required file in the negative probe), all five new files are BOM-free, RR-B-15 PASS with the accepted RR-B-32 WARN, commit on the branch.

### Task 4: Pages landing page and distribution ledger

**Files:**
- Create: `docs/index.html`
- Create: `docs/.nojekyll` (empty file)
- Create: `docs/DISTRIBUTION.md`

**Interfaces:**
- Consumes: the licence-enquiry URL, the Pages URL, the exact About description, and version 0.1.0 (Global Constraints); the issue-form filenames from Task 3.
- Produces: the two files whose absence made the Task 3 gate red, so `python scripts/check_release.py` exits 0 (AC2); `docs/index.html` carrying the licence-enquiry URL (auditor RR-B-20 file-level row); ledger rows named in the Task 5 PR body.

**Model:** flash

- [ ] **Step 1: Write `docs/index.html`** (Capella executed shape with archimate strings: system fonts only, inline CSS, canonical plus OG tags, licence-enquiry link, focus-visible and reduced-motion rules, no em dash, no CDN, no third-party fonts):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Awesome ArchiMate</title>
  <meta name="description" content="Curated ArchiMate resources for enterprise architecture and MBSE practitioners.">
  <link rel="canonical" href="https://jgsystemsconsulting.github.io/awesome-archimate/">
  <meta property="og:title" content="Awesome ArchiMate">
  <meta property="og:description" content="Curated ArchiMate resources for enterprise architecture and MBSE practitioners.">
  <meta property="og:url" content="https://jgsystemsconsulting.github.io/awesome-archimate/">
  <meta property="og:type" content="website">
  <style>
    :root { color-scheme: light dark; }
    body {
      margin: 0;
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
      line-height: 1.5;
      max-width: 42rem;
      padding: 1.5rem;
    }
    a:focus-visible { outline: 2px solid currentColor; outline-offset: 2px; }
    @media (prefers-reduced-motion: reduce) {
      * { animation: none !important; transition: none !important; }
    }
    header { margin-bottom: 1.5rem; }
    h1 { font-size: 1.75rem; margin: 0 0 0.5rem; }
    .meta { opacity: 0.85; font-size: 0.95rem; }
    ul { padding-left: 1.2rem; }
    footer { margin-top: 2rem; font-size: 0.9rem; opacity: 0.9; }
  </style>
</head>
<body>
  <header>
    <h1>Awesome ArchiMate</h1>
    <p class="meta">Curated ArchiMate resources for enterprise architecture and MBSE practitioners. Version 0.1.0.</p>
  </header>
  <main>
    <p>
      This is a public-domain (CC0) curated index of Open Group ArchiMate
      specifications and certification, the Archi tool and its plugins, books,
      and openable example models. Nothing to install: open the list and follow
      the links.
    </p>
    <h2>First run</h2>
    <ol>
      <li>Open the full list on GitHub (README with searchable Contents).</li>
      <li>Jump to a section that matches your work (specifications, tool, plugins, models).</li>
      <li>Suggest a resource or report a dead link via the repository issue forms.</li>
    </ol>
    <h2>Links</h2>
    <ul>
      <li><a href="https://github.com/jgsystemsconsulting/awesome-archimate">GitHub repository and full README</a></li>
      <li><a href="https://github.com/jgsystemsconsulting/awesome-archimate/blob/main/CONTRIBUTING.md">How to contribute</a></li>
      <li><a href="https://github.com/jgsystemsconsulting/awesome-archimate/issues/new?template=suggest-resource.yml">Suggest a resource</a></li>
      <li><a href="https://github.com/jgsystemsconsulting/awesome-archimate/issues/new?template=bug_report.yml">Report a bug or dead link</a></li>
      <li><a href="https://labs.jgsystemsconsulting.com/licensing.html">Licence enquiries</a></li>
    </ul>
  </main>
  <footer>
    <p>Maintained by JG Systems Consulting Ltd. Licence: <a href="https://github.com/jgsystemsconsulting/awesome-archimate/blob/main/LICENSE">CC0-1.0</a>.</p>
  </footer>
</body>
</html>
```

- [ ] **Step 2: Create `docs/.nojekyll`** (empty) and write `docs/DISTRIBUTION.md`:

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
mkdir -p docs && touch docs/.nojekyll
```

Write `docs/DISTRIBUTION.md` (nine channel rows; RR-B-36 status vocabulary only: `submitted`, `in progress`, `deferred`, `deliberate N/A`, `planned`; every non-submitted row carries a decision plus date):

```markdown
# Distribution ledger

Last reviewed: 0.1.0 (2026-09-17)

Per-channel status for Awesome ArchiMate under Release Repo Standard RR-B-36.

| Channel | Artifact | Status | Decision / notes | Date |
| --- | --- | --- | --- | --- |
| GitHub repo (public) | jgsystemsconsulting/awesome-archimate | submitted | Canonical home of the list. | 2026-09-17 |
| GitHub Releases | v0.1.0 | submitted | Release v0.1.0 published from the CHANGELOG entry with the licence-enquiry footer. | 2026-09-17 |
| GitHub Pages landing | docs/index.html | submitted | Served from main /docs; the repo homepage URL points here. | 2026-09-17 |
| GitHub About, topics, homepage | repo settings | submitted | Exact description, six topics, homepage set to the Pages URL. | 2026-09-17 |
| Org catalogue (labs.jgsystemsconsulting.com) | site entry | planned | Add a list entry alongside the other awesome-mbse spokes. | 2026-09-17 |
| sindresorhus/awesome | list PR | deferred | Acceptability gate not passed: membership bar, review bandwidth, and naming conventions need assessment before submitting. | 2026-09-17 |
| In-host agent and IDE marketplaces (Claude Code, Cursor, Codex, Gemini CLI) | n/a | deliberate N/A | A curated list is browsed on GitHub, not installed into an agent host, so no marketplace manifests apply (RR-B-29). | 2026-09-17 |
| MCP directories (awesome-mcp-servers, Glama, Smithery, PulseMCP) | n/a | deliberate N/A | The list speaks no MCP; RR-M rows are out of profile (RR-B Base only). | 2026-09-17 |
| Community EA and ArchiMate directories | link posts | deferred | Assess each directory's scope and licence bar before posting. | 2026-09-17 |

Multi-page assessment (RR-B-30): content walked; outcome is one HTML landing plus the
README as deep content; nothing justifies a third page.
```

- [ ] **Step 3: Verify**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/landing_taste.py" docs/index.html
python scripts/check_release.py; echo "exit=$?"
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base | grep -E "RR-B-20|RR-B-24|RR-B-28|RR-B-34|RR-B-36"
grep -n $'\u2014' docs/index.html docs/DISTRIBUTION.md
```

Expected: `landing_taste.py` prints `PASS` (this is the RR-B-24 mechanical overlay; the taste-skill pre-flight itself is a MANUAL note recorded in the PR per D5); the gate prints `release gate: PASS (scanned N files)` with N at least 1 and `exit=0` (AC2); RR-B-20 PASS (`docs/index.html contains licence-enquiry URL`), RR-B-24 PASS, RR-B-28 PASS, RR-B-34 PASS, RR-B-36 PASS; the em-dash grep prints nothing.

- [ ] **Step 4: Commit**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
git add docs/index.html docs/.nojekyll docs/DISTRIBUTION.md
git commit -m "feat: Pages landing page and distribution ledger (RR-B-20,24,30,36)"
```

Done when: landing_taste PASS, gate exit 0 with a scanned count of at least 1, RR-B-20/24/28/34/36 PASS, no em dash in either docs file, commit on the branch.

### Task 5: Full audit snapshot, PR with MANUAL closures, merge

**Files:**
- Modify: none in the tree (PR body and platform records only)

**Interfaces:**
- Consumes: the complete branch from Tasks 1-4; `gh` with `workflow` scope; `/tmp/archimate-audit-baseline.txt` and the recorded entry sha256 from Task 1.
- Produces: the merged main HEAD SHA (Task 6 tags this exact SHA); the PR body that closes the spec's MANUAL items (AC6) and records the baseline-to-final audit diff and the keep/drop phrase.

**Model:** standard

- [ ] **Step 1: Confirm workflow push scope (AC8)**

```bash
gh auth status
```

If the token lacks `workflow` scope, run `gh auth refresh -s workflow` and re-check. The push in Step 3 creates `.github/workflows/validate.yml`; without the scope GitHub rejects the whole push.

- [ ] **Step 2: Run the pre-merge audit snapshot and check the keep/drop inventory**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base; echo "exit=$?"
git ls-files
```

Expected audit shape: the only FAIL row is `RR-B-18` (tag v0.1.0 missing until Task 6; the tag ships on this same change set's merge commit). Every other row is PASS except the accepted RR-B-32 improvement-form WARN. Keep/drop inventory (RR-B-35): the `git ls-files` list (now 24 files) contains no maintainer-only prefixes; the PR body records `RR-B-35: git ls-files walked: no maintainer-only candidates tracked`. Compare the FAIL count against `/tmp/archimate-audit-baseline.txt` and cite both numbers in the PR.

- [ ] **Step 3: Push and open the PR with the MANUAL closures**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
git push -u origin release/0.1.0-standard
gh pr create --base main --head release/0.1.0-standard \
  --title "Release standard 0.1.0: legal, gate, landing, ledger" \
  --body-file - <<'EOF'
## Summary

Release Repo Standard v1.14 (RR-B Base) packaging for the list. New: COPYRIGHT, NOTICE, CITATION.cff, RELEASE-INFO.txt, .gitignore, scripts/check_release.py, .github/workflows/validate.yml, bug report and suggestion forms plus chooser, PR template, docs/index.html + docs/.nojekyll, docs/DISTRIBUTION.md. Rewritten: CHANGELOG (Keep a Changelog, [0.1.0]), SECURITY.md (private advisory route, 7-day ack, no email), README Install/Usage/Licence/Support/Version. LICENSE gains one trailing org line; CC0 body untouched. The 17 entries and the 8-link Contents block are byte-identical (25 `- [` lines diffed against pre-edit origin/main; sha256 recorded below). Family triad links.yml / lint.yml / stale.yml untouched.

## Seed freeze

- Baseline audit (pre-change): recorded in session notes; FAIL/WARN/PASS counts quoted here.
- Entry sha256 before and after: identical, 25 `- [` lines.

## MANUAL items closed

- RR-B-06 (D6): list product; Install says nothing to install (browse or clone); Usage covers browse, search, open links, contribute via forms. Depth carried by README Install+Usage plus CONTRIBUTING.md; no docs/usage.md.
- RR-B-12: CONTRIBUTING.md and CODE_OF_CONDUCT.md existed; PR template added this PR.
- RR-B-19: org catalogue row `planned` in docs/DISTRIBUTION.md.
- RR-B-24: landing_taste.py PASS on docs/index.html. MANUAL taste note: page kind is a reference-index landing for EA and MBSE practitioners; minimal and quiet; no hero, no scroll cues, system fonts, single column, footer carries the licence-enquiry link. SEO pass recorded: title, meta description, canonical, OG tags present. Playwright 2-breakpoint screenshots when the tool is available, else named residual.
- RR-B-26: no ASCII diagrams in README; no Mermaid needed for a list; callout/table usage unchanged.
- RR-B-28: new prose written clean; em-dash grep clean across README.md, SECURITY.md, CHANGELOG.md, docs/DISTRIBUTION.md, docs/index.html; old SECURITY.md em dash and support@ email removed.
- RR-B-29 (D7): whole requirement deliberate N/A (a list is not installed into an agent host); ledger row with date.
- RR-B-30 (D5): multi-page assessment done; content walked; outcome: one HTML landing + README deep content; nothing justifies a third page.
- RR-B-35: git ls-files walked: no maintainer-only candidates tracked.
- RR-B-36: ledger at 0.1.0 / 2026-09-17, nine channels, RR-B-36 status vocabulary only, every non-submitted row has decision + date.

## Platform steps after merge (fixed order)

Merge, Pages enable from /docs, About + topics + homepage, tag v0.1.0 on main HEAD, branch protection. RR-B-18 stays FAIL until the tag exists (expected for this snapshot).
EOF
```

- [ ] **Step 4: Watch the PR checks**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
gh pr checks --watch
```

Expected: `validate` (release gate) green, the `lint` jobs (`awesome-lint` on README.md, `markdownlint` on README.md and CONTRIBUTING.md) green, and the `Links` PR run green (advisory by design). If `awesome-lint` or `markdownlint` fails on the new README sections, fix the section prose (entries stay untouched), push, and re-watch.

- [ ] **Step 5: Merge and record the release SHA**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
gh pr merge --squash --delete-branch
git checkout main && git pull origin main
git rev-parse HEAD
```

Record the printed SHA: it is the release commit. Task 6 tags exactly this SHA. Also re-check `gh api repos/jgsystemsconsulting/awesome-archimate/license --jq .license.spdx_id` now that LICENSE changed on origin; it must still be `CC0-1.0` (AC9; if `NOASSERTION`, follow the Task 1 Step 7 fallback).

Done when: PR checks green (validate plus triad), PR merged with squash, main HEAD SHA recorded, PR body contains the MANUAL closures, the baseline-to-final audit diff, and the keep/drop phrase.

### Task 6: Platform state in the fixed order (D10)

**Files:**
- Modify: none in the tree (GitHub platform state only; the temporary release-notes file and any ledger amendment commit excepted)

**Interfaces:**
- Consumes: merge SHA from Task 5; CHANGELOG notes (Task 2); Pages URL and exact About string (Global Constraints).
- Produces: live Pages site; homepageUrl; local plus pushed tag `v0.1.0` on the merge SHA; published Release v0.1.0 with the exact footer line; branch protection whose required check matches the reported context name. These make RR-B-18/20/21/22/23 PASS in Task 7's `--gh` audit.

**Model:** deep

- [ ] **Step 1: Enable Pages from /docs and verify it serves**

```bash
gh api -X POST repos/jgsystemsconsulting/awesome-archimate/pages \
  -f "source[branch]=main" -f "source[path]=/docs"
gh api repos/jgsystemsconsulting/awesome-archimate/pages --jq .html_url
gh api repos/jgsystemsconsulting/awesome-archimate/pages/builds/latest --jq .status
curl -fsSL -o /dev/null -w '%{http_code}\n' https://jgsystemsconsulting.github.io/awesome-archimate/
```

Expected: `https://jgsystemsconsulting.github.io/awesome-archimate/`, build status `built` (re-run the builds call until it flips from `building`; the first build can take a minute or two), then HTTP `200`. If the POST returns "already exists", confirm the existing source is `main` `/docs` via the GET call. If curl returns 404 after the build is `built`, re-run the curl once after 30 seconds before investigating. Pages enablement needs admin on the repo (spec risk note).

- [ ] **Step 2: Set About description, the one missing topic, and homepage (homepage only now that Pages serves)**

```bash
gh repo edit jgsystemsconsulting/awesome-archimate \
  --description "Curated ArchiMate resources for enterprise architecture and MBSE practitioners" \
  --homepage "https://jgsystemsconsulting.github.io/awesome-archimate/"
gh repo edit jgsystemsconsulting/awesome-archimate --add-topic togaf
gh repo view jgsystemsconsulting/awesome-archimate --json description,homepageUrl,repositoryTopics
```

Expected JSON: description is the exact string; homepageUrl is the Pages URL; six topics (`archimate`, `awesome`, `awesome-list`, `enterprise-architecture`, `mbse`, `togaf`). Six is required: the auditor's RR-B-21 row demands at least 6 (the other five already exist; `togaf` is the only add).

- [ ] **Step 3: Tag v0.1.0 on the main HEAD SHA and push it**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
SHA=$(git rev-parse origin/main)
git tag -a v0.1.0 "$SHA" -m "Awesome ArchiMate 0.1.0"
git push origin v0.1.0
git tag -l v0.1.0
```

Expected: the tag lists locally after push. The tagged SHA must equal the SHA recorded at the end of Task 5.

- [ ] **Step 4: Publish the GitHub Release with the exact footer line**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
cat > release-notes-v0.1.0.md <<'EOF'
# Awesome ArchiMate 0.1.0

First tagged release of the curated ArchiMate resource list.

## Added

- 17 verified entries across eight sections: specifications and standards,
  certification, the Archi tool, plugins and collaboration, books, example
  models, TOGAF alignment, and communities.
- Release-standard packaging: CITATION.cff, RELEASE-INFO.txt, COPYRIGHT and
  NOTICE, private security advisory route, bug report and suggestion forms,
  release gate CI, and a Pages landing page.

## Licence

See LICENSE in the repository (CC0-1.0).

Licence enquiries: https://labs.jgsystemsconsulting.com/licensing.html
EOF
gh release create v0.1.0 -R jgsystemsconsulting/awesome-archimate \
  --title "v0.1.0" --notes-file release-notes-v0.1.0.md
rm release-notes-v0.1.0.md
gh release view v0.1.0 -R jgsystemsconsulting/awesome-archimate --json body --jq .body | grep -c "https://labs.jgsystemsconsulting.com/licensing.html"
```

Expected: the release is published and the grep count is at least 1 (the exact footer line `Licence enquiries: https://labs.jgsystemsconsulting.com/licensing.html` is present verbatim).

- [ ] **Step 5: Apply branch protection (first-time PUT, solo-maintainer shape)**

First probe the exact check context GitHub reports for the release commit:

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
SHA=$(git rev-parse origin/main)
gh api "repos/jgsystemsconsulting/awesome-archimate/commits/$SHA/check-runs" --jq '.check_runs[].name'
gh api "repos/jgsystemsconsulting/awesome-archimate/commits/$SHA/status" --jq '[.statuses[].context]'
```

Expected: the check run name is `validate` (workflow `validate`, job id `validate`). If the probe instead reports `validate / validate`, use that string in the PUT below.

```bash
gh api -X PUT repos/jgsystemsconsulting/awesome-archimate/branches/main/protection \
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
gh api repos/jgsystemsconsulting/awesome-archimate/branches/main/protection \
  --jq '{contexts: .required_status_checks.contexts, force: .allow_force_pushes.enabled, del: .allow_deletions.enabled, admins: .enforce_admins.enabled, reviews: .required_pull_request_reviews.required_approving_review_count}'
```

Expected GET: `contexts` contains the probed check name, `force` false, `del` false, `admins` false, `reviews` 0. If the PUT fails on permissions (403/404), do not retry blindly and do not mark RR-B-23 done: record it in the PR as the named maintainer action with this exact command, and continue to Task 7 (the `--gh` audit will then show RR-B-23 WARN, which is reported, not hidden). Solo-maintainer residual per spec: `enforce_admins` off means direct pushes can bypass; the residual is named in the PR.

- [ ] **Step 6: Reconcile DISTRIBUTION.md channel statuses after platform success**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
git checkout main && git pull origin main
# Confirm the four platform rows in docs/DISTRIBUTION.md match reality:
# GitHub repo (submitted), Releases v0.1.0 (submitted), Pages landing (submitted),
# About/topics/homepage (submitted). If any channel did not complete (for example
# Pages blocked on admin), set that row to `in progress` with the blocker named.
git add docs/DISTRIBUTION.md
git commit -m "docs: reconcile distribution ledger after 0.1.0 platform steps" --allow-empty
git push origin main
```

Expected: the ledger matches actual platform state; no channel row claims `submitted` for a channel that did not complete.

Done when: Pages returns 200 from the `/docs` source, homepageUrl is the Pages URL with six topics, tag v0.1.0 exists locally and on origin on the merge SHA, Release v0.1.0 is published with the exact footer line, protection GET returns the expected shape (or the failure is recorded as the named maintainer action in the PR), and the ledger rows match reality.

### Task 7: Acceptance verification (AC1-9)

**Files:**
- Modify: none (verification only; any fix loops back to its source task)

**Interfaces:**
- Consumes: the merged main, the tag and Release from Task 6, the gate script, the Task 1 baseline and freeze files in `/tmp`.
- Produces: the recorded evidence block for the PR (final audit outputs, AC1-9 results, triad run ids) that the session notes cite when claiming standard-complete.

**Model:** standard

- [ ] **Step 1: Plain audit exits 0 (AC1)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base; echo "exit=$?"
```

Expected: `exit=0` with zero FAIL rows. The only WARN is the accepted RR-B-32 improvement-form glob row (D8). Any other WARN or any FAIL means a fix loop back to its task, then re-run. Record final counts next to the baseline counts from `/tmp/archimate-audit-baseline.txt`.

- [ ] **Step 2: Platform and link audit (AC3)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base --gh --links; echo "exit=$?"
```

Expected: `exit=0`; rows RR-B-20 PASS (Pages URL shown), RR-B-21 PASS (description true, topics >= 6; the auditor does not fail on unset homepageUrl, so also verify homepage product policy separately with `gh api repos/jgsystemsconsulting/awesome-archimate --jq .homepage`), RR-B-22 PASS (Release published with licence-enquiry URL), RR-B-23 PASS (branch protection configured) or named WARN residual, RR-B-25 PASS (all links resolve). If a README issue-template URL 404s under the link check, replace that markdown link with the plain issues URL `https://github.com/jgsystemsconsulting/awesome-archimate/issues` (Support and Usage sections only), land the fix through a small follow-up PR, and re-run this step. If RR-B-23 shows WARN because Task 6 Step 5 was blocked, report it as the named maintainer residual rather than looping.

- [ ] **Step 3: Gate and seed freeze (AC2, AC4)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
python scripts/check_release.py; echo "exit=$?"
grep '^- \[' README.md | diff - /tmp/archimate-entries-before.txt && echo "25 `- [` lines byte-identical post-merge"
grep -c '^- \[' README.md
SHA=$(git rev-parse origin/main)
gh run list --workflow=lint.yml --branch main --limit 5 --json conclusion,headSha \
  --jq '.[] | select(.headSha=="'"$SHA"'") | .conclusion'
```

Expected: gate prints `release gate: PASS (scanned N files)` with N at least 1, exit 0; freeze diff empty, count `25`; the lint run for the merge SHA prints `success` (selecting by headSha because the Task 6 Step 6 ledger push creates a newer lint run on main). AC4: lint green via the release push, not `workflow_dispatch`, which `lint.yml` does not have.

- [ ] **Step 4: Family triad links run on main (AC5)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
gh workflow run links.yml --ref main
sleep 10
RUN_ID=$(gh run list --workflow=links.yml --limit 1 --json databaseId --jq '.[0].databaseId')
gh run watch "$RUN_ID" --exit-status; echo "links exit=$?"
```

Expected: the lychee link-check job concludes green on the dispatch run. Record the run id. (`stale.yml` is untouched and runs on its own monthly schedule; no action.)

- [ ] **Step 5: Em-dash, email, and licence checks (AC7, AC9)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
grep -n $'\u2014' README.md SECURITY.md CHANGELOG.md docs/DISTRIBUTION.md docs/index.html
echo "em-dash grep exit=$? (1 means clean)"
grep -n "support@jgsystemsconsulting.com" README.md SECURITY.md CHANGELOG.md docs/DISTRIBUTION.md docs/index.html
echo "email grep exit=$? (1 means clean)"
gh api repos/jgsystemsconsulting/awesome-archimate/license --jq .license.spdx_id
```

Expected: both greps find nothing (exit 1) across the five customer-surface files; the licence API returns `CC0-1.0` (not `NOASSERTION`).

- [ ] **Step 6: Confirm the PR carries the MANUAL closures (AC6) and record the evidence**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
gh pr list --state merged --limit 1 --json number,body --jq '.[0].body' | grep -c "MANUAL items closed"
```

Expected: count at least 1. Then post a comment on the merged PR with: the baseline audit counts and final audit counts from Step 1, the `--gh --links` output from Step 2, the triad run ids from Steps 3-4, the entry sha256 pair, and the AC1-9 checklist. AC8 is evidenced by Task 5 Step 1 (workflow scope confirmed or refreshed before the push succeeded). Nothing is committed in this task; the evidence lives in the PR comment and the session notes.

Done when: all nine acceptance criteria have a recorded PASS (or the two named residuals: the accepted RR-B-32 WARN and, only if the PUT was blocked, RR-B-23 as a maintainer action with the exact command), and the evidence comment is on the PR.

## Acceptance criteria coverage

| AC | Where |
|----|-------|
| AC1 plain audit exit 0, baseline recorded | Task 1 Step 1 (baseline), Task 7 Step 1 (final; tag from Task 6 closes RR-B-18) |
| AC2 gate exit 0, scanned >= 1 | Task 3 Step 2 (red), Task 4 Step 3 and Task 7 Step 3 (green) |
| AC3 --gh --links rows PASS | Task 6 Steps 1-2, 4-5; Task 7 Step 2 |
| AC4 25 `- [` lines frozen, lint green on push | Task 1 Step 1 (freeze capture), Task 2 Step 5, Task 7 Step 3 |
| AC5 triad green: links dispatch, lint push | Task 5 Step 4 (PR), Task 7 Steps 3-4 (main) |
| AC6 MANUAL items in PR | Task 5 Step 3, Task 7 Step 6 |
| AC7 no em dash, no email | Task 2 Step 5, Task 4 Step 3, Task 7 Step 5 |
| AC8 workflow scope | Task 5 Step 1 |
| AC9 licence spdx id CC0-1.0 | Task 1 Steps 1 and 7, Task 5 Step 5, Task 7 Step 5 |

Locked decisions D1-D11 map onto: D1/D2/D3 (Global Constraints plus Tasks 1 and 3), D4 (Task 2 plus Task 6 Steps 3-4), D5 (Task 4 plus Task 6 Steps 1-2 plus the Task 5 PR body), D6 (Task 2 README sections plus PR body), D7 and D8 (Task 3 Step 6 plus Task 4 ledger plus PR body), D9 (Task 2 SECURITY.md), D10 (Task 6 fixed order), D11 (no hub edits anywhere; family pointer untouched).
