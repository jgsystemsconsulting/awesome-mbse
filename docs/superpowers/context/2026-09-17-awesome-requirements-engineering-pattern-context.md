# Context: awesome-requirements-engineering spoke pattern

## Context brief

**Primary question:** How does this workspace (awesome-mbse hub) and the sibling
template `awesome-sysml-v2` define the pattern for creating a new family spoke
`awesome-requirements-engineering`?

**Sub-questions:**

1. What files and CI shape must every family spoke ship (FAMILY.md shared standard +
   sysml-v2 as the live spoke exemplar)?
2. What entry-format, tag, year, dedupe, and neutrality rules must be copied from the
   hub CONTRIBUTING.md versus what awesome-sysml-v2 simplified?
3. What hub-side updates (FAMILY.md registry status, hub README spoke link) happen
   after the spoke is live?
4. Where should the new git repo live relative to this workspace (sibling clone vs
   inside hub)?
5. What is already planned for `awesome-requirements-engineering` in FAMILY.md?

**Success criteria (decision-bearing):**

- SC1: Required file set for a spoke is listed with evidence locs from FAMILY.md
  and/or awesome-sysml-v2.
- SC2: CI expectations (lychee, markdownlint, awesome-lint, schedules) are stated
  with evidence.
- SC3: Entry format and tag/year/dedupe/neutrality source-of-truth paths are named
  (hub CONTRIBUTING sections vs sysml-v2 contributing).
- SC4: Hub registry/README update steps after go-live are stated from FAMILY.md
  Starting a new list.
- SC5: New-repo location decision (sibling under org, not nested in hub) is supported
  by family model text and existing sibling layout.
- SC6: Current FAMILY.md status/scope row for awesome-requirements-engineering is
  quoted.

**Out of scope:**

- Authoring the spoke README body (spec/plan/execute).
- External world facts about RE resources (research-loop).
- Creating GitHub remote (execute step).

**Budget:** up to 3 context rounds; lenses may read hub and `../awesome-sysml-v2`.

**Workspace baseline:**

- HEAD: `4f7c0a63eb84e8ca29db1e565918a021e818cff3`
- porcelain sha256: `0933b130d260f82993853e7b62552af5ff0dccda8cd3a8192496cf60092999d2`
- Date: 2026-09-17

## Findings

1. **Shared standard / required files (SC1).** FAMILY.md states every family repo
   ships README.md (Awesome badge, one-line scope, Last full sweep badge, family
   pointer, flat ToC), entry format with tags and year, inclusion bar, tag vocabulary
   axes, year and canonical-URL rules from hub CONTRIBUTING §§5–6, editorial
   neutrality, and files LICENSE (CC0-1.0), CONTRIBUTING.md, CODE_OF_CONDUCT.md,
   SECURITY.md, CHANGELOG.md, plus CI. (`FAMILY.md` shared standard section.)

2. **Registry row already planned (SC6).**  
   `| awesome-requirements-engineering | Requirements as a discipline: EARS, KAOS, ReqIF, tooling, papers | Planned. Namespace empty as of 2026-09 |`  
   Scope boundary: “Requirements elicitation and management as its own discipline”
   homes here. (`FAMILY.md` registry and scope tables.)

3. **Entry format SoT is hub, not sysml-v2 (SC3).** FAMILY mandates  
   `- [Resource Name](url) - One-line factual description `tags` (YYYY).`  
   Hub CONTRIBUTING.md defines hyphen separator, ≤140 char description, tag order
   `language → method → tool → has-model → type → spec/standard → paid → year`, year
   rule, canonical-URL dedupe, neutrality. awesome-sysml-v2 `contributing.md` and
   README use untagged `- [Name](URL) - Description.` and omit Last full sweep / family
   pointer. **New spoke follows FAMILY + hub CONTRIBUTING; do not copy sysml untagged
   format.**

4. **CI (SC2).** FAMILY requires link check on every PR plus scheduled sweep (lychee
   `--include-fragments anchor-only`), markdown lint, awesome-lint. Hub
   `link-check-pr.yml` uses `fail: true`. awesome-sysml-v2 `links.yml` uses
   `fail: false` (advisory) and ships `.markdownlint-cli2.jsonc` + lint.yml + stale.yml.
   Hub under-implements markdownlint relative to FAMILY. **New spoke: blocking lychee
   on PR (hub), markdownlint + awesome-lint (sysml shape), scheduled sweep.**

