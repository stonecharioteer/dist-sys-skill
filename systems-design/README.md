# Systems Design Exercise Set

This folder contains an ordered, language-agnostic systems design curriculum derived from:

- `dist-sys/deep-research-report.md`
- `dist-sys/deep-research-report-2.md`

The ordering now follows the second report's curriculum-first spec:

- **foundation**: local reasoning and single-machine design
- **applied**: realistic workload, scaling basics, and basic NFR pressure
- **distributed**: partitioning, replication, messaging, retries, and consistency choices
- **production**: operability, multi-region or reconfiguration pressure, ambiguity management, and cost trade-offs

Each exercise has its own numbered folder with:

- `README.md` for humans
- `AGENT.md` for future agent-driven scaffolding and evaluation work

## Ordered exercise index

| #   | Exercise                                                                                                                       | Tier        | Exercise type                                | Primary phases                                                            | Prereqs        |
| --- | ------------------------------------------------------------------------------------------------------------------------------ | ----------- | -------------------------------------------- | ------------------------------------------------------------------------- | -------------- |
| 01  | [In-memory rate limiter](./01-in-memory-rate-limiter/README.md)                                                                | foundation  | focused_component_design                     | single_machine, scalability                                               | —              |
| 02  | [LRU cache](./02-lru-cache/README.md)                                                                                          | foundation  | focused_component_design                     | single_machine, storage                                                   | —              |
| 03  | [Database index design for a read-heavy workload](./03-database-index-design/README.md)                                        | foundation  | focused_component_design                     | single_machine, storage                                                   | —              |
| 04  | [Single-process job scheduler](./04-single-process-job-scheduler/README.md)                                                    | foundation  | focused_component_design                     | single_machine, reliability                                               | —              |
| 05  | [Append-only log with crash recovery](./05-append-only-log-crash-recovery/README.md)                                           | foundation  | fault_injection                              | single_machine, storage, reliability                                      | 04             |
| 06  | [Single-node key-value store](./06-single-node-kv-store/README.md)                                                             | foundation  | open_ended_design                            | single_machine, storage                                                   | 05             |
| 07  | [Linearizable key-value store with compare-and-set](./07-linearizable-kv-cas/README.md)                                        | foundation  | focused_component_design                     | single_machine, reliability                                               | 06             |
| 08  | [Lock / lease service](./08-lock-lease-service/README.md)                                                                      | applied     | focused_component_design                     | single_machine, reliability                                               | 07             |
| 09  | [Metadata index with crash recovery](./09-metadata-index-crash-recovery/README.md)                                             | applied     | focused_component_design                     | single_machine, storage, reliability                                      | 05, 06         |
| 10  | [Refactor a stateful service into a stateless service](./10-refactor-stateful-service-stateless/README.md)                     | applied     | implementation_agnostic_architecture_diagram | scalability, reliability                                                  | 06             |
| 11  | [Load balancing and autoscaling for bursty traffic](./11-load-balancing-and-autoscaling/README.md)                             | applied     | capacity_planning                            | scalability, reliability                                                  | 10             |
| 12  | [Durable job queue](./12-durable-job-queue/README.md)                                                                          | applied     | open_ended_design                            | messaging, reliability                                                    | 04, 05, 08     |
| 13  | [MapReduce coordinator](./13-mapreduce-coordinator/README.md)                                                                  | applied     | whiteboard_sketch                            | messaging, reliability, scalability                                       | 12             |
| 14  | [Cache-backed task dispatcher](./14-cache-backed-task-dispatcher/README.md)                                                    | applied     | open_ended_design                            | scalability, messaging, reliability                                       | 12             |
| 15  | [Search index and document retrieval service](./15-search-index-document-retrieval/README.md)                                  | applied     | focused_component_design                     | storage, scalability                                                      | 03, 10         |
| 16  | [Workflow orchestration engine](./16-workflow-orchestration-engine/README.md)                                                  | applied     | focused_component_design                     | messaging, reliability                                                    | 12, 13         |
| 17  | [Partition-key selection for a multi-tenant event platform](./17-partition-key-selection-multitenant-event-platform/README.md) | distributed | tradeoff_analysis                            | partitioning, messaging                                                   | 12             |
| 18  | [Consistent hashing for a distributed cache cluster](./18-consistent-hashing-distributed-cache/README.md)                      | distributed | focused_component_design                     | partitioning, scalability                                                 | 02, 10         |
| 19  | [Read replicas and stale-read mitigation](./19-read-replicas-stale-read-mitigation/README.md)                                  | distributed | fault_injection                              | replication_consistency, reliability                                      | 06, 07         |
| 20  | [Idempotent webhook ingestion and processing pipeline](./20-idempotent-webhook-ingestion/README.md)                            | distributed | open_ended_design                            | messaging, reliability, observability                                     | 12, 19         |
| 21  | [Scaling consumer groups for ordered event processing](./21-scaling-consumer-groups-ordered-processing/README.md)              | distributed | capacity_planning                            | messaging, partitioning                                                   | 12, 17         |
| 22  | [Fault-tolerant key-value service](./22-fault-tolerant-kv-service/README.md)                                                   | distributed | open_ended_design                            | replication_consistency, reliability, storage                             | 07, 19         |
| 23  | [Sharded rate limiter](./23-sharded-rate-limiter/README.md)                                                                    | distributed | whiteboard_sketch                            | partitioning, replication_consistency, reliability                        | 01, 17, 18     |
| 24  | [Tenant-isolated durable job queue](./24-tenant-isolated-durable-job-queue/README.md)                                          | distributed | open_ended_design                            | messaging, partitioning, reliability                                      | 12, 17, 21     |
| 25  | [Approximate semantic retrieval / RAG retrieval platform](./25-approximate-semantic-retrieval-rag/README.md)                   | distributed | open_ended_design                            | storage, scalability, observability, large_scale_patterns                 | 15             |
| 26  | [Multi-tenant LLM gateway with token budget enforcement](./26-multitenant-llm-gateway-token-budget-enforcement/README.md)      | production  | open_ended_design                            | partitioning, replication_consistency, reliability, observability         | 23, 24         |
| 27  | [Conversation memory service](./27-conversation-memory-service/README.md)                                                      | production  | focused_component_design                     | storage, reliability, large_scale_patterns                                | 06, 15, 25     |
| 28  | [Agent workflow orchestrator](./28-agent-workflow-orchestrator/README.md)                                                      | production  | open_ended_design                            | messaging, reliability, observability, large_scale_patterns               | 16, 20, 26     |
| 29  | [Multi-tenant feed fan-out](./29-multi-tenant-feed-fan-out/README.md)                                                          | production  | time_boxed_mock_interview                    | large_scale_patterns, storage, messaging                                  | 21, 24         |
| 30  | [Social graph edge store under skew](./30-social-graph-edge-store-under-skew/README.md)                                        | production  | open_ended_design                            | large_scale_patterns, storage, partitioning                               | 15, 17, 18, 29 |
| 31  | [Reconfigurable sharded key-value service](./31-reconfigurable-sharded-kv-service/README.md)                                   | production  | time_boxed_mock_interview                    | partitioning, replication_consistency, reliability, observability         | 22, 23         |
| 32  | [Geo-replicated control plane](./32-geo-replicated-control-plane/README.md)                                                    | production  | time_boxed_mock_interview                    | replication_consistency, reliability, observability, large_scale_patterns | 26, 31         |

## Conventions

- Folder numbering is the recommended build order.
- Exercises stay language-agnostic until a language-specific implementation track is chosen.
- Future scaffolding should map back to the exercise type, phases, and stated invariants.
- Prerequisites are soft dependencies for learning order, not hard technical blockers.
