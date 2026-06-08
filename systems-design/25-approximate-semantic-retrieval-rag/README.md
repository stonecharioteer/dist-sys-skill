# 25. Approximate semantic retrieval / RAG retrieval platform

- **Tier:** `distributed`
- **Exercise type:** `open_ended_design`
- **Primary phases:** `storage`, `scalability`, `observability`, `large_scale_patterns`
- **Prerequisites:** [`15. Search index and document retrieval service`](../15-search-index-document-retrieval/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `distributed`-level systems reasoning.

## What to learn

- approximate retrieval trade-offs
- index freshness for embeddings
- latency/quality observability

## Prep reading

### Required (about 45–60 minutes total)
- *Designing Data-Intensive Applications* — Chapter 3, **Storage and Retrieval**
  - Why: still the right chapter for indexing and retrieval-path thinking.
- Google Research — **The Tail at Scale**: https://research.google/pubs/the-tail-at-scale/
  - Why: great reading for why retrieval latency distributions matter.

### Optional (10–15 minutes)
- OpenTelemetry docs — **Signals**: https://opentelemetry.io/docs/concepts/signals/
  - Why: useful if you want better operational vocabulary for retrieval observability.

### Enough for today when you understand
- why retrieval freshness and retrieval latency are both system properties
- why approximate retrieval needs observability, not just intuition
- why query fanout can dominate p95/p99 behavior


## What to build

Design a retrieval system for RAG-style workloads with ingestion, embedding/index refresh, filtering, and low-latency query serving.

## What a strong solution should show

A good solution separates ingestion from serving, addresses freshness lag, and defines how retrieval quality is measured operationally.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier


## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 25 start`
- `dist-sys 25 new`
- `dist-sys 25 list`
- `dist-sys 25 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under [`./submissions/`](./submissions/).
