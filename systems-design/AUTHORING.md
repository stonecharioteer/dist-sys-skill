# Systems Design Authoring Notes

This folder follows the spec guidance from `dist-sys/deep-research-report.md` and
`dist-sys/deep-research-report-2.md`.

## Build rules

- Start from learning objectives, not components.
- Keep exercises language-agnostic and platform-neutral by default.
- Every `distributed` or `production` exercise should include:
  - workload assumptions
  - at least one failure mode
  - non-functional requirements
  - observability expectations
  - explicit trade-offs
- Prefer stepping-stone exercises before composite production designs.
- AI-era exercises should evolve naturally from older systems patterns where possible.
- Review and guidance must be progression-aware: do not pressure learners to solve later-tier problems while they are still on an earlier exercise.
- When a later concern is mentioned early, explicitly label it as future-facing rather than required now.

## Folder contract

Each numbered exercise folder should contain:

- `README.md` for humans
- `AGENT.md` for future agent-driven scaffolding

## Templates

- `templates/exercise-artifact-template.yaml`
- `templates/generation-request-template.yaml`

## Machine-readable catalog

- `index.yaml`
