# 12. Durable job queue

- **Tier:** `applied`
- **Exercise type:** `open_ended_design`
- **Primary phases:** `messaging`, `reliability`
- **Prerequisites:** [`04. Single-process job scheduler`](../04-single-process-job-scheduler/README.md), [`05. Append-only log with crash recovery`](../05-append-only-log-crash-recovery/README.md), [`08. Lock / lease service`](../08-lock-lease-service/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `applied`-level systems reasoning.

## What to learn

- ack boundaries
- at-least-once delivery
- leases, retries, and DLQ behavior

## Prep reading

### Required (about 45–60 minutes total)

- _Designing Data-Intensive Applications_ — Chapter 11, **Stream Processing**
  - Why: strong background for thinking about durable work queues, replay, and consumers.
- Apache Kafka documentation: https://kafka.apache.org/documentation/
  - Why: familiarizes you with partitions, retention, consumers, and delivery semantics.

### Optional (10–15 minutes)

- Wikipedia — **Idempotence**: https://en.wikipedia.org/wiki/Idempotence
  - Why: useful framing for duplicate delivery and safe retries.

### Enough for today when you understand

- what an enqueue acknowledgment means
- why at-least-once delivery implies duplicates
- why retries and DLQs are part of the core design

## What to build

Design a durable queue with Enqueue, Lease, Ack, Nack, retries, and dead-letter handling.

## What a strong solution should show

A good solution defines what an enqueue acknowledgment means, how leases expire, and how duplicates are handled.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier

## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 12 start`
- `dist-sys 12 new`
- `dist-sys 12 list`
- `dist-sys 12 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under the exercise's default attempt store in `~/.dist-sys/<exercise-folder>/submissions/`.
