# Spec: Release Repo Standard for jgsystemsconsulting/awesome-capella

**Date:** 2026-09-17
**Target repo:** `C:\Users\gower\OneDrive\Documents\GitHub\awesome-capella` (public spoke, https://github.com/jgsystemsconsulting/awesome-capella)
**Standard:** Release Repo Standard v1.14, profile **RR-B Base only**, **open-source posture (CC0-1.0)**, **standalone build model**
**Auditor:** `tools/audit.py` from the `release-repo-standard` skill, run with `--profile base`

## Problem

The 2026-09-17 audit run of `tools/audit.py --repo .../awesome-capella --profile base` reported **14 FAIL, 2 WARN, 8 PASS**. The spoke is a live awesome list (73 verified entries, family CI triad green), but under Release Repo Standard v1.14 Base it is not release-ready: missing COPYRIGHT/NOTICE, release identity (semver, RELEASE-INFO.txt, CITATION.cff, tag), release gate CI, .gitignore, distribution ledger, complete issue forms, SECURITY private-advisory route (no email), README Install/Usage/Licence/Support headings (with licence-enquiry URL), SPDX header on the checker, and a Pages landing page (RR-B-20 MUST).

This spec closes the machine-checkable gaps and the RR-B-20 MUST with the smallest spoke-local set, keeps the family CI triad untouched, and records list-product interpretations. **Audit exit 0 is necessary but not sufficient for "standard-complete"** until named MANUAL items and RR-B-20 Pages enablement are done. A separate hub runbook (family public-release context) covers private-to-public visibility flips; this pass is RR-B packaging on an already-public list, by explicit user invoke of the release-repo-standard skill.

## Goals

1. `python tools/audit.py --repo ../awesome-capella --profile base` exits 0 (zero FAIL rows). With `--gh --links`, RR-B-20/21/22/23/25 are **PASS** (no residual-named stop-short).
2. Release identity end to end: version 0.1.0 across CHANGELOG, RELEASE-INFO.txt, CITATION.cff, tag `v0.1.0`, published GitHub Release notes with licence-enquiry URL.
3. Automated release gate: `scripts/check_release.py` plus `.github/workflows/validate.yml`, additive to the family triad.
4. SECURITY.md: private advisory route, no email, no em dash.
5. `docs/index.html` + `docs/.nojekyll` ship; GitHub Pages serves the site (RR-B-20 MUST). Homepage URL set to the Pages URL (RR-B-21).
6. Deliberate N/A or deferred channels (marketplaces, catalogue, sindresorhus) live in `docs/DISTRIBUTION.md` with decision + date.

## Non-goals

- No changes to the 73 README entries, their ordering, tags, or the flat `## Contents` block.
- No changes to `.github/workflows/link-check-pr.yml` or `link-check-schedule.yml`; the triad stays as is.
- No licence change. The repo stays CC0-1.0; the sibling sysml-v2 MIT pattern is copied only for CITATION.cff shape.
- No multi-page docs site beyond the single RR-B-20 landing page. No marketing redesign beyond a minimal self-contained list landing.
- No hub (awesome-mbse) edits. Everything here is spoke-local.
- No git history rewrite. RR-B-27 already passes: all commits use `245595077+jgsystemsconsulting@users.noreply.github.com`.
- No MCP/skills/research profile work (no RR-M/RR-S/RR-R rows).

## Locked decisions

These are fixed by the dispatch or by this spec as the single recommendation. They are not open for re-litigation in the plan or execution.

| # | Decision |
|---|----------|
| D1 | Profile: RR-B Base only. The list is a curated index, not an MCP bridge, skills pack, or research instrument. |
| D2 | Licence posture: open source, CC0-1.0, unchanged. COPYRIGHT/NOTICE ship per templates; NOTICE states no third-party code is distributed. |
| D3 | Build model: standalone. Fixes commit directly to the spoke; the RR-B-15 gate is `scripts/check_release.py` + `.github/workflows/validate.yml`. |
| D4 | Version: **0.1.0**, dated 2026-09-17. CHANGELOG.md (top entry) is the version source; propagated to RELEASE-INFO.txt, CITATION.cff, tag `v0.1.0`, GitHub Release. |
| D5 | Landing surface: ship **RR-B-20 MUST** as a minimal self-contained `docs/index.html` + `docs/.nojekyll`, enable GitHub Pages from `/docs`, set homepage to the Pages URL. Content: what the list is, how to browse, how to suggest an entry, link to README on GitHub, licence-enquiry URL. No CDN, no third-party fonts, no em dash. RR-B-24: run mechanical taste overlay when available; taste-skill MANUAL recorded. RR-B-30: assessment outcome "one HTML landing + README deep content". |
| D6 | Usage interpretation: for a list product, **Install** heading states there is nothing to install (browse on GitHub or clone). **Usage** covers browse, search Contents, open links, contribute via issue form/PR. RR-B-06 depth is README Install+Usage plus CONTRIBUTING.md; no separate docs/usage.md. |
| D7 | RR-B-29: the whole requirement is deliberate N/A (a list is not installed into an agent host, so no marketplace manifests). Recorded in the ledger with a date. |
| D8 | RR-B-32 improvement form: the existing `suggest-resource.yml` is the list's improvement channel. The audit's filename glob (`improv`/`enhanc`) will show a WARN row; that WARN is accepted and the mapping is named in the README Support section and the ledger. Renaming or duplicating the form is rejected. |
| D9 | SECURITY route: private GitHub security advisory (and PR with fix for non-sensitive issues). No email anywhere in SECURITY.md, so the RR-B-07 row stays PASS rather than WARN. |
| D10 | Platform state in this pass: tag + published GitHub Release v0.1.0 (RR-B-18/22), branch protection on `main` (RR-B-23 solo-maintainer shape), About description + topics, **homepageUrl = Pages URL** after RR-B-20 is live (RR-B-21). |
| D11 | Family pointer stays text-only on the public spoke (FAMILY Private mode). No hub FAMILY.md hyperlink. |

## Requirement mapping (RR-B id to Capella action)

| ID | Requirement | Action for awesome-capella | Audit row after |
|----|-------------|----------------------------|-----------------|
| RR-B-00 | Fix source, not output | N/A (standalone model) | none |
| RR-B-01 | LICENSE | Keep CC0-1.0. If GitHub licensee returns NOASSERTION, strip non-canonical preamble so spdx_id is CC0-1.0 (copyright lives in COPYRIGHT/NOTICE) | PASS (spdx_id CC0-1.0) |
| RR-B-02 | COPYRIGHT + NOTICE | Add both from skill templates `COPYRIGHT.tmpl` / `NOTICE.tmpl` with org **JG Systems Consulting Ltd**, year 2026, product Awesome Capella. NOTICE: no vendored third-party code; linked resources keep their own licences. Body text is the filled template, not invented prose | PASS x2 |
| RR-B-03 | Per-file headers | Audit greps first-party .py (and template .md when present). Add two-line header to `scripts/check_entries.py`; `check_release.py` ships with one. New markdown from templates carry headers where required. Existing long README/CONTRIBUTING are not rewritten for headers unless audit expands to .md | PASS on auditor scope |
| RR-B-04 | SPDX | `SPDX-License-Identifier: CC0-1.0` in the same Python headers | PASS |
| RR-B-05 | README sections | Add real headings **Install**, **Usage**, **Licence** (links LICENSE + `https://labs.jgsystemsconsulting.com/licensing.html`), **Support**, plus Version/changelog line. Install body: nothing to install; browse or clone | PASS |
| RR-B-06 | Install/usage depth | Install + Usage sections (D6) plus CONTRIBUTING.md. No separate docs/usage.md | MANUAL, addressed |
| RR-B-07 | SECURITY route | Rewrite SECURITY.md: private advisory link `https://github.com/jgsystemsconsulting/awesome-capella/security/advisories/new`, PR-with-fix for non-sensitive, response-time **We aim to acknowledge reports within 7 days**, scope notes (malicious/hijacked links, CI), no email, no em dash | PASS |
| RR-B-08/09 | CHANGELOG + version source | Reformat CHANGELOG to Keep a Changelog: `## [0.1.0] - 2026-09-17` top entry holding the existing seed bullets under Added/Notes. RR-B-09 is the version-match PASS row; RR-B-08 is presence of CHANGELOG (auditor may not emit a separate PASS label) | PASS (09) / present (08) |
| RR-B-10 | RELEASE-INFO.txt | Add: Product Awesome Capella, Version 0.1.0, Built: UTC ISO-8601 `YYYY-MM-DDTHH:MM:SSZ` at release-commit time, Tag: v0.1.0 | PASS |
| RR-B-11 | Clean layout | Already clean; new files land in their standard slots | PASS |
| RR-B-12 | Community files (OSS posture) | CONTRIBUTING, CODE_OF_CONDUCT, PR template all exist; PR template already carries guardrail checkboxes. No change | MANUAL, already met |
| RR-B-13 | .gitignore | Add root `.gitignore` (OS cruft, `__pycache__/`, `.venv/`, `.lycheecache`, `.playwright-mcp/`, `*.bak`) | PASS |
| RR-B-14 | No secrets | Nothing to add; leak scan stays clean | PASS |
| RR-B-15 | Automated release gate | Add `scripts/check_release.py` from skill template `templates/scripts/check_release.py` (or tools path as shipped): REQUIRED = `README.md`, `LICENSE`, `COPYRIGHT`, `NOTICE`, `CHANGELOG.md`, `SECURITY.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `RELEASE-INFO.txt`, `CITATION.cff`, `docs/DISTRIBUTION.md`, `docs/index.html`, `scripts/check_entries.py`, `scripts/check_release.py`; header sentinel `Copyright (c) 2026 JG Systems Consulting Ltd`; SCAN_GLOBS = `scripts/*.py` (and any other first-party .py). Gate must print count of files scanned ≥ 1. `.github/workflows/validate.yml` from template: `permissions: contents: read` (or read-all), `actions/checkout@v4` allowed for reading the tree only (no executing unchecked remote code beyond the gate script), step names plain English (`Checkout`, `Run release gate`), triggers push+pull_request to main, runs `python scripts/check_release.py`. Separate file; family triad untouched | PASS |
| RR-B-16 | Agent-install prompt | Skipped: SHOULD, and a list has no install step to automate | not checked |
| RR-B-17 | llms.txt / AGENTS.md | Skipped: MAY | not checked |
| RR-B-18 | Tagged release | Create and push tag `v0.1.0` on the release commit | PASS |
| RR-B-19 | Catalogue entry | No org catalogue entry exists; ledger row `planned` with date | MANUAL via ledger |
| RR-B-20 | Landing page | Ship `docs/index.html` + `docs/.nojekyll`; enable Pages from /docs (D5). Self-contained; licence-enquiry link; first-run = open the list | PASS with --gh |
| RR-B-21 | About metadata | Description exactly: `Curated Capella tool and Arcadia method resources for MBSE practitioners`. Topics: `capella`, `arcadia`, `mbse`, `awesome-list`, `model-based-systems-engineering` (keep existing `awesome` if present). homepageUrl = Pages URL after enablement | PASS with --gh |
| RR-B-22 | GitHub Release | Publish Release v0.1.0 from CHANGELOG notes. Footer line exactly: `Licence enquiries: https://labs.jgsystemsconsulting.com/licensing.html` | PASS with --gh |
| RR-B-23 | Branch protection | Protect `main`: required PR + the validate check, force-push and deletion off, `enforce_admins` off and 0 required approvals (solo maintainer) | PASS with --gh |
| RR-B-24 | Landing quality | Mechanical taste overlay on docs/*.html when tool available; MANUAL taste-skill note in PR. Design-system precedence | PASS or named MANUAL residual |
| RR-B-25 | Link integrity | Family triad (lychee anchor-only) already covers README anchors and links; run `audit.py --links` once after README edits and record the pass | PASS |
| RR-B-26 | Doc presentation | No ASCII diagrams in the README; no Mermaid needed for a list. Callout/table usage already fine | MANUAL, met |
| RR-B-27 | Commit identity | Already canonical (noreply identity on every commit). No action | PASS |
| RR-B-28 | De-slopped prose | New/edited prose (README sections, SECURITY.md, CHANGELOG entry, ledger) written clean; run the de-slop pass over README/docs/CHANGELOG; SECURITY.md em dash removed; grep shows zero em dashes on the customer surface | PASS |
| RR-B-29 | Marketplace manifests | Deliberate N/A with reason + date in ledger (D7) | none on plain run |
| RR-B-30 | Multi-page assessment | Recorded: content walked, outcome **one HTML landing + README deep content** (D5); nothing justifies a third page | MANUAL, recorded |
| RR-B-31 | CITATION.cff | Add CFF 1.2.0: title Awesome Capella, version "0.1.0", date-released 2026-09-17, authors entity JG Systems Consulting Ltd, repository-code the repo URL, license CC0-1.0 (sysml-v2 shape plus version/date) | PASS |
| RR-B-32 | Bug-report channel | Add `bug_report.yml` (list-adapted: affected entry URL, problem type, list version, required hygiene checkbox) and `config.yml` with `blank_issues_enabled: false` and contact_links: (1) title `Security advisory`, url `https://github.com/jgsystemsconsulting/awesome-capella/security/advisories/new`; (2) title `awesome-sysml-v2 issues`, url `https://github.com/jgsystemsconsulting/awesome-sysml-v2/issues`. Keep suggest-resource.yml as the improvement channel (D8). README Support names every channel | PASS + accepted WARN |
| RR-B-33 | No BOM | Write new YAML/CFF as plain UTF-8, verify first bytes; audit covers it | PASS |
| RR-B-34 | No local paths | New files carry no machine-local paths; audit verifies | PASS |
| RR-B-35 | Keep/drop inventory | Walk `git ls-files`: no maintainer-only prefixes tracked (no .planning/, docs/specs/, GATES.md). Record "no candidates" in the PR | PASS |
| RR-B-36 | Distribution ledger | Add `docs/DISTRIBUTION.md`: GitHub repo (live), GitHub Releases v0.1.0 (submitted), Pages landing (live), About/topics+homepage (applied), org catalogue (planned), sindresorhus/awesome (deferred, acceptability gate), in-host marketplaces (deliberate N/A), MCP directories (deliberate N/A), community MBSE directories (deferred). Header: last reviewed 0.1.0, 2026-09-17 | PASS |

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
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`

Modified files:

- `README.md` (Install, Usage, Licence, Support, Version sections; entries and Contents untouched)
- `SECURITY.md` (advisory route, no email, no em dash)
- `CHANGELOG.md` (Keep a Changelog shape, `[0.1.0]` top entry)
- `scripts/check_entries.py` (copyright + SPDX header lines only)

Platform actions (recorded in the PR, not files), **order fixed**:

1. Merge release commit to `main` (final SHA).
2. Enable GitHub Pages from `/docs`; verify the site serves (HTTP 200 on the Pages URL).
3. Set About description + topics; set **homepageUrl only after** Pages serves.
4. Tag `v0.1.0` on **that main HEAD** SHA; publish GitHub Release v0.1.0 from CHANGELOG + licence-enquiry footer.
5. Branch protection on `main` (first-time PUT): required status check name exactly `validate` (or the job name emitted by validate.yml), force-push off, deletion off, `enforce_admins` false, required approving reviews 0 (solo maintainer residual: direct pushes can bypass; named in PR).

## Acceptance criteria

1. `python tools/audit.py --repo ../awesome-capella --profile base` exits 0: zero FAIL rows. Expected non-blocking: `RR-B-32` WARN (improvement-form filename glob) if still present. RR-B-20 is proven only under AC3 (`--gh`), not by absence of a plain-run FAIL row.
2. `python scripts/check_release.py` in the spoke root exits 0.
3. With `--gh --links`: RR-B-20 PASS (Pages serves docs/), RR-B-21 PASS (homepage set), RR-B-22 PASS (Release notes contain `https://labs.jgsystemsconsulting.com/licensing.html`), RR-B-23 PASS (validate check required), RR-B-25 PASS.
4. `python scripts/check_entries.py` exits 0; README still has exactly 73 entry bullets.
5. Family triad green after README/SECURITY edits (`link-check-pr.yml` workflow_dispatch on main).
6. MANUAL items closed in the PR: RR-B-06 (D6), RR-B-12 (present), RR-B-19/29 (ledger), RR-B-24 (taste note), RR-B-26, RR-B-28 (de-slop recorded), RR-B-30 (one HTML + README), RR-B-35, RR-B-36 (ledger at 0.1.0).
7. No em dash in README.md, SECURITY.md, CHANGELOG.md, docs/DISTRIBUTION.md, docs/index.html body copy.
8. Workflow file push succeeds (`gh auth refresh -s workflow` if needed).
9. `gh api repos/jgsystemsconsulting/awesome-capella/license --jq .license.spdx_id` returns a CC0-compatible id (not NOASSERTION).

## Risks

- **RR-B-20 is MUST.** Deferring Pages leaves a standard residual even if plain audit.py stays quiet; this pass ships the landing page. Pages enablement needs admin on the repo.

- **README edits can trip awesome-lint.** The badge line and flat `## Contents` stay byte-identical; new sections are appended below. Entry-format rules are unaffected because no entry line changes. The triad run (criterion 5) is the guard.
- **Adding version artifacts creates a new RR-B-18 FAIL until the tag exists.** The tag is part of the same change set, created on the release commit before the audit claim. Do not split the version files from the tag across PRs.
- **`check_release.py` template defaults assume an src/ layout and unsubstituted placeholders.** The REQUIRED list, SCAN_GLOBS, and the header sentinel must be edited for this tree, or the gate false-fails (sentinel never matches) or false-passes (globs match nothing). Both directions are covered by criteria 1 and 2.
- **SECURITY.md wording is load-bearing.** The audit row requires the word `advisories` or `pull request`; any email in the file downgrades to WARN. The rewrite keeps the advisory link and drops the email.
- **Windows BOM risk on hand-written YAML/CFF.** RR-B-33 fails on a BOM'd `.cff` or `.yml`. Verify first bytes after writing; the audit also checks.
- **Branch protection PUT can fail on permissions.** If the `gh api` PUT fails, record RR-B-23 as the named maintainer action with the exact command in the PR; do not mark it done.

## Research

- https://github.com/jgsystemsconsulting/awesome-capella
- https://github.com/jgsystemsconsulting/awesome-sysml-v2
- file://C:/Users/gower/.zcode/skills/release-repo-standard/references/release-repo-standard.md (v1.14, normative)
- file://C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py (auditor; 2026-09-17 run: 14 FAIL, 2 WARN, 8 PASS)
- file://C:/Users/gower/.zcode/skills/release-repo-standard/templates/ (COPYRIGHT, NOTICE, RELEASE-INFO.txt, CITATION.cff, SECURITY.md, check_release.py, validate.yml, ISSUE_TEMPLATE)
- file://C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse/docs/superpowers/research/2026-09-17-repo-release-standard-capella-research.md
- file://C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse/docs/superpowers/context/2026-09-17-repo-release-standard-capella-context.md

## Codebase context

The spoke ships: README (73 entries across nine sections, flat hand-maintained Contents), CC0-1.0 LICENSE, CONTRIBUTING (entry format, tag vocabulary, canonical-URL rule), CODE_OF_CONDUCT, SECURITY.md, CHANGELOG (date-headed, not semver), `scripts/check_entries.py` (entry format gate), two link-check workflows (lychee anchor-only on PR and schedule, plus awesome-lint and markdownlint), one issue form (`suggest-resource.yml`), a PR template with guardrail checkboxes, `.markdownlint-cli2.jsonc`, and an empty `.lycheeignore`. Missing relative to the standard: everything in the File inventory above.

Family constraints that bind this pass: the CI triad is green and must stay untouched; the public spoke uses a text-only family pointer (FAMILY Private mode, no hub FAMILY.md URL); workspace baseline porcelain sha256 `0933b130d260f82993853e7b62552af5ff0dccda8cd3a8192496cf60092999d2`. The sibling spoke `awesome-sysml-v2` already ships a CITATION.cff (entity JG Systems Consulting Ltd, 2026) and is the shape reference; its MIT licence is not copied.
