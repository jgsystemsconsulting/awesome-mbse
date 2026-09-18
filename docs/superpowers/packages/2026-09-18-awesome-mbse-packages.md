---
date: 2026-09-18
project: awesome-mbse
mode: light
rounds: 1
input_digest: 3d71470afe55ddc024f0ca19da0a41cf042f149990f672ac2c43df61fcd03613
open_objections: []
---

# Work packages: awesome-mbse (2026-09-18, light mode, round 1)

First package-loop run for the hub Path S landing cut. Trigger state: DESIGN +
docs/index.html + scripts/check_release.py landing truth already on
feat/pages-landing-and-packages; taste audit found no should-fix (visitor copy
and chrome nits already applied in the seed). Lens wave found candidates across
value/risk/cohesion; merge unioned four packages; triage graded all four PASS
with zero critical defects. Dependency order: P1, P2, P3, P4. P2 and P4 are
independent of each other; P3 follows P1.

Landing-visitor-copy and a standalone pin-validate-setup-python package were
killed or absorbed: visitor copy is already live on docs/index.html; SHA pins
for validate.yml birth sit in P1; SHA pins for link-check workflows sit in P2.

## P1: landing-truth-gate

| Field | Value |
|---|---|
| id | P1 |
| name | landing-truth-gate |
| size | M |
| deps | none |
| status | done |
| promoted_ids | [] |
| corroboration | 3 (value, risk, cohesion) |
| first_prompt | `/superpowers-process full landing truth gate` |

**Problem.** scripts/check_release.py already asserts landing chips (version,
sweep, entries) and the six section-index fragments against RELEASE-INFO and
README, and PASSes locally. No workflow runs it. Chip or section-index drift can
merge green on link-check alone. Maintainer write path is silent: PR template
and CONTRIBUTING never mention chips or the gate.

**Evidence.**

- scripts/check_release.py landing truth block and PASS on current tree
- no `.github/workflows/validate.yml`
- docs/index.html chips version 1.0.0 / sweep 2026-06 / entries 85
- awesome-archimate validate.yml pattern (checkout + setup-python SHA pins, run check_release.py)
- .github/PULL_REQUEST_TEMPLATE.md housekeeping has no landing-chip note

**In scope.** Add `.github/workflows/validate.yml` (push/PR to main +
workflow_dispatch) running `python scripts/check_release.py`; birth it with full
commit SHA pins and version comments for checkout and setup-python; document the
single write path for chips and section-index (PR template and/or CONTRIBUTING
hygiene note); confirm local gate still PASS.

**Out of scope.** Rewriting check_release chip/fragment logic; lychee args and
fail policy (P2); visitor copy or chrome on docs/index.html (already done); org
catalogue; sindresorhus PR; human Pages enable / public flip.

**Why now.** Gate exists but is not a merge barrier. Must land before catalogue
traffic and further release bumps trust the router.

**Triage notes.** PASS. Size M. SHA pin for validate.yml absorbed here (no
separate pin package).

## P2: link-check-product-surface

| Field | Value |
|---|---|
| id | P2 |
| name | link-check-product-surface |
| size | M |
| deps | none |
| status | ready |
| promoted_ids | [] |
| corroboration | 3 (value, risk, cohesion) |
| first_prompt | `/superpowers-process full landing link check coverage` |

**Problem.** PR and weekly lychee scan README.md only. PR path filters ignore
docs/index.html, so landing hrefs never wake the job. Link-check workflows also
leave actions/checkout@v4, actions/setup-node@v4, and
peter-evans/create-issue-from-file@v5 on mutable major tags while lychee-action
is already SHA-pinned.

**Evidence.**

- .github/workflows/link-check-pr.yml paths and args README-only; fail: true
- .github/workflows/link-check-schedule.yml args README-only; fail: false
- docs/index.html CTAs, section-index, contribute, licence links
- checkout@v4 / setup-node@v4 / create-issue-from-file@v5 mutable tags

