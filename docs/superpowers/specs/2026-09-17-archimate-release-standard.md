# Spec: Release Repo Standard for jgsystemsconsulting/awesome-archimate

**Date:** 2026-09-17
**Target repo:** `C:\Users\gower\OneDrive\Documents\GitHub\awesome-archimate` (public spoke, https://github.com/jgsystemsconsulting/awesome-archimate)
**Standard:** Release Repo Standard v1.14, profile **RR-B Base only**, **open-source posture (CC0-1.0)**, **standalone build model**
**Auditor:** `tools/audit.py` from the `release-repo-standard` skill, run with `--profile base`
**Pattern source:** the Capella RR-B close executed 2026-09-17 (`docs/superpowers/specs/2026-09-17-repo-release-standard-capella.md`). Same decisions, ArchiMate product strings, 17-entry facts, and the archimate family triad file names.

## Problem

The archimate spoke is a live awesome list (17 verified seed entries, family CI triad `links.yml`/`lint.yml`/`stale.yml`) but under Release Repo Standard v1.14 Base it is not release-ready. It has no scripts, no docs, no issue forms, no PR template, and none of the release identity surface: missing COPYRIGHT/NOTICE, RELEASE-INFO.txt, CITATION.cff, semver CHANGELOG (Unreleased-only today), release gate CI, .gitignore, distribution ledger, SECURITY private-advisory route (the current file publishes `support@jgsystemsconsulting.com` instead), README Install/Usage/Licence/Support headings with the licence-enquiry URL, and the RR-B-20 MUST Pages landing page. A baseline `audit.py --profile base` count has not been recorded for this spoke; the plan snapshots it on first run before any edit.

This spec closes the machine-checkable gaps and the RR-B-20 MUST with the smallest spoke-local set, clones the Capella locked decisions, keeps the family triad untouched, and records list-product interpretations. **Audit exit 0 is necessary but not sufficient for "standard-complete"** until named MANUAL items and Pages enablement are done. This pass is RR-B packaging on an already-public list; visibility flips are the hub runbook's concern and stay out of scope.

## Goals

1. `python tools/audit.py --repo ../awesome-archimate --profile base` exits 0 (zero FAIL rows). With `--gh --links`: RR-B-21/22/25 are **PASS**; RR-B-20 is **PASS** when Pages is enabled (file-level PASS once `docs/index.html` carries the licence-enquiry URL; platform row is PASS once Pages API succeeds, WARN only if enablement lags); RR-B-23 is **PASS** once branch protection exists, otherwise **WARN** (solo-maintainer SHOULD until protection is applied, still MUST when external contributions are accepted).
2. Release identity end to end: version 0.1.0 across CHANGELOG, RELEASE-INFO.txt, CITATION.cff, tag `v0.1.0`, published GitHub Release notes with licence-enquiry URL.
3. Automated release gate: `scripts/check_release.py` plus `.github/workflows/validate.yml`, additive to the family triad.
4. SECURITY.md: private advisory route, email removed, no em dash.
5. `docs/index.html` + `docs/.nojekyll` ship self-contained (no CDN, no third-party fonts, fixing the sysml-v2 flaw); GitHub Pages serves the site (RR-B-20 MUST). Homepage URL set to the Pages URL (RR-B-21).
6. Deliberate N/A or deferred channels live in `docs/DISTRIBUTION.md` with decision + date.

## Non-goals

- No changes to the 17 README seed entries, their ordering, tags, or the flat `## Contents` block (8 hand-maintained links). Those stay byte-identical.
- No changes to `links.yml`, `lint.yml`, or `stale.yml`; the triad stays as is. `validate.yml` is added as a separate file.
- No licence change. The repo stays CC0-1.0; GitHub already detects CC0-1.0 on LICENSE.
- No entry-format checker script. Capella needed `check_entries.py` because it shipped one; archimate has no scripts and `lint.yml` (awesome-lint, markdownlint) is the existing format gate. Adding one is YAGNI unless audit demands it.
- No multi-page docs site beyond the single RR-B-20 landing page. No marketing redesign.
- No hub (awesome-mbse) edits. Everything here is spoke-local.
- No git history rewrite. RR-B-27 already passes: commits use `245595077+jgsystemsconsulting@users.noreply.github.com`.
- No MCP/skills/research profile work (no RR-M/RR-S/RR-R rows).

## Locked decisions

These are fixed by the dispatch or by this spec as the single recommendation. They are not open for re-litigation in the plan or execution.

| # | Decision |
|---|----------|
| D1 | Profile: RR-B Base only. The list is a curated index, not an MCP bridge, skills pack, or research instrument. |
| D2 | Licence posture: open source, CC0-1.0, unchanged. COPYRIGHT/NOTICE ship per templates; NOTICE states no third-party code is distributed. |
| D3 | Build model: standalone. Fixes commit directly to the spoke; the RR-B-15 gate is `scripts/check_release.py` + `.github/workflows/validate.yml`. |
| D4 | Version: **0.1.0**, dated 2026-09-17. CHANGELOG.md (top entry) is the version source; propagated to RELEASE-INFO.txt, CITATION.cff, tag `v0.1.0`, GitHub Release. |
| D5 | Landing surface: ship **RR-B-20 MUST** as a minimal self-contained `docs/index.html` + `docs/.nojekyll`, enable GitHub Pages from `/docs`, set homepage to https://jgsystemsconsulting.github.io/awesome-archimate/. Content: what the list is, how to browse, how to suggest an entry, link to README on GitHub, licence-enquiry URL. Required meta: non-empty title, meta description, canonical link, Open Graph tags. No CDN, no third-party fonts, no em dash. Include `@media (prefers-reduced-motion: reduce)`. RR-B-24: mechanical taste overlay when available (overlay FAIL must be fixed for audit exit 0); Playwright desktop+mobile screenshots recorded if tool available, else named MANUAL residual; SEO pass recorded. RR-B-30: outcome "one HTML landing + README deep content". |
| D6 | Usage interpretation: **Install** heading states there is nothing to install (browse on GitHub or clone). **Usage** covers browse, search Contents, open links, contribute via issue form/PR. RR-B-06 depth is README Install+Usage plus the existing CONTRIBUTING.md; no separate docs/usage.md. |
| D7 | RR-B-29: the whole requirement is deliberate N/A (a list is not installed into an agent host, so no marketplace manifests). Recorded in the ledger with a date. |
| D8 | RR-B-32 improvement form: unlike Capella (which kept a legacy form and accepted a WARN), archimate has **no issue forms at all**, so the pass **adds `suggest-resource.yml`** (resource name, URL, section, why it fits, licence checkbox) alongside `bug_report.yml` and `config.yml`. The auditor improvement-form glob matches substrings `improv`/`enhanc` in the filename; `suggest-resource.yml` will not match, so a **WARN** is expected and accepted (named in the PR). Do not rename the form solely to silence the glob. |
| D9 | SECURITY route: private GitHub security advisory (and PR with fix for non-sensitive issues). The `support@jgsystemsconsulting.com` line is removed. No email anywhere in SECURITY.md, so RR-B-07 stays PASS rather than WARN. |
| D10 | Platform state in this pass: tag + published GitHub Release v0.1.0 (RR-B-18/22), branch protection on `main` (RR-B-23 solo-maintainer shape), About description + topics, **homepageUrl = the Pages URL** after RR-B-20 is live (RR-B-21). |
| D11 | Family pointer stays text-only on the public spoke (FAMILY Private mode). No hub FAMILY.md hyperlink. |

## Requirement mapping (RR-B id to archimate action)

| ID | Requirement | Action for awesome-archimate | Audit row after |
|----|-------------|------------------------------|-----------------|
| RR-B-00 | Fix source, not output | N/A (standalone model) | none |
| RR-B-01 | LICENSE | Keep the CC0-1.0 Universal body. Append one trailing line `Copyright (c) 2026 JG Systems Consulting Ltd.` so `audit.py` finds the org string (same append Capella used on its LICENSE for the auditor; COPYRIGHT/NOTICE still carry the full copyright assertion). Do not rewrite the CC0 legal text. After append, re-check `gh api repos/.../license --jq .license.spdx_id` stays CC0-1.0; if it flips to NOASSERTION, restore canonical CC0 text and put the org string only in COPYRIGHT/NOTICE while documenting a residual RR-B-01 strategy change | PASS |
| RR-B-02 | COPYRIGHT + NOTICE | Add both from skill templates `COPYRIGHT.tmpl` / `NOTICE.tmpl` with org **JG Systems Consulting Ltd**, year 2026, product Awesome ArchiMate. NOTICE: no vendored third-party code; linked resources keep their own licences. Body text is the filled template, not invented prose | PASS x2 |
| RR-B-03 | Per-file headers | The repo has zero first-party .py today; `check_release.py` ships with the two-line header, which covers the auditor's grep scope. No existing file needs a header | PASS on auditor scope |
| RR-B-04 | SPDX | `SPDX-License-Identifier: CC0-1.0` in the check_release.py header | PASS |
| RR-B-05 | README sections | Add real headings **Install**, **Usage**, **Licence** (links LICENSE + `https://labs.jgsystemsconsulting.com/licensing.html`), **Support**, plus Version/changelog line. Install body: nothing to install; browse or clone. Seed entries and Contents untouched | PASS |
| RR-B-06 | Install/usage depth | Install + Usage sections (D6) plus existing CONTRIBUTING.md. No separate docs/usage.md | MANUAL, addressed |
| RR-B-07 | SECURITY route | Rewrite SECURITY.md: private advisory link `https://github.com/jgsystemsconsulting/awesome-archimate/security/advisories/new`, PR-with-fix for non-sensitive, response-time **We aim to acknowledge reports within 7 days**, scope notes (malicious/hijacked links, CI), remove the support@ email, no em dash | PASS |
| RR-B-08/09 | CHANGELOG + version source | CHANGELOG already declares Keep a Changelog 1.1.0 but is Unreleased-only. Replace `## [Unreleased]` content with `## [0.1.0] - 2026-09-17` top entry holding the seed bullets under Added/Notes; keep an empty `[Unreleased]` above it | PASS (09) / present (08) |
| RR-B-10 | RELEASE-INFO.txt | Add: Product Awesome ArchiMate, Version 0.1.0, Built: UTC ISO-8601 `YYYY-MM-DDTHH:MM:SSZ` at release-commit time, Tag: v0.1.0 | PASS |
| RR-B-11 | Clean layout | Already clean (**10** tracked files today per `git ls-files`); new files land in their standard slots | PASS |
| RR-B-12 | Community files (OSS posture) | CONTRIBUTING, CODE_OF_CONDUCT exist. PR template does **not**: add `.github/PULL_REQUEST_TEMPLATE.md` with guardrail checkboxes (entries untouched, links checked, no em dash, version files updated together) | MANUAL, met after add |
| RR-B-13 | .gitignore | Add root `.gitignore` (OS cruft, `__pycache__/`, `.venv/`, `.lycheecache`, `.playwright-mcp/`, `*.bak`) | PASS |
| RR-B-14 | No secrets | Nothing to add; leak scan stays clean | PASS |
| RR-B-15 | Automated release gate | Clone Capella spoke `scripts/check_release.py` and `.github/workflows/validate.yml`, then adapt: drop `scripts/check_entries.py` from REQUIRED; keep REQUIRED without that path; header lines exactly `# Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE.` and `# SPDX-License-Identifier: CC0-1.0`; SCAN_GLOBS = `scripts/*.py`. Gate exits 0 and prints scanned count >= 1. `validate.yml`: job id `validate`, `on: push/pull_request to main` plus `workflow_dispatch`, `permissions: contents: read`, pin checkout to full SHA `actions/checkout@11d5960a326750d5838078e36cf38b85af677262` (# v4, same as triad), setup-python 3.12 with pin from Capella validate if present else SHA-pinned setup-python, run `python scripts/check_release.py`. Separate file; triad untouched | PASS |
| RR-B-16 | Agent-install prompt | Skipped: SHOULD, and a list has no install step to automate | not checked |
| RR-B-17 | llms.txt / AGENTS.md | Skipped: MAY | not checked |
| RR-B-18 | Tagged release | Create and push tag `v0.1.0` on the release commit | PASS |
| RR-B-19 | Catalogue entry | No org catalogue entry exists; ledger row `planned` with date | MANUAL via ledger |
| RR-B-20 | Landing page | Ship `docs/index.html` + `docs/.nojekyll`; enable Pages from /docs (D5). Self-contained; licence-enquiry link; first-run = open the list | PASS with --gh |
| RR-B-21 | About metadata | Description exactly: `Curated ArchiMate resources for enterprise architecture and MBSE practitioners`. Topics (at least six names for the auditor): `archimate`, `awesome`, `awesome-list`, `enterprise-architecture`, `mbse`, `togaf`. Set homepageUrl to https://jgsystemsconsulting.github.io/awesome-archimate/ after Pages enablement. Note: current `audit.py --gh` PASS for RR-B-21 keys on description + topics count (>=6) and does not fail on missing homepageUrl; still set homepage as product policy | PASS with --gh |
| RR-B-22 | GitHub Release | Publish Release v0.1.0 from CHANGELOG notes. Footer line exactly: `Licence enquiries: https://labs.jgsystemsconsulting.com/licensing.html` | PASS with --gh |
| RR-B-23 | Branch protection | Protect `main`: required PR + the `validate` check, force-push and deletion off, `enforce_admins` off and 0 required approvals (solo maintainer). Auditor emits PASS when protection API succeeds, WARN when absent | PASS or WARN until applied |
| RR-B-24 | Landing quality | Mechanical taste overlay on docs/*.html when tool available: any FAIL finding must be fixed before claiming audit exit 0. MANUAL: taste note + Playwright 2-breakpoint screenshots when tool available, else named residual; SEO pass recorded | PASS or named MANUAL residual after overlay clean |
| RR-B-25 | Link integrity | Family triad (`links.yml`, lychee, PR + weekly schedule + dispatch) already covers README links; run it once via workflow_dispatch after README edits; record the pass. Run `audit.py --links` once | PASS |
| RR-B-26 | Doc presentation | No ASCII diagrams in the README; no Mermaid needed for a list. Callout/table usage already fine | MANUAL, met |
| RR-B-27 | Commit identity | Already canonical (noreply identity on every commit). No action | PASS |
| RR-B-28 | De-slopped prose | New/edited prose (README sections, SECURITY.md, CHANGELOG entry, ledger, landing page) written clean; run the de-slop pass over README/docs/CHANGELOG; SECURITY.md email and em dash removed; grep shows zero em dashes on the customer surface | PASS |
| RR-B-29 | Marketplace manifests | Deliberate N/A with reason + date in ledger (D7) | none on plain run |
| RR-B-30 | Multi-page assessment | Recorded: content walked, outcome **one HTML landing + README deep content** (D5); nothing justifies a third page | MANUAL, recorded |
| RR-B-31 | CITATION.cff | Add CFF 1.2.0: title Awesome ArchiMate, version "0.1.0", date-released 2026-09-17, authors entity JG Systems Consulting Ltd, repository-code the repo URL, license CC0-1.0 (Capella/sysml-v2 shape with archimate strings) | PASS |
| RR-B-32 | Bug-report + improvement channels | Clone Capella issue-form YAML shapes where present; adapt strings. Add `bug_report.yml`, `config.yml` (`blank_issues_enabled: false`; contact_links: (1) Security advisory -> `https://github.com/jgsystemsconsulting/awesome-archimate/security/advisories/new`, (2) awesome-capella issues -> `https://github.com/jgsystemsconsulting/awesome-capella/issues`), and `suggest-resource.yml` as the improvement channel (D8). README Support names every channel | PASS (+ WARN only if the filename glob still objects, non-blocking) |
| RR-B-33 | No BOM | Write new YAML/CFF as plain UTF-8, verify first bytes; audit covers it | PASS |
| RR-B-34 | No local paths | New files carry no machine-local paths; audit verifies | PASS |
| RR-B-35 | Keep/drop inventory | Walk `git ls-files` (10 files today): no maintainer-only prefixes tracked. Record "no candidates" in the PR | PASS |
| RR-B-36 | Distribution ledger | Add `docs/DISTRIBUTION.md` using RR-B-36 status vocabulary only (`submitted`, `in progress`, `deferred`, `deliberate N/A`, `planned`): GitHub repo (submitted), GitHub Releases v0.1.0 (submitted), Pages landing (submitted once enabled), About/topics+homepage (submitted), org catalogue (planned), sindresorhus/awesome (deferred, acceptability gate), in-host marketplaces (deliberate N/A), MCP directories (deliberate N/A), community EA/ArchiMate directories (deferred). Header: last reviewed 0.1.0, 2026-09-17 | PASS |

## File inventory

New files (all in the spoke):

- `COPYRIGHT`
- `NOTICE`
- `RELEASE-INFO.txt`
- `CITATION.cff`
- `.gitignore`
- `docs/DISTRIBUTION.md`
- `docs/index.html`
- `docs/.nojekyll`
- `scripts/check_release.py`
- `.github/workflows/validate.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/suggest-resource.yml`

Modified files:

- `README.md` (Install, Usage, Licence, Support, Version sections; the 17 entries and the 8-link Contents untouched)
- `SECURITY.md` (advisory route, email removed, no em dash)
- `CHANGELOG.md` (`## [0.1.0] - 2026-09-17` top entry, seed bullets moved under Added/Notes, empty `[Unreleased]` kept)

Platform actions (recorded in the PR, not files), **order fixed**:

1. Merge release commit to `main` (final SHA).
2. Enable GitHub Pages from `/docs`; verify the site serves (HTTP 200 on the Pages URL).
3. Set About description + topics; set **homepageUrl only after** Pages serves.
4. Tag `v0.1.0` on **that main HEAD** SHA; publish GitHub Release v0.1.0 from CHANGELOG + licence-enquiry footer.
5. Branch protection on `main` (first-time PUT): after the first green `validate` run, set required checks to the exact context string GitHub reports for that check (often `validate` for a job named `validate` in workflow `validate`; if UI shows `validate / validate`, use that string). Force-push off, deletion off, `enforce_admins` false, required approving reviews 0 (solo maintainer residual: direct pushes can bypass; named in PR).

## Acceptance criteria

1. Baseline audit count recorded on first run, then `python tools/audit.py --repo ../awesome-archimate --profile base` exits 0: zero FAIL rows. Expected non-blocking: at most an RR-B-32 WARN from the improvement-form filename glob (D8). RR-B-20 is proven only under AC3 (`--gh`), not by absence of a plain-run FAIL row.
2. `python scripts/check_release.py` in the spoke root exits 0 and prints a scanned-file count >= 1.
3. With `--gh --links`: RR-B-21 PASS (description + >=6 topics), RR-B-22 PASS (Release notes contain `https://labs.jgsystemsconsulting.com/licensing.html`), RR-B-25 PASS; RR-B-20 PASS once Pages is enabled and `docs/index.html` contains the licence-enquiry URL (file-level check always, platform PASS after enablement); RR-B-23 PASS after protection is applied (WARN acceptable only if protection is deferred and named). Homepage URL is set to the Pages URL as product policy even though the auditor may not fail on unset homepage.
4. Entry integrity: README still has exactly 17 seed-entry bullets plus the 8 Contents links (25 total `- [` bullets). Prove seed freeze by hashing or diffing the 25 `- [` lines against pre-edit `git show HEAD:README.md` (or equivalent); counts alone are not enough. After the release push to `main`, `lint.yml` is green on that push (awesome-lint + markdownlint are the format gate; no separate checker script by design). Do not require `workflow_dispatch` on `lint.yml` (it has no such trigger; triad stays unchanged).
5. Family triad green after README/SECURITY edits: `links.yml` via `workflow_dispatch` on main; `lint.yml` via the release push on main (see AC4).
6. MANUAL items closed in the PR: RR-B-06 (D6), RR-B-12 (PR template added), RR-B-19/29 (ledger), RR-B-24 (taste + Playwright/SEO or named residual), RR-B-26, RR-B-28 (de-slop = em-dash/email grep zero on customer surface plus prose review note), RR-B-30 (one HTML + README), RR-B-35 (no candidates), RR-B-36 (ledger at 0.1.0).
7. No em dash and no `support@jgsystemsconsulting.com` occurrence in README.md, SECURITY.md, CHANGELOG.md, docs/DISTRIBUTION.md, docs/index.html body copy.
8. Workflow file push succeeds (`gh auth refresh -s workflow` if needed).
9. `gh api repos/jgsystemsconsulting/awesome-archimate/license --jq .license.spdx_id` returns CC0-1.0 (research indicates it already does).

## Risks

- **RR-B-20 is MUST.** Deferring Pages leaves a standard residual even if plain audit.py stays quiet; this pass ships the landing page. Pages enablement needs admin on the repo.
- **No baseline audit number exists for this spoke.** The plan snapshots `--profile base` before the first edit so the closing diff is provable. Do not quote a FAIL count that was never run.
- **README edits can trip awesome-lint.** The badge line and flat `## Contents` stay byte-identical; new sections are appended below. Entry-format rules are unaffected because no entry line changes. The triad run (criterion 5) is the guard.
- **Adding version artifacts creates a new RR-B-18 FAIL until the tag exists.** The tag is part of the same change set, created on the release commit before the audit claim. Do not split the version files from the tag across PRs.
- **`check_release.py` template defaults assume an src/ layout and unsubstituted placeholders.** The REQUIRED list, SCAN_GLOBS, and the header sentinel must be edited for this tree, or the gate false-fails (sentinel never matches) or false-passes (globs match nothing). Both directions are covered by criteria 1 and 2.
- **SECURITY.md wording is load-bearing.** The audit row requires the word `advisories` or `pull request`; any email in the file downgrades to WARN. The rewrite keeps the advisory link and deletes the support@ line.
- **Windows BOM risk on hand-written YAML/CFF.** RR-B-33 fails on a BOM'd `.cff` or `.yml`. Verify first bytes after writing; the audit also checks.
- **Branch protection PUT can fail on permissions.** If the `gh api` PUT fails, record RR-B-23 as the named maintainer action with the exact command in the PR; do not mark it done.

## Research

- https://github.com/jgsystemsconsulting/awesome-archimate
- https://jgsystemsconsulting.github.io/awesome-archimate/ (planned Pages URL; 404 until RR-B-20 enablement)
- https://labs.jgsystemsconsulting.com/licensing.html
- https://github.com/jgsystemsconsulting/awesome-archimate/security/advisories/new
- https://github.com/jgsystemsconsulting/awesome-capella
- file://C:/Users/gower/.zcode/skills/release-repo-standard/references/release-repo-standard.md (v1.14, normative)
- file://C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py (auditor)
- file://C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse/docs/superpowers/research/2026-09-17-archimate-release-standard-research.md
- file://C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse/docs/superpowers/context/2026-09-17-archimate-release-standard-context.md
- file://C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse/docs/superpowers/specs/2026-09-17-repo-release-standard-capella.md (pattern source, executed 2026-09-17)

## Codebase context

The spoke ships **10** tracked files (`git ls-files`): README (17 entries across eight sections plus an 8-link flat Contents, awesome badge line 1), CC0-1.0 LICENSE, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY.md (line 9 publishes `support@jgsystemsconsulting.com`; must go), CHANGELOG (Keep a Changelog 1.1.0 header, `[Unreleased]` only), `.markdownlint-cli2.jsonc`, and the family triad `.github/workflows/links.yml` (lychee, PR + Monday schedule + dispatch), `lint.yml` (lint on PR/push to main only, no workflow_dispatch), `stale.yml` (monthly freshness report). Action refs in the triad are pinned to full-length commit SHAs (`actions/checkout@11d5960a326750d5838078e36cf38b85af677262`); validate.yml follows the same pinning discipline. Missing relative to the standard: everything in the File inventory above; there are no scripts, docs, issue forms, or PR template today. Plan execution clones Capella `check_release.py` / `validate.yml` / COPYRIGHT / NOTICE / CITATION shapes rather than inventing them.

Family constraints that bind this pass: the triad is green and must stay untouched; the public spoke uses a text-only family pointer (FAMILY Private mode, no hub FAMILY.md URL); commit identity is already the canonical noreply address. The sibling spoke `awesome-capella` closed the same bar on 2026-09-17 and is the executed pattern; `awesome-sysml-v2` supplies the CITATION.cff shape but still fails many Base rows, so it is not the clone target.
