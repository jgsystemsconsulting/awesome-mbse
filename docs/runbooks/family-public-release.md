# Family public release runbook

This runbook takes awesome-mbse family repos from private to public: one spoke at a
time, the hub itself, and the sindresorhus/awesome submission that follows a hub
release. It exists so a release is a checklist execution instead of a re-derivation of
rules that used to live in chat.

Two gates run through everything:

- **Spoke-public gate (Checklist A):** one family repo's own visibility flip, private
  to public.
- **Hub-public gate (Checklist B):** the hub's flip, which is also the unlock that
  lets public spokes hyperlink `FAMILY.md` instead of using a text-only family
  pointer.

Every visibility flip in this runbook is a human decision executed by hand. No command
below is automated, batched, or wired into CI.

## Pointer class grammar

A spoke's family pointer line is one of two classes. The class is what greps enforce;
the preferred string is what new writes use.

**Class hub-private (text-only):** no `FAMILY.md` URL and no `awesome-mbse/blob`
hyperlink. Preferred line:

```
Part of the awesome-mbse list family (hub repository currently private).
```

Existing text-only variants that name the hub without a URL (awesome-sysml-v2,
awesome-capella, awesome-archimate, awesome-requirements-engineering) stay compliant
until the next edit to that spoke, then normalize to the preferred line. Hyperlinks to
the private hub are non-compliant.

**Class hub-public (hyperlink):** preferred line:

```
Part of the [awesome-mbse list family](https://github.com/jgsystemsconsulting/awesome-mbse/blob/main/FAMILY.md).
```

Mapping: while hub Visibility is `private`, every **public** spoke must be class
hub-private. After the hub goes public, every **public** spoke must be class
hub-public. Private spokes may keep a text-only line until they themselves go public
(Checklist A then picks the class from current hub visibility).

## Decision issue template

Before any `gh repo edit --visibility` command, open a GitHub issue in the repo being
flipped. Title: `Public release decision <YYYY-MM-DD>`. Body:

```markdown
- Decision: public
- Decision date: YYYY-MM-DD
- Decision maker: <github-login>
- Reason: <one line>
```

Command, with the date and repo filled in:

```bash
gh issue create -R jgsystemsconsulting/<repo> \
  -t "Public release decision <YYYY-MM-DD>" \
  -b "- Decision: public
- Decision date: <YYYY-MM-DD>
- Decision maker: <github-login>
- Reason: <one line>"
```

Keep the issue open until the flip and the hub registry/README edits land, then close
it. Each flip also gets a CHANGELOG note in the repo that flipped. If gh rejects the
`--accept-visibility-change-consequences` flag below, check `gh repo edit --help` for
the current flag name before running anything.

## Checklist A: spoke public release

Example in flight: awesome-requirements-engineering (Live, private, 40 entries as of
2026-09-17). Run top to bottom; do not flip until every box above the flip is ticked.

- [ ] CI green on default branch: link check, scheduled sweep, markdown lint,
      awesome-lint (`gh run list --limit 5` in the spoke checkout).
- [ ] Every entry link passes the public-availability bar; no private-only resources
      anywhere in the list (the jgs-magic-sysmlv2-mcp CHANGELOG removal is the
      precedent).
- [ ] README matches the family skeleton: Awesome badge, sweep badge, one-line scope,
      table of contents.
- [ ] Family pointer class matches current hub visibility. Hub still private: class
      hub-private (preferred string or a compliant text-only variant; no FAMILY.md
      URL). Hub already public: class hub-public (preferred hyperlink). Fix any
      wrong-class pointer before the flip.
- [ ] No machine-local paths, maintainer-only draft notes, or untracked dumps in
      tracked files:

  ```bash
  git grep -nIE "C:\\\\Users|/Users/|OneDrive" -- .
  git grep -nwIE "TODO|WIP" -- .
  git status --porcelain
  ```

  Fail the check if any appear in tracked files. Expected: no output from either
  grep and no unexpected untracked files.
