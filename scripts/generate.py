#!/usr/bin/env python3
"""Generate README.md for awesome-mbse from data/*.yaml + README.template.md.

Usage:
  python scripts/generate.py              # write README.md
  python scripts/generate.py --check      # verify README.md matches data (CI; exit!=0 on drift)
  python scripts/generate.py --self-check # run built-in assertions (no test framework)

The committed README.md is a build artifact. Edit data/entries.yaml + data/tags.yaml,
then regenerate. See docs/superpowers/specs/2026-06-24-generator-driven-language-restructure-design.md
"""
from __future__ import annotations

import datetime
import difflib
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
ENTRIES_FILE = ROOT / "data" / "entries.yaml"
TAGS_FILE = ROOT / "data" / "tags.yaml"
TEMPLATE_FILE = ROOT / "README.template.md"
OUTPUT_FILE = ROOT / "README.md"
CURRENT_YEAR = datetime.date.today().year  # only bounds date validation; never rendered

LANGS = ["sysml-v1", "sysml-v2", "uaf", "arcadia", "opm", "oml", "cross-cutting"]
TYPES = ["methodology", "tutorial", "course", "book-paper", "model",
         "tool", "community", "spec", "api"]
REQUIRED = ("title", "url", "desc", "date", "lang", "type")
ADJACENT = {"arcadia", "opm", "oml"}          # H3 blocks under a prose H2
VIEW_IDS = ["view-openable-models", "view-by-tool", "view-by-type", "view-tag-legend"]
MARQUEE_TITLE = "Magic Grid & Cameo / CATIA Magic"

LANG_TITLES = {
    "sysml-v1": "SysML v1",
    "sysml-v2": "SysML v2",
    "uaf": "UAF & architecture frameworks",
    "arcadia": "Arcadia / Capella",
    "opm": "OPM",
    "oml": "OML",
    "cross-cutting": "Cross-cutting (language-general)",
}
TYPE_TITLES = {
    "methodology": "Methodology & guides",
    "tutorial": "Tutorials",
    "course": "Courses & learning paths",
    "book-paper": "Books & papers",
    "model": "Example models",
    "tool": "Tools, plugins & automation",
    "community": "Communities & blogs",
    "spec": "Specifications & standards",
    "api": "APIs & automation",
}

MARKER_RE = re.compile(r"<!-- AUTOGEN:(START|END) section=([a-z0-9-]+) -->")


# --------------------------------------------------------------------------- #
# Core helpers
# --------------------------------------------------------------------------- #
def slug(title: str) -> str:
    """GitHub heading-anchor algorithm. Do NOT 'tidy' it - must match GitHub byte-for-byte.

    lowercase; keep [a-z0-9_- ] (strip other punctuation with NO replacement);
    space -> hyphen; do not collapse or strip hyphens.
    'Magic Grid & Cameo' -> 'magic-grid--cameo'.
    """
    s = title.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s, flags=re.UNICODE)  # \w keeps underscore, like GitHub
    return s.replace(" ", "-")


def esc(text: object) -> str:
    """Escape markdown/HTML breakout chars in untrusted title/desc (spec: Security)."""
    out = str(text)
    for ch in "\\[]()!|<>`":  # backslash first
        out = out.replace(ch, "\\" + ch)
    return out


def url_ok(url: object) -> bool:
    """Allow only http(s), checked on the whitespace/control-stripped, lowercased form."""
    u = "".join(c for c in str(url).strip() if ord(c) >= 0x20)
    return u.lower().startswith(("https://", "http://"))


def normalise(text: str) -> str:
    """LF, no BOM - so --check never false-diffs on a CRLF/BOM checkout."""
    return text.replace("﻿", "").replace("\r\n", "\n").replace("\r", "\n")


def order(entries: list[dict]) -> list[dict]:
    """Deterministic: date descending, then title ascending (case-insensitive)."""
    return sorted(entries, key=lambda e: (-int(e["date"]), e["title"].lower()))


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)  # safe_load only - never yaml.load (spec: Security)


# --------------------------------------------------------------------------- #
# Validation (fail closed)
# --------------------------------------------------------------------------- #
def tool_tokens(legend: dict) -> list[str]:
    return [t for t in legend if (legend[t] or {}).get("tool")]


