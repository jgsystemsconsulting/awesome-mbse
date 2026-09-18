# Contributing

Thanks for helping keep this the best-curated MBSE / SysML index anywhere — with the
deepest Magic Grid / Cameo coverage around. Read this before opening a PR — the CI gates
enforce most of it.

The fastest path: open an [issue using the "Suggest a resource" form](../../issues/new/choose),
or open a pull request that edits `README.md` directly.

## 1. How to suggest a resource

- **Issue:** use the *Suggest a resource* form. Good for "I found this, you decide."
- **PR:** edit `README.md`, follow the entry format below, tick the PR checklist. CI
  link-checks your entry and lints the list.

## 2. Inclusion bar

An entry is accepted only if **all** hold:

1. **On-topic** — genuinely about MBSE practice or SysML v1/v2 (the Magic Grid / Cameo
   section or the broader-context section).
2. **Substantive** — it teaches, demonstrates, specifies, or provides something usable.
   Not a stub. Not pure vendor marketing.
3. **Live** — the link resolves right now.
4. **Not duplicative** — not already listed (see the canonical-URL rule, §6).
5. **Legally linkable** — publicly accessible. We **link**, we never re-host model files,
   PDFs, or proprietary content.

Tie-breakers (nice-to-have, not gates): has a real openable model (`has-model`), recently
updated, from a recognized source (OMG, INCOSE, Eclipse, Dassault, a university, an
established practitioner).

## 3. Entry format

One line per entry, **hyphen separator** (` - `, never an en/em-dash — awesome-lint
rejects those), tags as **inline code spans inside the sentence before the terminal
period**, year parenthesized as the last token:

```
- [Resource Name](https://example.com) - One-line factual description `SysMLv2` `Cameo` `has-model` `tutorial` (2024).
```

- **Description:** factual, one line, **≤ 140 characters** (measured from the first
  character after ` - ` to the last character before the first tag, excluding the link
  markup and tags). No hype.
- **`has-model`** means: a **directly downloadable, non-paywalled** file in a recognized
  model format (`.mdzip`, `.mdxml`, `.sysml`, `.uml`, or an Eclipse model project) that
  opens in a named tool. Screenshots, papers *describing* a model, and access-gated /
  request-only files **do not** qualify.

## 4. Tag vocabulary, cardinality & order

Tags appear in this fixed order, drawn **only** from this vocabulary:

`language → method → tool → has-model → type → spec/standard → paid → year`

| Axis | Cardinality | Values |
|------|-------------|--------|
| language | exactly 1 | `SysMLv1` · `SysMLv2` · `SysML-general` (version-agnostic: methodology, books, both-version docs — not a lazy default) |
| method | 0 or 1 | `MagicGrid` |
| tool | 0 or more | `Cameo` · `CATIA-Magic` · `Papyrus` · `Rhapsody` · `SysON` · `other-tool` |
| has-model | 0 or 1 | `has-model` |
| type | exactly 1 (dominant form) | `tutorial` · `course` · `book` · `paper` · `blog` · `video` · `tool` · `plugin` · `mcp` |
| spec/standard | 0 or 1 | `spec` · `standard` |
| paid | 0 or 1 | `paid` |
| year | exactly 1 | `(YYYY)` (see §5) |

- `other-tool` graduates to its own tag only once ≥ 3 entries share it.
- For an OMG/INCOSE normative document use `spec`/`standard` and omit `paper`.

## 5. The year rule (`YYYY`)

`(YYYY)` = the year of the resource's **most recent author-published version**:

- a paper → its publication year;
- a repo → its latest tagged release, or the latest default-branch commit if untagged;
- a course → its current cohort year.

**Trivial edits (typo fixes) don't count.** Examples:

- A 2019 paper with a 2024 typo-fix commit → `(2019)`.
- A repo whose latest release tag is `v2.1` from 2023 → `(2023)`.

## 6. Canonical-URL rule (dedupe)