- [ ] Decision issue filed (template above), then, by hand:

  ```bash
  gh repo edit jgsystemsconsulting/awesome-<niche> --visibility public --accept-visibility-change-consequences
  ```
- [ ] Anonymous access verified: the repo URL and every README link resolve logged
      out.

  ```bash
  curl -s -o /dev/null -w "%{http_code}\n" https://github.com/jgsystemsconsulting/awesome-<niche>
  ```

  Expect 200. A 404 means the flip did not take; README links are covered by the CI
  lychee job on the default branch.
- [ ] Hub edits: FAMILY.md registry Visibility cell private to public; hub README
      family table row gains the spoke URL (was name-only with a location note).
      Status stays `Live`.
- [ ] CHANGELOG note in the spoke recording the release date; close the decision
      issue (`gh issue close <number> -R jgsystemsconsulting/awesome-<niche> -c "Released <YYYY-MM-DD>."`).

## Checklist B: hub public release plus pointer unlock

Gate, then flip, then unlock.

- [ ] Coherence bar met: every registry row with Status `Live` has Visibility
      `public`, or a Live private row is listed under a registry footnote or the
      planned-spoke note block as `Exception: <repo> remains private — <reason> — <YYYY-MM-DD>`
      (Visibility cell stays `private`; never invent a fifth Visibility token). A hub
      that 404s its own family table from an anonymous browser is not coherent.
      `In development` and `Planned` rows stay name-only and do not block.
- [ ] Hub README family table consistent: public spokes linked, private exceptions
      name-only, `In development` / `Planned` rows name-only.
- [ ] Hub CI green; sweep badge current; no private-only entries in hub list bodies.
- [ ] Decision issue filed in the hub (template above), then, by hand:

  ```bash
  gh repo edit jgsystemsconsulting/awesome-mbse --visibility public --accept-visibility-change-consequences
  ```
- [ ] FAMILY.md resolves logged out:

  ```bash
  curl -s -o /dev/null -w "%{http_code}\n" https://github.com/jgsystemsconsulting/awesome-mbse/blob/main/FAMILY.md
  ```

  Expect 200.
- [ ] Pointer unlock sweep: in every **public** spoke README, set the class
      hub-public preferred hyperlink. One commit per spoke, same day. Private spokes
      unchanged.
- [ ] Registry: hub row Visibility private to public. CHANGELOG note in the hub;
      close the decision issue.
- [ ] Close backlog row `list-family-private-structure-4` in
      `docs/superpowers/backlog.md` (status to `done`).

## Checklist C: sindresorhus/awesome submission (per list, after hub public)

- [ ] Prerequisites: hub public, public-spoke pointer unlock done, the list stable:
      last full sweep badge current, CI green, and either at least 40 inclusion-bar
      entries (the family Starting-a-new-list bar) or the README carries the honest
      growth label line exactly:

  ```
  > Initial seed; growth in progress. Entry count is under the family 40+ bar on purpose.
  ```

  placed immediately under the family pointer. The maintainer sets it; remove it when
  the count clears 40.
- [ ] Submit per the live PR template:
      https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md
      (link the template; never fork their guidelines into this repo).
- [ ] Target: https://github.com/sindresorhus/awesome
- [ ] Record the submission (date, PR link) in the spoke CHANGELOG.

## Standing fixes

- **DE drift fix (applied 2026-09-17, before any flip):**
  `awesome-digital-engineering/README.md` hyperlinked the private hub's FAMILY.md,
  which 404s for anonymous readers. Replaced with the preferred class hub-private
  text-only line.
- **Recurring check (run at each sweep):** from a workspace that has the hub plus
  sibling spoke checkouts (`../awesome-*/`):

  ```bash
  grep -rn "FAMILY.md\|awesome-mbse/blob\|awesome-mbse list family" ../awesome-*/README.md
  ```

  Confirm every public spoke is the correct class for current hub visibility: no
  private-hub URL while the hub is private; the preferred hyperlink after the hub is
  public. If sibling checkouts are missing, clone each Live public spoke shallow once
  (`git clone --depth 1 https://github.com/jgsystemsconsulting/<repo>`), then run the
  same grep.
