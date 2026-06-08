# 16. Workflow orchestration engine

- **Tier:** `applied`
- **Exercise type:** `focused_component_design`
- **Primary phases:** `messaging`, `reliability`
- **Prerequisites:** [`12. Durable job queue`](../12-durable-job-queue/README.md), [`13. MapReduce coordinator`](../13-mapreduce-coordinator/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `applied`-level systems reasoning.

## What to learn

- long-running state machines
- step retries/compensation
- workflow visibility and recovery

## Prep reading

### Required (about 40–55 minutes total)
- *Designing Data-Intensive Applications* — Chapter 11, **Stream Processing**
  - Why: strong background for stepwise, durable work execution.
- Martin Fowler — **Circuit Breaker**: https://martinfowler.com/bliki/CircuitBreaker.html
  - Why: useful as a small operational reading about failure control in multi-step systems.

### Optional (10–15 minutes)
- AWS Builders’ Library — **Timeouts, retries, and backoff with jitter**: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
  - Why: practical companion for step retries and failure handling.

### Enough for today when you understand
- why workflow state must be explicit
- why retries and compensation are design choices, not patch-ups
- why long-running work needs visibility


## What to build

Design a workflow engine that executes multi-step jobs with persisted state, retries, and compensation hooks.

## What a strong solution should show

A good solution defines workflow state, step idempotency expectations, and what happens after engine restarts.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier


## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 16 start`
- `dist-sys 16 new`
- `dist-sys 16 list`
- `dist-sys 16 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under [`./submissions/`](./submissions/).
