# Spec: repo-release-standard (awesome-mbse list family)

Date: 2026-09-17
Mode: planning deliverable (docs and pointer edits only; no visibility flips in this run)

## Summary

The awesome-mbse list family has no durable, in-repo standard for taking family repos
from private to public. The rules that exist are scattered: a Private mode section in
FAMILY.md, per-spoke notes, and decisions that lived in chat. This spec defines one
runbook, `docs/runbooks/family-public-release.md`, plus a short FAMILY.md amendment, so
that any future release (one spoke, the hub, or the sindresorhus/awesome submission) is
a checklist execution instead of a re-derivation.

Two gates run through everything:

- **Spoke-public gate:** one family repo's own visibility flip, private to public.
- **Hub-public gate:** the hub's flip, which is also the unlock that lets public spokes
  hyperlink `FAMILY.md` instead of using a text-only family pointer.

## Scope

In scope: the runbook document, the FAMILY.md Private mode amendment, the family
pointer rules for spoke READMEs, the release checklists for spokes and hub, and the
sindresorhus/awesome step that comes after hub public.

Out of scope, explicitly:

- **Out of scope: RR-B.** The user-scope skill `release-repo-standard` (RR-B / RR-M /
  RR-S, `audit.py`, marketplace and landing-page requirements) is a product-repo
  standard. Pure awesome lists are CC0 link indexes; they do not take product packaging.
  This spec governs family visibility and pointer rules only and must not grow RR-B
  scaffolding.
- No automatic visibility flips. Every `gh repo edit --visibility` command is run by
  the maintainer, by hand, after a human decision.
- No sindresorhus/awesome work while the hub is private. It appears only as the
  post-hub-public checklist.
- No execution of the flips in this run. Default Superpowers mode: this spec and the
  later plan define the docs; execution happens on a full or implement-now dispatch.
- No new spokes, no magic-grid re-scope, no sweep work (tracked elsewhere in the
  backlog).

## Current state and drift

Live mix on 2026-09-17 (evidence in the research doc): hub private; awesome-sysml-v2,
awesome-capella, awesome-digital-engineering public; awesome-requirements-engineering
Live but private; archimate and stpa planned; magic-grid local only.

Family pointer audit across family spokes (2026-09-17 local checkouts):

- awesome-sysml-v2 (public): compliant, text-only ("hub repository currently private").
- awesome-capella (public): compliant, text-only with the Private mode citation.
- awesome-requirements-engineering (private Live): compliant, text-only.
- **awesome-digital-engineering (public): violates Private mode.** Its README line 8
  hyperlinks
  `https://github.com/jgsystemsconsulting/awesome-mbse/blob/main/FAMILY.md`, which 404s
  for anonymous readers while the hub is private. Parent-verified against the local
  checkout and anonymous fetch of the hub blob URL.

The drift has a generator: the README skeleton in FAMILY.md ships the hyperlink as the
default family pointer. Anyone creating a spoke from the skeleton while the hub is
private reproduces the violation. The amendment in this spec fixes the skeleton, and the
runbook's spoke checklist catches it at release time.

Related backlog rows this work addresses:

- `list-family-private-structure-4` (hub public when coherent; then allow FAMILY URL
  from public spokes): the runbook defines the coherence bar and the unlock sweep. The
  row itself closes only when the flip actually happens.
- `awesome-requirements-engineering-1` (public-release runbook for the RE spoke):
  closed by this work; the runbook is the RE public-release path.

## Design decisions

1. **One runbook, in `docs/runbooks/`.** Preferred path
   `docs/runbooks/family-public-release.md`. It is durable maintainer documentation, not
   a process artifact, so it stays out of the `docs/superpowers/` tree. (The
   `docs/superpowers/runbooks/` alternative was considered and declined for that reason.)
2. **Pointer grammar: two classes, one preferred string each.** Class is what greps
   enforce; the preferred string is what new writes use.
   - **Class hub-private (text-only):** no `FAMILY.md` URL and no
     `awesome-mbse/blob` hyperlink. Preferred line for new writes:
     `Part of the awesome-mbse list family (hub repository currently private).`
     Existing variants (Capella, RE) that are still text-only and name the hub without a
     URL remain **compliant** until the next spoke edit, then normalize to the preferred
     line. Hyperlinks to the private hub are **non-compliant**.
   - **Class hub-public (hyperlink):** preferred line
     `Part of the [awesome-mbse list family](https://github.com/jgsystemsconsulting/awesome-mbse/blob/main/FAMILY.md).`
   Mapping: while hub Visibility is `private`, every **public** spoke must be class
   hub-private. After hub public, every **public** spoke must be class hub-public.
   Private spokes may keep a text-only line until they themselves go public (Checklist A
   then picks class from current hub visibility).
