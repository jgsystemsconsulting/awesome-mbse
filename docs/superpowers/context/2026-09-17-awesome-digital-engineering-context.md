# Context: awesome-digital-engineering family spoke

## Context brief

**Primary question:** How does the awesome-mbse list family create a new spoke repo, and what must awesome-digital-engineering copy vs adapt?

**Success criteria:** SC1 registry+scope; SC2 shared standard; SC3 start checklist; SC4 README skeleton; SC5 CONTRIBUTING port rules; SC6 sysml-v2 layout; SC7 where new repo lives.

**Workspace baseline (Phase 0):** HEAD `4f7c0a63eb84e8ca29db1e565918a021e818cff3`; porcelain hash recorded at gate start. docs/superpowers may be untracked.

## Findings

1. **FAMILY.md is the family constitution.** One hub, many spokes. Registry already lists `awesome-digital-engineering` as Planned with scope "Digital thread, model-based definition, digital engineering transformation" and "Namespace empty as of 2026-09". Scope table routes digital thread, MBD, DE policy and standards to that spoke. SysML v2, Magic Grid, ArchiMate, Capella, RE, STPA, and general MBSE have other homes.

2. **Shared standard (every family repo):** Awesome badge; one-line scope; Last full sweep badge; family pointer to FAMILY.md; flat hand-maintained ToC; entry format with tags and year; inclusion bar; tag axes language/method/tool/has-model/type/spec/standard/paid/year; year + canonical-URL dedupe + editorial neutrality ported from hub CONTRIBUTING; files LICENSE (CC0-1.0), CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md, CHANGELOG.md; CI link-check PR + schedule (lychee `--include-fragments=anchor-only`), markdown lint, awesome-lint; quarterly sweep.

3. **Start checklist (FAMILY):** (1) GitHub namespace check same day; (2) ~40+ candidate entries; (3) create repo from skeleton, adapt tags, port year/dedupe/neutrality; (4) populate + CI; (5) registry row + hub README spoke link; (6) later sindresorhus/awesome submission.

4. **README skeleton** lives in FAMILY.md (lines ~108-128).

5. **Hub CONTRIBUTING.md** is the port source for entry format, tag vocabulary table, year rule, canonical-URL dedupe, editorial neutrality.

6. **Hub CI to copy:** `.github/workflows/link-check-pr.yml`, `link-check-schedule.yml`, `.lycheeignore`, `PULL_REQUEST_TEMPLATE.md`, suggest-resource issue form. Implements lychee + awesome-lint. FAMILY also names markdown lint; hub does not currently run a markdownlint job (known gap).

7. **awesome-sysml-v2 is a live spoke but drifted:** no family pointer, no Last full sweep badge, plain Name/URL/Description without tags/year, lowercase contributing.md, CI links.yml / lint.yml / stale.yml, CITATION.cff still says MIT while LICENSE is CC0. New DE spoke should follow FAMILY + hub patterns, not copy sysml-v2 drift (unless a future family decision grandfathers the old spoke).

8. **Where the repo lives:** separate GitHub repo `https://github.com/jgsystemsconsulting/awesome-digital-engineering` (confirmed empty/404). Local convention beside other clones: `C:\Users\gower\OneDrive\Documents\GitHub\awesome-digital-engineering`. Not a subdirectory of awesome-mbse.

9. **Enforcement:** 40+ entry bar and same-day namespace check are maintainer discipline only (no CI). Registry already has Planned rows before repos exist (including this one).

## Synthesis

**Build target:** new sibling git repository under org `jgsystemsconsulting`, name `awesome-digital-engineering`.

**Normative template:** FAMILY.md shared standard + hub CONTRIBUTING rules + hub CI workflows. Use awesome-sysml-v2 only as a live-spoke existence proof and for section-depth habits, not as the file/format source of truth.

**Hub follow-up (same change set or immediate after):** flip registry Status to Live with URL; add spoke link near top of hub README; optionally shrink any future hub DE section to a pointer.

**Spec must decide:** (a) thin skeleton launch vs block on 40+ seed inventory; (b) whether new spoke CI adds markdownlint to match FAMILY text or matches hub actual (lychee + awesome-lint only); (c) DE-specific tag value vocabulary.

**User wording note:** "awesome archimit" in the ask maps to planned `awesome-archimate` in FAMILY, but the subject line and bullet corpus are digital engineering. This work targets **awesome-digital-engineering**. ArchiMate remains a separate planned spoke.

## Evidence index

| loc | kind |
|-----|------|
| FAMILY.md:9-128 | doc |
| FAMILY.md:41 | doc |
| FAMILY.md:58 | doc |
| CONTRIBUTING.md (hub) | doc |
| NOTICE | doc |
| .github/workflows/link-check-pr.yml | config |
| .github/workflows/link-check-schedule.yml | config |
| ../awesome-sysml-v2/README.md | doc |
| ../awesome-sysml-v2/contributing.md | doc |
| ../awesome-sysml-v2/.github/workflows/* | config |
| gh api repos/jgsystemsconsulting/awesome-digital-engineering | config (404) |
