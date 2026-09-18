# Design spec: awesome-capella family spoke

- **Date:** 2026-09-17
- **Status:** draft for step-2 plan review
- **Owner:** jgsystemsconsulting
- **Gates:** research `docs/superpowers/research/2026-09-17-awesome-capella-sources-research.md`; context `docs/superpowers/context/2026-09-17-awesome-capella-pattern-context.md`; constitution `FAMILY.md` (hub repo root)

## Problem

The awesome-mbse family routes Capella workbenches and Arcadia method material to a
dedicated spoke. The FAMILY.md registry already carries the row, `awesome-capella`,
status Planned, namespace checked empty as of 2026-09. Research supplies seed pillars
for a spoke (depth bar and final namespace remain execute gates): a canonical product
home at mbse-capella.org, an active eclipse-capella GitHub org with addon repos,
scripting tools (python4capella, py-capellambse), two Arcadia method books at Elsevier,
an annual Capella Days hub, and vendor case studies from Rolls-Royce, ArianeGroup, and
CNES. A 2026-09-17 GitHub probe found no prominent incumbent awesome list but hit rate
limits mid-search (research R7 provisional); the create-day namespace recheck is the
sole hard gate (FAMILY step 1).

The work: create the spoke repo to the family shared standard, seed it with verified
entries toward the 40-entry depth bar, wire the family CI triad, and flip the hub
records only when the depth bar is met.

## Goals

- Create `jgsystemsconsulting/awesome-capella`, public, with local clone as a sibling
  of the hub at `C:\Users\gower\OneDrive\Documents\GitHub\awesome-capella`.
- Editorial rules from FAMILY.md and hub CONTRIBUTING.md: tagged entries with year,
  hyphen separator, 140-character description cap, year rule, canonical-URL dedupe,
  editorial neutrality. The awesome-sysml-v2 untagged format is explicitly not the
  template; that repo is the workflow existence proof and the markdownlint reference
  only.
- Full family CI triad: strict lychee with `--include-fragments=anchor-only` on PR and
  scheduled sweep, plus markdownlint and awesome-lint.
- Seed pass targets 40 or more entries that pass the inclusion bar, drawn from the
  research pillars.
- Hub and FAMILY.md records updated in the same effort only when the depth bar is met.

## Non-goals

- No submission to `sindresorhus/awesome` in this effort (FAMILY step 6, later, using
  the awesome-sysml-v2 runbook).
- No content re-hosting; the list links only.
- No sibling spokes (awesome-archimate, awesome-stpa, and the rest) in this effort.
- No hub edits when the depth bar is unmet; the spoke ships, the hub stays as-is.
- No listing of dead or redirect hosts: arcadia-method.com (DNS dead, multi-probe),
  capella.polarsys.org and projects.eclipse.org/projects/modeling.capella (research
  probes failed; re-probe on seed before treating as permanent), and legacy
  eclipse.org/capella or eclipse.dev/capella paths (302 off-host redirects to
  mbse-capella.org).
- No Model Gallery. The hub's anchor-table cross-listing pattern is a hub feature;
  the spoke adds one only if example-model entries ever pile up.

## Approach

Clone target is FAMILY.md plus the hub CONTRIBUTING.md editorial rules, with CI
assembled from both family references: lychee flags and awesome-lint from the hub,
markdownlint from awesome-sysml-v2. Entry format follows the hub tagged form with
year. Repo creation happens only after a same-day namespace recheck.

### Locked decisions

| # | Decision | Choice |
|---|----------|--------|
| 1 | Editorial template | FAMILY/hub tagged entry format with year; uppercase CONTRIBUTING.md; port hub year (§5), dedupe (§6), neutrality (§7); Capella-specific tag values below |
| 2 | CI | Full FAMILY triad: hub-style strict lychee (anchor-only fragments) on PR and schedule, plus markdownlint (from awesome-sysml-v2) and awesome-lint (from hub) |
| 3 | README structure | FAMILY skeleton with nine Capella/Arcadia sections (below) |
| 4 | Depth bar | Execute attempts 40+ verified entries; under 40, repo still ships, FAMILY status stays Planned, hub untouched, shortfall documented |
| 5 | Collab product | Resolve the Team for Capella / Collaboration Manager durable URL during execute; no durable page means omit that product entry only; the Collaboration section may still ship thin with other bar-passing entries |
| 6 | Hub updates | Bar met: flip FAMILY status to Live, add hub README spoke link, shrink hub Capella/Arcadia section to a pointer plus cross-cutting entries. Bar unmet: spoke only |
| 7 | Canonical URLs | mbse-capella.org over eclipse.org redirects; dead hosts never listed |
| 8 | Namespace | Recheck GitHub for awesome-capella incumbents on create day, before `gh repo create` |

