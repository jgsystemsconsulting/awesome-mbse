# Awesome ArchiMate Pages Landing Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restyle the single GitHub Pages landing at `awesome-archimate/docs/index.html` to the locked DESIGN.md pilot composition (nav, hero, evidence, section index, curation, contribute, footer), self-host IBM Plex Sans/Mono woff2 under `docs/fonts/`, update NOTICE + OFL attribution, and commit `DESIGN.md` / `DESIGN_BRIEF.md` with the same change set, without touching README seed catalogue lines or the family CI triad.

**Architecture:** Path S only. Static files under spoke `docs/`. One long `docs/index.html` (inline `<style>` preferred; optional same-folder `docs/site.css` if it keeps markup clearer). No Node, no Next, no package.json requirement for Pages. Empty `docs/.nojekyll` stays. Canonical deep list remains README on GitHub; landing section index deep-links eight README `##` headings via `blob/main/README.md#<slug>`. Release gate stays `python scripts/check_release.py`.

**Tech Stack:** HTML5 + CSS custom properties (oklch tokens from DESIGN.md) + self-hosted IBM Plex Sans/Mono `.woff2` via `@font-face`. No CDN, no remote `@import`, no component library. Verification: Git Bash greps, Python one-liners, `scripts/check_release.py`.

**Spec:** `docs/superpowers/specs/2026-09-17-archimate-pages-site.md` (normative; F1-F6, R-*, AC-*, Path S).

**Context:** `docs/superpowers/context/2026-09-17-archimate-pages-site-context.md` (F1-F6 framing, preserve list, sibling analogs).

**Spoke workspace:** `C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate`

## Research

Cite from spec Research (light tier). Font and Pages constraints:

- IBM Plex upstream (SIL OFL; vendor static webfonts only): https://github.com/IBM/plex
- GitHub Pages can publish from a `/docs` folder on the source branch: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- About GitHub Pages (static HTML/CSS/JS hosting overview): https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages

Practice locked by F2 (not Research alone): place `.woff2` under `docs/fonts/`, reference only via relative `url(...)` in `@font-face`, ship OFL text beside fonts, never hotlink CDN fonts.

## Global Constraints

Every task includes these. Do not reopen F1-F6 without a new human decision.

| Lock | Rule |
| --- | --- |
| F1 | Same single page restyle; RR-B-30 holds (no third HTML content page) |
| F2 | Vendored Plex allowed; no remote font/CSS CDN; NOTICE + OFL in same change set |
| F3 | Light-only; no `color-scheme: light dark` |
| F4 | Section index = eight README deep links; do not mirror 17 entry bullets |
| F5 | Custom HTML/CSS only; shadcn/lucide non-binding |
| F6 | Commit `DESIGN.md` and `DESIGN_BRIEF.md` with landing/fonts/NOTICE |
| Path S | Static `docs/` only |
| R-V1 | Inline the locked oklch token block exactly |
| R-F4 | Primary CTA href pinned to README blob URL |
| D11 | Evidence family sentence is plain text only (no hub FAMILY.md hyperlink) |
| README | No seed entry bullet or Contents catalogue link edits |
| CI | Do not edit `links.yml`, `lint.yml`, `stale.yml` (or `validate.yml`) |
| Hub | Superpowers artifacts only in awesome-mbse; no hub product edits |

**Primary CTA (exact):** `https://github.com/jgsystemsconsulting/awesome-archimate/blob/main/README.md`

**Locked claim / meta description (exact):** `Curated ArchiMate resources for enterprise architecture and MBSE practitioners.`

**D11 family sentence (exact):** `Part of the awesome-mbse list family; registry and family rules live in FAMILY.md in the jgsystemsconsulting/awesome-mbse repository.`

**Evidence chips (exact):** version `0.1.0`, last sweep `2026-09`, entry count `17`.

### GitHub heading slugs (section index)

