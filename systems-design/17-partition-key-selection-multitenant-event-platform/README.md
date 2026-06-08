# 17. Partition-key selection for a multi-tenant event platform

- **Tier:** `distributed`
- **Exercise type:** `tradeoff_analysis`
- **Primary phases:** `partitioning`, `messaging`
- **Prerequisites:** [`12. Durable job queue`](../12-durable-job-queue/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `distributed`-level systems reasoning.

## What to learn

- hash vs range partitioning
- tenant isolation under skew
- rebalance cost awareness

## Prep reading

### Required (about 45–60 minutes total)
- *Designing Data-Intensive Applications* — Chapter 6, **Partitioning**
  - Why: this is the chapter for partition-key reasoning, skew, and movement cost.
- PostgreSQL documentation — **Table Partitioning**: https://www.postgresql.org/docs/current/ddl-partitioning.html
  - Why: practical complement to abstract partitioning trade-offs.

### Enough for today when you understand
- why partition keys encode trade-offs, not just hashing choices
- why skew matters as much as average distribution
- why rebalancing cost belongs in the first design, not later


## What to build

Choose and justify a partitioning strategy for a multi-tenant event pipeline with hotspot risk and ordering needs.

## What a strong solution should show

A good solution compares keys, models skew, and explains migration/rebalancing consequences.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier


## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 17 start`
- `dist-sys 17 new`
- `dist-sys 17 list`
- `dist-sys 17 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under [`./submissions/`](./submissions/).
