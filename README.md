# dist-sys-skill

A curriculum-aware systems-design interview skill and exercise set.

## What this repo contains

- `SKILL.md` — the skill definition
- `SPEC.md` — spec/research index for the packaged skill repo
- `systems-design/` — the numbered exercise curriculum
- `systems-design/scripts/dist_sys_status.py` — helper script for `ls`, `next`, and per-exercise attempt listing
- `prompts/dist-sys.md` — optional Pi prompt template
- `deep-research-report.md` and `deep-research-report-2.md` — source research documents behind the curriculum/spec

## Commands

The skill is designed around these chat commands:

- `dist-sys ls`
- `dist-sys ls attempted`
- `dist-sys ls pending`
- `dist-sys next`
- `dist-sys 01 start`
- `dist-sys 01 new`
- `dist-sys 01 list`
- `dist-sys 01 review`

After `start` or `new`, the interaction should continue as natural chat in mock-interview style.

## Attempt lifecycle

- new attempts start as `in_progress`
- after review they should become `completed`
- use `dist-sys <n> new` to retry an exercise later
- attempts are stored by default under `~/.dist-sys/`, which should be created automatically if missing

## Reading material

Each exercise README includes a bounded prep-reading section with:

- a manageable reading load for roughly one day
- verified web links where included
- valid chapter names from books where chapters are listed

## Helper script

Use the helper directly if needed:

```bash
python3 systems-design/scripts/dist_sys_status.py ls
python3 systems-design/scripts/dist_sys_status.py next
python3 systems-design/scripts/dist_sys_status.py exercise-list 1
```

Or with uv:

```bash
uv run python systems-design/scripts/dist_sys_status.py next
```

## Development tooling

This repo includes:

- `.pre-commit-config.yaml`
- `.markdownlint.json`
- `.prettierignore`
- `justfile`

Pre-commit runs checks for:

- Python lint/format via Ruff
- Markdown linting
- JS/TS/JSON/YAML/Markdown formatting via Prettier
- Conventional Commit enforcement on commit messages

Install hooks with:

```bash
uvx pre-commit install --hook-type pre-commit --hook-type commit-msg
```

Run all hooks manually with:

```bash
uvx pre-commit run --all-files
```

Useful `just` commands:

```bash
just install-hooks
just lint
just test-status
just next
```

## Publishing / installation notes

This repo is structured as a skill directory itself, so a skill-aware agent can load it from the repo root where `SKILL.md` lives.

## Install the skill

### Option 1: symlink into a global Pi skills directory

```bash
ln -s /Users/stonecharioteer/code/checkouts/learning/dist-sys-skill ~/.agents/skills/dist-sys-skill
```

Or:

```bash
ln -s /Users/stonecharioteer/code/checkouts/learning/dist-sys-skill ~/.pi/agent/skills/dist-sys-skill
```

### Option 2: copy it into a project

From another project, place it under:

```text
.agents/skills/dist-sys-skill/
```

or

```text
.pi/skills/dist-sys-skill/
```

### Option 3: add the repo path in Pi settings

Add the repo path to Pi's `skills` array in settings:

```json
{
  "skills": ["/Users/stonecharioteer/code/checkouts/learning/dist-sys-skill"]
}
```

### Pi

Pi should discover the skill from one of these locations or settings entries:

- `~/.pi/agent/skills/`
- `~/.agents/skills/`
- `.agents/skills/` in a project
- `.pi/skills/` in a project
- explicit `skills` settings entries

### Other harnesses

Pi's skills documentation notes that other Agent Skills-compatible harnesses can usually consume the same skill directory if they support `SKILL.md`-based discovery. The core curriculum files in `systems-design/` are also usable directly even outside a skill-aware environment.

### Prompt template for Pi

If you want the `/dist-sys` prompt shortcut, copy `prompts/dist-sys.md` into:

- `~/.pi/agent/prompts/`
- or `.pi/prompts/` in your project

## Attempt storage

Learner attempts live by default under `~/.dist-sys/<exercise-folder>/submissions/` so the repo stays clean and reusable for other learners.
