# Generator-driven `awesome-mbse` Restructure — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the hand-edited `README.md` into a build artifact generated from `data/*.yaml` + `README.template.md`, restructured by modelling language, with four cross-views and self-explaining "which notation fits whom" guidance.

**Architecture:** A single Python generator (`scripts/generate.py`) loads YAML entries + a tag legend, validates them fail-closed, and fills AUTOGEN marker blocks in a markdown template to produce a normalised `README.md`. CI verifies the committed README matches the data (`--check`), passes `awesome-lint`, and has no dead links (`lychee`). The generator carries its own assert-based self-check (`--self-check`) — no test framework.

**Tech Stack:** Python 3.11 (stdlib + pinned PyYAML), GitHub Actions, pre-commit, awesome-lint, lychee.

**Authoritative spec:** [docs/superpowers/specs/2026-06-24-generator-driven-language-restructure-design.md](../specs/2026-06-24-generator-driven-language-restructure-design.md) (hardened, spec-review converged in 4 rounds). Read it before starting.

---

## File structure

| File | Responsibility |
|---|---|
| `scripts/generate.py` | The whole generator: load → validate → render → fill template → write/check; plus `--self-check`. One focused module. |
| `data/entries.yaml` | Single source of truth — the list of entry records. |
| `data/tags.yaml` | Controlled tag vocabulary: `tag → {desc, tool?}`. Authority for the Tag-legend view + validation; `tool: true` marks By-tool grouping tokens. |
| `README.template.md` | All narrative prose (intro, "Choosing a notation" chooser, per-section "Use this when…" blurbs, competitive landscape, contributing, support) + AUTOGEN marker blocks. |
| `README.md` | **Generated output.** Committed (GitHub renders it), never hand-edited. |
| `requirements.txt` | `PyYAML==6.0.2` (pinned). |
| `.python-version` | `3.11` (canonical version). |
| `.pre-commit-config.yaml` | Local hook running the generator before commit. |
| `.github/workflows/generate-check.yml` | CI: `generate.py --check`, no token, runs every PR. |
| `.github/workflows/awesome-lint.yml` | CI: awesome-lint on committed README. |
| `.github/workflows/regenerate.yml` | Maintainer-gated rescue: regenerate + commit to PR branch (code from base, data from PR). |
| `CONTRIBUTING.md` | Updated: YAML record format, tag vocab, "never edit README.md directly", pre-commit + Python 3.11 + issue-form path. |

**Test mechanism (spec: "no test framework"):** every "test" step adds assertions to the generator's `self_check()` and runs `python scripts/generate.py --self-check`. Test-first = write the assertion, watch it fail, implement, watch it pass.

---

## Task 1: Scaffold + slug function (the historical CI pain point)

**Files:**
- Create: `requirements.txt`, `.python-version`, `scripts/generate.py`

- [ ] **Step 1: Pin the runtime**

`requirements.txt`:
```
PyYAML==6.0.2
```
`.python-version`:
```
3.11
```

- [ ] **Step 2: Write the generator skeleton with the slug self-check (test-first)**

Create `scripts/generate.py`:
```python
#!/usr/bin/env python3
"""Generate README.md for awesome-mbse from data/*.yaml + README.template.md.

Usage:
  python scripts/generate.py              # write README.md
  python scripts/generate.py --check      # verify README.md matches data (CI; exit!=0 on drift)
  python scripts/generate.py --self-check # run built-in assertions
"""
from __future__ import annotations
import sys, re, difflib, datetime
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
ENTRIES_FILE = ROOT / "data" / "entries.yaml"
TAGS_FILE = ROOT / "data" / "tags.yaml"
TEMPLATE_FILE = ROOT / "README.template.md"
OUTPUT_FILE = ROOT / "README.md"
CURRENT_YEAR = datetime.date.today().year  # only used for date upper-bound; never rendered

def slug(title: str) -> str:
    """GitHub heading-anchor algorithm. Do NOT 'tidy' — must match GitHub byte-for-byte.
    lowercase; keep [a-z0-9_- ] (strip other punctuation, NO replacement); space->hyphen;
    do not collapse or strip hyphens. 'Magic Grid & Cameo' -> 'magic-grid--cameo'."""
    s = title.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s, flags=re.UNICODE)  # \w keeps underscore, like GitHub
    return s.replace(" ", "-")

def self_check() -> None:
    # slug must match GitHub, including double-hyphen where punctuation sat between spaces
    assert slug("SysML v2") == "sysml-v2", slug("SysML v2")
    assert slug("Magic Grid & Cameo / CATIA Magic") == "magic-grid--cameo--catia-magic", \
        slug("Magic Grid & Cameo / CATIA Magic")
    assert slug("UAF & architecture frameworks") == "uaf--architecture-frameworks"
    print("self-check OK")

def main(argv: list[str]) -> int:
    if "--self-check" in argv:
        self_check(); return 0
    raise SystemExit("not implemented yet")

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
```

- [ ] **Step 3: Run the self-check — verify it passes**

