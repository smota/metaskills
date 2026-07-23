# Runtime capabilities

Agent: `<agent-name>`

| Capability | Required/optional/unavailable | Harness support | Owner | Evidence | Fallback | Validation |
| --- | --- | --- | --- | --- | --- | --- |
| Knowledge retrieval |  |  |  |  |  |  |
| MCP/OpenAPI tools/actions |  |  |  |  |  |  |
| Mutating actions |  |  |  |  |  |  |
| Agent-to-agent handoff |  |  |  |  | manual handoff checklist |  |
| Reviewer/validator gate |  |  |  |  | human review checklist |  |
| Subprocess/job start |  |  |  |  | user-run command |  |
| Job observe/wait/cancel/retry/resume |  |  |  |  | explicit status instructions |  |
| Async follow-up |  |  |  |  | user-run status check |  |
| Audit/logging |  |  |  |  | changelog note |  |
| Feedback/evals |  |  |  |  | local eval notes |  |

## Rules

- Use `unknown` when support is not verified.
- Missing capability is not failure if fallback is safe and documented.
- Mutating or externally visible capabilities require confirmation and rollback notes.
- Do not store secrets in generated package files.
