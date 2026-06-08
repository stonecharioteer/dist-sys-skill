# 15. Search index and document retrieval service

- **Tier:** `applied`
- **Exercise type:** `focused_component_design`
- **Primary phases:** `storage`, `scalability`
- **Prerequisites:** [`03. Database index design for a read-heavy workload`](../03-database-index-design/README.md), [`10. Refactor a stateful service into a stateless service`](../10-refactor-stateful-service-stateless/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `applied`-level systems reasoning.

## What to learn

- index/build/query separation
- freshness vs indexing cost
- ranking and pagination basics

## Prep reading

### Required (about 45–60 minutes total)
- *Designing Data-Intensive Applications* — Chapter 3, **Storage and Retrieval**
  - Why: strongest chapter for local indexing and query access paths.
- PostgreSQL documentation — **Introduction to Indexes**: https://www.postgresql.org/docs/current/indexes-intro.html
  - Why: concise operational intuition for index-backed retrieval.
- PostgreSQL documentation — **Index Types**: https://www.postgresql.org/docs/current/indexes-types.html
  - Why: useful reminder that index choice depends on query shape.

### Enough for today when you understand
- why indexing and serving are separate concerns
- why freshness lag is part of retrieval design
- why pagination and ranking change access-path needs


## What to build

Design a document retrieval service with indexing, querying, pagination, and bounded freshness lag.

## What a strong solution should show

A good solution explains ingestion, indexing, search query flow, and how updates become visible.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier


## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 15 start`
- `dist-sys 15 new`
- `dist-sys 15 list`
- `dist-sys 15 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under [`./submissions/`](./submissions/).
