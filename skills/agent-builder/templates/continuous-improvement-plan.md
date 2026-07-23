# Continuous improvement plan

## Loop

1. Observe failures or feedback.
2. Classify: scope, knowledge, tool/action, safety, UX, orchestration, environment.
3. Patch evals or regression cases first when possible.
4. Update instructions, tools/actions, adapters, or contracts.
5. Validate against eval suite and maturity scorecard.
6. Record change in `CHANGELOG.md`.

## Feedback handling

- Keep feedback local unless user approves sharing.
- Redact secrets, tokens, private credentials, customer data, and sensitive prompts.
- Store minimal evidence needed to reproduce issue.

## Improvement record

| Date | Signal | Category | Change | Eval added/updated | Result | Follow-up |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

## Benchmark cadence

- Before major instruction changes.
- Before adding mutating tools/actions.
- Before release.
- After repeated failures in same category.
