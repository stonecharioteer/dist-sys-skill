# 09. Metadata index with crash recovery

- **Tier:** `applied`
- **Exercise type:** `focused_component_design`
- **Primary phases:** `single_machine`, `storage`, `reliability`
- **Prerequisites:** [`05. Append-only log with crash recovery`](../05-append-only-log-crash-recovery/README.md), [`06. Single-node key-value store`](../06-single-node-kv-store/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `applied`-level systems reasoning.

## What to learn

- secondary-index recovery
- replay ordering
- rebuild vs persist trade-offs

## Prep reading

### Required (about 40–55 minutes total)

- _Designing Data-Intensive Applications_ — Chapter 3, **Storage and Retrieval**
  - Why: sets up derived data structures and update-path trade-offs.
- PostgreSQL documentation — **Write-Ahead Logging (WAL)**: https://www.postgresql.org/docs/current/wal-intro.html
  - Why: gives a concrete model for durable ordering and crash recovery.

### Optional (10–15 minutes)

- PostgreSQL documentation — **Introduction to Indexes**: https://www.postgresql.org/docs/current/indexes-intro.html
  - Why: useful reminder that secondary structures have maintenance cost.

### Enough for today when you understand

- why primary data and derived indexes can diverge
- why recovery ordering matters
- when rebuild-on-startup is better than persisting everything

## What to build

Design a metadata indexing service whose primary data and derived indexes remain usable after crashes.

## What a strong solution should show

A good solution explains which indexes are persisted, which can be rebuilt, and how torn updates are repaired.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier

## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 09 start`
- `dist-sys 09 new`
- `dist-sys 09 list`
- `dist-sys 09 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under the exercise's default attempt store in `~/.dist-sys/<exercise-folder>/submissions/`.
