# Figure Stage Boundary Hardening

status: review-needed
owner: docs/worklogs/active
last_reviewed: 2026-08-03
superseded_by:
notes: Stage 0 and Stage 1 density locked; visual precedents and omitted-source re-verification deferred.

## What changed

- Locked Stage 0 to a quick marker-like rough picture idea and Stage 1 to a simple skeleton only.
- Added explicit Stage 0 and Stage 1 information ceilings to both SkillForge runtime entrypoints.
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

Stages 0, 1, and 2 now have positive allowed vocabularies and explicit
forbidden lists. Stage 0 remains a disposable visual idea; Stage 1 cannot
borrow volume or character drawing from later passes; Stage 2 remains the first
dimensional construction.
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

A generator may still beautify Stage 0 or Stage 1 despite the stop rules. Text
alone cannot prove visual density. Future tests must reject any Stage 1 that
reads as a character sketch rather than a sparse skeleton, and any Stage 2 that
reads as specific anatomy or presentation art.

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
