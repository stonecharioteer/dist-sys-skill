# 29. Multi-tenant feed fan-out

- **Tier:** `production`
- **Exercise type:** `time_boxed_mock_interview`
- **Primary phases:** `large_scale_patterns`, `storage`, `messaging`
- **Prerequisites:** [`21. Scaling consumer groups for ordered event processing`](../21-scaling-consumer-groups-ordered-processing/README.md), [`24. Tenant-isolated durable job queue`](../24-tenant-isolated-durable-job-queue/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `production`-level systems reasoning.

## What to learn

- fanout-on-write vs fanout-on-read
- celebrity skew
- ranking and cache trade-offs in social-style feeds

## Prep reading

### Required (about 45–60 minutes total)

- _Designing Data-Intensive Applications_ — Chapter 11, **Stream Processing**
  - Why: good background for fanout pipelines and asynchronous serving.
- Google Research — **The Tail at Scale**: https://research.google/pubs/the-tail-at-scale/
  - Why: feed systems are dominated by skew and tail latency.

### Enough for today when you understand

- why fanout strategy is workload-dependent
- why celebrity skew changes everything
- why cache warmth and backfill behavior belong in the initial design

## What to build

Design a feed system for many tenants with uneven publisher popularity, freshness constraints, and bounded storage/cost budgets.

## What a strong solution should show

A good solution chooses a fan-out strategy, models hot publishers, and explains cache, ranking, and backfill behavior.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier

## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 29 start`
- `dist-sys 29 new`
- `dist-sys 29 list`
- `dist-sys 29 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under the exercise's default attempt store in `~/.dist-sys/<exercise-folder>/submissions/`.
