# Microsoft Foundry adapter

Map canonical agent package assets into Microsoft Foundry or Copilot-style configuration when target environment uses those services. Microsoft deployment is optional.

## Required features

- `AGENT.md` canonical instructions.
- Target Foundry project or equivalent deployment environment only when deployment is requested.
- Tool/action schemas, preferably OpenAPI, for action-enabled agents.

## Supported features

- Instructions: map from `AGENT.md`.
- Knowledge: map from `knowledge-sources.md`.
- Actions: map from `tools-actions.md` and OpenAPI schema.
- Evaluation: map from `evals.md` or eval suite.
- Monitoring: map improvement signals to `continuous-improvement-plan.md`.

## Unsupported or unknown features

- No Foundry project -> fallback: keep package as local harness-neutral agent docs.
- No action deployment -> fallback: manual procedure from `tools-actions.md`.
- No continuous monitoring -> fallback: local feedback/eval loop.
- No A2A orchestration -> fallback: handoff checklist.

## Configuration notes

- Do not put tenant IDs, keys, secrets, or private endpoints in committed files.
- Keep deployment-specific IDs in local environment/config, not canonical package.
- Use `microsoft-foundry` deployment guidance only when user asks for Foundry implementation.

## Validation

- Validate OpenAPI schema before import.
- Run at least one prompt eval and one action-failure fallback eval.
- Confirm deployed instructions match `AGENT.md` or document intentional adapter-only invocation differences.

## No semantic override

This adapter must not redefine role, scope, authority, safety rules, or success criteria from `AGENT.md`.
