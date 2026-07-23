# Harness adapter model

Agent packages should be harness-neutral by default and harness-capability-aware when installed somewhere with extra primitives.

## Boundary

- `AGENT.md` defines canonical semantics: role, scope, safety, success criteria.
- Adapters define invocation mechanics and optional capability mappings.
- Adapters must not redefine scope, authority, or safety rules.
- Missing harness capability must be explicit and paired with fallback.

## Capability mapping

| Semantic need | Harness primitive when present | Generic fallback |
| --- | --- | --- |
| Research delegation | subagent single/parallel | manual handoff checklist |
| Review gate | reviewer/validator agent | human review checklist |
| Planner-worker split | chained agents | sequential checklist in `AGENT.md` |
| Long-running work | async `subprocess/job` | command instructions plus resume notes |
| Tool call | MCP/OpenAPI tool/action | documented manual procedure |
| Notifications/follow-up | inbox, event, or job completion hook | user-run status check |
| Memory/learning | local feedback/eval store | changelog and manual eval notes |

## Adapter requirements

Each adapter must state:

- target harness and version assumptions
- supported capabilities
- unsupported or unknown capabilities
- configuration steps
- fallback behavior
- validation check
- no-semantic-override statement
