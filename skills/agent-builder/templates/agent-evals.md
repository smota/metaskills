# Agent evals

## Rule

When improving an agent, add or update evals before or alongside instruction changes.

## Eval case template

| Field | Value |
| --- | --- |
| Scenario |  |
| Prompt |  |
| Maturity level |  |
| Category | scope / knowledge / tool-action / safety / UX / orchestration / environment |
| Expected behavior |  |
| Must include |  |
| Must not include |  |
| Known gap? | false |
| Regression? | false |
| Pass criteria |  |

## Required coverage

- happy path
- out-of-scope/refusal
- missing knowledge
- missing tool or runtime capability
- tool/action failure, if applicable
- delegation/job failure, if applicable
- safety boundary
