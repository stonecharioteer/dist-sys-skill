---
name: dist-sys-interview-loop
description: Runs the dist-sys systems-design study loop when the user types commands like "dist-sys ls", "dist-sys 01 start", "dist-sys 01 new", "dist-sys 01 list", or "dist-sys 01 review". Use for curriculum-aware learning sessions, attempt tracking, submission logging, review generation, and diagram-aware feedback on the numbered exercises under systems-design/.
---

# Dist-sys Interview Loop

Use this skill when the user wants to study or review the systems-design curriculum in `systems-design/` using CLI-shaped chat commands.

## Command contract

Recognize commands in these forms:

```text
dist-sys ls [attempted|pending]
dist-sys next
dist-sys <exercise-number> <action> [arg] [--mode coaching|balanced|strict_interview] [--depth light|standard|deep]
```

Supported actions:

- `ls`
- `next`
- `start`
- `new`
- `list`
- `review`

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

After `start` or `new`, switch into a natural chat loop. Do **not** require more commands for ordinary learner interaction.

The interaction style should feel like a **mock systems-design interview**, especially for `start` and `new`.

## Files to load first

Read these before acting:

- `systems-design/index.yaml`
- `systems-design/WORKFLOW.md`
- `systems-design/AUTHORING.md`
- the selected exercise folder's:
  - `README.md`
  - `AGENT.md`
  - `exercise-artifact.yaml` if it exists

Use the index to resolve the exercise number to its folder and title.

## Behavior by action

### `dist-sys ls [attempted|pending]`

Use the helper script:

```bash
python3 systems-design/scripts/dist_sys_status.py ls [attempted|pending]
```

Show a curriculum-wide summary.

For each exercise, compute from its default submissions directory under `~/.dist-sys/<exercise-folder>/submissions/`.
Create `~/.dist-sys/` first if it does not exist.

- exercise number and title
- attempt count
- latest attempt id if any
- latest attempt date if any
- whether any attempt is still in progress
- whether the latest attempt has been reviewed
- assessment of the latest attempt if it has been reviewed, using a compact action-oriented label that tells the learner at a glance whether they should revisit it later

Assessment should be a short, action-oriented summary derived from the latest reviewed attempt's `review.md`, preferably from the review's recommended next step or equivalent top-level judgment.

Prefer labels that are glanceable and directly answer "what should I do with this later?", such as:

- `move_on`
- `revise_now`
- `redo_later`
- `not_reviewed` when no reviewed latest attempt exists

Avoid vague labels. The assessment should help the learner immediately decide whether the exercise is done for now or worth revisiting.

Filters:

- `dist-sys ls` shows all exercises
- `dist-sys ls attempted` shows only exercises with one or more attempts
- `dist-sys ls pending` shows exercises with an in-progress or unreviewed latest attempt

### `dist-sys next`

Use the helper script:

```bash
python3 systems-design/scripts/dist_sys_status.py next
```

Recommend the next exercise to work on.

Use this priority:

1. first exercise with an in-progress attempt
2. otherwise first exercise whose latest attempt exists but is unreviewed
3. otherwise the earliest exercise with no attempts yet whose prerequisites are reasonably satisfied
4. otherwise the next exercise after the highest-numbered reviewed exercise that still has no later reviewed work

If there is more than one good next choice at the same stage, provide a small set of alternatives rather than forcing only one answer.

When offering alternatives:

- prefer exercises whose prerequisites have already been attempted or reviewed
- prefer lower-numbered exercises when all else is equal
- explain why each option is a sensible next step
- clearly mark one as the default recommendation if appropriate

When responding, include:

- exercise number and title
- why it is the recommended next step
- a suggested command, usually `dist-sys <n> start`
- optional alternatives when multiple next steps are equally reasonable

### `dist-sys <n> start`

1. Resolve the exercise from `index.yaml`.
2. Check the exercise's default submissions directory at `~/.dist-sys/<exercise-folder>/submissions/`.
   Create `~/.dist-sys/` first if it does not exist.
3. If there is an unfinished attempt (`metadata.yaml` with `status: in_progress`), resume it.
4. Otherwise create a new dated attempt.
5. Start the guided study loop in **interviewer mode**.
6. Respect `--mode coaching|balanced|strict_interview` if supplied; otherwise default to `balanced` or infer from the learner's request.
7. Respect `--depth light|standard|deep` if supplied; otherwise default to `deep` or infer from the learner's request.
8. Include the exercise's **Prep reading** from `README.md` in the opening response, both for resumed and fresh attempts.

### `dist-sys <n> new`

1. Resolve the exercise.
2. Always create a fresh attempt.
3. Start the guided study loop in **interviewer mode**.
4. Respect `--mode coaching|balanced|strict_interview` if supplied; otherwise default to `balanced` or infer from the learner's request.
5. Respect `--depth light|standard|deep` if supplied; otherwise default to `deep` or infer from the learner's request.
6. Include the exercise's **Prep reading** from `README.md` in the opening response.

