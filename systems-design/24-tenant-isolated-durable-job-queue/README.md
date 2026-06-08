# 24. Tenant-isolated durable job queue

- **Tier:** `distributed`
- **Exercise type:** `open_ended_design`
- **Primary phases:** `messaging`, `partitioning`, `reliability`
- **Prerequisites:** [`12. Durable job queue`](../12-durable-job-queue/README.md), [`17. Partition-key selection for a multi-tenant event platform`](../17-partition-key-selection-multitenant-event-platform/README.md), [`21. Scaling consumer groups for ordered event processing`](../21-scaling-consumer-groups-ordered-processing/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `distributed`-level systems reasoning.

## What to learn

- multi-tenant fairness
- virtual sharding
- burst isolation under durable delivery

## Prep reading

### Required (about 45–60 minutes total)
- Apache Kafka documentation: https://kafka.apache.org/documentation/
  - Why: useful for partitions, consumers, and durable delivery mental models.
- AWS Builders’ Library — **Workload isolation using shuffle sharding**: https://aws.amazon.com/builders-library/workload-isolation-using-shuffle-sharding/
  - Why: one of the best practical readings for tenant isolation under burst.

### Optional (10–15 minutes)
- AWS Builders’ Library — **Using load shedding to avoid overload**: https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/
  - Why: complements fairness with overload behavior.

### Enough for today when you understand
- why durable delivery and tenant fairness pull in different directions
- why hot tenants can bury shared infrastructure
- why isolation strategy is part of the queue design itself


## What to build

Design a durable queue that isolates bursty tenants without losing acknowledged jobs or burying smaller tenants.

## What a strong solution should show

A good solution defines tenant placement, fairness policy, delivery semantics, and observability for lag and spillover.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier


## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 24 start`
- `dist-sys 24 new`
- `dist-sys 24 list`
- `dist-sys 24 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under [`./submissions/`](./submissions/).
