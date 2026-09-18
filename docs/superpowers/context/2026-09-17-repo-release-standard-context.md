# Context: repo-release-standard (family public release)

## Context brief

**Primary question:** What does this workspace already define for taking
awesome-mbse family repos from private (or private-structure) to public, and
what durable standard/runbook should live in-repo?

**Success criteria:**

- SC1: FAMILY.md private-mode rules quoted (when hub private, public spokes
  text-only family pointer; sindresorhus deferred).
- SC2: Current registry Visibility mix (hub private, RE private, several public
  spokes) recorded with evidence.
- SC3: Difference from user-scope skill `release-repo-standard` (RR-B product
  standard) stated so this work does not conflate the two.
- SC4: Concrete file touch list for releasing one private spoke (e.g. RE) and
  for releasing the hub later.
- SC5: Existing backlog rows that this standard should close or partially close.

**Out of scope:** Actually flipping any repo public in this planning run
(default Superpowers mode stops after plan review unless full). RR-B audit of
product monorepos.

**Date:** 2026-09-17

## Findings

1. **FAMILY private mode** (`FAMILY.md`): default create is private until
   explicitly released. While hub is private, public spokes use text-only family
   pointer (no FAMILY.md URL). sindresorhus/awesome submission is deferred to a
   future public-release runbook. Sweep/CI unchanged by privacy.

2. **Registry (live):** hub `private`; awesome-sysml-v2, awesome-capella,
   awesome-digital-engineering `public`; awesome-requirements-engineering
   `Live|private`; archimate/stpa planned; magic-grid local only.

3. **Public spokes already live** with hub still private: they use text-only
   family lines (sysml: "hub repository currently private"). Hub README links
   public spokes with markdown URLs; private RE is name-only with location note.

4. **User-scope `release-repo-standard` skill** is RR-B/RR-M/RR-S product
   release-ready (LICENSE, marketplace, landing page, audit.py). It is **not**
   the awesome-list family private→public flip. This workspace standard should
   be a FAMILY runbook, optionally cross-linking RR-B only if a spoke ever
   needs product packaging (it should not for pure awesome lists).

5. **Backlog:** `list-family-private-structure-4` (hub public when coherent);
   `awesome-requirements-engineering-1` (public-release runbook for RE spoke).

6. **Deliverable shape (decision):** durable doc under hub
   `docs/runbooks/family-public-release.md` (or `docs/superpowers/runbooks/`)
   plus short pointer from FAMILY.md Private mode section to that runbook.
   Checklist steps for spoke-only release vs hub release vs full-family
   hyperlink unlock.

## Synthesis

Build an in-hub **family public-release standard/runbook**, not an RR-B clone.
Gates: CI green, 40+ bar or honest growth label, no private-only entry links,
Visibility column flip, hub table URL when public, family pointer upgrade only
when hub is public. Hub public is a separate higher bar (coherent family).
sindresorhus remains after hub public + list stable.

## Evidence index

| loc | kind |
|-----|------|
| FAMILY.md Private mode | doc |
| FAMILY.md registry Visibility column | doc |
| FAMILY.md RE/DE/Capella checklists | doc |
| README.md List family table | doc |
| ../awesome-sysml-v2/README.md family pointer | doc |
| docs/superpowers/backlog.md rows | doc |
| ~/.zcode/skills/release-repo-standard/SKILL.md | doc (out of band, contrast) |