### Entry format and tags (decision 1)

Entry line, identical shape to the hub:

```
- [Resource Name](https://example.com) - One-line factual description `Capella` `Arcadia` `tool` (2026).
```

CONTRIBUTING.md (uppercase filename) ports from the hub. Inclusion bar (all five must
hold), with on-topic reworded for this spoke:

1. **On-topic** — genuinely about Capella or the Arcadia method (not general MBSE only).
2. **Substantive** — teaches, demonstrates, specifies, or provides something usable. Not
   a stub. Not pure vendor marketing.
3. **Live** — the link resolves at seed or PR time.
4. **Not duplicative** — not already listed (canonical-URL rule below).
5. **Legally linkable** — publicly accessible. We link, we never re-host content.

**Verified entry** (depth bar and AC3): one README bullet that passes the five inclusion
checks, uses the tagged format, and has a live URL at seed time. Count = number of such
bullets under the nine section headings (not Contents lines, not prose).

Year rule (hub §5, frozen here):

`(YYYY)` = year of the resource's most recent author-published version: paper →
publication year; repo → latest tagged release, or latest default-branch commit if
untagged; course → current cohort year. Trivial edits (typo fixes) do not count.

Canonical-URL rule (hub §6, frozen here): force `https`, lowercase host, strip trailing
slash, drop query and fragment unless semantically required; matching canonical forms
are duplicates.

Tag axes (order fixed: language → method → tool → has-model → type → spec/standard →
paid → year). Year is the parenthetical `(YYYY)` token, not a backtick tag.

| Axis | Cardinality | Values |
|------|-------------|--------|
| language | exactly 1 | `Capella` (native Capella viewpoints/metamodel **and** Arcadia-method-only resources whose home is Capella), `UAF` (UAF/UPDM through a Capella addon), `SysML-general` (resources that primarily position Capella or Arcadia against SysML) |
| method | 0 or 1 | `Arcadia` |
| tool | 0 or more | `python4capella`, `py-capellambse`, `Capella-Studio`, `other-tool` (at 3+ entries sharing `other-tool`, graduate a named tag and update CONTRIBUTING in the same change) |
| has-model | 0 or 1 | `has-model`: directly downloadable, non-paywalled Capella model (Eclipse model project with `.aird`); screenshots and papers describing models do not qualify |
| type | exactly 1 | `tutorial`, `course`, `book`, `paper`, `blog`, `video`, `tool`, `plugin`, `docs`, `case-study` (pick the dominant form) |
| spec/standard | 0 or 1 | `standard` (use only after seed verifies the Arcadia standard id, e.g. AFNOR Z67-140 on the method page; research graded that id provisional) |
| paid | 0 or 1 | `paid` (Elsevier books, commercial training) |
| year | exactly 1 | `(YYYY)` per the year rule above |

Type values differ from the hub on purpose: `docs` is added because official
documentation is a major pillar here, `case-study` because vendor case studies are a
pillar and are not papers, and `mcp` is dropped because the research corpus did not
surface a Capella MCP (re-check on seed; add the type if one appears).

Neutrality text: JG Systems Consulting discloses its commercial MBSE consulting.
JGS-adjacent entries meet the same inclusion bar as everything else, sit next to at
least one competing entry, and a superior competitor ranks above a JGS one. Execute
writes the specific disclosure paragraph.

### CI (decision 2)

Two workflow files, assembled from the family triad:

- `.github/workflows/link-check-pr.yml`, ported from the hub file: runs on PRs
  touching README, `.lycheeignore`, or the workflow. lychee v0.24.2 via
  lycheeverse/lychee-action with `--include-fragments=anchor-only --max-concurrency 4
  --accept 200..=299,429 --no-progress README.md`, `fail: true`, and GITHUB_TOKEN so
  github.com links check authenticated instead of hitting the 60 req/hr anonymous
  limit. A second job runs awesome-lint (npx, Node 20), copied from the hub. A third
  job runs markdownlint (npx markdownlint-cli2 on README.md and CONTRIBUTING.md)
  with `.markdownlint-cli2.jsonc` copied from
  `../awesome-sysml-v2/.markdownlint-cli2.jsonc` (or equivalent minimal allowlist
  that accepts hub-style tagged list lines). Pin awesome-lint by copying the hub
  workflow pin verbatim (currently `awesome-lint@2.3.0` on hub and sysml-v2).
