# Spec: awesome-stpa, a spoke list in the awesome-mbse family

## Problem

The awesome-mbse family registry lists `awesome-stpa` as Planned with visibility
`none yet` (FAMILY.md Registry table, awesome-stpa row), and the scope-boundary
table routes STAMP/STPA, hazard analysis, and functional safety standards to it
(FAMILY.md Scope boundaries, STAMP/STPA row). Nothing has been built. A
practitioner hunting STPA material today has MIT PSAS pages, scattered GitHub
repos, and paywalled standards, but no curated, dated, link-checked index.
Research found no incumbent `awesome-stpa` or `awesome-stamp` list on GitHub or in
sindresorhus/awesome, and a candidate pool of 40+ distinct URL-backed resources.
The family's depth bar (roughly 40+ live entries, no incumbent) is met, so per
FAMILY Model rule 2 the niche earns its own repo.

## Goal

Ship `jgsystemsconsulting/awesome-stpa` v1 to the FAMILY shared standard with at
least 40 live, format-conformant entries, and flip the hub (FAMILY.md registry row
and hub README spoke link) to Live in the same program of work.

## Non-goals

- An ArchiMate list. The user once said "archimit" in the same breath; that
  referred to the separate `awesome-archimate` planned spoke and does not apply
  to this stem. ArchiMate stays untouched here.
- Bulk-importing the MIT STAMP workshop presentations archive as individual list
  rows. Workshop PDFs enter only where individually linkable and substantive.
- Claiming that ISO 26262, ARP4761A, or IEC 61508 mandate STPA. They are
  functional-safety context; the list prose must not assert a mandate without a
  verified primary quote.
- Re-hosting any PDF or content. The list links canonical sources only.
- Companion docs site, CITATION.cff, stale.yml workflow, GitHub issue forms, and
  the sindresorhus/awesome submission. All are post-v1 (see Deferred).
- Duplicating STPA entries into the hub README. The hub keeps no STPA section.

## Constraints

Locked by the user, FAMILY.md, or the gates:

1. **FAMILY.md is normative.** `awesome-sysml-v2` is a file/CI skeleton only. The
   documented sysml drift must not be copied: entry format needs tags plus year,
   the filename is `CONTRIBUTING.md` (uppercase), lychee is blocking with
   `--include-fragments=anchor-only`, the README carries the Last full sweep
   badge and family pointer, and license attribution is CC0 throughout (the
   sysml CITATION.cff says MIT; this repo ships no CITATION.cff).
2. **License CC0-1.0** (FAMILY files rule).
3. **Owner and namespace:** `jgsystemsconsulting/awesome-stpa`, re-checked the
   day the remote is created (FAMILY.md Registry namespace rule + External lists
   and namespaces table, awesome-stpa row).
4. **Local path:** sibling clone at `C:\Users\gower\OneDrive\Documents\GitHub\awesome-stpa`,
   next to `awesome-mbse` and `awesome-sysml-v2`.
5. **Visibility:** FAMILY Private mode is default. Create the GitHub repo
   **private** first (FAMILY Starting a new list / awesome-stpa checklist).
   Entry URLs remain public-availability resources. Public release of the spoke
   is a later explicit step (matches awesome-sysml-v2 once Live+public); v1
   acceptance may complete while the spoke is still private if the maintainer
   can verify CI.
6. **Entry format:** `- [Name](url) - Description `tags` (YYYY).`, hyphen
   separator, description at most 140 characters, tags as inline code spans
   before the terminal period, year as the last token (FAMILY.md Shared
   standard, Entry format bullet).
7. **Ported rules:** hub CONTRIBUTING.md section 5 (year rule) and section 6
   (canonical-URL rule) copied verbatim into the spoke CONTRIBUTING.md
   (FAMILY.md Shared standard, Year rule and canonical-URL bullets). Editorial
   neutrality ported and adapted.
8. **Family pointer while hub private:** text only, no `FAMILY.md` hyperlink
   from the spoke (FAMILY.md Private mode). Match awesome-sysml-v2:
   `Part of the awesome-mbse list family (hub repository currently private).`
