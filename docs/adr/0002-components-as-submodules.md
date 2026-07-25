# ADR 0002: External components are submodules

## Status

Accepted

## Context

Some useful references have their own repositories, history, release cadence, issues, and upstream contribution paths.

## Decision

External repositories should be linked under `components/` as Git submodules with sibling `.metaskills.md` metadata.

## Consequences

- Native assets should not copy external source when a submodule is more appropriate.
- Component mode must be explicit: `reference-only`, `development-companion`, or `tool-provider`.
- Reference-only components must not be required for installation or runtime.
- Changes inside submodules must be committed and pushed in the submodule before updating parent pointers.
