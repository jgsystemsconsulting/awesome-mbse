# Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE.
# SPDX-License-Identifier: CC0-1.0
"""Release gate for Awesome MBSE (Base + list files + landing truth)."""
import pathlib
import re
import subprocess
import sys

fails: list[str] = []

REQUIRED = [
    "LICENSE", "NOTICE", "README.md", "CHANGELOG.md",
    "RELEASE-INFO.txt", "SECURITY.md", ".gitignore",
    "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "docs/DISTRIBUTION.md",
    "docs/index.html", "scripts/check_release.py",
    "DESIGN.md", "DESIGN_BRIEF.md",
    "COPYRIGHT", "CITATION.cff",
]
for f in REQUIRED:
    if not pathlib.Path(f).is_file():
        fails.append(f"required file missing: {f}")

CFF_FIELDS = ["cff-version", "message", "title", "authors", "license", "repository-code"]
_cff = pathlib.Path("CITATION.cff").read_text(encoding="utf-8")
missing = [f for f in CFF_FIELDS if f"{f}:" not in _cff]
assert not missing, f"CITATION.cff missing fields: {missing}"

tracked = subprocess.run(
    ["git", "ls-files"], capture_output=True, text=True, check=True
).stdout.splitlines()
FORBIDDEN_PATH_PARTS = [
    "__pycache__", ".venv", ".worktrees", ".pytest_cache", ".ruff_cache", ".bak",
]
for f in tracked:
    if any(part in f for part in FORBIDDEN_PATH_PARTS):
        fails.append(f"forbidden tracked path: {f}")

FORBIDDEN_CONTENT = [
    re.compile(r"BEGIN [A-Z ]*PRIVATE KEY"),
]
SCAN_GLOBS = ["scripts/*.py", "*.md", "*.txt", "*.cff", "docs/**/*.md", "docs/**/*.html"]
scanned = 0
for g in SCAN_GLOBS:
    for path in pathlib.Path(".").glob(g):
        if not path.is_file():
            continue
        scanned += 1
        text = path.read_text(encoding="utf-8", errors="ignore")
        for rx in FORBIDDEN_CONTENT:
            if rx.search(text):
                fails.append(f"forbidden content in {path}: {rx.pattern}")

HEADER_SENTINEL = "Copyright (c) 2026 JG Systems Consulting Ltd"
for path in pathlib.Path("scripts").glob("*.py"):
    head = path.read_text(encoding="utf-8", errors="ignore")[:400]
    if HEADER_SENTINEL not in head:
        fails.append(f"header missing: {path}")
    if "SPDX-License-Identifier: CC0-1.0" not in head:
        fails.append(f"SPDX missing: {path}")

# --- landing truth gate: landing chips and section index vs sources ---


def read_source(path):
    try:
        return pathlib.Path(path).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        fails.append(f"unreadable source file: {path}")
        return None


def landing_chip(html, name):
    hits = re.findall(rf"<dt>{re.escape(name)}</dt>\s*<dd>([^<]*)</dd>", html)
    if len(hits) != 1:
        fails.append(f"landing chip missing or ambiguous: {name}")
        return None
    return hits[0].strip()


release_info = read_source("RELEASE-INFO.txt")
readme = read_source("README.md")
html = read_source("docs/index.html")

if release_info is not None:
    # Allow variable spacing after the label (hub RELEASE-INFO uses padded columns).
    version_hits = re.findall(r"(?m)^Version:\s*(\S+)\s*$", release_info)
    if len(version_hits) != 1:
        fails.append(
            f"RELEASE-INFO Version field missing or ambiguous: {len(version_hits)} matches"
        )
    else:
        chip_version = landing_chip(html, "version") if html is not None else None
        if chip_version is not None and chip_version != version_hits[0]:
            fails.append(
                f"landing version chip {chip_version} != RELEASE-INFO Version {version_hits[0]}"
            )

if readme is not None:
    sweep_hits = re.findall(r"!\[Last full sweep: (\d{4}-\d{2})\]", readme)
    if len(sweep_hits) != 1:
        fails.append(f"README sweep badge missing or ambiguous: {len(sweep_hits)} matches")
    else:
        chip_sweep = landing_chip(html, "sweep") if html is not None else None
        if chip_sweep is not None and chip_sweep != sweep_hits[0]:
            fails.append(
                f"landing sweep chip {chip_sweep} != README sweep badge {sweep_hits[0]}"
            )