3. **Coherence bar for hub public.** The hub may go public when every registry row with
   Status `Live` has Visibility `public`, or when a Live private row is listed under a
   registry footnote or the planned-spoke note block as
   `Exception: <repo> remains private — <reason> — <YYYY-MM-DD>` (Visibility cell stays
   `private`; do not invent a fifth Visibility token). A hub that 404s its own family
   table from an anonymous browser is not coherent. `In development` and `Planned` rows
   stay name-only and do not block.
4. **Visibility flips are human commands, recorded.** Before each `gh repo edit
   --visibility` command, open a GitHub issue in the repo being flipped titled
   `Public release decision <YYYY-MM-DD>` with: decision (public), decision date,
   decision maker (GitHub login), and one-line reason. Close the issue when the flip and
   hub registry/README edits land. The runbook prints the exact `gh` command; the flip is
   never automated, never part of CI, never batched silently. Each flip also gets a
   CHANGELOG note in the repo that flipped.
5. **The unlock is one sweep, not a dribble.** After the hub flip lands, all **public**
   spokes get their pointer upgraded to class hub-public in a single pass (same day, one
   commit each). Private Live spokes stay text-only until Checklist A runs for them.

## Deliverable 1: the runbook

File: `docs/runbooks/family-public-release.md` (hub repo).

Structure and content the runbook must carry:

### Header

What this runbook is for, the two-gate model, the pointer grammar, and the sentence
"every visibility flip in this runbook is a human decision executed by hand."

### Checklist A: spoke public release (example: awesome-requirements-engineering)

- [ ] CI green on default branch: link check, scheduled sweep, markdown lint, awesome-lint.
- [ ] Every entry link passes the public-availability bar; no private-only resources
      anywhere in the list (family standard; the jgs-magic-sysmlv2-mcp CHANGELOG removal
      is the precedent).
- [ ] README matches the family skeleton: Awesome badge, sweep badge, one-line scope,
      table of contents.
- [ ] Family pointer class matches **current hub visibility**: if hub is still
      private, class hub-private (preferred string or compliant text-only variant; no
      FAMILY.md URL). If hub is already public, class hub-public (preferred hyperlink).
      Fix any wrong-class pointer before the flip.
