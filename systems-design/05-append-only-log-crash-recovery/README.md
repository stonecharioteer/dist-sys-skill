# 05. Append-only log with crash recovery

- **Tier:** `foundation`
- **Exercise type:** `fault_injection`
- **Primary phases:** `single_machine`, `storage`, `reliability`
- **Prerequisites:** [`04. Single-process job scheduler`](../04-single-process-job-scheduler/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `foundation`-level systems reasoning.

## What to learn

- durability boundaries
- fsync/ack semantics
- replay and corruption handling

## Prep reading

### Required (about 40–55 minutes total)

- _Designing Data-Intensive Applications_ — Chapter 3, **Storage and Retrieval**
  - Why: useful background for append-only structures and recovery trade-offs.
- PostgreSQL documentation — **Write-Ahead Logging (WAL)**: https://www.postgresql.org/docs/current/wal-intro.html
  - Why: concrete and trustworthy example of durable append-first thinking.

### Optional (10–15 minutes)

- PostgreSQL documentation — **Introduction to MVCC**: https://www.postgresql.org/docs/current/mvcc-intro.html
  - Why: helpful if you want more intuition about durable state and visibility.

### Enough for today when you understand

- what an acknowledgment means for durability
- why partial writes and tail corruption matter
- why replay logic is part of the design, not an afterthought

## What to build

Design a local append-only log and replay mechanism that can recover state after process or machine crashes.

## What a strong solution should show

A good solution is explicit about when writes are acknowledged, how partial records are handled, and how replay rebuilds state.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier

## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 05 start`
- `dist-sys 05 new`
- `dist-sys 05 list`
- `dist-sys 05 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under the exercise's default attempt store in `~/.dist-sys/<exercise-folder>/submissions/`.
