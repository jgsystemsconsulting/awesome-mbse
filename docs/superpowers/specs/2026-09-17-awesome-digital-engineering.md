# Spec: awesome-digital-engineering (family spoke)

Date: 2026-09-17. Author: sp-spec-author (Superpowers step 1). Status: ready for step 2 (plan).

## Problem / goal

The awesome-mbse family already routes "Digital thread, model-based definition, digital
engineering transformation" to a spoke named `awesome-digital-engineering` in the FAMILY.md
registry, but no repo exists (org namespace confirmed empty, 404 as of 2026-09). Readers who
want DE resources have no canonical family home: the hub has no DE resource section today,
and the hub's scope table promises a spoke that does not exist.

Goal: create `jgsystemsconsulting/awesome-digital-engineering` as a public sibling git repo,
built to the FAMILY shared standard (not to awesome-sysml-v2 drift), launched in
skeleton-plus-verified-seed mode, with CI green on day one, and with the hub registry and
README updated in the same effort.

Launch mode is locked: ship with every entry that passes the inclusion bar and a live,
verified URL, then grow toward the FAMILY ~40-entry bar via a tracked seed inventory. A
launch with fewer than 40 entries is acceptable and must be labeled honestly (README and
CHANGELOG note "initial seed; growth in progress"). The repo does not block on 40.

## Non-goals

- **No awesome-archimate work.** The user prompt said "awesome archimit"; that maps to the
  separate planned spoke `awesome-archimate`. This effort touches only
  `awesome-digital-engineering`.
- **No SysML v2 content.** Language spec, parsers, editors, API clients stay on
  awesome-sysml-v2. General MBSE methodology stays on the hub.
- **No re-hosting of paywalled or proprietary standards.** ASME, ISO, SAE storefront or
  free-overview links only. We link, never redistribute.
- **No markdownlint CI in v1.** FAMILY text names markdown lint; the hub actually runs only
  lychee + awesome-lint. v1 matches hub actual. Adding markdownlint is a family-wide
  decision, not a per-spoke one.
- **No sindresorhus/awesome submission** in this effort. That is FAMILY step 6, run later
  with the awesome-sysml-v2 runbook.
- **No commercial PLM/CAD feature matrices or vendor comparisons.** Commercial platforms
  appear as link-level entries tagged `paid`, same inclusion bar as everything else.
- **No scraping or WAF circumvention.** Bot-blocked hosts are handled by the .lycheeignore
  rule (below) only after a human confirms the link is live in a browser.
- **No ArchiMate, Capella, requirements-engineering, STPA, or Magic Grid content.** Other
  registry rows own those.

## Repo identity and location

- **GitHub repo:** `jgsystemsconsulting/awesome-digital-engineering`, public, default
  branch `main`. Namespace verified empty on 2026-09-17 (`gh api` 404; GitHub search shows
  no substantive incumbent list for this niche).
- **Local clone (new git root, NOT a hub subdirectory):**
  `C:\Users\gower\OneDrive\Documents\GitHub\awesome-digital-engineering`, sibling of the
  hub clone, matching the existing family convention.
- **Creation command (plan must carry this):** from the local clone after the initial commit,
  `gh repo create jgsystemsconsulting/awesome-digital-engineering --public --source . --remote origin --push`
  (or web-UI create + `git remote add origin …` + `git push -u origin main` if `gh` lacks
  auth/org permission). That first push establishes `main`. **CI green path (AC6):** after
  workflows land on `main`, open a launch PR that only touches list content (or a no-op
  `chore: launch ci proof` branch) so `link-check (PR)` runs green; also run
  `workflow_dispatch` on the schedule workflow once. Direct push alone does not satisfy AC6.
- **License:** CC0-1.0 (standard legal text) plus a NOTICE file following the hub pattern
  (CC0 waiver statement, linked-resources ownership line, nominative-use trademark line
  adapted to DE: reference standards by number and name, no endorsement implied).