- [ ] No machine-local paths (`C:\Users\`, `/Users/<you>/`, OneDrive absolute paths),
      `TODO`/`WIP` draft notes meant for maintainers only, or untracked maintainer-only
      dumps committed under the repo root. Fail the check if any appear in tracked files.
- [ ] Human decision issue filed (title `Public release decision <YYYY-MM-DD>`, fields
      above), then: `gh repo edit jgsystemsconsulting/awesome-<niche> --visibility public --accept-visibility-change-consequences`
- [ ] Verify anonymous access: the repo URL and every README link resolve logged out.
- [ ] Hub edits: FAMILY.md registry Visibility private to public; hub README family
      table row gains the spoke URL (was name-only with a location note). Status stays `Live`.
- [ ] CHANGELOG note in the spoke recording the release date; close the decision issue.

### Checklist B: hub public release plus pointer unlock

Gate, then flip, then unlock:

- [ ] Coherence bar met: all `Live` spokes public, or exception-listed in the registry
      with reason and date.
- [ ] Hub README family table consistent: public spokes linked, private exceptions
      name-only, `In development` / `Planned` rows name-only.
- [ ] Hub CI green; sweep badge current; no private-only entries in hub list bodies.
- [ ] Human decision issue filed in the hub (same title/fields pattern as Checklist A),
      then: `gh repo edit jgsystemsconsulting/awesome-mbse --visibility public --accept-visibility-change-consequences`
- [ ] Verify `https://github.com/jgsystemsconsulting/awesome-mbse/blob/main/FAMILY.md`
      resolves logged out.
- [ ] Pointer unlock sweep: in every **public** spoke README, set class hub-public
      preferred hyperlink. One commit per spoke. Private spokes unchanged.
- [ ] Registry: hub row Visibility private to public. CHANGELOG note in the hub; close
      the decision issue.
- [ ] Close `list-family-private-structure-4`.

### Checklist C: sindresorhus/awesome submission (per list, after hub public)

- [ ] Prerequisites: hub public, public-spoke pointer unlock done, the list is stable:
      last full sweep badge current, CI green, and either at least 40 inclusion-bar
      entries (FAMILY Starting a new list bar) **or** the README carries the honest growth
      label line exactly:
      `> Initial seed; growth in progress. Entry count is under the family 40+ bar on purpose.`
      placed immediately under the family pointer (maintainer sets it; remove when count
      clears 40).
- [ ] Submit per the live PR template at
      https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md.
      The runbook links the template; it does not fork their guidelines into this repo.
- [ ] Target: https://github.com/sindresorhus/awesome
- [ ] Record the submission (date, PR link) in the spoke CHANGELOG.

### Standing fixes the runbook requires

- **DE drift fix (do with the runbook commit, before any flip):** replace the private-hub
  FAMILY.md hyperlink in `awesome-digital-engineering/README.md` (currently the family
  pointer line) with the preferred class hub-private text-only line. Removes a live 404
  for anonymous readers.
- **Recurring check:** from a workspace that has hub plus sibling spoke checkouts
  (`../awesome-*/`), run `grep -rn "FAMILY.md\|awesome-mbse/blob\|awesome-mbse list family" ../awesome-*/README.md`
  and confirm every public spoke is the correct class for current hub visibility (no
  private-hub URL while hub private; preferred hyperlink after hub public). If siblings
  are missing, clone each Live public spoke shallow once, then run the same grep. Run at
  each sweep.

## Deliverable 2: FAMILY.md Private mode amendment

Short edit to the Private mode section, three additions and one fix:

1. Link the runbook: "The release procedure lives in
   `docs/runbooks/family-public-release.md`." (One sentence, after the sindresorhus
   deferral bullet, which now points at that runbook instead of "a future public-release
   runbook".)
2. Status versus Visibility: Status is content maturity (`Live` / `In development` /
   `Planned`); Visibility is who can open the repo (`public` / `private` / `local only` /
   `none yet`). They flip independently; a spoke going public does not move the hub.
3. The two gates named: spoke-public (Checklist A) and hub-public (Checklist B, which
   also unlocks FAMILY.md hyperlinks in public spokes).
4. Skeleton fix: in the README skeleton, replace the hyperlinked family pointer line
   with the text-only default and a comment naming the post-unlock hyperlink. This stops
   the skeleton from generating the DE-style violation.

## Execute touch list (for the later plan)

| File | Change |
|------|--------|
| `docs/runbooks/family-public-release.md` | New. Content per Deliverable 1. |
| `FAMILY.md` | Private mode amendment per Deliverable 2. |
| `../awesome-digital-engineering/README.md` | Two pointer lines to text-only (standing fix). |
| `docs/superpowers/backlog.md` | Close `awesome-requirements-engineering-1`; annotate `list-family-private-structure-4` as runbook-ready, flip pending. |

No visibility changes, no spoke CI changes, no RR-B files.

## Verification

- The runbook exists at the named path and carries Checklists A, B, C plus the standing
  fixes, each item verifiable by command or by reading the named file.
- FAMILY.md Private mode section names the runbook, states the Status/Visibility split,
  and defines both gates; the skeleton ships the text-only pointer.
- `grep -rn "FAMILY.md" ../awesome-*/README.md` shows no public spoke hyperlinking
  FAMILY.md while the hub is private (DE fix verified by the same check).
- Registry and hub README family table agree with each other; actual GitHub visibility
  agrees with both (checked via `gh repo view --json visibility` at execution time).
- A reader who has never seen this spec can execute Checklist A on the RE spoke without
  asking a question.

## Open questions

None blocking. The runbook path (`docs/runbooks/`) and the coherence bar (all Live
spokes public, or written exceptions) are decided here; the maintainer can revisit the
bar when the hub flip is actually scheduled.

## Research

- Research doc: `docs/superpowers/research/2026-09-17-repo-release-standard-research.md`
- https://github.com/sindresorhus/awesome (list-of-lists submission target, post-hub-public only)
- https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md (live submission template; linked, never forked)
- Confirmed in research: public spokes resolve without auth; the FAMILY.md URL on the
  private hub 404s for anonymous readers, which is the basis for the text-only rule.

research: internal-primary + sindresorhus/awesome pointers (see research doc and URLs above).

## Codebase context

Context doc: `docs/superpowers/context/2026-09-17-repo-release-standard-context.md`.
It established: FAMILY.md already carries the Private mode rules this spec amends
(default private, text-only pointers while hub private, sindresorhus deferred, sweep
unchanged by privacy); the registry Visibility column is the source of truth for the
live mix; the hub README family table tracks the same mix for readers. The user-scope
`release-repo-standard` skill was read for contrast: RR-B covers legal, marketplace,
landing page, and audit tooling for product repos, none of which applies to CC0 link
lists. The spoke READMEs were checked directly for pointer style (three compliant, DE
violating). Backlog rows `list-family-private-structure-4` and
`awesome-requirements-engineering-1` are the open items this spec serves.
