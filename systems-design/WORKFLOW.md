# Dist-sys interactive study workflow

This curriculum supports a chat-driven interview/practice loop with CLI-shaped entry commands.

## Command surface

Use commands in these forms:

```text
dist-sys ls [attempted|pending]
dist-sys next
dist-sys <exercise-number> <action> [--mode coaching|balanced|strict_interview] [--depth light|standard|deep]
```

Examples:

- `dist-sys ls`
- `dist-sys ls attempted`
- `dist-sys ls pending`
- `dist-sys next`
- `dist-sys 01 start`
- `dist-sys 01 start --mode strict_interview`
- `dist-sys 01 start --depth deep`
- `dist-sys 01 new`
- `dist-sys 01 new --mode coaching`
- `dist-sys 01 new --depth light`
- `dist-sys 01 list`
- `dist-sys 01 review`
- `dist-sys 01 review 2026-06-07-attempt-01`

## Command semantics

### `dist-sys ls [attempted|pending]`

- show a curriculum-wide summary with attempt counts
- optionally filter to attempted or pending work
- use `python3 dist-sys/systems-design/scripts/dist_sys_status.py ls ...` as the canonical helper

### `dist-sys next`

- recommend the next exercise to work on
- prefer unfinished work, then unreviewed work, then the first untouched exercise whose prerequisites are reasonably satisfied
- if there are multiple good next choices, provide alternatives and explain the trade-off in choosing among them
- use `python3 dist-sys/systems-design/scripts/dist_sys_status.py next` as the canonical helper

### `dist-sys <n> start`

- start the guided chat loop for exercise `<n>`
- if there is an unfinished active attempt, resume it
- otherwise create a new attempt and begin questioning
- frame the problem first like a mock interviewer before drilling into sub-questions
- support `--mode coaching|balanced|strict_interview` to control how much scaffolding is given
- support `--depth light|standard|deep` to control how deeply the learner is evaluated in discussion

### `dist-sys <n> new`

- always create a new attempt for exercise `<n>`
- begin a fresh guided chat loop
- present the exercise as a mock interview prompt before asking the first question
- support `--mode coaching|balanced|strict_interview` to control how much scaffolding is given
- support `--depth light|standard|deep` to control how deeply the learner is evaluated in discussion

### `dist-sys <n> list`

- list previous attempts for exercise `<n>`
- show date, attempt id, and review status

### `dist-sys <n> review`

- review the latest or current attempt for exercise `<n>`
- once reviewed, mark the attempt as `completed`

### `dist-sys <n> review <attempt-id>`

- review a specific previous attempt
- once reviewed, mark the attempt as `completed`

## Expected chat behavior after `start` or `new`

After the entry command, the rest of the interaction should be natural chat.

The opening should feel like a mock interview: restate the problem, define scope, mention key constraints, ask the learner to restate the problem in their own words, ask how they want to approach it, and then ask the first substantive question.

The agent should infer from conversation whether the learner is:

- answering the exercise
- revising a previous answer
- asking for a hint
- asking for a checkpoint review
- attaching or referring to a diagram
- asking to wrap up the attempt

The learner should not need extra commands for ordinary back-and-forth.

Because these exercises are discussion-first, deeper evaluation should come from assumption testing, alternative comparison, failure-mode probing, operational reasoning, and final design defense rather than code-writing prompts.

## Attempt storage layout

Each exercise stores attempts by default under `~/.dist-sys/`. Create `~/.dist-sys/` if it does not already exist.

```text
~/.dist-sys/
  <exercise-folder>/
    submissions/
      YYYY-MM-DD-attempt-01/
        submission.md
        review.md
        metadata.yaml
        assets/
          diagram-01.png
          diagram-02.svg
```

## Diagram submissions

The learner may export diagrams from Excalidraw as:

- PNG
- SVG

The agent should place those files in the active attempt's `assets/` directory and reference them from `submission.md` and `review.md`.

## Review behavior

Review must be:

- curriculum-aware
- scoped to the current exercise tier
- aware of prerequisite and future exercises
- resistant to overengineering beginner exercises
- explicit about when a concern belongs to a later exercise instead

A review should reward solving the current problem well, not prematurely solving later problems.

## Progression guardrail

The reviewer should actively protect the learner from being pushed too far ahead.

That means:

- for `foundation` exercises, prefer local reasoning and simple component choices
- for `applied` exercises, allow realistic scaling and failure discussion without demanding full distributed coordination
- for `distributed` exercises, require partitioning/replication/messaging trade-offs where appropriate
- for `production` exercises, allow broader ambiguity, operability, and multi-region or reconfiguration pressure

If the learner raises an advanced concern early, the reviewer may acknowledge it, but should clearly say whether it is:

- worth a brief note now, or
- better deferred to a later exercise in the curriculum

The reviewer should be comfortable saying things like:

- "Good concern, but that belongs later in the curriculum."
- "For this exercise, keep the design local and simple."
- "You do not need sharding, consensus, or distributed quotas here yet."
