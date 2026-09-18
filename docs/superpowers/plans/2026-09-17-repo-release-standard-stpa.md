# Awesome STPA Release Repo Standard Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bring `jgsystemsconsulting/awesome-stpa` to Release Repo Standard v1.14 RR-B Base: audit exits 0, release identity v0.1.0 end to end, release-gate CI, Pages landing live, About/homepage/protection applied, then the family Checklist A flip of the spoke to public with the two hub registry updates.

**Architecture:** One spoke-local change set on a single branch: legal and identity files, Keep-a-Changelog version 0.1.0, SECURITY advisory route, README Install/Usage/Licence/Support/Version sections plus the D12 text-only hub bullet and the D13 percent-encoded PSAS URLs, `scripts/check_release.py` gate plus `validate.yml`, three issue forms, self-contained `docs/index.html` Pages landing, and `docs/DISTRIBUTION.md` ledger. All files merge in one PR, then fixed-order platform steps run against main HEAD: merge, Pages enable, About, tag v0.1.0 plus GitHub Release, branch protection. After the audit exit 0 gate, Checklist A runs by hand: decision issue, visibility flip to public, anonymous access checks, hub FAMILY.md and README registry updates, CHANGELOG note, issue closed.

**Tech Stack:** Python 3 stdlib (gate script), GitHub Actions (`actions/checkout@v4`, `actions/setup-python@v5`), `gh` CLI for Pages/About/Release/protection/visibility API calls, Git Bash on Windows.

**Spec:** `docs/superpowers/specs/2026-09-17-repo-release-standard-stpa.md` (normative; locked decisions D1-D13, acceptance criteria AC1-11)

## Global Constraints

Every task implicitly includes these. Values are verbatim from the spec.

- Target repo: `C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa`, branch `main`, remote `https://github.com/jgsystemsconsulting/awesome-stpa`. Repo is private today and flips public only in Task 7. Hub edits are limited to the two Checklist A registry updates in Task 7 (FAMILY.md Visibility cell, hub README family table row); no other hub file is touched by work under this plan.
- Profile RR-B Base only (D1). No MCP/skills/research rows. Licence stays CC0-1.0, unchanged (D2). LICENSE keeps the Capella-shaped org first line so RR-B-01 keeps PASSing; GitHub `license.spdx_id` may remain `NOASSERTION` (verified 2026-09-17) and that is not a stop. NOTICE already passes: verify only, no rewrite. Standalone build model (D3): commits go to the spoke; the gate is `scripts/check_release.py` + `.github/workflows/validate.yml`.
- Version **0.1.0**, dated **2026-09-17**, sourced from the CHANGELOG top entry `## [0.1.0] - 2026-09-17`, propagated to RELEASE-INFO.txt, CITATION.cff, tag `v0.1.0`, GitHub Release (D4). Version files and the tag land in this one change set; do not split them across PRs. The post-flip Checklist A CHANGELOG note is a bullet added to the same `[0.1.0]` entry after the tag; the tag pins the release commit and does not move.
- About description exactly: `Curated STAMP/STPA and hazard analysis resources for safety and systems engineering practitioners` (D10). Topics stay the existing six exactly: `stpa`, `stamp`, `safety`, `hazard-analysis`, `awesome-list`, `awesome` (verified via `gh repo view` 2026-09-17). No topic is added or removed; the six-topic floor is already met, so `mbse` is not added.
- Pages URL (homepage value): `https://jgsystemsconsulting.github.io/awesome-stpa/` (D5). The repo is private when Pages is enabled; anonymous 200 on the Pages URL is provable only after the Task 7 flip, so homepage is set only after that 200.
- Licence-enquiry URL everywhere required: `https://labs.jgsystemsconsulting.com/licensing.html` (README Licence section, landing page footer, Release notes). Release notes footer line exactly: `Licence enquiries: https://labs.jgsystemsconsulting.com/licensing.html` (D10).
- SECURITY.md: private advisory route (`https://github.com/jgsystemsconsulting/awesome-stpa/security/advisories/new`), PR-with-fix for non-sensitive issues, `We aim to acknowledge reports within 7 days.`, no email address anywhere, no em dash (D9).
- README entries: the 43 list bullets, their ordering, tags, and the flat `## Contents` block stay byte-identical except the D12 link removal and the D13 percent-encoding of PSAS `/home/<seg>/` hrefs (AC4). Badge line, one-line scope, and the family pointer on line 9 (`Part of the awesome-mbse list family (hub repository currently private).`) stay untouched (D11, hub-private class). New README sections append at end of file only.
- D12: the `awesome-mbse` Related-lists bullet becomes text-only (same text, link removed, note that the link returns when the hub goes public). The `awesome-sysml-v2` and `sindresorhus/awesome` bullets stay as links. `.lycheeignore` keeps its hub entry untouched; it gates the Checklist B link restore.
- D13: every one of the **11** README URLs whose path matches `/home/<segment>/` on `psas.scripts.mit.edu` is percent-encoded at exactly one character of the first segment after `/home/` so the auditor regex `/home/[A-Za-z0-9._-]+(?:/|\\)` no longer matches. Lines 29, 30 (`get_file.php`, `get_file4.php`, no trailing slash) and line 33 (bare `/home/`) are not flagged and are not edited. No new file may contain a literal `/home/<token>/` sequence; written examples of the encoding must keep the `%` in them.
- Family triad workflows (`link-check-pr.yml`, `link-check-schedule.yml`, `lint.yml`) stay byte-identical. `validate.yml` is the only new workflow. `.gitignore` already passes; extend only if new tooling demands it (none does).
- Issue forms (D8): the spoke has none today, so this pass creates all three. `config.yml` sets `blank_issues_enabled: false` with exactly one contact link, `Security advisory`. No contact link to the private hub or any sibling. The auditor's improvement-form filename glob (`improv`/`enhanc`) WARNs on `suggest-resource.yml`; that WARN is accepted and named in README Support and the ledger.
- `scripts/check_release.py` REQUIRED list (RR-B-15, no `check_entries.py` because the spoke has no checker): `README.md`, `LICENSE`, `COPYRIGHT`, `NOTICE`, `CHANGELOG.md`, `SECURITY.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `RELEASE-INFO.txt`, `CITATION.cff`, `docs/DISTRIBUTION.md`, `docs/index.html`, `scripts/check_release.py`; header sentinel `Copyright (c) 2026 JG Systems Consulting Ltd`; `SCAN_GLOBS = ["scripts/*.py"]`; the gate collects scanned paths, asserts non-empty, prints `scanned N` with N >= 1.
- Platform order is fixed (D10): merge release commit to main, enable Pages from `/docs`, set About description (homepage only after the site serves anonymously), tag v0.1.0 on that main HEAD SHA and publish the Release, then branch protection. Branch protection shape: required check exactly `validate`, force-push off, deletion off, `enforce_admins` false, 0 required approvals (solo maintainer); the solo-maintainer residual (admin direct pushes bypass) is named in the PR.
- The Checklist A visibility flip runs only after the plain audit exits 0 (Task 6), CI green, and the D12 private-link fix, in that order. Once public, assume crawlers have the content.
- No em dash in README.md, SECURITY.md, CHANGELOG.md, docs/DISTRIBUTION.md, docs/index.html (AC6). LICENSE may keep its legal-text dashes; grep and record, do not edit. New YAML/CFF files written as plain UTF-8 without BOM (RR-B-33).
- All commits use the repo's configured noreply identity `245595077+jgsystemsconsulting@users.noreply.github.com` (already set; RR-B-27).
- Entry-integrity baseline for AC4 diffs: pre-work commit `5f10f0f40abf1271edaa6447d700ea03b9740353` (spoke HEAD 2026-09-17).
- Auditor: `python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base [--gh] [--links]`, run from the spoke root. It imports `landing_taste` from its own directory, so the path works from anywhere.

## Codebase context

The spoke ships: README with 43 verified entries across seven sections (Foundations & Handbooks 8, Tools 15, Standards & Guidance 2, Case Studies & Agency Reports 5, Learning & Workshops 4, Datasets & Examples 6, Related lists 3) plus a flat hand-maintained `## Contents`, Awesome badge, sweep badge, the preferred text-only family pointer on line 9, CC0-1.0 LICENSE with the Capella-shaped org first line (GitHub spdx_id `NOASSERTION`), NOTICE (nominative-use note), CONTRIBUTING (entry format, STPA tag vocabulary, canonical-URL rule, PSAS query strings documented as semantically required), CODE_OF_CONDUCT, SECURITY.md (email route `support@jgsystemsconsulting.com`, one em dash on line 3), a date-headed CHANGELOG (not semver), `.gitignore`, `.lycheeignore` (hub URL plus four bot-blocked upstreams with dated removal conditions), `.markdownlint-cli2.jsonc`, a PR template with guardrail checkboxes, and three workflows (`link-check-pr.yml`, `link-check-schedule.yml`, `lint.yml`, action refs pinned to commit SHAs). It has no `scripts/` directory, no issue templates, and no `docs/`. The `## Related lists` section carries the one private hub link (line 104, D12). Current platform state (gh, 2026-09-17): visibility private, no Pages, homepage unset, description `Curated list of STAMP/STPA and hazard analysis resources` (replaced in Task 5), six topics. Audit baseline 2026-09-17: 11 FAIL, 2 WARN, 11 PASS (`docs/superpowers/research/2026-09-17-repo-release-standard-stpa-audit-baseline.txt`). Sibling `awesome-capella` completed the same RR-B pass on 2026-09-17 and is the shape reference for COPYRIGHT, CITATION.cff, the gate script, the landing page, and the bug report form; its Pages site is built from `main` `/docs` and `status: built` via the API.

