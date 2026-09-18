# Spec: Release Repo Standard for jgsystemsconsulting/awesome-stpa

**Date:** 2026-09-17
**Target repo:** `C:\Users\gower\OneDrive\Documents\GitHub\awesome-stpa` (private spoke, https://github.com/jgsystemsconsulting/awesome-stpa)
**Standard:** Release Repo Standard v1.14, profile **RR-B Base only**, **open-source posture (CC0-1.0)**, **standalone build model**
**Auditor:** `tools/audit.py` from the `release-repo-standard` skill, run with `--profile base`
**Second phase:** family Checklist A public release per `docs/runbooks/family-public-release.md`

## Problem

The 2026-09-17 audit run of `tools/audit.py --repo .../awesome-stpa --profile base` reported **11 FAIL, 2 WARN, 11 PASS** (saved at `docs/superpowers/research/2026-09-17-repo-release-standard-stpa-audit-baseline.txt`). The spoke is a live curated list (43 verified entries, seven sections, family CI triad green), but under RR-B it is not release-ready: missing COPYRIGHT, release identity (semver, RELEASE-INFO.txt, CITATION.cff, tag), release gate CI, README Install/Usage/Licence/Support sections, SECURITY private-advisory route (today it publishes an email address), one SECURITY em dash, CITATION.cff, both required issue forms, the distribution ledger, and the RR-B-20 Pages landing page. Two defects are stpa-specific: GitHub licensee returns `NOASSERTION` for the Capella-shaped LICENSE (org first line kept so RR-B-01 still PASSes), and RR-B-34 false-positives on **11** public MIT PSAS `/home/<segment>/` URL hits.

This spec closes the machine-checkable gaps plus the RR-B-20 MUST with the smallest spoke-local set, then runs Checklist A to flip the spoke public and update the hub registry. **Audit exit 0 gates the visibility flip; it is not sufficient by itself** until the named MANUAL items and the platform steps are done. The hub stays private, so the spoke's family pointer stays text-only (class hub-private).

## Goals

1. `python tools/audit.py --repo ../awesome-stpa --profile base` exits 0 (zero FAIL rows). With `--gh --links`, RR-B-20/21/22/23/25 are PASS.
2. Release identity end to end: version **0.1.0** across CHANGELOG, RELEASE-INFO.txt, CITATION.cff, tag `v0.1.0`, published GitHub Release with the licence-enquiry URL.
3. Automated release gate: `scripts/check_release.py` plus `.github/workflows/validate.yml`, additive to the family triad.
4. SECURITY.md: private advisory route, no email, no em dash.
5. `docs/index.html` + `docs/.nojekyll` ship; GitHub Pages serves `https://jgsystemsconsulting.github.io/awesome-stpa/`; homepage set to that URL.
6. `docs/DISTRIBUTION.md` records every distribution channel with a decision and date.
7. Checklist A executed by hand: decision issue, visibility flip to public, anonymous access verified, hub FAMILY.md Visibility cell and hub README family table updated, spoke CHANGELOG note, issue closed.

## Non-goals

- No changes to the 43 entry bullets or the `## Contents` block, except the one Related-lists hub bullet specified in D12 (link removal only; its text stays).
- No changes to `.github/workflows/link-check-pr.yml`, `link-check-schedule.yml`, or `lint.yml`; the triad stays byte-identical. `validate.yml` is the only new workflow.
- No licence change. CC0-1.0 stands; LICENSE keeps the org first line required by RR-B-01.
- No multi-page docs site. One RR-B-20 landing page, nothing more.
- No hub (awesome-mbse) edits beyond the two Checklist A registry updates (FAMILY.md cell, README family table row). No hub FAMILY.md hyperlink from the spoke while the hub is private.
- No git history rewrite. RR-B-27 already passes on the noreply identity.
- No MCP/skills/research profile work (no RR-M/RR-S/RR-R rows).
- No sindresorhus/awesome submission (Checklist C is post-hub-public, out of scope).

## Locked decisions

Fixed by the dispatch or by this spec as the single recommendation. Not open for re-litigation in the plan or execution.

| # | Decision |
|---|----------|
| D1 | Profile: RR-B Base only. The list is a curated index, not an MCP bridge, skills pack, or research instrument. |
| D2 | Licence posture: open source, CC0-1.0, unchanged. Add COPYRIGHT from the skill template (org **JG Systems Consulting Ltd**, year 2026, product Awesome STPA). NOTICE already exists and passes; keep it. LICENSE keeps the Capella-shaped org first line so audit RR-B-01 continues to find the org string (verified PASS today). GitHub licensee already returns `NOASSERTION` for that shape (verified 2026-09-17); do not strip the org line to chase spdx_id if that would fail RR-B-01. Optional pure-CC0 experiment only if a dual-file approach is proven not to break the auditor. |
| D3 | Build model: standalone. Commits go directly to the spoke; the RR-B-15 gate is `scripts/check_release.py` + `.github/workflows/validate.yml`. The spoke has no `scripts/` directory and no checker today, so the gate REQUIRED list omits `check_entries.py` (Capella had one). |
| D4 | Version: **0.1.0**, dated 2026-09-17. CHANGELOG.md reformatted to Keep a Changelog with `## [0.1.0] - 2026-09-17` as the top entry holding the existing seed bullets; that entry is the version source for RELEASE-INFO.txt, CITATION.cff, tag `v0.1.0`, and the GitHub Release. The post-flip Checklist A CHANGELOG note is a bullet added to the same `[0.1.0]` entry after the tag; the tag pins the release commit and does not move. |
| D5 | Landing surface: minimal self-contained `docs/index.html` + `docs/.nojekyll`, Pages enabled from `/docs`, homepage set to `https://jgsystemsconsulting.github.io/awesome-stpa/` only after the site serves. Content: what the list is, how to browse, how to suggest an entry, link to the README on GitHub, licence-enquiry URL. Inline CSS only: include `:focus-visible` and `prefers-reduced-motion` rules; no CDN, no third-party fonts, no 100vh hero, no em dash, no AI-purple hex. RR-B-24 mechanical overlay when available; MANUAL taste note otherwise. RR-B-30: one HTML landing + README deep content. |
| D6 | Usage interpretation: **Install** states there is nothing to install (browse on GitHub or clone). **Usage** covers browse, search the Contents, open links, contribute via the suggest-resource form or PR. RR-B-06 depth is README Install+Usage plus the existing CONTRIBUTING.md; no separate docs/usage.md. |
| D7 | RR-B-29: deliberate N/A (a list is not installed into an agent host, so no marketplace manifests). Ledger row with reason and date. RR-B-19 org catalogue: ledger row `planned` with date. |
| D8 | Issue forms: the spoke has none today, so this pass creates all three. `suggest-resource.yml` is the improvement channel (resource URL, target section, inclusion-bar rationale); `bug_report.yml` is list-adapted (affected entry URL, problem type, list version, hygiene checkbox); `config.yml` sets `blank_issues_enabled: false` with one contact link, `Security advisory` pointing at `https://github.com/jgsystemsconsulting/awesome-stpa/security/advisories/new`. The auditor's improvement-form filename glob (`improv`/`enhanc`) will still WARN on `suggest-resource.yml`; that WARN is accepted and named in README Support and the ledger, same as Capella D8. No contact link to the private hub. |
| D9 | SECURITY route: private GitHub security advisory, plus PR-with-fix for non-sensitive issues. No email anywhere in SECURITY.md (the current `support@jgsystemsconsulting.com` line is removed), so RR-B-07 stays PASS rather than WARN. Response-time line: We aim to acknowledge reports within 7 days. Scope: malicious or hijacked linked resources, and the repo's own CI. |
| D10 | Platform state in this pass: About description exactly `Curated STAMP/STPA and hazard analysis resources for safety and systems engineering practitioners`; topics unchanged at the existing six (`stpa`, `stamp`, `safety`, `hazard-analysis`, `awesome-list`, `awesome`; the six-topic floor is already met, so `mbse` is not added); tag `v0.1.0` on the release commit; published GitHub Release v0.1.0 with footer line exactly `Licence enquiries: https://labs.jgsystemsconsulting.com/licensing.html`; homepageUrl = the Pages URL; branch protection on `main` with the `validate` check required, `enforce_admins` off, 0 required approvals (solo maintainer). |
| D11 | Family pointer stays the exact text-only preferred line on line 9 of the README (class hub-private). No edit needed; no hub FAMILY.md hyperlink. |
| D12 | Related-lists hub bullet: the README links the private hub at `awesome-mbse` inside `## Related lists`, which fails Checklist A's no-private-only-entries bar for anonymous readers. Convert that single bullet to a text-only line (same text, link removed, note that the link returns at hub-public). All 43 bullets stay. Verified safe for awesome-lint v2.3.0: the list-item rule skips any item whose first paragraph child is plain text. The bullet converts back to a hyperlink in the Checklist B pointer-unlock sweep after the hub goes public. The sibling bullet for awesome-sysml-v2 and the sindresorhus/awesome bullet stay as links (both public). |
| D13 | RR-B-34 false positive: auditor regex `/home/<token>/` matches **11** README hits (unique path prefixes on 2026-09-17): `/home/books-and-handbooks/`, `/home/materials/`, `/home/publications/`, `/home/stamp-tools/`, `/home/stamp-workshop-information/`, `/home/mit-stamp-workshop-presentations/`, `/home/mit-stamp-workshop-tutorials/`, `/home/online-education/`, `/home/wp-content/` (plus any remaining `/home/<seg>/` the same regex finds). These are public MIT PSAS web paths, not machine-local homes. **Must** percent-encode at least one character in the segment after `/home/` for **every** matching URL (e.g. first hyphen as `%2D`, or `wp-content` as `wp%2Dcontent`) so the regex no longer matches, links still resolve (RFC 3986), and `audit.py` exits 0 with zero FAIL. Document encodings in DISTRIBUTION.md. Do not claim the auditor can exempt a FAIL while exiting 0 (it cannot). Do not drop PSAS links. Do not edit the shared auditor. |

## Requirement mapping (RR-B id to stpa action)

| ID | Requirement | Action for awesome-stpa | Audit row after |
|----|-------------|-------------------------|-----------------|
| RR-B-00 | Fix source, not output | N/A (standalone model) | none |
| RR-B-01 | LICENSE | Keep Capella-shaped LICENSE (org first line + CC0 body) so audit finds the org string. COPYRIGHT/NOTICE carry copyright detail. GitHub `license.spdx_id` may remain NOASSERTION; that is not the RR-B-01 audit row | PASS (org present) |
| RR-B-02 | COPYRIGHT + NOTICE | Add COPYRIGHT from skill template; NOTICE already passes, no change | PASS x2 |
| RR-B-03 | Per-file headers | Zero first-party .py today (baseline PASS vacuous). `check_release.py` ships with the two-line header | PASS on auditor scope |
| RR-B-04 | SPDX | `SPDX-License-Identifier: CC0-1.0` in the same header | PASS |
| RR-B-05 | README sections | Add headings **Install**, **Usage**, **Licence** (links LICENSE + `https://labs.jgsystemsconsulting.com/licensing.html`), **Support**, plus a Version/changelog line. Install body: nothing to install; browse or clone. Appended below existing content; badge line and Contents untouched | PASS |
| RR-B-06 | Install/usage depth | Install + Usage (D6) plus existing CONTRIBUTING.md. No docs/usage.md | MANUAL, addressed |
| RR-B-07 | SECURITY route | Rewrite SECURITY.md per D9: advisory link `https://github.com/jgsystemsconsulting/awesome-stpa/security/advisories/new`, PR-with-fix for non-sensitive, 7-day acknowledgement, scope, no email, no em dash | PASS |
| RR-B-08/09 | CHANGELOG + version source | Reformat to Keep a Changelog: `## [0.1.0] - 2026-09-17` top entry holding the existing seed bullets under Added/Notes. Sweep-history bullets stay in the entry | PASS (09) / present (08) |
| RR-B-10 | RELEASE-INFO.txt | Add: Product Awesome STPA, Version 0.1.0, Built: UTC ISO-8601 `YYYY-MM-DDTHH:MM:SSZ` at release-commit time, Tag: v0.1.0 | PASS |
| RR-B-11 | Clean layout | Already clean (baseline PASS); new files land in standard slots | PASS |
| RR-B-12 | Community files (OSS posture) | CONTRIBUTING, CODE_OF_CONDUCT, PR template all exist. No change | MANUAL, already met |
| RR-B-13 | .gitignore | Already exists (baseline PASS). Extend only if new tooling needs an entry | PASS |
| RR-B-14 | No secrets | Nothing to add; leak scan stays clean | PASS |
| RR-B-15 | Automated release gate | Add `scripts/check_release.py` REQUIRED list as Capella (minus check_entries): README, LICENSE, COPYRIGHT, NOTICE, CHANGELOG, SECURITY, CONTRIBUTING, CODE_OF_CONDUCT, RELEASE-INFO.txt, CITATION.cff, docs/DISTRIBUTION.md, docs/index.html, scripts/check_release.py; header sentinel `Copyright (c) 2026 JG Systems Consulting Ltd`; SCAN_GLOBS = `scripts/*.py`; collect paths, assert non-empty, print `scanned N` with N>=1. Workflow `.github/workflows/validate.yml` **inline full YAML** (do not paste stock template with pip/pytest): `name: validate`, job id `validate`, `permissions: contents: read`, triggers push+pull_request to main, steps only Checkout (`actions/checkout@v4`), Setup Python 3.x, Run `python scripts/check_release.py`. No pip install, no pytest. Check name for branch protection is `validate`. Triad untouched | PASS |
| RR-B-16 | Agent-install prompt | Skipped: SHOULD, and a list has no install step | not checked |
| RR-B-17 | llms.txt / AGENTS.md | Skipped: MAY | not checked |
| RR-B-18 | Tagged release | Create and push tag `v0.1.0` on the release commit | PASS |
| RR-B-19 | Catalogue entry | No org catalogue entry; ledger row `planned` with date | MANUAL via ledger |
| RR-B-20 | Landing page | Ship `docs/index.html` + `docs/.nojekyll`; enable Pages from /docs (D5). Self-contained; licence-enquiry link; first-run = open the list | PASS with --gh |
| RR-B-21 | About metadata | Description exactly the D10 string. Topics: keep the six, no additions. homepageUrl = Pages URL after enablement | PASS with --gh |
| RR-B-22 | GitHub Release | Publish Release v0.1.0 from CHANGELOG notes. Footer line exactly `Licence enquiries: https://labs.jgsystemsconsulting.com/licensing.html` | PASS with --gh |
| RR-B-23 | Branch protection | Protect `main`: required `validate` check, force-push and deletion off, `enforce_admins` off, 0 required approvals (solo maintainer) | PASS with --gh |
| RR-B-24 | Landing quality | Mechanical taste overlay when available; MANUAL taste-skill note in PR otherwise. Design-system precedence | PASS or named MANUAL residual |
| RR-B-25 | Link integrity | Family triad lychee jobs already cover README links and anchors; run `audit.py --links` once after README edits and record the pass; curl-verify a sample of encoded PSAS URLs return 200 | PASS |
| RR-B-26 | Doc presentation | No ASCII diagrams; no Mermaid needed for a list. Existing presentation fine | MANUAL, met |
| RR-B-27 | Commit identity | Already canonical (noreply identity on every commit). No action | PASS |
| RR-B-28 | De-slopped prose | New/edited prose written clean; de-slop pass over README/SECURITY/CHANGELOG/docs; remove the **one** em dash in SECURITY.md (line 3, "links — it ships"); grep shows zero em dashes on the customer surface | PASS |
| RR-B-29 | Marketplace manifests | Deliberate N/A with reason + date in ledger (D7) | none on plain run |
| RR-B-30 | Multi-page assessment | Recorded: content walked, outcome one HTML landing + README deep content (D5) | MANUAL, recorded |
| RR-B-31 | CITATION.cff | Add CFF 1.2.0: title Awesome STPA, version "0.1.0", date-released 2026-09-17, authors entity JG Systems Consulting Ltd, repository-code the repo URL, license CC0-1.0 | PASS |
| RR-B-32 | Bug-report channel | Create `bug_report.yml`, `config.yml`, `suggest-resource.yml` per D8. README Support names every channel (advisory, suggest-resource, bug report) | PASS + accepted WARN |
| RR-B-33 | No BOM | Write new YAML/CFF as plain UTF-8; verify first bytes; audit covers it | PASS |
| RR-B-34 | No local paths | D13: percent-encode every matching `/home/<seg>/` PSAS URL until audit RR-B-34 PASS and exit 0 | PASS |
| RR-B-35 | Keep/drop inventory | Walk `git ls-files`: no maintainer-only prefixes tracked (baseline PASS). Record "no candidates" in the PR | PASS |
| RR-B-36 | Distribution ledger | Add `docs/DISTRIBUTION.md`: GitHub repo (live), GitHub Releases v0.1.0 (submitted), Pages landing (live), About/topics+homepage (applied), org catalogue (planned), sindresorhus/awesome (deferred to Checklist C, after hub public), in-host marketplaces (deliberate N/A), MCP directories (deliberate N/A), community safety/MBSE directories (deferred), PSAS URL encoding note (D13). Header: last reviewed 0.1.0, 2026-09-17 | PASS |

## File inventory

New files (all in the spoke):

- `COPYRIGHT`
- `RELEASE-INFO.txt`
- `CITATION.cff`
- `docs/DISTRIBUTION.md`
- `docs/index.html`
- `docs/.nojekyll`
- `scripts/check_release.py`
- `.github/workflows/validate.yml`
- `.github/ISSUE_TEMPLATE/suggest-resource.yml`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`

Modified files:

- `README.md` (Install, Usage, Licence, Support, Version sections; the one D12 Related-lists bullet to text-only; entries and Contents untouched)
- `SECURITY.md` (advisory route, no email, no em dash)
- `CHANGELOG.md` (Keep a Changelog shape, `[0.1.0]` top entry)
- LICENSE: verify-only (org line present); no required edit unless em-dash policy on LICENSE first line is applied without dropping org

`NOTICE` and `.gitignore` already exist and pass; no change expected.

## Platform actions (recorded in the PR, not files), order fixed

1. Merge the release commit to `main` (final SHA for RR-B packaging).
2. Enable GitHub Pages from `/docs`; verify HTTP 200 on `https://jgsystemsconsulting.github.io/awesome-stpa/`.
3. Set the About description (D10 string) and topics; set homepageUrl only after Pages serves.
4. Tag `v0.1.0` on the release SHA; publish GitHub Release v0.1.0 from the CHANGELOG entry plus the licence-enquiry footer line.
5. Branch protection on `main` (first-time PUT): required status check exactly the job name emitted by `validate.yml`, force-push off, deletion off, `enforce_admins` false, required approving reviews 0. Solo-maintainer residual (direct pushes can bypass) named in the PR.

## Family Checklist A (runs after RR-B audit exit 0)

From `docs/runbooks/family-public-release.md`, applied to this spoke, in order:

1. Pre-flip gates: CI green on default branch (`gh run list --limit 5` in the spoke checkout); every entry link publicly resolvable (D12 closes the one private link); README already matches the family skeleton (Awesome badge, sweep badge, one-line scope, Contents); pointer class hub-private (D11, already correct); `git grep -nIE "C:\\Users|/Users/|OneDrive"` and `git grep -nwIE "TODO|WIP"` return nothing on tracked files; `git status --porcelain` clean.
2. File the decision issue in the spoke: title `Public release decision 2026-09-17`, body per the runbook template (Decision public, date, maker, reason).
3. By hand: `gh repo edit jgsystemsconsulting/awesome-stpa --visibility public --accept-visibility-change-consequences`. If gh rejects the flag name, check `gh repo edit --help` for the current flag before running anything.
4. Verify anonymous access: `curl` on the repo URL and on the Pages URL returns 200 logged out.
5. Hub edits: FAMILY.md registry row for awesome-stpa Visibility `private` to `public`; hub README family table row gains the spoke URL (was name-only with a location note). Status stays `Live`. Hub stays private.
6. Add the CHANGELOG bullet to the spoke's `[0.1.0]` entry recording the release date; close the decision issue with `Released 2026-09-17.`

## Acceptance criteria

1. `python tools/audit.py --repo ../awesome-stpa --profile base` exits 0: zero FAIL rows. Expected non-blocking: the RR-B-32 improvement-form WARN. RR-B-20 is proven only under AC3, not by absence of a plain-run FAIL.
2. `python scripts/check_release.py` in the spoke root exits 0 and prints a scanned-file count >= 1.
3. With `--gh --links`: RR-B-20 PASS (Pages serves), RR-B-21 PASS (homepage set, topics>=6), RR-B-22 PASS (Release notes contain licence-enquiry URL), RR-B-23 PASS, RR-B-25 PASS. **Additionally** (not inferred from RR-B-21 alone): `gh repo view --json description,repositoryTopics` shows description exactly the D10 string and topic names exactly the six D10 tags.
4. Entry integrity: Contents block byte-identical. Exactly **43** list items remain under the seven content sections (D12 hub row stays a list item, text-only). Allowed entry-adjacent diffs: D12 link removal and D13 percent-encoding of PSAS `/home/<seg>/` hrefs only. `npx -y awesome-lint` and markdownlint green.
5. `audit.py` RR-B-01 PASS with org string present in LICENSE. GitHub `license.spdx_id` may remain NOASSERTION for Capella-shaped CC0 files; that is not a stop if RR-B-01 PASSes.
6. No em dash in README.md, SECURITY.md, CHANGELOG.md, docs/DISTRIBUTION.md, docs/index.html body copy. LICENSE may keep the Capella-shaped first-line em dash if Capella pattern is retained (prefer removing it only if org string still remains elsewhere in LICENSE or the auditor only scans for org not dash). Prefer zero customer-facing em dashes outside LICENSE legal text.
7. D13: every former RR-B-34 hit is encoded; RR-B-34 audit row is PASS; plain `audit.py --profile base` exits 0 with zero FAIL.
8. Checklist A: repo is public; anonymous curl 200 on repo and Pages URLs; hub FAMILY.md Visibility is `public`; hub README already links or continues to link the spoke (verify, do not invent a second URL cell); spoke family pointer remains hub-private text-only preferred line; spoke CHANGELOG carries the release note; decision issue closed.
9. Family triad green after the README/SECURITY edits: `lint.yml` on push, `link-check-pr.yml` via workflow_dispatch on main, scheduled sweep unaffected.
10. MANUAL items closed in the PR: RR-B-06 (D6), RR-B-12 (present), RR-B-19/29 (ledger), RR-B-24 (taste note), RR-B-26, RR-B-28 (de-slop recorded), RR-B-30 (one landing + README), RR-B-35, RR-B-36 (ledger at 0.1.0).
11. Workflow file push succeeds (`gh auth refresh -s workflow` if needed).

## Risks

- **RR-B-20 is MUST.** Deferring Pages leaves a standard residual even when the plain audit is quiet; this pass ships the landing page. Pages enablement needs admin on the repo.
- **The visibility flip is irreversible reputationally, not technically.** Once public, assume crawlers have the content. That is why Checklist A runs only after audit exit 0, CI green, and the D12 private-link fix, in that order.
- **README edits can trip awesome-lint.** The badge line and flat Contents stay byte-identical; new sections append below. The D12 text-only bullet is verified safe against the lint rule source (text-first items are skipped), and AC4 re-proves it in CI. If a future awesome-lint bump starts flagging text-only items, the fallback is pinning the lint version, not restoring the private link.
- **Version artifacts create a transient RR-B-18 FAIL until the tag exists.** Version files and the tag land in one change set on the release commit. Do not split them across PRs.
- **`check_release.py` template defaults assume an src/ layout and unsubstituted placeholders.** REQUIRED, SCAN_GLOBS, and the sentinel must be edited for this tree, or the gate false-fails (sentinel never matches) or false-passes (globs match nothing). Criteria 1 and 2 cover both directions.
- **SECURITY.md wording is load-bearing.** The row needs the word `advisories` or `pull request`; any email in the file downgrades to WARN. The rewrite keeps the advisory link and drops the address.
- **The D13 encoding must not be "fixed" later.** A well-meant cleanup restoring the plain URLs reinstates the FAIL. The ledger row and PR note name it explicitly; the fallback path exists if a target ever rejects the encoded form.
- **Windows BOM risk on hand-written YAML/CFF.** RR-B-33 fails on a BOM'd `.cff` or `.yml`. Verify first bytes after writing; the audit re-checks.
- **Branch protection PUT can fail on permissions.** If the `gh api` PUT fails, record RR-B-23 as a named maintainer action with the exact command in the PR; do not mark it done.
- **Post-tag CHANGELOG edit (Checklist A note).** The `[0.1.0]` entry gains a bullet after the tag exists. The tag pins the release commit; the note is a normal follow-up commit on main, not a re-tag.

## Research

- research: docs/superpowers/research/2026-09-17-repo-release-standard-stpa-research.md
- context: docs/superpowers/context/2026-09-17-repo-release-standard-stpa-context.md
- audit baseline capture: docs/superpowers/research/2026-09-17-repo-release-standard-stpa-audit-baseline.txt (11 FAIL, 2 WARN, 11 PASS)
- https://github.com/jgsystemsconsulting/awesome-stpa
- https://github.com/jgsystemsconsulting/awesome-capella
- https://github.com/sindresorhus/awesome
- https://jgsystemsconsulting.github.io/awesome-stpa/ (target Pages URL, not yet live at spec time)
- Topics verified 2026-09-17 via `gh repo view`: awesome, awesome-list, hazard-analysis, safety, stamp, stpa
- file://C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse/docs/superpowers/research/2026-09-17-repo-release-standard-stpa-research.md (research gate)
- file://C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse/docs/superpowers/context/2026-09-17-repo-release-standard-stpa-context.md (context gate)
- file://C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse/docs/superpowers/specs/2026-09-17-repo-release-standard-capella.md (Capella pattern, D1-D11 source)
- file://C:/Users/gower/OneDrive/Documents/GitHub/awesome-mbse/docs/runbooks/family-public-release.md (Checklist A, normative)
- file://C:/Users/gower/.zcode/skills/release-repo-standard/references/release-repo-standard.md (v1.14, normative)
- file://C:/Users/gower/.zcode/skills/release-repo-standard/tools/audit.py (auditor; 2026-09-17 run on awesome-stpa: 11 FAIL, 2 WARN, 11 PASS)
- file://C:/Users/gower/.zcode/skills/release-repo-standard/templates/ (COPYRIGHT, RELEASE-INFO.txt, CITATION.cff, SECURITY.md, check_release.py, validate.yml, ISSUE_TEMPLATE)
- file://C:/Users/gower/AppData/Local/npm-cache/_npx/*/node_modules/awesome-lint/rules/list-item.js (D12 lint-skip verification, v2.3.0)

## Codebase context

The spoke ships: README (43 entries across seven sections, flat hand-maintained Contents, Awesome badge, sweep badge, the preferred text-only family pointer line), CC0-1.0 LICENSE with Capella-shaped org first line (GitHub spdx_id NOASSERTION), NOTICE (nominative-use note for STPA/STAMP/CAST), CONTRIBUTING (entry format, tag vocabulary, canonical-URL rule, PSAS query strings documented as semantically required), CODE_OF_CONDUCT, SECURITY.md (email route, **one** em dash), a date-headed CHANGELOG, `.gitignore`, `.lycheeignore`, `.markdownlint-cli2.jsonc`, a PR template with guardrail checkboxes, and three workflows (`link-check-pr.yml`, `link-check-schedule.yml`, `lint.yml` with awesome-lint plus markdownlint, action refs pinned to commit SHAs). It has no `scripts/` directory, no issue templates, and no `docs/`. The Related lists section carries the one private hub link (D12). Topics (gh 2026-09-17): awesome, awesome-list, hazard-analysis, safety, stamp, stpa.

Family constraints that bind this pass: the CI triad is green and must stay untouched; the hub `awesome-mbse` is private and lists awesome-stpa as Live/private in FAMILY.md; the spoke keeps the text-only pointer class until the hub goes public. The sibling `awesome-capella` completed the same RR-B pass on 2026-09-17 and is the shape reference for COPYRIGHT, CITATION.cff, the gate script, and the landing page; its spec at `docs/superpowers/specs/2026-09-17-repo-release-standard-capella.md` locked D1-D11, adapted here with stpa-specific D12 and D13.