def validate(entries: list[dict], legend: dict) -> None:
    missing_tools = set(tool_tokens(legend)) - set(legend)
    if missing_tools:
        raise ValueError(f"tool tokens not in tag legend: {sorted(missing_tools)}")
    seen_slugs: dict[str, str] = {}
    for e in entries:
        who = e.get("title", "<no title>")
        for f in REQUIRED:
            if e.get(f) in (None, "") and e.get(f) != 0:
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


# --------------------------------------------------------------------------- #
# Rendering - spine
# --------------------------------------------------------------------------- #
def render_entry(e: dict) -> str:
    title = esc(e["title"])
    desc = esc(str(e["desc"]).rstrip(" ."))
    tags = " ".join(f"`{t}`" for t in e.get("tags", []))
    tail = f" {tags}" if tags else ""
    return f"- [{title}]({e['url']}) - {desc}{tail} ({e['date']})."


def _type_subsections(entries: list[dict], heading: str) -> list[str]:
    out: list[str] = []
    for t in TYPES:
        group = order([e for e in entries if e["type"] == t])
        if not group:
            continue  # empty subsection -> no heading
        out.append(f"{heading} {TYPE_TITLES[t]}\n")
        out.extend(render_entry(e) for e in group)
        out.append("")
    return out


def render_spine(entries: list[dict], legend: dict) -> dict[str, str]:
    """{lang_id: markdown}. Every record lands in exactly one lang block."""
    blocks: dict[str, str] = {}
    for lang in LANGS:
        here = [e for e in entries if e["lang"] == lang]
        lines: list[str] = []
        sub_heading = "####" if lang in ADJACENT else "###"
        if lang in ADJACENT:
            lines.append(f"### {LANG_TITLES[lang]}\n")
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
        blocks[lang] = ("\n".join(lines).rstrip() + "\n") if lines else "\n"
    return blocks


# --------------------------------------------------------------------------- #
# Rendering - views
# --------------------------------------------------------------------------- #
def render_views(entries: list[dict], legend: dict) -> dict[str, str]:
    v: dict[str, str] = {}

    models = order([e for e in entries if e["type"] == "model"])
    rows = ["| Model | Home | Tags |", "| --- | --- | --- |"]
    for e in models:
        home_title = LANG_TITLES[e["lang"]]
        home = f"[{home_title}](#{slug(home_title)})"
        tags = " ".join(f"`{t}`" for t in e.get("tags", []))
        rows.append(f"| [{esc(e['title'])}](#{slug(e['title'])}) | {home} | {tags} |")
    v["view-openable-models"] = "\n".join(rows) + "\n"

    parts: list[str] = []
    for tok in tool_tokens(legend):
        group = order([e for e in entries if tok in e.get("tags", [])])
        if not group:
            continue
        parts.append(f"### {tok}\n")
        parts.extend(f"- [{esc(e['title'])}](#{slug(e['title'])})" for e in group)
        parts.append("")
    v["view-by-tool"] = ("\n".join(parts).rstrip() + "\n") if parts else "\n"

    parts = []
    for t in TYPES:
        group = order([e for e in entries if e["type"] == t])
        if not group:
            continue
        parts.append(f"### {TYPE_TITLES[t]}\n")
        parts.extend(f"- [{esc(e['title'])}](#{slug(e['title'])})" for e in group)
        parts.append("")
    v["view-by-type"] = ("\n".join(parts).rstrip() + "\n") if parts else "\n"

    rows = ["| Tag | Meaning |", "| --- | --- |"]
    for tag in sorted(legend):
        rows.append(f"| `{tag}` | {esc(legend[tag]['desc'])} |")
    v["view-tag-legend"] = "\n".join(rows) + "\n"
    return v


def assert_view_consistency(entries: list[dict], views: dict[str, str]) -> None:
    model_rows = sum(1 for ln in views["view-openable-models"].splitlines()
                     if ln.startswith("| ["))
    n_models = sum(1 for e in entries if e["type"] == "model")
    if model_rows != n_models:
        raise ValueError(f"openable-models rows {model_rows} != count(model) {n_models}")


# --------------------------------------------------------------------------- #
# Template assembly
# --------------------------------------------------------------------------- #
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


def check_blurbs(template: str, sections: list[tuple[str, str]]) -> None:
    """Each (heading, marker_id) must have non-empty prose between heading and START."""
    for heading, marker in sections:
        m = re.search(
            rf"^## {re.escape(heading)}\s*\n(.*?)<!-- AUTOGEN:START section={marker} -->",
            template, re.S | re.M)
        if not m or not m.group(1).strip():
            raise ValueError(f"missing 'Use this when' blurb for section {marker!r}")


