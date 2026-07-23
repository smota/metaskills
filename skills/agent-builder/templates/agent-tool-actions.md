# Agent tools/actions

Document each tool/action with MCP or OpenAPI schemas before enabling it. Avoid ad-hoc input/output docs when a standard schema can represent the contract.

## Permission tiers

- `read`: retrieve or inspect only.
- `suggest`: produce recommendations only.
- `stage`: prepare local changes without external effects.
- `mutate`: change files, databases, or state.
- `external-publish`: send, deploy, post, or notify outside the local workspace.
- `admin`: manage permissions, secrets, billing, production, or destructive operations.

## Tool/action template

```yaml
name:
purpose:
permission_tier: read | suggest | stage | mutate | external-publish | admin
read_only: true
schema_ref: mcp-tool-schema.json | openapi-tool-schema.yaml
inputs:
  schema:
outputs:
  schema:
auth:
  required: false
  notes: "never commit secrets"
safety:
  confirmation_required: false
  constraints: []
  rollback: ""
  audit: ""
fallbacks:
  tool_absent: "manual procedure or degraded answer"
  tool_failure: "retry/diagnose/escalate behavior"
failure_modes:
  - failure: ""
    handling: ""
validation:
  - check: ""
```

## Rules

- Prefer read-only tools until mutation is necessary.
- Ask for confirmation before destructive or externally visible actions.
- Never require secrets to be written into committed files.
- Separate tool absence from tool failure.
- Include fallback behavior for every tool/action.
