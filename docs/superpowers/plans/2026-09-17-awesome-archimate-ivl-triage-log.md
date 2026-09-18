# IVL triage log: 2026-09-17-awesome-archimate

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|

## Check commands

- Spoke entry-format python (http(s) entries, language tag, year-last)
- `npx awesome-lint@2.3.0 README.md` in spoke
- `npx markdownlint-cli2 "README.md" "CONTRIBUTING.md"` in spoke
- Spoke tree file set + workflows greps
- Hub FAMILY Live row + README spoke link
- `gh run list` / recent CI success on spoke (if available)

## Baseline

(pending)

## Baseline

- entry-format python: exit 0, 17 entries, no OMG, c226+c260 present
- awesome-lint@2.3.0: exit 0
- markdownlint-cli2: exit 0, 0 issues
- file set + workflows present; include-fragments=anchor-only; fail false; CONTRIBUTING glob; Inclusion bar in stale
- hub FAMILY Live public; README links spoke; CHANGELOG launch section
- CI: Links success 35236725659; Lint success 35236678930

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| (none from R1 wave) | R1 | R1 | — | behavior/regression/contract all NO_CRITICAL_OR_MAJOR |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| — | behavior, regression, contract | — | — | No findings (Round 1) |

Fixes applied: 0
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: PASS
Commands: entry-format -> 0; awesome-lint -> 0; markdownlint -> 0; gh CI Links/Lint success; hub FAMILY/README greps -> 0
Note: regression used GP fallback (ivl-regression pin failed).

## Converged: Round 1

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 1  |  Total fixes: 0
Implementation verification ready.