def check_count_invariant(entries: list[dict], spine: dict[str, str]) -> None:
    placed = sum(1 for e in entries if f"]({e['url']})" in spine.get(e["lang"], ""))
    if placed != len(entries):
        raise ValueError(f"count invariant: placed {placed} != records {len(entries)}")
    marquee = spine.get("sysml-v1", "")
    flag_rendered = sum(1 for e in entries
                        if e.get("flagship") and f"]({e['url']})" in marquee)
    n_flag = sum(1 for e in entries if e.get("flagship"))
    if flag_rendered != n_flag:
        raise ValueError(f"marquee count {flag_rendered} != flagship {n_flag}")


def render_toc(template: str) -> str:
    out: list[str] = []
    for line in template.splitlines():
        m = re.match(r"^## (.+)$", line)
        if m and "Contents" not in m.group(1):
            out.append(f"- [{m.group(1)}](#{slug(m.group(1))})")
    return "\n".join(out) + "\n"


def fill(template: str, blocks: dict[str, str]) -> str:
    for section, body in blocks.items():
        pat = re.compile(
            rf"(<!-- AUTOGEN:START section={re.escape(section)} -->\n).*?"
            rf"(\n<!-- AUTOGEN:END section={re.escape(section)} -->)", re.S)
        template = pat.sub(lambda m, b=body: m.group(1) + b.rstrip("\n") + m.group(2),
                           template)
    return template


def _blurb_sections() -> list[tuple[str, str]]:
    out = [(LANG_TITLES[l], l) for l in LANGS if l not in ADJACENT]
    out.append(("Adjacent & non-SysML notations", "arcadia"))
    return out


def build(entries: list[dict], legend: dict, template: str) -> str:
    validate(entries, legend)
    check_markers(template, expected_marker_set())
    check_blurbs(template, _blurb_sections())
    spine = render_spine(entries, legend)
    check_count_invariant(entries, spine)
    views = render_views(entries, legend)
    assert_view_consistency(entries, views)
    blocks = {"contents": render_toc(template), **spine, **views}
    return normalise(fill(template, blocks)).rstrip("\n") + "\n"


def generate() -> str:
    return build(load_yaml(ENTRIES_FILE), load_yaml(TAGS_FILE),
                 TEMPLATE_FILE.read_text(encoding="utf-8"))


# --------------------------------------------------------------------------- #
# Self-check (no test framework)
# --------------------------------------------------------------------------- #
def _fixture_tags() -> dict:
    return {
        "MagicGrid": {"desc": "x"}, "Cameo": {"desc": "x", "tool": True},
        "Papyrus": {"desc": "x", "tool": True}, "SysMLv1": {"desc": "x"},
        "SysMLv2": {"desc": "x"}, "SysML-general": {"desc": "x"},
        "book": {"desc": "x"}, "tool": {"desc": "x"}, "paper": {"desc": "x"},
        "has-model": {"desc": "x"},
    }


def _fixture_entries() -> list[dict]:
    return [
        {"title": "Alpha Guide", "url": "https://a.example", "desc": "d", "date": 2021,
         "lang": "sysml-v1", "type": "methodology", "flagship": True, "tags": ["MagicGrid"]},
        {"title": "Beta Models", "url": "https://b.example", "desc": "d", "date": 2025,
         "lang": "sysml-v2", "type": "model", "tags": ["SysMLv2", "has-model"]},
        {"title": "Gamma Survey", "url": "https://g.example", "desc": "d", "date": 2008,
         "lang": "cross-cutting", "type": "methodology", "tags": ["SysML-general", "paper"]},
    ]


