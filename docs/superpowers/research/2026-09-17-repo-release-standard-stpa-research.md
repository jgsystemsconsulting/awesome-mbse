# Research: Release Repo Standard for awesome-stpa

## Research brief

Apply Release Repo Standard v1.14 RR-B Base to `jgsystemsconsulting/awesome-stpa` (private STAMP/STPA awesome list).

## Findings

- **ESTABLISHED.** Standard path: `C:/Users/gower/.zcode/skills/release-repo-standard/references/release-repo-standard.md` v1.14. Auditor: `tools/audit.py --profile base`.
- **ESTABLISHED (audit 2026-09-17).** On `../awesome-stpa`: **11 FAIL, 2 WARN, 11 PASS**.
  - FAIL: COPYRIGHT, README Install/Usage + licensing URL, SECURITY advisory route, version mismatch, RELEASE-INFO, gate+CI, em dash SECURITY, CITATION.cff, bug form+config, machine-local path false positive on MIT `psas.../home/` URLs (RR-B-34), DISTRIBUTION.md.
  - WARN: no docs HTML taste, no improvement form filename match.
  - PASS: LICENSE, NOTICE, headers/SPDX (0 py), tree, gitignore, leaks, noreply, BOM, maintainer prefixes.
- **ESTABLISHED.** Sibling Capella RR-B pass: `docs/superpowers/specs/2026-09-17-repo-release-standard-capella.md` locked D1–D11 list-product interpretations.
- **ESTABLISHED.** Family public-release runbook: `docs/runbooks/family-public-release.md` Checklist A for spoke private→public; hub still private so pointer stays hub-private class.
- **ESTABLISHED.** Spoke HEAD private Live, 43 entries, CI triad green, text-only family pointer already correct.

## Synthesis

Profile **RR-B Base + OSS CC0 + standalone**. Close 11 FAILs with Capella-shaped packaging. Treat RR-B-34 `/home/` hits on `psas.scripts.mit.edu/home/` as **false positives** (public URLs, not machine-local paths); document in ledger if auditor cannot suppress. After packaging green, run **Checklist A** to flip spoke public and set hub Visibility `public` (hub itself stays private). RR-B-29 N/A for lists. suggest-resource form = improvement channel (WARN accepted).

## Sources

- https://github.com/jgsystemsconsulting/awesome-stpa
- https://github.com/jgsystemsconsulting/awesome-capella
- file://C:/Users/gower/.zcode/skills/release-repo-standard/references/release-repo-standard.md
- file://docs/runbooks/family-public-release.md
- audit.py run 2026-09-17 (11 FAIL / 2 WARN / 11 PASS)