# Product sections whose grammar-valid bullets count toward the entries chip.
# Model Gallery is a pointer table, not entry bullets. Contents/meta sections excluded.
CURATED_SECTIONS = (
    "Magic Grid & Cameo / CATIA Magic",
    "Broader SysML / MBSE Context",
    "External awesome lists",
)

# Section-index order matches the README Contents product anchors (six links).
SECTION_INDEX = (
    "List family",
    "Magic Grid & Cameo / CATIA Magic",
    "Model Gallery",
    "Broader SysML / MBSE Context",
    "External awesome lists",
    "Support & security",
)

ENTRY_RX = re.compile(r"^- \[[^\]]+\]\(https?://[^)\s]+\)\s+-\s+.+\(\d{4}\)\.?$")


def curated_walk(readme_text):
    """Count grammar-valid bullets under curated headings and tally exact ## hits."""
    count = 0
    heading_hits = {title: 0 for title in CURATED_SECTIONS}
    current = None
    in_fence = False
    for raw in readme_text.splitlines():
        line = raw.strip()
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        stripped = line.strip()
        if stripped.startswith("## ") and not stripped.startswith("###"):
            current = stripped[3:].strip()
            if current in heading_hits:
                heading_hits[current] += 1
            continue
        if current in heading_hits and line and re.match(r"^[-*] \[", line):
            probe = "- " + line[2:] if line.startswith("* ") else line
            if ENTRY_RX.match(probe):
                count += 1
            else:
                fails.append(f"curated entry malformed in {current}: {line[:60]}")
    return count, heading_hits


curated_count = None
heading_hits = {}
if readme is not None:
    curated_count, heading_hits = curated_walk(readme)

chip_entries = landing_chip(html, "entries") if html is not None else None
if chip_entries is not None:
    if not re.fullmatch(r"[0-9]+", chip_entries):
        fails.append(f"landing entries chip not an integer: {chip_entries}")
    elif curated_count is not None and int(chip_entries) != curated_count:
        fails.append(f"landing entries chip {chip_entries} != curated count {curated_count}")


def github_slug(title):
    return re.sub(r"[^\w\s-]", "", title.lower()).strip().replace(" ", "-")


for title, hits in heading_hits.items():
    if hits == 0:
        fails.append(f"curated heading missing from README: {title}")
    elif hits > 1:
        fails.append(f"curated heading duplicated in README ({hits}x): {title}")

# Section-index headings must exist once each in README (index set, not only curated).
if readme is not None:
    index_hits = {title: 0 for title in SECTION_INDEX}
    in_fence = False
    for raw in readme.splitlines():
        line = raw.strip()
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.startswith("## ") and not line.startswith("###"):
            title = line[3:].strip()
            if title in index_hits:
                index_hits[title] += 1
    for title, hits in index_hits.items():
        if hits == 0:
            fails.append(f"section-index heading missing from README: {title}")
        elif hits > 1:
            fails.append(f"section-index heading duplicated in README ({hits}x): {title}")

if html is not None:
    blocks = re.findall(r'<ul class="section-index">(.*?)</ul>', html, re.DOTALL)
    if len(blocks) != 1:
        fails.append(f"landing section-index list missing or ambiguous: {len(blocks)} found")
    else:
        lis = re.findall(r"<li\b[^>]*>.*?</li>", blocks[0], re.DOTALL)
        expected_n = len(SECTION_INDEX)
        if len(lis) != expected_n:
            fails.append(f"section-index li count {len(lis)} != {expected_n}")
        else:
            fragments = []
            for li in lis:
                hrefs = re.findall(r'href="[^"#]*#([^"]+)"', li)
                if len(hrefs) != 1:
                    fails.append(f"section-index li href missing or ambiguous: {li[:60]}")
                    fragments = None
                    break
                fragments.append(hrefs[0])
            if fragments is not None:
                expected = [github_slug(t) for t in SECTION_INDEX]
                for got, want in zip(fragments, expected):
                    if got != want:
                        fails.append(f"section-index fragment mismatch: {got} != {want}")

if scanned < 1:
    fails.append("SCAN_GLOBS matched zero files")

if fails:
    print("RELEASE GATE FAILED:")
    for f in fails:
        print(f"  - {f}")
    sys.exit(1)
print(f"release gate: PASS (scanned {scanned} files)")
