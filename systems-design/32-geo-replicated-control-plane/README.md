# 32. Geo-replicated control plane

- **Tier:** `production`
- **Exercise type:** `time_boxed_mock_interview`
- **Primary phases:** `replication_consistency`, `reliability`, `observability`, `large_scale_patterns`
- **Prerequisites:** [`26. Multi-tenant LLM gateway with token budget enforcement`](../26-multitenant-llm-gateway-token-budget-enforcement/README.md), [`31. Reconfigurable sharded key-value service`](../31-reconfigurable-sharded-kv-service/README.md)

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `production`-level systems reasoning.

## What to learn

- multi-region control/data-plane separation
- blast-radius control
- consistency and failover under region loss

## Prep reading

### Required (about 45–60 minutes total)
- *Designing Data-Intensive Applications* — Chapter 5, **Replication**
  - Why: baseline reading for geo-replication trade-offs.
- *Designing Data-Intensive Applications* — Chapter 9, **Consistency and Consensus**
  - Why: necessary for control-plane correctness across regions.
- AWS Well-Architected — **Reliability Pillar**: https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html
  - Why: practical framing for regional failure and recovery goals.

### Optional (10–15 minutes)
- OpenTelemetry docs — **Signals**: https://opentelemetry.io/docs/concepts/signals/
  - Why: useful for monitoring a control plane under failover and degraded modes.

### Enough for today when you understand
- why multi-region adds both latency and correctness pressure
- why control-plane consistency is not the same as data-plane throughput
- why degraded operation must be designed before the outage happens


## What to build

Design a geo-replicated control plane that serves global clients, survives region outages, and minimizes inconsistent configuration state.

## What a strong solution should show

A good solution makes region-failure behavior explicit, chooses a consistency model deliberately, and defines safe degraded operation.

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier


## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 32 start`
- `dist-sys 32 new`
- `dist-sys 32 list`
- `dist-sys 32 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under [`./submissions/`](./submissions/).
