# Context: awesome-capella from family pattern

## Context brief

**Primary question:** What workspace patterns must a new `awesome-capella` spoke repo copy from `awesome-mbse` (hub) and `awesome-sysml-v2` (live spoke) so it meets the family shared standard?

**Sub-questions:**
1. What files and README shape does every family list require (FAMILY.md shared standard)?
2. What does the live spoke `awesome-sysml-v2` actually ship (CI, CONTRIBUTING, entry format, badges)?
3. What does FAMILY.md already lock for `awesome-capella` scope and registry status?
4. Where should the new repo live relative to this workspace, and what hub updates are in-scope vs out?
5. Does the hub entry format (tags + year) or the simpler sysml-v2 format win for Capella?

**Success criteria (design work must know):**
- S1: Exact shared-standard file set and README must-haves from FAMILY.md
- S2: Spoke entry format, tag axes, year/dedupe/neutrality rules location
- S3: CI pattern used by awesome-sysml-v2 and/or hub (workflows, lychee flags, lint)
- S4: awesome-capella registry row and scope boundary text already written
- S5: Whether hub FAMILY/README updates are required when the spoke goes live
- S6: Intended on-disk location of the new repo (sibling path)

**Out of scope:** Capella world facts (research gate); writing the new repo contents (execute); inventing a different family standard.

**Budget:** light tier, 1 round preferred.

**Workspace baseline:** porcelain sha256 `0933b130d260f82993853e7b62552af5ff0dccda8cd3a8192496cf60092999d2`; HEAD `4f7c0a63eb84e8ca29db1e565918a021e818cff3` (informational).

## Findings

All decision-bearing claims below are **SINGLE-SOURCE** (doc/config family; no runtime code). That is expected for list-family standards.

- **S1.** Every family repo must have: README.md (Awesome badge, one-line scope, Last full sweep badge, family pointer, flat ToC), LICENSE CC0-1.0, CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md, CHANGELOG.md. Loc: FAMILY.md shared-standard and README skeleton sections.
- **S2.** Entry format is hub/FAMILY form, not sysml-v2 form:
  `- [Resource Name](url) - One-line factual description \`tags\` (YYYY).`
  Copy hub CONTRIBUTING year rule (§5), canonical-URL dedupe (§6), and editorial neutrality (§7) into the spoke. Tag axes same as hub with Capella-specific values. **Do not** clone awesome-sysml-v2's untagged `- [Name](URL) - Description.` format.
- **S3.** FAMILY CI triad: lychee on every PR + scheduled sweep with `--include-fragments=anchor-only`, markdown lint, awesome-lint. Hub implements strict lychee+fragments; sysml-v2 implements markdownlint+awesome-lint and advisory lychee without fragments. New spoke should implement the full triad (hub lychee flags + sysml lint jobs), not a pure clone of either.
- **S4.** Registry row and scope already exist: `awesome-capella | Capella tool and the Arcadia method | Planned. Namespace empty as of 2026-09`. Scope table: Capella workbenches, Arcadia method material → awesome-capella.
- **S5.** Go-live hub work: flip registry Status to Live; add spoke link near top of hub README; shrink hub Capella/Arcadia section to pointer + cross-cutting only (hub still lists Arcadia method entry today). Registry row text already present (no invent-scope step).
- **S6.** On-disk convention: sibling of hub at `../awesome-capella` (same parent as awesome-sysml-v2). FAMILY.md does not lock filesystem path; only GitHub namespace check. CONTRIBUTING filename: prefer `CONTRIBUTING.md` (FAMILY/hub), not lowercase `contributing.md` (sysml-v2), unless CI globs force otherwise—then pin the path CI uses.

## Synthesis

**Clone target is FAMILY.md + hub CONTRIBUTING/README shape, with CI assembled to the FAMILY triad.** awesome-sysml-v2 is a live spoke existence proof and a partial CI/lint reference, not the editorial template. User ask "similar way to awesome-sysml-v2" means family spoke workflow and repo creation, not its divergent untagged entry format.

Build path: create sibling repo `awesome-capella` under jgsystemsconsulting; seed README to FAMILY skeleton with Capella sections; port hub year/dedupe/neutrality; wire full CI triad; populate from research seeds; then hub Status flip + README spoke link + Capella section shrink. Until ≥40 inclusion-bar entries land, Status can remain Planned.

## Evidence index

| loc | kind |
|-----|------|
| FAMILY.md:1 (hub model) | doc |
| FAMILY.md:39 (capella registry) | doc |
| FAMILY.md:56 (scope boundary) | doc |
| FAMILY.md:68–88 (shared standard) | doc |
| FAMILY.md:73 (entry format) | doc |
| FAMILY.md:81 (year/dedupe copy) | doc |
| FAMILY.md:95–105 (starting a new list) | doc |
| FAMILY.md:108+ (README skeleton) | doc |
| CONTRIBUTING.md §3–7 (hub entry/tags/year/dedupe/neutrality) | doc |
| README.md (hub tags+year examples; family pointer; Arcadia entry) | doc |
| .github/workflows/link-check-pr.yml (fragments anchor-only) | config |
| ../awesome-sysml-v2/README.md | doc |
| ../awesome-sysml-v2/contributing.md | doc |
| ../awesome-sysml-v2/.github/workflows/links.yml | config |
| ../awesome-sysml-v2/.github/workflows/lint.yml | config |
