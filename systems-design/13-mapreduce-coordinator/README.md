# 13. MapReduce coordinator

- **Tier:** `applied`
- **Exercise type:** `whiteboard_sketch`
- **Primary phases:** `messaging`, `reliability`, `scalability`
- **Prerequisites:** [`12. Durable job queue`](../12-durable-job-queue/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `applied`-level systems reasoning.

## What to learn

- task assignment and reassignment
- worker timeout handling
- phase transitions under failure

## Prep reading

### Required (about 40–55 minutes total)

- _Designing Data-Intensive Applications_ — Chapter 10, **Batch Processing**
  - Why: gives the right mental model for staged work and coordinator responsibilities.
- Google Research — **MapReduce: Simplified Data Processing on Large Clusters**: https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/
  - Why: canonical reference for the problem shape you are modeling.

### Enough for today when you understand

- why coordinators assign and reassign work
- why task completion needs explicit bookkeeping
- what worker failure changes in a staged job system

## What to build

Design a coordinator that hands out map and reduce tasks, tracks progress, and recovers from worker loss.

## What a strong solution should show

A good solution defines assignment, timeout, completion, and duplicate-work handling for each phase.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier

## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 13 start`
- `dist-sys 13 new`
- `dist-sys 13 list`
- `dist-sys 13 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under the exercise's default attempt store in `~/.dist-sys/<exercise-folder>/submissions/`.
