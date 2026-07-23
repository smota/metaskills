# Level 2 tool-enabled agent fixture

Current maturity: Level 2 tool-enabled agent.
Target maturity: Level 3 action agent.

## Package shape

```text
agents/dependency-lookup-agent/
├── README.md
├── AGENT.md
├── tools-actions.md
├── runtime-capabilities.md
├── capability-maturity-scorecard.md
├── agent-validation-checklist.md
├── evals.md
└── schemas/
    ├── mcp-tool-schema.json
    └── openapi-tool-schema.yaml
```

## Tool/action contract

- Tool: package metadata lookup.
- Permission tier: `read`.
- Schema: MCP or OpenAPI lookup schema.
- Auth: none or documented token from environment; no committed secrets.
- Confirmation: not required for read-only lookup.

## Fallback behavior

- Tool absent: explain lookup unavailable and provide manual registry search steps.
- Tool failure: quote error summary, ask whether to retry, and avoid stale claims.

## Validation

- JSON schema validates.
- OpenAPI YAML parses.
- Missing-tool eval returns manual procedure.
- `AGENT.md` remains canonical and harness-neutral.
