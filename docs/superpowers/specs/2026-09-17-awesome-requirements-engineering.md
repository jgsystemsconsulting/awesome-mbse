# Spec: awesome-requirements-engineering family spoke

Date: 2026-09-17
Status: draft for planning (superpowers step 1)
Owner: JG Systems Consulting (jgsystemsconsulting org)

## Goal

Create `jgsystemsconsulting/awesome-requirements-engineering`, a new GitHub
awesome-list repo and family spoke of the awesome-mbse list, covering
requirements engineering as its own discipline: methods, standards,
interchange formats, books and papers, open-source and commercial tools, and
community resources. The spoke follows the FAMILY.md shared standard. The
hub's format rules win over the simplifications awesome-sysml-v2 introduced,
so entries are tagged and year-stamped in the hub style, and CI blocks broken
links on PRs.

Population target: at least 40 entries that pass the inclusion bar, built
from the research pool (SC1-SC4 complete, 40+ live candidate URLs).

## Non-goals

- No work on `awesome-archimate`. That is a separate planned spoke with its
  own stem; its artifacts under `docs/superpowers/` are not inputs here.
- No submission to `sindresorhus/awesome`. That is FAMILY step 6, run later
  with the sysml-v2 submission runbook, once the list is stable.
- No requirements-engineering tooling development. This list links
  resources; it does not build them.
- No changes to the hub beyond the two go-live edits listed under
  "Hub-side updates" (registry status, README spoke link).
- No SysML v2 requirements-diagram material. That stays in
  awesome-sysml-v2 and the hub.
- No paid or gated content re-hosting. The list links; it never re-hosts.

## Scope boundaries

Route by primary subject, per FAMILY.md:

- **vs the hub (awesome-mbse).** The hub keeps cross-cutting MBSE material.
  Requirements elicitation, writing, and management as a discipline route
  here. The hub has no RE section today, so this run does not migrate hub
  entry text. Future RE-primary finds list here; the hub may keep a pointer
  only. One canonical home per resource: entry text is never copied between
  lists.
- **vs awesome-sysml-v2.** That spoke owns SysML v2 the language, including
  its requirements-modeling support. This spoke owns the RE discipline
  itself (29148, EARS, KAOS, ReqIF, RM tools). A paper on writing EARS
  requirements for SysML models lists here; a paper on SysML v2 syntax
  lists there.
- **vs awesome-magic-grid.** Magic Grid method and Cameo practice stay with
  that spoke. Cameo requirements-diagram how-tos do not list here.
- **vs awesome-archimate.** Different niche, separate run. Nothing shared.

## Deliverables

### New sibling repo (local checkout beside the hub, like `../awesome-sysml-v2`)

| File | Content |
|------|---------|
| `README.md` | FAMILY skeleton: Awesome badge, one-line scope, Last full sweep badge, family pointer, maintainer line with Editorial neutrality link to CONTRIBUTING.md, flat ToC, seven sections, 40+ entries |
| `CONTRIBUTING.md` | Uppercase name per FAMILY. Port hub CONTRIBUTING sections verbatim where FAMILY mandates it: inclusion bar (adapted examples), entry format, year rule (§5), canonical-URL dedupe (§6), neutrality (adapted), maintenance cadence. Tag vocabulary replaced with the RE table below |
| `LICENSE` | CC0-1.0, copied from hub |
| `CODE_OF_CONDUCT.md` | Ported from hub |
| `SECURITY.md` | Ported from hub, malicious-link reporting path intact |
| `CHANGELOG.md` | Initial entry: list created and first full sweep dated |
| `.github/workflows/link-check-pr.yml` | Port of hub workflow: lychee `fail: true`, `--include-fragments=anchor-only`, authenticated with `GITHUB_TOKEN`, plus the awesome-lint job |
| `.github/workflows/link-check-schedule.yml` | Port of hub workflow: weekly lychee, `fail: false`, single open `link-rot` issue (close previous, create fresh) |
| `.github/workflows/lint.yml` | markdownlint-cli2 on `README.md` and `CONTRIBUTING.md`, PR and push to main. Action refs pinned to commit SHAs, sysml-v2 style |
| `.markdownlint-cli2.jsonc` | Port from sysml-v2 (`MD013: false`), globs widened to both markdown files |
| `.lycheeignore` | Only if execute finds bot-blocked domains; each line needs a comment with reason and date |
| `.github/PULL_REQUEST_TEMPLATE.md` | Ported from hub: format, tag order, year, dedupe, neutrality, ToC checklist |
| `.github/ISSUE_TEMPLATE/suggest-resource.yml` | Ported from hub issue form, RE wording |

