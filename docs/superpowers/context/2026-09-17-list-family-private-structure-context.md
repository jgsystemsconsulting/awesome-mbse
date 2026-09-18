# Context: list-family private structure

## Context brief

**Primary question:** What already exists in the awesome-mbse hub and sibling awesome repos so we can structure a private hub+spokes family without going public?

**Sub-questions:**
1. What does FAMILY.md already lock (registry, standards, split rules)?
2. What is the hub README shape vs awesome-magic-grid and awesome-sysml-v2?
3. What CI, CONTRIBUTING, and entry-format patterns can spokes reuse?
4. Where are gaps (planned spokes, missing registry links, thin sections)?
5. What must stay TODO (create/find remote repos) vs what can be structured in-tree now?

**Success criteria:**
- Map hub files that define family contract and list content
- Map sibling local/remote awesome repos and their maturity
- Identify reusable patterns (entry format, CI, CONTRIBUTING rules)
- Name constraints that block public publish vs private structure work
- List concrete in-tree surfaces that can hold private structure (FAMILY, hub README sections, gap TODOs)

**Out of scope:** Making any repo public; full entry curation for every niche; sindresorhus submission.

**Budget:** light tier, 1 round preferred.

**Workspace baseline:**
- HEAD: `4f7c0a63eb84e8ca29db1e565918a021e818cff3`
- porcelain fingerprint: `0933b130d260f82993853e7b62552af5ff0dccda8cd3a8192496cf60092999d2`

## Findings

1. **FAMILY.md is the family contract** (CORROBORATED, doc×2). Hub+spokes model, registry, scope boundaries, shared standard, new-list steps, README skeleton. `FAMILY.md:1-129`.

2. **Hub README is still a deep content list** (SINGLE-SOURCE). Points to FAMILY.md but keeps Magic Grid as flagship and Model Gallery; does not list spoke URLs near the top despite FAMILY saying it should. `README.md:20-31`.

3. **Reusable patterns exist in hub** (CORROBORATED, doc+config). Entry format with tags/year; lychee PR+schedule with `--include-fragments=anchor-only`; awesome-lint; CONTRIBUTING year/dedupe/neutrality. `FAMILY.md:68-92`, `.github/workflows/link-check-pr.yml`.

4. **Sibling maturity is uneven** (CORROBORATED). `awesome-sysml-v2` Live public but omits family pointer, sweep badge, tags/year. Local `awesome-magic-grid` is still titled Awesome MBSE and generator-driven from `data/entries.yaml`, not a Magic Grid niche spoke. Planned spokes (archimate, capella, RE, digital-eng, stpa) are registry rows only; no local repos. `FAMILY.md:33-46`.

5. **Public vs private constraints** (CORROBORATED). Hub is private on GitHub. Inclusion bar rejects private resources (CHANGELOG removed private JGS MCP link). FAMILY still points at public sindresorhus submission as end state. Private structure work must keep visibility TODO and not invent public URLs for missing repos.

6. **Contract drift is the main risk** (SINGLE-SOURCE cluster, skeptic). One-canonical-home unenforced (hub still holds deep SysML v2 gallery). Markdownlint listed in FAMILY but not in hub CI. Generator spoke vs hand-maintained skeleton conflict.

## Synthesis

Enough workspace fact to design private structure now:

| Surface | Use now (private) | Leave TODO |
|---------|-------------------|------------|
| FAMILY.md | Expand registry statuses, gap/TODO section, external lists section, private-mode notes | Create remote repos |
| Hub README | List family section with live/in-dev/planned; external awesome lists; gap callouts; keep deep content until spokes real | Hollow Magic Grid before spoke is real niche |
| awesome-sysml-v2 | Family pointer + sweep badge + standard alignment (when touching that tree) | Force public process changes |
| awesome-magic-grid | Re-scope to Magic Grid niche or mark as hub fork needing rename | Public GitHub create |
| Planned spokes | In-hub stub sections + TODO create-repo checklist | Empty GitHub repos |
| CI/CONTRIBUTING | Keep hub pattern as clone template documented in FAMILY | markdownlint job optional later |

Do not create empty public repos. Do not make hub public. Structure the *look* of the family inside the private hub and local siblings.

## Evidence index

| loc | kind |
|-----|------|
| FAMILY.md:1-129 | doc |
| FAMILY.md:16 | doc |
| FAMILY.md:33-46 | doc |
| FAMILY.md:53-60 | doc |
| FAMILY.md:68-92 | doc |
| FAMILY.md:103 | doc |
| README.md:3 | doc |
| README.md:20-31 | doc |
| CHANGELOG.md:14-17 | doc |
| .github/workflows/link-check-pr.yml | config |
| ../awesome-magic-grid/README.md:1-20 | doc |
| ../awesome-sysml-v2/README.md:1 | doc |
| ../awesome-sysml-v2/contributing.md:18 | doc |
