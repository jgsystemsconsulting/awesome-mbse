# Context: awesome-archimate release-standard close

## Context brief

**Primary question:** What must change in the live spoke `awesome-archimate` to clear Release Repo Standard Base (OSS, CC0, standalone), matching the Capella RR-B close pattern?

**Success criteria:**
- S1: Current audit FAIL list for awesome-archimate
- S2: Capella RR-B file inventory and decisions that already closed the same bar
- S3: Archimate-specific deltas (workflow names, entry count 17, SECURITY email, no scripts yet)
- S4: Hub stays out of scope

**Out of scope:** Changing README seed entries content/order; hub edits; MCP/skills profiles.

## Findings

1. Spoke is public at `jgsystemsconsulting/awesome-archimate` with family triad (`links.yml`, `lint.yml`, `stale.yml`), 17 entries, CC0 LICENSE, CONTRIBUTING, CoC, SECURITY (hub email style), CHANGELOG Unreleased-only.
2. Capella already has an executed RR-B pack pattern in hub specs/plans (`2026-09-17-repo-release-standard-capella.md`) with locked decisions D1-D11.
3. Sysml-v2 has partial surface (CITATION, Pages, SECURITY advisory) but still fails many Base rows; Capella is the better clone target for full close.
4. Archimate has no `scripts/`, no `docs/`, no issue forms, no PR template, no COPYRIGHT/NOTICE/RELEASE-INFO/CITATION/DISTRIBUTION.

## Synthesis

Clone Capella RR-B decisions with ArchiMate product strings, 17-entry facts, and family triad file names. Keep family CI untouched; add validate.yml + check_release.py. Ship Pages landing. Version 0.1.0.

## Evidence index

| loc | kind |
|-----|------|
| ../awesome-archimate/* | code |
| docs/superpowers/specs/2026-09-17-repo-release-standard-capella.md | doc |
| ../awesome-capella/* | code |
