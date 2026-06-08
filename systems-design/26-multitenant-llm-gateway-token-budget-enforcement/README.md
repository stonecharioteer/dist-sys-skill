# 26. Multi-tenant LLM gateway with token budget enforcement

- **Tier:** `production`
- **Exercise type:** `open_ended_design`
- **Primary phases:** `partitioning`, `replication_consistency`, `reliability`, `observability`
- **Prerequisites:** [`23. Sharded rate limiter`](../23-sharded-rate-limiter/README.md), [`24. Tenant-isolated durable job queue`](../24-tenant-isolated-durable-job-queue/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `production`-level systems reasoning.

## What to learn

- token-based quota enforcement
- soft vs hard budget control
- usage metering with retries and streaming

## Prep reading

### Required (about 45–60 minutes total)

- AWS Builders’ Library — **Using load shedding to avoid overload**: https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/
  - Why: admission control is central to a token-budget gateway.
- OpenTelemetry docs — **Signals**: https://opentelemetry.io/docs/concepts/signals/
  - Why: budgeting and spend-control systems need strong observability.
- _Designing Data-Intensive Applications_ — Chapter 5, **Replication** or Chapter 6, **Partitioning**
  - Why: read the one you need most depending on whether you want to focus on accounting correctness or tenant sharding.

### Enough for today when you understand

- why request count is a poor proxy for LLM spend
- why accounting, routing, and quotas interact tightly
- why admission control and reconciliation are different stages

## What to build

Design an AI gateway that routes requests to model providers, meters token usage, enforces tenant budgets, and handles retries or provider failover.

## What a strong solution should show

A good solution defines admission checks, reconciliation of predicted vs actual token usage, and how duplicate billing is avoided.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier

## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 26 start`
- `dist-sys 26 new`
- `dist-sys 26 list`
- `dist-sys 26 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under [`./submissions/`](./submissions/).
