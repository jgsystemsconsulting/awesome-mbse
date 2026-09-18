# FCL triage log: 2026-09-17-repo-release-standard-capella

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| RR-B-20 MUST deferred as maintainer deferral | R1 | R1 | Genuine | Ship docs/index.html + Pages |
| RR-B-05 Install via substring dodge | R1 | R1 | Genuine | Real Install heading |
| RR-B-03 overclaim on all .md headers | R1 | R1 | Genuine | Auditor .py scope named |
| audit-green = standard-complete framing | R1 | R1 | Genuine | Necessary not sufficient |
| LICENSE preamble / NOASSERTION | R1 | R1 | Genuine | Verify spdx_id AC |
| RR-B-08 PASS label | R1 | R1 | Genuine | present vs 09 PASS |
| Family context pure-list no RR-B | R1 | R1 | Design | User explicitly invoked release-repo-standard on Capella; this pass is RR-B packaging not family flip runbook |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| RR-B-20 deferral | skeptic | CRIT | Genuine | Fixed D5 ship Pages |
| Install heading | skeptic | MAJ | Genuine | Fixed |
| RR-B-03 scope | skeptic | MAJ | Genuine | Fixed |
| Framing | skeptic | MAJ | Genuine | Fixed |
| Family RR-B ban | correspondent | CRIT | Design | Wontfix user invoke |

Fixes applied: 6
Inflation rate: ~15%
Validation: SKIP

## Round 2 Summary (parent confirmation)

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| D5/Install/RR-B-20 strings on disk | parent | — | resolved by this change | Verified |

## Converged: Round 2

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Document is ready.
Total rounds: 2  |  Total fixes: 6
