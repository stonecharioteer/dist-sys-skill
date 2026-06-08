# 02. LRU cache

- **Tier:** `foundation`
- **Exercise type:** `focused_component_design`
- **Primary phases:** `single_machine`, `storage`
- **Prerequisites:** None

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `foundation`-level systems reasoning.

## What to learn

- eviction policy design
- read/write path cost
- memory accounting and hit-rate trade-offs

## Prep reading

### Required (about 35–50 minutes total)

- _Designing Data-Intensive Applications_ — Chapter 3, **Storage and Retrieval**
  - Why: frames local data-structure trade-offs and lookup-path costs.
- Wikipedia — **Cache replacement policies**: https://en.wikipedia.org/wiki/Cache_replacement_policies
  - Why: gives the shortest reliable overview of LRU and related eviction strategies.

### Optional (10–15 minutes)

- Redis documentation — **Key eviction**: https://redis.io/docs/latest/develop/reference/eviction/
  - Why: helps you see how eviction policy shows up in a real cache system.

### Enough for today when you understand

- why LRU needs both fast lookup and fast recency updates
- what eviction policy means operationally
- why a cache can be locally correct yet still ineffective if hit rates are poor

## What to build

Design a bounded in-memory cache with LRU eviction, optional TTLs, and metrics for hit rate and churn.

## What a strong solution should show

A good solution explains data structures, eviction complexity, stale-entry handling, and behavior under skewed access.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier

## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 02 start`
- `dist-sys 02 new`
- `dist-sys 02 list`
- `dist-sys 02 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under [`./submissions/`](./submissions/).
