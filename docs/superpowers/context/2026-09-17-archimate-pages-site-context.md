# Context: archimate-pages-site

## Context brief

**Primary question:** What already exists in awesome-archimate (and sibling spokes) that a DESIGN.md-driven GitHub Pages landing redesign must reuse, preserve, or not break?

**Sub-questions:**

1. What is the current `docs/index.html` structure, constraints, and content obligations (meta, licence URL, first-run, links)?
2. What does the locked `DESIGN.md` / `DESIGN_BRIEF.md` require that the current landing does not yet implement?
3. What sibling spoke Pages landings exist as nearest analogs (Capella, STPA, sysml-v2)?
4. What RR-B / release-standard and DISTRIBUTION constraints bind Pages (no CDN, no third-party fonts, self-contained, single landing outcome)?
5. Where do fonts, CSS, and static assets live (or not) today?
6. What must stay byte-stable outside the landing (README seed entries, family CI)?

**Success criteria (design work must know):**

- C1: Exact path and role of the Pages entry (`docs/index.html`, `.nojekyll`) and whether Pages is already the homepage target.
- C2: Current landing content obligations that redesign must keep (title, description, canonical, OG, licence-enquiry URL, contribute/issue links, version string).
- C3: Locked design contract location and key implementation constraints (Path S static, self-host Plex, composition order, tokens).
- C4: Nearest sibling landing pattern (file layout, size, self-contained CSS vs external).
- C5: DISTRIBUTION / RR-B-20 / RR-B-30 constraints that limit multi-page or CDN.
- C6: Non-goals for this slice (README seed freeze, family CI triad untouched, no DI repo edits).

**Out of scope:** Implementing the redesign; Next.js app path; multi-spoke theme package extraction; hub org catalogue.

**Budget:** 1 round preferred; max 3. Light tier parent.

**Workspace baseline:**

- Repo: `C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate`
- HEAD (info): `95947c1bd55032f5801a191a4c6aa376e89051ae`
- porcelain sha256: `1f56d8bf3d5311ed4a4a91bc05fcb303ef0d31f3e4daf2423b0e9e95d5ddd625`

## Findings

1. Pages entry is `docs/index.html` plus empty `docs/.nojekyll`; `docs/` also holds `DISTRIBUTION.md` only (no `fonts/`, no external CSS). Sites: cartographer docs tree; prospector layout. Grade: CORROBORATED (code + doc).
2. DISTRIBUTION and D5/RR-B-20/21 bind serve-from `/docs`, homepage `https://jgsystemsconsulting.github.io/awesome-archimate/`. Grade: CORROBORATED (doc sites).
3. Live head already carries title, meta description, canonical, OG tags; body has version 0.1.0, first-run list, README/CONTRIBUTING/suggest/bug/licence-enquiry links, CC0 footer. Grade: CORROBORATED (code).
4. Locked contracts are spoke-root `DESIGN.md` and `DESIGN_BRIEF.md` (present, **untracked** `??`). Path S static `docs/`, self-host IBM Plex under `docs/fonts/`, Path N deferred, composition nav→hero→evidence→section index→curation→contribute→footer. Grade: CORROBORATED for content (doc); git status SINGLE-SOURCE for untracked (config).
5. Live page is Capella-shaped: single file, inline CSS, `system-ui`…`Roboto` stack, reduced-motion present, `color-scheme: light dark`. No DESIGN composition landmarks. Grade: CORROBORATED.
6. Sibling analogs: Capella nearest twin; STPA richer inline sections still system fonts; sysml-v2 external `site.css` + Google Fonts CDN is the named anti-pattern to avoid. Grade: CORROBORATED.
7. RR-B-30 / DISTRIBUTION: one HTML landing + README deep content; no third page. Release non-goal text also said "No marketing redesign" for the **prior** RR-B packaging pass. Grade: CORROBORATED on single-page; CONFLICT framed below on redesign scope.
8. `scripts/check_release.py` requires `docs/index.html` and `docs/DISTRIBUTION.md`. Family triad `links/lint/stale` untouched; `validate.yml` runs check only. Grade: CORROBORATED.
9. NOTICE line: "Third-party components are not distributed with this repository." Collides with vendoring Plex binaries unless NOTICE (and any RR-B-02 reading) is updated when fonts ship. Grade: CONFLICT framed.
10. Seed freeze: 17 README entry bullets + 8 Contents links stay byte-identical. DESIGN's optional later mirror of entries is out of this slice. Grade: CORROBORATED (doc).
11. RR-B file PASS does not equal DESIGN compliance; redesign is additive chrome on a page that already meets D5 content checklist. Grade: CORROBORATED (skeptic + composition gap).

## Synthesis

**Decision-ready facts.** Implement Path S only under `awesome-archimate/docs/`. Keep single `index.html` (CSS may stay inline or split to a same-folder static file with no CDN). Preserve meta/OG/canonical, licence-enquiry URL, contribute/issue links, version evidence, reduced-motion. Do not touch README seed lines, family CI triad, or design-intelligence. Capella is structural seed; STPA is section-density reference; sysml-v2 is anti-pattern for fonts/CDN.

**Open conflicts (framed for the spec, not left vague):**

| ID | Tension | Spec must lock |
|---|---|---|
| F1 | Prior RR-B "No marketing redesign" vs locked DESIGN richer shell | This work is a **new** slice: DESIGN-driven restyle of the same single page. Still one HTML + README deep content (RR-B-30 holds). Not a multi-page site. |
| F2 | D5 "no third-party fonts" + NOTICE "no third-party components" vs DESIGN self-host Plex | Ship Plex as **vendored webfont files** under `docs/fonts/` (no CDN). Update NOTICE (and SIL OFL attribution) when fonts are added. Interpret RR-B "no third-party fonts" as **no remote font fetches**, matching the sysml-v2 flaw fix. |
| F3 | Live `color-scheme: light dark` vs DESIGN light shell | Force light design tokens; drop dual color-scheme or pin light-only. |
| F4 | DESIGN optional entry mirror vs seed freeze | **This slice:** section index = anchors to on-page section labels and/or deep-links into GitHub README headings. **Do not** duplicate the 17 entry bullets onto the landing. |
| F5 | shadcn/lucide named in DESIGN | Non-binding for this slice. Custom HTML/CSS only. |
| F6 | DESIGN.md untracked | Spec/plan include committing DESIGN.md + DESIGN_BRIEF.md with the landing change set. |

**Single-source notes.** Platform homepage URL is ledger-asserted, not a local config file. Empty `.nojekyll` has no line quote.

**Coverage:** C1–C6 met for design planning. Decision-bearing claims either CORROBORATED or framed above.

## Evidence index

| loc | kind |
|---|---|
| awesome-archimate/docs/index.html | code |
| awesome-archimate/docs/.nojekyll | config |
| awesome-archimate/docs/DISTRIBUTION.md | doc |
| awesome-archimate/DESIGN.md | doc |
| awesome-archimate/DESIGN_BRIEF.md | doc |
| awesome-archimate/NOTICE | doc |
| awesome-archimate/scripts/check_release.py | code |
| awesome-archimate/.github/workflows/* | config |
| awesome-capella/docs/index.html | code |
| awesome-stpa/docs/index.html | code |
| awesome-sysml-v2/docs/index.html | code |
| awesome-sysml-v2/docs/site.css | code |
| awesome-mbse/docs/superpowers/specs/2026-09-17-archimate-release-standard.md | doc |
