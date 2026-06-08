# 11. Load balancing and autoscaling for bursty traffic

- **Tier:** `applied`
- **Exercise type:** `capacity_planning`
- **Primary phases:** `scalability`, `reliability`
- **Prerequisites:** [`10. Refactor a stateful service into a stateless service`](../10-refactor-stateful-service-stateless/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `applied`-level systems reasoning.

## What to learn

- capacity headroom math
- burst absorption
- scaling signals and saturation metrics

## Prep reading

### Required (about 35–50 minutes total)
- Google SRE book — **Handling Overload**: https://sre.google/sre-book/handling-overload/
  - Why: directly useful for burst handling and headroom thinking.
- AWS Builders’ Library — **Using load shedding to avoid overload**: https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/
  - Why: concrete guidance on protecting a service under stress.

### Optional (10–15 minutes)
- AWS Builders’ Library — **Timeouts, retries, and backoff with jitter**: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
  - Why: complements scaling by showing how clients can amplify overload.

### Enough for today when you understand
- why average load is not enough for planning
- why headroom and reaction lag matter
- why autoscaling still needs overload behavior defined up front


## What to build

Design a load-balancing and autoscaling strategy for a service with predictable baseline load and sudden spikes.

## What a strong solution should show

A good solution quantifies headroom, scale-up lag, queueing or shedding behavior, and failure-safe defaults.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier


## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 11 start`
- `dist-sys 11 new`
- `dist-sys 11 list`
- `dist-sys 11 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under [`./submissions/`](./submissions/).
