# skill-builder component

Mode: `reference-only`

Upstream repository: <https://github.com/metaskills/skill-builder>

Used by:

- [`skills/skill-creator`](../skills/skill-creator/)

## Purpose

This submodule provides a pinned, inspectable reference for production-ready skill structure, progressive disclosure, intention-revealing supporting files, and converting sub-agents into skills.

The native `skill-creator` skill borrows concepts from this component, but does not vendor its source or require it at runtime.

## Not used for

- runtime imports
- generated code copied into `skills/skill-creator`
- automated builds
- required `npx skill` installation content
- mandatory downstream project setup

## Contribution workflow

If an improvement belongs upstream, branch inside `components/skill-builder`, make the change, push to the upstream repository or fork, and open a PR. After upstream accepts the change, update this parent repository's submodule pointer intentionally.