## Codebase context

Normative template is the hub repo (`awesome-mbse`) at HEAD `4f7c0a63eb84e8ca29db1e565918a021e818cff3`:

- `FAMILY.md` defines the family model, the registry row for this spoke, the scope table
  routing DE/MBD/digital thread here, the shared standard (files, entry format, tag axes,
  CI, sweep cadence), the start-new-list checklist, and the README skeleton (lines 108-128).
- Hub `CONTRIBUTING.md` is the port source for: entry format (§3), tag vocabulary table and
  cardinality (§4), the year rule (§5) and canonical-URL dedupe rule (§6) which FAMILY says
  to copy verbatim, and editorial neutrality (§7) adapted to this niche.
- Hub CI is `.github/workflows/link-check-pr.yml` (lychee `--include-fragments=anchor-only`
  with `--accept 200..=299,429`, plus awesome-lint) and `link-check-schedule.yml` (weekly
  Monday cron, report-only lychee, single rolling `link-rot` issue). Supporting files:
  `.lycheeignore` (bot-blocked hosts, commented, re-verified each sweep),
  `.github/ISSUE_TEMPLATE/suggest-resource.yml`, `.github/PULL_REQUEST_TEMPLATE.md`.
- awesome-sysml-v2 is a live spoke but has drifted from FAMILY: no family pointer, no sweep
  badge, plain untagged entries, lowercase `contributing.md`, differently named CI
  workflows, and a CITATION.cff license mismatch. It is used only as an existence proof of
  a live spoke. Do not copy its layout, filenames, or entry style.

## File inventory

Required in the new repo at launch:

| File | Source / rule |
|------|---------------|
| `README.md` | FAMILY skeleton, sections below, verified seed entries |
| `CONTRIBUTING.md` | uppercase name; hub CONTRIBUTING ported (bar, format, tags, year rule §5 and dedupe rule §6 verbatim, neutrality adapted, ToC rule, local link-check, cadence) |
| `LICENSE` | CC0-1.0 full legal text |
| `NOTICE` | hub pattern, DE-adapted trademark line |
| `CODE_OF_CONDUCT.md` | hub copy, repo name swapped |
| `SECURITY.md` | hub copy, repo name swapped |
| `CHANGELOG.md` | hub style; launch entry; initial-seed note if under 40 entries |
| `.github/workflows/link-check-pr.yml` | hub file copied; trigger paths unchanged |
| `.github/workflows/link-check-schedule.yml` | hub file copied verbatim |
| `.github/ISSUE_TEMPLATE/suggest-resource.yml` | hub form, DE wording |
| `.github/PULL_REQUEST_TEMPLATE.md` | hub template, DE wording |
| `.lycheeignore` | new file, hub header comment style, DE entries only after browser verification |
| `.gitignore` | hub copy |

No other files at launch. No CITATION.cff (the hub has none; sysml-v2's is a known
inconsistency, not a pattern to copy). `docs/` stays empty.

## README structure and section taxonomy

Skeleton order, per FAMILY: Awesome badge; one-line scope statement; `Last full sweep`
badge dated the launch month (`2026-09`); family pointer as an **absolute** URL to
`https://github.com/jgsystemsconsulting/awesome-mbse/blob/main/FAMILY.md` (separate git
root; relative paths will break); maintained-by line linking JG Systems Consulting and the
CONTRIBUTING neutrality section; flat hand-maintained `## Contents` (top-level sections
only, each ToC line is a markdown anchor to an H2 that exists); then sections.

Eight top-level sections, in this order. **Empty sections are allowed at launch** (seed may
be thin): keep the H2 and a single italic stub line `_No verified entries yet._` so the
flat ToC still resolves. Do not omit an H2.

1. **Policy and strategy** - national and organizational DE strategies, roadmaps, policy
   documents (DoD Digital Engineering Strategy and successors, allied-nation equivalents
   once verified).