9. **Superpowers full mode implements after reviews.** This spec does not write
   the plan.

## Recommended approach

Create a new sibling repo `jgsystemsconsulting/awesome-stpa` (private first per
FAMILY Private mode; public optional later) and apply hub registry/README edits
in the same program of work, hub edits last.

Why a sibling repo and not a hub section: the depth bar and namespace rules
(FAMILY.md Model, spoke-earns-repo bullets) are satisfied, the registry and
scope table already name a separate repo, and the hub-and-spoke model gives the
niche room to grow past what the hub would carry.

Why not a folder inside the awesome-mbse repo: it would break the one-repo-per-
spoke registry model, share CI and issue queues with the hub, and contradict
the scope table.

Order of work: skeleton and required files first, then entry population with a
live-link pass, then CI green on main, then hub edits (the registry Status
column needs the live URL, and FAMILY requires a same-day namespace re-check).

## Deliverable shape and v1 file set

New GitHub repo, created **private** first. Default branch `main`. Repo
description: "Curated list of STAMP/STPA and hazard analysis resources". Topics:
`stpa`, `stamp`, `safety`, `hazard-analysis`, `awesome-list`, `awesome`.

| File | Content and notes |
|------|-------------------|
| `README.md` | FAMILY skeleton: H1 with Awesome badge, one-line scope, Last full sweep badge dated to the real ship month, family pointer **text only while hub is private** (sysml-v2 wording), maintainer line with neutrality pointer, flat hand-maintained `## Contents` (ToC only, not one of the seven content sections), then the seven sections below. When the hub later goes public, upgrade the pointer to a FAMILY.md hyperlink in a follow-on change. |
| `LICENSE` | CC0-1.0 full legal text. |
| `CONTRIBUTING.md` | Uppercase filename. Sections: how to suggest (PR path in v1), inclusion bar (on-topic STAMP/STPA/CAST/hazard analysis; substantive not stub or pure marketing; live at ship; not duplicative; legally linkable; no re-host), entry format, tag vocabulary with cardinality and order, year rule (copy hub CONTRIBUTING.md section 5 verbatim at execute), canonical-URL rule (copy hub CONTRIBUTING.md section 6 verbatim, with PSAS `get_file.php?name=` called out as semantically required query strings), editorial neutrality, local link-check (`lychee` same args as link-check-pr on README.md), maintenance cadence, known-rot appendix. |
| `CODE_OF_CONDUCT.md` | Contributor Covenant, ported from hub. |
| `SECURITY.md` | Ported from hub, repo name adjusted. |
| `CHANGELOG.md` | Initial release entry dated to the real ship day; first full sweep month matches the README badge. |
| `NOTICE` | The hub carries one, so this repo does too, adapted: CC0 waiver, linked resources are the property of their owners and referenced not redistributed, nominative use of method names. No Dassault/OMG trademark text is needed here. |
| `.gitignore` | Minimal OS and editor entries. |
| `.lycheeignore` | Ships comment-only with the ignore policy written in comments; entries appear only when a browser-verifiable canonical URL fails CI (see Seed entry set). |
| `.markdownlint-cli2.jsonc` | Copied from `awesome-sysml-v2`, globs updated to `README.md` and `CONTRIBUTING.md` (uppercase). |
| `.github/workflows/link-check-pr.yml` | Triggers: `pull_request` and `push` to `main`. Blocking: lychee with `--include-fragments=anchor-only`, `--max-retries 3`, `--accept 200..=299,429`, `--max-concurrency 4`, README.md, `fail: true`, token passed so github.com links check authenticated. Pin every action ref to a full commit SHA (stricter than current hub, which still floats `actions/checkout@v4` and only SHA-pins lychee-action; matches the sysml-v2 pin discipline). |
| `.github/workflows/link-check-schedule.yml` | Triggers: weekly cron only (no push). Advisory: same lychee args, `fail: false`. Match hub `link-check-schedule.yml`: open or replace a "Weekly link-rot report" issue labeled `link-rot` (not the sysml-v2 "Link Checker Report" / `report`+`broken-links` labels). |
| `.github/workflows/lint.yml` | Triggers: `pull_request` and `push` to `main`. awesome-lint plus markdownlint-cli2; every action SHA-pinned; node 20. |
| `.github/PULL_REQUEST_TEMPLATE.md` | Short checklist: entry format, tags from vocabulary, year token, canonical-URL dedupe, link resolves. |

