# 28. Agent workflow orchestrator

- **Tier:** `production`
- **Exercise type:** `open_ended_design`
- **Primary phases:** `messaging`, `reliability`, `observability`, `large_scale_patterns`
- **Prerequisites:** [`16. Workflow orchestration engine`](../16-workflow-orchestration-engine/README.md), [`20. Idempotent webhook ingestion and processing pipeline`](../20-idempotent-webhook-ingestion/README.md), [`26. Multi-tenant LLM gateway with token budget enforcement`](../26-multitenant-llm-gateway-token-budget-enforcement/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `production`-level systems reasoning.

## What to learn

- dynamic multi-step execution
- tool-call retries and compensations
- state recovery for long-running agent tasks

## Prep reading

### Required (about 45–60 minutes total)
- *Designing Data-Intensive Applications* — Chapter 11, **Stream Processing**
  - Why: strong foundation for durable step execution and eventful workflows.
- AWS Builders’ Library — **Timeouts, retries, and backoff with jitter**: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
  - Why: excellent practical reading for tool-call retries and failure amplification.

### Optional (10–15 minutes)
- OpenTelemetry docs — **Signals**: https://opentelemetry.io/docs/concepts/signals/
  - Why: useful if you want better trace vocabulary for multi-step agent runs.

### Enough for today when you understand
- why an orchestrator needs explicit durable state
- why retries and branching can amplify work unexpectedly
- why traceability is part of correctness for long-running workflows


## What to build

Design an orchestrator for agent-style workflows that can branch, call tools, recover from partial failure, and expose execution traces.

## What a strong solution should show

A good solution defines workflow state, tool isolation, retry/idempotency boundaries, and operator visibility into stuck or looping agents.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier


## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 28 start`
- `dist-sys 28 new`
- `dist-sys 28 list`
- `dist-sys 28 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under [`./submissions/`](./submissions/).
