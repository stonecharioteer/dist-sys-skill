# Systems Design Curriculum TODO

## Completed

- [x] Reworked the exercise list using the curriculum/spec ideas from `deep-research-report-2.md`
- [x] Numbered the exercises in learning order
- [x] Added exercise type, tier, phases, and prerequisite structure
- [x] Created one folder per exercise
- [x] Added `README.md` for human-facing exercise guidance in each folder
- [x] Added `AGENT.md` for future language-agnostic scaffolding/evaluation planning in each folder
- [x] Linked prerequisite exercises from each exercise README

## Next

- [x] Add a machine-readable curriculum index (`index.yaml` or `index.json`)
- [x] Add a canonical exercise artifact template for authoring future exercises
- [x] Add a generation request template for future agent-based exercise generation
- [x] Add folder-level authoring notes to keep future work aligned with the spec
- [ ] Expand each exercise with explicit workload tables, NFRs, and failure modes
- [x] Convert exercise `01-in-memory-rate-limiter` into a fully fleshed example folder without a solution
- [x] Add a project skill for the `dist-sys <exercise> <action>` interview loop
- [x] Add a Pi prompt template for quickly invoking the dist-sys loop
- [x] Update the skill so `start` and `new` behave like mock-interview openings instead of jumping straight into tiny follow-up questions
- [x] Add a helper script for `dist-sys ls`, `dist-sys next`, and per-exercise attempt listing
- [x] Mark reviewed attempts as `completed` so the loop can distinguish finished work from resumable work
- [ ] Decide which exercises should get Python, TypeScript, and Rust tracks first
- [ ] Once a language is chosen for an exercise, create real test scaffolding from its `AGENT.md`

## Notes

- Keep the curriculum language-agnostic until an implementation track is intentionally added.
- Prefer small stepping-stone exercises before production-style composite designs.
- AI-era exercises should remain connected to earlier systems patterns instead of standing alone as novelty prompts.