def self_check() -> None:
    # --- slug: must match GitHub, incl. double-hyphen where punctuation sat between spaces
    assert slug("SysML v2") == "sysml-v2", slug("SysML v2")
    assert slug("Magic Grid & Cameo / CATIA Magic") == "magic-grid--cameo--catia-magic"
    assert slug("UAF & architecture frameworks") == "uaf--architecture-frameworks"

    good, legend = _fixture_entries(), _fixture_tags()
    validate(good, legend)  # must not raise

    def must_raise(mutate, needle):
        bad = [dict(e) for e in good]
        mutate(bad)
        try:
            validate(bad, legend)
        except ValueError as ex:
            assert needle in str(ex), f"wrong error for {needle!r}: {ex}"
        else:
            raise AssertionError(f"expected ValueError containing {needle!r}")

    must_raise(lambda b: b[0].update(url=" JAVASCRIPT:alert(1)"), "url")
    must_raise(lambda b: b[1].update(flagship=True), "flagship")   # b[1] is sysml-v2
    must_raise(lambda b: b[0].update(lang="sysmlv2"), "lang")
    must_raise(lambda b: b[0].update(tags=["NotInLegend"]), "tag")
    must_raise(lambda b: b[0].update(title=b[1]["title"]), "slug")
    must_raise(lambda b: b[0].update(date=3000), "date")

    # --- ordering
    ordered = order(good + [
        {"title": "Aardvark", "url": "https://z.example", "desc": "d", "date": 2025,
         "lang": "sysml-v2", "type": "tool", "tags": ["tool"]}])
    assert [e["title"] for e in ordered][:2] == ["Aardvark", "Beta Models"], \
        [e["title"] for e in ordered]

    # --- escaping
    line = render_entry({"title": "A|B [x]", "url": "https://h.example", "desc": "d (note)",
                         "date": 2020, "lang": "sysml-v1", "type": "tool", "tags": ["tool"]})
    assert "A\\|B \\[x\\]" in line and "https://h.example" in line and "(2020)." in line, line

    # --- spine
    blocks = render_spine(good, legend)
    v1 = blocks["sysml-v1"]
    assert f"### {MARQUEE_TITLE}" in v1 and "Alpha Guide" in v1, v1
    assert "### Tutorials" not in v1
    assert "### Example models" in blocks["sysml-v2"] and "Beta Models" in blocks["sysml-v2"]
    assert set(blocks) == set(LANGS)

    # --- views
    two_tool = {"title": "Dual Tool", "url": "https://d.example", "desc": "d", "date": 2024,
                "lang": "sysml-v1", "type": "tool", "tags": ["Cameo", "Papyrus"]}
    es = good + [two_tool]
    views = render_views(es, legend)
    assert "Beta Models" in views["view-openable-models"]
    assert "Alpha Guide" not in views["view-openable-models"]
    assert views["view-by-tool"].count("Dual Tool") == 2, views["view-by-tool"]
    assert "### Cameo" in views["view-by-tool"] and "### Papyrus" in views["view-by-tool"]
    assert "Cameo" in views["view-tag-legend"]
    assert_view_consistency(es, views)

    # --- template assembly
    tmpl = (
        "# Awesome MBSE\n\n## Contents\n"
        "<!-- AUTOGEN:START section=contents -->\n<!-- AUTOGEN:END section=contents -->\n\n"
        "## SysML v1\nUse this when you run Cameo today.\n"
        "<!-- AUTOGEN:START section=sysml-v1 -->\n<!-- AUTOGEN:END section=sysml-v1 -->\n\n"
        "## SysML v2\nUse this when greenfield.\n"
        "<!-- AUTOGEN:START section=sysml-v2 -->\n<!-- AUTOGEN:END section=sysml-v2 -->\n"
    )
    check_markers(tmpl, {"contents", "sysml-v1", "sysml-v2"})  # must not raise
    check_blurbs(tmpl, [("SysML v1", "sysml-v1"), ("SysML v2", "sysml-v2")])
    nob = tmpl.replace("Use this when greenfield.\n", "")
    try:
        check_blurbs(nob, [("SysML v2", "sysml-v2")])
    except ValueError as ex:
        assert "blurb" in str(ex), ex
    else:
        raise AssertionError("blurb check missed empty blurb")

    check_count_invariant(good, render_spine(good, legend))  # must not raise
    assert normalise("﻿a\r\nb\r\n") == "a\nb\n", repr(normalise("﻿a\r\nb\r\n"))

    print("self-check OK")


def main(argv: list[str]) -> int:
    if "--self-check" in argv:
        self_check()
        return 0
    rendered = generate()
    if "--check" in argv:
        current = normalise(OUTPUT_FILE.read_text(encoding="utf-8")) if OUTPUT_FILE.exists() else ""
        if current != rendered:
            sys.stdout.writelines(difflib.unified_diff(
                current.splitlines(True), rendered.splitlines(True),
                "README.md (committed)", "README.md (regenerated)"))
            return 1
        print("README.md up to date")
        return 0
    OUTPUT_FILE.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_FILE}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