2. **Standards** - MBD and product-data standards in document order: ASME Y14.41 family,
   ISO 10303 (STEP) parts, QIF / ISO 23952, DMIS / ISO 22093, LOTAR / EN-NAS 9300,
   OAIS / ISO 14721. Storefront, committee, and free-overview links only. Flat list; group
   by standard family in document order rather than subsections, so the ToC stays flat.
3. **Digital thread and interoperability** - thread architecture, data exchange in
   practice, PLM interoperability resources, authority-data and configuration-linked data.
4. **Model-based definition and PMI** - MBD practice, product and manufacturing
   information, GD&T in model-based workflows, TDP guidance.
5. **Government and consortia programs** - program offices, working groups, and
   consortia outputs (NDIA, INCOSE DE working groups, DMSC, LOTAR International, PDES
   activity) once their pages verify.
6. **Open tools and reference implementations** - open-source STEP/QIF/JT tooling,
   parsers, converters, model viewers. `has-model` lives here most often.
7. **Learning and reports** - courses, tutorials, books, survey papers, government and
   academic reports.
8. **Commercial platforms** - paid tools, training, and platforms. Every entry here
   carries `paid`. Kept last and small.

Routing tie-break: a government or consortium report about a specific program or standard
goes to section 5 or 2 by its primary subject; explainers, surveys, and teaching material
go to 7. Borderline family routing may add a **hub** cross-link only in v1 (no requirement
to edit other spoke repos in this effort).

**Section → default `domain` (exactly one domain tag per entry):**

| Section | Default domain | Notes |
|---------|----------------|-------|
| 1 Policy and strategy | `DE-general` | |
| 2 Standards | `MBD` or `digital-thread` by primary subject (STEP/thread exchange → `digital-thread`; Y14.41/PMI/QIF metrology → `MBD`) | never `DE-general` |
| 3 Digital thread | `digital-thread` | |
| 4 MBD and PMI | `MBD` | method `GD&T` when the entry is primarily GD&T |
| 5 Government/consortia | `DE-general` unless the page is only about one standard family | |
| 6 Open tools | `digital-thread` or `MBD` by file/tool focus | type usually `tool` |
| 7 Learning and reports | `DE-general` unless topic-locked to thread or MBD | |
| 8 Commercial | match the product's primary claim | always `paid` |

`DE-general` is legal only when the entry's primary subject is not specifically digital-thread
or MBD (strategy surveys, broad DE transformation, multi-topic reports). If either specialized
domain fits, use it. Reviewers reject lazy `DE-general` on standards and pure MBD/thread tools.

## Entry format and DE-specific tag vocabulary

Entry format is the hub format verbatim:

```
- [Resource Name](https://example.com) - One-line factual description `tag` `tag` (YYYY).
```

Hyphen separator (never an en/em dash). **Description length:** at most 140 characters
measured from the first non-space character after ` - ` through the character before the
first tag backtick (hub CONTRIBUTING §3). Tags as inline code spans before the terminal
period, year in parentheses as the last token. **Year rule (hub §5, restated):** use the
resource's publication or last-substantive-update year as four digits; if unknown, omit the
entry until known (do not invent). **Canonical-URL dedupe (hub §6, restated):** before
adding, normalize candidate and existing URLs (https, strip trailing slash and tracking
query noise) and reject duplicates of the same canonical form.

**Inclusion bar (hub §2, restated for inventory pass/fail):** on-topic for this spoke's
scope table; substantive (not a stub, not pure vendor marketing fluff); live URL; not
duplicative under the canonical-URL rule; legally linkable and publicly accessible (we
link, never re-host). Inventory rows record pass/fail against this bar.

Example entry (legal under the DE table: domain, type, standard, paid, year):

```
- [ASME Y14.41](https://www.asme.org/codes-standards/find-codes-standards/y14-41-digital-product-definition-data-practices) - Digital product definition data practices for annotated model-based 3D datasets `MBD` `report` `standard` `paid` (2026).
```

