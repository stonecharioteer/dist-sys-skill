# 22. Fault-tolerant key-value service

- **Tier:** `distributed`
- **Exercise type:** `open_ended_design`
- **Primary phases:** `replication_consistency`, `reliability`, `storage`
- **Prerequisites:** [`07. Linearizable key-value store with compare-and-set`](../07-linearizable-kv-cas/README.md), [`19. Read replicas and stale-read mitigation`](../19-read-replicas-stale-read-mitigation/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `distributed`-level systems reasoning.

## What to learn

- replicated-log thinking
- leader/follower safety
- availability vs durability trade-offs

## Prep reading

### Required (about 50–65 minutes total)

- _Designing Data-Intensive Applications_ — Chapter 5, **Replication**
  - Why: foundation for replicated data services.
- _Designing Data-Intensive Applications_ — Chapter 9, **Consistency and Consensus**
  - Why: necessary for thinking clearly about safety and failover.
- Raft site: https://raft.github.io/
  - Why: clean accessible introduction to replicated-log reasoning.

### Enough for today when you understand

- what a write acknowledgment means in a replicated service
- why failover changes correctness, not just availability
- why “replicated KV” is mostly a semantics problem

## What to build

Design a replicated key-value service that tolerates node failures while preserving stated consistency guarantees.

## What a strong solution should show

A good solution makes write acknowledgment rules, failover behavior, and replica catch-up explicit.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier

## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 22 start`
- `dist-sys 22 new`
- `dist-sys 22 list`
- `dist-sys 22 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under the exercise's default attempt store in `~/.dist-sys/<exercise-folder>/submissions/`.
