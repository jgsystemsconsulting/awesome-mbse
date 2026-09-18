# FCL triage log: 2026-09-17-awesome-archimate (plan)

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| M1 Mastering ArchiMate sold-until ship inference | R1 | R1 | Genuine | Research marks Wierda provisional; plan invented sold-until→ship date. Fixed: keep (2022) only if page states year, else drop entry. |
| M2 undated pages (2026) via "addendum" vs hub §5 | R1 | R1 | Genuine | CONTRIBUTING already carries undated-page verification-year sentence; table now cites that rule, not a phantom addendum. |
| A1 GitHub tag dates only in plan | R1 | R1 | Advisory-skipped | Task 4 Step 1 already re-verifies via gh api. |
| A2 C226/C260 day precision | R1 | R1 | Advisory-skipped | Research ESTABLISHED; source lens clean. |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Wierda year inference | skeptic | MAJ | Genuine | Fixed (Round 1) |
| undated page year provenance | skeptic | MAJ | Genuine | Fixed (Round 1) |
| GitHub dates | skeptic | ADV | Advisory-skipped | Skipped (Round 1) |
| C226/C260 dates | skeptic | ADV | Advisory-skipped | Skipped (Round 1) |

Fixes applied: 2
Inflation rate: 0% (0/2 CRITICAL+MAJOR triaged FP/Design/Recurring)
Validation: SKIP

## Round 2 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| L463 undated year | skeptic, correspondent | CONF | resolved by this change | Confirmed (Round 2) |
| L469 Wierda year | skeptic, correspondent | CONF | resolved by this change | Confirmed (Round 2) |
| L259 hub §5 verbatim vs undated sentence | source | MAJ | Genuine | Fixed as amendment (spoke addendum split) |

Fixes applied: 1 (amendment after confirm wave)
Inflation rate: n/a for pure confirm; 1 new MAJOR from source on residual wording
Validation: SKIP

## Amendment 1

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| Hub §5 claimed verbatim while undated sentence was inline | R2 | R2 | Genuine | Split undated-page into spoke addendum; fixed L51/L76/L259/table/self-review |
| Year-rule body omits hub phrase under verbatim claim | R2-amend | R2-amend | FP | Hub CONTRIBUTING.md:73 and plan year-rule body match character-for-character on the (YYYY) sentence; only heading omits section number 5, which is expected for spoke. |

Why: undated-page was split out of the hub year-rule body. Residual source MAJOR on missing 'the year of' does not match the file text.

## Converged: Round 2 (amended)

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 2  |  Total fixes: 3
Document is ready.