Run: `python scripts/generate.py --self-check`
Expected: `self-check OK` (exit 0). If a slug assertion fails, the slug function is wrong — fix it, do not change the expected values (they are GitHub's truth).

- [ ] **Step 4: Commit**

```bash
git add requirements.txt .python-version scripts/generate.py
git commit -m "feat(generator): scaffold + GitHub-faithful slug with self-check"
```

---

## Task 2: Data files (tag legend + seed entries)

**Files:**
- Create: `data/tags.yaml`, `data/entries.yaml`

- [ ] **Step 1: Create the tag vocabulary**

`data/tags.yaml` (legend + tool flags; this is the authority validation checks against). Seed with the tags the current README already uses:
```yaml
# tag: {desc: "...", tool: true}   # tool:true marks a By-tool grouping token
SysML-general: {desc: "Applies across SysML versions / language-general"}
SysMLv1: {desc: "SysML version 1.x"}
SysMLv2: {desc: "SysML version 2.x (textual)"}
MagicGrid: {desc: "The MagicGrid modelling method"}
Cameo: {desc: "Cameo Systems Modeler / CATIA Magic", tool: true}
CATIA-Magic: {desc: "CATIA Magic (No Magic) platform", tool: true}
Papyrus: {desc: "Eclipse Papyrus", tool: true}
Rhapsody: {desc: "IBM Engineering Systems Design Rhapsody", tool: true}
SysON: {desc: "Eclipse SysON web modeler", tool: true}
Modelio: {desc: "Modelio open-source modeler", tool: true}
other-tool: {desc: "A tool outside the named set"}
book: {desc: "Book"}
paper: {desc: "Academic / technical paper"}
tutorial: {desc: "Hands-on tutorial"}
video: {desc: "Video resource"}
course: {desc: "Training course"}
paid: {desc: "Paid / commercial resource"}
spec: {desc: "Specification document"}
standard: {desc: "Standard / handbook"}
blog: {desc: "Blog / community site"}
plugin: {desc: "Tool plugin / profile"}
mcp: {desc: "Model Context Protocol server"}
tool: {desc: "Software tool"}
has-model: {desc: "Ships an openable model"}
```
> Note: `tool: true` tokens MUST be a subset of these keys (validation enforces it). Add `SysIDE`, `Capella`, `Gaphor` here with `tool: true` when their entries are migrated in Task 9.

- [ ] **Step 2: Create a small seed `data/entries.yaml` to develop against**

`data/entries.yaml` (full migration is Task 9; this seed exercises every code path — a flagship v1 entry, a v2 model, a cross-cutting entry, a two-tool entry):
```yaml
- title: MagicGrid Book of Knowledge
  url: https://discover.3ds.com/magicgrid-book-of-knowledge
  desc: The definitive practitioner guide to the MagicGrid method
  date: 2021
  lang: sysml-v1
  type: methodology
  flagship: true
  tags: [MagicGrid, Cameo, book]
- title: Eclipse Papyrus
  url: https://eclipse.dev/papyrus/
  desc: Industrial-grade open-source Eclipse modeling tool for UML with SysML support
  date: 2024
  lang: sysml-v1
  type: tool
  tags: [SysMLv1, Papyrus, tool]
- title: GfSE SysML v2 Models
  url: https://github.com/GfSE/SysML-v2-Models
  desc: Curated, CI-validated collection of SysML v2 models
  date: 2025
  lang: sysml-v2
  type: model
  tags: [SysMLv2, has-model]
- title: Survey of MBSE Methodologies (Estefan)
  url: https://www.omg.org/sysml/MBSE_Methodology_Survey_RevB.pdf
  desc: The standard comparative reference for MBSE methods
  date: 2008
  lang: cross-cutting
  type: methodology
  tags: [SysML-general, paper]
```

- [ ] **Step 3: Commit**

```bash
git add data/tags.yaml data/entries.yaml
git commit -m "feat(data): tag legend + seed entries"
```

---

## Task 3: Loading + fail-closed validation

**Files:**
- Modify: `scripts/generate.py`

- [ ] **Step 1: Add load + validation self-check assertions (test-first)**

Add to `self_check()` before the final `print`:
```python
    # --- validation fail-closed cases ---
    good = _fixture_entries()
    legend = _fixture_tags()
    validate(good, legend)  # must not raise

    def must_raise(mutate, needle):
        bad = [dict(e) for e in good]
        mutate(bad)
        try:
            validate(bad, legend)
        except ValueError as ex:
            assert needle in str(ex), f"wrong error: {ex}"
        else:
            raise AssertionError(f"expected ValueError containing {needle!r}")

    must_raise(lambda b: b[0].update(url=" JAVASCRIPT:alert(1)"), "url")
    must_raise(lambda b: b[1].update(flagship=True), "flagship")       # b[1] is sysml-v2
    must_raise(lambda b: b[0].update(lang="sysmlv2"), "lang")          # typo
    must_raise(lambda b: b[0].update(tags=["NotInLegend"]), "tag")
    must_raise(lambda b: b[0].update(title=b[1]["title"]), "slug")     # duplicate slug
    must_raise(lambda b: b[0].update(date=3000), "date")
```

Add fixtures + loaders + validator:
```python
LANGS = ["sysml-v1", "sysml-v2", "uaf", "arcadia", "opm", "oml", "cross-cutting"]
TYPES = ["methodology", "tutorial", "course", "book-paper", "model",
         "tool", "community", "spec", "api"]
REQUIRED = ("title", "url", "desc", "date", "lang", "type")

def _fixture_tags():
    return {"MagicGrid": {"desc": "x"}, "Cameo": {"desc": "x", "tool": True},
            "Papyrus": {"desc": "x", "tool": True}, "SysMLv2": {"desc": "x"},
            "book": {"desc": "x"}, "tool": {"desc": "x"}, "paper": {"desc": "x"},
            "has-model": {"desc": "x"}, "SysML-general": {"desc": "x"},
            "SysMLv1": {"desc": "x"}}

def _fixture_entries():
    return [
        {"title": "Alpha Guide", "url": "https://a.example", "desc": "d", "date": 2021,
         "lang": "sysml-v1", "type": "methodology", "flagship": True, "tags": ["MagicGrid"]},
        {"title": "Beta Models", "url": "https://b.example", "desc": "d", "date": 2025,
         "lang": "sysml-v2", "type": "model", "tags": ["SysMLv2", "has-model"]},
    ]

def load_yaml(path: Path):
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)   # safe_load only — never yaml.load (spec: Security)

def url_ok(url: str) -> bool:
    u = "".join(c for c in str(url).strip() if ord(c) >= 0x20)  # strip ws + control chars
    return u.lower().startswith(("https://", "http://"))        # scheme check on decoded form

def validate(entries: list[dict], legend: dict) -> None:
    tool_tokens = {t for t, meta in legend.items() if (meta or {}).get("tool")}
    missing_tools = tool_tokens - set(legend)
    if missing_tools:
        raise ValueError(f"tool tokens not in tag legend: {sorted(missing_tools)}")
    seen_slugs: dict[str, str] = {}
    for e in entries:
        who = e.get("title", "<no title>")
        for f in REQUIRED:
            if not e.get(f) and e.get(f) != 0:
                raise ValueError(f"entry {who!r}: missing required field {f!r}")
        if e["lang"] not in LANGS:
            raise ValueError(f"entry {who!r}: unknown lang {e['lang']!r}")
        if e["type"] not in TYPES:
            raise ValueError(f"entry {who!r}: unknown type {e['type']!r}")
        if e.get("flagship") and e["lang"] != "sysml-v1":
            raise ValueError(f"entry {who!r}: flagship only valid for sysml-v1")
        if not url_ok(e["url"]):
            raise ValueError(f"entry {who!r}: url scheme not allowed: {e['url']!r}")
        if not isinstance(e["date"], int) or not (1990 <= e["date"] <= CURRENT_YEAR + 1):
            raise ValueError(f"entry {who!r}: date out of range: {e['date']!r}")
        for t in e.get("tags", []):
            if t not in legend:
                raise ValueError(f"entry {who!r}: tag {t!r} not in legend")
        sg = slug(e["title"])
        if sg in seen_slugs:
            raise ValueError(f"entry {who!r}: slug {sg!r} collides with {seen_slugs[sg]!r}")
        seen_slugs[sg] = who
```

- [ ] **Step 2: Run self-check — verify it passes**

Run: `python scripts/generate.py --self-check`
Expected: `self-check OK`. Each `must_raise` confirms validation fails closed.

- [ ] **Step 3: Commit**

```bash
git add scripts/generate.py
git commit -m "feat(generator): fail-closed validation (yaml.safe_load, url allowlist, enums, slug uniqueness, tag coverage)"
```

---

## Task 4: Ordering + entry rendering + escaping

**Files:**
- Modify: `scripts/generate.py`

- [ ] **Step 1: Add rendering self-check assertions (test-first)**

Add to `self_check()`:
```python
    # ordering: date desc, then title asc (case-insensitive)
    ordered = order(_fixture_entries() + [
        {"title": "Aardvark", "url": "https://z.example", "desc": "d", "date": 2025,
         "lang": "sysml-v2", "type": "tool", "tags": ["tool"]}])
    assert [e["title"] for e in ordered][:2] == ["Aardvark", "Beta Models"], \
        [e["title"] for e in ordered]
    # escaping: pipe and brackets neutralised; url left intact
    line = render_entry({"title": "A|B [x]", "url": "https://h.example",
                         "desc": "d (note)", "date": 2020, "lang": "sysml-v1",
                         "type": "tool", "tags": ["tool"]})
    assert "A\\|B \\[x\\]" in line and "https://h.example" in line, line
    assert "(2020)." in line, line
```

Add functions:
```python
def order(entries: list[dict]) -> list[dict]:
    return sorted(entries, key=lambda e: (-int(e["date"]), e["title"].lower()))

def esc(text: str) -> str:
    out = str(text)
    for ch in "\\[]()!|<>`":   # backslash first
        out = out.replace(ch, "\\" + ch)
    return out

def render_entry(e: dict) -> str:
    title = esc(e["title"])
    desc = esc(str(e["desc"]).rstrip(" ."))
    tags = " ".join(f"`{t}`" for t in e.get("tags", []))
    tail = f" {tags}" if tags else ""
    return f"- [{title}]({e['url']}) - {desc}.{tail} ({e['date']})."
```

- [ ] **Step 2: Run self-check — verify it passes**

Run: `python scripts/generate.py --self-check`
Expected: `self-check OK`.

- [ ] **Step 3: Commit**

```bash
git add scripts/generate.py
git commit -m "feat(generator): deterministic ordering + escaped entry rendering"
```

---

## Task 5: Spine rendering (marquee, type subsections, empty-skip)

**Files:**
- Modify: `scripts/generate.py`

- [ ] **Step 1: Add spine self-check assertions (test-first)**

Add to `self_check()`:
```python
    blocks = render_spine(_fixture_entries(), _fixture_tags())
    v1 = blocks["sysml-v1"]
    assert "### Magic Grid & Cameo / CATIA Magic" in v1, v1   # flagship marquee present
    assert "Alpha Guide" in v1
    assert "### Tutorials" not in v1                          # empty subsection skipped
    v2 = blocks["sysml-v2"]
    assert "### Example models" in v2 and "Beta Models" in v2
    assert "view-by-tool" not in blocks                       # spine has only lang ids
    for lang_id in blocks:
        assert lang_id in LANGS
```

Add functions:
```python
LANG_TITLES = {
    "sysml-v1": "SysML v1", "sysml-v2": "SysML v2",
    "uaf": "UAF & architecture frameworks",
    "arcadia": "Arcadia / Capella", "opm": "OPM", "oml": "OML",
    "cross-cutting": "Cross-cutting (language-general)",
}
TYPE_TITLES = {
    "methodology": "Methodology & guides", "tutorial": "Tutorials",
    "course": "Courses & learning paths", "book-paper": "Books & papers",
    "model": "Example models", "tool": "Tools, plugins & automation",
    "community": "Communities & blogs", "spec": "Specifications & standards",
    "api": "APIs & automation",
}
ADJACENT = {"arcadia", "opm", "oml"}        # rendered as H3 under a prose H2
MARQUEE_TITLE = "Magic Grid & Cameo / CATIA Magic"

def _type_subsections(entries: list[dict], heading: str) -> list[str]:
    out = []
    for t in TYPES:
        group = order([e for e in entries if e["type"] == t])
        if not group:
            continue                              # empty subsection -> no heading
        out.append(f"{heading} {TYPE_TITLES[t]}\n")
        out.extend(render_entry(e) for e in group)
        out.append("")
    return out

def render_spine(entries: list[dict], legend: dict) -> dict[str, str]:
    """Return {lang_id: markdown}. Every record lands in exactly one lang block."""
    blocks: dict[str, str] = {}
    for lang in LANGS:
        here = [e for e in entries if e["lang"] == lang]
        lines: list[str] = []
        sub_heading = "###" if lang not in ADJACENT else "####"
        if lang in ADJACENT:
            lines.append(f"### {LANG_TITLES[lang]}\n")   # H3 under the prose H2
        if lang == "sysml-v1":
            flagship = order([e for e in here if e.get("flagship")])
            if flagship:
                lines.append(f"### {MARQUEE_TITLE}\n")
                lines.extend(render_entry(e) for e in flagship)
                lines.append("")
            rest = [e for e in here if not e.get("flagship")]
            lines.extend(_type_subsections(rest, sub_heading))
        else:
            lines.extend(_type_subsections(here, sub_heading))
        blocks[lang] = "\n".join(lines).rstrip() + "\n"
    return blocks
```

- [ ] **Step 2: Run self-check — verify it passes**

Run: `python scripts/generate.py --self-check`
Expected: `self-check OK`.

- [ ] **Step 3: Commit**

```bash
git add scripts/generate.py
git commit -m "feat(generator): spine rendering with flagship marquee + empty-subsection skip"
```

---

## Task 6: The four views + view-consistency assertion

**Files:**
- Modify: `scripts/generate.py`

- [ ] **Step 1: Add view self-check assertions (test-first)**

Add to `self_check()`:
```python
    two_tool = {"title": "Dual Tool", "url": "https://d.example", "desc": "d",
                "date": 2024, "lang": "sysml-v1", "type": "tool",
                "tags": ["Cameo", "Papyrus"]}
    es = _fixture_entries() + [two_tool]
    views = render_views(es, _fixture_tags())
    assert "Beta Models" in views["view-openable-models"]            # type==model
    assert "Alpha Guide" not in views["view-openable-models"]
    assert views["view-by-tool"].count("Dual Tool") == 2            # appears under both tools
    assert "### Cameo" in views["view-by-tool"] and "### Papyrus" in views["view-by-tool"]
    assert "Cameo" in views["view-tag-legend"]                       # legend rendered
    # view-consistency: N tool tags -> N groups; openable rows == count(type==model)
    assert_view_consistency(es, views)
```

Add functions:
```python
def _tool_tokens(legend: dict) -> list[str]:
    return [t for t in legend if (legend[t] or {}).get("tool")]

def render_views(entries: list[dict], legend: dict) -> dict[str, str]:
    v: dict[str, str] = {}
    # Openable models
    models = order([e for e in entries if e["type"] == "model"])
    rows = ["| Model | Home | Tags |", "| --- | --- | --- |"]
    for e in models:
        home = f"[{LANG_TITLES[e['lang']]}](#{slug(LANG_TITLES[e['lang']])})"
        tags = " ".join(f"`{t}`" for t in e.get("tags", []))
        rows.append(f"| [{esc(e['title'])}](#{slug(e['title'])}) | {home} | {tags} |")
    v["view-openable-models"] = "\n".join(rows) + "\n"
    # By tool
    parts = []
    for tok in _tool_tokens(legend):
        group = order([e for e in entries if tok in e.get("tags", [])])
        if not group:
            continue
        parts.append(f"### {tok}\n")
        parts.extend(f"- [{esc(e['title'])}](#{slug(e['title'])})" for e in group)
        parts.append("")
    v["view-by-tool"] = "\n".join(parts).rstrip() + "\n"
    # By resource type
    parts = []
    for t in TYPES:
        group = order([e for e in entries if e["type"] == t])
        if not group:
            continue
        parts.append(f"### {TYPE_TITLES[t]}\n")
        parts.extend(f"- [{esc(e['title'])}](#{slug(e['title'])})" for e in group)
        parts.append("")
    v["view-by-type"] = "\n".join(parts).rstrip() + "\n"
    # Tag legend
    rows = ["| Tag | Meaning |", "| --- | --- |"]
    for tag in sorted(legend):
        rows.append(f"| `{tag}` | {esc(legend[tag]['desc'])} |")
    v["view-tag-legend"] = "\n".join(rows) + "\n"
    return v

def assert_view_consistency(entries: list[dict], views: dict[str, str]) -> None:
    model_rows = sum(1 for ln in views["view-openable-models"].splitlines()
                     if ln.startswith("| [") )
    n_models = sum(1 for e in entries if e["type"] == "model")
    if model_rows != n_models:
        raise ValueError(f"openable-models rows {model_rows} != count(model) {n_models}")
```

- [ ] **Step 2: Run self-check — verify it passes**

Run: `python scripts/generate.py --self-check`
Expected: `self-check OK`.

- [ ] **Step 3: Commit**

```bash
git add scripts/generate.py
git commit -m "feat(generator): four cross-views + view-consistency assertion"
```

---

## Task 7: Template fill, Contents/ToC, blurb check, count invariant, write + --check

**Files:**
- Modify: `scripts/generate.py`

- [ ] **Step 1: Add template/marker/blurb/check self-check assertions (test-first)**

Add to `self_check()`:
```python
    tmpl = (
        "# Awesome MBSE\n\n## Contents\n"
        "<!-- AUTOGEN:START section=contents -->\n<!-- AUTOGEN:END section=contents -->\n\n"
        "## SysML v1\nUse this when you run Cameo today. It is the stable incumbent.\n"
        "<!-- AUTOGEN:START section=sysml-v1 -->\n<!-- AUTOGEN:END section=sysml-v1 -->\n\n"
        "## SysML v2\nUse this when greenfield and text-friendly.\n"
        "<!-- AUTOGEN:START section=sysml-v2 -->\n<!-- AUTOGEN:END section=sysml-v2 -->\n"
    )
    expected_markers = {"contents", "sysml-v1", "sysml-v2"}
    check_markers(tmpl, expected_markers)                       # must not raise
    check_blurbs(tmpl, ["sysml-v1", "sysml-v2"])               # blurbs present -> ok
    # missing blurb fails
    nob = tmpl.replace("Use this when greenfield and text-friendly.\n", "")
    try:
        check_blurbs(nob, ["sysml-v1", "sysml-v2"]); raise AssertionError("blurb check missed")
    except ValueError as ex:
        assert "blurb" in str(ex), ex
    # count invariant: every record placed once
    spine = render_spine(_fixture_entries(), _fixture_tags())
    check_count_invariant(_fixture_entries(), spine)            # must not raise
    # normalisation: CRLF/BOM compares clean
    assert normalise("﻿a\r\nb\r\n") == "a\nb\n", repr(normalise("﻿a\r\nb\r\n"))
```

Add functions:
```python
MARKER_RE = re.compile(r"<!-- AUTOGEN:(START|END) section=([a-z0-9-]+) -->")
VIEW_IDS = ["view-openable-models", "view-by-tool", "view-by-type", "view-tag-legend"]

def expected_marker_set() -> set[str]:
    return {"contents", *LANGS, *VIEW_IDS}

def check_markers(template: str, expected: set[str]) -> None:
    pairs: dict[str, list[str]] = {}
    for kind, sect in MARKER_RE.findall(template):
        pairs.setdefault(sect, []).append(kind)
    for sect in expected:
        seq = pairs.get(sect, [])
        if seq != ["START", "END"]:
            raise ValueError(f"marker {sect!r}: expected one START+END pair, got {seq}")
    unknown = set(pairs) - expected
    if unknown:
        raise ValueError(f"unknown AUTOGEN markers: {sorted(unknown)}")

def check_blurbs(template: str, lang_ids: list[str]) -> None:
    """Each ## notation section's text between its heading and AUTOGEN:START must be non-empty."""
    for lang in lang_ids:
        title = re.escape(LANG_TITLES[lang]) if lang not in ADJACENT else \
                re.escape("Adjacent & non-SysML notations")
        m = re.search(rf"^## {title}\s*\n(.*?)<!-- AUTOGEN:START section={lang} -->",
                      template, re.S | re.M)
        if not m or not m.group(1).strip():
            raise ValueError(f"missing 'Use this when' blurb for section {lang!r}")

def check_count_invariant(entries: list[dict], spine: dict[str, str]) -> None:
    placed = sum(1 for e in entries
                 if (f"](" + e["url"] + ")") in spine.get(e["lang"], ""))
    if placed != len(entries):
        raise ValueError(f"count invariant: placed {placed} != records {len(entries)}")
    marquee = spine.get("sysml-v1", "")
    flag_rendered = sum(1 for e in entries
                        if e.get("flagship") and (f"]({e['url']})") in marquee)
    n_flag = sum(1 for e in entries if e.get("flagship"))
    if flag_rendered != n_flag:
        raise ValueError(f"marquee count {flag_rendered} != flagship {n_flag}")

def normalise(text: str) -> str:
    return text.replace("﻿", "").replace("\r\n", "\n").replace("\r", "\n")

def render_toc(template: str) -> str:
    """ToC links every '## ' heading in the template, using the GitHub slug fn."""
    out = []
    for line in template.splitlines():
        m = re.match(r"^## (.+)$", line)
        if m and "Contents" not in m.group(1):
            out.append(f"- [{m.group(1)}](#{slug(m.group(1))})")
    return "\n".join(out) + "\n"

def fill(template: str, blocks: dict[str, str]) -> str:
    def repl(section: str, body: str) -> None:
        nonlocal template
        pat = re.compile(
            rf"(<!-- AUTOGEN:START section={re.escape(section)} -->\n).*?"
            rf"(\n<!-- AUTOGEN:END section={re.escape(section)} -->)", re.S)
        template = pat.sub(lambda m: m.group(1) + body.rstrip("\n") + m.group(2), template)
    for section, body in blocks.items():
        repl(section, body)
    return template

def build(entries: list[dict], legend: dict, template: str) -> str:
    validate(entries, legend)
    check_markers(template, expected_marker_set())
    check_blurbs(template, [l for l in LANGS if l not in ADJACENT] + ["arcadia"])
    spine = render_spine(entries, legend)
    check_count_invariant(entries, spine)
    views = render_views(entries, legend)
    assert_view_consistency(entries, views)
    blocks = {"contents": render_toc(template), **spine, **views}
    return normalise(fill(template, blocks)).rstrip("\n") + "\n"

def generate() -> str:
    entries = load_yaml(ENTRIES_FILE)
    legend = load_yaml(TAGS_FILE)
    template = TEMPLATE_FILE.read_text(encoding="utf-8")
    return build(entries, legend, template)
```

Wire `main()`:
```python
def main(argv: list[str]) -> int:
    if "--self-check" in argv:
        self_check(); return 0
    rendered = generate()
    if "--check" in argv:
        current = normalise(OUTPUT_FILE.read_text(encoding="utf-8")) if OUTPUT_FILE.exists() else ""
        if current != rendered:
            sys.stdout.writelines(difflib.unified_diff(
                current.splitlines(True), rendered.splitlines(True),
                "README.md (committed)", "README.md (regenerated)"))
            return 1
        print("README.md up to date"); return 0
    OUTPUT_FILE.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_FILE}"); return 0
