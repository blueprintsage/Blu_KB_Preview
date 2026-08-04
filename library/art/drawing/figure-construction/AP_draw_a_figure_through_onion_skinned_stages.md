---
object_id: AP_draw_a_figure_through_onion_skinned_stages
object_type: ap
name: Draw a Figure Through Onion-Skinned Stages
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
  - figure_drawing
  - onion_skinning
  - construction
  - rendering
cross_links:
  - rel: related_to
    target_object_id: AP_plan_and_build_work_from_thumbnail_to_final
  - rel: related_to
    target_object_id: PAT_build_gesture_into_clear_masses
  - rel: related_to
    target_object_id: AP_notate_a_figure_in_structural_order
  - rel: related_to
    target_object_id: AP_control_foreshortened_form_size_in_stage_two
  - rel: related_to
    target_object_id: AP_gate_staged_visual_work_by_approval
  - rel: related_to
    target_object_id: PAT_calibrate_stage_information_density_against_precedent
  - rel: related_to
    target_object_id: PAT_preserve_structure_during_stage4_amplification
reference:
  source_id: gen1_art_fundamentals_4step
  source_title: PASS Gen 1 Universal Step 0 + Four-Stage Workflow
  author: Blu + Admin
  publish_date: 2026-07-30
  media_type: archive
  locator: universal_step_zero_four_stage_workflow, workflow text and staged figure process 1
  evidence_type: mixed
confidence: medium
references:
  - image_path: library/art/drawing/figure-construction/assets/source_staged_figure_process_1.png
    caption: One figure keeps its action and landmarks while gesture, masses, specific form, and finish are developed in sequence.
    derived_from: universal_step_zero_four_stage_workflow, staged figure process 1
    origin: first_party_source
    review: passed
variants: []
---

# Draw a Figure Through Onion-Skinned Stages

## Objective
Carry one intended figure from a visualized pose to the requested refinement level while preserving its action, viewpoint, attachments, and depth through every successive drawing state.