Repo creation order:

1. `gh repo create jgsystemsconsulting/awesome-requirements-engineering --private`
   (default branch `main`). Namespace was empty on 2026-09-17 (research SC3).
2. Bootstrap push to `main` with at least LICENSE and a minimal README so the
   default branch exists (GitHub cannot open PRs against an empty repo).
3. Population work lands as commits or a PR on top of that bootstrap.
4. Hub-side PR only after population CI is green.

### Hub-side updates (separate PR, only after spoke CI is green)

1. `FAMILY.md` registry row for awesome-requirements-engineering: Status
   `Planned. Namespace empty as of 2026-09` becomes `Live`. The row already
   exists; do not add a second one.
2. Hub `README.md` List family table: set the requirements-engineering row
   Status to Live and note the private spoke location (no public URL required
   while the spoke is private).

Nothing else in the hub changes. The hub carries no RE section today, so no
content shrink is needed.

## README structure

Skeleton from FAMILY.md badges and pointer lines. While the hub is private,
the family pointer is text-only (no hyperlink to hub FAMILY.md). Scope line:

> Curated list of requirements engineering resources: standards, methods,
> interchange formats, tools, books, and community.

Seven top-level sections (research SC4 clustering), flat hand-maintained ToC:

1. Standards and guides
2. Interchange and integration
3. Methods and notation
4. Books and foundational papers
5. Open-source tools
6. Commercial tools
7. Learning, certification, and community

Minimum count: 40 entries passing the inclusion bar at execute time. The
research pool exceeds 40 live candidates; curation applies the bar, not the
pool dump. Drop-offs already decided by research: V&V-only tools (LDRA,
VectorCAST) are not primary RE entries; Wikipedia overview pages are
orientation, not entries; SEBoK gets at most one pointer entry under
Learning, or stays out.

Required list entries (not ToC anchors) at these canonical URLs:

- ISO/IEC/IEEE 29148: https://ieeexplore.ieee.org/document/6170935 (Standards)
- OMG ReqIF 1.2: https://www.omg.org/spec/ReqIF/1.2/ (Interchange)
- IREB CPRE: https://cpre.ireb.org/en/ (Learning)
- EARS (Mavin): https://alistairmavin.com/ears/ (Methods); second entry RE'09
  paper https://doi.org/10.1109/RE.2009.9 (Books and foundational papers)
- KAOS (van Lamsweerde): https://webperso.info.ucl.ac.be/~avl/ (Methods);
  second entry Wiley book
  https://www.wiley.com/en-us/Requirements+Engineering%3A+From+System+Goals+to+UML+Models+to+Software+Specifications-p-9780470012703
  (Books)
- Wiegers & Beatty: https://www.microsoftpressstore.com/store/software-requirements-9780735679665 (Books)
- ReqView: https://www.reqview.com/ (Commercial tools)
- IBM DOORS Next: https://www.ibm.com/products/requirements-management-doors-next (Commercial tools)
- JAMA Connect: https://www.jamasoftware.com/platform/jama-connect/ (Commercial tools)
- Visure: https://visuresolutions.com/ (Commercial tools)

Canonical-URL choices from research stand: IEEE Explore landing for 29148
(iso.org 403s bots), Microsoft Press over Amazon for Wiegers, UCL page for
KAOS (kaos.com is parked), stable product names for IBM pages whose SPA
subtitle text fluctuates.

## CONTRIBUTING tag vocabulary

Hub axis set, cardinality, and order are kept per FAMILY. Values are the RE
adaptation, defined in the spoke CONTRIBUTING.md:

Order: `language → method → tool → has-model → type → spec/standard → paid → year`

