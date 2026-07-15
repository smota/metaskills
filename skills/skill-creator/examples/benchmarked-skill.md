# Example: benchmarked skill

## Benchmark

- Skill: `release-note-helper`
- Baseline: v1
- Candidate: v2

## Result summary

| Case | Baseline | Candidate | Winner | Notes |
| --- | --- | --- | --- | --- |
| groups changes | pass | pass | tie | both grouped features/fixes |
| detects breaking changes | partial | pass | candidate | v2 added explicit breaking-change scan |
| avoids unsupported claims | pass | pass | tie | both cited missing context |

## Decision

Adopt candidate v2.

## Learning log entry

Release-note skills need an explicit breaking-change scan because commit summaries often hide compatibility impact.
