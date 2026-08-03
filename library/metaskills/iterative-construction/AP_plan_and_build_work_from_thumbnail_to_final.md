---
object_id: AP_plan_and_build_work_from_thumbnail_to_final
object_type: ap
name: Plan and Build Work From Thumbnail to Final
library_path:
  - metaskills
  - iterative-construction
stage_binding: 0 design
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
  - planning
  - iterative_construction
  - error_prevention
  - refinement
cross_links: []
reference:
  source_id: gen1_art_fundamentals_4step
  source_title: PASS Gen 1 Universal Step 0 + Four-Stage Workflow
  author: Blu + Admin
  publish_date: 2026-07-30
  media_type: archive
  locator: universal_step_zero_four_stage_workflow, workflow text and staged image set
  evidence_type: mixed
confidence: high
references: []
variants:
  - variant_id: VAR_ch06_action_centerline_figure_build
    variant_name: Action-Centerline Figure Build
    variant_basis: method_sequence
    source_id: marvel_how_to_draw_comics
    source_title: How to Draw Comics the Marvel Way
    locator: ch06, PDF pp. 61-62
    difference_from_foundation: Starts the skeleton with an action center line, develops primitive figure masses with loose draw-through strokes, selects the strongest exploratory lines, then adds tonal form.
    when_to_use: Use when a figure must preserve a lively action curve through construction and cleanup.
    when_not_to_use: Avoid when the primary problem is an unclear overall composition rather than a figure's gesture and structure.
    absorbed_from_object_id: none
  - variant_id: VAR_ch10_page_wide_staged_pencilling
    variant_name: Page-Wide Staged Comics Pencilling
    variant_basis: method_sequence
    source_id: marvel_how_to_draw_comics
    source_title: How to Draw Comics the Marvel Way
    locator: ch10, PDF pp. 108-114
    difference_from_foundation: "Holds the whole comics page at each construction stage: lay out every panel as stick-figure action, build all figures with primitive masses and draw-through, then flesh out the page rather than finishing one panel before the rest are designed."
    when_to_use: Use when a multi-panel page needs its action flow and figure relationships judged before local finish work can lock them in.
    when_not_to_use: Avoid when the work has no page-level sequence or when a single illustration's composition is already settled and its remaining risk is local form construction.
    absorbed_from_object_id: none
  - variant_id: VAR_ch11_editorial_cover_layout_review
    variant_name: Editorial Cover Layout Review
    variant_basis: method_sequence
    source_id: marvel_how_to_draw_comics
    source_title: How to Draw Comics the Marvel Way
    locator: ch11, PDF pp. 117-121
    difference_from_foundation: Creates several rough cover layouts, compares their reader hierarchy and production zones with an editor, then develops the selected layout from construction drawing to final pencils.
    when_to_use: Use when a cover or other promotional image must satisfy an editorial brief before detailed drawing makes its composition expensive to change.
    when_not_to_use: Avoid when the work has no stakeholder review or promotional-format constraints and a single thumbnail already resolves the intent.
    absorbed_from_object_id: none
---

# Plan and Build Work From Thumbnail to Final

## Objective
Carry a chosen intention from a cheap, testable concept to a finished work while catching the largest mistakes before detail makes them expensive to correct.

## Steps / Flow
1. **Step 0 — show a rough idea of the result.** Make one or more quick, low-cost probes that let the intended picture, argument, behavior, or outcome be seen and judged before production begins. In visual work, use a quick-and-dirty marker-like thumbnail: broad strokes, flat shapes, rough gesture, camera, crop, silhouette, and major value or spatial groups. It is an idea, not a commitment or a registered construction layer. It may be ugly, incomplete, and easily replaced. Select a direction only when the rough idea is clear enough to test.
2. **Skeleton — locate the essential structure only.** Translate the chosen idea into the sparsest working map that preserves its main relationships. In figure work this is a simple skeleton: action line, head oval and facing axis, shoulder and hip axes, single-line limbs, joint circles, simple symbols for rib cage and pelvis, hand and foot markers, and plain paths or silhouettes for critical props and appendages. Do not add volume, cross-contours, anatomy, facial features, costume, surface design, lighting, or polished contour. Advance only when the structure is obvious and cheap to correct.
3. **Block — make the structure functional and dimensional.** Give the skeleton its major masses, sections, components, or interfaces. Establish dependencies, scale, direction, and hierarchy before adding fine detail. Stop as soon as those large relationships are proven. The block is an information ceiling: detail, ornament, polish, and presentation that belong to the rough or final pass are defects here even when they are attractive.
4. **Rough — connect and correct.** Add the necessary internal connections, planes, reasoning, behavior, or supporting detail, but correct the biggest proportion, logic, or priority error first. The work should now function as a complete rough version without borrowing final polish, spectacle, or cleanup.
5. **Final — select and finish.** Remove what no longer serves the intent, strengthen the most important edges or signals, and add only the detail, testing, editing, or rendering that makes the work clear and reliable. Do not use finish work to hide an unresolved structural problem.
6. **Read backward against Step 0.** Test the finished result at the appropriate distance or scale. Its primary intent must still read first, its structure must still support that intent, and every later addition must reinforce rather than contradict the initial concept.

## Notes
The staged image set demonstrates the same construction order across a human figure, architecture, a dragon, and an alien. The subject changes, but the safeguard does not: expose a rough idea cheaply, locate the minimum structure without beautifying it, prove volume before elaborating it, then let refinement reveal the original decision instead of replacing it. Each stage is both a floor and a ceiling: it must answer its own question, and it must refuse information whose only purpose belongs to a later pass. For visual work, remember the short form: **Stage 0 shows a rough idea. Stage 1 locates everything. Stage 2 constructs the volumes. Stage 3 develops the subject. Stage 4 presents the finished image.**

A C++ random-number generator follows the same order. At Step 0, decide the caller-facing behavior: required number range, whether equal seeds must reproduce a sequence, ownership of generator state, and any relevant performance or concurrency constraints. The skeleton is the smallest API and state boundary that can express those decisions. The block adds the chosen generator and range-mapping behavior; the rough version exercises normal and boundary requests to expose wrong range, seed, or ownership assumptions. Only then does final work add tests, documentation, error handling, and cleanup. This does not make the universal AP a C++ recipe; it shows why resolving intent and structure before implementation improves the resulting codebase.

`VAR_ch06_action_centerline_figure_build` adapts the scaffold to an action figure: begin with a center-line gesture, add spheres, cubes, and cylinders through loose exploratory strokes, retain only the marks that clarify the form, and then use tonal treatment to complete it. Use this route when preserving gesture is the main risk; it is not a replacement for a composition-first thumbnail when the whole image still lacks a clear intent.

`VAR_ch10_page_wide_staged_pencilling` adapts the scaffold to a comics page: rough every panel's action as stick figures before finishing any one drawing, build the page's figures with spheres, cubes, cylinders, and necessary draw-through, then flesh out the page. Use it when the page's sequence and action flow need to remain visible throughout construction; it is not a substitute for the general foundation when there is no multi-panel whole to coordinate.

`VAR_ch11_editorial_cover_layout_review` adapts the scaffold to a comicbook cover: make several rough layouts, compare their lead-character visibility, scale, eye level, and available production areas with the editor, then develop the selected layout through construction to finished pencils. Use it when a promotional image must carry a clear editorial hierarchy before detail; it adds review time and format constraints that an ordinary single-image thumbnail may not need.