- `.github/workflows/link-check-schedule.yml`, ported from the hub scheduled file:
  same lychee arguments on a cron sweep; on failure open or update a report issue
  the way the hub schedule does (report-only, matching hub `fail: false` plus issue).
- `.lycheeignore`: created empty, kept only if the seed pass finds hosts that need
  exclusion.

The strict anchor-only flag enforces the hand-maintained flat Contents ToC the same
way it does on the hub.

### README structure (decision 3)

FAMILY README skeleton (literal shape; sweep month `2026-09` on ship):

```markdown
# Awesome Capella [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Curated Capella tool and Arcadia method resources for MBSE practitioners.

![Last full sweep: 2026-09](https://img.shields.io/badge/last%20full%20sweep-2026--09-brightgreen)

Part of the [awesome-mbse list
family](https://github.com/jgsystemsconsulting/awesome-mbse/blob/main/FAMILY.md).

Maintained by [JG Systems Consulting Ltd.](https://github.com/jgsystemsconsulting).
See [Editorial neutrality](CONTRIBUTING.md#editorial-neutrality).

## Contents

- [Arcadia method](#arcadia-method)
- [Capella core](#capella-core)
- [Addons and extensions](#addons-and-extensions)
- [Scripting and automation](#scripting-and-automation)
- [Collaboration and model management](#collaboration-and-model-management)
- [Books, courses, and training](#books-courses-and-training)
- [Community and events](#community-and-events)
- [Example models and case studies](#example-models-and-case-studies)
- [Commercial offers](#commercial-offers)

## Arcadia method

## Capella core

## Addons and extensions

## Scripting and automation

## Collaboration and model management

## Books, courses, and training

## Community and events

## Example models and case studies

## Commercial offers
```

Nine H2 section titles match Contents order above. Placement notes: the product home, source repo, docs, download, and releases go in
Capella core; the addons catalog page heads Addons; python4capella and
py-capellambse go in Scripting; the Capella Days hub goes in Community and events
(prior-edition links only if the page or linked hosts still list them; do not invent
replay playlists); the Obeo professional offer heads Commercial offers, which is
also where competing training vendors list.

### Seed pass and depth bar (decisions 4 and 5)

Execute runs an explicit inventory against the research pillars and attempts 40 or
more inclusion-bar entries. Indicative pillar targets, summing past 40 so a few
failures do not sink the bar: core and docs 5, addons catalog plus named addon repos
12, scripting 4, method 4, books 3, Days and related community pages 4, example
models and case studies 6, commercial and training 3. Every entry must pass the bar
and the canonical-URL rule; quality gates the count, the count never gates quality.

Version identity: the research reports Capella v7.1.0 (03 Aug 2026) as provisional
because the direct tag URL 404'd. Verify the release tag on seed before stamping any
year derived from it.

Collab product (research R4, open): no durable public URL was found for "Capella
Collaboration Manager"; the wiki references "Team for Capella" as the product name,
and candidate ObeoNetwork and eclipse-capella paths 404. Execute resolves the current
Obeo or Thales product page. No durable page means the Collaboration section ships
with whatever else passes the bar (for example labs4capella/mms-capella) or with a
single entry, and the spec accepts a thin section.

Fallback: if the seed pass lands under 40 verified entries, ship the repo with what
passed, keep the FAMILY registry status Planned, leave the hub untouched, and record
the exact count and shortfall in the spoke CHANGELOG. Do not pad the list to hit the
number.

### Hub updates (decision 6)

Only when the bar is met:

- FAMILY.md registry row: `awesome-capella` status Planned to Live.
- Hub README: add the spoke link near the top with the other family links, and shrink
  Capella/Arcadia material. **Move** entries whose primary subject is Capella or Arcadia
  alone (for example the Arcadia method official page, Eclipse Capella product home,
  Capella-only scripts such as py-capellambse when listed only as Capella tooling) to
  the spoke or replace with a one-line pointer to the spoke. **Keep** on the hub only
  entries that remain primarily multi-method or multi-tool MBSE (for example a
  methodology directory that lists Arcadia among many methods). When unsure, primary
  subject = what a reader would search by; Capella/Arcadia-primary goes to the spoke.
