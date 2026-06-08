# 06. Single-node key-value store

- **Tier:** `foundation`
- **Exercise type:** `open_ended_design`
- **Primary phases:** `single_machine`, `storage`
- **Prerequisites:** [`05. Append-only log with crash recovery`](../05-append-only-log-crash-recovery/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `foundation`-level systems reasoning.

## What to learn

- request lifecycle design
- durable state reconstruction
- basic local capacity reasoning

## Prep reading

### Required (about 45–60 minutes total)

- _Designing Data-Intensive Applications_ — Chapter 2, **Data Models and Query Languages**
  - Why: helps you decide what your key-value interface is really promising.
- _Designing Data-Intensive Applications_ — Chapter 3, **Storage and Retrieval**
  - Why: gives the right storage/index/durability background for a local KV design.

### Optional (10–15 minutes)

- PostgreSQL documentation — **Write-Ahead Logging (WAL)**: https://www.postgresql.org/docs/current/wal-intro.html
  - Why: nice concrete example of durable-write sequencing.

### Enough for today when you understand

- the difference between API semantics and storage layout
- why a KV store still needs a recovery story
- what “single-node” does and does not simplify

## What to build

Design a single-node key-value service with Get, Put, Delete, persistence, and crash recovery.

## What a strong solution should show

A good solution describes the write path, storage/index layout, compaction or cleanup strategy, and restart behavior.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier

## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 06 start`
- `dist-sys 06 new`
- `dist-sys 06 list`
- `dist-sys 06 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under the exercise's default attempt store in `~/.dist-sys/<exercise-folder>/submissions/`.
