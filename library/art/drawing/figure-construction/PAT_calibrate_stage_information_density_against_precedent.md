---
object_id: PAT_calibrate_stage_information_density_against_precedent
object_type: pattern
name: Calibrate Stage Information Density Against Approved Precedent
library_path:
  - art
  - drawing
  - figure-construction
stage_binding: 0 design
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: medium
foundation_object_id: none
tags:
  - staged_drawing
  - precedent_calibration
  - information_density
  - over_rendering
cross_links:
  - rel: supports
    target_object_id: AP_draw_a_figure_through_onion_skinned_stages
  - rel: supports
    target_object_id: AP_gate_staged_visual_work_by_approval
  - rel: related_to
    target_object_id: PAT_build_gesture_into_clear_masses
reference:
  source_id: gen1_art_fundamentals_4step
  source_title: PASS Gen 1 Universal Step 0 + Four-Stage Workflow
  author: Blu + Admin
  publish_date: 2026-07-30
  media_type: archive
  locator: universal_step_zero_four_stage_workflow, staged figure, dragon, and alien process images; guided corrections defining stage ceilings
  evidence_type: mixed
confidence: high
references:
  - image_path: library/art/drawing/figure-construction/assets/source_staged_figure_process_1.png
    caption: Use the four panels as purpose and density references for framework, blocking, developed form, and final line treatment rather than as subject templates.
    derived_from: universal_step_zero_four_stage_workflow, staged figure process 1
    origin: first_party_source
    review: passed
  - image_path: library/art/drawing/figure-construction/assets/source_staged_dragon_process.png
    caption: The dragon sequence shows a sparse articulated framework, a primitive block, specific organic development, and a rendered final while preserving one action.
    derived_from: universal_step_zero_four_stage_workflow, staged dragon process
    origin: first_party_source
    review: passed
  - image_path: library/art/drawing/figure-construction/assets/source_staged_alien_process.png
    caption: The alien sequence supplies an organic nonhuman comparison so stage density is not calibrated only against human anatomy.
    derived_from: universal_step_zero_four_stage_workflow, staged alien process
    origin: first_party_source
    review: passed
variants: []
---

# Calibrate Stage Information Density Against Approved Precedent

## Pattern Rule
**IF** a staged drawing is about to be generated, revised, or approved and an accepted same-stage process image exists in the repository
**THEN** inspect the matching stage and the immediately following stage before production, match the current stage's purpose and information density, and reject any result that resembles the following stage more closely than its own
**ELSE** use the written stage contract as the ceiling, state that visual calibration coverage is missing, and avoid inventing a denser substitute

## Do
- Choose the nearest useful lane before comparison: sparse skeleton and primitive block for structured or hard-surface subjects; sparse gesture and accumulated mass for organic scribble subjects. Compare purpose and commitment, not species, costume, or style.
- For Stage 0, compare with `precedent_stage0_dragon_marker_thumbnail.png`: broad marker-like strokes, flat value groups, camera, crop, gesture, silhouette, and major environment placement only.
- For Stage 1, compare with the first panel of the dragon or alien process: action, axes, joint locations, simple torso or pelvis symbols, endpoint markers, and critical prop paths. No developed thickness, anatomy, costume, shading, or environmental rendering.
- For Stage 2, compare with the blocking panel of the four-step process: obvious primitive masses, draw-through, centerlines, cross-contours, seated joints, overlap, and depth. Stop before anatomy, surface design, polished contour, or cinematic value modeling.
- For Stage 3, compare with the developed-form panel: the specific anatomy, creature, costume, armor, or mechanism may now be described, but final color, material spectacle, atmosphere, and presentation polish remain restrained.
- For Stage 4, compare with the final panel only after the earlier structure is approved. Add presentation information without changing the approved construction.
- Perform the comparison twice: once before generation to set the ceiling, and once after generation to inspect the actual artifact rather than trusting its stage label.
- When a result is too dense, strip the earliest class of next-stage information that entered; do not merely blur, desaturate, or relabel the same overworked image.

## Don't
- Treat captions, stage numbers, or a tutorial layout as proof that the drawing obeys the stage. Judge only the visible marks and information.
- Average several stages into a visually attractive compromise. Each stage must answer its own question and refuse the next stage's answer.
- Copy the precedent's subject, pose, or design. The precedent controls density, commitment, and function, not content.
- Use a known over-rendered case-study panel as permission to over-render. The Warbot and astronaut Stage 2 panels are cautionary ceilings, not positive Stage 2 targets.
- Advance because the image is impressive. A beautiful Stage 1 or Stage 2 is still wrong when its beauty comes from anatomy, detail, value modeling, or finish that belongs later.

## Checklist
- The current stage can be identified from visible information without reading its label.
- The current image resembles the approved same-stage precedent more than the next-stage precedent.
- Every mark has a current-stage job; no mark exists only to make the panel attractive.
- Stage 0 remains disposable, Stage 1 remains redrawable in about a minute, and Stage 2 remains visibly primitive and editable.
- Removing all next-stage information leaves the current stage fully readable.
- The pose, camera, attachments, endpoints, and depth order still reduce cleanly to the previously approved stage.

## Notes
Visual precedent is a calibration instrument, not a template. Prompt words such as “rough,” “construction,” and “tutorial sketch” are interpreted inconsistently by image generators; an accepted image gives a concrete ceiling for line density, volume commitment, anatomy, detail, and finish. The decisive test is comparative: if a proposed Stage 2 looks more like the repository's developed-form panel than its blocking panel, it is Stage 3 information wearing a Stage 2 label.

The original four-step images map to the current workflow as Stage 1 through Stage 4. Stage 0 was added later and uses the approved dragon marker thumbnail as its separate density target. The guided Warbot and zero-gravity astronaut sheets remain useful validation cases, but both contain Stage 2 over-rendering and therefore must not replace the cleaner blocking precedents.
