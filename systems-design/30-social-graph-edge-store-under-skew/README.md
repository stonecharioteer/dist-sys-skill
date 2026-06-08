# 30. Social graph edge store under skew

- **Tier:** `production`
- **Exercise type:** `open_ended_design`
- **Primary phases:** `large_scale_patterns`, `storage`, `partitioning`
- **Prerequisites:** [`15. Search index and document retrieval service`](../15-search-index-document-retrieval/README.md), [`17. Partition-key selection for a multi-tenant event platform`](../17-partition-key-selection-multitenant-event-platform/README.md), [`18. Consistent hashing for a distributed cache cluster`](../18-consistent-hashing-distributed-cache/README.md), [`29. Multi-tenant feed fan-out`](../29-multi-tenant-feed-fan-out/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `production`-level systems reasoning.

## What to learn

- power-law data distributions
- range-scan costs
- hot-node mitigation

## Prep reading

### Required (about 45–60 minutes total)

- _Designing Data-Intensive Applications_ — Chapter 6, **Partitioning**
  - Why: strong base for skew and placement reasoning.
- Google Research — **Bigtable: A Distributed Storage System for Structured Data**: https://research.google/pubs/bigtable-a-distributed-storage-system-for-structured-data/
  - Why: useful for thinking about large structured stores under skewed access.
- Google Research — **The Tail at Scale**: https://research.google/pubs/the-tail-at-scale/
  - Why: hot nodes and range scans are tail-latency problems.

### Enough for today when you understand

- why average-degree reasoning hides the hard cases
- why partitioning must acknowledge power-law skew
- why scan behavior and hot-node behavior cannot be separated

## What to build

Design a graph edge store that supports point reads, range scans, and writes under highly skewed degree distributions.

## What a strong solution should show

A good solution explains partitioning for hot nodes, scan pagination, cache strategy, and tail-latency risks for high-degree entities.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier

## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 30 start`
- `dist-sys 30 new`
- `dist-sys 30 list`
- `dist-sys 30 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under the exercise's default attempt store in `~/.dist-sys/<exercise-folder>/submissions/`.