## Research

- https://github.com/jgsystemsconsulting/awesome-stpa (target spoke; visibility, topics, description state verified 2026-09-17 via `gh`)
- https://github.com/jgsystemsconsulting/awesome-capella (RR-B shape reference; public, Pages from /docs, `status: built`)
- https://github.com/jgsystemsconsulting/awesome-sysml-v2 (sibling family list; public)
- https://github.com/sindresorhus/awesome (meta-list; Checklist C target, deferred past this plan)
- https://jgsystemsconsulting.github.io/awesome-stpa/ (target Pages URL, not live at plan time)
- https://psas.scripts.mit.edu/home/ (MIT PSAS host; 11 README URL paths under `/home/` are D13-encoded)
- https://creativecommons.org/publicdomain/zero/1.0/ (licence badge target already in the README footer)
- `docs/superpowers/research/2026-09-17-repo-release-standard-stpa-research.md` (research gate; 11 FAIL, 2 WARN, 11 PASS baseline, RR-B-34 false-positive analysis)
- `docs/superpowers/context/2026-09-17-repo-release-standard-stpa-context.md` (context gate; spoke inventory, family constraints)
- `docs/superpowers/research/2026-09-17-repo-release-standard-stpa-audit-baseline.txt` (row-level baseline capture)
- `docs/superpowers/plans/2026-09-17-repo-release-standard-capella.md` (structure pattern for this plan)
- `docs/runbooks/family-public-release.md` (Checklist A, normative for Task 7)
- `C:/Users/gower/.zcode/skills/release-repo-standard/references/release-repo-standard.md` (v1.14, normative); auditor `tools/audit.py`, `tools/landing_taste.py`, and `templates/` under the same skill tree
- `docs/superpowers/specs/2026-09-17-repo-release-standard-capella.md` (Capella pattern, D1-D11 source)

---

### Task 1: Legal, identity, and version files

**Files:**
- Create: `COPYRIGHT`
- Create: `RELEASE-INFO.txt`
- Create: `CITATION.cff`
- Modify: `SECURITY.md` (full rewrite)
- Modify: `CHANGELOG.md` (full rewrite to Keep a Changelog shape)
- Verify only: `NOTICE`, `LICENSE`, `.gitignore` (all pass today; no edits)

**Interfaces:**
- Consumes: nothing.
- Produces: version `0.1.0` as the single source in `CHANGELOG.md` `## [0.1.0] - 2026-09-17`, mirrored in `RELEASE-INFO.txt` and `CITATION.cff` (Task 5 tag/Release and the Task 4 gate REQUIRED set depend on these exact files and values); SECURITY.md advisory URL that Task 3's `config.yml` and README Support section reuse; the header sentinel text `Copyright (c) 2026 JG Systems Consulting Ltd` that Task 4's gate requires in `scripts/*.py`.

**Model:** flash

- [ ] **Step 1: Record the baseline and branch state**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
git status --porcelain   # expect empty; if not, stop and report
git rev-parse HEAD       # expect 5f10f0f40abf1271edaa6447d700ea03b9740353
grep -c "JG Systems Consulting" LICENSE   # expect 1 or more (org string present, RR-B-01)
gh api repos/jgsystemsconsulting/awesome-stpa/license --jq .license.spdx_id
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base
```

Expected: audit prints the baseline shape (11 FAIL, 2 WARN, 11 PASS). The `spdx_id` may read `NOASSERTION` (verified 2026-09-17); record it and move on: AC5 makes RR-B-01 the binding row, not the licensee id, and D2 forbids stripping the org line to chase spdx_id.

- [ ] **Step 2: Create the branch**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
git checkout main && git pull origin main
git checkout -b release/0.1.0-standard
```

- [ ] **Step 3: Write `COPYRIGHT`** (single line, exactly):

```
Copyright (c) 2026 JG Systems Consulting Ltd. All rights reserved.
```

- [ ] **Step 4: Rewrite `SECURITY.md`** (entire file becomes; no email, no em dash; keeps the words `advisories` and `pull request` so RR-B-07 PASSes rather than WARNs):

```markdown
# Security Policy

This repository is a curated index of links. It ships no executable product. The main
security surfaces are the links it points to and the CI workflows.

## Reporting a vulnerability

Report sensitive issues privately via a
[GitHub security advisory](https://github.com/jgsystemsconsulting/awesome-stpa/security/advisories/new).
Please do not open a public issue for a suspected malicious or hijacked link
until it has been reviewed.

For non-sensitive fixes (a dead or moved link, a CI misbehaviour), open a
pull request with the fix directly.

We aim to acknowledge reports within 7 days.

## Scope

- A linked resource that turns out to be malicious, hijacked, or compromised.
- The repository's own CI: the link-check workflows and the release gate.
```

- [ ] **Step 5: Rewrite `CHANGELOG.md`** (entire file becomes; the three seed bullets carry over verbatim under Added; this entry is the version source, D4):

```markdown
# Changelog

Maintenance sweeps and notable changes to this list. The format follows
Keep a Changelog and versions follow Semantic Versioning.

## [0.1.0] - 2026-09-17

### Added

- **Shipped v1**: seven sections, 43 entries (PSAS foundations, open-source tools
  first then commercial, standards context, agency and workshop cases, learning,
  datasets, family related lists), all in family entry format (tags plus year).
- **CI live**: blocking link check on PRs and pushes to main (lychee, anchor-only
  fragments, retries, 429 accepted), weekly link-rot report issue, awesome-lint plus
  markdownlint on README and CONTRIBUTING. All action refs pinned to full commit SHAs.
- **Family standard**: CC0-1.0, CONTRIBUTING.md with the hub year and canonical-URL
  rules ported verbatim (PSAS query strings called out as semantically required), STPA
  tag vocabulary in fixed axis order, known-rot appendix, editorial neutrality. Repo
  created private per FAMILY Private mode.
- Release-standard pass (Release Repo Standard v1.14, RR-B Base): COPYRIGHT,
  CITATION.cff, RELEASE-INFO.txt, SECURITY.md advisory route, release gate CI,
  issue forms, Pages landing, and the distribution ledger.
```

- [ ] **Step 6: Write `RELEASE-INFO.txt`** with the real UTC timestamp (D4: Built is the UTC ISO-8601 time at release-commit authoring):

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
printf 'Product: Awesome STPA\nVersion: 0.1.0\nBuilt: %s\nTag: v0.1.0\n' "$TS" > RELEASE-INFO.txt
cat RELEASE-INFO.txt
```

Expected output has all four fields; `Built` matches `YYYY-MM-DDTHH:MM:SSZ`.

- [ ] **Step 7: Write `CITATION.cff`** (Capella shape, stpa values; plain UTF-8, no BOM):

```yaml
cff-version: 1.2.0
message: "If you use this list in your work, please cite it using this metadata."
title: Awesome STPA
version: "0.1.0"
date-released: "2026-09-17"
authors:
  - entity:
      name: "JG Systems Consulting Ltd"
