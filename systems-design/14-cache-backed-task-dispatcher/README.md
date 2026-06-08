# 14. Cache-backed task dispatcher

- **Tier:** `applied`
- **Exercise type:** `open_ended_design`
- **Primary phases:** `scalability`, `messaging`, `reliability`
- **Prerequisites:** [`12. Durable job queue`](../12-durable-job-queue/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `applied`-level systems reasoning.

## What to learn

- fast-path vs durable-path trade-offs
- cache invalidation under work dispatch
- backpressure and degraded modes

## Prep reading

### Required (about 40–55 minutes total)
- *Designing Data-Intensive Applications* — Chapter 11, **Stream Processing**
  - Why: useful for separating durable state from fast-path dispatch.
- AWS Builders’ Library — **Timeouts, retries, and backoff with jitter**: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
  - Why: practical background for dispatch, retries, and failure behavior.

### Optional (10–15 minutes)
- Google SRE book — **Handling Overload**: https://sre.google/sre-book/handling-overload/
  - Why: useful if you want to think harder about burst handling and backpressure.

### Enough for today when you understand
- why cached state should not silently replace durable truth
- how retries and stale cache entries can interact badly
- why degraded behavior should be designed intentionally


## What to build

Design a task-dispatching service that uses caching for speed but still preserves reliable work assignment.

## What a strong solution should show

A good solution states when cached state is authoritative, when it is advisory, and how stale cache entries are repaired.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier


## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 14 start`
- `dist-sys 14 new`
- `dist-sys 14 list`
- `dist-sys 14 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under [`./submissions/`](./submissions/).