5. **File casing.** FAMILY names `CONTRIBUTING.md`; sysml-v2 uses `contributing.md`.
   Prefer `CONTRIBUTING.md`.

6. **Starting a new list (SC4).** Steps: namespace check → ~40 candidates → create from
   skeleton → populate + CI → add registry row + hub README spoke link → later
   sindresorhus submission via sysml-v2 runbook. Registry/README hub updates are
   **after** go-live (step 5), not before empty remote.

7. **Location (SC5).** One hub, many spoke **repos**. Live exemplar is
   `https://github.com/jgsystemsconsulting/awesome-sysml-v2` as a sibling checkout
   (`../awesome-sysml-v2`). Do not nest the RE list inside the hub tree.

8. **Reuse analogs.** Copy structure from sysml-v2 workflows/PR template/CITATION
   carefully, then re-align to FAMILY. Hub LICENSE CC0, SECURITY (malicious-link
   reporting), CODE_OF_CONDUCT, CHANGELOG patterns. sysml-v2
   `docs/superpowers/runbooks/awesome-submission.md` is post-stable, out of MVP if
   needed. **Do not reuse** `docs/superpowers/*awesome-archimate*` artifacts as this
   stem’s sources.

9. **LICENSE.** Both hub and sysml-v2 are CC0-1.0; not a fork point.

## Synthesis

Decision-bearing answers for the RE spoke:

| Need | Decision | Evidence |
|------|----------|----------|
| Where to create | Sibling repo `jgsystemsconsulting/awesome-requirements-engineering` beside hub | FAMILY registry model; `../awesome-sysml-v2` |
| Status today | Planned; namespace empty | FAMILY.md:40 |
| README shape | FAMILY skeleton (badges + family pointer + flat ToC) | FAMILY.md README skeleton |
| Entry lines | Hub tagged format + year; RE-adapted tag values in CONTRIBUTING | FAMILY + hub CONTRIBUTING |
| CONTRIBUTING name | `CONTRIBUTING.md` | FAMILY file list |
| CI | PR lychee fail true + schedule; awesome-lint; markdownlint config | FAMILY + hub PR workflow + sysml markdownlint |
| When to touch hub | After spoke live: registry Status=Live, README family link | FAMILY step 5 |
| Template caution | sysml-v2 is structural CI/files analog only; format is non-conformant to FAMILY | skeptic findings |
| Stem isolation | Not archimate | separate context/research files |

All SC1–SC6 met. Grades are largely SINGLE-SOURCE doc/config (no application `code` in a docs repo); named as such in the log. No unresolved CONFLICTED facts about the hub; sysml vs FAMILY is a design constraint resolved toward FAMILY.

## Evidence index

| loc | kind |
|-----|------|
| FAMILY.md:9-105 (model, standard, starting list) | doc |
| FAMILY.md:40,57 (RE registry + scope) | doc |
| FAMILY.md:68-89 (shared standard, CI, files) | doc |
| FAMILY.md:93-105 (starting a new list) | doc |
| FAMILY.md:108+ (README skeleton) | doc |
| CONTRIBUTING.md:33+ (entry format, tags, year, dedupe, neutrality) | doc |
| .github/workflows/link-check-pr.yml (fail: true, lychee, awesome-lint) | config |
| .github/PULL_REQUEST_TEMPLATE.md | doc |
| LICENSE (CC0) | doc |
| ../awesome-sysml-v2/contributing.md (untagged format) | doc |
| ../awesome-sysml-v2/README.md (untagged entries, missing sweep badge) | doc |
| ../awesome-sysml-v2/.github/workflows/links.yml (fail: false) | config |
| ../awesome-sysml-v2/.github/workflows/lint.yml | config |
| ../awesome-sysml-v2/.markdownlint-cli2.jsonc | config |
| ../awesome-sysml-v2/docs/superpowers/runbooks/awesome-submission.md | doc |
| docs/superpowers/context/2026-09-17-awesome-archimate-pattern-context.md | doc (wrong stem) |