- Nothing else. The scope-boundary table row already exists; do not rewrite it.

### Canonical URLs (decision 7)

mbse-capella.org is the primary host for the product home, the Arcadia method page
(`arcadia.html`), the addons catalog, resources, and Capella Days. GitHub canonical
repos live under the eclipse-capella and labs4capella orgs. **Banned list URL
patterns** (must not appear as the href of any entry): `arcadia-method.com`,
`capella.polarsys.org`, `projects.eclipse.org/projects/modeling.capella`,
`eclipse.org/capella`, `eclipse.dev/capella`, and any other host that only 302s to
mbse-capella.org for the same page. Prefer the final mbse-capella.org URL. Treat
polarsys and the projects.eclipse.org path as do-not-list unless a seed re-probe
shows a live useful page that is not a pure redirect. The canonical-URL dedupe rule
makes the mbse-capella.org form win whenever both forms show up. **Redirect host**
for M6 means: the entry href's host is one of the banned patterns above, or the
href is a known permanent redirect to a canonical Capella page on another host.

### Namespace recheck (decision 8)

On create day, before `gh repo create jgsystemsconsulting/awesome-capella`: search
GitHub for `awesome-capella` and `awesome-arcadia` incumbents. A live incumbent,
roughly 100+ stars or updated within the last year, aborts creation per FAMILY step
1 and falls back to growing the hub section. The 2026-09-17 probe found the namespace
empty but hit rate limiting mid-search, so treat it as provisional. Record the
recheck result as the first CHANGELOG entry.

## Requirements

Must:

- M1. Repo `jgsystemsconsulting/awesome-capella` exists, public, with a local clone
  that is a sibling of the hub checkout (preferred path
  `...\GitHub\awesome-capella` next to `awesome-mbse`; any equivalent sibling clone
  of the named repo satisfies AC1).
- M2. All Must-inventory files below exist on main before any hub edits.
- M3. README matches the FAMILY skeleton: badges, one-line scope, family pointer,
  maintainer line, flat Contents whose anchors resolve.
- M4. Every entry matches the hub tagged format exactly: hyphen separator, code-span
  tags before the terminal period in axis order, required cardinalities from the tag
  table (exactly one language, exactly one type, exactly one year token),
  `(YYYY)` last token, description 140 characters or fewer (measured from after
  ` - ` to before the first tag).
- M5. CI triad green on main for the PR workflow: strict lychee with anchor-only
  fragments (`fail: true`), awesome-lint, markdownlint. Schedule workflow may be
  report-only (`fail: false` plus issue) and does not alone satisfy this Must.
- M6. Every entry passes the five-point inclusion bar and the canonical-URL rule;
  zero banned or redirect hosts listed (decision 7 pattern list).
- M7. Namespace recheck performed on create day and recorded in CHANGELOG.
- M8. Depth-bar rule applied: hub flips only at 40 or more verified entries;
  otherwise the spoke ships alone with the count documented.
- M9. LICENSE is CC0-1.0; CONTRIBUTING.md (uppercase) contains the ported year rule,
  canonical-URL rule, and neutrality section.
- M10. No content re-hosting anywhere in the list.

Should:

- S1. Issue template "Suggest a resource" adapted from the hub.
- S2. PR template checklist adapted from the hub.
- S3. Start with empty `.lycheeignore`; add host lines only for documented false
  positives. Never ignore banned Capella hosts from decision 7 to hide failures.

## File inventory (new repo)

Must-inventory (M2):

| File | Source | Notes |
|------|--------|-------|
| `README.md` | new, FAMILY skeleton | sections per decision 3; seeded entries |
| `LICENSE` | hub LICENSE | CC0-1.0, copy |
| `CONTRIBUTING.md` | new, ported from hub CONTRIBUTING.md | uppercase filename; inclusion bar and year/dedupe frozen in this spec; tag table Capella values; neutrality adapted; omit hub Model Gallery §8 |
| `CODE_OF_CONDUCT.md` | hub | copy |
| `SECURITY.md` | hub | copy |
| `CHANGELOG.md` | new | first entry: creation date, namespace recheck result, verified seed count |
| `.github/workflows/link-check-pr.yml` | hub link-check-pr.yml | lychee strict + awesome-lint@2.3.0 (or hub pin); markdownlint job |
| `.github/workflows/link-check-schedule.yml` | hub link-check-schedule.yml | same lychee args; report-only issue on failure |
| `.markdownlint-cli2.jsonc` | awesome-sysml-v2 | copy or minimal equivalent compatible with tagged lines |
| `.lycheeignore` | new empty | empty unless seed documents a false-positive host |

