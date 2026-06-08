# 04. Single-process job scheduler

- **Tier:** `foundation`
- **Exercise type:** `focused_component_design`
- **Primary phases:** `single_machine`, `reliability`
- **Prerequisites:** None

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `foundation`-level systems reasoning.

## What to learn

- task state machines
- retry/backoff basics
- poison-job handling without distribution

## Prep reading

### Required (about 35–50 minutes total)

- _Designing Data-Intensive Applications_ — Chapter 1, **Reliable, Scalable, and Maintainable Applications**
  - Why: gives a good framing for local reliability, workload, and failure handling.
- Google SRE book — **Handling Overload**: https://sre.google/sre-book/handling-overload/
  - Why: helps you think about queues, saturation, and backpressure before distribution enters the picture.

### Optional (10–15 minutes)

- AWS Builders’ Library — **Using load shedding to avoid overload**: https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/
  - Why: practical companion to overload and bounded work.

### Enough for today when you understand

- why a scheduler needs a state machine for jobs
- why retries and poison jobs change the design
- why bounded concurrency matters even on one machine

## What to build

Design a local background job scheduler with delayed execution, retries, cancellation, and bounded worker concurrency.

## What a strong solution should show

A good solution defines job states, retry rules, fairness under one process, and what metadata must survive crashes.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier

## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 04 start`
- `dist-sys 04 new`
- `dist-sys 04 list`
- `dist-sys 04 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under [`./submissions/`](./submissions/).
