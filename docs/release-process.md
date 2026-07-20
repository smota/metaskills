# Release process

`metaskills` uses lightweight GitHub releases to make changes easy to discover and share.

## Before release

1. Review `git status` and confirm only intended files changed.
2. Confirm README install commands are still accurate.
3. Confirm the skill catalog matches `skills/`.
4. Confirm examples do not include secrets, private data, or local-only assumptions.
5. Confirm website links to GitHub, examples, and install commands.
6. Update `CHANGELOG.md`.

## Suggested release notes structure

```markdown
## What changed

- Added or improved skills/examples/docs.

## Why it matters

- Explain the user-facing benefit.

## How to try it

```bash
npx skills add https://github.com/smota/metaskills --list --full-depth
```

## Validation

- List checks performed.
```

## After release

- Publish the GitHub release.
- Link the release from the website banner if relevant.
- Share concise announcement copy with examples and install commands.