```

> **Note for the implementer:** `check_blurbs` for the adjacent group keys on the H2 "Adjacent & non-SysML notations" with `section=arcadia` as its first marker; that is why `build` passes `+ ["arcadia"]` and not `opm`/`oml`. The H2 has one shared blurb.

- [ ] **Step 2: Run self-check — verify it passes**

Run: `python scripts/generate.py --self-check`
Expected: `self-check OK`.

- [ ] **Step 3: Commit**

```bash
git add scripts/generate.py
git commit -m "feat(generator): ToC, marker fill, blurb + count-invariant checks, --check + write modes"
```

---

## Task 8: Author `README.template.md`

**Files:**
- Create: `README.template.md`
- Reference: current `README.md` (for the prose to preserve)

- [ ] **Step 1: Write the template**

Port the existing prose, add the chooser + per-section blurbs, and place the marker blocks. Skeleton (fill the prose from the current README; every `##` notation section needs a real "Use this when…" blurb):
```markdown
# Awesome MBSE [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated, vetted, dated index of Model-Based Systems Engineering...
> (port the existing intro + maintainer-neutrality note verbatim)

### Choosing a notation

- **Run Cameo / a programme today** → SysML v1 · Magic Grid.
- **Greenfield, text-friendly, tool-flexible** → SysML v2.
- **Defence / enterprise architecture** → UAF & architecture frameworks.
- **Eclipse / non-SysML world** → Adjacent & non-SysML notations.
- **Just want an openable model** → Find it your way › Openable models.

## Contents
<!-- AUTOGEN:START section=contents -->
<!-- AUTOGEN:END section=contents -->

## SysML v1
Use this when you already model in Cameo/CATIA Magic or your programme mandates it. SysML v1 is the stable incumbent with the deepest tool support; the Magic Grid method below is the standout coverage here.
<!-- AUTOGEN:START section=sysml-v1 -->
<!-- AUTOGEN:END section=sysml-v1 -->

## SysML v2
Use this when starting fresh and you want a textual, tool-portable model. SysML v2 is the released successor with a large open `.sysml` corpus and a growing toolchain.
<!-- AUTOGEN:START section=sysml-v2 -->
<!-- AUTOGEN:END section=sysml-v2 -->

## UAF & architecture frameworks
Use this when you build defence or enterprise architectures. UAF is the modern OMG framework (it supersedes UPDM/DoDAF/MODAF) and runs natively in Cameo.
<!-- AUTOGEN:START section=uaf -->
<!-- AUTOGEN:END section=uaf -->

## Adjacent & non-SysML notations
Use this when your toolchain is Eclipse-based or you work in a non-SysML notation. Arcadia/Capella, OPM, and OML each bring their own method and tooling.
<!-- AUTOGEN:START section=arcadia -->
<!-- AUTOGEN:END section=arcadia -->
<!-- AUTOGEN:START section=opm -->
<!-- AUTOGEN:END section=opm -->
<!-- AUTOGEN:START section=oml -->
<!-- AUTOGEN:END section=oml -->

## Cross-cutting (language-general)
Use this when the resource applies regardless of notation — methods, standards, and communities that span SysML v1, v2, and beyond.
<!-- AUTOGEN:START section=cross-cutting -->
<!-- AUTOGEN:END section=cross-cutting -->

## Find it your way

### Openable models
<!-- AUTOGEN:START section=view-openable-models -->
<!-- AUTOGEN:END section=view-openable-models -->

### By tool
<!-- AUTOGEN:START section=view-by-tool -->
<!-- AUTOGEN:END section=view-by-tool -->

### By resource type
<!-- AUTOGEN:START section=view-by-type -->
<!-- AUTOGEN:END section=view-by-type -->

### Tag legend
<!-- AUTOGEN:START section=view-tag-legend -->
<!-- AUTOGEN:END section=view-tag-legend -->

## The competitive landscape
(port the existing competitive-landscape prose + table verbatim)

## Contributing
(port; then update in Task 11)

## Support & security
(port verbatim)

---

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the maintainers have waived all copyright...
```

