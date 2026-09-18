# Research: repo-release-standard (family public release)

## Research brief

External facts needed for a family public-release runbook: sindresorhus/awesome
submission expectations at high level; confirmation public GitHub repos are
reachable without auth for FAMILY hyperlinks.

## Findings

- sindresorhus/awesome pull_request_template exists on the main branch of
  https://github.com/sindresorhus/awesome and is the usual entry point for list
  submissions (list must already be public and meet their quality bar). Exact
  checklist text is versioned there; runbook should link the live template
  rather than fork it.
- Public family spokes (awesome-sysml-v2, awesome-capella,
  awesome-digital-engineering) are `PUBLIC` via gh; hub and
  awesome-requirements-engineering are `PRIVATE` (2026-09-17).
- While hub remains private, a public spoke cannot usefully hyperlink
  `github.com/jgsystemsconsulting/awesome-mbse/blob/main/FAMILY.md` for
  anonymous readers (404). That matches FAMILY private-mode text-only rule.
- Pointer audit (local checkouts 2026-09-17): sysml-v2, capella, and RE use
  text-only family lines. awesome-digital-engineering README line 8 still
  hyperlinks the private hub FAMILY.md blob URL (Private mode violation).

## Synthesis

research: internal-primary + one external pointer (sindresorhus/awesome).
No version-sensitive library choice. Runbook links
https://github.com/sindresorhus/awesome as post-hub-public step only.

## Sources

| URL | Role |
|-----|------|
| https://github.com/sindresorhus/awesome | List-of-lists submission target |
| https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md | Submission PR template |
