# Agent notes for 01. In-memory rate limiter

## Purpose

This file describes what future agent-based tooling should expect from a learner submission and how to prepare language-agnostic scaffolding for evaluation.

This is a **foundation-tier, single-process** exercise. The goal is not distributed coordination. The goal is precise local reasoning.

The intended solution target is an **in-process rate-limiting component** used by application code, such as a function, middleware layer, or library module. It is not a separate HTTP service.

## Expected submission shape

A strong learner submission should usually include:

- explicit assumptions
- a chosen rate-limiting algorithm
- exact allow/deny semantics
- per-key state description
- cleanup or eviction strategy
- complexity discussion
- restart behavior
- basic observability signals

Accept multiple valid algorithms, including:

- fixed window
- sliding window log
- sliding window counter
- token bucket
- leaky bucket equivalent

Do not require one canonical answer.

## What to look for in the design

### Correctness expectations

The learner should make clear:

- when a request is considered allowed
- when a request is considered denied
- how concurrent requests to the same key are handled in one process
- whether the limiter is exact or approximate near boundaries
- what happens after process restart

### Trade-off expectations

The learner should compare at least one chosen approach against one rejected alternative using factors like:

- implementation complexity
- memory cost per key
- burst handling
- fairness near boundaries
- cleanup cost
- operational simplicity

### Operational expectations

The learner should mention a minimum observability set such as:

- allow count
- deny count
- per-key or sampled hot-key concentration
- state size or memory growth
- cleanup activity
- limiter latency

## Out-of-scope items

Do not expect or require:

- multi-node consistency
- distributed quotas
- external durable stores
- provider-specific APIs
- full production hardening beyond the local-process scope

These can be mentioned as future evolution, but they are not required for correctness here.

## Evaluation dimensions

Use these dimensions for future rubric-based scoring:

- **Correctness**: are the semantics precise and self-consistent?
- **Trade-offs**: is the algorithm choice justified for the stated workload?
- **Capacity reasoning**: is memory and update cost discussed credibly?
- **Reliability**: is restart behavior explicit and acceptable for this scope?
- **Communication**: is the design easy to follow?

Suggested weight split for future scaffolding:

- Correctness: 35
- Trade-offs: 25
- Capacity reasoning: 20
- Reliability: 10
- Communication: 10

## Future scaffolding plan

When a language track is chosen later, build scaffolding around behavioral traces and workload fixtures rather than implementation-specific hooks.

### Recommended fixture categories

- steady traffic for many low-volume keys
- burst traffic for a small number of hot keys
- boundary traffic near limit edges
- idle-key churn to test cleanup
- restart scenarios

### Recommended future checks

1. **Decision trace replay**
   - feed request timestamps and keys
   - compare allow/deny output with the learner's declared algorithm semantics

2. **Boundary-condition checks**
   - validate behavior at the edge of windows or token refill moments
   - detect off-by-one ambiguity

3. **Memory-growth checks**
   - simulate many one-off keys and many idle keys
   - verify the design discusses cleanup or bounded state

4. **Hot-key stress checks**
   - simulate extreme skew on one key
   - inspect whether the design identifies contention and update hot paths

5. **Restart checks**
   - verify the design states what is lost on restart
   - ensure the claimed semantics remain internally consistent after reset

## Future scaffold shape

If implementation tracks are added later, a good shape is:

- `fixtures/traffic/`
  - steady.yaml
  - bursty.yaml
  - edge-boundary.yaml
  - idle-churn.yaml
- `cases/`
  - happy-path.md
  - hot-key.md
  - cleanup.md
  - restart.md
- `oracle/`
  - semantics.md
  - scoring.md
  - trace-format.md

## Guardrails for future agent work

- Preserve language agnosticism until a language track is explicitly chosen.
- Do not over-constrain the implementation if multiple algorithms are allowed.
- Prefer validating declared semantics over forcing a hidden “correct” algorithm.
- Keep the exercise small and local; do not accidentally upgrade it into a distributed rate-limiter problem.

## Session control contract

This exercise participates in the curriculum-wide session workflow in [`../WORKFLOW.md`](../WORKFLOW.md).

The controlling commands for this exercise are:

- `dist-sys 01 start`
- `dist-sys 01 new`
- `dist-sys 01 list`
- `dist-sys 01 review`

After `start` or `new`, the agent should switch into natural-chat interview mode and keep appending learner work to the active attempt folder under `submissions/`.

Expected attempt files:

- `submission.md`
- `review.md`
- `metadata.yaml`
- `assets/` for exported diagrams such as PNG or SVG from Excalidraw