- [ ] **Step 2: Generate against the seed data and eyeball it**

Run: `python scripts/generate.py && python scripts/generate.py --check`
Expected: `wrote .../README.md` then `README.md up to date`. Open `README.md`; confirm the four seed entries land in the right sections, the marquee shows "Alpha Guide", and the views populate.

- [ ] **Step 3: Commit**

```bash
git add README.template.md README.md
git commit -m "feat: README template (chooser + per-notation blurbs + AUTOGEN markers) and first generated README"
```

---

## Task 9: Migrate all ~80 entries (mechanical, verified)

**Files:**
- Modify: `data/entries.yaml`, `data/tags.yaml`
- Reference: the pre-restructure `README.md` (use `git show <pre-task-1-commit>:README.md` to read the original list)

- [ ] **Step 1: Transcribe every entry**

For each link in the original README, add a record to `data/entries.yaml`. Assign:
- `lang` from its original section (Magic Grid section → `sysml-v1` + `flagship: true`; "Broader context" v1 tools → `sysml-v1`; SysML v2 items → `sysml-v2`; UAF/frameworks → `uaf`; Capella/OPM/OML → `arcadia`/`opm`/`oml`; methods/standards/communities tagged `SysML-general` → `cross-cutting`).
- `type` from its original subsection (Methodology & guides → `methodology`, Example models / Model Gallery rows → `model`, Tools → `tool`, Specifications & standards → `spec`, APIs & automation → `api`, etc.).
- `tags`/`date` from the existing inline tags and `(YYYY)`.
Add any missing tool tokens (`SysIDE`, `Capella`, `Gaphor`, …) to `data/tags.yaml` with `tool: true` where they are tools.

