# Agent notes for 06. Single-node key-value store

## Purpose

This file is for future agent use when building real, language-specific scaffolding for this exercise.

## What to expect from a user solution

Expect API semantics, local durability design, and a small observability surface.

A strong submission should usually include:

- explicit assumptions about scale, constraints, and out-of-scope items
- a design that matches the declared tier and exercise type
- a clear explanation of trade-offs, failure behavior, and operational signals
- language-agnostic artifacts first; implementation details later if a language track exists

## Future scaffolding plan

When a real implementation track is chosen, scaffolding should stay language-agnostic at the contract level and only become language-specific at the harness layer.

Recommended future checks:

- check functional correctness for Get/Put/Delete histories
- inject crash/restart around acknowledged writes
- measure storage growth under overwrite-heavy workloads
- verify documented limits around large values or scans

## Suggested future scaffold shape

- `fixtures/` for workload descriptions, traces, or canned scenarios
- `cases/` for happy-path, edge-case, and failure-injection scenarios
- `oracle/` for invariants, expected outcomes, or scoring helpers
- `README.md` updates describing how the selected language track maps to the original exercise contract

## Guardrails for future agent work

- Do not overfit scaffolding to one language unless that track is intentionally selected.
- Preserve the exercise's stated invariants and failure model.
- Prefer contract tests, trace replay, and rubric checks over framework-specific implementation requirements.
- Keep room for multiple valid designs when the exercise is intentionally open-ended.

## Session control contract

This exercise participates in the curriculum-wide session workflow in [`../WORKFLOW.md`](../WORKFLOW.md).

The controlling commands for this exercise are:

- `dist-sys 06 start`
- `dist-sys 06 new`
- `dist-sys 06 list`
- `dist-sys 06 review`

After `start` or `new`, the agent should switch into natural-chat interview mode and keep appending learner work to the active attempt folder under `~/.dist-sys/<exercise-folder>/submissions/`.

Expected attempt files:

- `submission.md`
- `review.md`
- `metadata.yaml`
- `assets/` for exported diagrams such as PNG or SVG from Excalidraw