FAMILY fixes the axis order and cardinality as `language → method → tool → has-model →
type → spec/standard → paid → year` (FAMILY.md shared-standard tag vocabulary). This spoke
keeps that order and the exactly-1 first-axis slot, but renames the first axis from
`language` to `domain` as an intentional per-list deviation: DE has no single modeling
language to name, and FAMILY allows per-list values while this list also needs a first-axis
label that is not a lie. Document the rename in CONTRIBUTING.md. DE values:

| Axis | Cardinality | Values |
|------|-------------|--------|
| domain | exactly 1 | `DE-general` · `digital-thread` · `MBD` (see section routing and DE-general rule above) |
| method | 0 or 1 | `MBE` (model-based enterprise practice) · `GD&T` (write as `` `GD&T` ``) |
| tool | 0 or more | v1 vocabulary: `other-tool` only. A named tool tag graduates when 3 or more entries share it, added in one PR |
| has-model | 0 or 1 | Apply only when the entry's **primary URL is the downloadable file** (or a landing page whose sole purpose is that file). Hub structure: directly downloadable, non-paywalled, opens in a named tool. Hub formats (MBSE): `.mdzip`, `.mdxml`, `.sysml`, `.uml`, Eclipse model project. DE formats: `.step`/`.stp`/`.p21`, `.qif`, `.jt`. Do **not** put `has-model` on a `type=tool` repo homepage; use `type=tool` alone. Screenshots and access-gated files never qualify. |
| type | exactly 1 | `tutorial` · `course` · `book` · `paper` · `report` · `blog` · `video` · `tool` · `plugin` (`mcp` omitted in v1). **Standards/storefront/policy/program home pages use `report`** (not a missing enum value). |
| spec/standard | 0 or 1 | `spec` · `standard` for normative documents. Pairing: if this axis is present, type must be one of `report`, `book`, `paper` (prefer `report` for storefronts); do not use `tutorial`/`tool` with `standard`. |
| paid | 0 or 1 | `paid` (storefront standards, commercial platforms and training) |
| year | exactly 1 | `(YYYY)` per year rule above |

`other-tool` graduates exactly like the hub rule. Tag order/cardinality and DE vocabulary are
enforced by human review + CONTRIBUTING in v1 (CI is lychee + awesome-lint only; no custom
tag linter).

## Seed policy and inventory gate

Three rules govern what ships at launch:

1. **Verified-only entries.** Every launch entry URL is live-checked during execute
   (HTTP 200-299 via browser fetch or lychee against that URL) before it lands. No entry is
   committed on citation reputation alone. Research grades are prioritization hints only:
   ASME Y14.41 is ESTABLISHED in research and still must pass the same live check at
   execute; all other candidates are PROVISIONAL until that check passes. HTTP 429 alone is
   **not** verified for launch (retry, browser-confirm 200-class, or omit).
2. **Provisional host list, no invented URLs.** Blocked or flaky hosts from the research
   gate: `acq.osd.mil`, `media.defense.gov`, `iso.org`, `incose.org`, `ndia.org`,
   `sebokwiki.org`, `ntrs.nasa.gov`, plus hub known blocks (ResearchGate, Wiley/INCOSE
   library). For each candidate on these hosts, execute either (a) verifies the exact URL
   is live (200-299) in a browser, adds the entry, and adds an **active** `.lycheeignore`
   pattern line with a trailing `# browser-verified YYYY-MM-DD: <reason>` comment, or (b)
   omits it. DoD strategy PDF paths stay out of the README until a **live URL** is verified;
   a local file hash may be recorded in the seed inventory for maintainer notes but is
   **not** a substitute for a public linkable URL in the README.
