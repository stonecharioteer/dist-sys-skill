# 27. Conversation memory service

- **Tier:** `production`
- **Exercise type:** `focused_component_design`
- **Primary phases:** `storage`, `reliability`, `large_scale_patterns`
- **Prerequisites:** [`06. Single-node key-value store`](../06-single-node-kv-store/README.md), [`15. Search index and document retrieval service`](../15-search-index-document-retrieval/README.md), [`25. Approximate semantic retrieval / RAG retrieval platform`](../25-approximate-semantic-retrieval-rag/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `production`-level systems reasoning.

## What to learn

- short-term vs long-term memory boundaries
- summarization/truncation trade-offs
- privacy and replay concerns for conversational state

## Prep reading

### Required (about 40–55 minutes total)

- _Designing Data-Intensive Applications_ — Chapter 3, **Storage and Retrieval**
  - Why: helpful for state layout and retrieval-path thinking.
- _Designing Data-Intensive Applications_ — Chapter 4, **Encoding and Evolution**
  - Why: useful for evolving memory formats and summaries over time.

### Optional (10–15 minutes)

- OpenTelemetry docs — **Signals**: https://opentelemetry.io/docs/concepts/signals/
  - Why: good if you want to think ahead about memory quality and latency signals.

### Enough for today when you understand

- why memory state is not just raw storage
- why summaries are a lossy representation with operational consequences
- why retrieval path and retention policy both matter

## What to build

Design a memory service that stores conversation context, supports truncation or summarization, and serves low-latency context assembly for AI applications.

## What a strong solution should show

A good solution explains what raw state is stored, what is summarized, how summaries are refreshed, and how users can recover from bad memory state.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier

## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 27 start`
- `dist-sys 27 new`
- `dist-sys 27 list`
- `dist-sys 27 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under [`./submissions/`](./submissions/).
