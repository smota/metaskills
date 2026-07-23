# Tool/action contract checklist

For each `tool/action`, verify:

- [ ] Purpose is clear.
- [ ] Permission tier is one of `read`, `suggest`, `stage`, `mutate`, `external-publish`, `admin`.
- [ ] MCP/OpenAPI schema reference exists.
- [ ] Inputs and outputs are documented.
- [ ] Auth requirements are documented without committed secrets.
- [ ] Confirmation rule is documented.
- [ ] Rollback/recovery exists for mutating or external actions.
- [ ] Audit/log expectation is documented.
- [ ] Tool absence fallback is distinct from tool failure fallback.
- [ ] Validation check exists.
