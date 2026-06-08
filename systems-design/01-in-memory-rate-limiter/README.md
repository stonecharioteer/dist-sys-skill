# 01. In-memory rate limiter

- **Tier:** `foundation`
- **Exercise type:** `focused_component_design`
- **Primary phases:** `single_machine`, `scalability`
- **Prerequisites:** None
- **Suggested timebox:** 25–35 minutes

## Why this exercise

This is the first exercise in the curriculum because it is small, concrete, and still rich in systems trade-offs.

You can solve it without distributed systems machinery, but it forces you to reason about:

- where state lives
- how requests are checked quickly
- what happens under bursts and hot keys
- how memory grows over time
- which guarantees are exact versus approximate

## What to learn

By the end of this exercise, you should be able to:

- compare fixed-window, sliding-window, token-bucket, and leaky-bucket style designs
- explain how an in-memory service trades simplicity for restart loss and process-local state
- reason about contention, hot keys, cleanup, and bounded memory growth
- define clear request-time semantics for allow/deny decisions
- identify the observability signals needed to debug a limiter in production-like conditions

## Scenario

You are designing a rate limiter for a single API process that serves a public HTTP API.

The process receives requests from many users, but a small number of API keys can become very hot during bursts. The limiter should decide whether a request is allowed before the expensive application work runs.

For this exercise, the rate limiter should be treated as an **in-process component** of the API service, not as a separate network service.

That means the core thing you are designing is the local decision mechanism, for example something conceptually like:

- a function
- a middleware/interceptor
- or a library component called by request-handling code

You may describe the HTTP response behavior of the API when a request is denied, but you do **not** need to design a separate HTTP endpoint for the rate limiter itself.

This is intentionally a **single-process, in-memory** design exercise. Do not distribute the limiter across multiple nodes. Do not introduce Redis, Kafka, or a database unless you are explicitly describing them as future evolution paths rather than part of the solution.

## Prep reading

### Required (about 45–60 minutes total)

- _Designing Data-Intensive Applications_ — Chapter 3, **Storage and Retrieval**
  - Why: gives you the right local-systems mental model for in-memory structures, logs, and performance trade-offs.
- Wikipedia — **Rate limiting**: https://en.wikipedia.org/wiki/Rate_limiting
  - Why: quick orientation to the problem space and common policy shapes.
- Wikipedia — **Token bucket**: https://en.wikipedia.org/wiki/Token_bucket
  - Why: useful contrast against the simpler first design you might choose here.

### Optional (10–15 minutes)

- AWS Builders’ Library — **Using load shedding to avoid overload**: https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/
  - Why: connects local admission control to real overload handling.

### Enough for today when you understand

- why a limiter is an admission-control component
- the difference between a simple windowed design and token-bucket-style reasoning
- why this exercise stays single-process and in-memory

## What to build

Design a single-process, in-memory rate-limiting component with:

- per-key limits
- clear refill or window semantics
- bounded memory usage
- predictable behavior under hot keys and bursts
- basic operational visibility

You may choose the algorithm, but you must justify it.

## Functional requirements

Your design must support:

1. Checking whether a request for a given key should be allowed or denied.
2. Returning enough information to the calling application code to explain the decision.
3. Maintaining independent limits per key.
4. Handling idle keys without unbounded state growth.
5. Supporting at least one configurable limit policy, such as:
   - 100 requests per minute per key
   - or an equivalent token/refill style policy.

## Input constraints

Use these as the default assumptions unless you state otherwise:

- active API keys at once: **up to 100,000**
- total request rate: **up to 20,000 requests/second**
- hot-key skew: **top 1% of keys can produce 30% of traffic**
- request payload size is irrelevant to limiting decisions
- deployment model: **one process on one machine**
- memory budget for limiter state: **512 MB**

## Non-functional requirements

Your design should aim for:

- decision latency added by the limiter: **p95 < 2 ms**
- deterministic semantics for a single process
- no unbounded in-memory growth from stale keys
- graceful handling of bursts without pathological CPU spikes
- restart behavior that is explicitly documented

## Required decisions

Your answer must make these choices explicit:

1. **Algorithm choice**
   - fixed window?
   - sliding window?
   - token bucket?
   - another design?

2. **Per-key state layout**
   - what is stored for each key?
   - how large is it?
   - how is it updated?

3. **Cleanup / eviction policy**
   - how do old keys leave memory?
   - what is the cost of cleanup?

4. **Hot-key behavior**
   - what happens when one key becomes very hot?
   - where does contention appear?

5. **Restart semantics**
   - what happens if the process restarts?
   - do counters reset?
   - is that acceptable for this exercise?

## Deliverables

Produce:

- a short list of assumptions
- a component or data-structure sketch
- the request decision path
- the per-key state model
- the cleanup strategy
- a short trade-off comparison against at least one rejected algorithm
- a brief observability plan

## What a strong solution should show

A strong solution will:

- pick an algorithm and defend it against the workload
- describe exact allow/deny semantics
- explain memory behavior for active and idle keys
- identify hot-key contention points
- discuss complexity of reads, writes, and cleanup
- state clearly what a restart does to limiter correctness
- define useful metrics such as allow rate, deny rate, hot-key concentration, and memory growth

## Common failure modes

Watch out for these:

- naming an algorithm without explaining its semantics
- ignoring cleanup and stale-key memory growth
- assuming uniform traffic instead of bursty/hot-key traffic
- claiming exact fairness without describing the mechanics
- hand-waving away process restart behavior
- giving a distributed answer to a single-process exercise

## Hints

### Hint 1

Think first about what data must be updated on every request for one key.

### Hint 2

If two algorithms both work, compare them on memory cost, burst smoothing, and implementation complexity.

### Hint 3

The best first answer is usually not the most sophisticated one; it is the one whose semantics and costs are easiest to explain clearly.

## How to use this exercise

Try answering in this order:

1. state assumptions
2. choose an algorithm
3. define request-time semantics
4. show per-key state and cleanup
5. discuss hot keys, complexity, and observability

If you later implement this in a language, keep the implementation aligned with the behavior contract you designed here.

## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 01 start`
- `dist-sys 01 new`
- `dist-sys 01 list`
- `dist-sys 01 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under [`./submissions/`](./submissions/).
