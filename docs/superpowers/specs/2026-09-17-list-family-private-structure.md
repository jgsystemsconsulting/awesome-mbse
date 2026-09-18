# Spec: Private-first awesome-mbse list family structure

Date: 2026-09-17
Status: Draft for implementation (superpowers step 1)

## Problem

FAMILY.md declares a hub-and-spokes family, but the family is nearly invisible in practice.

- The hub README reduces the family to a two-line pointer and lists no spokes.
- Five planned spokes (archimate, capella, requirements-engineering, digital-engineering, stpa) exist only as registry rows.
- The one public spoke, awesome-sysml-v2, does not mention the family at all.
- The local awesome-magic-grid sibling is a full hub clone (titled Awesome MBSE, generated from `data/entries.yaml`), not a Magic Grid spoke.
- The hub is private on GitHub, so any family pointer from a public repo to hub URLs 404s for outsiders.

The user wants to see what the family could look like, structured as far as possible now, entirely in private, with explicit TODOs where repos must be created or found. Thin areas are acceptable when marked.

## Goals and non-goals

Goals:

1. The hub README shows the family: live, in development, planned, with honest statuses and gap callouts.
2. FAMILY.md becomes the private-mode operating manual: visibility per repo, private rules, external-list registry, per-spoke create checklists.
3. The public spoke gets a safe, link-free family pointer.
4. The local magic-grid sibling gets an honest status note without fighting its generator.
5. Every missing piece is an explicit TODO or GAP marker, never a silent gap.

Non-goals:

- Making any repo public or changing visibility anywhere.
- Creating GitHub repos, local git repos, or directories for planned spokes.
- Re-scoping awesome-magic-grid content (pruning `data/entries.yaml`, retitling) in this work.
- Any sindresorhus/awesome submission step.
- Pruning the hub's Magic Grid or Model Gallery depth while that spoke is not real.

## Locked decisions

| # | Decision |
|---|----------|
| D1 | Structure lives in hub README and FAMILY.md. Allowed sibling edits only: `../awesome-magic-grid/STATUS.md` (create) and one pointer line in `../awesome-sysml-v2/README.md`. No new repos, no new directories under the hub. |
| D2 | awesome-magic-grid: add a status note file only; content re-scope stays TODO. |
| D3 | awesome-sysml-v2: one text family pointer, no hyperlink to the private hub. If awesome-lint rejects the line, drop it and record the pointer as TODO under the live-spoke checklist in FAMILY.md; that path still passes acceptance. |
| D4 | Planned spokes exist as stub rows and FAMILY checklists, never as links or empty repos. |
| D5 | All edits stay local. No visibility changes, no pushes beyond what the user orders. |

**Status vocabulary (registry Status column only):** `Live` | `In development` | `Planned`. Visibility is a separate column and never appears inside Status cells.

**Marker vocabulary:** `GAP` means the niche has no adequate hub home today. `TODO` means a concrete next action is pending (create repo, re-check namespace, re-scope).

## Design

### 1. Hub README reshape

New section order after the maintainer blockquote:

1. `## List family` (new). One-line lead: this repo is the hub; the registry and family rules live in FAMILY.md. Then a table with columns: List, Scope, Status, Where the niche lives today.

   Rows use the FAMILY.md registry names exactly. Columns: List | Scope | Status | Where the niche lives today.

   | List | Status | Where the niche lives today |
   |------|--------|-----------------------------|
   | awesome-mbse | Live | This repo (hub and cross-cutting) |
   | awesome-sysml-v2 | Live | Linked public spoke (URL allowed; only existing live spoke exception) |
   | awesome-magic-grid | In development | Hub section Magic Grid and Cameo (no spoke URL) |
   | awesome-archimate | Planned | GAP (no dedicated hub section) |
   | awesome-capella | Planned | Broader Context Capella/Arcadia entries (thin) |
   | awesome-requirements-engineering | Planned | GAP (absent) |
   | awesome-digital-engineering | Planned | GAP (absent) |
   | awesome-stpa | Planned | Model Gallery DLR-FT STPA library (one entry, thin) |

   Rules for this section:

   - Never hyperlink a repo that does not exist. Planned rows and magic-grid are plain text names.
   - Status cells use only the Status vocabulary above and match FAMILY Status exactly. Visibility lives only in FAMILY.
   - Below the table, a short Gaps list naming RE, digital engineering, ArchiMate as GAP; STPA one entry; Capella four entries (Arcadia method page, Arcadia primer, py-capellambse, Eclipse Capella). Dated snapshot, not a permanent census.
   - Contents order after the lead: List family, then existing deep section anchors (Magic Grid, Model Gallery, Broader Context), then External awesome lists, then Support and security.

2. `## Contents` gains bullets for List family and External awesome lists in that order relative to deep sections as above.