This is mechanical but human-judged. Acceptance criterion: the generator's count invariant passes AND a manual diff shows no dropped entry (next steps verify both).

- [ ] **Step 2: Generate and let validation + invariants gate it**

Run: `python scripts/generate.py`
Expected: `wrote .../README.md` with no `ValueError`. If validation fails, fix the offending record (the message names it). The count invariant guarantees every record is placed.

- [ ] **Step 3: Diff against the original to confirm no link lost**

Run:
```bash
git show HEAD~8:README.md | grep -oE 'https?://[^)]+' | sort -u > /tmp/old-urls.txt
grep -oE 'https?://[^)]+' README.md | sort -u > /tmp/new-urls.txt
comm -23 /tmp/old-urls.txt /tmp/new-urls.txt
```
(adjust `HEAD~8` to the commit before Task 1). Expected: empty output (every original URL still present). Investigate any line printed.

- [ ] **Step 4: Commit**

```bash
git add data/entries.yaml data/tags.yaml README.md
git commit -m "feat(data): migrate all README entries into entries.yaml; regenerate"
```

---

## Task 10: CI workflows + pre-commit

**Files:**
- Create: `.github/workflows/generate-check.yml`, `.github/workflows/awesome-lint.yml`, `.github/workflows/regenerate.yml`, `.pre-commit-config.yaml`