Deferred past v1 (each has a cheap upgrade path): `CITATION.cff` (would ship
with CC0, never MIT), `docs/` companion site, `stale.yml`, issue forms, social
card, sindresorhus/awesome submission (FAMILY step 6, once the list is stable).

## README sections

Seven top-level sections, flat ToC, in this order:

1. **Foundations & Handbooks**: STPA Handbook (Leveson & Thomas), CAST
   Handbook, Engineering a Safer World (MIT Press OA canonical URL),
   Introduction to System Safety Engineering, PSAS home, books-and-handbooks,
   materials, and publications indexes.
2. **Tools**: open source first: XSTAMPP, MicroSTAMP, PASTA (VS Code extension
   and source), stpa-capella, CAIRIS with its STPA docs, the STPA
   safety-based testing plugin. Then commercial: TRACEIT, VisualPro SA, RM
   Studio STPA, STPAmaster, Depict. Section intro notes that the PSAS
   stamp-tools catalog is linked as an awareness list, not an endorsement.
3. **Standards & Guidance**: ISO 26262 catalog page and SAE ARP4761A as the v1
   standards seed (both have catalog URLs in the research gate). SAE J3187 and
   AIR6913 stay in the tag vocabulary and may enter only after execute verifies
   a live SAE catalog URL; Capella STPA README names them but does not supply
   those URLs. Section prose states these documents are functional-safety
   assessment context where STPA is used or discussed; it does not claim any of
   them mandates STPA.
4. **Case Studies & Agency Reports**: FAA STPA aviation-safety evaluation
   (ROSAP PDF), the 2026 FAA eVTOL STPA test case at
   `https://psas.scripts.mit.edu/home/wp-content/uploads/2026/2026-03-24-1340__Adopting_STPA_Within_the_FAA__an_eVTOL_Test_C__PUB.pdf`
   (re-verify at ship), Network Rail STPA work, a healthcare CAST adverse-event
   case, the MIT STAMP workshop presentations archive.
5. **Learning & Workshops**: MIT STAMP workshop tutorials, PSAS online
   education, STAMP Institute training, STAMP workshop information pages.
6. **Datasets & Examples**: train-gate STPA control example, stpa-step1-dataset,
   triarchsecurity/stpa (STPA for threat modeling), anvil-safety-framework,
   ease-2026 replication package, gaphor (RAAML/STPA-adjacent).
7. **Related lists**: three full-format entries: awesome-mbse hub GitHub URL
   (works for org members while hub private; outside readers may 404 until hub
   is public, acceptable under Private mode), awesome-sysml-v2, sindresorhus/awesome.
   Do not hyperlink FAMILY.md from this section while hub is private. Type tag
   `list`. Language tag `STAMP-general`. No duplicated entry bodies.

## Entry format and tag vocabulary

Entry format is the FAMILY line with STPA tag values. Tag order is fixed and
matches the hub axes: `language -> method -> tool -> has-model -> type ->
spec/standard -> paid -> year`.

| Axis | Cardinality | STPA values |
|------|-------------|-------------|
| language | exactly 1 | Method family (no modeling language in this niche): `STPA` (process analysis primary), `CAST` (accident analysis primary), `STPA-Sec` (security/threat-model primary), `STAMP-general` (methodology-wide books, hubs, related lists, multi-method platforms, standards context). Multi-method tools use primary method or `STAMP-general`. |
| method | 0 or 1 | Companion technique when the resource couples them: `HARA`, `FTA`, `FMEA`, `HazOp` |
| tool | 0 or more | `XSTAMPP`, `PASTA`, `stpa-capella`, `MicroSTAMP`, `CAIRIS`, `other-tool` (graduates to its own tag at 3+ entries, hub rule). Required when `has-model` is present. |
| has-model | 0 or 1 | Token value is the literal tag `has-model`. Same bar as hub: directly downloadable, non-paywalled STPA case or example that opens in a named tool. |
| type | exactly 1 | `handbook`, `book`, `paper`, `standard`, `tool`, `course`, `video`, `case`, `dataset`, `workshop`, `list` |
| spec/standard | 0 or 1 | `ISO-26262`, `ARP4761A`, `IEC-61508`, `J3187`, `AIR6913` (entry is tied to that normative document) |
| paid | 0 or 1 | `paid` when the linked URL's primary artifact requires purchase or paid account. Free catalog/landing pages of paywalled standards are not `paid`. |
| year | exactly 1 | `(YYYY)` per the ported hub year rule |

