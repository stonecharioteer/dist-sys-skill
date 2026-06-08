# 20. Idempotent webhook ingestion and processing pipeline

- **Tier:** `distributed`
- **Exercise type:** `open_ended_design`
- **Primary phases:** `messaging`, `reliability`, `observability`
- **Prerequisites:** [`12. Durable job queue`](../12-durable-job-queue/README.md), [`19. Read replicas and stale-read mitigation`](../19-read-replicas-stale-read-mitigation/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `distributed`-level systems reasoning.

## What to learn

- ingress ack boundaries
- deduplication under retries
- replay and operator tooling

## Prep reading

### Required (about 45–60 minutes total)

- _Designing Data-Intensive Applications_ — Chapter 11, **Stream Processing**
  - Why: helpful for ingestion, replay, and downstream processing.
- Wikipedia — **Idempotence**: https://en.wikipedia.org/wiki/Idempotence
  - Why: the shortest useful reading for duplicate delivery and safe replay.
- AWS Builders’ Library — **Timeouts, retries, and backoff with jitter**: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
  - Why: practical grounding for duplicate and delayed delivery behavior.

### Enough for today when you understand

- why inbound acknowledgment boundaries matter
- why dedupe and replay are first-class design concerns
- why retry behavior can create duplicate side effects

## What to build

Design a webhook ingestion pipeline that verifies authenticity, persists events, deduplicates retries, and processes downstream actions asynchronously.

## What a strong solution should show

A good solution is explicit about when it acknowledges receipt, how it deduplicates, and how replay avoids duplicate side effects.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier

## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 20 start`
- `dist-sys 20 new`
- `dist-sys 20 list`
- `dist-sys 20 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under [`./submissions/`](./submissions/).
