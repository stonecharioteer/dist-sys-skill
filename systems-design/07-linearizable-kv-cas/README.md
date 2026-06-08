# 07. Linearizable key-value store with compare-and-set

- **Tier:** `foundation`
- **Exercise type:** `focused_component_design`
- **Primary phases:** `single_machine`, `reliability`
- **Prerequisites:** [`06. Single-node key-value store`](../06-single-node-kv-store/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `foundation`-level systems reasoning.

## What to learn

- linearizability as a behavior contract
- versioning/CAS semantics
- retry safety on a single node

## Prep reading

### Required (about 45–60 minutes total)

- _Designing Data-Intensive Applications_ — Chapter 9, **Consistency and Consensus**
  - Why: this is the cleanest way to ground yourself in linearizability and compare-and-set semantics.
- Raft site: https://raft.github.io/
  - Why: useful for building an intuition that correctness comes from explicit state transitions and guarantees.

### Optional (10–15 minutes)

- PostgreSQL documentation — **Introduction to MVCC**: https://www.postgresql.org/docs/current/mvcc-intro.html
  - Why: helps contrast local visibility semantics with stronger single-copy reasoning.

### Enough for today when you understand

- what linearizability is trying to guarantee
- why CAS is more than “read, then write”
- why retry behavior changes correctness arguments

## What to build

Extend a single-node key-value service with CompareAndSet and clearly defined linearizable semantics.

## What a strong solution should show

A good solution makes concurrent operation ordering and failed CAS behavior explicit.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier

## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 07 start`
- `dist-sys 07 new`
- `dist-sys 07 list`
- `dist-sys 07 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under the exercise's default attempt store in `~/.dist-sys/<exercise-folder>/submissions/`.