README already uses GitHub Contents anchors. Use these eight deep links in lock order (labels exact):

| Label | href |
| --- | --- |
| Specifications and standards | `https://github.com/jgsystemsconsulting/awesome-archimate/blob/main/README.md#specifications-and-standards` |
| Certification | `https://github.com/jgsystemsconsulting/awesome-archimate/blob/main/README.md#certification` |
| The Archi tool | `https://github.com/jgsystemsconsulting/awesome-archimate/blob/main/README.md#the-archi-tool` |
| Plugins and collaboration | `https://github.com/jgsystemsconsulting/awesome-archimate/blob/main/README.md#plugins-and-collaboration` |
| Books | `https://github.com/jgsystemsconsulting/awesome-archimate/blob/main/README.md#books` |
| Example models | `https://github.com/jgsystemsconsulting/awesome-archimate/blob/main/README.md#example-models` |
| TOGAF alignment | `https://github.com/jgsystemsconsulting/awesome-archimate/blob/main/README.md#togaf-alignment` |
| Communities | `https://github.com/jgsystemsconsulting/awesome-archimate/blob/main/README.md#communities` |

Slug rule: GitHub's algorithm on the README `##` title (lowercase; strip punctuation; spaces to hyphens). These match the live README Contents list. If a title ever changes, re-derive from that algorithm or verify by opening the README anchor on GitHub before shipping.

### R-V1 tokens (copy exactly into CSS `:root`)

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

### Required head / URLs (R-F5)

| Item | Value |
| --- | --- |
| `<title>` | `Awesome ArchiMate` |
| meta description | locked claim string above |
| canonical / og:url | `https://jgsystemsconsulting.github.io/awesome-archimate/` |
| og:title | `Awesome ArchiMate` |
| og:description | same as meta description |
| og:type | `website` |
| `lang` | `en` |
| Licence enquiries | `https://labs.jgsystemsconsulting.com/licensing.html` |
| Suggest resource | `https://github.com/jgsystemsconsulting/awesome-archimate/issues/new?template=suggest-resource.yml` |
| Bug / dead link | `https://github.com/jgsystemsconsulting/awesome-archimate/issues/new?template=bug_report.yml` |
| CONTRIBUTING | `https://github.com/jgsystemsconsulting/awesome-archimate/blob/main/CONTRIBUTING.md` |
| LICENSE | `https://github.com/jgsystemsconsulting/awesome-archimate/blob/main/LICENSE` |

### File layout (R-P1)

| Path | Action |
| --- | --- |
| `docs/index.html` | Rewrite structure + CSS |
| `docs/fonts/` | Add; Sans 400/500/600 + Mono 400 woff2 only |
| `docs/fonts/OFL.txt` (or equivalent) | Ship SIL OFL text for shipped faces |
| `docs/site.css` | Optional relative split; default prefer inline |
| `docs/.nojekyll` | Keep empty |
| `docs/DISTRIBUTION.md` | Keep (optional one-line restyle note only) |
| `NOTICE` | Disclose vendored Plex + OFL; drop blanket no-third-party claim |
| `DESIGN.md`, `DESIGN_BRIEF.md` | Track/commit with change set |
| README seed / Contents | Do not touch |
| `.github/workflows/links.yml`, `lint.yml`, `stale.yml` | Do not touch |

## Task 0: Branch and freeze baselines

**Files:** none modified yet.

**Model:** flash

- [ ] **Step 1: Confirm spoke cwd and clean baseline intent**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
git status --short
git rev-parse HEAD
```

Expected: spoke is the edit target. `DESIGN.md` and `DESIGN_BRIEF.md` may show as untracked (`??`). Do not edit README or workflow triad.

- [ ] **Step 2: Create working branch**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
git switch -c pages/design-landing
```

(Use another branch name only if this one already exists; stay off `main` for the change set.)

- [ ] **Step 3: Freeze README catalogue bytes for AC-readme-freeze**

