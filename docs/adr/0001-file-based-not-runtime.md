# ADR 0001: MetaSkills is file-based, not a runtime

## Status

Accepted

## Context

MetaSkills provides reusable skills, agents, toolsets, examples, and references. Users adopt these assets in their own repositories and harnesses.

## Decision

MetaSkills will remain file-based and portable. It will not become a hosted agent platform, runtime, queue, control plane, deployment system, or management service.

## Consequences

- Assets must be useful when copied into another repo.
- Harness capabilities are documented through adapters and contracts.
- Runtime machinery belongs to adopting environments.
- Documentation should distinguish portable intent from platform-specific execution.
