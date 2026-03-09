# COURSE.Science.PhysicsLab.11.CHECK_KEY

course_id: COURSE.Science.PhysicsLab.11
packet_file: CHECK_KEY
version: 0.9.0
status: DRAFT
updated: 2026-03-08
packet_mode: TEXTBOOK-SPINED
grade_level: 11
subject: Science
focus_window: Block 5 (Days 121-150) first-pass build
purpose: Teacher/check key for Physics w Lab packet-supported review and verification days.

grading_mode_defaults:
- tutoring_mode: CHECK_ONLY
- objective_workflow: mixed
- source_binding_required_for_concept_checks: yes
- diagram_proof_required_when_applicable: yes

completion_rules:
- COMPLETE requires:
  - visible prompt or source target
  - visible work/diagram/response artifact
  - enough evidence to verify the concept honestly
  - source-bound confirmation when the task depends on lesson/review content
- DEFERRED if:
  - the source is missing for a concept-dependent task
  - the diagram is missing where needed
  - the answer is too thin to verify
- REVIEW_REQUIRED if:
  - the answer may be plausible but cannot be grounded in the source
  - the vocabulary is imprecise enough to create ambiguity
  - the diagram is unclear or contradictory

## Day 132 Check Guide

day_number: 132
lesson_title: Optics Mixed Review + Verification Checkpoint

task_a_expected:
  reflection:
    - light bounces off a surface
  refraction:
    - light changes direction when entering a new medium because its speed changes
  distinction:
    - reflection stays in the original medium path context
    - refraction crosses into a new medium

task_b_expected:
  confused_concept:
    - reflection and refraction were confused
  corrected_explanation:
    - if the ray enters a new medium, it should pass into that medium and bend rather than bounce backward as a reflected ray would

task_c_expected:
  rule:
    - must be checked against the visible lesson/review source
  acceptable_verdicts:
    - supported
    - unsupported
    - incomplete
  full_credit_requirements:
    - names a concept from the source
    - points to a detail from the source
    - gives a verdict that matches the evidence

task_d_expected:
  d1:
    - the ray bends due to refraction when entering water from air
  d2:
    - a ray diagram helps visualize and justify the path of light
  d3:
    - an answer is not yet verifiable when it lacks source support, diagram support, or enough reasoning

rubric_dimensions:
- concept_accuracy
- source_use
- diagram_quality
- reasoning_quality
- clarity

concept_accuracy:
- strong:
  - concepts are correctly distinguished and applied
- partial:
  - generally right but imprecise
- weak:
  - concepts are blended or misidentified

source_use:
- strong:
  - refers to the relevant lesson/review material when needed
- partial:
  - source is present but weakly used
- weak:
  - no visible source support for a concept-dependent claim

diagram_quality:
- strong:
  - diagram is readable and conceptually consistent
- partial:
  - understandable but rough
- weak:
  - missing, unclear, or contradictory

reasoning_quality:
- strong:
  - explains why the answer fits the concept
- partial:
  - some explanation but underdeveloped
- weak:
  - mostly assertion

feedback_templates:
- strong:
  - "This is source-grounded and verifiable. The concept and the evidence line up."
- source_missing:
  - "I need the lesson or review source visible before I can verify this concept answer honestly."
- diagram_missing:
  - "This looks like a diagram question, so I still need the diagram or a clearer visual explanation."
- concept_mixup:
  - "You may be mixing reflection and refraction. Slow down and identify whether the light bounced or entered a new medium."
- too_thin:
  - "The answer may be close, but there is not enough evidence here to verify it honestly."

gradebook_write_template:
- course_id: COURSE.Science.PhysicsLab.11
- title: Physics w Lab Block 5 — Day 132 Optics Verification Checkpoint
- entry_type: ASSIGNMENT
- grading_basis: mixed
- status: FINAL only when evidence is sufficient
- notes:
  - include missing-source issue if relevant
  - include diagram quality note when relevant

notes:
- This key exists mainly to enforce honest verification.
- School should use it to block false completion when a concept-dependent answer was judged without the source.
