# COURSE.Math.Algebra2.11

course_id: COURSE.Math.Algebra2.11
version: 0.9.0
status: DRAFT
updated: 2026-03-08

title: Algebra 2
grade_level: 11
subject: Math
credit: 1.0
course_length_days: 180
semester_length_days: 90
block_length_days: 30

source_model:
  provider: Easy Peasy
  source_model_url: https://allinonehighschool.com/algebra-2-new/
  source_model_role:
    - primary workflow source
    - day-by-day progression model
    - assignment sequence anchor

textbook_spine:
  spine_status: pending_final_selection
  approved_open_supports:
    - TX.MATH.IA.001 — OpenStax Intermediate Algebra
    - TX.MATH.BIA.002 — Beginning and Intermediate Algebra (Tyler Wallace)
  preferred_primary_spine:
    - TX.MATH.A2.003 — open Algebra 2 spine (still needed)
  notes:
    - Until a dedicated open Algebra 2 spine is chosen, use Easy Peasy for daily sequence and Blu-made original worksheets for current-day work.
    - OpenStax / Wallace may be used for prerequisite refresh, alternate explanations, and extra practice.

school_runtime_defaults:
  class_mode: INTERNAL
  tutoring_mode: CHECK_ONLY
  expected_artifacts:
    - worksheet
    - show-work scan/photo
    - typed answers
  completion_requires:
    - assignment source or worksheet
    - completed work artifact
    - source-grounded verification

daily_resolution_contract:
- Resolve `day_number` against the Easy Peasy source model first.
- If a direct daily worksheet, PDF, or assignment page is available, bind it as the current source.
- If the Easy Peasy daily item is inaccessible or thin, use the current course objective plus Blu-made original Algebra 2 practice aligned to the open support spine.
- Day progression follows the student school record as the authoritative runtime source.

block_plan:
- block: 1
  days: 1-30
  focus: foundations refresh, equations, expressions, prerequisite repair
- block: 2
  days: 31-60
  focus: functions, graphing, systems, algebraic structure
- block: 3
  days: 61-90
  focus: quadratics, polynomials, factoring, roots
- block: 4
  days: 91-120
  focus: rational expressions, radicals, exponential/log ideas
- block: 5
  days: 121-150
  focus: advanced mixed problem solving, cumulative practice, course-specific late units
- block: 6
  days: 151-180
  focus: review, cumulative mastery, final readiness

day_132_runtime_note:
  known_status: active_current_day
  known_artifact_example: algebra-2-L132.pdf
  note:
    - Day 132 is already a live runtime checkpoint for Aiden and should remain easy to bind in School when available.

grading_artifacts:
- Daily Worksheet with show-work
- legible photo or scan allowed
- correction pass when CHECK_ONLY review identifies misses
- cumulative review / final artifacts later

notes:
- This shell is intentionally workflow-first so School can resume Aiden where he left off.
- Final open-text selection remains pending, but the runtime lane is usable now.
