# Plan: link-check product surface

research: skipped (CI workflow path/args and known action SHAs; no external library choice)

## Tasks

1. Update link-check-pr.yml: paths + args + SHA pins.
2. Update link-check-schedule.yml: args + SHA pins including create-issue-from-file.
3. Grep verify docs/index.html in both args; no @v4/@v5 mutable tags remain in these files.