3. `## External awesome lists` replaces `## The competitive landscape`. Keep a two-line "why this list exists" statement with the evidence date (gathered 2026-06). Convert the three competitor rows into family entry format. Worked example:

   `- [mycr0ft/awesome-sysml](https://github.com/mycr0ft/awesome-sysml) - Community SysML v2 tools and samples list; thin on Magic Grid and openable Cameo models \`SysMLv2\` \`external-list\` (2025).`

   Same shape for kktse/awesome-systems-engineering and rolling-robot/awesome-systems-engineering. Add TODO lines: namespace re-check on launch day for every planned spoke (capella/stpa rate-limited on 2026-09-17 list-family pass; archimate empty-ish; RE/DE probed in niche research but still re-check on create day).

4. All deep content sections (Magic Grid and Cameo, Model Gallery, Broader SysML / MBSE Context) are unchanged in this work. Per the FAMILY split rule, the hub shrinks a niche only when the spoke repo is real.

5. The current two-line "**List family:**" pointer paragraph is replaced by the new section, not duplicated.

CI impact: the only new outbound URL on the hub is the existing public awesome-sysml-v2 link in the family table (already a live family URL). Competitor URLs already exist. Lychee and awesome-lint configs need no change.

### 2. FAMILY.md expansion

a) Registry gains a Visibility column with values: public, private, local only, none yet.

- awesome-mbse: private.
- awesome-sysml-v2: public.
- awesome-magic-grid: local only. The row states plainly that no GitHub repo exists and the local working copy is a hub fork pending re-scope, not a niche spoke.
- The five planned rows: none yet, with their existing namespace-check dates.

b) New `## Private mode` section after `## Model`:

- Default state of every family repo is private until explicitly released.
- Entry links must still pass the public-availability inclusion bar. A private repo linking private resources still violates the bar (CHANGELOG 2026-06 precedent: jgs-magic-sysmlv2-mcp removed).
- Public spokes reference the family in text only while the hub is private. No FAMILY.md hyperlinks from public repos.
- sindresorhus submission is deferred to the future public-release runbook and is not part of private-structure work.
- Sweep badges, CI, and cadence are unchanged by privacy.

c) New `## External lists and namespaces` section:

- External registry table: list name, URL, coverage note, last-checked date (2026-06 for the three incumbent rows from the hub's old competitive table; 2026-09-17 for archimate).
- Namespace table for planned spokes: name, checked date, result, next action. awesome-archimate: checked 2026-09-17, empty-ish. awesome-capella and awesome-stpa: TODO re-check (rate-limited on the list-family pass). awesome-requirements-engineering and awesome-digital-engineering: niche research recorded org namespace free or thin incumbents; still TODO re-check on create day.

d) `## Starting a new list` gains a per-spoke checklist template plus one thin filled copy per planned spoke. Template checkboxes:

```markdown
- [ ] Namespace re-checked on YYYY-MM-DD (result: empty / incumbent found)
- [ ] Roughly 40 candidate entries gathered, all passing the inclusion bar
- [ ] Repo created (private) from the README skeleton
- [ ] Hub README family table row updated with the URL
- [ ] Registry status flipped to Live
```

Also add a **Live spoke alignment** checklist for awesome-sysml-v2 (not a create checklist):

```markdown
- [ ] Family pointer line present (text only while hub private)
- [ ] Last full sweep badge
- [ ] Entry tags and year tokens per family standard
- [ ] CONTRIBUTING year/dedupe/neutrality rules aligned
```

The checklists are the structure. Do not create the repos in this work.

e) Status honesty: the magic-grid registry row and the checklist note that the local copy runs a generator pipeline while the family standard mandates a hand-maintained table of contents. That conflict is surfaced and tracked in `../awesome-magic-grid/STATUS.md`, not resolved here.

Namespace result vocabulary for checklists and tables: `empty` | `incumbent found` | `TODO re-check`. Map "empty-ish" to `empty`.

### 3. awesome-magic-grid local sibling

Decision: no content re-scope in this work. The README is generated output (`scripts/generate.py` overwrites hand edits), and re-scoping means content curation: pruning `data/entries.yaml` to the Magic Grid niche, retitling, and deciding generator versus hand maintenance. That is list-building, not structure.

Action: add `STATUS.md` at that repo root with:

- One paragraph: this is a local fork of the awesome-mbse hub, not yet the awesome-magic-grid spoke; the family contract is awesome-mbse FAMILY.md.
- A TODO checklist: decide the final name and re-check the awesome-magic-grid namespace; prune `data/entries.yaml` to the niche or retire the generator for hand maintenance; retitle the generated README; create the private GitHub repo; register in FAMILY.md and the hub family table.
- A warning that README edits are overwritten by the generator, which is why the note is a separate file.

### 4. awesome-sysml-v2 public spoke

Decision: one text-only pointer line, placed under the intro line:

```markdown
> Part of the awesome-mbse list family (hub repository currently private).
```

