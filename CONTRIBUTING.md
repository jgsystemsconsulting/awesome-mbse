# Contributing

Thanks for helping keep this the best-curated MBSE / SysML index anywhere — with the
deepest Magic Grid / Cameo coverage around. Read this before opening a PR — the CI gates
enforce most of it.

> **`README.md` is generated — never edit it directly.** The list lives in
> [`data/entries.yaml`](data/entries.yaml) (the links) and [`data/tags.yaml`](data/tags.yaml)
> (the tag vocabulary). [`scripts/generate.py`](scripts/generate.py) renders `README.md`
> from them. Edit the data, regenerate, and commit both.

The fastest path: open an [issue using the "Suggest a resource" form](../../issues/new/choose)
— a maintainer adds the record for you, no tooling required. Or open a pull request that
edits `data/entries.yaml` (see below).

## 1. How to suggest a resource

- **Issue (no tools needed):** use the *Suggest a resource* form. Best if you can't run
  Python — a maintainer transcribes it into the data and regenerates.
- **PR:** add a record to `data/entries.yaml` (format in §3), run `python scripts/generate.py`,
  and commit both `data/entries.yaml` and the regenerated `README.md`. CI re-checks the
  data, link-checks, and lints the list.

## 2. Inclusion bar

An entry is accepted only if **all** hold:

1. **On-topic** — genuinely about MBSE practice or SysML v1/v2 (or an adjacent notation /
   language-general resource the list already covers).
2. **Substantive** — it teaches, demonstrates, specifies, or provides something usable.
   Not a stub. Not pure vendor marketing.
3. **Live** — the link resolves right now.
4. **Not duplicative** — not already listed (see the canonical-URL rule, §6).
5. **Legally linkable** — publicly accessible. We **link**, we never re-host model files,
   PDFs, or proprietary content.

Tie-breakers (nice-to-have, not gates): ships an openable model (`type: model`), recently
updated, from a recognized source (OMG, INCOSE, Eclipse, Dassault, a university, an
established practitioner).

## 3. Entry format (`data/entries.yaml`)

One YAML record per resource:

```yaml
- title: MagicGrid Book of Knowledge
  url: https://discover.3ds.com/magicgrid-book-of-knowledge
  desc: The definitive practitioner guide to the MagicGrid method
  date: 2021
  lang: sysml-v1          # spine section — see vocabulary below
  type: methodology       # resource type — see vocabulary below
  flagship: true          # OPTIONAL, sysml-v1 only — places it in the Magic Grid/Cameo marquee
  tags: [SysML-general, MagicGrid, Cameo, book]
```

- **`title`** doubles as the heading anchor — it must be **unique** (the generator errors
  on a slug collision; disambiguate the title rather than working around it).
- **`url`** must be `http(s)` — any other scheme is rejected.
- **`desc`** factual, one line, no hype. Don't end it with a period — the generator adds
  the tags and `(year).` tail.
- **`date`** the year as an integer (see §5).
- **`lang`** exactly one of: `sysml-v1` · `sysml-v2` · `uaf` · `arcadia` · `opm` · `oml` ·
  `cross-cutting` (language-general — methods, standards, communities that span notations).
- **`type`** exactly one of: `methodology` · `tutorial` · `course` · `book-paper` ·
  `model` · `tool` · `community` · `spec` · `api`.
- **`flagship: true`** is valid **only** when `lang: sysml-v1`; it pulls the entry into the
  marquee "Magic Grid & Cameo / CATIA Magic" subsection. Omit it otherwise.
- **`tags`** every value must be defined in `data/tags.yaml` (the generator errors on an
  unknown tag). Add a new tag there first, with a one-line meaning.

The generator validates all of this and fails closed, so a bad record stops CI with a
clear message.

## 4. Tag vocabulary (`data/tags.yaml`)

`data/tags.yaml` is the single authority for the controlled tag vocabulary and for which
tags are **tool tokens** (`tool: true`) that drive the *By tool* view. To add a tag:

```yaml
NewTag: {desc: "One-line meaning shown in the Tag legend"}
ToolName: {desc: "The tool's name", tool: true}   # tool: true -> appears as a By-tool group
```

Keep tags drawn from this vocabulary; the *Tag legend* view is generated from it, so every
tag is self-documenting. Tool tokens must be a subset of the vocabulary (the generator
enforces this).

## 5. The year rule (`date`)

`date` = the year of the resource's **most recent author-published version**:

- a paper → its publication year;
- a repo → its latest tagged release, or the latest default-branch commit if untagged;
- a course → its current cohort year.

**Trivial edits (typo fixes) don't count.** A 2019 paper with a 2024 typo-fix commit →
`date: 2019`. A repo whose latest release tag is `v2.1` from 2023 → `date: 2023`.

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

## 8. Generating & checking locally

You need Python **3.11** (the canonical version — use [pyenv](https://github.com/pyenv/pyenv)
or [asdf](https://asdf-vm.com/) to match it) and the pinned dependency:

```sh
pip install -r requirements.txt
python scripts/generate.py            # rewrite README.md from the data
python scripts/generate.py --check    # verify README.md matches the data (what CI runs)
python scripts/generate.py --self-check   # run the generator's built-in tests
```

**Enable the pre-commit hook once** so regeneration happens automatically before each commit:

```sh
pip install pre-commit && pre-commit install
```

CI runs three independent checks on every PR — `generate-check` (the data and both output
files are in sync and valid), `awesome-lint` (README structure), and `lychee` (links + ToC
anchors resolve). All three must pass. The four cross-views live in
[`docs/find-it-your-way.md`](docs/find-it-your-way.md) (also generated) so the README links
each resource exactly once and stays awesome-lint-clean.

## 9. Maintenance cadence

The maintainers run a **quarterly sweep** (add new resources, prune rot), logged in
`CHANGELOG.md` with the date, and update the *Last full sweep* badge at the top of the
README template each time. If it's been **> 6 months** since the last sweep, the badge
flips to "maintenance lapsed" — call it out in an issue.
