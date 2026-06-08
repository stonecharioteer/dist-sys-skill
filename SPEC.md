# dist-sys-skill specification index

This repo packages the systems-design interview skill plus the curriculum and supporting spec files.

## Core skill files

- `SKILL.md` — skill entrypoint and command contract
- `prompts/dist-sys.md` — optional Pi prompt shortcut

## Curriculum and workflow

- `systems-design/README.md` — ordered exercise curriculum
- `systems-design/WORKFLOW.md` — attempt lifecycle and command semantics
- `systems-design/AUTHORING.md` — authoring/review guardrails
- `systems-design/index.yaml` — machine-readable curriculum index
- `systems-design/scripts/dist_sys_status.py` — helper for `ls`, `next`, and per-exercise attempt listing

## Templates

- `systems-design/templates/exercise-artifact-template.yaml`
- `systems-design/templates/generation-request-template.yaml`
- `systems-design/templates/attempt-submission-template.md`
- `systems-design/templates/attempt-review-template.md`
- `systems-design/templates/attempt-metadata-template.yaml`

## Research / rationale

- `deep-research-report.md` — original research and rationale
- `deep-research-report-2.md` — production-oriented generator/spec research

## Exercise-level spec artifacts

Some exercises may also include:

- `exercise-artifact.yaml`
- `README.md`
- `AGENT.md`

The intended long-term direction is for each exercise to gain a fuller machine-readable artifact.