No `domain` tag. Research SC4 proposed `domain` values (`aerospace`, `automotive`,
and so on); FAMILY requires the same axes as the hub, so domain stays in the
description prose only. With 40-60 entries a domain filter is not needed.

Worked examples (years are illustrative placeholders; execute fills real
publication years from the research inventory and primary pages):

```markdown
- [STPA Handbook](https://psas.scripts.mit.edu/home/get_file.php?name=STPA_Handbook.pdf) - Free process handbook for System-Theoretic Process Analysis by Leveson and Thomas `STPA` `handbook` (2018).
- [XSTAMPP](https://github.com/SE-Stuttgart/XSTAMPP) - Open-source Eclipse-based STAMP platform supporting STPA and CAST analyses `STPA` `XSTAMPP` `tool` (2024).
- [Engineering a Safer World](https://direct.mit.edu/books/oa-monograph/2908/Engineering-a-Safer-WorldSystems-Thinking-Applied) - Leveson's open-access foundations of STAMP systems thinking `STAMP-general` `book` (2011).
```

## Seed entry set and live-link bar

- Ship v1 with at least 40 full-format entries. Primary pool: the research
  inventory (~42 candidates) plus Related lists (3) and any extra live PSAS
  index or workshop-case URLs that clear the bar at ship (attrition buffer).
  Dropped for rot, marketing-only, or failed live-link do not count. Soft
  section targets (not hard quotas): foundations 8–10, tools 12–15, standards
  2 (ISO 26262 + ARP4761A; J3187/AIR6913 only if URLs verify), cases 5–7,
  learning 6–8, datasets 4–6, related lists 3.
- Canonical URLs: the PSAS `get_file.php?name=...` query strings are
  semantically required and survive the canonical-URL dedupe rule, which drops
  query strings "unless they're semantically required". Call this out in the
  spoke CONTRIBUTING dedupe section.
- 403-prone canonical URLs: Engineering a Safer World keeps the MIT Press
  open-access URL even when some automated fetchers get 403. Policy: if lychee
  reports 403 on a URL that resolves in a browser, add the exact URL to
  `.lycheeignore` with a dated comment naming the manual verification method.
  This is the only sanctioned ignore use.
- Quarantine (known-rot appendix in CONTRIBUTING.md, seeded from the research
  exclusion list): sunnyday.mit.edu and handbook mirrors (timeouts),
  stamp-workshop.mit.edu and stamp-workshop.org (DNS), sahra.ch (parked),
  safetbox.de (TLS, recheck before listing), SafetyHAT/Volpe (host timeouts,
  landing 403), SpecTRM at safeware-eng.com (expired certificate), MathWorks
  File Exchange STPA tool (403 from some clients). Each row carries host,
  reason, date, and recheck condition. Quarantined hosts are never shipped as
  live entries and are not added without a passing recheck.
- Workshop presentations: individual entries only where a PDF has a stable URL
  and case-study substance. No bulk slide rows.

## Hub go-live edits

Applied after the spoke's CI is green on main, as the closing change set of the
same program of work:

1. Re-check the `awesome-stpa` GitHub namespace that day (FAMILY External lists
   and namespaces table).
2. FAMILY.md registry row: `awesome-stpa` Status Planned becomes Live; Visibility
   set to `private` (or `public` if intentionally released the same day); URL in
   the Repo column when linkable.
3. Hub README: family pointer / spoke table updated per current hub chrome so
   both live spokes are named near the top (FAMILY Model: hub links every spoke
   near the top). While hub is private this is for maintainers.