3. **Inventory gate toward 40.** Execute maintains a seed inventory checklist (working
   markdown in the superpowers workspace, not committed to the spoke): one row per
   candidate with target URL, host verdict, inclusion-bar pass/fail, and reason. The bar
   is the FAMILY ~40 live entries. If launch day closes below 40: ship anyway, add the
   line "initial seed; growth in progress" to the README scope block and the CHANGELOG
   launch entry, convert remaining checklist rows to GitHub issues labeled
   `seed-inventory`, and flip the hub registry row to Live anyway. This is an explicit
   override of FAMILY.md earn-a-repo prose (~40+ live entries or keep the niche as a hub
   section only): locked user decision for this launch is Live = existing public repo +
   green CI + honest under-40 label, not a hard 40-entry floor.

Known seed signals to mine during execute: the verified ASME storefront; DMSC/QIF and
LOTAR sites (curl-verified homepages); NASA NTRS API signal of roughly 79 public-distribution
hits for "digital engineering" (PROVISIONAL count from the research gate, not a curated
entry list; curate a handful of specific citations after verify, not a search dump);
open-source STEP tooling projects (verify each repo live before entry); SEBoK, NDIA,
INCOSE DE pages (browser-verify or omit). Wikipedia is a fallback explainer link only if
nothing better verifies; prefer primary and named-secondary sources.

## CI and quality gates

Copy the hub actual for v1, filenames and all:

- `link-check-pr.yml`: lychee v0.24.2 via lychee-action with
  `--include-fragments=anchor-only --max-concurrency 4 --accept 200..=299,429 --no-progress
  README.md`, `fail: true`, `GITHUB_TOKEN` passed for authenticated github.com checks;
  awesome-lint job on Node 20 (`npx -y awesome-lint`). Triggers on PRs touching
  `README.md`, `.lycheeignore`, or the workflow file.
- `link-check-schedule.yml`: Mondays 06:00 UTC plus `workflow_dispatch`; report-only
  lychee (`fail: false`, output to `./lychee/out.md`), closes prior `link-rot` issues and
  opens one fresh report via create-issue-from-file with the `link-rot` label.
- `.lycheeignore`: starts empty except the hub header comment. Add a line only after the
  URL is confirmed live in a browser and documented as bot-blocked. Re-verify every
  quarterly sweep. Expected early candidates: `iso.org`, `ndia.org`, `incose.org`,
  `media.defense.gov`, `researchgate.net`.
- **No markdownlint job in v1** (locked; matches hub actual). Revisit as a family change.
- **Quality gates that are prose, not CI** (hub discipline): canonical-URL dedupe, year
  rule, description length, tag vocabulary and order, flat ToC with hand-updated anchors.
  The PR template checklist carries them, lychee anchor-only validates ToC and in-doc
  anchors, awesome-lint validates list manifest conformance.
- **Cadence:** quarterly sweep logged in CHANGELOG.md with the `Last full sweep` badge
  updated; the weekly scheduled workflow is the rot detector between sweeps. The launch
  sweep date is the launch month.

## Hub integration

Same overall effort, after the spoke repo exists and CI is green on `main`:

1. Flip the FAMILY.md registry row from "Planned. Namespace empty as of 2026-09" to
   **Live** with the repo URL.
2. Add a spoke link near the top of the hub README (where existing spokes are listed).
3. If the hub carries DE/MBD/digital-thread material outside its legitimate cross-cutting
   entries, shrink that material to a short pointer to the spoke plus genuinely
   cross-cutting entries, per FAMILY. Scope: touch only DE-routed content; no general hub
   reorganization.
4. One canonical home per resource holds across the family: a DE-standard entry lives in
   the spoke; the hub may link to it, never copy the entry text.

## Acceptance criteria

1. `https://github.com/jgsystemsconsulting/awesome-digital-engineering` exists, is public,
   default branch `main`, and is its own git root (not inside the hub tree). Preferred local
   path is the sibling path above; any other clone path is fine if the remote matches.
