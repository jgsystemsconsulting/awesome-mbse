| Finding | First seen | Last seen | Verdict | Rationale |
|---------|------------|-----------|---------|-----------|
| Wiley required URL replaced by LCCN | R1 | R1 | Design | Plan listed Wiley product URL; live fetch 404. Inclusion bar requires live links. LCCN 2008042045 is same book, HTTP 200. Live-link priority over dead plan URL. |

## Check commands

1. Spoke entry checker (count/format/years)
2. gh visibility PRIVATE
3. FAMILY Live|private + README Live
4. Text-only family pointer
5. Workflows + link-rot issue
6. Required URL scan (11/12 exact; Wiley→LCCN design)

## Baseline

entry_count 40
hub_family_link False
text_only_pointer True
required_missing none (with LCCN standing for Wiley book identity)
entries_without_year 0
visibility PRIVATE
link-rot open: 1 (#2)
FAMILY Live | private
README Live private spoke note
Wiley plan URL HTTP 404; LCCN HTTP 200

## Round 1 Summary

| Finding | Lens | Severity | Verdict | Action |
|---------|------|----------|---------|--------|
| Wiley URL vs LCCN | behavior | CRIT | Design | Wontfix keep live LCCN |
| private/40/CI/hub | behavior, contract | — | clean | — |
| regression files | parent (regression model unavailable) | — | clean | CONTRIBUTING+CI present |

Fixes applied: 0
Inflation rate: 100% (1 of 1 CRITICAL+MAJOR Design)
Validation: PASS
Commands: entry checker exit 0; gh visibility PRIVATE; curl Wiley 404; curl LCCN 200; hub grep Live|private

## Converged: Round 1

Track 1: Merged verdict NO_CRITICAL_OR_MAJOR.
Total rounds: 1  |  Total fixes: 0
Implementation verification ready.

Note: regression lens type unavailable (GLM-5.2); parent verified CONTRIBUTING.md, workflows, fail:true, no FAMILY hyperlink.
