# Agent package release checklist

- [ ] Review `git status` and confirm intended files only.
- [ ] Package can be copied out of `metaskills` with no runtime dependency on this repo.
- [ ] `AGENT.md` is canonical; compatibility files/adapters point back to it.
- [ ] No long instructions are duplicated across harness files.
- [ ] Runtime capabilities include required/optional/unavailable/unknown states.
- [ ] Adapter files are isolated under `adapters/` or documented target sections.
- [ ] Feedback artifacts contain redaction/local-only guidance and no secrets.
- [ ] Examples state maturity level and fallback behavior.
- [ ] JSON templates validate.
- [ ] OpenAPI YAML indentation and schema structure reviewed.
- [ ] README and SKILL template lists match files shipped.
- [ ] Changelog records what changed and why.