## Steps / Flow
1. **Step 0 — show one rough idea of the picture and stop.** Make a quick-and-dirty marker-like thumbnail that suggests the subject, action, camera, crop, balance, silhouette, focal priority, major prop placement, shadow or value grouping, and near-to-far arrangement. Use broad strokes and flat shapes. For an open-ended drawing request, deliver Stage 0 only unless the user explicitly requested a finished result immediately. Do not solve anatomy, construction, features, costume, or finish here.
2. **Revise or approve the Stage 0 picture.** A rejected thumbnail is cheap: make another or change only the named decisions. Approval locks camera, framing, subject scale, action, major placements, negative space, and story beat. Stage 1 may correct local pose or proportion while preserving that approved picture; a major camera or composition change returns to Stage 0.
3. **Step 1 — translate the idea into a simple skeleton.** Use only a sparse structural map: action line and torso centerline; head oval with one facing axis; shoulder and hip axes; single-line limbs; joint circles; simple flat symbols for rib cage and pelvis; mitten, wedge, or point markers for hands and feet; and plain lines or flat silhouettes for critical props, wings, tails, shields, weapons, and contact points. Do not add limb thickness, developed masses, cross-contours, anatomy, facial features, hair, clothing, armor, texture, shading, environment detail, or polished silhouette.
4. **Calibrate Stage 1 before and after generation.** Apply `PAT_calibrate_stage_information_density_against_precedent`. Compare with the sparse skeleton panel and with the blocking panel as the forbidden next-stage ceiling. If the result looks like a character sketch, mannequin, or finished illustration when enlarged, simplify it before proceeding.
5. **Register the next sheet to the accepted skeleton.** Use the exact preceding artifact as the underdrawing, edit source, or light-board guide. Lock the canvas, camera, action, landmark positions, joint centers, member count, attachments, major proportions, critical endpoints, and near-to-far order. Make an intentional correction in the underlying stage when one of those decisions is wrong; never restart from the verbal prompt and hope for a similar pose.
6. **Step 2 — build a plain articulated maquette and stop.** Convert the accepted framework into the simplest masses that prove the figure: cranial ball and facial wedge, rib-cage barrel, pelvic wedge, tapered limb cylinders, joint blocks, hand wedges, foot wedges, and simple rigid prop masses. Use centerlines, cross-contours, draw-through, taper, overlap, foreshortening, width, projected length, and seated attachments. Do not model muscles, resolve facial identity, style hair, design fabric folds, add armor detail, texture, dramatic light, polished contour, or atmosphere.
7. **Pass the Stage 2 precedent and information-budget gates.** Compare the block directly with the approved blocking panels and the developed-form panels. If it resembles Stage 3 more than Stage 2, remove anatomy, surface design, line polish, value modeling, and environment detail until the primitives carry the pose by themselves. Lock one coherent position for every major mass, limb, joint, attachment, support point, overlap, and functional endpoint.
8. **Step 3 — describe the specific figure on a registered layer.** Turn the generic masses into the intended anatomy, identity, expression, hair masses, costume, creature structure, armor, or designed mechanism. Connect forms through believable transitions and refine hands, feet, face, and props. The accepted Stage 2 masses, attachments, and depth order remain fixed. Stop before complete lighting, material effects, atmospheric integration, texture finish, and presentation polish.
9. **Build a Stage 4 preview and stop for walkthrough approval.** Present the intended lighting, color, material, atmosphere, and focal hierarchy at process-sheet scale without changing Stage 3. Review the entire sequence backward and forward. Correct the earliest failing stage, propagate the repair, and secure approval before spending the standalone final pass.
10. **Create the standalone Stage 4 render from the approved visual sources.** Use the approved Stage 3 drawing and Stage 4 preview as controlling references. Render the full image at presentation scale; do not substitute a crop unless the user explicitly asks to extract the existing panel. Apply `PAT_preserve_structure_during_stage4_amplification`: preserve framing and load-bearing structure while allowing controlled presentational amplification.
11. **Inspect global and local drift before delivery.** Compare camera, crop, subject scale, negative space, silhouette, joint centers, articulated chains, attachments, endpoint inventory, props, directional effects, depth order, and unaffected objects. A beam, projectile, grappling line, or tether must begin at its correct endpoint and follow the emitter or attachment axis. Reject global drift; repair a local fault when possible without discarding successful presentation.

## Notes
This is the drawing-medium specialization of the universal thumbnail-to-final workflow. Its central production constraint is onion skinning: each stage is a developed state of one drawing, not an independent interpretation of the same prompt. A later pass may correct an earlier decision, but it should do so deliberately and carry that correction through the underlying construction rather than silently redesigning the figure. Approval now gates the expensive transitions: Stage 0 only → approval → Stage 1–4 walkthrough → approval → standalone Stage 4 → drift inspection. Each generated stage is compared with its approved same-stage precedent before it advances. The stage boundary can be remembered as: **Stage 0 shows a rough idea; Stage 1 locates everything; Stage 2 solves the body; Stage 3 describes the body; Stage 4 presents the body.** A beautiful Stage 1 or Stage 2 that already describes or presents the figure is overworked, not advanced. If a stage resembles the next precedent more closely than its own, it must be simplified or rebuilt.

The figure-mass pattern supplies the general Step 2 move: preserve the action while placing connected masses. For human action figures, the structural-order AP supplies the subordinate sequence and routes local torso, leg, arm, foot, and head decisions to their Chapter 2 patterns. The Chapter 4 size-control AP strengthens the block when foreshortened members make length unreliable. Other construction, anatomy, lighting, or rendering patterns can be chained into the stage where their decision is needed as the library grows. A Drill may be run before the piece as a warm-up or during a failed stage as a low-cost side study; the result of the Drill informs the main artifact but does not replace it.

Skill retrieval and image registration are separate success criteria. First verify that SkillForge was actually active and that the relevant procedure entered context. Then verify onion-skinned continuity directly: the exact prior image must be used as the edit target and the result must pass a registration check. Do not infer either condition from repository files merely being present.

A drawing must make forms exist in space. A clean diagram can explain names or relationships, but it does not satisfy this procedure when the requested product is a sketch, figure study, illustration, or render. Depth must survive without captions through orientation, overlap, recession, attachment, support, and turning planes.
