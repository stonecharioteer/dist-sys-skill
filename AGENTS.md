# Repository Guidelines

## Purpose

This repo packages a curriculum-aware systems-design interview skill plus its supporting exercise set, workflow, templates, and research rationale.

The intended user experience is:

- invoke the skill with CLI-shaped commands such as `dist-sys ls`, `dist-sys next`, or `dist-sys 01 start`
- enter a mock-interview-style chat loop
- have attempts recorded by default under `~/.dist-sys/<exercise-folder>/submissions/`
- get curriculum-aware reviews that do not push later-tier complexity too early

## Interaction Model

### Command surface

The skill should support:

- `dist-sys ls`
- `dist-sys ls attempted`
- `dist-sys ls pending`
- `dist-sys next`
- `dist-sys <exercise> start`
- `dist-sys <exercise> new`
- `dist-sys <exercise> list`
- `dist-sys <exercise> review`
- `dist-sys <exercise> review <attempt-id>`

### Mock interview style

For `start` and `new`, the skill should:

1. frame the exercise like an interviewer
2. restate the problem in a few lines
3. define the scope and important constraints
4. tell the learner what kind of answer is expected at that tier
5. ask the first question

After that, the rest of the interaction should be natural chat.

### Progression guardrail

The reviewer/interviewer must be aware of the larger curriculum and avoid forcing later-tier concerns too early.

Examples:

- do not push distributed coordination into foundation exercises
- do not require sharding, multi-region semantics, or consensus before the appropriate stage
- explicitly say when a concern is better deferred to a later exercise

## Attempt Lifecycle

Attempts use a simple lifecycle:

- `in_progress`
- `completed`

Rules:

- `start` resumes unfinished work if present, otherwise creates a new attempt
- `new` always creates a fresh attempt
- after review, attempts should become:
  - `status: completed`
  - `review_status: reviewed`

Reviewed work can be revisited later by creating a new attempt.

## Attempt Storage

Each exercise stores attempts by default under `~/.dist-sys/<exercise-folder>/submissions/`.
Create `~/.dist-sys/` if it does not exist.

Expected files per attempt:

- `submission.md`
- `review.md`
- `metadata.yaml`
- `assets/` for diagrams such as exported Excalidraw PNG/SVG

Keeping attempts outside the repo keeps it reusable for other learners.

## Canonical Helpers

Use `systems-design/scripts/dist_sys_status.py` as the canonical helper for:

- `dist-sys ls`
- `dist-sys next`
- `dist-sys <exercise> list`

Do not re-derive this status logic ad hoc if the helper script can answer it.

## Reading Material

Each exercise README should include a bounded **Prep reading** section.

Requirements:

- manageable in about a day
- preferably official docs, stable blog posts, or valid book chapters
- links should be verified before being added
- reading should match the tier and not overwhelm the learner with later topics

## Style for Exercise Content

- keep exercises language-agnostic
- prefer precise behavior and trade-offs over framework detail
- make prerequisites explicit and link them
- keep beginner exercises small and concrete
- AI-era exercises should feel like natural extensions of earlier systems patterns

## Tooling

### Pre-commit

This repo uses `.pre-commit-config.yaml` for:

- Python lint/format via Ruff
- Markdown linting
- JS/TS/JSON/YAML/Markdown formatting via Prettier
- Conventional Commit enforcement on commit messages

Install hooks with:

```bash
uvx pre-commit install --hook-type pre-commit --hook-type commit-msg
```

Run them manually with:

```bash
uvx pre-commit run --all-files
```
