# Execution model: subprocess/job contracts

Use this when an agent may trigger external commands, builds, tests, scans, deployments, or long-running work. This file describes contracts only; it is not a job runner.

## Job inventory

| Job | Purpose | Mutating? | Confirmation required? | Timeout | Retry policy | Rollback | Fallback |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `test` | Run project tests | no | no | project-specific | retry after dependency/environment fix | none | user-run test command |
| `lint` | Run style/static checks | no | no | project-specific | retry after code/config fix | none | user-run lint command |
| `build` | Compile/package project | maybe | ask if outputs are committed/published | project-specific | retry only after fix | clean generated artifacts | user-run build command |
| `security-scan` | Detect secrets/vulnerabilities | no | no | project-specific | retry after tool/config fix | none | manual checklist scan |
| `data-processing` | Transform or summarize input data | maybe | ask before overwriting files | project-specific | retry only if idempotent | restore backup/original | dry-run or manual procedure |
| `deploy` | Publish externally visible changes | yes | yes | project-specific | retry only with approval | rollback release/deployment | deployment runbook |
| `<job-name>` |  | no | no |  |  |  | user-run command |

## Lifecycle

1. start: define command/action, inputs, cwd/environment, and authority.
2. observe: capture output without flooding context; summarize important lines.
3. wait: state when the agent should wait vs return with follow-up instructions.
4. cancel: define safe cancellation trigger and cleanup.
5. retry: retry only idempotent jobs or after user approval.
6. resume: record job id/path/status and next command.
7. complete: report output, validation, changed state, risks, and follow-up.

## Error/fallback schema

```yaml
job: ""
status: failed | cancelled | timed-out | blocked
error: ""
known_cause: ""
fallback: ""
retry_safe: false
requires_human: true
```

## Safety rules

- Mutating jobs require confirmation before start.
- Production or externally visible jobs require rollback notes.
- Never hide failed jobs; report exact status.
- Do not require secrets in committed files.