**In scope.** Add docs/index.html to lychee args on PR and schedule workflows;
extend PR path filters so landing edits re-run the job; keep PR fail:true and
scheduled report-only behavior; SHA-pin mutable action tags in those workflows
with version comments.

**Out of scope.** check_release assertions (P1); new validate.yml (P1);
awesome-lint policy beyond incidental needs; distribution submissions.

**Why now.** Truth gate can prove anchors match README while outbound landing
URLs rot uncaught. Link integrity is the core failure mode of an awesome list.

**Triage notes.** PASS. Independent of P1. Link-check SHA pins absorbed here.

## P3: org-catalogue-entry

| Field | Value |
|---|---|
| id | P3 |
| name | org-catalogue-entry |
| size | S |
| deps | P1 |
| status | ready |
| promoted_ids | [] |
| corroboration | 2 (value, cohesion) |
| first_prompt | `/superpowers-process full org catalogue entry` |

**Problem.** docs/DISTRIBUTION.md marks the org catalogue
(labs.jgsystemsconsulting.com) planned. jgsystemsconsulting-website
data/products.yml has no awesome-mbse row. Discovery stays capped until Labs
routes practitioners to the hub list/Pages URL.

**Evidence.**

- docs/DISTRIBUTION.md org catalogue and Pages rows planned (2026-09-18)
- awesome-archimate products.yml entry shape (name, url, page, blurb, tier, featured, order)
- DESIGN.md primary users and surface

**In scope.** Add awesome-mbse entry on the org catalogue (products.yml + render
docs/index.html per Labs site process) with accurate one-line description;
update DISTRIBUTION.md org-catalogue (and Pages/About when the same cut makes
them true) from planned to submitted with date; leave a clean Labs branch ready
to merge.

**Out of scope.** sindresorhus PR (P4 gates assessment only); community
directory posts; landing redesign; marketplace/MCP rows (N/A).

**Why now.** Next named channel in the ledger after the landing router is
CI-gated (P1).

**Triage notes.** PASS. External-site work plus ledger update. Depends on P1.
Pages enable and public flip remain human gates outside this package if they
block a live URL; package still prepares the entry and branch.

## P4: awesome-acceptability-assessment

| Field | Value |
|---|---|
| id | P4 |
| name | awesome-acceptability-assessment |
| size | S |
| deps | none |
| status | ready |
| promoted_ids | [] |
| corroboration | 2 (value, cohesion) |
| first_prompt | `/superpowers-process full awesome acceptability assessment` |

**Problem.** sindresorhus/awesome is deferred with no written go/no-go.
DISTRIBUTION forbids opening a PR until assessment is go and the hub is public.
Without the assessment artifact the largest external channel cannot be pursued
or closed.

**Evidence.**

- docs/DISTRIBUTION.md sindresorhus row deferred
- README.md already carries the Awesome badge
- docs/runbooks/family-public-release.md Checklist C (hub public prerequisite)
- awesome-archimate assessment pattern under docs/superpowers/specs/

**In scope.** Written acceptability assessment against sindresorhus/awesome
membership bar, naming, and review expectations; explicit go/no-go plus
prerequisites; DISTRIBUTION.md note update with decision date and pointer.
Assessment only: do not open the awesome PR.

**Out of scope.** Opening the awesome PR; org catalogue work; community
directory posts; CI or landing implementation.

**Why now.** Pure gate-assessment debt; independent of P2/P3; does not block
landing CI.

**Triage notes.** PASS. Independent.

## Kills and absorptions

- landing-visitor-copy: already applied on docs/index.html (Top/Status, single
  Open full list CTA, no FAMILY lecture, favicon, woff2 preload, 44px nav, no
  IE shim). No package.
- pin-validate-setup-python as standalone: absorbed into P1 (validate.yml birth
  pins) and P2 (link-check workflow pins). No third pin package.
- Pages public enable / hub visibility flip: human DISTRIBUTION and runbook
  gates, not code packages.
- COPYRIGHT/CITATION.cff parity, Dependabot bot, a11y contrast polish: backlog
  only (see backlog delta).
