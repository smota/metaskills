# Agent guardrails matrix

| Capability | Permission tier | Allowed? | Confirmation required? | Mutation authority | Secret exposure risk | Delegated scope | Audit/trace | Rollback/fallback |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Knowledge lookup | read | yes | no | none | low | none | cite source | missing-context answer |
| Tool/action |  |  |  |  |  |  |  |  |
| Agent-to-agent handoff |  |  |  |  | do not forward secrets |  | handoff record | manual checklist |
| Subprocess/job |  |  |  |  |  |  | job status | cancel/retry/resume plan |

## Default rules

- Do not expose secrets, tokens, credentials, or sensitive customer data.
- Do not escalate delegated authority beyond this matrix.
- Confirm destructive, external, production, or admin actions.
- Report validation honestly.