Write and run a one-shot freeze script from spoke root (prefer a temp file so nested shell heredocs are not required):

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
mkdir -p /tmp
python /tmp/freeze_archimate_readme_catalogue.py
```

Script body for `/tmp/freeze_archimate_readme_catalogue.py`:

```python
from pathlib import Path
import sys
out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/tmp/archimate-pages-freeze")
out.mkdir(parents=True, exist_ok=True)
text = Path("README.md").read_text(encoding="utf-8")
lines = text.splitlines()
labels = {
    "Specifications and standards", "Certification", "The Archi tool",
    "Plugins and collaboration", "Books", "Example models",
    "TOGAF alignment", "Communities",
}
contents, entries = [], []
in_contents = False
in_catalogue = False
for line in lines:
    if line.strip() == "## Contents":
        in_contents = True
        in_catalogue = False
        continue
    if in_contents:
        if line.startswith("## "):
            in_contents = False
            title = line[3:].strip()
            in_catalogue = title in labels
        elif line.startswith("- [") and "](#" in line:
            label = line.split("]")[0].split("[", 1)[-1]
            if label in labels:
                contents.append(line)
        continue
    if line.startswith("## "):
        title = line[3:].strip()
        in_catalogue = title in labels
        continue
    if in_catalogue and line.startswith("- [") and "](http" in line:
        entries.append(line)
(out / "contents.txt").write_text("\n".join(contents) + "\n", encoding="utf-8")
(out / "entries.txt").write_text("\n".join(entries) + "\n", encoding="utf-8")
print(f"contents={len(contents)} entries={len(entries)} out={out}")
assert len(contents) == 8, len(contents)
assert len(entries) == 17, len(entries)
```

First run (baseline):

```bash
python /tmp/freeze_archimate_readme_catalogue.py /tmp/archimate-pages-freeze-before
```

Expected: `contents=8 entries=17`.

- [ ] **Step 4: Freeze CI triad + validate.yml paths**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
git hash-object .github/workflows/links.yml .github/workflows/lint.yml .github/workflows/stale.yml .github/workflows/validate.yml > /tmp/archimate-pages-ci-before.sha
cat /tmp/archimate-pages-ci-before.sha
```

Done when: branch exists, freeze-before files written, counts 8 and 17, CI hashes captured.

## Task 1: Obtain IBM Plex woff2 + OFL

**Files:**
- Create: `docs/fonts/` directory
- Create: `docs/fonts/*.woff2` (Sans 400/500/600, Mono 400 only)
- Create: `docs/fonts/OFL.txt` (SIL Open Font License text shipped with the faces)

**Interfaces:**
- Consumes: IBM/plex sanctioned build artifacts (release zip or official package path consistent with OFL).
- Produces: relative font files referenced later by `@font-face`.

**Model:** standard

- [ ] **Step 1: Create fonts directory**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
mkdir -p docs/fonts
```

- [ ] **Step 2: Download a sanctioned IBM Plex release and extract only needed woff2**

Prefer an official IBM/plex GitHub release asset or the published package files that include woff2. Example pattern (adjust tag/asset name to the current release you actually fetch; record the version):

```bash
cd /tmp
# Pin a real IBM/plex release tag when implementing (replace TAG).
# Verify on https://github.com/IBM/plex/releases
TAG="REPLACE_WITH_REAL_TAG"
curl -sL -o plex.zip "https://github.com/IBM/plex/archive/refs/tags/${TAG}.zip"
# Or download the release asset that contains web/woff2 builds if the tag tree lacks prebuilt woff2
unzip -l plex.zip | head
```

If the tag source tree lacks ready `.woff2`, use the official npm package tarball or release asset that ships web fonts, still under SIL OFL. Do not use Google Fonts, jsDelivr, or unpkg hotlinks in the page.

Copy only these faces into the spoke (rename cleanly if needed):

| Logical face | Suggested filename |
| --- | --- |
| IBM Plex Sans Regular 400 | `docs/fonts/IBMPlexSans-Regular.woff2` |
| IBM Plex Sans Medium 500 | `docs/fonts/IBMPlexSans-Medium.woff2` |
| IBM Plex Sans SemiBold 600 | `docs/fonts/IBMPlexSans-SemiBold.woff2` |
| IBM Plex Mono Regular 400 | `docs/fonts/IBMPlexMono-Regular.woff2` |

Do not vendor the full monorepo tree (R-P4).

- [ ] **Step 3: Ship OFL text**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
# Copy OFL from the obtained package (path varies by asset).
# cp /tmp/plex-extract/path/to/OFL.txt docs/fonts/OFL.txt
test -f docs/fonts/OFL.txt
grep -qi "SIL OPEN FONT LICENSE" docs/fonts/OFL.txt
```

