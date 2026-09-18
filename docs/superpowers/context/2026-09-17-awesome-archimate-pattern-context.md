# Context: awesome-archimate from family pattern

## Context brief

**Primary question:** What workspace patterns must a new `awesome-archimate` spoke repo copy from `awesome-mbse` (hub) and `awesome-sysml-v2` (live spoke) so it meets the family shared standard?

**Sub-questions:**
1. What files and README shape does every family list require (FAMILY.md shared standard)?
2. What does the live spoke `awesome-sysml-v2` actually ship (CI, CONTRIBUTING, entry format, badges)?
3. What does FAMILY.md already lock for `awesome-archimate` scope and registry status?
4. Where should the new repo live relative to this workspace, and what hub updates are in-scope vs out?

**Success criteria (design work must know):**
- S1: Exact shared-standard file set and README must-haves from FAMILY.md
- S2: Spoke entry format, tag axes, year/dedupe/neutrality rules location
- S3: CI pattern used by awesome-sysml-v2 (workflows, lychee flags, lint)
- S4: awesome-archimate registry row and scope boundary text already written
- S5: Whether hub FAMILY/README updates are required when the spoke goes live

**Out of scope:** ArchiMate world facts (research gate); writing the new repo contents (execute); inventing a different family standard.

**Budget:** light tier, 1 round preferred.

**Workspace baseline:** porcelain sha256 `3dde6c9dc2faf6309d45ddcbd0e059d02c898dab290edb9dc9ad884eab666f44`, HEAD `325918717bd8fd82bd602f67a06128dc8d11f7f8` (gate start).

## Findings

1. FAMILY shared standard is normative for every spoke: Awesome badge, one-line scope, Last full sweep badge, family pointer, flat ToC; entry line with tags and `(YYYY)`; files LICENSE (CC0-1.0), CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md, CHANGELOG.md; CI lychee (with `--include-fragments` anchor-only), markdownlint, awesome-lint. (FAMILY.md:66-92)
2. Entry format, tag axis order, year rule, canonical-URL dedupe, and editorial neutrality live in hub CONTRIBUTING.md and must be copied into each spoke CONTRIBUTING.md with niche tag values. (CONTRIBUTING.md; FAMILY.md:81-82)
3. Live spoke `awesome-sysml-v2` is a partial template only: three workflows (`links.yml`, `lint.yml`, `stale.yml`), lowercase `contributing.md`, entry format without tags/year, lychee without `--include-fragments`, advisory `fail: false` link check, no sweep badge or family pointer. (sibling repo)
4. Registry already lists `awesome-archimate` as Planned with scope "ArchiMate 3.x, the Archi tool, EA modeling practice"; boundary row routes ArchiMate viewpoints / Archi / TOGAF-aligned modeling to that spoke. (FAMILY.md:38,55)
5. New list is a separate GitHub spoke repo (sibling of hub), not nested under awesome-mbse. Launch steps require registry status update and hub README spoke link (FAMILY "Starting a new list" steps 5-6). Hub README today only points at FAMILY.md, not individual spokes. (FAMILY.md:11,93-105; README.md:20-21)
6. Depth bar (~40+ entries, no incumbent) is maintainer policy, not CI. LICENSE is CC0-1.0 on hub and sysml-v2. (FAMILY.md:25; LICENSE files)

## Synthesis

**Decision for design:** treat FAMILY.md as the contract. Use `awesome-sysml-v2` for layout and CI shape (three workflows, awesome-lint pin, freshness report), then close the gaps to FAMILY: `CONTRIBUTING.md` casing, hub entry format with ArchiMate tag values, sweep + family badges, lychee `--include-fragments=anchor-only`, year/dedupe/neutrality sections.

**S1-S5 coverage:** all met. S3 is met with an explicit CONFLICT framed above: sysml-v2 CI is the structural analog, not a full FAMILY match.

**Open questions:** none blocking. Hub README still lacks per-spoke links; fixing that is part of launch step 5, not a blocker for creating the spoke.

## Evidence index

| loc | kind |
|-----|------|
| FAMILY.md:11 | doc |
| FAMILY.md:16 | doc |
| FAMILY.md:25 | doc |
| FAMILY.md:38 | doc |
| FAMILY.md:55 | doc |
| FAMILY.md:66-92 | doc |
| FAMILY.md:81-82 | doc |
| FAMILY.md:93-105 | doc |
| FAMILY.md:109 | doc |
| README.md:20-21 | doc |
| CONTRIBUTING.md:35 | doc |
| CONTRIBUTING.md:55 | doc |
| CONTRIBUTING.md:73 | doc |
| CONTRIBUTING.md:86 | doc |
| CONTRIBUTING.md:95 | doc |
| .github/workflows/link-check-pr.yml:24 | config |
| .github/PULL_REQUEST_TEMPLATE.md:1 | doc |
| ../awesome-sysml-v2/contributing.md:18 | doc |
| ../awesome-sysml-v2/.github/workflows/links.yml:28-29 | config |
| ../awesome-sysml-v2/.github/workflows/lint.yml | config |
| ../awesome-sysml-v2/.github/workflows/stale.yml | config |
| ../awesome-sysml-v2/README.md:3 | doc |
| ../awesome-sysml-v2/LICENSE:3 | doc |