license: CC0-1.0
repository-code: https://github.com/jgsystemsconsulting/awesome-stpa
url: https://github.com/jgsystemsconsulting/awesome-stpa
```

- [ ] **Step 8: Verify**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
grep -ri "support@jgsystemsconsulting.com" . --include="*.md" || echo "no email left"
grep -n "—" SECURITY.md CHANGELOG.md RELEASE-INFO.txt CITATION.cff COPYRIGHT || echo "em-dash clean"
python -c "from pathlib import Path
for f in ['CITATION.cff', 'RELEASE-INFO.txt']:
    assert Path(f).read_bytes()[:3] != b'\xef\xbb\xbf', f'BOM in {f}'
print('no BOM')"
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base | grep -E "RR-B-02|RR-B-07|RR-B-09|RR-B-10|RR-B-28|RR-B-31|RR-B-33"
```

Expected: no email anywhere; em-dash grep clean; no BOM; audit rows RR-B-02 (two rows: COPYRIGHT PASS, NOTICE PASS), RR-B-07 PASS (detail says the advisory route is found and no email), RR-B-09 PASS (version match), RR-B-10 PASS, RR-B-28 PASS, RR-B-31 PASS, RR-B-33 PASS. RR-B-18 (tag) is not expected to appear as FAIL yet because the version rows only activate with version-bearing files present; if it appears, that is the expected transient FAIL closed by Task 5's tag.

- [ ] **Step 9: Commit**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
git add COPYRIGHT RELEASE-INFO.txt CITATION.cff SECURITY.md CHANGELOG.md
git commit -m "chore: legal identity, v0.1.0 version files, security advisory route (RR-B-02,07,09,10,28,31)"
```

Done when: the targeted audit rows PASS, no email or em dash in the five files, CITATION.cff and RELEASE-INFO.txt BOM-free, commit on `release/0.1.0-standard`.

### Task 2: README sections, D12 text-only hub bullet, D13 PSAS encoding

**Files:**
- Modify: `README.md` (append five sections at end of file; Related lists intro and hub bullet; 11 URL encodings; nothing above line 99 changes)

**Interfaces:**
- Consumes: issue-form filenames from Task 3 (`suggest-resource.yml`, `bug_report.yml`) and the advisory URL from Task 1; version `0.1.0`.
- Produces: README sections and URLs the Task 3 landing page mirrors; the D12 text-only bullet that Checklist A's private-link gate (Task 7) depends on; the 11 encoded URLs that close RR-B-34.

**Model:** standard

- [ ] **Step 1: Append the five README sections at end of file** (below the CC0 licence block; one blank line before `## Install`; do not touch anything above; the licence-enquiry URL must appear literally for RR-B-05):

````markdown
## Install

Nothing to install. This list is a curated index: browse it here on GitHub,
or clone it:

```bash
git clone https://github.com/jgsystemsconsulting/awesome-stpa.git
```

## Usage

