---
object_id: PAT_preserve_structure_during_stage4_amplification
object_type: pattern
name: Preserve Structure During Stage 4 Amplification
library_path:
  - art
  - drawing
  - figure-construction
stage_binding: 4 final
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: medium
foundation_object_id: none
tags:
  - stage_4
  - visual_continuity
  - drift_control
  - rendering
cross_links:
  - rel: supports
    target_object_id: AP_draw_a_figure_through_onion_skinned_stages
  - rel: supports
    target_object_id: AP_gate_staged_visual_work_by_approval
  - rel: related_to
    target_object_id: PAT_preserve_articulated_limb_chain
reference:
  source_id: guided_staged_visual_validation_2026_08_03
  source_title: "Guided Staged Visual Validation: Warbot and Zero-G Astronaut"
  author: Blu + Admin
  publish_date: 2026-08-03
  media_type: archive
  locator: approval_precedent_and_drift_validation, Warbot and zero-gravity astronaut process sheets, standalone Stage 4 renders, and guided critique
  evidence_type: mixed
confidence: high
references:
  - image_path: library/art/drawing/figure-construction/assets/precedent_warbot_process_sheet.png
    caption: The Warbot sheet preserves the broad action well and exposes Stage 2 density as a remaining weakness.
    derived_from: guided staged Warbot validation, process sheet
    origin: first_party_source
    review: passed
  - image_path: library/art/drawing/figure-construction/assets/precedent_warbot_final_render_a.png
    caption: The standalone Warbot final demonstrates strong subject continuity but also shows why muzzle axis and framing require explicit checks.
    derived_from: guided staged Warbot validation, standalone final A
    origin: first_party_source
    review: passed
  - image_path: library/art/drawing/figure-construction/assets/precedent_zero_g_astronaut_process_sheet.png
    caption: The astronaut sheet locks a difficult zero-gravity composition before final amplification.
    derived_from: guided staged zero-gravity astronaut validation, process sheet
    origin: first_party_source
    review: passed
  - image_path: library/art/drawing/figure-construction/assets/precedent_zero_g_astronaut_final_render.png
    caption: The amplified astronaut final gains cinematic impact while introducing a localized left-leg joint-chain error.
    derived_from: guided staged zero-gravity astronaut validation, standalone final
    origin: first_party_source
    review: passed
variants: []
---

# Preserve Structure During Stage 4 Amplification

## Pattern Rule
**IF** an approved Stage 3 or Stage 4 preview is being turned into a standalone final render
**THEN** preserve every approved structural and framing relationship while allowing lighting, color, material, atmosphere, depth cues, texture, and focal impact to intensify, then inspect global and local drift separately
**ELSE** return to the earliest unresolved stage instead of using rendering to invent or conceal structure

## Do
- Use the approved Stage 3 drawing and Stage 4 preview as active controlling references for the standalone render. A new final is a constrained amplification, not a fresh prompt interpretation.
- Lock global relationships first: camera position, lens impression, aspect ratio, crop, subject-to-frame scale, negative space, major silhouette, action, prop placement, and near-to-far order.
- Permit controlled presentational amplification: stronger light hierarchy, color contrast, atmosphere, materials, texture, edge control, depth cues, effects, and storytelling accents that do not move the underlying construction.
- Inspect every articulated chain after rendering: parent mass to joint, joint to member, member to endpoint. For a leg, trace hip → knee hinge → ankle → foot direction; for an arm, trace shoulder → elbow → wrist → hand action.
- Treat directional effects as geometry. A beam, projectile, grappling line, or tether begins at the correct endpoint and follows the muzzle, emitter, or attachment axis in one coherent path unless the design explicitly bends it.
- Distinguish **global drift**, which changes the picture, from **local drift**, which damages a part. Reject global drift. Repair local drift without discarding successful presentation when a constrained correction can preserve the whole.
- Interpret delivery language literally: “extract/crop this panel” means preserve pixels; “give me the final Stage 4 render” means create a full standalone render from the approved stage, not merely enlarge a crop.

## Don't
- Change the camera, crop, pose, silhouette, proportions, appendage path, endpoint function, or prop contact merely to make the final more dramatic.
- Let armor, clothing, smoke, darkness, or motion effects hide an impossible joint chain.
- Allow a foreground hand, foot, weapon, or muzzle to rotate independently from the member that supports it.
- Offset or curve a straight beam away from the muzzle axis for compositional convenience.
- Substitute a crop when the user requested a standalone final render, or regenerate from text alone when an approved visual source is available.
- Reject all amplification merely because some drift is possible. The goal is to fence creativity away from load-bearing structure, not to flatten Stage 4 into a mechanical copy.

## Checklist
- The final still reads as the same approved picture before details are examined.
- Camera, crop, subject scale, margins, and negative-space distribution remain intentional and traceable to the approved preview.
- Every limb and articulated appendage has one continuous mechanically plausible chain.
- Hands, feet, head, weapon contacts, visible joints, and other functional endpoints still exist and perform the approved action.
- Muzzle, flash, beam, projectile, tether, and grappling paths share the correct origin and axis.
- Added lighting, color, material, atmosphere, and effects clarify the structure instead of replacing it.
- Any remaining drift is named as global or local before approval.

## Notes
The Warbot and astronaut tests show why Stage 4 should preserve structure while allowing controlled amplification. The Warbot retained its design and action but exposed framing changes and an off-axis firing effect. The astronaut final hit harder than its process-sheet preview because lighting, depth, atmosphere, and perspective were amplified, yet the left leg became locally corkscrewed between hip, knee, ankle, and foot. The workflow succeeded by reducing a former whole-picture redesign into a specific repairable fault.

Rigid stages therefore act as constraint rails, not pixel guarantees. The acceptance target is not “nothing changes”; it is “nothing load-bearing changes.” Presentation may become stronger than the preview, but joint logic, endpoint function, prop alignment, framing, and the approved spatial relationships remain protected.