- [ ] **Step 1: `generate-check` (no token, every PR)**

`.github/workflows/generate-check.yml`:
```yaml
name: generate-check
on:
  pull_request:
permissions:
  contents: read           # no token needed; runs contributor code, so holds none
jobs:
  generate-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version-file: ".python-version"
      - run: pip install -r requirements.txt
      - run: python scripts/generate.py --self-check
      - run: python scripts/generate.py --check
```

- [ ] **Step 2: `awesome-lint` (named required job)**

`.github/workflows/awesome-lint.yml`:
```yaml
name: awesome-lint
on:
  pull_request:
permissions:
  contents: read
jobs:
  awesome-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: "20"
      - run: npx awesome-lint
```

- [ ] **Step 3: `regenerate` rescue (maintainer-gated; code from base, data from PR)**

`.github/workflows/regenerate.yml`:
```yaml
name: regenerate (maintainer rescue)
on:
  workflow_dispatch:
    inputs:
      pr:
        description: "PR number to regenerate"
        required: true
permissions:
  contents: write
jobs:
  regenerate:
    runs-on: ubuntu-latest
    steps:
      # CRITICAL: code (generate.py, template) comes from the BASE branch (this checkout),
      # NOT the PR head — never run contributor code with the write token.
      - uses: actions/checkout@v4
      - name: Fetch only the PR's data files
        env:
          GH_TOKEN: ${{ github.token }}
        run: |
          gh pr checkout ${{ inputs.pr }} -- data/   # data only; code stays from base
          can=$(gh pr view ${{ inputs.pr }} --json maintainerCanModify -q .maintainerCanModify)
          if [ "$can" != "true" ]; then
            gh pr comment ${{ inputs.pr }} --body "Enable 'Allow edits by maintainers' so I can push the regenerated README, or run \`python scripts/generate.py\` and commit it yourself."
            exit 1
          fi
      - uses: actions/setup-python@v5
        with:
          python-version-file: ".python-version"
      - run: pip install -r requirements.txt
      - run: python scripts/generate.py        # base-branch generator, PR data
      - name: Commit regenerated README to the PR branch
        env:
          GH_TOKEN: ${{ github.token }}
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git commit -am "chore: regenerate README.md" || echo "nothing to regenerate"
          git push
```
> Implementer note: `gh pr checkout ... -- data/` keeps `scripts/` and `README.template.md` at the base-branch versions. If a cleaner isolation is needed, copy `data/` out of the PR via the API into a base checkout. The non-negotiable rule (spec §Security): the generator code executed here must be the base-branch copy.