4. Tick the FAMILY.md awesome-stpa checklist items that this work completes.
5. Scope-boundary row stays as-is; it already routes correctly.
6. No STPA entries are copied into the hub README beyond any pre-existing
   cross-cutting Model Gallery mention FAMILY already notes.

## Editorial neutrality for this niche

JG Systems Consulting sells SysML/Cameo tooling. It has no STPA, CAST, or
hazard-analysis product. The spoke's neutrality section states that plainly,
then ports the hub rules so they bind if that ever changes: any future JGS
entry meets the same inclusion bar, sits next to at least one genuine
competing entry, and lists below a superior competitor. The Tools section intro
additionally notes that the PSAS stamp-tools catalog is an awareness list, not
an endorsement, and that commercial entries must clear the same "not pure
vendor marketing" bar, linking product documentation with substance rather
than landing pages alone.

## Acceptance criteria

1. Repo `jgsystemsconsulting/awesome-stpa` exists under the org, default branch
   `main`, created private per FAMILY Private mode, with the v1 file set above
   present at the repo root. Making the spoke public is optional in the same
   program of work and is recorded in the FAMILY Visibility cell.
2. `CONTRIBUTING.md` exists with uppercase filename; contains the hub year rule
   and canonical-URL rule verbatim (including the PSAS query-string callout),
   the STPA tag vocabulary with cardinalities in the fixed order, the inclusion
   bar, the neutrality statement, and the known-rot appendix.
3. `LICENSE` is CC0-1.0. No MIT *license* text or MIT license metadata anywhere
   in the repo. Nominative use of MIT (PSAS, MIT Press, workshops) in README
   entry names and descriptions is required and allowed.
4. README contains the Awesome badge, a one-line scope statement, a Last full
   sweep badge for the real ship month, the family pointer as **text only** while
   the hub is private (no FAMILY.md hyperlink), the maintainer line with
   neutrality pointer, and a flat `## Contents` ToC whose anchors all resolve.
5. README has exactly the seven content sections listed above (Foundations
   through Related lists); `## Contents` is ToC chrome only. The ToC lists
   exactly those seven.
6. Every list entry (including Related lists) matches
   `- [Name](url) - description `tags` (YYYY).` with hyphen separator,
   description at most 140 characters, exactly one language tag and exactly one
   type tag from the vocabulary, remaining tags only from the vocabulary in axis
   order, year as the last token. Format is enforced by PR template checklist
   plus maintainer review in v1 (no separate format-lint script required).
7. At least 40 full-format entries ship. Every entry URL either (a) passes
   lychee on main with the blocking PR configuration (`fail: true`,
   `--include-fragments=anchor-only`) or (b) is listed in `.lycheeignore` with a
   dated comment and browser-verification note under the sanctioned 403 policy.
   Quarantined hosts never appear as live entry URLs.
8. CI: link-check-pr.yml on `pull_request` and `push` to main blocks dead links
   and bad anchors; link-check-schedule.yml is cron-only weekly and opens or
   updates a `link-rot` report issue; lint.yml on `pull_request` and `push` runs
   awesome-lint and markdownlint on README.md and CONTRIBUTING.md. All action
   refs pinned to full commit SHAs.
9. On the initial main push, link-check-pr.yml and lint.yml complete
   successfully. Schedule workflow is not required to run on that push.
10. No entry text claims ISO 26262, ARP4761A, or IEC 61508 mandates STPA; the
    Standards section prose carries the context-not-mandate sentence.
11. No entry re-hosts content; every link points at a canonical source.
12. No quarantined host appears as a live entry URL.
13. Hub edits land only after the spoke repo exists and the push workflows in AC9
    are green: FAMILY.md registry row is Live with correct Visibility, hub README
    names both live spokes near the family pointer, and the hub does not gain a
    duplicated STPA entry section.
14. CHANGELOG has the initial release entry with the sweep date; the Last full
    sweep badge matches it.

## Risks

