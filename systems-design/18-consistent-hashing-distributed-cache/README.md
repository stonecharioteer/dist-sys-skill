# 18. Consistent hashing for a distributed cache cluster

- **Tier:** `distributed`
- **Exercise type:** `focused_component_design`
- **Primary phases:** `partitioning`, `scalability`
- **Prerequisites:** [`02. LRU cache`](../02-lru-cache/README.md), [`10. Refactor a stateful service into a stateless service`](../10-refactor-stateful-service-stateless/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `distributed`-level systems reasoning.

## What to learn

- membership change handling
- rebalance cost
- cache key distribution under skew

## Prep reading

### Required (about 35–50 minutes total)
- *Designing Data-Intensive Applications* — Chapter 6, **Partitioning**
  - Why: gives the right background for distribution and movement cost.
- Wikipedia — **Consistent hashing**: https://en.wikipedia.org/wiki/Consistent_hashing
  - Why: quick and adequate introduction to the core placement idea.

### Enough for today when you understand
- why node membership changes are expensive without good placement strategy
- what consistent hashing is trying to minimize
- why skew and hot keys still matter even with elegant hashing


## What to build

Design a distributed cache placement strategy using consistent hashing or an alternative with comparable goals.

## What a strong solution should show

A good solution explains placement, virtual nodes or equivalents, and behavior during node joins/leaves.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier


## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 18 start`
- `dist-sys 18 new`
- `dist-sys 18 list`
- `dist-sys 18 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under [`./submissions/`](./submissions/).
