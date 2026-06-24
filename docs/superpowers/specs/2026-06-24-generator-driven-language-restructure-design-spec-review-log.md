# Spec Review Triage Log

Spec: `2026-06-24-generator-driven-language-restructure-design.md`
Domain mapping: software/tooling — Security = CI/supply-chain + markdown injection + link safety; Ops = CI reliability, generator maintainability, contributor workflow.

| Round | Persona | Severity | Finding | Verdict | Action |
|-------|---------|----------|---------|---------|--------|
| 1 | Security | CRITICAL | yaml.load → code exec on untrusted YAML | accepted | Mandated yaml.safe_load in Security section |
| 1 | Security | CRITICAL | No URL scheme allowlist (javascript:/data:) | accepted | URL allowlist https/http in Validation + Security |
| 1 | Architect+QA | CRITICAL (promoted) | --check diff CRLF/LF undefined | accepted | Normalised LF output + normalised compare |
| 1 | Security | MAJOR | title/desc markdown/HTML injection | accepted | Escaping rule in Security section |
| 1 | Security+Ops | MAJOR | CI token exposure / PR runs generate.py | accepted | generate-check no secrets, contents:read; lychee separate |
| 1 | QA | MAJOR | "no entry dropped" not automated | accepted | Permanent entry/flagship count invariant |
| 1 | QA+Security | MAJOR | slug collision / flagship misuse / enum typos | accepted | Validation rules subsection (fail closed) |
| 1 | Architect | MAJOR | AUTOGEN marker format undefined | accepted | AUTOGEN marker exact contract subsection |
| 1 | Ops | MAJOR | Python/PyYAML unpinned → non-reproducible | accepted | Reproducibility (pinned) subsection |
| 1 | Ops+Product | MAJOR (promoted) | stale-README contribution friction | accepted | Pre-commit hook; kept local-generate w/ rationale |
| 1 | Product | MAJOR→ (advisory promoted) | awesome-lint structural rules absent | accepted | awesome-lint conformance subsection |
| 1 | Architect | ADVISORY | lang mixes notation + routing | clarified | Defined lang: cross-cutting explicitly |
| 1 | QA | ADVISORY | view filters not in real fields | accepted | View filter definitions subsection |
| 1 | Architect | ADVISORY | sort order within sections undefined | accepted | Ordering (deterministic) subsection |
| 1 | Ops | ADVISORY | rollback path unstated | accepted | Rollback note in CI section |
| 1 | Product | MAJOR | remove competitive-landscape (neutrality) | rejected | Pre-existing content, out of scope; neutrality in CONTRIBUTING §7 |
| 1 | Product | ADVISORY | defer views 2-4 until list grows | rejected | User explicitly chose all four views |
| 2 | Test/QA | CRITICAL | count invariant ambiguous for cross-cutting/no-subsection | accepted | Rewrote invariant: spine placement, exactly-one-home, views excluded |
| 2 | Test/QA | CRITICAL | By-tool double-count breaks invariant | accepted | Invariant counts distinct records; separate N-tags→N-groups assertion |
| 2 | Product | MAJOR | "which fits whom" half not delivered by structure | accepted | Mandated intro chooser + per-notation "Use this when" blurb + criterion |
| 2 | Ops | MAJOR | web-UI/non-Python contributor dead-end | accepted | Maintainer rescue path (issue form + label-triggered regen job) |
| 2 | Ops | MAJOR | pre-commit hook distribution unspecified | accepted | .pre-commit-config.yaml + documented install command |
| 2 | Test/QA | MAJOR | tag legend bidirectional coverage unchecked | accepted | Validation: every used tag must be in legend; orphan=warn |
| 2 | Test/QA | MAJOR | awesome-lint not a named CI job | accepted | Added awesome-lint as third required CI job |
| 2 | Test/QA | MAJOR | empty-section "non-empty" undefined | accepted | Defined non-empty + self-check fixture case |
| 2 | Security | MAJOR | URL allowlist bypass (case/whitespace) | accepted | Normalise (strip+lowercase scheme) before check, decoded form |
| 2 | Security | MAJOR | image-syntax / table-cell breakout | accepted | Escape set extended to [ ] ( ) ! \| < > backtick |
| 2 | Architect | MAJOR | marker name↔section mapping unclear | accepted | Added marker mapping table (section id = lang value) |
| 2 | Architect | MAJOR | tool set vs tag vocab unreconciled | accepted | Validation: tool tokens strict subset of tag vocab |
| 2 | Test/QA | ADVISORY | slug algorithm imprecise; BOM/reorder untested | accepted | Specified GitHub slug algorithm; enumerated self-check fixtures |
| 2 | Architect | ADVISORY | missing template file unhandled | accepted | Template-integrity validation rule |
| 2 | Ops | ADVISORY | Python version drift local vs CI | accepted | CONTRIBUTING names 3.11 canonical (pyenv/asdf) |
| 2 | Ops | ADVISORY | generate-check no path filter | accepted | Added paths filter to generate-check |
| 2 | Security | ADVISORY | pre-commit token clarity; entity-decoded URL | accepted | Hook local-only no token; URL check on decoded form |
| 2 | Product | ADVISORY | no success criterion for self-explaining | accepted | Added notation-guidance success criterion |
| 3 | Security | CRITICAL | rescue job could run PR-head code with write token | accepted | Rescue job: code from base branch only, data from PR after validation |
| 3 | Test/QA | MAJOR | jump-to-notation CI vs manual unclear | clarified | Stated lychee anchor-only check verifies Contents links (already CI) |
| 3 | Test/QA | MAJOR | per-section blurb presence unchecked | accepted | Validation rule: blurb non-empty before AUTOGEN:START or error |
| 3 | Ops | MAJOR | paths-filter + required-check skip-blocks-merge trap | accepted | Dropped paths filter; generate-check always runs, fast exit |
| 3 | Ops | MAJOR | rescue job needs fork "Allow edits by maintainers" | accepted | Job checks maintainerCanModify, comments if false; documented |
| 3 | Architect | ADVISORY | arcadia/opm/oml marker mapping unclear | accepted | Each lang = own marker; combined H2 is prose |
| 3 | Architect | ADVISORY | count-invariant view caveat redundant/confusing | accepted | Reworded: spine placement vs view rows |
| 3 | Product | — | CLEAN | converged | No action; not re-run in R4 |
| 4 | Security | — | CLEAN | converged | Rescue-job fix verified sound |
| 4 | Ops | — | CLEAN | converged | CI/rescue fixes verified sound |
| 4 | Architect | — | CLEAN | converged | Marker/structure consistency verified |
| 4 | Test/QA | ADVISORY | no blurb-missing self-check fixture | accepted | Added blurb-missing case to self-check enumeration |

**CONVERGED in 4 rounds** — Round 4 returned no CRITICAL or MAJOR findings (all four re-run personas CLEAN; one advisory applied).