### `dist-sys <n> list`

Use the helper script:

```bash
python3 systems-design/scripts/dist_sys_status.py exercise-list <n>
```

List attempts in the exercise's default submissions directory under `~/.dist-sys/` with:

- attempt id
- date
- status
- review status
- whether assets exist

If there are no attempts, say so plainly.

### `dist-sys <n> review [attempt-id]`

1. Resolve the exercise.
2. Select the specified attempt or the latest/current one.
3. Read `submission.md`, `metadata.yaml`, and note any assets under `assets/`.
4. Generate or update `review.md`.
5. Update `metadata.yaml` so reviewed attempts become:
   - `review_status: reviewed`
   - `status: completed`
6. Return a concise review summary in chat.

## Guided study loop

Once an attempt is active, the learner should be able to respond naturally in chat.

### Interview strictness modes

The study loop should support three interviewing styles, either inferred from the learner's request or set explicitly when they ask:

- `coaching`
- `balanced`
- `strict_interview`

Default to `balanced`.

Mode behavior:

- `coaching`:
  - more clarification help
  - more explicit scaffolding when the learner is stuck
  - okay to offer examples earlier
- `balanced`:
  - ask open questions first
  - offer hints only after the learner shows confusion or asks
  - maintain interview feel without being overly withholding
- `strict_interview`:
  - minimize hints
  - avoid suggesting likely solution structures unless the learner explicitly requests help
  - prefer short interviewer-style follow-ups

If the learner says things like:

- "be stricter"
- "don't hint"
- "coach me more"
- "treat this like a real interview"

adapt the mode immediately and say so briefly.

### Evaluation depth

In addition to interview strictness, the study loop should support evaluation depth levels:

- `light`
- `standard`
- `deep`

Default to `deep`.

Depth behavior:

- `light`:
  - fewer follow-up questions
  - focus on getting to a coherent answer
- `standard`:
  - probe core assumptions, trade-offs, and failure cases
- `deep`:
  - probe assumptions more aggressively
  - require at least one rejected alternative when the exercise format allows it
  - ask explicit failure-mode and operational questions
  - ask the learner to defend the chosen design, name the biggest weakness, and say what they would improve next

If the learner says things like:

- "push harder"
- "go deeper"
- "evaluate this more strictly"
- "light touch"

adapt the depth immediately and say so briefly.

## Interviewer-mode opening

When starting a new or resumed attempt, do not jump straight to a tiny follow-up question.

First, frame the exercise like an interviewer would:

1. State the exercise title.
2. Summarize the problem statement in 3-6 lines.
3. State the expected scope clearly.
4. Mention any especially important constraints.
5. Tell the learner what kind of answer is expected at this tier.
6. Show the bounded **Prep reading** section from the exercise `README.md` as part of the opening, preserving any required vs optional structure and links.
7. Ask the learner to briefly restate the problem in their own words before moving into design details.
8. Ask how they would like to approach the answer before drilling into details.
9. Only after that, ask the first substantive interview question.

A good opening sounds like:

- "Let's work on 01, In-memory rate limiter."
- "You're designing an in-process rate-limiting component for a single API process..."
- "Keep this local and simple; no distributed coordination yet."
- "Prep reading: ..."
- "Before we go deeper, restate the problem in your own words so I can check we have the same mental model."
- "Then tell me how you would choose to approach the answer."

After the opening, infer from the learner's messages whether they are:

- answering the current question
- revising a previous answer
- asking for a hint
- asking for a checkpoint review
- referencing a diagram
- asking to wrap up

### Questioning style

For `foundation` exercises:

- ask one small interview-style question at a time
- keep the learner focused on the local problem
- prefer simple component/interface reasoning
- do not push later distributed concerns
- explicitly tell the learner what kind of answer you want next when they seem unsure
- begin by asking the learner to rephrase the problem in their own words and describe how they would like to approach the answer
- separate three phases clearly:
  - problem clarification
  - learner assumptions / framing
  - actual design work
- do not move into design work until the learner's mental model is clear enough
- avoid prematurely steering them toward a specific implementation shape before they have shown their own understanding
- do not reveal the most polished or "optimal" solution structure too early; let the learner propose a direction first, then coach from there
- do not embed likely answers in the question itself through leading examples, parenthetical hints, or suggested data structures/API shapes unless the learner explicitly asks for hints
- when asking about design choices, prefer open questions first; only offer examples after the learner asks for help or is clearly stuck
- for bounded exercises, prefer the bounded prompt from the exercise README rather than asking the learner to invent the entire domain, schema, workload, and constraints from scratch
- at `standard` or `deep` evaluation depth, probe at least assumptions, trade-offs, and one failure case
- at `deep` evaluation depth, also probe:
  - one rejected alternative
  - one operational/observability concern
  - one scaling or limit concern appropriate to the tier
  - a short defense of why the chosen design fits this exercise

For `applied` exercises:

- allow realistic workload and failure reasoning
- do not demand full distributed coordination unless the exercise requires it