| Axis | Cardinality | Values |
|------|-------------|--------|
| language (requirement notation) | exactly 1 | `textual` · `model-based` · `RE-general` |
| method | 0 or 1 | `EARS` · `KAOS` · `Volere` · `other-method` |
| tool | 0 or more | `DOORS` · `ReqView` · `Jama` · `Visure` · `Polarion` · `other-tool` |
| has-model | 0 or 1 | `has-model` · `has-template` (pick one; two downloadables get two entries) |
| type | exactly 1 | `tutorial` · `course` · `book` · `paper` · `blog` · `video` · `tool` · `plugin` · `template` · `standard` · `spec` · `guide` · `community` |
| spec/standard | 0 or 1 | `spec` · `standard` (optional echo of type when type is `spec` or `standard`) |
| paid | 0 or 1 | `paid` |
| year | exactly 1 | `(YYYY)` per hub §5 |

Order stays the hub axis order:
`language → method → tool → has-model → type → spec/standard → paid → year`

Definitions the spoke CONTRIBUTING.md must carry:

- `textual`: natural-language requirement writing (EARS, quality guides, Volere
  template practice). `model-based`: goal-oriented or other model-centric RE
  (KAOS and kin). `RE-general`: default for tools, interchange, certification,
  community, and discipline-wide standards/books when no notation focus.
- `has-model`: downloadable goal model or ReqIF sample. `has-template`:
  downloadable requirements template or pattern sheet. Cardinality remains 0
  or 1 on this axis; if both apply, split into two list entries.
- `other-tool` and `other-method` graduate to their own tags once 3 or more
  entries share them (hub graduation rule).
- Type for commercial or open-source products is `tool` (plugins: `plugin` under
  Open-source tools unless paid commercial). Type for ISO/IEEE normative docs
  is `standard`; OMG/consortium formats `spec`; informal practice guides
  `guide`; orgs/conferences/magazines `community`. Do not also use type `paper`
  on those.
- Optional `spec`/`standard` axis may echo the same token; it never replaces type.
- Any non-free resource (tool, book, course, cert) carries `paid` when access
  requires purchase or paid enrollment. Free open-source tools omit `paid`.

Year rule, canonical-URL dedupe rule, description cap (140 characters), and
hyphen separator are copied from hub CONTRIBUTING sections 5, 6, and 3 as
FAMILY requires. Editorial neutrality: JG Systems Consulting currently sells
no requirements-management product; the section states that, keeps the
disclosure, and applies the competing-entry-alongside rule if that ever
changes.

## CI and workflows

Three workflows, all ported and retargeted, action refs pinned to SHAs:

1. **link-check-pr.yml** (PR paths: README.md, .lycheeignore, the workflow
   itself). Lychee v0.24.x, `--include-fragments=anchor-only`,
   `--accept 200..=299,429`, `fail: true`, `GITHUB_TOKEN` passed so github.com
   links are checked authenticated. Second job: `npx -y awesome-lint`.
2. **link-check-schedule.yml** (cron Mondays 06:00 UTC, workflow_dispatch).
   Lychee `fail: false`, writes `lychee/out.md`, closes prior `link-rot`
   issues, opens one fresh report. `issues: write` permission.
3. **lint.yml** (PR and push to main). markdownlint-cli2 over README.md and
   CONTRIBUTING.md. awesome-lint stays in workflow 1, matching the hub.

Note the deliberate differences from awesome-sysml-v2: its `links.yml` runs
`fail: false` on PRs (advisory) and its entries are untagged. FAMILY requires
a PR link check plus the tagged entry format; the hub implements the PR check
as blocking (`fail: true` in `link-check-pr.yml`). Copy sysml-v2 structure and
markdownlint config, not its untagged entry format or its advisory PR link
gate.

## Success criteria / acceptance

1. Repo `jgsystemsconsulting/awesome-requirements-engineering` exists,
   private (FAMILY private-mode default), default branch `main`, sibling
   checkout locally. Public release is out of scope for this run.
2. Full spoke file set from the Deliverables table is present (README,
   CONTRIBUTING.md, LICENSE CC0, CODE_OF_CONDUCT.md, SECURITY.md, CHANGELOG.md,
   three workflows, markdownlint config, PR template, suggest-resource issue
   form).
3. README matches the FAMILY skeleton: Awesome badge, scope line, Last full
   sweep badge, family pointer, maintainer line with neutrality link, flat
   ToC whose every anchor resolves, seven sections.
4. At least 40 entries after the inclusion bar; every entry matches the tagged
   format with a year token; every required list entry URL above is present in
   its assigned section.
5. All three workflows exist and the population PR shows lychee
   (`fail: true`), awesome-lint, and markdownlint green.
