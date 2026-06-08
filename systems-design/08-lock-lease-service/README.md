# 08. Lock / lease service

- **Tier:** `applied`
- **Exercise type:** `focused_component_design`
- **Primary phases:** `single_machine`, `reliability`
- **Prerequisites:** [`07. Linearizable key-value store with compare-and-set`](../07-linearizable-kv-cas/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `applied`-level systems reasoning.

## What to learn

- ownership semantics
- lease expiry vs safe release
- stale client handling

## Prep reading

### Required (about 40–55 minutes total)

- _Designing Data-Intensive Applications_ — Chapter 8, **The Trouble with Distributed Systems**
  - Why: even a simple lease design is shaped by time, pauses, and failure assumptions.
- Raft site: https://raft.github.io/
  - Why: good practice in being explicit about ownership and state transitions.

### Optional (10–15 minutes)

- Wikipedia — **Rate limiting**: https://en.wikipedia.org/wiki/Rate_limiting
  - Why: useful only as a reminder that admission/ownership rules need precise semantics.

### Enough for today when you understand

- why a lease is not just a boolean lock
- why expiry and stale release behavior must be explicit
- why failure assumptions matter even in a simple service

## What to build

Design a lock or lease service with Acquire, Renew, and Release, including retry safety and stale-owner protection.

## What a strong solution should show

A good solution defines lock ownership, expiration semantics, and how stale releases are rejected.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier

## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 08 start`
- `dist-sys 08 new`
- `dist-sys 08 list`
- `dist-sys 08 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under [`./submissions/`](./submissions/).
