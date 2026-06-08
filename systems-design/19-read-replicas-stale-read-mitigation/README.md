# 19. Read replicas and stale-read mitigation

- **Tier:** `distributed`
- **Exercise type:** `fault_injection`
- **Primary phases:** `replication_consistency`, `reliability`
- **Prerequisites:** [`06. Single-node key-value store`](../06-single-node-kv-store/README.md), [`07. Linearizable key-value store with compare-and-set`](../07-linearizable-kv-cas/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `distributed`-level systems reasoning.

## What to learn

- replication lag effects
- read-your-writes mitigation
- failover trade-offs

## Prep reading

### Required (about 45–60 minutes total)
- *Designing Data-Intensive Applications* — Chapter 5, **Replication**
  - Why: this is the chapter you want for leader/follower and lag thinking.
- PostgreSQL documentation — **Hot Standby / Streaming Replication**: https://www.postgresql.org/docs/current/warm-standby.html
  - Why: practical source for read replicas and failover trade-offs.

### Enough for today when you understand
- why replicas help reads but complicate semantics
- what stale reads mean operationally
- why failover and lag are part of the same discussion


## What to build

Design a read-scaling strategy with replicas while handling stale reads and failover explicitly.

## What a strong solution should show

A good solution states acceptable staleness, routing rules, and how clients recover from lag or failover.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier


## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 19 start`
- `dist-sys 19 new`
- `dist-sys 19 list`
- `dist-sys 19 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under [`./submissions/`](./submissions/).
