# Agent Guardrails Matrix

| Action / Capability | Scope Limit | User Confirmation Required? | Fallback / Failure Mode | Data Privacy |
| :--- | :--- | :--- | :--- | :--- |
| e.g., File Write | e.g., Only within ./src/ | e.g., Yes | e.g., Halt and prompt user | e.g., No PII extraction |
| e.g., Autonomous Loop | e.g., Max 5 iterations | e.g., No | e.g., Fallback to user | e.g., Local only |
| e.g., Tool Call | e.g., Max 10 calls | e.g., No | e.g., Terminate run | e.g., N/A |
