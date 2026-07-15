# Example: improved skill

## Original issue

Users asked a deployment skill to roll back a failed release, but the skill only documented forward deployment.

## Evidence

- Failed eval: `rollback-required`
- Feedback: users expected rollback guidance

## Improvement

- Added rollback boundary: ask for confirmation before production actions.
- Added `references/rollback-runbook.md`.
- Added eval case for failed deployment.

## Acceptance

- Existing deployment evals still pass.
- New rollback eval passes.
- Skill remains focused on deployment support, not incident management.