- [ ] **Step 4: pre-commit hook**

`.pre-commit-config.yaml`:
```yaml
repos:
  - repo: local
    hooks:
      - id: generate-readme
        name: regenerate README.md
        entry: python scripts/generate.py
        language: system
        pass_filenames: false
        files: ^(data/.*\.yaml|README\.template\.md|scripts/generate\.py)$
```

- [ ] **Step 5: Verify locally**

Run: `python scripts/generate.py --self-check && python scripts/generate.py --check && npx awesome-lint`
Expected: self-check OK; README up to date; awesome-lint passes (fix any structural finding in the template, regenerate, re-run).

- [ ] **Step 6: Commit**

```bash
git add .github/workflows/generate-check.yml .github/workflows/awesome-lint.yml .github/workflows/regenerate.yml .pre-commit-config.yaml
git commit -m "ci: generate-check + awesome-lint + maintainer regenerate; pre-commit hook"
```

---

## Task 11: Update CONTRIBUTING + issue form

**Files:**
- Modify: `CONTRIBUTING.md`
- Modify: `.github/ISSUE_TEMPLATE/*` (the suggest-a-resource form)

- [ ] **Step 1: Rewrite the contribution instructions**

In `CONTRIBUTING.md`, replace the raw-markdown-line format with:
- **Never edit `README.md` directly — it is generated.** Edit `data/entries.yaml`.
- The YAML record format (copy the Task 2 example) and the field vocabulary (`lang`, `type`, `flagship`, `tags`, `date`).
- The tag vocabulary lives in `data/tags.yaml`; add a new tag there before using it.
- Enable the hook once: `pip install pre-commit && pre-commit install`. Python 3.11 is canonical (use pyenv/asdf).
- Non-Python contributors: use the suggest-a-resource issue form; a maintainer adds the record.
- Keep the editorial-neutrality section (§7) unchanged.