No URL while the hub is private; a FAMILY.md link would 404 for public readers. Everything else the family standard requires of spokes (sweep badge, tags and years, CONTRIBUTING alignment) stays TODO in FAMILY's per-spoke checklist; honesty in the registry beats a rushed badge. If awesome-lint on that repo rejects the line, drop the line and record the pointer as TODO in FAMILY instead. Local edit only in this work; the user controls pushes to the public repo.

### 5. Stubs versus empty remote repos

Decided: in-hub stubs. The sindresorhus culture rejects empty and duplicate lists, the family's own bar is roughly 40 entries before a repo exists, and an empty repo creates future public cleanup. A planned spoke therefore exists as: a family table row, a gap callout where the hub is thin, and a per-spoke checklist. Nothing else.

## Acceptance criteria (privately verifiable)

Paths are relative to the hub repo root `awesome-mbse/` unless stated.

1. Hub README contains `## List family` and `## External awesome lists`; Contents lists both; the old `**List family:**` pointer paragraph is gone. Family table Status cells are only `Live` / `In development` / `Planned` and match FAMILY Status. Planned spoke names and `awesome-magic-grid` have no markdown link targets.
2. `rg -n "awesome-(archimate|capella|requirements-engineering|digital-engineering|stpa|magic-grid)" README.md FAMILY.md` shows no `](https://github.com/` on the same line as those names (except none for magic-grid / planned).
3. FAMILY.md has Visibility column with values public|private|local only|none yet for each registry row; sections `## Private mode` and `## External lists and namespaces`; five planned-spoke create checklists plus one live-spoke alignment checklist for awesome-sysml-v2, all with unchecked boxes where work remains.
4. `../awesome-magic-grid/STATUS.md` exists and names hub-fork state, generator overwrite risk, and re-scope TODOs.
5. Either `../awesome-sysml-v2/README.md` contains the text-only family pointer line and `rg -n "jgsystemsconsulting/awesome-mbse" ../awesome-sysml-v2` returns nothing, or the pointer is absent and FAMILY live-spoke checklist records the pointer as TODO (lint fallback).
6. Hub deep content untouched: count of `- [` lines under `## Magic Grid & Cameo` through the next `##` heading, and count of Model Gallery data rows (24 before), unchanged after.
7. Working tree shows no visibility metadata change; no new sindresorhus submission files. Process negatives are out of band: do not run `gh repo edit --visibility` or open submission PRs in this work.
8. Zero new em dashes in changed hub prose. Required markers present: GAP for archimate, RE, digital-engineering; TODO on planned-spoke checklists and namespace re-check lines.

## Risks

- awesome-lint on the public spoke may flag the pointer line; the fallback (drop the line, TODO in FAMILY) is documented.
- Removing the competitive-landscape table weakens the differentiation evidence; mitigated by keeping the dated why-this-exists line and per-list coverage notes in the new section.
- STATUS.md in magic-grid is outside the family standard's required file list; it is a private working note, deleted at re-scope.
- The generator-versus-hand-maintained conflict in magic-grid is surfaced, not solved; resolving it needs the re-scope conversation.

## Codebase context

From the context doc (`docs/superpowers/context/2026-09-17-list-family-private-structure-context.md`):

- FAMILY.md (129 lines) is the contract: model, registry, scope routing table, shared standard, start-a-list steps, README skeleton.
- The hub README carries only a two-line family pointer (lines 20-31 area) and no spoke links; deep content is the Magic Grid section, a 24-row Model Gallery table (README data rows under Model Gallery), and Broader Context.
- CHANGELOG 2026-06 shows the inclusion bar enforced against private links (jgs-magic-sysmlv2-mcp removed).
- CI: `link-check-pr.yml` plus a scheduled lychee sweep with `--include-fragments=anchor-only`; awesome-lint active; markdownlint listed in FAMILY but absent from hub CI (known drift, not fixed here).
- `../awesome-magic-grid`: generated README with AUTOGEN markers, `data/entries.yaml` plus `scripts/generate.py`, still titled Awesome MBSE.
- `../awesome-sysml-v2`: public, flat entry format without tags or years, no family pointer, no sweep badge.

## Research

- https://github.com/sindresorhus/awesome (meta-list pattern the hub mirrors privately)
- https://github.com/sindresorhus/awesome/blob/main/create-list.md (list-creation bar behind the 40-entry rule)
- https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md (submission bar, deferred)
- https://github.com/sindresorhus/awesome-lint (lint rules affecting the public spoke pointer)
- https://github.com/mycr0ft/awesome-sysml (external SysML list, first external registry row)
- https://github.com/topics/awesome (topic scale)
- https://github.com/search?q=awesome-archimate&type=repositories (namespace check, 2026-09)
- https://awesome.re (badge ecosystem)

Full findings: `docs/superpowers/research/2026-09-17-list-family-private-structure-research.md`
