# Figure Stage Boundary Hardening

status: review-needed
owner: docs/worklogs/active
last_reviewed: 2026-08-03
superseded_by:
notes: Textual contract complete; Stage 2 visual precedents and omitted-source re-verification deferred.

## What changed

- Added a stage information-ceiling gate to both SkillForge runtime entrypoints.
- Hardened the universal construction foundation so block and rough passes stop
  before later-stage detail and polish.
- Rewrote the figure Stage 2 gate as a plain articulated maquette budget.
- Propagated that budget into figure massing, structural notation, and Chapter 4
  foreshortening controls.
- Recorded the decision and synchronized the art-lane next step.

## What was tested or reviewed

- SkillForge resolver bundle for the stage-hardening task.
- PASS schema validation: 259 objects passed.
- Deterministic index generation: 45 indexes, zero changes on repeat.
- Tooling unit tests: 36 passed.
- Hogarth grounding: four processed units passed.
- `git diff --check` on the resulting documentation changes.

## What worked

Stage 2 now has a positive allowed vocabulary and an explicit forbidden list.
The rule is available before image generation through the runtime skill, not
only inside a card that may or may not be retrieved.

## What failed

No new Stage 2 image was suitable for promotion as the canonical visual
precedent. The recent couple poster is evidence of the failure being corrected,
not the desired Stage 2 target. The recovered repo archive omits the original
`gen1_art_fundamentals_4step` source bundle and direct source images, so
`verify_grounding.py` and `verify_references.py` cannot complete for that source
from this archive. This is a packaging omission in the input archive, not a card
shape or tooling-test failure.

## Known risks

A generator may still render past the stop rule. Text alone cannot prove visual
density. The user-provided example pass must test and refine the visual boundary.

## Next safe step

Install the same overlay into the Project archive and Blu's active SkillForge
repo. In a canonical checkout that retains the first-party source bundle and
source images, re-run the grounding and reference gates. Later, compare candidate
Stage 2 examples against the information budget, attach reviewed references, and
only then tune retrieval or prompts further.

## Files changed

- `.agents/skills/skillforge/SKILL.md`
- `.claude/skills/skillforge/SKILL.md`
- `library/metaskills/iterative-construction/AP_plan_and_build_work_from_thumbnail_to_final.md`
- `library/art/drawing/figure-construction/AP_draw_a_figure_through_onion_skinned_stages.md`
- `library/art/drawing/figure-construction/PAT_build_gesture_into_clear_masses.md`
- `library/art/drawing/figure-construction/AP_notate_a_figure_in_structural_order.md`
- `library/art/drawing/figure-construction/AP_control_foreshortened_form_size_in_stage_two.md`
- continuity docs
