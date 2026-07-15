# agent-skill-creator component

Mode: `reference-only`

Upstream repository: <https://github.com/FrancyJGLisboa/agent-skill-creator>

Used by:

- [`skills/agent-builder`](../skills/agent-builder/)

## Purpose

This submodule provides a pinned, inspectable reference for plain-English-to-skill workflows, reusable skill packaging, validation, security scanning, eval guidance, and cross-platform installation ideas.

The `agent-builder` skill borrows concepts from this component, but does not vendor its source or require it at runtime.

## Not used for

- runtime imports
- generated code copied into `skills/agent-builder`
- automated builds
- required `npx skill` installation content
- mandatory downstream project setup

## Contribution workflow

If an improvement belongs upstream:

```bash
cd components/agent-skill-creator
git checkout -b <branch-name>
# make changes
git add .
git commit -m "Describe upstream improvement"
git push origin <branch-name>
```

Open a PR against the upstream repository or appropriate fork. After the upstream change is accepted, update this parent repository's submodule pointer intentionally.

## Parent pointer update

```bash
cd components/agent-skill-creator
git checkout main
git pull origin main

cd ../..
git add components/agent-skill-creator
git commit -m "Update agent-skill-creator component"
```