- [ ] **Step 2: Point the issue form at the YAML fields**

Update the suggest-a-resource issue form fields to collect: title, url, one-line description, suggested `lang`, suggested `type`, tags, year — matching the record schema.

- [ ] **Step 3: Verify links still resolve**

Run: `npx awesome-lint && python scripts/generate.py --check`
Expected: both clean (CONTRIBUTING changes don't affect the generated README; this confirms nothing regressed).

- [ ] **Step 4: Commit**

```bash
git add CONTRIBUTING.md .github/ISSUE_TEMPLATE
git commit -m "docs: contribution workflow for the data-driven generator"
```

---

## Self-review notes (author)

- **Spec coverage:** architecture/files (T1,T8,T10), data model + tag legend (T2), validation rules incl. blurb presence + tool-subset + template integrity (T3,T7), slug algorithm GitHub-faithful (T1), ordering (T4), security (safe_load/url allowlist/escaping in T3–T4; CI trust boundary + base-branch rescue in T10), spine + marquee + empty-skip (T5), four views + consistency (T6), AUTOGEN markers + ToC + count invariant + --check normalisation (T7), notation guidance (T8), awesome-lint job (T10), maintainer rescue + pre-commit + pinning (T10), migration with count + diff verification (T9), CONTRIBUTING/issue form (T11). Success criteria map to T7 (--check), T10 (awesome-lint/lychee jobs — lychee already exists), T6/T9 (invariants), T8 (chooser+blurbs), T3 (fail-closed).
- **Manual/human-gated step:** Task 9 transcription is mechanical-with-judgement; its acceptance is automated (count invariant) + verifiable (URL diff command).
- **Type consistency:** function names used across tasks — `slug`, `validate`, `order`, `esc`, `render_entry`, `render_spine`, `render_views`, `assert_view_consistency`, `check_markers`, `check_blurbs`, `check_count_invariant`, `normalise`, `render_toc`, `fill`, `build`, `generate`, `main`, `self_check` — are defined once and reused consistently.