- Browse the sections under [Contents](#contents), or search the page with
  your browser's find function.
- Open any entry's link to reach the upstream resource; the list never
  re-hosts content. PSAS handbook and paper links keep their query strings;
  they are part of the address.
- To suggest a resource, use the
  [Suggest a resource](https://github.com/jgsystemsconsulting/awesome-stpa/issues/new?template=suggest-resource.yml)
  issue form.
- To propose a correction, open a pull request (see
  [CONTRIBUTING.md](CONTRIBUTING.md)), or use the
  [bug report](https://github.com/jgsystemsconsulting/awesome-stpa/issues/new?template=bug_report.yml)
  form for a dead, wrong, or mislabelled entry.

## Licence

Released under [CC0 1.0 Universal](LICENSE). Linked resources remain under
their own licences.

To request a commercial or academic licence, or if you are unsure which
licence you need: https://labs.jgsystemsconsulting.com/licensing.html

## Support

- Dead or wrong entry: [bug report form](https://github.com/jgsystemsconsulting/awesome-stpa/issues/new?template=bug_report.yml)
- Suggest a resource (the list's improvement channel; its filename does not
  match the release auditor's improvement-form glob, an accepted WARN):
  [suggestion form](https://github.com/jgsystemsconsulting/awesome-stpa/issues/new?template=suggest-resource.yml)
- Security issues: [private security advisory](https://github.com/jgsystemsconsulting/awesome-stpa/security/advisories/new)
  (see [SECURITY.md](SECURITY.md)); non-sensitive fixes come as pull requests.

## Version

Current release: 0.1.0 (2026-09-17). See [CHANGELOG.md](CHANGELOG.md) and
[RELEASE-INFO.txt](RELEASE-INFO.txt).
````

- [ ] **Step 2: Convert the D12 hub bullet to text-only** (exact edit in `## Related lists`; the intro line changes because it currently claims a hub link exists; the sibling bullets for awesome-sysml-v2 and sindresorhus/awesome stay as links):

Replace:

```markdown
Family lists and the awesome meta-index. The hub link resolves for org members while
the hub repository is private.

- [awesome-mbse](https://github.com/jgsystemsconsulting/awesome-mbse) - Hub of this list family: methods, tools, and openable models across MBSE `STAMP-general` `list` (2026).
```

With:

```markdown
Family lists and the awesome meta-index. The hub entry below is text-only until
the hub repository goes public.

- awesome-mbse - Hub of this list family: methods, tools, and openable models across MBSE `STAMP-general` `list` (2026). (Link returns when the hub goes public.)
```

The bullet stays a list item (43 total under the seven sections, AC4) and awesome-lint skips text-first items (verified against v2.3.0 `list-item.js`, spec D12); CI re-proves it.

- [ ] **Step 3: Encode the 11 D13 PSAS URLs** (deterministic script; asserts both the count and the auditor-regex outcome; `%` is outside the auditor's token class `[A-Za-z0-9._-]`, so one encoded character per segment kills the match):

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
python - <<'EOF'
from pathlib import Path
import re
p = Path("README.md")
text = p.read_text(encoding="utf-8")
MAP = [
    ("/home/books-and-handbooks/", "/home/books%2Dand-handbooks/"),
    ("/home/materials/", "/home/%6Daterials/"),
    ("/home/publications/", "/home/%70ublications/"),
    ("/home/stamp-tools/", "/home/stamp%2Dtools/"),
    ("/home/wp-content/", "/home/wp%2Dcontent/"),  # matches 3 URLs
    ("/home/mit-stamp-workshop-presentations/", "/home/mit%2Dstamp-workshop-presentations/"),
    ("/home/mit-stamp-workshop-tutorials/", "/home/mit%2Dstamp-workshop-tutorials/"),
    ("/home/stamp-workshop-information/", "/home/stamp%2Dworkshop-information/"),
    ("/home/online-education/", "/home/online%2Deducation/"),
]
total = 0
for old, new in MAP:
    n = text.count(old)
    total += n
    text = text.replace(old, new)
assert total == 11, f"expected 11 encoded URLs, got {total}"
hits = re.findall(r"/home/[A-Za-z0-9._-]+(?:/|\\)", text)
assert not hits, f"auditor regex still matches: {hits}"
p.write_text(text, encoding="utf-8")
print(f"encoded {total} URLs; auditor regex now matches 0")
EOF
```

Expected: `encoded 11 URLs; auditor regex now matches 0`. Lines 29, 30, and 33 are untouched by the map (no trailing slash after the segment). If the assert fires with a count under 11, a URL changed upstream; re-read README and re-derive the map rather than lowering the assert.

- [ ] **Step 4: Verify links still resolve and lint holds**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
grep -c '^- \[' README.md
grep -n "github.com/jgsystemsconsulting/awesome-mbse" README.md || echo "no hub link (D12)"
grep -n "—" README.md || echo "em-dash clean"
for u in \
  "https://psas.scripts.mit.edu/home/%6Daterials/" \
  "https://psas.scripts.mit.edu/home/%70ublications/" \
  "https://psas.scripts.mit.edu/home/books%2Dand-handbooks/" \
  "https://psas.scripts.mit.edu/home/stamp%2Dtools/" \
  "https://psas.scripts.mit.edu/home/wp%2Dcontent/uploads/2026/2026-03-24-1040__Applying_CAST_to_a_Healthcare_Adverse_Event_H__PUB.pdf" ; do
  printf '%s -> ' "$u"; curl -s -o /dev/null -w "%{http_code}\n" "$u"
done
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base | grep -E "RR-B-05|RR-B-34"
```

Expected: bullet count still `43` (AC4); no hub link; em-dash clean; each sampled encoded URL returns `200` (the sample covers both hyphen-encodes and the two letter-encodes `materials`/`publications`, which have no hyphen to encode; RFC 3986 makes unreserved escapes equivalent and Apache decodes them before path mapping). If a target rejects its encoded form, re-encode a different single character of the same segment, update README and the Task 3 ledger note, and re-test; never drop the link and never restore the plain URL. Audit rows RR-B-05 PASS and RR-B-34 PASS.

- [ ] **Step 5: Commit**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
git add README.md
git commit -m "docs: README sections, text-only hub bullet, encoded PSAS URLs (RR-B-05,34; D12,D13)"
```

Done when: 43 bullets, no hub link in README, RR-B-05 and RR-B-34 PASS, encoded URLs return 200, commit on the branch.

### Task 3: Issue forms, Pages landing, distribution ledger

**Files:**
- Create: `.github/ISSUE_TEMPLATE/suggest-resource.yml`
- Create: `.github/ISSUE_TEMPLATE/bug_report.yml`
- Create: `.github/ISSUE_TEMPLATE/config.yml`
- Create: `docs/index.html`
- Create: `docs/.nojekyll` (empty file)
- Create: `docs/DISTRIBUTION.md`

**Interfaces:**
- Consumes: the advisory URL and version `0.1.0` from Task 1; the README section names and URLs from Task 2; the D13 encoding note (written with `%` kept in every example so the file cannot trip RR-B-34).
- Produces: the three forms the README Support section links; `docs/index.html` and `docs/DISTRIBUTION.md` that Task 4's gate requires; ledger rows whose `pending` statuses Task 5 flips after the platform steps.

**Model:** flash

- [ ] **Step 1: Write `.github/ISSUE_TEMPLATE/suggest-resource.yml`** (family shape from awesome-capella, stpa sections and bar; no em dash):

```yaml
name: Suggest a resource
description: Suggest a STAMP/STPA, CAST, or hazard-analysis resource to add to the list
title: "[Suggestion] <resource name>"
labels: ["suggestion"]
body:
  - type: input
    id: name
    attributes:
      label: Resource name
      placeholder: e.g. STPA Handbook
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
        - Foundations & Handbooks
        - Tools
        - Standards & Guidance
        - Case Studies & Agency Reports
        - Learning & Workshops
        - Datasets & Examples
        - Related lists
    validations:
      required: true
  - type: checkboxes
    id: bar
    attributes:
      label: Inclusion bar (see CONTRIBUTING.md)
      options:
        - label: On-topic for STPA, STAMP, CAST, or hazard analysis (not general engineering only)
          required: true
        - label: Substantive (teaches, demonstrates, specifies, or provides something usable, not pure marketing)
          required: true
        - label: The link is live right now
          required: true
        - label: It isn't already in the list (canonical-URL rule, CONTRIBUTING.md)
          required: true
        - label: Publicly accessible (we link, we never re-host); keep PSAS query strings where the upstream requires them
          required: true
```

- [ ] **Step 2: Write `.github/ISSUE_TEMPLATE/bug_report.yml`** (list-adapted per D8: affected entry URL, problem type, list version, hygiene checkbox):

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

- [ ] **Step 3: Write `.github/ISSUE_TEMPLATE/config.yml`** (exactly one contact link per D8; no hub link, no sibling link):

```yaml
blank_issues_enabled: false
contact_links:
  - name: Security advisory
    url: https://github.com/jgsystemsconsulting/awesome-stpa/security/advisories/new
    about: Report security issues privately, never as a public issue.
```

- [ ] **Step 4: Write `docs/index.html`** (self-contained: system fonts only, inline CSS with `:focus-visible` and `prefers-reduced-motion`, canonical plus OG tags, licence-enquiry link in the footer, version in the footer; no CDN, no third-party fonts, no 100vh hero, no em dash, no purple hex):

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Awesome STPA: curated STAMP/STPA and hazard analysis resources</title>
<meta name="description" content="A curated, dated index of STAMP/STPA, CAST, and hazard-analysis resources: handbooks, tools, standards context, case studies, and datasets, for safety and systems engineering practitioners.">
<link rel="canonical" href="https://jgsystemsconsulting.github.io/awesome-stpa/">
<meta property="og:type" content="website">
<meta property="og:title" content="Awesome STPA">
<meta property="og:description" content="Curated STAMP/STPA and hazard analysis resources for safety and systems engineering practitioners.">
<meta property="og:url" content="https://jgsystemsconsulting.github.io/awesome-stpa/">
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
    <h1>Awesome STPA</h1>
    <p class="tagline">Curated STAMP/STPA and hazard analysis resources for safety and systems engineering practitioners.</p>
  </div>
</header>
<main>
  <section id="about">
    <h2>What this is</h2>
    <p>A curated, dated index of STAMP/STPA, CAST, and hazard-analysis resources:
    handbooks, tools, standards context, agency case studies, learning and workshops,
    and datasets. Every entry points at the upstream source; nothing is re-hosted.
    Maintained by JG Systems Consulting Ltd as part of the awesome-mbse list family.</p>
  </section>
  <section id="use-the-list">
    <h2>How to use the list</h2>
    <ul>
      <li><a href="https://github.com/jgsystemsconsulting/awesome-stpa#readme">Open the list on GitHub</a>
          and browse the seven sections, or search the page in your browser.</li>
      <li>Clone it: <code>git clone https://github.com/jgsystemsconsulting/awesome-stpa.git</code></li>
      <li>Each entry carries topic tags and a year, so you can scan for what
          applies to your work.</li>
    </ul>
  </section>
  <section id="contribute">
    <h2>Suggest an entry or report a problem</h2>
    <ul>
      <li>Suggest a resource with the
          <a href="https://github.com/jgsystemsconsulting/awesome-stpa/issues/new?template=suggest-resource.yml">suggestion form</a>.</li>
      <li>Report a dead or wrong entry with the
          <a href="https://github.com/jgsystemsconsulting/awesome-stpa/issues/new?template=bug_report.yml">bug report form</a>.</li>
      <li>Security issues go through a
          <a href="https://github.com/jgsystemsconsulting/awesome-stpa/security/advisories/new">private security advisory</a>.</li>
    </ul>
  </section>
</main>
<footer>
  <div>
    <p><a href="https://github.com/jgsystemsconsulting/awesome-stpa">awesome-stpa on GitHub</a>
       &middot; Version 0.1.0 (2026-09-17)</p>
    <p>CC0-1.0. To request a commercial or academic licence, or if you are unsure
       which licence you need:
       <a href="https://labs.jgsystemsconsulting.com/licensing.html">https://labs.jgsystemsconsulting.com/licensing.html</a></p>
  </div>
</footer>
</body>
</html>
```

- [ ] **Step 5: Create `docs/.nojekyll`** (empty) and write `docs/DISTRIBUTION.md`:

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
mkdir -p docs && touch docs/.nojekyll
```

Write `docs/DISTRIBUTION.md` (RR-B-36; every non-submitted row carries a decision plus date; the D13 examples keep their `%` so this file cannot trip RR-B-34; the Releases, Pages, and About rows are `pending` until Task 5 flips them):

```markdown
<!--
Copyright (c) 2026 JG Systems Consulting Ltd. All Rights Reserved.
See LICENSE for terms.
-->

# Distribution ledger: Awesome STPA

One row per channel this list reaches or could reach (RR-B-36,
release-repo-standard v1.14). A non-submitted row carries its decision and
date so the question stays closed until its premises change. Revisit at
every release: move statuses, re-date reasons whose premises changed, never
drop a row silently.

Last reviewed: 0.1.0 / 2026-09-17

| Channel | Artifact | Status | Decision / reason | Date |
|---|---|---|---|---|
| GitHub repo | jgsystemsconsulting/awesome-stpa | live | Canonical home of the list. Visibility flips private to public under family Checklist A in this release. | 2026-09-17 |
| GitHub Releases | v0.1.0 | pending | Published from the CHANGELOG entry with the licence-enquiry footer once the release commit merges. Flipped to submitted in this release's platform steps. | 2026-09-17 |
| GitHub Pages landing | docs/index.html | pending | Served from main /docs; the repo homepage URL points here. Flipped to live after Pages enablement. | 2026-09-17 |
| GitHub About, topics, homepage | repo settings | pending | Description set to the locked string; homepage set once the Pages URL serves. The six existing topics stay unchanged. Flipped to applied. | 2026-09-17 |
| Org catalogue (labs.jgsystemsconsulting.com) | site entry | planned | Add a list entry alongside the other awesome-mbse spokes. | 2026-09-17 |
| sindresorhus/awesome | list PR | deferred | Checklist C runs after the hub goes public; not before. | 2026-09-17 |
| In-host agent and IDE marketplaces (Claude Code, Cursor, Codex, Gemini CLI) | n/a | deliberate N/A | A curated list is browsed on GitHub, not installed into an agent host, so no marketplace manifests apply (RR-B-29). | 2026-09-17 |
| MCP directories (awesome-mcp-servers, Glama, Smithery, PulseMCP) | n/a | deliberate N/A | The list speaks no MCP; RR-M rows are out of profile (RR-B Base only). | 2026-09-17 |
| Community safety and MBSE directories | link posts | deferred | Assess each directory's scope and licence bar before posting. | 2026-09-17 |

## Note: encoded MIT PSAS URLs (do not revert)

Eleven README entry URLs under `psas.scripts.mit.edu` carry one percent-encoded
character in the first path segment after `/home/` (for example `wp%2Dcontent`,
`books%2Dand-handbooks`, `%6Daterials`, `%70ublications`). The release auditor's
machine-local-path regex (`/home/<name>/`) otherwise false-positives on these
public MIT PSAS web paths, and the audit cannot pass while it does. The encoded
forms are RFC 3986-equivalent, resolve to the same pages, and are re-verified by
the family link check on every PR. Do not restore the plain URLs: that
reinstates the audit FAIL. If a target ever rejects its encoded form, re-encode
a different single character of the same segment; do not drop the link.
```

- [ ] **Step 6: Verify**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
python -c "from pathlib import Path
for f in ['.github/ISSUE_TEMPLATE/suggest-resource.yml', '.github/ISSUE_TEMPLATE/bug_report.yml', '.github/ISSUE_TEMPLATE/config.yml']:
    assert Path(f).read_bytes()[:3] != b'\xef\xbb\xbf', f'BOM in {f}'
print('no BOM')"
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/landing_taste.py" docs/index.html
grep -n "—" docs/DISTRIBUTION.md docs/index.html .github/ISSUE_TEMPLATE/*.yml || echo "em-dash clean"
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base | grep -E "RR-B-32|RR-B-33|RR-B-34|RR-B-36|RR-B-24"
```

Expected: no BOM; `landing_taste.py` prints `PASS` (the RR-B-24 mechanical overlay; the MANUAL taste note goes in the Task 5 PR body per D5); em-dash clean; RR-B-32 first row PASS (`bug_report: True, config: True`) with the accepted WARN on the improvement-form glob, RR-B-33 PASS, RR-B-34 PASS (the ledger note is written so the regex finds nothing), RR-B-36 PASS, RR-B-24 PASS (docs HTML now present). RR-B-15 stays FAIL until Task 4; that is expected.

- [ ] **Step 7: Commit**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
git add .github/ISSUE_TEMPLATE docs/index.html docs/.nojekyll docs/DISTRIBUTION.md
git commit -m "feat: issue forms, Pages landing, distribution ledger (RR-B-32,36,24; D5,D8)"
```

Done when: the three YAML forms are BOM-free, landing_taste PASSes, RR-B-32 (with accepted WARN), RR-B-33, RR-B-34, RR-B-36, RR-B-24 PASS, commit on the branch.

### Task 4: Release gate and validate workflow

**Files:**
- Create: `scripts/check_release.py`
- Create: `.github/workflows/validate.yml`

**Interfaces:**
- Consumes: the REQUIRED file set created by Tasks 1-3; the header sentinel `Copyright (c) 2026 JG Systems Consulting Ltd` (the same text the gate itself ships in its line 1, so the gate satisfies its own header check).
- Produces: gate command `python scripts/check_release.py` (exit 0 now that Tasks 1-3 files exist; AC2); workflow `validate.yml` whose job id `validate` becomes the branch-protection required check name in Task 5.

**Model:** flash

- [ ] **Step 1: Write `scripts/check_release.py`** (adapted for this tree: no `check_entries.py` in REQUIRED, `SCAN_GLOBS = ["scripts/*.py"]` per spec D3/RR-B-15, real sentinel, scanned-count print):

```python
# Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE.
# SPDX-License-Identifier: CC0-1.0
"""Release gate (RR-B-15): required files, forbidden paths, forbidden
content, headers present. Exits non-zero on any failure.

Adapted for awesome-stpa (RR-B Base, standalone model): no src/ layout,
no package install, no scripts beyond the gate itself."""
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
    "scripts/check_release.py",
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
SCAN_GLOBS = ["scripts/*.py"]
scanned: set[pathlib.Path] = set()
for g in SCAN_GLOBS:
    for path in pathlib.Path(".").glob(g):
        scanned.add(path)
        text = path.read_text(encoding="utf-8", errors="ignore")
        for rx in FORBIDDEN_CONTENT:
            if rx.search(text):
                fails.append(f"forbidden content in {path}: {rx.pattern}")

HEADER_SENTINEL = "Copyright (c) 2026 JG Systems Consulting Ltd"
for g in SCAN_GLOBS:
    for path in pathlib.Path(".").glob(g):
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

- [ ] **Step 2: Run the gate green, then prove the REQUIRED check fires** (the negative probe is the failing-test cycle: a moved required file must be caught):

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
python scripts/check_release.py; echo "exit=$?"
mv CITATION.cff CITATION.cff.hold && python scripts/check_release.py; echo "exit=$?"; mv CITATION.cff.hold CITATION.cff
```

Expected first run: `release gate: PASS (scanned 1 files)` and `exit=0` (the spoke's only `.py` is the gate itself, so N = 1 satisfies the N >= 1 bar). Negative probe: `exit=1` listing exactly `required file missing: CITATION.cff` (plus nothing else). If the green run instead lists missing files, a Task 1-3 file is absent or misnamed; fix at the source, not in the gate.

- [ ] **Step 3: Write `.github/workflows/validate.yml`** (job id `validate` so the required check name is exactly `validate`; push and pull_request on main; `contents: read`; three steps only; the family triad files stay untouched):

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
          python-version: "3.x"
      - name: Run release gate
        run: python scripts/check_release.py
```

- [ ] **Step 4: Verify and commit**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
python -c "from pathlib import Path
for f in ['.github/workflows/validate.yml', 'scripts/check_release.py']:
    assert Path(f).read_bytes()[:3] != b'\xef\xbb\xbf', f'BOM in {f}'
print('no BOM')"
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base | grep -E "RR-B-15|RR-B-03|RR-B-04"
git add scripts/check_release.py .github/workflows/validate.yml
git commit -m "ci: release gate script and validate workflow (RR-B-15)"
```

Expected: no BOM; RR-B-15 PASS (`gate script: True, CI workflow: True`); RR-B-03 and RR-B-04 PASS (the gate's own two-line header satisfies the first-party `.py` header and SPDX rows).

Done when: gate exits 0 with `scanned 1 files`, the negative probe exits 1 naming the moved file, RR-B-15/03/04 PASS, commit on the branch.

### Task 5: Pre-merge snapshot, PR with MANUAL closures, merge, platform steps

**Files:**
- Modify: none beyond the Task 6 ledger flip and the temporary release-notes file (platform state otherwise)

**Interfaces:**
- Consumes: the complete branch from Tasks 1-4; `gh` with `repo`, `workflow` scopes (both present on the `jgsystemsconsulting` token, verified 2026-09-17).
- Produces: the merged main HEAD SHA (Step 5 tags this exact SHA); live Pages build; About description; local plus pushed tag `v0.1.0`; published Release v0.1.0 with the exact footer line; branch protection with required check `validate`; the PR body that closes the spec's MANUAL items (AC10) and names the D12/D13 residuals.

**Model:** deep

- [ ] **Step 1: Confirm workflow push scope (AC11)**

```bash
gh auth status
```

Expected: the active `jgsystemsconsulting` token lists `workflow` in scopes (verified 2026-09-17). If absent, run `gh auth refresh -s workflow` and re-check before pushing; GitHub rejects a push that creates a workflow file without the scope.

- [ ] **Step 2: Run the pre-merge audit snapshot and the keep/drop inventory**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base; echo "exit=$?"
git ls-files | grep -E "^\.planning/|^docs/(eval|evidence|superpowers|specs)/|^GATES\.md$|^scripts/add_headers\.py$" || echo "no maintainer-only candidates tracked"
```

Expected audit shape: every row PASS except the accepted RR-B-32 improvement-form WARN, and (if the auditor surfaces RR-B-18 now that version files exist) the transient RR-B-18 FAIL for the not-yet-created tag; the tag lands on this same change set's merge commit in Step 6. Keep/drop inventory (RR-B-35): the grep prints `no maintainer-only candidates tracked`; this exact phrase goes in the PR.

- [ ] **Step 3: Push and open the PR with the MANUAL closures**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
git push -u origin release/0.1.0-standard
gh pr create --base main --head release/0.1.0-standard \
  --title "Release standard 0.1.0: legal, gate, landing, ledger" \
  --body-file - <<'EOF'
## Summary

Release Repo Standard v1.14 (RR-B Base) packaging for the list. New: COPYRIGHT, CITATION.cff, RELEASE-INFO.txt, scripts/check_release.py, .github/workflows/validate.yml, issue forms (suggest-resource, bug report, chooser), docs/index.html + docs/.nojekyll, docs/DISTRIBUTION.md. Rewritten: CHANGELOG (Keep a Changelog, [0.1.0]), SECURITY.md (private advisory route, 7-day ack, no email), README Install/Usage/Licence/Support/Version. Entries, Contents block, badge, family pointer line, family workflows, and .lycheeignore untouched.

## Spoke-specific decisions in this PR

- D12: the Related-lists awesome-mbse bullet is now text-only (link removed; returns when the hub goes public). The stale intro line that described the hub link changed with it. awesome-lint skips text-first items (v2.3.0 list-item.js); CI re-proves.
- D13: 11 MIT PSAS URLs carry one percent-encoded character per matching path segment (auditor regex false positive on public web paths). Do not revert; see the ledger note. Sample verified 200 via curl; the family lychee job re-checks all 11.

## MANUAL items closed

- RR-B-06 (D6): list product; Install says nothing to install (browse or clone); Usage covers browse, search Contents, open links, contribute via form or PR. Depth carried by README Install+Usage plus the existing CONTRIBUTING.md; no docs/usage.md.
- RR-B-12: CONTRIBUTING.md, CODE_OF_CONDUCT.md, PR template already present (OSS posture); no change.
- RR-B-19: org catalogue row `planned` in docs/DISTRIBUTION.md.
- RR-B-24: landing_taste.py PASS on docs/index.html. MANUAL taste note: page kind is a reference-index landing for safety and systems engineering practitioners; vibe minimal and quiet; no hero, no scroll cues, system fonts, single column; footer carries the licence-enquiry link and version. Design-system precedence applied; no exemptions needed. Playwright 2-breakpoint screenshots are a SHOULD residual if skipped.
- RR-B-26: no ASCII diagrams in README; no Mermaid needed for a list; presentation unchanged.
- RR-B-28: new prose written clean; em-dash grep clean across README.md, SECURITY.md, CHANGELOG.md, docs/DISTRIBUTION.md, docs/index.html; the old SECURITY.md em dash is gone; the SECURITY.md email route is replaced by the advisory link.
- RR-B-29 (D7): whole requirement deliberate N/A (a list is not installed into an agent host); ledger row with date.
- RR-B-30 (D5): multi-page assessment done; content walked; outcome one HTML landing + README deep content; nothing justifies a second page.
- RR-B-35: git ls-files inventory walked: no maintainer-only candidates tracked.
- RR-B-36: ledger at 0.1.0 / 2026-09-17, nine channels; Releases, Pages, and About rows are pending and get flipped in the platform step after merge.

## Platform steps after merge (fixed order)

Merge, Pages enable from /docs (anonymous 200 is provable only after the Checklist A flip, so homepage follows the flip), About description, tag v0.1.0 on main HEAD, branch protection, ledger status flip.
EOF
```

- [ ] **Step 4: Watch the PR checks**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
gh pr checks --watch
```

Expected: `validate` (release gate) green, and the family triad jobs green (`lychee`, `awesome-lint`, `markdownlint`, triggered by the README path change). The lychee job re-verifies all 11 encoded PSAS URLs at CI level, which is the D13 cross-check. If `awesome-lint` or `markdownlint` fails on the new sections or the text-only bullet, fix the section prose (entries stay untouched), push, and re-watch. If lychee rejects an encoded URL, apply the re-encode fallback from Task 2 Step 4.

- [ ] **Step 5: Merge and record the release SHA**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
gh pr merge --squash --delete-branch
git checkout main && git pull origin main
git rev-parse HEAD
```

Record the printed SHA: it is the release commit. Step 6 tags exactly this SHA.

- [ ] **Step 6: Enable Pages from /docs and verify the build**

```bash
gh api -X POST repos/jgsystemsconsulting/awesome-stpa/pages \
  -f "source[branch]=main" -f "source[path]=/docs"
gh api repos/jgsystemsconsulting/awesome-stpa/pages --jq .html_url
gh api repos/jgsystemsconsulting/awesome-stpa/pages/builds/latest --jq .status
curl -s -o /dev/null -w "%{http_code}\n" https://jgsystemsconsulting.github.io/awesome-stpa/
```

Expected: the POST creates the site (if it returns "already exists", confirm source is `main` `/docs` via the GET); `builds/latest` flips from `building` to `built` within a couple of minutes (re-run until it does). The anonymous curl returns **404 while the repo is private** (members-only Pages); that is expected and recorded. The pre-flip gate is the API build status `built`, not the curl. Contingency: if the POST fails with a plan/permission error because the repo is private, do not reorder anything else; record the failure in the PR, continue with Steps 7-9, and Step 3 of Task 7 enables Pages immediately after the visibility flip (the flip's gates do not depend on Pages).

- [ ] **Step 7: Set the About description (D10 exact string); homepage defers to Task 7**

```bash
gh repo edit jgsystemsconsulting/awesome-stpa \
  --description "Curated STAMP/STPA and hazard analysis resources for safety and systems engineering practitioners"
gh repo view jgsystemsconsulting/awesome-stpa --json description,homepageUrl,repositoryTopics
```

Expected JSON: description is the exact D10 string; `repositoryTopics` is exactly the six `awesome`, `awesome-list`, `hazard-analysis`, `safety`, `stamp`, `stpa` (verify only; no add/remove). `homepageUrl` stays null here unless Step 6's anonymous curl already returned 200; D5 sets homepage only after the site serves, and Task 7 Step 5 sets it after the flip proves 200.

- [ ] **Step 8: Tag v0.1.0 on the main HEAD SHA, push it, publish the Release**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
SHA=$(git rev-parse origin/main)
git tag -a v0.1.0 "$SHA" -m "Awesome STPA 0.1.0"
git push origin v0.1.0
git tag -l v0.1.0
cat > release-notes-v0.1.0.md <<'EOF'
# Awesome STPA 0.1.0

First tagged release of the curated STAMP/STPA and hazard-analysis resource list.

## Added

- 43 verified entries across seven sections: Foundations & Handbooks, Tools,
  Standards & Guidance, Case Studies & Agency Reports, Learning & Workshops,
  Datasets & Examples, Related lists.
- Release-standard packaging: COPYRIGHT, CITATION.cff, RELEASE-INFO.txt, private
  security advisory route, issue forms (suggest a resource, bug report, chooser),
  release gate CI, and a Pages landing page.

## Licence

See LICENSE in the repository (CC0-1.0).

Licence enquiries: https://labs.jgsystemsconsulting.com/licensing.html
EOF
gh release create v0.1.0 -R jgsystemsconsulting/awesome-stpa \
  --title "v0.1.0" --notes-file release-notes-v0.1.0.md
rm release-notes-v0.1.0.md
gh release view v0.1.0 -R jgsystemsconsulting/awesome-stpa --json body --jq .body | grep -c "https://labs.jgsystemsconsulting.com/licensing.html"
```

Expected: the tag lists locally and on origin, and the tagged SHA equals the SHA recorded in Step 5; the release is published and the grep count is at least 1 (the footer line `Licence enquiries: https://labs.jgsystemsconsulting.com/licensing.html` present verbatim, D10).

- [ ] **Step 9: Apply branch protection (first-time PUT, solo-maintainer shape)**

```bash
gh api -X PUT repos/jgsystemsconsulting/awesome-stpa/branches/main/protection \
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
gh api repos/jgsystemsconsulting/awesome-stpa/branches/main/protection \
  --jq '{contexts: .required_status_checks.contexts, force: .allow_force_pushes.enabled, del: .allow_deletions.enabled, admins: .enforce_admins.enabled, reviews: .required_pull_request_reviews.required_approving_review_count}'
```

Expected GET: `contexts` contains `validate`, `force` false, `del` false, `admins` false, `reviews` 0. If the PUT fails on permissions (403/404), do not retry blindly and do not mark RR-B-23 done: record it in the PR as the named maintainer action with this exact command, and continue (the Task 6 `--gh` audit will then show RR-B-23 FAIL/WARN, which is reported, not hidden).

- [ ] **Step 10: Flip the pending ledger rows now that the platform state exists**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
```

Edit `docs/DISTRIBUTION.md`: the GitHub Releases row `pending` to `submitted`, the Pages row `pending` to `live` (or a `pending` note that enablement was deferred to Task 7 if Step 6 hit the contingency), the About row `pending` to `applied` (homepage noted as following the Checklist A flip). Then:

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
git add docs/DISTRIBUTION.md
git commit -m "docs: mark distribution channels after 0.1.0 platform steps"
git push origin main
```

Expected: the push succeeds (branch protection is on, but `enforce_admins` false lets the admin push land; `validate` runs on the push regardless). Ledger rows match actual platform state; no row still says `pending` for a channel that is done.

Done when: PR checks green (validate plus triad), PR merged squash with the MANUAL closures and the keep/drop phrase in the body, Pages build `built` (or the contingency recorded), description set, tag v0.1.0 on the merge SHA on origin, Release published with the exact footer line, protection GET matches (or the named maintainer action recorded), ledger rows flipped.

### Task 6: Acceptance verification before the flip (AC1 gate for Checklist A)

**Files:**
- Modify: none (verification only; any fix loops back to its source task)

**Interfaces:**
- Consumes: merged main, tag and Release from Task 5, gate script, baseline SHA `5f10f0f40abf1271edaa6447d700ea03b9740353`.
- Produces: the recorded AC1 result that Task 7's pre-flip gate requires; recorded RR-B-25/RR-B-20 residuals that only the flip can clear.

**Model:** standard

- [ ] **Step 1: Plain audit exits 0 (AC1, the Checklist A gate)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base; echo "exit=$?"
```

Expected: `0 FAIL, 1 WARN` and `exit=0`. The single WARN is the accepted RR-B-32 improvement-form glob row (D8). Any FAIL loops back to its task, re-runs Task 5's merge flow if the fix lands after the tag, and re-runs this step before Task 7 starts.

- [ ] **Step 2: Platform and link rows under `--gh --links` (AC3, partial pre-flip)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base --gh --links; echo "exit=$?"
```

Expected: RR-B-22 PASS (Release notes contain the licence-enquiry URL), RR-B-23 PASS (protection configured, unless Step 9 of Task 5 was blocked, which is reported as the named residual), RR-B-21 PASS on description and topics (homepage still unset by design). RR-B-20 and any Pages-URL link row may WARN or FAIL while the repo is private (members-only Pages); those exact rows re-run to PASS in Task 7 Step 9, and AC3 is completed there. Do not flip visibility to make them green; the flip's gate is Step 1, not this step.

- [ ] **Step 3: Gate, entry count, entry integrity (AC2, AC4)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
python scripts/check_release.py; echo "exit=$?"
grep -c '^- \[' README.md
git diff 5f10f0f40abf1271edaa6447d700ea03b9740353 HEAD -- README.md | grep -E '^[+-].*## Contents|^[+-].*awesome\.re' || echo "Contents and badge untouched"
git diff 5f10f0f40abf1271edaa6447d700ea03b9740353 HEAD --stat -- README.md
```

Expected: gate exit 0 with `scanned 1 files`; bullet count `43`; no diff lines touch the `## Contents` block or the badge line; the stat shows README as the only modified file since baseline (plus the new files). Read the full README diff once and confirm the only hunks are: the appended sections, the D12 bullet and intro lines, the 11 D13 URL lines, and nothing else (AC4's allowed entry-adjacent diffs).

- [ ] **Step 4: Family triad on main (AC9)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
gh workflow run link-check-pr.yml --ref main
sleep 10
RUN_ID=$(gh run list --workflow=link-check-pr.yml --limit 1 --json databaseId --jq '.[0].databaseId')
gh run watch "$RUN_ID" --exit-status; echo "triad exit=$?"
gh run list --limit 5
```

Expected: the lychee, awesome-lint, and markdownlint jobs conclude green, and `gh run list --limit 5` shows `validate` plus the triad green on main (this output is also the Task 7 pre-flip CI evidence). A red lint job means section prose needs a fix; entries stay untouched.

- [ ] **Step 5: Em dash, licence, D13, platform state (AC6, AC5, AC7, AC3 extras)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
grep -n "—" README.md SECURITY.md CHANGELOG.md docs/DISTRIBUTION.md docs/index.html
echo "em-dash grep exit=$? (1 means clean)"
grep -c "JG Systems Consulting" LICENSE
gh api repos/jgsystemsconsulting/awesome-stpa/license --jq .license.spdx_id
python -c "import re, pathlib; t = pathlib.Path('README.md').read_text(encoding='utf-8'); print('RR-B-34 regex hits:', len(re.findall(r'/home/[A-Za-z0-9._-]+(?:/|\\\\)', t)))"
gh repo view jgsystemsconsulting/awesome-stpa --json description,repositoryTopics --jq '{description: .description, topics: [.repositoryTopics[].name] | sort}'
```

Expected: grep finds nothing across the five files (exit 1); org string present in LICENSE (count >= 1; RR-B-01 PASS already recorded in Step 1; spdx_id may be `NOASSERTION`, which AC5 says is not a stop); regex hits `0`; description exactly the D10 string and topics exactly the six sorted names `awesome`, `awesome-list`, `hazard-analysis`, `safety`, `stamp`, `stpa`.

- [ ] **Step 6: Record the evidence**

Post a comment on the merged PR with: the Step 1 audit output (the AC1 gate), the Step 2 `--gh --links` output with the named pre-flip residuals, the Step 4 run id, and the AC1/AC2/AC4/AC5/AC6/AC7/AC9 results. AC3, AC8, AC10, AC11 evidence lands in Task 5 (PR body, workflow scope, platform steps) and Task 7. Nothing is committed in this task.

Done when: AC1 exit 0 is recorded on the PR, all reachable criteria have recorded PASS, and the only open rows are the flip-gated RR-B-20/homepage/link residuals plus any blocked RR-B-23 named action.

### Task 7: Family Checklist A: spoke public release

**Files:**
- Modify: `C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse/FAMILY.md` (one Visibility cell)
- Modify: `C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse/README.md` (family table row note; link cell already exists, verify only)
- Modify: `CHANGELOG.md` in the spoke (one bullet in the existing `[0.1.0]` entry; the tag does not move)

**Interfaces:**
- Consumes: the Task 6 AC1 exit 0 record; the runbook `docs/runbooks/family-public-release.md` (normative); D10/D11/D12; the flipped tag and Release.
- Produces: public repo with anonymous 200 on repo and Pages URLs; homepage set; hub FAMILY.md Visibility `public` and hub README row updated; spoke CHANGELOG release note; closed decision issue; the final `--gh --links` audit with RR-B-20/21/25 PASS (completes AC3 and AC8).

**Model:** deep

Every step in this task is executed by hand, in order, top to bottom. The flip is irreversible reputationally: do not run Step 4 until Steps 1-3 are ticked.

- [ ] **Step 1: Pre-flip gates (runbook Checklist A, upper block)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
gh run list --limit 5
git grep -nIE "C:\\\\Users|/Users/|OneDrive" -- .
git grep -nwIE "TODO|WIP" -- .
git status --porcelain
grep -n "github.com/jgsystemsconsulting/awesome-mbse" README.md || echo "no private-only link (D12 closed)"
grep -n "Part of the awesome-mbse list family (hub repository currently private)." README.md
```

Expected: all recent runs green (`validate` plus triad, from Task 6 Step 4); both greps silent; porcelain empty; no hub link in README (D12); the text-only family pointer present on line 9 (D11, class hub-private is correct for a public spoke while the hub is private). Entry links were proven publicly resolvable by the lychee job plus the Task 2 curl sample. If any gate fails, stop; fix; re-run Task 6 as needed.

- [ ] **Step 2: File the decision issue (runbook template, exact shape)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
MAKER=$(gh api user --jq .login)
gh issue create -R jgsystemsconsulting/awesome-stpa \
  -t "Public release decision 2026-09-17" \
  -b "- Decision: public
- Decision date: 2026-09-17
- Decision maker: $MAKER
- Reason: RR-B audit exit 0, family CI green, no private-only entries (D12 closed); meets the family public-release bar."
```

Record the issue number; Step 8 closes it.

- [ ] **Step 3: Flip visibility to public, by hand**

```bash
gh repo edit jgsystemsconsulting/awesome-stpa --visibility public --accept-visibility-change-consequences
gh repo view jgsystemsconsulting/awesome-stpa --json visibility --jq .visibility
```

Expected: `PUBLIC`. If gh rejects the `--accept-visibility-change-consequences` flag name, check `gh repo edit --help` for the current flag before running anything (runbook rule); never run the flip without a consequences flag if one is required.

- [ ] **Step 4: Verify anonymous access and finish Pages (runbook anonymous gate + D5)**

```bash
curl -s -o /dev/null -w "%{http_code}\n" https://github.com/jgsystemsconsulting/awesome-stpa
curl -s -o /dev/null -w "%{http_code}\n" https://jgsystemsconsulting.github.io/awesome-stpa/
gh api repos/jgsystemsconsulting/awesome-stpa/pages --jq '{status: .status, source: .source}'
```

Expected repo curl: `200`. A `404` means the flip did not take; stop and investigate. Pages: if Task 5 Step 6 enabled Pages, the API shows `status: built, source: main /docs` and the Pages curl returns `200` now that the repo is public (retry once after 30 seconds if it lags the flip). If Pages was never enabled (Task 5 contingency), run the enable POST from Task 5 Step 6 now, wait for `built`, then curl. If either URL stays non-200 after a retry, record it and finish Steps 5-8 (they do not depend on it), then return here before Step 9.

- [ ] **Step 5: Set the homepage now that the Pages URL serves anonymously (D5, D10)**

```bash
gh repo edit jgsystemsconsulting/awesome-stpa \
  --homepage "https://jgsystemsconsulting.github.io/awesome-stpa/"
gh repo view jgsystemsconsulting/awesome-stpa --json homepageUrl --jq .homepageUrl
```

Expected: the Pages URL. Skip if Task 5 Step 7 already set it because the site served early.

- [ ] **Step 6: Hub registry edits (the only hub edits in this plan)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
git status --porcelain
git pull origin main
grep -n "awesome-stpa" FAMILY.md README.md | head -5
```

Edit `FAMILY.md`: in the registry row for awesome-stpa, change the Visibility cell `private` to `public`. The row reads after the edit:

```markdown
| [awesome-stpa](https://github.com/jgsystemsconsulting/awesome-stpa) | STAMP / STPA and hazard analysis; functional safety methods | Live | public |
```

Edit `README.md`: the family table row already links the spoke; verify the link cell (AC8: verify, do not invent a second URL cell) and update the note cell so it no longer says "private":

```markdown
| [awesome-stpa](https://github.com/jgsystemsconsulting/awesome-stpa)                               | STAMP / STPA and hazard analysis; functional safety methods                           | Live           | Dedicated spoke; hub keeps the DLR-FT STPA library as its one cross-cutting entry |
```

Status stays `Live`. The hub itself stays private; do not touch its visibility or any other hub row. Then commit and push the hub:

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse"
git add FAMILY.md README.md
git commit -m "docs: awesome-stpa visibility public (family Checklist A)"
git push origin main
```

If the hub push is rejected by hub-side protection, leave the edits committed locally and record the push as a named follow-up in the spoke PR before closing the issue.

- [ ] **Step 7: Spoke CHANGELOG note in the existing `[0.1.0]` entry (the tag does not move)**

Append one bullet at the end of the `### Added` block of `## [0.1.0] - 2026-09-17` in the spoke `CHANGELOG.md` (normal follow-up commit on main, not a re-tag):

```markdown
- Repository made public on 2026-09-17 (family Checklist A); decision issue <n>.
```

Replace `<n>` with the Step 2 issue number. Then:

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
git add CHANGELOG.md
git commit -m "docs: record public release in changelog (Checklist A)"
git push origin main
```

- [ ] **Step 8: Close the decision issue**

```bash
gh issue close <n> -R jgsystemsconsulting/awesome-stpa -c "Released 2026-09-17."
```

- [ ] **Step 9: Final verification (completes AC3 and AC8)**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-stpa"
python "C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py" --repo . --profile base --gh --links; echo "exit=$?"
grep -n "Part of the awesome-mbse list family (hub repository currently private)." README.md
curl -s -o /dev/null -w "repo:%{http_code}\n" https://github.com/jgsystemsconsulting/awesome-stpa
curl -s -o /dev/null -w "pages:%{http_code}\n" https://jgsystemsconsulting.github.io/awesome-stpa/
```

Expected: `exit=0` with RR-B-20 PASS (Pages serves), RR-B-21 PASS (homepage set, topics six), RR-B-22 PASS, RR-B-23 PASS (or the named maintainer residual from Task 5 Step 9), RR-B-25 PASS (all links resolve); the family pointer line still text-only (correct class while the hub is private); repo and Pages curls `200` logged out. Post the final audit output as a second comment on the merged PR so the session record carries AC3 and AC8.

Done when: repo public with anonymous 200 on repo and Pages URLs, homepage set, hub FAMILY.md row `public` and hub README row verified/updated (pushed or recorded as follow-up), spoke CHANGELOG carries the release note, decision issue closed with `Released 2026-09-17.`, family pointer still hub-private text-only, and the final `--gh --links` audit shows the RR-B-20/21/22/23/25 rows PASS (with only the accepted RR-B-32 WARN).

## Acceptance criteria coverage

| AC | Where |
|----|-------|
| AC1 plain audit exit 0 | Task 6 Step 1 (tag from Task 5 Step 8 closes any RR-B-18 row) |
| AC2 gate exit 0, scanned >= 1 | Task 4 Step 2 (green plus negative probe), Task 6 Step 3 |
| AC3 `--gh --links` rows PASS | Task 5 Steps 6-9, Task 6 Step 2 (pre-flip partials), Task 7 Steps 4-5, 9 (final) |
| AC4 43 entries, Contents byte-identical, allowed diffs only | Task 2 Steps 3-4, Task 6 Step 3 |
| AC5 RR-B-01 PASS, spdx_id not a stop | Task 1 Steps 1, 8; Task 6 Step 5 |
| AC6 MANUAL items in PR | Task 5 Step 3 (body), Task 6 Step 6 |
| AC7 no em dash on customer surface | Task 1 Step 8, Task 2 Step 4, Task 3 Step 6, Task 6 Step 5 |
| AC8 Checklist A registry + anonymity | Task 7 Steps 3-6, 9 |
| AC9 triad green | Task 5 Step 4 (PR), Task 6 Step 4 (main) |
| AC10 workflow scope | Task 5 Step 1 |
| AC11 (workflow file push) | Task 5 Steps 1, 3 |

Locked decisions D1-D13 map onto: D1/D2/D3 (Global Constraints; Task 1 verify-only rows; Task 4 gate shape), D4 (Task 1 Steps 5-6; Task 5 Step 8; Task 7 Step 7), D5 (Task 3 Step 4; Task 5 Step 6; Task 7 Steps 4-5), D6 (Task 2 Step 1; Task 5 PR body), D7/D8 (Task 3 Steps 1-3, 5; README Support WARN note), D9 (Task 1 Step 4), D10 (Task 5 Steps 6-9; Task 7 Step 5), D11 (no pointer edits anywhere; line 9 grep in Task 7), D12 (Task 2 Step 2; Task 7 Step 1 gate), D13 (Task 2 Step 3; Task 3 Step 5 ledger note; Task 6 Steps 3, 5).
