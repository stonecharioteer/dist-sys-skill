# 03. Database index design for a read-heavy workload

- **Tier:** `foundation`
- **Exercise type:** `focused_component_design`
- **Primary phases:** `single_machine`, `storage`
- **Prerequisites:** None

## Why this exercise

This exercise exists to strengthen the step from the previous topics into `foundation`-level systems reasoning.

## What to learn

- query-pattern-first schema thinking
- read optimization vs write amplification
- how indexes shape local performance

## Prep reading

### Required (about 45–60 minutes total)

- _Designing Data-Intensive Applications_ — Chapter 3, **Storage and Retrieval**
  - Why: introduces index-driven thinking and read/write trade-offs.
- PostgreSQL documentation — **Introduction to Indexes**: https://www.postgresql.org/docs/current/indexes-intro.html
  - Why: short, concrete explanation of what indexes are for.
- PostgreSQL documentation — **Index Types**: https://www.postgresql.org/docs/current/indexes-types.html
  - Why: useful catalog of common index shapes and when they help.

### Optional (10–15 minutes)

- Cockroach Labs blog — **SQL performance best practices**: https://www.cockroachlabs.com/blog/sql-performance-best-practices/
  - Why: good practical intuition about query shape and index impact.

### Enough for today when you understand

- why you index query patterns, not tables in the abstract
- why extra indexes speed reads but cost writes and storage
- that “index everything” is usually the wrong answer

## What to build

Design indexes and access paths for a small relational workload with a fixed schema and explicit hot queries.

### Problem statement

You are given a single-node relational database for a Pokédex-style game.

Assume these tables exist:

- `users(id, name)`
- `regions(id, name)`
- `pokemon(id, name, primary_type, secondary_type, region_id)`
- `sightings(user_id, pokemon_id, region_id, sighted_at)`

The workload is read-heavy, but sightings are still written continuously.

Assume:

- about 100,000 users
- about 5,000 Pokémon species
- about 50 million rows in `sightings`
- storage budget is limited: do not propose more than 5 secondary indexes total across all tables unless you can justify them strongly
- this is a `foundation` exercise: stay local to one database node and do not introduce sharding, replicas, or distributed search

Your job is to choose a small index set for the following hot queries:

1. find Pokémon species by `region` and `primary_type` (optionally also `secondary_type`)
2. list all Pokémon sighted by a given user
3. check whether a given user has ever sighted a specific Pokémon species
4. list all sightings in a given region
5. look up a user by exact `name`

You should explain:

- which indexes you would create
- which query each index helps
- which indexes you would avoid
- what write and storage costs your choices introduce

## What a strong solution should show

A good solution:

- ties each index directly to one or more query shapes
- prefers a small, high-value index set over indexing every column
- notices when a composite index can replace a weaker single-column index
- discusses read benefit vs write amplification and storage cost
- stays within the exercise scope without introducing distributed concerns

## Deliverables for the learner

- assumptions and constraints
- architecture or component design
- key invariants and trade-offs
- failure handling notes
- observability or debugging signals appropriate for the tier

## Interactive study loop

This exercise is designed to work with the curriculum chat loop described in [`../WORKFLOW.md`](../WORKFLOW.md).

Typical entry commands:

- `dist-sys 03 start`
- `dist-sys 03 new`
- `dist-sys 03 list`
- `dist-sys 03 review`

During an active attempt, the rest of the interaction should be natural chat. Your dated submissions and reviews should live under the exercise's default attempt store in `~/.dist-sys/<exercise-folder>/submissions/`.
