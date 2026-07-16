# Agent tools/actions

Document each tool or action using standard Model Context Protocol (MCP) or OpenAPI schemas before enabling it.
Avoid ad-hoc custom documentation for inputs and outputs. Instead, reference standard JSON Schema for `inputSchema` (MCP) or standard OpenAPI paths.

## Tool/action template

```yaml
name:
purpose:
read_only: true | false
schema_ref: # Reference to mcp-tool-schema.json or openapi-tool-schema.yaml
auth:
  required: true | false
  notes:
safety:
  confirmation_required: true | false
  constraints:
    -
failure_modes:
  - failure:
    handling:
validation:
  - check:
```

## Rules

- Prefer read-only tools until mutation is necessary.
- Ask for confirmation before destructive or externally visible actions.
- Never require secrets to be written into committed files.
- Include fallback behavior for tool failures.