- [ ] **Step 4: Record source version for NOTICE**

Write the exact IBM/plex release tag or package version you used into a one-line note you will paste into NOTICE in Task 2 (example shape: IBM Plex Sans + Mono woff2 from IBM/plex <tag-or-version>).

- [ ] **Step 5: Verify files present**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
ls -la docs/fonts/
python -c "from pathlib import Path; need=["IBMPlexSans-Regular.woff2","IBMPlexSans-Medium.woff2","IBMPlexSans-SemiBold.woff2","IBMPlexMono-Regular.woff2","OFL.txt"]; root=Path("docs/fonts"); missing=[n for n in need if not (root/n).is_file()]; assert not missing, missing; assert all((root/n).stat().st_size>1000 for n in need if n.endswith(".woff2")); print("fonts ok")"
```

Done when: four woff2 + OFL.txt exist under `docs/fonts/`, source version string known for NOTICE. **Maps AC-plex-files (files half).**

## Task 2: Update NOTICE (F2)

**Files:**
- Modify: `NOTICE`

**Interfaces:**
- Consumes: Plex version string + `docs/fonts/OFL.txt` path from Task 1.
- Produces: disclosure that supersedes the blanket "Third-party components are not distributed" line.

**Model:** flash

- [ ] **Step 1: Rewrite NOTICE**

Replace the current blanket third-party denial. Keep product copyright header. Disclose vendored fonts and point at OFL. Example body (adjust version string to the real tag):

```text
Awesome ArchiMate
Copyright (c) 2026 JG Systems Consulting Ltd.

The curated list content is dedicated to the public domain under CC0-1.0 (see LICENSE).
Linked upstream resources remain under their own licences; this repository does not
re-host those resources.

Vendored third-party fonts (self-hosted for the GitHub Pages landing only):
  IBM Plex Sans and IBM Plex Mono (woff2), obtained from IBM/plex <TAG_OR_VERSION>.
  Licensed under the SIL Open Font License 1.1. Full license text: docs/fonts/OFL.txt.
  Font files live under docs/fonts/ and are referenced only via relative URLs in page CSS.
  No remote font CDN is used.
```

- [ ] **Step 2: Verify NOTICE**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
grep -n "IBM Plex\|SIL\|OFL\|docs/fonts" NOTICE
if grep -qi "Third-party components are not distributed" NOTICE; then echo "FAIL: blanket no-third-party claim still present"; exit 1; fi
echo "NOTICE ok"
```

Done when: NOTICE names IBM Plex, SIL OFL, and `docs/fonts/OFL.txt` (or equivalent cited path); blanket denial gone. **Maps AC-notice.**

## Task 3: Rewrite `docs/index.html` to composition + tokens

**Files:**
- Modify: `docs/index.html` (full structural rewrite)
- Optional create: `docs/site.css` (only if inline CSS becomes unreadable; relative link only)

**Interfaces:**
- Consumes: R-V1 tokens, R-F3 composition, R-F5 head/URLs, fonts from Task 1.
- Produces: DESIGN-compliant Path S landing.

