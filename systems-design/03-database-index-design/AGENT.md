# Agent notes for 03. Database index design for a read-heavy workload

## Purpose

This file is for future agent use when building real, language-specific scaffolding for this exercise.

## What to expect from a user solution

Expect the learner to work from the fixed schema and hot-query prompt in `README.md`, not to invent the entire workload from scratch. Testing and review should focus on query behavior and index choice, not vendor syntax.

A strong submission should usually include:

- the proposed secondary indexes for the provided schema
- a mapping from each chosen index to one or more explicit hot queries
- recognition of when a composite index is more useful than multiple single-column indexes
- discussion of write amplification, storage cost, and redundant indexes
- clear scope control: single-node reasoning only, no distributed extensions

## Future scaffolding plan

When a real implementation track is chosen, scaffolding should stay language-agnostic at the contract level and only become language-specific at the harness layer.

Recommended future checks:

- provide the canonical schema and hot queries from `README.md` during interview startup
- check whether proposed indexes cover the hot queries
- probe whether the learner can explain composite index ordering
- probe write-heavy updates for index maintenance cost
- flag redundant or low-value indexes
- flag solutions that exceed the stated index-budget constraint without strong justification

## Suggested future scaffold shape

- `fixtures/` for workload descriptions, traces, or canned scenarios
- `cases/` for happy-path, edge-case, and failure-injection scenarios
- `oracle/` for invariants, expected outcomes, or scoring helpers
- `README.md` updates describing how the selected language track maps to the original exercise contract

## Guardrails for future agent work

- Do not overfit scaffolding to one language unless that track is intentionally selected.
- Preserve the exercise's stated invariants and failure model.
- Prefer contract tests, trace replay, and rubric checks over framework-specific implementation requirements.
- This is a foundation exercise: do not force the learner to invent the domain, schema, and workload all at once.
- Start from the bounded problem statement in `README.md`, including the scale assumptions and index-budget constraint.
- Keep room for multiple valid index sets, but anchor discussion to the provided hot queries.

## Session control contract

This exercise participates in the curriculum-wide session workflow in [`../WORKFLOW.md`](../WORKFLOW.md).

The controlling commands for this exercise are:

- `dist-sys 03 start`
- `dist-sys 03 new`
- `dist-sys 03 list`
- `dist-sys 03 review`

After `start` or `new`, the agent should switch into natural-chat interview mode and keep appending learner work to the active attempt folder under `~/.dist-sys/<exercise-folder>/submissions/`.

The opening for this specific exercise should restate the provided schema, workload scale, hot queries, and the limit on total secondary indexes before asking the learner to choose an index strategy.

## Review rubric

Review this exercise against the bounded problem in `README.md`.

### Strong submission

A strong submission should:

- propose a small index set that fits within the stated index budget, or justify any extra index clearly
- map each chosen index to one or more of the provided hot queries
- use composite indexes where they clearly outperform multiple weaker single-column indexes
- explain left-to-right index ordering in terms of the query filters and joins
- identify at least one index that is unnecessary or redundant
- discuss write amplification and storage overhead, especially on the large `sightings` table
- stay within single-node scope

### Partial submission

A partial submission may:

- identify some useful indexes but fail to connect them cleanly to query shapes
- overuse single-column indexes where a composite index would be better
- mention trade-offs only vaguely
- miss the fact that a composite index may make a prefix single-column index redundant

### Weak submission

A weak submission typically:

- indexes nearly every filtered column without prioritization
- ignores the index-budget constraint
- does not tie indexes to explicit hot queries
- does not discuss write or storage cost
- drifts into distributed systems concerns that are out of scope here

### Common coaching points

Use these during review when relevant:

- "Index the query pattern, not the table in the abstract."
- "A foreign key can also be part of an index; constraints and access paths are different concerns."
- "A composite index may make a weaker single-column index redundant."
- "On a large event table, every extra index increases write cost."
- "You do not need sharding, replicas, or distributed indexing for this exercise."

Expected attempt files:

- `submission.md`
- `review.md`
- `metadata.yaml`
- `assets/` for exported diagrams such as PNG or SVG from Excalidraw
