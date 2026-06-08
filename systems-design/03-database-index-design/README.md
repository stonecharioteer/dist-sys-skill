# 03. Database index design for a read-heavy workload

- **Tier:** `foundation`
- **Exercise type:** `focused_component_design`
- **Primary phases:** `single_machine`, `storage`
- **Prerequisites:** None

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `foundation`-level systems reasoning.

## What to learn

- query-pattern-first schema thinking
- read optimization vs write amplification
- how indexes shape local performance

## Prep reading

### Required (about 45–60 minutes total)

- _Designing Data-Intensive Applications_ — Chapter 3, **Storage and Retrieval**
  - Why: introduces index-driven thinking and read/write trade-offs.
- PostgreSQL documentation — **Introduction to Indexes**: https://www.postgresql.org/docs/current/indexes-intro.html
  - Why: short, concrete explanation of what indexes are for.
- PostgreSQL documentation — **Index Types**: https://www.postgresql.org/docs/current/indexes-types.html
  - Why: useful catalog of common index shapes and when they help.

### Optional (10–15 minutes)

- Cockroach Labs blog — **SQL performance best practices**: https://www.cockroachlabs.com/blog/sql-performance-best-practices/
  - Why: good practical intuition about query shape and index impact.

### Enough for today when you understand

- why you index query patterns, not tables in the abstract
- why extra indexes speed reads but cost writes and storage
- that “index everything” is usually the wrong answer

## What to build

Design indexes and access paths for a relational-style workload with a few dominant queries and a moderate write rate.

## What a strong solution should show

A good solution ties each index to query shapes, discusses update cost, and avoids indexing everything blindly.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier

## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 03 start`
- `dist-sys 03 new`
- `dist-sys 03 list`
- `dist-sys 03 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under [`./submissions/`](./submissions/).
