# Link-check product surface

## Research

research: skipped (CI workflow path/args and known action SHAs; no external library choice)

## Goal

Lychee covers README.md and docs/index.html. PR path filters include the landing.
Mutable action tags in link-check workflows become full SHAs. PR fail:true stays;
schedule remains report-only.

## Acceptance

1. Both workflows list docs/index.html in lychee args.
2. PR paths include docs/index.html.
3. checkout, setup-node, create-issue-from-file use full SHAs with version comments.
4. lychee-action pin unchanged.
