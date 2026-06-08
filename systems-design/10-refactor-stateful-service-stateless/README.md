# 10. Refactor a stateful service into a stateless service

- **Tier:** `applied`
- **Exercise type:** `implementation_agnostic_architecture_diagram`
- **Primary phases:** `scalability`, `reliability`
- **Prerequisites:** [`06. Single-node key-value store`](../06-single-node-kv-store/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `applied`-level systems reasoning.

## What to learn

- compute/state separation
- horizontal scaling basics
- session and cache externalization

## Prep reading

### Required (about 35–50 minutes total)
- *Designing Data-Intensive Applications* — Chapter 1, **Reliable, Scalable, and Maintainable Applications**
  - Why: strong conceptual grounding for separating state from compute.
- AWS Well-Architected — **Reliability Pillar**: https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html
  - Why: practical framing for failure domains, recovery, and service shape.

### Optional (10–15 minutes)
- Google SRE book — **Handling Overload**: https://sre.google/sre-book/handling-overload/
  - Why: helps you see why statelessness matters under burst and failure.

### Enough for today when you understand
- why sticky state constrains horizontal scale
- what state must move out of process
- what new bottlenecks appear after externalizing state


## What to build

Take a stateful web service and redesign it so compute nodes can scale horizontally without sticky assumptions.

## What a strong solution should show

A good solution identifies what state must move, what consistency is needed, and what new failure modes appear.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier


## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 10 start`
- `dist-sys 10 new`
- `dist-sys 10 list`
- `dist-sys 10 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under [`./submissions/`](./submissions/).
