# COURSE.Science.PhysicsLab.11

course_id: COURSE.Science.PhysicsLab.11
version: 0.9.0
status: DRAFT
updated: 2026-03-08

title: Physics w Lab
grade_level: 11
subject: Science
credit: 1.0
course_length_days: 180
semester_length_days: 90
block_length_days: 30

source_model:
  provider: Easy Peasy
  source_model_url: https://allinonehighschool.com/physics-with-lab-2018/
  source_model_role:
    - primary workflow source
    - day-by-day lesson and lab sequence
    - assignment anchor

textbook_spine:
  spine_status: pending_final_selection
  likely_open_spine_types:
    - open physics textbook
    - open lab/activity notes
    - Blu-made guided problem sets and lab check sheets
  notes:
    - An open physics spine should be chosen, but the course can run now from Easy Peasy sequence + captured lesson/lab sources + Blu-made checks.

school_runtime_defaults:
  class_mode: INTERNAL
  tutoring_mode: CHECK_ONLY
  expected_artifacts:
    - worked problems
    - screenshots/photos of diagrams
    - lab notes
    - quiz result screenshots
  completion_requires:
    - source-bound lesson or lab prompt
    - visible work artifact
    - source-grounded verification

daily_resolution_contract:
- Resolve `day_number` against the Easy Peasy source model first.
- Bind the current lesson page, lab page, quiz, or linked review source as needed.
- For source-dependent conceptual questions, School must not judge correctness without the relevant lesson or review source.
- Physics remains a proof-heavy CHECK_ONLY lane.

block_plan:
- block: 1
  days: 1-30
  focus: foundations, measurement, motion, setup of physics habits
- block: 2
  days: 31-60
  focus: forces, energy, work, and problem solving
- block: 3
  days: 61-90
  focus: waves, sound, light, and labs
- block: 4
  days: 91-120
  focus: electricity, magnetism, and related review
- block: 5
  days: 121-150
  focus: optics, mixed review, late-course problem solving
- block: 6
  days: 151-180
  focus: cumulative review, labs, final readiness

day_132_runtime_note:
  known_status: active_current_day
  known_artifact_examples:
    - physics lesson link
    - optics review link
    - quiz link
  note:
    - Day 132 already exposed the need for source-binding discipline in School, so this course should stay evidence-first.

grading_artifacts:
- worked problem sets
- diagram screenshots/photos
- lab proof
- quiz result screenshots
- corrected resubmission when needed

notes:
- This shell is built to prevent the old “Physics was already linked but forgot the source” failure mode.