Should-inventory (S1–S2; not M2):

| File | Source | Notes |
|------|--------|-------|
| `.github/ISSUE_TEMPLATE/` | hub | Suggest a resource form, adapted |
| `.github/PULL_REQUEST_TEMPLATE.md` | hub | checklist adapted |

## Hub touch list (conditional on depth bar)

1. `FAMILY.md` registry row `awesome-capella`: status Planned to Live.
2. Hub `README.md`: spoke link near the top; Capella/Arcadia section shrunk to a
   pointer plus cross-cutting entries.
3. Nothing else.

## Acceptance criteria

- AC1. `gh repo view jgsystemsconsulting/awesome-capella` succeeds and a local
  sibling clone of that repo exists next to the hub checkout.
- AC2. The latest **PR** link-check workflow on main (or the push that landed main)
  is green across lychee (`fail: true`, anchor-only), awesome-lint, and
  markdownlint. Schedule-only green does not count.
- AC3. Verified entry count uses the definition under Entry format (section bullets
  passing inclusion + format + live URL). If count ≥ 40, hub touch list is done; if
  fewer, CHANGELOG states the exact count and the FAMILY row still reads Planned.
- AC4. Searching README hrefs for banned patterns returns nothing:
  `arcadia-method.com`, `polarsys`, `projects.eclipse.org/projects/modeling.capella`,
  `eclipse.org/capella`, `eclipse.dev/capella`. Official Capella pages use
  mbse-capella.org.
- AC5. Every entry matches the tagged format and tag cardinalities (hyphen
  separator, code-span tags in axis order, exactly one language and type, terminal
  `(YYYY).`, description ≤ 140), verified by script or full manual pass (spot check
  alone is not enough for ship).
- AC6. CONTRIBUTING.md exists with the uppercase name and contains the year rule,
  canonical-URL rule, and neutrality section.
- AC7. The lychee anchor-only run passes, proving every Contents anchor and any
  in-page anchor resolves.

## Risks

| Risk | Mitigation |
|------|-----------|
| Collab product URL stays unresolvable (research R4 open) | Ship the collaboration section thin or with the entries that pass; never guess a URL |
| Seed pass lands under 40 (research R8 open) | Spoke ships, status stays Planned, count documented; no padding |
| Capella release tag v7.1.0 unverified | Verify the tag during seeding; year stamps depend on the actual release date |
| lychee rate limits on many github.com links | Authenticated GITHUB_TOKEN and 429 accepted, per the hub workflow |
| Namespace grabbed between now and create day | Recheck on create day; abort per FAMILY step 1 on a live incumbent |
| awesome-lint rejects README title or scope shapes | Follow the FAMILY skeleton literally and lint before push |

## Research

- https://mbse-capella.org/ (Capella product home, canonical)
- https://mbse-capella.org/arcadia.html (Arcadia method page)
- https://mbse-capella.org/addons.html (official addons catalog)
- https://github.com/eclipse-capella/capella (core repo)
- https://github.com/eclipse-capella (org, addon repos)
- https://github.com/labs4capella/python4capella (scripting)
- https://github.com/DSD-DBS/py-capellambse (headless Python)
- https://mbse-capella.org/capella_days_2026.html (Capella Days hub)
- https://shop.elsevier.com/books/model-based-system-and-architecture-engineering-with-the-arcadia-method/voirin/978-1-78548-169-7 (Voirin book)
- https://shop.elsevier.com/books/systems-architecture-modeling-with-the-arcadia-method/roques/978-1-78548-168-0 (Roques book)

Full source table, dead-host list, and open items R4 (collab URL) and R8 (depth
count) live in `docs/superpowers/research/2026-09-17-awesome-capella-sources-research.md`.
Pattern evidence and file locations for the clone target live in
`docs/superpowers/context/2026-09-17-awesome-capella-pattern-context.md`.
