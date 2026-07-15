# Agent tools/actions

Document each tool or action before enabling it.

## Tool/action template

```yaml
name:
purpose:
read_only: true | false
inputs:
  - name:
    type:
    required: true | false
outputs:
  - name:
    type:
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
