# 31. Reconfigurable sharded key-value service

- **Tier:** `production`
- **Exercise type:** `time_boxed_mock_interview`
- **Primary phases:** `partitioning`, `replication_consistency`, `reliability`, `observability`
- **Prerequisites:** [`22. Fault-tolerant key-value service`](../22-fault-tolerant-kv-service/README.md), [`23. Sharded rate limiter`](../23-sharded-rate-limiter/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `production`-level systems reasoning.

## What to learn

- epoch-based ownership
- safe shard migration
- availability during reconfiguration

## Prep reading

### Required (about 50–65 minutes total)
- *Designing Data-Intensive Applications* — Chapter 6, **Partitioning**
  - Why: required for shard movement and ownership reasoning.
- *Designing Data-Intensive Applications* — Chapter 9, **Consistency and Consensus**
  - Why: needed for safe reconfiguration semantics.
- Raft site: https://raft.github.io/
  - Why: good reinforcement for replicated state and epoch thinking.

### Enough for today when you understand
- why ownership must be explicit during migration
- why configuration state and data state are separate concerns
- why reconfiguration is a correctness problem, not just an ops task


## What to build

Design a sharded replicated key-value system that can move shards safely while reads and writes continue.

## What a strong solution should show

A good solution defines configuration epochs, migration steps, and how double-serving is prevented during controller or network failure.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier


## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 31 start`
- `dist-sys 31 new`
- `dist-sys 31 list`
- `dist-sys 31 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under [`./submissions/`](./submissions/).