- **MIT host flakiness.** Prefer `psas.scripts.mit.edu` for handbook and case
  PDFs. Research timed out on `sunnyday.mit.edu` (and related handbook mirrors),
  not on the PSAS catalog itself. Mitigation: lychee `--max-retries 3`, accept
  429, the dated `.lycheeignore` policy for browser-verifiable URLs, and the
  known-rot appendix for genuinely dead hosts (`sunnyday.mit.edu`, old workshop
  DNS, parked tool sites).
- **Paywalled standard pages.** iso.org and SAE pages can reject automated
  fetches. Link catalog pages, not PDFs; apply the same 403 policy.
- **Commercial tool marketing drift.** RM Studio, STPAmaster, and Depict pages
  may read as marketing. Enforce the inclusion bar by linking documentation or
  method pages with substance; drop entries that cannot clear it.
- **awesome-lint strictness.** The FAMILY skeleton is already conformant
  (single H1, badge, one-line scope); keeping the ToC flat and hand-maintained
  avoids the doctoc problem the hub documented.
- **Maintenance cadence.** A new repo adds a quarterly sweep obligation. The
  badge and CHANGELOG cadence, plus the six-month lapsed rule, carry over from
  FAMILY; the hub sweep schedule should absorb this spoke in the same quarter.
- **Sequencing.** Hub registry flip before the spoke is live would point at a
  dead URL. The order of work fixes hub edits last.

## Open questions

None blocking. Items the plan settles mechanically: `gh repo create` invocation
and auth path for `jgsystemsconsulting`; exact publication years for each seed
entry taken from the research inventory at execute; optional J3187 and AIR6913
entries only after a live SAE catalog URL is verified (not required for the
≥40 count).

## Research

Gate files:

- research: docs/superpowers/research/2026-09-17-awesome-stpa-sources-research.md
  (namespace check SC1, 42-candidate inventory SC2, skeleton SC3, tag values SC4,
  exclusion list; retrieved 2026-09-17)
- context: docs/superpowers/context/2026-09-17-awesome-stpa-pattern-context.md
  (FAMILY normative findings, sysml-v2 drift list, hub go-live pattern,
  CONTRIBUTING port targets; HEAD 4f7c0a63 at gate start)

Primary sources cited in the inventory:

- https://psas.scripts.mit.edu/home/
- https://psas.scripts.mit.edu/home/stamp-tools/
- https://psas.scripts.mit.edu/home/get_file.php?name=STPA_Handbook.pdf
- https://direct.mit.edu/books/oa-monograph/2908/Engineering-a-Safer-WorldSystems-Thinking-Applied
- https://github.com/SE-Stuttgart/XSTAMPP
- https://github.com/Micro-STAMP/microstamp
- https://github.com/kieler/pasta
- https://github.com/labs4capella/stpa-capella
- https://www.sae.org/standards/content/arp4761a/
- https://www.iso.org/standard/68383.html
- https://rosap.ntl.bts.gov/view/dot/78914/dot_78914_DS1.pdf
- https://github.com/sindresorhus/awesome
- https://awesome.re/badge.svg

## Codebase context

FAMILY.md is the constitution: Private mode (text-only family pointer while hub
private), Registry table (awesome-stpa Planned row), Scope boundaries
(STAMP/STPA route), Shared standard, Starting a new list / awesome-stpa
checklist. Hub CONTRIBUTING.md sections 5 to 7 are the verbatim port source for
year, dedupe, and neutrality. The hub PR lychee workflow
(`.github/workflows/link-check-pr.yml`) is the blocking CI reference: fragments
anchor-only, accept 200..299 and 429, `fail: true`, authenticated token. The
sibling `awesome-sysml-v2` repo supplies the skeleton shape (README,
CONTRIBUTING, CoC, SECURITY, CHANGELOG, LICENSE, docs/, three workflows,
markdownlint config) and the drift list this spec fixes: bare entries without
tags or years, lowercase contributing.md, advisory lychee without fragments,
missing sweep badge, absolute FAMILY hyperlink while hub private, MIT/CC0 mismatch in
CITATION.cff. Prior spoke specs (awesome-archimate, awesome-capella,
awesome-requirements-engineering, awesome-digital-engineering) live in
`docs/superpowers/specs/` beside this file and establish the house format.
