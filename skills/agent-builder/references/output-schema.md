# Agent builder output schema

Use this shape when returning a generated agent package summary.

```json
{
  "name": "agent-name",
  "description": "when to use this agent",
  "current_maturity_level": 0,
  "target_maturity_level": 1,
  "canonical_files": ["AGENT.md", "README.md"],
  "runtime_capabilities": {
    "required": [],
    "optional": [],
    "unavailable": [],
    "unknown": []
  },
  "knowledge_sources": [],
  "tools_actions": [],
  "handoff_contracts": [],
  "subprocess_jobs": [],
  "adapters": [],
  "evals": [],
  "known_gaps": [],
  "validation": {
    "status": "pass|partial|fail",
    "checks": []
  },
  "follow_up": []
}
```
