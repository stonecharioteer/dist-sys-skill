# 21. Scaling consumer groups for ordered event processing

- **Tier:** `distributed`
- **Exercise type:** `capacity_planning`
- **Primary phases:** `messaging`, `partitioning`
- **Prerequisites:** [`12. Durable job queue`](../12-durable-job-queue/README.md), [`17. Partition-key selection for a multi-tenant event platform`](../17-partition-key-selection-multitenant-event-platform/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `distributed`-level systems reasoning.

## What to learn

- ordering scope vs parallelism
- lag math
- rebalance and hot-partition effects

## Prep reading

### Required (about 40–55 minutes total)

- Apache Kafka documentation: https://kafka.apache.org/documentation/
  - Why: best short official source for partitions, ordering, and consumer groups.
- _Designing Data-Intensive Applications_ — Chapter 11, **Stream Processing**
  - Why: complements Kafka with stronger system-level reasoning.

### Enough for today when you understand

- why ordering scope limits parallelism
- why consumer lag is a first-class signal
- why rebalances are not free

## What to build

Plan how a consumer group can scale while preserving the required ordering boundary for a partitioned event stream.

## What a strong solution should show

A good solution quantifies partitions, consumer parallelism, lag budgets, and what happens during rebalances.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier

## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 21 start`
- `dist-sys 21 new`
- `dist-sys 21 list`
- `dist-sys 21 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under the exercise's default attempt store in `~/.dist-sys/<exercise-folder>/submissions/`.
