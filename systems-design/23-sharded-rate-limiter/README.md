# 23. Sharded rate limiter

- **Tier:** `distributed`
- **Exercise type:** `whiteboard_sketch`
- **Primary phases:** `partitioning`, `replication_consistency`, `reliability`
- **Prerequisites:** [`01. In-memory rate limiter`](../01-in-memory-rate-limiter/README.md), [`17. Partition-key selection for a multi-tenant event platform`](../17-partition-key-selection-multitenant-event-platform/README.md), [`18. Consistent hashing for a distributed cache cluster`](../18-consistent-hashing-distributed-cache/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `distributed`-level systems reasoning.

## What to learn

- global vs local quotas
- hot-key mitigation
- strictness vs latency trade-offs

## Prep reading

### Required (about 40–55 minutes total)

- _Designing Data-Intensive Applications_ — Chapter 6, **Partitioning**
  - Why: required for hot-key and placement reasoning.
- Wikipedia — **Rate limiting**: https://en.wikipedia.org/wiki/Rate_limiting
  - Why: quick reminder of the policy problem.
- Wikipedia — **Consistent hashing**: https://en.wikipedia.org/wiki/Consistent_hashing
  - Why: useful for sharding intuition.

### Enough for today when you understand

- why global quotas are harder than local ones
- why hot keys dominate distributed limiter design
- why exactness and latency often pull in opposite directions

## What to build

Design a rate-limiting service that scales across shards and remains fair under hot tenants or keys.

## What a strong solution should show

A good solution defines where counters live, how strict the limits are, and what happens during partial outages.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier

## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 23 start`
- `dist-sys 23 new`
- `dist-sys 23 list`
- `dist-sys 23 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under [`./submissions/`](./submissions/).