Before deciding "is this a duplicate", canonicalize both URLs: force `https`, lowercase
the host, strip a trailing slash, drop the query string and fragment unless they're
semantically required. If the canonical forms match, it's a duplicate.

## 7. Editorial neutrality

This list is maintained by JG Systems Consulting Ltd., a commercial vendor of
SysML/Cameo tooling. To keep it trustworthy:

- JGS products are listed by the **same inclusion bar** as everything else.
- Every JGS entry sits next to **≥ 1 genuine competing/alternative entry**.
- **A superior competing tool is listed above a JGS one.** Neutrality is enforced by
  this rule, not by tone.

> **Table of Contents:** the `## Contents` ToC is hand-maintained and lists only the
> top-level sections (a flat ToC keeps awesome-lint happy). If you add or rename a
> **top-level** section, update the ToC by hand; sub-sections are not listed. CI validates
> every ToC anchor resolves (lychee `--include-fragments anchor-only`).

## 8. Cross-listing (Model Gallery)

Each `has-model` entry has **exactly one canonical home** — its section under *Magic Grid
& Cameo*. The **Model Gallery** is a *table* (not a list) of anchor links back to those
canonical entries — never duplicated entry text.

To make a model appear in the Gallery, write a matched **triple**:

```
<!-- canonical home, in its section: -->
<a id="resource-name"></a>
- [Resource Name](https://example.com) - Description `SysMLv2` `Cameo` `has-model` (2024).
```

```
<!-- Gallery row, in the Model Gallery table: -->
| [Resource Name](#resource-name) | Magic Grid › Example models | `Cameo` `has-model` `(2024)` |
```

**The `<a id>` value MUST equal the slugified resource name:** lowercase, spaces → `-`,
drop every character outside `[a-z0-9-]`, collapse repeats, append `-1`/`-2`… on
collision. (CI checks an anchor *exists*; it can't check the slug *matches the name* —
so get it right by following this rule and the worked example above.) The Gallery `Tags`
column is a convenience subset, not the canonical tag run.

## 9. Local link-check

No install needed — check your changed links with Docker:

```sh
docker run --rm -v "$PWD:/d" -w /d lycheeverse/lychee --include-fragments anchor-only README.md
```

Or just open a **draft PR** and let CI check it for you.

## 10. Maintenance cadence

The maintainers run a **quarterly sweep** (add new resources, prune rot), logged in
`CHANGELOG.md` with the date, and update the *Last full sweep* badge at the top of the
README each time. If it's been **> 6 months** since the last sweep, the badge flips to
"maintenance lapsed" — call it out in an issue.

## 11. Landing page truth

CI runs `scripts/check_release.py` on every push and PR to main (workflow `validate`).
The gate treats these landing-page bits as inputs (not freehand chrome):

- Chip `<dt>` names must stay exactly `version`, `sweep`, and `entries`. Their `<dd>`
  values must match the `Version:` field in `RELEASE-INFO.txt`, the README
  `Last full sweep: YYYY-MM` badge, and the curated bullet count.
- Curated bullets counted for the entries chip live only under these three README
  `##` sections: Magic Grid & Cameo / CATIA Magic, Broader SysML / MBSE Context,
  External awesome lists. Model Gallery is a pointer table and is not counted.
- The six section-index `<li>` href fragments must equal the GitHub slugs of these
  headings, in this order: List family, Magic Grid & Cameo / CATIA Magic, Model
  Gallery, Broader SysML / MBSE Context, External awesome lists, Support & security.
  Fragments today: `#list-family`, `#magic-grid--cameo--catia-magic`,
  `#model-gallery`, `#broader-sysml--mbse-context`, `#external-awesome-lists`,
  `#support--security`.
- Visible display text (labels around chip values, section-index link wording) may
  change. The gate reads names, values, and fragments only.

If you rename a top-level product section or bump version/sweep/entry count, update
`docs/index.html` in the same change.

