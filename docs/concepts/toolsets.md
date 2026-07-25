# Toolsets

A toolset documents reusable tool integration knowledge: schemas, wrappers, command patterns, MCP/OpenAPI notes, auth constraints, and validation procedures.

## Use a toolset when

- the primary value is integration mechanics
- multiple agents or skills need the same tool guidance
- schemas or wrappers should be reusable
- usage boundaries and failure modes matter

## Typical package

```text
toolsets/<toolset-name>/
├── README.md
├── schemas/
├── examples/
└── validation.md
```

Toolsets should not become hosted services inside this repo. Keep them portable and inspectable.