For `distributed` exercises:

- ask about partitioning, replication, messaging, retries, and consistency when relevant

For `production` exercises:

- allow ambiguity, operations, cost, reconfiguration, and multi-region pressure

### Progression guardrail

The reviewer and coach must be aware of the larger curriculum.

Do **not** overwhelm the learner by requiring later-tier ideas early.

If the learner raises a future concern too early, respond like:

- "Good concern, but that belongs later in the curriculum."
- "For this exercise, keep the design local and simple."
- "You do not need sharding, consensus, or distributed quotas here yet."

Reward a strong answer to the current exercise, not a premature answer to later exercises.

## Attempt creation

Attempt folders live under the selected exercise's default attempt store:

```text
~/.dist-sys/<exercise-folder>/submissions/YYYY-MM-DD-attempt-XX/
```

Create these files:

- `submission.md`
- `metadata.yaml`
- `assets/`

Use these templates:

- `systems-design/templates/attempt-submission-template.md`
- `systems-design/templates/attempt-metadata-template.yaml`
- `systems-design/templates/attempt-review-template.md` (only when reviewing)

### Attempt id rules

Use the current date and the next available ordinal for that day:

- `2026-06-07-attempt-01`
- `2026-06-07-attempt-02`

## Writing learner progress

Append useful learner content into `submission.md` as the chat proceeds.

At minimum capture:

- assumptions
- design/interface ideas
- trade-offs
- failure/edge-case notes
- observability notes
- references to diagrams

Do not dump the entire raw chat transcript. Summarize and structure the learner's content so the file remains readable.

When the learner signals a settled answer with phrases like:

- "this is my final answer"
- "let's wrap up"
- "that's my answer"

append a short `### Final answer` section to `submission.md` that cleanly summarizes the final chosen design, not just the exploratory discussion.

Before a full final review, especially at `standard` or `deep` evaluation depth, try to capture a compact pre-review summary covering:

- assumptions
- chosen design
- rejected alternative (if any)
- biggest risk / weakness
- what the learner would improve next

## Diagram handling

If the learner provides a path to an exported Excalidraw PNG or SVG:

1. Copy it into the active attempt's `assets/` directory.
2. Name it clearly, e.g. `diagram-01.png`.
3. Add a link to it from `submission.md`.
4. Mention it during review.

If the learner only attaches an image in chat without a filesystem path, you may review it in-chat, but explain that persisting it into the attempt folder requires a path you can copy from.

## Review generation

When reviewing:

1. Use the current exercise rubric and scope.
2. Stay curriculum-aware.
3. Mention what is strong.
4. Mention what is missing.
5. Call out overengineering.
6. State which concerns should be deferred to later exercises.
7. Recommend one next step using a standardized label: `move on`, `revise now`, or `redo later`.

Write the full result to `review.md` using `systems-design/templates/attempt-review-template.md` as the shape.

When possible, make the review's final recommendation easy to parse from the `## Recommended next step` section so `dist-sys ls` can surface a compact latest-attempt assessment.

Prefer exact phrases that map cleanly to the `ls` assessment label, for example:

- `move on`
- `revise now`
- `redo later`

### Checkpoint reviews

If the learner asks for a checkpoint review before the final review, structure it explicitly around:

- what is already strong enough
- what is still missing
- whether they should continue, tighten the answer, or wrap up

Checkpoint reviews should not mark the attempt complete unless the learner is clearly asking for the full final review.

For discussion-first exercises, use checkpoint and final reviews to deepen evaluation rather than asking for code. Good evaluation questions include:

- Which assumption matters most to your design?
- What alternative did you reject and why?
- What breaks first under failure or load?
- How would an operator notice the problem?
- Why is this design appropriate for this curriculum tier?

## Practical file operations

You may use shell commands for directory creation, copying assets, and listing attempts.

Typical operations include:

- create `~/.dist-sys/` if it does not exist
- create attempt directories under `~/.dist-sys/<exercise-folder>/submissions/`
- populate files from templates
- use `python3 systems-design/scripts/dist_sys_status.py ...` for `ls`, `next`, and attempt listing
- copy learner-provided diagram files into `assets/`
- update metadata after review so reviewed attempts are marked completed

## Response style

- Be calm and coaching-oriented.
- Sound like a thoughtful mock interviewer, not just a file manager.
- Keep the learner moving.
- Ask the next useful question instead of flooding them with the whole rubric.
- Be explicit about scope when the learner is overcomplicating the exercise.
- When starting an attempt, frame the problem before questioning.
- Ask the learner to restate the problem in their own words before drilling into design specifics.
- Ask how they want to approach the answer before narrowing into implementation details.
- Let the learner propose an initial approach before suggesting likely solution structures.
- Avoid putting candidate answers into the prompt unless the learner explicitly asks for examples or hints.
- When the learner seems lost, restate the problem and ask a narrower interview question.
- For foundation exercises especially, prefer bounded prompts from the README over asking the learner to invent every part of the problem setup.
