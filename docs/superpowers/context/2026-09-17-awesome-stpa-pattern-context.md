# Context: awesome-stpa spoke pattern

## Context brief

**Primary question:** What existing hub and sibling patterns must a new `awesome-stpa` family spoke follow so it matches `awesome-sysml-v2` and `FAMILY.md`?

**Sub-questions:**
1. What does FAMILY.md require to start a new list (namespace, depth bar, skeleton, registry update)?
2. What is the shared standard (README shape, entry format, tags, CI, files)?
3. What is the concrete file/workflow tree of `awesome-sysml-v2` to copy as template?
4. How do hub pointer and scope-boundary rows work when a spoke goes live?
5. What CONTRIBUTING rules must be ported (year, dedupe, neutrality, tags)?

**Success criteria:**
- SC1: FAMILY start checklist and depth bar located with file:line evidence.
- SC2: Shared standard bullets (README, entry format, tags, CI, files) located.
- SC3: `awesome-sysml-v2` root + `.github/workflows` inventory as copy template.
- SC4: Hub registry / scope-boundary / hub-pointer pattern for going live located.
- SC5: CONTRIBUTING port targets (year, dedupe, neutrality, tag axes) located.

**Out of scope:** Writing the STPA resource list itself; GitHub remote creation mechanics beyond what the hub docs already say; ArchiMate spoke work.

**Budget:** 1–3 rounds, full tier.

**Workspace baseline:** HEAD `4f7c0a63eb84e8ca29db1e565918a021e818cff3`; porcelain fingerprint `0933b130d260f82993853e7b62552af5ff0dccda8cd3a8192496cf60092999d2` at gate start.

## Findings

1. **Start checklist (SC1, SINGLE-SOURCE).** `FAMILY.md` section "Starting a new list" (from line 93) requires namespace check, ~40 candidate depth bar, skeleton create, tag vocabulary adapt, port year/dedupe/neutrality from hub CONTRIBUTING, then registry status update when live.
2. **Shared standard (SC2, SINGLE-SOURCE).** `FAMILY.md` "Shared standard" (from line 66): Awesome badge, one-line scope, Last full sweep badge, family pointer, flat TOC; entry format with tags and `(YYYY)`; inclusion bar; tag axes; year and canonical-URL rules; editorial neutrality; required files; CI (lychee with fragments, markdown lint, awesome-lint); quarterly sweep.
3. **Template tree (SC3, SINGLE-SOURCE + config).** Live spoke `../awesome-sysml-v2` has README, contributing.md, CODE_OF_CONDUCT, SECURITY, CHANGELOG, LICENSE, CITATION.cff, docs/ companion site, workflows `links.yml`, `lint.yml`, `stale.yml`.
4. **Go-live hub pattern (SC4, SINGLE-SOURCE).** Registry row already lists `awesome-stpa` as Planned (FAMILY.md:42). Scope boundary table routes STAMP/STPA to awesome-stpa. Hub README currently only links FAMILY.md, not per-spoke URLs (gap vs FAMILY prose that hub links every spoke near the top).
5. **CONTRIBUTING ports (SC5, CORROBORATED).** Port hub `CONTRIBUTING.md` sections 5–7 (year, canonical-URL dedupe, editorial neutrality). Define STPA tag values in spoke CONTRIBUTING. FAMILY points at these rules at lines 81–85.
6. **Do not naive-copy sysml-v2 (CORROBORATED gotchas).**
   - Entry format: FAMILY wants tags + year; sysml-v2 is bare `- [Name](URL) - Description.`
   - Filename: FAMILY says `CONTRIBUTING.md`; sysml-v2 uses `contributing.md` and hard-codes that in lint/PR template.
   - CI: FAMILY + hub PR lychee use blocking `fail:true` and `--include-fragments=anchor-only`; sysml-v2 is advisory `fail:false` without fragments.
   - README chrome: sysml-v2 lacks Last full sweep badge and family pointer line.
   - CITATION.cff on sysml says MIT while LICENSE is CC0; use CC0 consistently.
   - Prefer hub CONTRIBUTING + FAMILY skeleton for content rules; take sysml workflow *shape* then harden to hub lychee strength and include markdownlint + awesome-lint.

## Synthesis

Build `awesome-stpa` as a new sibling repo under `jgsystemsconsulting`, not inside this hub tree as the list body. Use FAMILY.md as the normative standard and hub CONTRIBUTING.md as the rules source. Use awesome-sysml-v2 only as a file/CI skeleton, then fix the documented drift (entry format, CONTRIBUTING casing, blocking lychee + fragments, badges, CC0 citation).

On go-live in the same change set as the spoke: flip FAMILY registry Status to Live with GitHub URL, re-check namespace that day, add hub README spoke link near the family pointer, keep scope-boundary row as-is.

Decision-bearing SINGLE-SOURCE items are acceptable here: they are map facts from the constitution docs themselves. Multi-site CORROBORATED items cover the copy traps that would break a naive sysml clone.

Open for plan/execute (not context gaps): GitHub `gh repo create` target org path; whether companion docs site ships in v1 or later (sysml has `docs/`; FAMILY does not require it).

## Evidence index

| loc | kind |
|-----|------|
| FAMILY.md:33 | doc |
| FAMILY.md:42 | doc |
| FAMILY.md:66 | doc |
| FAMILY.md:81 | doc |
| FAMILY.md:86 | doc |
| FAMILY.md:88 | doc |
| FAMILY.md:93 | doc |
| FAMILY.md:108 | doc |
| CONTRIBUTING.md:71 | doc |
| README.md:20 | doc |
| ../awesome-sysml-v2/README.md:1 | doc |
| ../awesome-sysml-v2/contributing.md:18 | doc |
| ../awesome-sysml-v2/contributing.md:48 | doc |
| ../awesome-sysml-v2/.github/workflows/links.yml:9 | config |
| ../awesome-sysml-v2/.github/workflows/links.yml:28 | config |
| ../awesome-sysml-v2/.github/workflows/lint.yml:35 | config |
| ../awesome-sysml-v2/CITATION.cff:7 | config |
| .github/workflows/link-check-pr.yml:34 | config |
