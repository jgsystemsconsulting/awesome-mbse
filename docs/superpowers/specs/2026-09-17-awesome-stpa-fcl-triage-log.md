# FCL triage log: 2026-09-17-awesome-stpa

| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| C1 L294 MIT Press URL 403 + path malformed | R1 | R1 | FP (path) / Advisory-skipped (403) | Both path variants 403; canonical OA URL kept per research policy |
| M1 L96 SHA pin claim | R1 | R2 | Genuine | Fixed R1; R2 confirmed resolved |
| M2 L97 schedule labels | R1 | R2 | Genuine | Fixed R1; R2 confirmed resolved |
| M3 L118-121 J3187/AIR6913 | R1 | R2 | Genuine | Fixed R1; R2 confirmed resolved |
| M4 L123 eVTOL URL | R1 | R2 | Genuine | Fixed R1; R2 confirmed resolved (HTTP 200) |
| M5 L140-153 domain tag | R1 | R2 | Design | FAMILY axes override; R2 correspondent confirmed |
| M6 L160 tag order | R1 | R2 | Genuine | Fixed R1; R2 confirmed resolved |
| A1 L26 ~120 | R1 | R2 | Genuine | Fixed R1; R2 confirmed resolved |
| A2 illustrative years | R1 | R2 | Advisory-skipped | Labeled placeholders; R2 source confirmed |
| A3 sunnyday host | R1 | R2 | Genuine | Fixed R1; R2 confirmed resolved |

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| SHA pin claim | skeptic | MAJ | Genuine | Fixed |
| Schedule issue labels | skeptic | MAJ | Genuine | Fixed |
| J3187/AIR6913 URLs | source | MAJ | Genuine | Fixed |
| eVTOL URL | source | MAJ | Genuine | Fixed |
| domain tag | correspondent | MAJ | Design | Wontfix + note |
| tag order example | skeptic | MAJ | Genuine | Fixed |
| MIT Press 403 | source, correspondent | CRIT-promoted | FP/Advisory | Skipped per policy |
| ~120 count | skeptic | ADV | Genuine | Fixed |
| illustrative years | source | ADV | Advisory-skipped | Kept |
| sunnyday host | skeptic | ADV | Genuine | Fixed |

Fixes applied: 6 major + 2 advisory
Inflation rate: 17%
Validation: SKIP

## Round 2 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| All R1 fixed locs | skeptic, source, correspondent | — | resolved by this change | Confirmed |
| New C/M | all | — | none | — |

Fixes applied: 0
Inflation rate: n/a (0 CRITICAL+MAJOR findings this round)
Validation: SKIP

## Converged: Round 2

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 2  |  Total fixes: 8
Document is ready.
