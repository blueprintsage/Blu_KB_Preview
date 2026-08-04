---
object_id: AP_gate_staged_visual_work_by_approval
object_type: ap
name: Gate Staged Visual Work by Approval
library_path:
  - art
  - drawing
  - figure-construction
stage_binding: 0 design
lane_fit: skill
foundation_role: specialization
routing_class: specialized
specialization_axis: medium
foundation_object_id: AP_plan_and_build_work_from_thumbnail_to_final
tags:
  - approval_gate
  - staged_visual_work
  - iteration
  - drift_prevention
cross_links:
  - rel: related_to
    target_object_id: AP_draw_a_figure_through_onion_skinned_stages
  - rel: related_to
    target_object_id: PAT_calibrate_stage_information_density_against_precedent
  - rel: related_to
    target_object_id: PAT_preserve_structure_during_stage4_amplification
reference:
  source_id: guided_staged_visual_validation_2026_08_03
  source_title: "Guided Staged Visual Validation: Warbot and Zero-G Astronaut"
  author: Blu + Admin
  publish_date: 2026-08-03
  media_type: archive
  locator: approval_precedent_and_drift_validation, approval-gated workflow decision, Warbot test, zero-gravity astronaut test, and final critique
  evidence_type: mixed
confidence: high
references: []
variants: []
---

# Gate Staged Visual Work by Approval

## Objective
Prevent downstream effort and visual drift by securing explicit approval at the rough-picture and staged-walkthrough decision points before committing to a standalone final render.

## Steps / Flow
1. **Resolve the requested delivery mode.** When the user explicitly asks for a finished image immediately, hidden planning may support that request. Otherwise, for an open-ended request to draw or design an image, default to the approval-gated route and deliver Stage 0 only.
2. **Generate Stage 0 and stop.** Show one quick marker-like rough idea containing the camera, crop, main gesture, silhouette, major subjects and props, environment masses, and broad value grouping. Do not include a process sheet, construction stages, or final rendering in the same response.
3. **Revise or approve the picture idea.** On rejection, make another Stage 0 or revise only the named decisions. On approval, lock the broad picture: camera, framing, subject scale, action, major placements, negative space, and story beat. Record any elements that remain intentionally open.
4. **Build the staged walkthrough from the approved idea.** Produce Stage 1 through Stage 4 preview as registered states of the same picture. Before and after each stage, apply `PAT_calibrate_stage_information_density_against_precedent`. Stage labels do not excuse visible over-rendering.
5. **Stop for walkthrough approval.** Review continuity, Stage 2 density, endpoint inventory, joint chains, prop alignment, and whether Stage 3 can fit the accepted block. Correct the earliest failing stage and propagate the repair forward. Do not spend a standalone final render on an unapproved walkthrough.
6. **Create the standalone Stage 4 render.** Use the approved Stage 3 and Stage 4 preview as controlling visual sources. Render the full image at presentation scale, preserving the approved framing and structure while allowing controlled lighting, color, material, atmosphere, texture, and focal amplification. A crop or enlargement is used only when the user asks to extract the existing panel.
7. **Inspect before delivery.** Apply `PAT_preserve_structure_during_stage4_amplification`. Separate global drift from local drift, verify every critical endpoint and articulated chain, and check directional effects against their emitters or attachments. Repair a local defect when possible; return to the earlier stage when the picture itself has changed.
8. **Preserve the accepted artifacts as precedents.** Store the Stage 0, process sheet, final render, and a short note naming both successes and failures. Future calibration should reuse the lesson, not silently canonize a flawed panel as a positive target.

## Notes
The approval gates protect different decisions. Stage 0 approval protects the picture idea before construction makes it expensive. Walkthrough approval protects the structure before final rendering makes errors harder to see. The standalone Stage 4 pass then has room to become more powerful without being permitted to redesign the approved work.

The guided Warbot and zero-gravity astronaut tests demonstrate the value and limit of this method. Global drift became small enough to diagnose, but Stage 2 still tended to borrow Stage 3 information and Stage 4 still introduced local framing, projectile-axis, or joint-chain changes. Approval and precedent calibration therefore work together: approval locks intent, visual precedents enforce stage ceilings, and final inspection catches the remaining local drift.