**Model:** deep

- [ ] **Step 1: Keep packaging invariants**

Preserve empty `docs/.nojekyll`. Do not rename the Pages folder. Do not add a second content HTML page under `docs/`.

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
test -f docs/.nojekyll
```

- [ ] **Step 2: Write head (meta unchanged in intent)**

`docs/index.html` must include:

- `<!DOCTYPE html>` and `<html lang="en">`
- charset + viewport
- title, description, canonical, og:title, og:description, og:url, og:type per R-F5
- Either inline `<style>` **or** `<link rel="stylesheet" href="site.css">` (relative only)

- [ ] **Step 3: `@font-face` blocks (relative only, `font-display: swap`)**

Minimum four faces. Paths match Task 1 filenames. Each face uses relative `url("fonts/....woff2")` only:

- IBM Plex Sans 400 -> `fonts/IBMPlexSans-Regular.woff2`
- IBM Plex Sans 500 -> `fonts/IBMPlexSans-Medium.woff2`
- IBM Plex Sans 600 -> `fonts/IBMPlexSans-SemiBold.woff2`
- IBM Plex Mono 400 -> `fonts/IBMPlexMono-Regular.woff2`

Body stack: `"IBM Plex Sans", system-ui, -apple-system, "Segoe UI", sans-serif`. Mono for chips/version/date: `"IBM Plex Mono", ui-monospace, monospace`. System fallback after Plex is allowed (R-V7); Inter/Roboto-only as the designed stack is not.

- [ ] **Step 4: Tokens, light-only, layout, a11y CSS**

In `:root`:

- Paste R-V1 token block exactly (string match).
- `color-scheme: light;` only (F3). **Never** `light dark`.
- Type scale from 16px base (~1.25): meta 12.8, body 16, h3 20, h2 25, h1 31 (px or rem equivalent).
- Weights 400 / 500 / 600 as specified.
- Content shell max-width 1120px, centered, horizontal padding.
- Spacing scale 4/8/16/32/56; major sections 64-96px apart.
- Radius 3/5/7 only; hairline `1px solid var(--color-border)`.
- Focus: `:focus-visible { outline: 2px solid var(--color-focus-ring); outline-offset: 2px; }` on interactive controls.
- Primary CTA: accent treatment; min-height 44px on small viewports; at most one soft shadow.
- Motion 120-200ms ease-out only if used; hover colour/underline only.
- Required: `@media (prefers-reduced-motion: reduce)` disables animation and transition.
- Section index: compact linked grid or two-column list at desktop (>=1024px); stacked on small screens. Not a three-card deck.
- Density: 1px dividers inside index, not card stacks.
- Anti-patterns to avoid: gradient hero, glass, glow, violet/indigo default accent (use locked accent token), emoji chrome, multi-hue tags, stock images, CDN font URLs.

- [ ] **Step 5: Body composition order (exact)**

DOM order and ids:

1. **Nav** (`<nav>` landmark; sticky optional): in-page links to `#hero`, `#evidence`, `#sections`, `#curation`, `#contribute`, plus one external text link "Full list" to the primary CTA blob URL. Not multi-panel app chrome.
2. **Hero** (`#hero`): single `h1` product name; claim paragraph with locked claim string; **exactly one** primary CTA control (implementer may use class `primary` as a local convention; verifier keys on href + count, not class name) with href = pinned blob README URL. Optional short supporting copy may fold first-run intent 1.
3. **Evidence** (`#evidence`): mono chips or definition list showing `0.1.0`, `2026-09`, `17`, plus the locked D11 family sentence as plain text (no anchor to hub FAMILY.md).
4. **Section index** (`#sections`): heading + exactly eight links, labels and order as the slug table; each href is the blob deep link. No entry title rows.
5. **Curation** (`#curation`): one short paragraph: public-domain / CC0 curated index; nothing to install; list does not re-host upstream content. May absorb first-run framing.
6. **Contribute** (`#contribute`): links to CONTRIBUTING, suggest-resource form, bug_report form (repo link optional). First-run intent 3 lives here.
7. **Footer** (`<footer>`): CC0 / LICENSE link, licence-enquiry URL, maintainer "JG Systems Consulting Ltd."

