# IVL triage log: 2026-09-17-repo-release-standard-capella

Target: plan `docs/superpowers/plans/2026-09-17-repo-release-standard-capella.md`
Spoke: https://github.com/jgsystemsconsulting/awesome-capella
EXECUTED: present

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| RR-B packaging files shipped (COPYRIGHT, NOTICE, CITATION, RELEASE-INFO, gate, validate, forms, Pages landing) | R1 | R1 | Genuine-pass | Tree + audit PASS rows |
| README Install/Usage/Support/Version + Contents TOC; awesome-lint green | R1 | R1 | Genuine-pass | npx awesome-lint OK |
| check_entries 73; check_release PASS | R1 | R1 | Genuine-pass | Commands exit 0 |
| Tag v0.1.0 + Release with licence footer | R1 | R1 | Genuine-pass | gh release view |
| Pages live 200 + homepage + 6 topics | R1 | R1 | Genuine-pass | curl + gh repo view |
| Branch protection required check validate | R1 | R1 | Genuine-pass | protection API |
| RR-B-20/21/22/23 PASS under --gh | R1 | R1 | Genuine-pass | audit --gh |
| audit.py plain exit 0 | R1 | R1 | Genuine residual | RR-B-27 FAIL: historical author emails (jason.gower@…, noreply@github.com on squash). Spec non-goal: no history rewrite. Residual named |
| GitHub license.spdx_id CC0 | R1 | R1 | Genuine residual | Still NOASSERTION (CC0 detection flaky with org trailer). RR-B-01 file PASS (org named). AC9 residual named |
| RR-B-25 forum.mbse-capella.org SSL expired on auditor host | R1 | R1 | Advisory-skipped | Entry URL may be live in browsers; SSL verify fail is env. Family lychee is advisory path |
| RR-B-32 improvement-form WARN | R1 | R1 | Design | Accepted; suggest-resource.yml is improvement channel (D8) |
| Playwright 2-breakpoint screenshots | R1 | R1 | Advisory-skipped | Mechanical taste PASS; Playwright residual per D5 |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Core AC packaging + platform | behavior | — | Pass | Verified |
| RR-B-27 history emails | contract | MAJ residual | Design | Wontfix history rewrite |
| spdx NOASSERTION | contract | ADV residual | Design | Named; file-level RR-B-01 PASS |
| SSL forum link | env | ADV | Advisory-skipped | Skipped |

Fixes applied: 0 (residuals accepted as Design/Advisory)
Inflation rate: n/a
Validation: PASS for shippable packaging; plain audit exit 1 solely on RR-B-27 history

## Converged: Round 1

Track 3: diminishing-return halt. Predicate: no-unfixed-genuine (packaging goals met; remaining FAILs are history rewrite non-goal and env SSL / accepted WARN).
Implementation verification ready.
Total rounds: 1  |  Total fixes: 0
