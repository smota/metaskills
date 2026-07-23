# Level 2 tool-enabled agent example

Current maturity: Level 2. Target maturity: Level 3.

Uses read-only MCP/OpenAPI lookup action with `read` permission tier.

Fallback: if tool absent, provide manual lookup steps. If tool fails, report error and ask whether to retry.
## Validation

- Portable without `metaskills` runtime.
- `AGENT.md` remains canonical.
- Missing capability fallback is explicit.
