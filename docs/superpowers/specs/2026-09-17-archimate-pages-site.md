# Spec: archimate-pages-site

**Date:** 2026-09-17  
**Topic:** archimate-pages-site  
**Product:** GitHub Pages landing redesign for [awesome-archimate](https://github.com/jgsystemsconsulting/awesome-archimate)  
**Mode:** planning only through plan review (implement later under Superpowers)  
**Spoke workspace:** `C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate`  
**Hub artifacts only in this repo:** superpowers context, this spec, later plan/reviews

## Context and normative inputs

| Input | Path / URL | Role |
| --- | --- | --- |
| Context gate (synthesis + F1-F6) | `docs/superpowers/context/2026-09-17-archimate-pages-site-context.md` | Decision framing, preserve/break list, evidence index |
| Design contract (normative visual) | spoke-root `DESIGN.md` | Tokens, type, layout, motion, a11y, composition order, anti-patterns |
| Design brief | spoke-root `DESIGN_BRIEF.md` | Audience, impression, avoid list |
| Live landing seed | spoke `docs/index.html` | Capella-shaped single file to restyle |
| Distribution ledger | spoke `docs/DISTRIBUTION.md` | Pages channel, RR-B-30 single landing |
| Release gate | spoke `scripts/check_release.py` | Requires `docs/index.html` and `docs/DISTRIBUTION.md` present and scannable |
| Canonical deep list | spoke `README.md` | 17 seed entry bullets + 8 Contents catalogue links stay byte-identical |

`DESIGN.md` is the normative visual contract for this slice. If HTML/CSS drift from tokens, type scale, radius, motion, or pilot composition order, the implementation is wrong even if content links still work. Context gate path above is required input for the later plan.

## Problem / background

Awesome ArchiMate already ships a valid GitHub Pages homepage at `https://jgsystemsconsulting.github.io/awesome-archimate/` from `docs/index.html` (with empty `docs/.nojekyll`). The page meets D5 content checklist obligations from the prior RR-B packaging pass: title, meta description, canonical, Open Graph tags, version string, contribute and issue-form links, licence-enquiry URL, CC0 footer, and reduced-motion CSS.

That packaging pass listed "No marketing redesign" as a non-goal for RR-B packaging (release-standard non-goals). It did not schedule a later redesign. This slice is a separate, human-approved design pass on the same single page. The live page is Capella-shaped: narrow max-width, system-ui/Roboto stack, dual `color-scheme: light dark`, inline minimal CSS, and a short first-run plus links block. It does not implement the locked minimal-technical shell in spoke-root `DESIGN.md` / `DESIGN_BRIEF.md` (present, currently untracked).

The live landing meets release packaging checks but does not yet carry the locked DESIGN composition (hero, evidence strip, section index). Sibling anti-pattern: awesome-sysml-v2 external CSS plus Google Fonts CDN. Nearest structural twin: awesome-capella single-file landing. Section-density reference: awesome-stpa.

This slice redesigns the **same single page** under Path S (static `docs/` only). It does not open a multi-page site, Next.js path, or hub catalogue work.

## Goals

1. Restyle `docs/index.html` to the locked pilot composition and visual system in `DESIGN.md` (minimal-technical, light shell only).
2. Self-host IBM Plex Sans and IBM Plex Mono as woff2 under `docs/fonts/` with no remote font or CSS CDN fetches.
3. Present nav, hero (one claim + one primary CTA), evidence strip, section index, short curation note, contribute links, and footer in that order.
4. Preserve SEO/meta, licence-enquiry, issue-form, contribute, reduced-motion, and release-gate obligations listed in R-F5 and R-F8. Exception: F3/R-V6 replace dual `color-scheme: light dark` with light-only (do not preserve dual theme).
5. Commit `DESIGN.md` and `DESIGN_BRIEF.md` with the spoke change set.
6. Keep `scripts/check_release.py` passing; keep family CI triad (`links.yml`, `lint.yml`, `stale.yml`) untouched.
7. Leave README seed catalogue byte-identical (17 entry bullets + 8 Contents section links).

## Non-goals

- Path N (Next.js / app export), shadcn/ui, lucide, React, or any build step for Pages.
- Multi-page site, third HTML page, or mirroring the 17 README entry bullets onto the landing.
- Editing README seed entry lines or Contents catalogue link lines.
- Touching family CI triad workflows or `validate.yml` behavior beyond still running check.
- Editing the design-intelligence repo or awesome-mbse hub product files outside superpowers artifacts.
- Org catalogue entry on labs.jgsystemsconsulting.com (DISTRIBUTION remains planned).
- Dark theme, dual color-scheme, stock imagery, OG social image asset, emoji chrome.
- Extracting a shared multi-spoke theme package.
- Changing CC0 product licence of the list; fonts carry their own SIL OFL notice separately.

## Locked decisions (F1-F6)

From context synthesis. Do not reopen in plan or implement without a new human decision.

| ID | Decision | Binding rule |
| --- | --- | --- |
| **F1** | New design slice on the same single page | Prior RR-B packaging non-goal was "No marketing redesign" (no deferred-later wording). Human decision opens this DESIGN-driven restyle of one HTML landing; README remains the deep catalogue store only (R-F7 / AC-readme-freeze: no seed edit). RR-B-30 still holds: no third page. |
| **F2** | Vendored Plex is allowed (policy supersession) | D5/RR-B literal text says "No CDN, no third-party fonts." NOTICE today says third-party components are not distributed. **This slice supersedes that literal ban for self-hosted webfont files only:** ship IBM Plex woff2 under `docs/fonts/` with no remote font fetches (no Google Fonts, jsDelivr, unpkg, or other CDN). Update `NOTICE` and add SIL OFL attribution in the same change set. Policy basis is F2 + human lock, not the Research section alone. |
| **F3** | Light-only color scheme | Apply DESIGN light tokens. Drop live `color-scheme: light dark` dual mode; pin light-only (`color-scheme: light` or equivalent). |
| **F4** | Section index without entry duplication | Section index = in-page section anchors and/or deep links to GitHub README heading anchors. **Do not** copy the 17 seed entry bullets onto the landing. Optional later mirror of entries is out of this slice. |
| **F5** | Custom HTML/CSS only | shadcn/lucide named in DESIGN are non-binding for this slice. No component library. |
| **F6** | Commit design contracts | Include spoke-root `DESIGN.md` and `DESIGN_BRIEF.md` in the same change set as the landing/fonts/NOTICE work. |

Additional locked product constraints (user, not reopenable):

- Primary style: minimal-technical; secondary: none.
- Path S only this slice.
- Surface: one long landing with anchors.
- Tokens, motion, type, radius from `DESIGN.md`.
- Homepage remains `https://jgsystemsconsulting.github.io/awesome-archimate/`.

## Research

Light tier. Font and Pages constraints verified against intended public sources (live fetch may be deferred in author environment; treat URLs as required cites for plan/implement).

- IBM Plex is maintained under the SIL Open Font License; the upstream project is suitable to vendor as static webfont files for self-hosting: https://github.com/IBM/plex
- GitHub Pages serves static files from the repository (here `/docs` on `main`); self-hosted assets under the Pages tree are the standard approach with no application server: https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages

**Implementation practice (policy F2; Research only confirms OFL and Pages static hosting):** place `.woff2` files under `docs/fonts/`, reference them only via relative `url(...)` in page CSS (`@font-face`), ship OFL license text beside the fonts (or a clearly linked `docs/fonts/OFL.txt` / NOTICE pointer), and never hotlink fonts from a CDN. Context gate path for the plan: `docs/superpowers/context/2026-09-17-archimate-pages-site-context.md`.

## Requirements

### Functional

**R-F1 Landing entry.** Keep Pages entry at `docs/index.html`. Keep empty `docs/.nojekyll`. Do not rename the Pages source folder.

**R-F2 Single document.** One long scrolling landing. In-page `id` anchors for major sections used by nav and section index. No second HTML content page.

**R-F3 Composition order (pilot).** Body content order must be:

1. **Nav (required; sticky optional):** in-page anchors to `#hero`, `#evidence`, `#sections`, `#curation`, `#contribute` plus one external "Full list" text link to the CTA URL. Not multi-panel app chrome.
2. **Hero (`#hero`):** product claim + **one** primary CTA. Locked claim string: `Curated ArchiMate resources for enterprise architecture and MBSE practitioners.` (may match meta description).
3. **Evidence strip (`#evidence`):** version display **`0.1.0`** (exact), last sweep **`2026-09`**, entry count **`17`** (snapshot = curated resource bullets under the eight catalogue README sections at lock time; re-count README bullets if the freeze set changes in a later slice), and text-only family pointer exact sentence: `Part of the awesome-mbse list family; registry and family rules live in FAMILY.md in the jgsystemsconsulting/awesome-mbse repository.` (D11: plain text only, no hub FAMILY.md hyperlink).
4. **Section index (`#sections`, primary):** eight links, exact labels and order: Specifications and standards; Certification; The Archi tool; Plugins and collaboration; Books; Example models; TOGAF alignment; Communities. Each `href` is a GitHub README heading deep link of the form `https://github.com/jgsystemsconsulting/awesome-archimate/blob/main/README.md#<github-slug>` where `<github-slug>` is GitHub's heading anchor for that README `##` title. No on-page empty anchors as the sole target. Landing does not host entry rows.
5. **Short curation note (`#curation`):** public-domain / CC0 curated index framing; nothing to install; list does not re-host upstream content. One short paragraph.
6. **Contribute links (`#contribute`):** CONTRIBUTING, suggest-resource issue form, bug_report issue form (repository link optional).
7. **Footer:** CC0 / LICENSE link, licence-enquiry, maintainer (JG Systems Consulting Ltd.).

**R-F4 Primary CTA.** Exactly one primary CTA in the hero. Locked `href`: `https://github.com/jgsystemsconsulting/awesome-archimate/blob/main/README.md`. Secondary text links may exist in nav/contribute; they must not visually compete as a second filled primary button in the hero.

**R-F5 Preserve head and critical URLs (exact intent).**

| Item | Required value / behavior |
| --- | --- |
| `<title>` | `Awesome ArchiMate` |
| meta description | `Curated ArchiMate resources for enterprise architecture and MBSE practitioners.` |
| canonical | `https://jgsystemsconsulting.github.io/awesome-archimate/` |
| og:title | `Awesome ArchiMate` |
| og:description | same as meta description |
| og:url | same as canonical |
| og:type | `website` |
| lang | `en` on `<html>` |
| Licence enquiries | `https://labs.jgsystemsconsulting.com/licensing.html` |
| Suggest resource | `https://github.com/jgsystemsconsulting/awesome-archimate/issues/new?template=suggest-resource.yml` |
| Bug / dead link | `https://github.com/jgsystemsconsulting/awesome-archimate/issues/new?template=bug_report.yml` |
| CONTRIBUTING | `https://github.com/jgsystemsconsulting/awesome-archimate/blob/main/CONTRIBUTING.md` (link only; no editorial rewrite) |
| LICENSE / CC0 | `https://github.com/jgsystemsconsulting/awesome-archimate/blob/main/LICENSE` |
| Version evidence | `0.1.0` visible in evidence strip |

**R-F6 First-run content.** Live "First run" ordered steps may be folded into hero supporting copy, curation note, or a compact how-to near contribute. Do not drop the three intents: open full list, jump by section, suggest/report via issue forms.

**R-F7 README freeze.** Do not modify the 17 curated entry bullets or the 8 Contents links that point at catalogue sections. Other README edits are out of scope for this slice unless a one-line Pages pointer is already planned elsewhere (default: no README edit).

**R-F8 Release and CI.** `python scripts/check_release.py` (or repo's documented invoke) still passes. `docs/index.html` remains present and scannable under existing `SCAN_GLOBS`. Do not edit `.github/workflows/links.yml`, `lint.yml`, or `stale.yml`.

**R-F9 DISTRIBUTION.** Keep `docs/DISTRIBUTION.md`. Optionally note landing restyle in ledger notes only if a one-line status refresh is needed; do not change channel outcomes without cause. RR-B-30 outcome remains one HTML landing + README deep content.

### Visual / design system

**R-V1 Tokens.** Spoke `DESIGN.md` is a mandatory companion read (F6 commits it). Implement these CSS custom properties exactly (oklch):

```css
--color-bg: oklch(0.985 0.006 255);
--color-surface-1: oklch(0.995 0.005 255);
--color-surface-2: oklch(0.998 0.004 255);
--color-surface-3: oklch(1.0 0 0);
--color-primary: oklch(0.19 0.015 260);
--color-accent: oklch(0.58 0.17 253);
--color-text: oklch(0.17 0.012 258);
--color-text-muted: oklch(0.50 0.012 258);
--color-border: oklch(0.915 0.008 255);
--color-focus-ring: var(--color-accent);
--color-success: oklch(0.45 0.10 150);
--color-danger: oklch(0.50 0.14 25);
--color-attention: oklch(0.55 0.12 85);
```

Semantic success/danger/attention may be defined without a visible chrome consumer on this landing.

**R-V2 Typography.**

- Body/display: IBM Plex Sans via `@font-face` from `docs/fonts/`.
- Mono: IBM Plex Mono for versions, dates, tags, slugs, entry metadata chips.
- Scale from 16px base with ~1.25 ratio: 12.8 meta, 16 body, 20 h3, 25 h2, 31 h1 (px or rem equivalent).
- Weights: 400 body, 500 labels/emphasis, 600 section headings.
- Headings by weight and size, not colour alone.
- Prose measure ~65-75ch inside content shell.

**R-V3 Layout.**

- Content max width 1120px; center shell with horizontal padding.
- Spacing scale 4 / 8 / 16 / 32 / 56; major sections separated by 64-96px.
- Section index: compact linked grid or two-column list on desktop; stacked on small screens. Not a centred three-card deck.
- Density high inside index/link blocks; 1px dividers, not card stacks.

**R-V4 Shape.**

- Radius sm 3px, md 5px, lg 7px only.
- Hairline borders `1px solid var(--color-border)`.
- Elevation none by default; at most one soft shadow on primary CTA.

**R-V5 Motion.**

- 120-200ms ease-out; opacity and 4-8px translate only when motion is used.
- Hover: colour/underline on links; no scale, parallax, or bounce.
- `@media (prefers-reduced-motion: reduce)` disables animation and transition (preserve existing guarantee).

**R-V6 Light only.** No dark palette branch. No `color-scheme: light dark`.

**R-V7 Anti-patterns (must not ship).** Gradient heroes, glass, glow, emoji chrome, violet/indigo default accent, three equal feature cards, stock photos, multi-hue tags, centre-everything marketing theatre, CDN fonts, accordion-hiding the catalogue, unthemed shadcn, Inter/Roboto-only as the designed stack (system fallback cascade after Plex is OK).

### Accessibility

**R-A1** Body and muted text meet WCAG AA contrast on bg/surfaces.  
**R-A2** Visible `:focus-visible` ring using accent, 2px, offset 2px, on every interactive control.  
**R-A3** Keyboard operable nav anchors, CTAs, and issue links.  
**R-A4** Primary actions touch target >=44px height on small viewports.  
**R-A5** Landmarks: `header` / `nav` / `main` / `footer` as appropriate; single `h1`; heading order h1->h2->h3 without skips for exposed sections.  
**R-A6** `lang="en"`. Reduced motion as R-V5.

### Responsive

**R-R1** Desktop >=1024px: full index density; optional two-column section index.  
**R-R2** Tablet: single column; nav wraps or simple horizontal scroll of anchors without page horizontal overflow.  
**R-R3** Mobile ~390px: stacked hero, full-width primary CTA >=44px tall, section anchors stacked, no horizontal overflow, body >=16px.

### Packaging / fonts / attribution

**R-P1 Path S file layout (spoke).**

| Path | Action |
| --- | --- |
| `docs/index.html` | Rewrite structure + CSS to this spec |
| `docs/fonts/` | Add directory; IBM Plex Sans + Mono woff2 files needed for weights 400/500/600 used |
| `docs/fonts/` license text | Include OFL (e.g. `OFL.txt`) or equivalent clear attribution file for shipped faces |
| `docs/site.css` | Optional same-folder split; if used, link relatively only; no CDN |
| `docs/.nojekyll` | Keep |
| `docs/DISTRIBUTION.md` | Keep (minor note optional) |
| `NOTICE` | Update: remove or replace blanket "Third-party components are not distributed" so vendored Plex is disclosed; point to OFL files |
| `DESIGN.md`, `DESIGN_BRIEF.md` | Add/commit with change set (F6) |
| `.github/workflows/links.yml`, `lint.yml`, `stale.yml` | **Do not touch** |
| `README.md` seed entries / Contents catalogue links | **Do not touch** |
| hub awesome-mbse product files | **Do not touch** (superpowers artifacts only) |
| design-intelligence repo | **Do not touch** |

**R-P2 Font loading.** `@font-face` with `font-display: swap` (or equivalent non-blocking strategy). Relative paths only (`fonts/...`). Forbid any absolute `http(s):` URL in `@font-face` `src` and any `@import` of remote CSS. Minimum faces: Plex Sans 400/500/600 and Plex Mono 400 (add 500 mono only if used). Record IBM/plex release or package version in NOTICE.

**R-P3 CSS placement.** Inline `<style>` in `index.html` **or** one relative `docs/*.css` file. Prefer fewest files: single HTML with inline CSS is acceptable if readable; split only if it keeps the HTML clearer without adding a build step.

**R-P4 Binary hygiene.** Commit only the woff2 faces actually referenced (Sans + Mono, weights used). Do not vendor the entire IBM Plex monorepo tree.

**R-P5 check_release.** After changes, `python scripts/check_release.py` exits 0. That script is the only scanner oracle for this slice (presence of required files + its encoded checks). No additional "plain HTML" subjective gate.

## Acceptance criteria

Testable checks for plan/implement/verify.

1. **AC-composition.** DOM order matches nav -> hero -> evidence -> section index -> curation -> contribute -> footer; ids `#hero` `#evidence` `#sections` `#curation` `#contribute` present.
2. **AC-cta.** Hero contains exactly one primary CTA; `href` equals `https://github.com/jgsystemsconsulting/awesome-archimate/blob/main/README.md`.
3. **AC-evidence.** Evidence strip shows version `0.1.0`, last sweep `2026-09`, entry count `17`, and the locked D11 family pointer sentence (no hub FAMILY.md hyperlink).
4. **AC-sections.** Section index has exactly eight links with the locked labels/order; each href is a `blob/main/README.md#...` deep link; no duplicated 17 entry title rows on the landing.
5. **AC-first-run.** Three intents visible without hunting: open full list (CTA), jump by section (section index), suggest/report (issue-form links in contribute).
6. **AC-meta.** Title, description, canonical, og:title, og:description, og:url, og:type match R-F5.
7. **AC-links.** Licence-enquiry, suggest-resource, bug_report, CONTRIBUTING, LICENSE, and maintainer attribution present with R-F5 hrefs.
8. **AC-fonts-local.** `@font-face` `src` values are relative only; grep of `docs/**/*.{html,css}` finds zero `https://` or `http://` inside `@font-face` blocks and zero `fonts.googleapis` / `fonts.gstatic` / `@import` remote stylesheets.
9. **AC-plex-files.** Woff2 files for Sans 400/500/600 and Mono 400 exist under `docs/fonts/` and are referenced by `@font-face`.
10. **AC-notice.** `NOTICE` discloses vendored IBM Plex + SIL OFL and removes any blanket "no third-party components are distributed" claim; include OFL text file under `docs/fonts/` or path cited from NOTICE.
11. **AC-tokens.** CSS defines all R-V1 custom properties with the locked oklch values (string match in source).
12. **AC-light.** No `color-scheme: light dark`; light-only.
13. **AC-a11y.** `prefers-reduced-motion: reduce` disables animation/transition; `:focus-visible` 2px accent offset 2px on interactive controls; landmarks include nav/main/footer (header optional if nav/hero cover); single h1; heading levels do not skip; body text and muted text AA on bg (manual or tooling check once).
14. **AC-responsive.** At 390px width, no horizontal scrollbar; primary CTA >=44px tall.
15. **AC-anti-pattern.** No gradient hero, glass/glow, three equal feature cards, emoji in nav/hero chrome, violet/indigo accent default, multi-hue tag carnival, stock photos, CDN fonts, accordion-hidden catalogue.
16. **AC-readme-freeze.** `git diff` on README shows no changes to the 17 entry bullets or 8 Contents catalogue links (ideally empty README diff).
17. **AC-ci-freeze.** `git diff` on `.github/workflows/links.yml`, `lint.yml`, `stale.yml` is empty; do not edit `validate.yml` either.
18. **AC-design-commit.** `DESIGN.md` and `DESIGN_BRIEF.md` are tracked files in the spoke change set.
19. **AC-release.** `scripts/check_release.py` exits 0 with `docs/index.html` still present.
20. **AC-rr-b-30.** Single Pages HTML landing only (no new content HTML pages under `docs/`).

## Implementation constraints

- **Repo to edit:** `awesome-archimate` only (plus this hub superpowers spec already written).
- **Path S:** static files only; no Node build, no Next, no package.json requirement for Pages.
- **Seed:** restyle existing `docs/index.html`; Capella structure is historical seed, not visual authority once DESIGN applies.
- **Normative visual file:** spoke `DESIGN.md`. Brief is supporting product intent.
- **Plan later must cite:** this spec + `docs/superpowers/context/2026-09-17-archimate-pages-site-context.md`.
- **IBM Plex obtainment:** copy sanctioned woff2 build artifacts from IBM/plex releases or official package paths consistent with OFL; record source version in NOTICE or fonts README one-liner if helpful.
- **Entry count:** curated resource bullets under catalogue sections = **17** (do not count Contents chrome or non-entry lines).
- **Family pointer (D11):** use the locked exact sentence in R-F3 evidence strip (text only).
- **Do not** implement from design-intelligence templates beyond what is already locked into spoke DESIGN.md.

## Out of scope

- Mirroring README entries into HTML rows or generating the landing from README.
- Path N app shell, shadcn, lucide-react.
- Dark mode toggle or system dark adaptation.
- New OG image, favicon set, or PWA manifest (favicon optional only if already needed; not required).
- sindresorhus/awesome submission, org catalogue publish, marketplace manifests.
- Changes to CONTRIBUTING editorial rules, seed list membership, or CHANGELOG version bump solely for cosmetics (version stays 0.1.0 unless release process says otherwise).
- Multi-spoke shared CSS package extraction.
- Editing awesome-mbse hub list product or other spokes' landings in this slice.
- Reopening F1-F6.

## Risks

| Risk | Mitigation |
| --- | --- |
| NOTICE / RR-B-02 reading conflicts with vendored fonts | F2 + R-P1 NOTICE/OFL update in same PR as fonts |
| Accidental README seed edit while adding Pages pointer | AC-readme-freeze; default no README touch |
| CDN habit from sysml-v2 sibling | AC-fonts-local grep gate; Path S relative only |
| Scope creep into entry mirror or multi-page | F4, F1, AC-rr-b-30 |
| check_release or scan breaks on exotic markup | Keep semantic HTML; run check_release before merge |
| Font weight/file bloat | R-P4 only referenced woff2 |
| Dual theme leftover | F3, AC-light |
| DESIGN.md left untracked | F6, AC-design-commit |
| Visual regression into generic AI landing | R-V7 anti-patterns; quality bar in DESIGN.md |
| Family CI churn | AC-ci-freeze; do not "improve" triad while here |

## Quality bar (from DESIGN.md)

Operational bar for this slice: satisfy R-V1 through R-V7 and the anti-pattern list (no gradient hero, no Inter/Roboto-only stack, no feature-card trio, no glass/glow, no CDN fonts, no SaaS launch layout). DESIGN.md quality prose remains advisory colour; acceptance is the AC list above.

## Traceability

| Concern | Source |
| --- | --- |
| Composition, tokens, type, motion, a11y | spoke `DESIGN.md` |
| Audience, avoid list | spoke `DESIGN_BRIEF.md` |
| F1-F6, preserve list, sibling analogs | hub `docs/superpowers/context/2026-09-17-archimate-pages-site-context.md` |
| Pages channel + RR-B-30 | spoke `docs/DISTRIBUTION.md` |
| Release file presence | spoke `scripts/check_release.py` |
| Font licence practice | Research URLs (IBM/plex, GitHub Pages docs) |

## Deliverable summary for implementer

In `awesome-archimate`: rewrite `docs/index.html` to DESIGN composition and tokens; vendor Plex under `docs/fonts/`; update `NOTICE` (+ OFL file); commit `DESIGN.md` and `DESIGN_BRIEF.md`; leave README seed and family CI triad alone; prove check_release and acceptance criteria above.

Hub work for this step ends at this spec. Plan author uses this file next; no implementation in planning-only mode until the user runs full Superpowers execute.
