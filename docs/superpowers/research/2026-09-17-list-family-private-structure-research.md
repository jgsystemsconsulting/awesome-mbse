# Research: list-family private structure

## Research brief

**Primary question:** What external conventions and existing awesome lists should guide a private-first MBSE hub+spokes family (list of lists + deep niche spokes)?

**Sub-questions:**
1. How do meta awesome lists / list-of-lists structure themselves?
2. What does sindresorhus/awesome expect for list quality and family pointers?
3. Which external awesome lists already cover SysML, MBSE, ArchiMate, Capella, requirements, digital engineering, STPA?
4. What are known pitfalls of multi-repo awesome families (empty repos, duplication, private hubs)?

**Success criteria:**
- Cite at least one primary pattern for list-of-lists or awesome hub structure
- Note awesome.re / sindresorhus submission bar at high level
- Inventory external niche competitors or confirm empty namespaces for planned spokes
- Capture failure modes that should become TODOs or gap callouts in the private structure

**Out of scope:** Full link audit of every MBSE resource; implementing public release.

**Budget:** light tier, 1 round preferred.

**Retrieved window:** 2026-09-17

## Findings

1. **Canonical meta pattern is sindresorhus/awesome** (ESTABLISHED). Category-grouped links to topic awesome lists; badge ecosystem via awesome.re. https://github.com/sindresorhus/awesome

2. **Submission bar (high level)** (ESTABLISHED / PROVISIONAL mix). At least 30 days age; pass awesome-lint; Awesome badge beside title; section named Contents; CC0; description starts uppercase ends with period; search for duplicates before creating. https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md , create-list.md, awesome-lint.

3. **External niche inventory (partial)**
   - SysML: `mycr0ft/awesome-sysml` exists (~5 stars, SysML v2 tools focus). PROVISIONAL star count.
   - ArchiMate: no `awesome-archimate` found (0 results). ESTABLISHED empty-ish namespace for that exact name.
   - MBSE: search surfaced interview Q&A list, not a general MBSE hub competitor. PROVISIONAL.
   - Capella, STPA, digital engineering namespace searches: **TODO recheck** (GitHub 429 this round).

4. **Failure modes to bake into private structure** (mostly from local policy + submission docs; external skeptic fetch failed)
   - Empty planned repos look worse than hub sections (FAMILY 40+ bar).
   - Duplicate lists rejected culture (search before create).
   - Private hub cannot earn sindresorhus listing or public stars until public.
   - Hub private + one spoke public already true (sysml-v2); family pointer on public spoke must not imply public hub if hub stays private (link to FAMILY only works for collaborators, or omit until hub public).
   - Rate limits blocked complete competitor scan: treat planned-spoke "namespace empty" as **stale until rechecked**.

## Synthesis

Private-first design should **look like** a sindresorhus-style meta hub (family registry + external lists + cross-cutting) while keeping deep content until spokes earn density. Do not create empty GitHub repos. Mark external competitor TODOs explicitly. When linking the live public spoke, note hub privacy so public readers are not sent to a 404 FAMILY path unless hub is public.

Decision inputs for spec/plan:
- Hub structure sections: List family | External awesome lists | Cross-cutting | Deep niches (with GAP/TODO badges)
- Spoke create checklist stays TODO until 40 candidates
- External list rows: mycr0ft/awesome-sysml at minimum
- Namespace recheck TODO for capella/stpa/digital-eng/RE

## Sources

| URL | Role |
|-----|------|
| https://github.com/sindresorhus/awesome | primary meta hub |
| https://awesome.re | badge / redirect |
| https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md | submission bar |
| https://github.com/sindresorhus/awesome/blob/main/create-list.md | create guidance |
| https://github.com/sindresorhus/awesome-lint | lint rules |
| https://github.com/mycr0ft/awesome-sysml | external SysML competitor |
| https://github.com/topics/awesome | awesome topic scale |
| https://github.com/search?q=awesome-archimate&type=repositories | empty archimate name |