Landmarks: `nav`, `main`, `footer` required; `header` optional if nav/hero cover. Heading order h1 then h2s for sections; no skips.

- [ ] **Step 6: Optional CSS split**

Default: keep CSS inline in `index.html` (fewest files). Split to `docs/site.css` only if the HTML is clearer; if split, link relatively and keep all tokens/`@font-face` in that file (still no CDN).

- [ ] **Step 7: Sanity open locally (optional)**

Open `docs/index.html` in a browser; confirm no network font requests in devtools.

Done when: file implements composition, tokens, fonts, light-only, a11y hooks. **Maps AC-composition, AC-cta, AC-evidence, AC-sections, AC-first-run, AC-meta, AC-links, AC-tokens, AC-light, AC-a11y (source), AC-responsive (source), AC-anti-pattern (source), AC-plex-files (reference half).**

## Task 4: Verification greps and acceptance mapping

**Files:** none required; fix `docs/index.html` / NOTICE / fonts only if a check fails.

**Model:** standard

Run all steps from spoke root. Author one temp verifier `/tmp/verify_archimate_pages.py` during execute that encodes assertion items 1-12 below (avoids fragile one-liners). Still run freeze diffs and `check_release.py` as separate commands.

- [ ] **Step 0: Author `/tmp/verify_archimate_pages.py`**

The verifier must assert:

1. **AC-composition:** ids `#hero` `#evidence` `#sections` `#curation` `#contribute` present in that order; landmarks include `nav`, `main`, `footer`.
2. **AC-cta (source):** hero region contains exactly one control whose href is the pinned CTA URL `https://github.com/jgsystemsconsulting/awesome-archimate/blob/main/README.md` (do not require a CSS class named primary).
3. **AC-evidence:** evidence region contains `0.1.0`, `2026-09`, `17`, and the locked D11 family sentence; no `href` containing `FAMILY.md`.
4. **AC-sections:** exactly eight `blob/main/README.md#...` hrefs with locked labels/order/slugs from the slug table; no 17 entry title rows duplicated as landing list items.
5. **AC-first-run:** full-list CTA URL, a section deep link, suggest-resource template URL, bug_report template URL all present.
6. **AC-meta / AC-links:** title `Awesome ArchiMate`; locked description string; canonical and og:url `https://jgsystemsconsulting.github.io/awesome-archimate/`; og:title; og:type `website`; `lang="en"`; licence-enquiry, CONTRIBUTING, LICENSE, issue-form URLs; maintainer string.
7. **AC-fonts-local / AC-plex-files:** all `@font-face` `src` values relative only; each face uses `font-display: swap` (or equivalent); zero `fonts.googleapis` / `fonts.gstatic` / remote `@import` in `docs/**/*.{html,css}`; four woff2 files exist under `docs/fonts/` and are referenced.
8. **AC-tokens / AC-light:** all thirteen R-V1 custom property declarations string-match; no `color-scheme: light dark`; light-only present.
9. **AC-a11y (source half):** `prefers-reduced-motion` present; `:focus-visible` with 2px outline and outline-offset 2px; single `h1`. Contrast AA, keyboard operability, and heading no-skip are **manual** (Step 1), not claimed by this grep.
10. **AC-responsive (source half):** primary CTA `min-height` (or equivalent) includes `44px` in CSS. Overflow at 390px is **manual** (Step 1).
11. **AC-anti-pattern:** no `linear-gradient(`; no `backdrop-filter`; no google fonts; no emoji in nav/hero chrome region.
12. **AC-rr-b-30:** only `docs/index.html` under `docs/**/*.html`.

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
python /tmp/verify_archimate_pages.py
```

- [ ] **Step 1: Manual a11y, responsive, and residual anti-pattern checks (required)**

Record pass/fail in the execute log (one line each). Do not skip.

1. Keyboard-tab nav anchors, primary CTA, and issue links; visible focus ring.
2. At ~390px width: no horizontal scrollbar; primary CTA height >= 44px.
3. Body and muted text contrast on bg meets WCAG AA (tooling or careful spot-check).
4. Heading levels do not skip under exposed sections.
5. Residual R-V7 (beyond verifier item 11): no glass/glow, no three equal feature cards, no violet/indigo default accent, no multi-hue tag carnival, no stock photos, no accordion-hidden catalogue, no centre-everything marketing theatre, no unthemed shadcn, designed stack is Plex (system fallback OK).

- [ ] **Step 2: AC-readme-freeze**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
git diff -- README.md
python /tmp/freeze_archimate_readme_catalogue.py /tmp/archimate-pages-freeze-after
diff -u /tmp/archimate-pages-freeze-before/contents.txt /tmp/archimate-pages-freeze-after/contents.txt
diff -u /tmp/archimate-pages-freeze-before/entries.txt /tmp/archimate-pages-freeze-after/entries.txt
```