2. All 13 files in the inventory table exist; `CONTRIBUTING.md` is uppercase; hub year rule
   and canonical-URL dedupe appear in it (verbatim port of hub §5/§6); CONTRIBUTING also
   documents the `language`→`domain` first-axis rename, DE value set, section→domain table,
   and `DE-general` rule.
3. README follows the FAMILY skeleton: Awesome badge, one-line scope, sweep badge dated
   `2026-09`, **absolute** family pointer URL, maintained-by line, flat ToC; every ToC
   anchor resolves under lychee `--include-fragments=anchor-only`.
4. All eight section H2s exist in the specified order (empty stub lines allowed); every
   real entry line matches entry format (hyphen separator, ≤140-char description measured
   as above, tags in axis order from the DE table including exactly one `type`, year last).
5. Every entry URL returned HTTP 200-299 during execute verification. Bot-blocked hosts that
   still ship use an **active** `.lycheeignore` pattern plus trailing browser-verified
   comment; 429-only is not enough. **Access-control exemption (one line):** the absolute
   family pointer to private hub `FAMILY.md` may carry an active `.lycheeignore` pattern
   from launch without browser 200 (spoke CI token cannot read the private hub). Comment
   must say access-controlled until family public release; remove the line when the hub
   goes public. This is the only non-browser-verified ignore allowed.
6. CI proof: both workflows present with hub filenames; awesome-lint passing; lychee PR
   workflow green on a launch PR (not only a direct push); schedule workflow run once via
   `workflow_dispatch`. No markdownlint workflow exists.
7. `LICENSE` is CC0-1.0 and `NOTICE` follows the hub pattern with DE-adapted trademarks.
8. CHANGELOG has a dated launch entry; if entry count is under 40, README and CHANGELOG
   both carry the "initial seed; growth in progress" note.
9. The seed inventory checklist exists outside the repo with one row per candidate, inclusion-bar
   pass/fail, host verdict, and remaining viable rows converted to `seed-inventory` issues
   (create the GitHub label if missing).
10. Hub FAMILY.md registry row says Live with the URL; hub README links the spoke near
    the top; no DE-routed hub section remains unshrunk (pointer rule applied or the hub
    had no such section).
11. No URL from the provisional/blocked host set appears in the README without browser
    200-299 verification and the matching `.lycheeignore` treatment; no file in the repo
    re-hosts third-party content.

## Open questions

None blocking. Execute owns two verifications the research gate could not close: (a) a
live, citable URL for the DoD Digital Engineering Strategy (or omission), and (b) exact
ISO catalog entry points for the STEP/QIF/LOTAR standards (or storefront/overview
alternatives). Both follow the seed policy rules above. Private-hub family-pointer
lycheeignore exemption is locked under AC5 (not an open question).

## Research

Research gate: `docs/superpowers/research/2026-09-17-awesome-digital-engineering-research.md`
(log: `docs/superpowers/research/2026-09-17-awesome-digital-engineering-research-log.md`).
Context gate: `docs/superpowers/context/2026-09-17-awesome-digital-engineering-context.md`.

URLs established or provisionally identified by the gate:

- https://www.asme.org/codes-standards/find-codes-standards/y14-41-digital-product-definition-data-practices
- https://qifstandards.org/about-dmsc/
- https://lotar-international.org/
- https://ntrs.nasa.gov/api/citations/search/?q=%22digital%20engineering%22&page.size=5
- https://en.wikipedia.org/wiki/ISO_10303
- https://github.com/search?q=awesome-digital-engineering&type=repositories
- https://api.github.com/repos/jgsystemsconsulting/awesome-digital-engineering
- https://github.com/jgsystemsconsulting/awesome-mbse/blob/main/CONTRIBUTING.md
- https://github.com/jgsystemsconsulting/awesome-mbse/blob/main/FAMILY.md

Blocked this session, candidates only until browser-verified in execute:
`acq.osd.mil`, `media.defense.gov`, `iso.org`, `incose.org`, `ndia.org`, `sebokwiki.org`.