6. Scheduled workflow has been proven once via `workflow_dispatch` and produces
   the single `link-rot` issue shape (do not rely on waiting for Monday cron).
7. Hub updates land in their own PR only after step 5: FAMILY registry
   status becomes `Live` with Visibility `private`; hub README List family
   row becomes Live with a private-spoke location note.
8. CHANGELOG records the initial sweep date; the badge matches it.
9. No entry text is copied from awesome-sysml-v2, the hub, or the niche
   `awesome-requirements-writer` list found in the namespace check.

## Risks and mitigations

- **sysml-v2 exemplar drift.** The nearest structural exemplar diverges on
  untagged entries, lowercase `contributing.md`, and advisory PR lychee
  (`fail: false`). FAMILY forbids the untagged format and requires a PR link
  check; the hub's blocking gate is the pattern this spoke copies. Mitigation:
  copy structure and configs only; hub CONTRIBUTING and FAMILY are the format
  source of truth; acceptance criteria 4 and 9 catch regression.
- **Link rot and SPA churn.** IBM and other vendor pages fluctuate; two
  vendor URLs already needed a second research round. Mitigation: weekly
  scheduled sweep, stable product names in descriptions, IEEE/Publisher
  canonical URLs over catalog pages that 403 bots.
- **Bot-blocked domains.** iso.org and INCOSE 403 automated clients.
  Mitigation: research already picked fetchable canonical URLs; if lychee
  still reports false dead links, add justified `.lycheeignore` lines, each
  with reason and date.
- **Marketing-only vendor entries.** Commercial tool pages drift toward
  brochure copy. Mitigation: inclusion bar in CONTRIBUTING, factual one-line
  descriptions, research-mandated exclusions (V&V-only tools) carried into
  execute.
- **GitHub rate limits in CI.** Anonymous lychee reports live links dead at
  60 req/hr. Mitigation: pass `GITHUB_TOKEN` to the action, hub pattern.
- **Premature hub flip.** Marking the registry Live before CI is green
  violates FAMILY step 5 ordering. Mitigation: hub edits are a separate PR
  gated on the spoke's green population run; acceptance criteria 5 and 7
  enforce the order.

## Research

Findings document: `docs/superpowers/research/2026-09-17-awesome-requirements-engineering-sources-research.md`
(SC1-SC4 RESEARCH_COMPLETE, retrieved 2026-09-17, 40+ live candidate URLs,
namespace check, section clustering).

Key source URLs behind the anchors:

- https://ieeexplore.ieee.org/document/6170935
- https://www.omg.org/spec/ReqIF/1.2/
- https://alistairmavin.com/ears/
- https://webperso.info.ucl.ac.be/~avl/
- https://www.microsoftpressstore.com/store/software-requirements-9780735679665
- https://www.ibm.com/products/requirements-management-doors-next
- https://eclipse.dev/rmf/
- https://github.com/doorstop-dev/doorstop
- https://github.com/strictdoc-project/strictdoc

## Codebase context

Pattern context document:
`docs/superpowers/context/2026-09-17-awesome-requirements-engineering-pattern-context.md`
(SC1-SC6 met against hub HEAD `4f7c0a6`). Decisions it locks and this spec
inherits: sibling repo under the org, never nested in the hub; hub
FAMILY/CONTRIBUTING tagged entry format beats the sysml-v2 untagged format;
uppercase `CONTRIBUTING.md`; blocking lychee on PR plus weekly sweep,
awesome-lint, and markdownlint (sysml-v2 shape, hub gate); hub registry and
README updates only after the spoke is populated and green; CC0-1.0
license; ignore `docs/superpowers/*awesome-archimate*` artifacts as stem
sources. Source files read: `FAMILY.md` (model, registry, shared standard,
starting-a-new-list, README skeleton), hub `CONTRIBUTING.md` (entry format,
tag axes, year and dedupe rules, neutrality), hub `.github/workflows/`
(link-check-pr.yml, link-check-schedule.yml), and the awesome-sysml-v2
checkout (`lint.yml`, `.markdownlint-cli2.jsonc`, `contributing.md`,
`README.md`).

## Open questions

None blocking. Two judgment calls planning may revisit: the language-axis
value names (`textual` / `model-based` / `RE-general`) and whether SEBoK
earns one pointer entry under Learning. Both are one-line CONTRIBUTING or
README edits, not design forks.