Expected: empty diffs for the eight Contents lines and seventeen catalogue entry bullets. Default remains **no README edit**.

- [ ] **Step 3: AC-ci-freeze**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
git diff -- .github/workflows/links.yml .github/workflows/lint.yml .github/workflows/stale.yml .github/workflows/validate.yml
git hash-object .github/workflows/links.yml .github/workflows/lint.yml .github/workflows/stale.yml .github/workflows/validate.yml > /tmp/archimate-pages-ci-after.sha
diff -u /tmp/archimate-pages-ci-before.sha /tmp/archimate-pages-ci-after.sha
```

Expected: empty diffs.

- [ ] **Step 4: AC-notice re-check**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
grep -E "IBM Plex|OFL|docs/fonts" NOTICE
! grep -i "Third-party components are not distributed" NOTICE
test -f docs/fonts/OFL.txt
```

- [ ] **Step 5: AC-release**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
python scripts/check_release.py
```

Expected: `release gate: PASS` and exit 0. **Maps AC-release.**

Done when: verifier items 1-12 pass, **Step 1 manual checklist all pass**, freezes empty-diff, NOTICE/OFL checks pass, and `check_release.py` exits 0. Fix forward in Tasks 1-3 only; do not expand scope.

## Task 5: Stage design contracts and change set (commit notes)

**Files:**
- Add: `DESIGN.md`, `DESIGN_BRIEF.md` (currently untracked; F6)
- Already modified/created from prior tasks: `docs/index.html`, `docs/fonts/**`, `NOTICE`, optional `docs/site.css`, optional one-line `docs/DISTRIBUTION.md`

**Model:** flash

Plan notes only: **do not commit unless the user / execute track explicitly tells you to commit.**

- [ ] **Step 1: Review status**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
git status --short
git diff --stat
```

Expected tracked-to-be paths include at least:

- `docs/index.html`
- `docs/fonts/*`
- `NOTICE`
- `DESIGN.md`
- `DESIGN_BRIEF.md`
- optional `docs/site.css`
- optional `docs/DISTRIBUTION.md` (ledger note only)

Must **not** include README catalogue edits or workflow triad edits.

- [ ] **Step 2: AC-design-commit readiness**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
test -f DESIGN.md && test -f DESIGN_BRIEF.md
# After add (when told to commit):
# git add DESIGN.md DESIGN_BRIEF.md docs/index.html docs/fonts NOTICE
# optional: docs/site.css docs/DISTRIBUTION.md
# git status --short
```

- [ ] **Step 3: Suggested commit message (only when execute track authorizes commit)**

```text
feat(pages): DESIGN landing with self-hosted Plex

Restyle docs/index.html to pilot composition and DESIGN tokens.
Vendor IBM Plex Sans/Mono woff2 under docs/fonts with OFL.
Update NOTICE for vendored fonts. Track DESIGN.md and DESIGN_BRIEF.md.
```

- [ ] **Step 4: Final freeze + gate before any commit**

```bash
cd "C:/Users/gower/OneDrive/Documents/GitHub/awesome-archimate"
git diff -- README.md .github/workflows/links.yml .github/workflows/lint.yml .github/workflows/stale.yml .github/workflows/validate.yml
python /tmp/verify_archimate_pages.py
python scripts/check_release.py
```

Done when: change set is reviewable; DESIGN files present for F6; freezes hold; verifier + gate PASS. **AC-design-commit** is fully closed only when execute authorizes `git add` of DESIGN files (this task stages readiness; do not claim tracked until that commit). Commit only on explicit execute instruction.

## Acceptance criteria traceability

| AC | Where verified |
| --- | --- |
| AC-composition | Task 4 verifier item 1 |
| AC-cta | Task 4 verifier item 2 |
| AC-evidence | Task 4 verifier item 3 |
| AC-sections | Task 4 verifier item 4 |
| AC-first-run | Task 4 verifier item 5 |
| AC-meta | Task 4 verifier item 6 |
| AC-links | Task 4 verifier item 6 |
| AC-fonts-local | Task 4 verifier item 7 |
| AC-plex-files | Task 1 Step 5 + Task 4 verifier item 7 |
| AC-notice | Task 2 Step 2 + Task 4 Step 4 |
| AC-tokens | Task 4 verifier item 8 |
| AC-light | Task 4 verifier item 8 |
| AC-a11y | Task 4 verifier item 9 (source half) + Task 4 Step 1 manual (contrast, keyboard, heading order) |
| AC-responsive | Task 4 verifier item 10 (source half) + Task 4 Step 1 manual (390px overflow) |
| AC-anti-pattern | Task 3 Step 4 + Task 4 verifier item 11 (source) + Task 4 Step 1 residual R-V7 checklist |
| AC-readme-freeze | Task 0 Step 3 + Task 4 Step 2 |
| AC-ci-freeze | Task 0 Step 4 + Task 4 Step 3 |
| AC-design-commit | Task 5 |
| AC-release | Task 4 Step 5 (`python scripts/check_release.py`) |
| AC-rr-b-30 | Task 4 verifier item 12 |

## Out of scope (do not implement)

- Path N / Next / React / shadcn / lucide
- Mirroring 17 README entries onto the landing
- README seed or Contents edits
- Family CI triad or validate.yml edits
- Dark mode
- OG image, PWA, multi-page site
- Hub awesome-mbse product files (except this superpowers plan already written)
- design-intelligence repo edits
- Reopening F1-F6

## Risk checklist (from spec)

| Risk | Plan control |
| --- | --- |
| NOTICE vs vendored fonts | Task 2 before/with fonts |
| README seed edit | Task 0 freeze + Task 4 AC-readme-freeze; default no README touch |
| CDN habit | Task 4 AC-fonts-local |
| Entry mirror / multi-page | F4 + AC-sections + AC-rr-b-30 |
| check_release break | Task 4 Step 5 |
| Font bloat | Task 1 only four woff2 |
| Dual theme leftover | Task 4 AC-light |
| DESIGN untracked | Task 5 F6 |
| CI churn | Task 4 AC-ci-freeze |

## Deliverable summary

In `awesome-archimate`: vendor Plex under `docs/fonts/` + OFL; update NOTICE; rewrite `docs/index.html` to DESIGN composition and R-V1 tokens (light-only); leave README seed and CI triad alone; prove greps/ACs and `python scripts/check_release.py`; include `DESIGN.md` and `DESIGN_BRIEF.md` in the change set. Commit only when the execute track says so.
