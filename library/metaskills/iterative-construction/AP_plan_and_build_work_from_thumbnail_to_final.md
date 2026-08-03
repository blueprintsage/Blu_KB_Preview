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
1. **Step 0 — thumbnail the intent.** Make one or more small, low-cost concepts that state the composition, priority, and intended result before committing to production. In visual work this is a compositional thumbnail; in writing it can be a brief scene or argument shape; in coding it can be the smallest design sketch that exposes the desired behavior. Select a direction only when its main idea is clear enough to judge.
2. **Skeleton — establish the minimum working structure.** Lay down the essential relationships in their simplest form: the main gesture or hierarchy in art, the sequence of thought in writing, or the core path and boundaries in code. Keep it sparse enough that a structural error is obvious. Advance only when the work still communicates the choice made in Step 0; do not borrow dimensional development or finish merely to make the skeleton look complete.
3. **Block — make the structure functional and dimensional.** Give the skeleton its major masses, sections, components, or interfaces. Establish dependencies, scale, direction, and hierarchy before adding fine detail. Stop as soon as those large relationships are proven. The block is an information ceiling: detail, ornament, polish, and presentation that belong to the rough or final pass are defects here even when they are attractive.
4. **Rough — connect and correct.** Add the necessary internal connections, planes, reasoning, behavior, or supporting detail, but correct the biggest proportion, logic, or priority error first. The work should now function as a complete rough version without borrowing final polish, spectacle, or cleanup.
5. **Final — select and finish.** Remove what no longer serves the intent, strengthen the most important edges or signals, and add only the detail, testing, editing, or rendering that makes the work clear and reliable. Do not use finish work to hide an unresolved structural problem.
6. **Read backward against Step 0.** Test the finished result at the appropriate distance or scale. Its primary intent must still read first, its structure must still support that intent, and every later addition must reinforce rather than contradict the initial concept.

## Notes
The staged image set demonstrates the same construction order across a human figure, architecture, a dragon, and an alien. The subject changes, but the safeguard does not: commit cheaply to an intention, prove the structure before elaborating it, then let refinement reveal the original decision instead of replacing it. Each stage is both a floor and a ceiling: it must answer its own question, and it must refuse information whose only purpose belongs to a later pass.

A C++ random-number generator follows the same order. At Step 0, decide the caller-facing behavior: required number range, whether equal seeds must reproduce a sequence, ownership of generator state, and any relevant performance or concurrency constraints. The skeleton is the smallest API and state boundary that can express those decisions. The block adds the chosen generator and range-mapping behavior; the rough version exercises normal and boundary requests to expose wrong range, seed, or ownership assumptions. Only then does final work add tests, documentation, error handling, and cleanup. This does not make the universal AP a C++ recipe; it shows why resolving intent and structure before implementation improves the resulting codebase.

`VAR_ch06_action_centerline_figure_build` adapts the scaffold to an action figure: begin with a center-line gesture, add spheres, cubes, and cylinders through loose exploratory strokes, retain only the marks that clarify the form, and then use tonal treatment to complete it. Use this route when preserving gesture is the main risk; it is not a replacement for a composition-first thumbnail when the whole image still lacks a clear intent.

`VAR_ch10_page_wide_staged_pencilling` adapts the scaffold to a comics page: rough every panel's action as stick figures before finishing any one drawing, build the page's figures with spheres, cubes, cylinders, and necessary draw-through, then flesh out the page. Use it when the page's sequence and action flow need to remain visible throughout construction; it is not a substitute for the general foundation when there is no multi-panel whole to coordinate.

`VAR_ch11_editorial_cover_layout_review` adapts the scaffold to a comicbook cover: make several rough layouts, compare their lead-character visibility, scale, eye level, and available production areas with the editor, then develop the selected layout through construction to finished pencils. Use it when a promotional image must carry a clear editorial hierarchy before detail; it adds review time and format constraints that an ordinary single-image thumbnail may not need.
