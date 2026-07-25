# Components

A component is an external repository linked under `components/` when it has its own lifecycle, history, release process, or upstream contribution path.

## Component modes

- `reference-only` — prior art or reference material; native assets must not require it at runtime.
- `development-companion` — used for upstream-compatible development and PRs.
- `tool-provider` — scripts, CLIs, schemas, or tests are intentionally called from the submodule.

## Metadata

Each component should have a sibling metadata file:

```text
components/<component-name>.metaskills.md
```

See [Submodules](../reference/submodules.md).
