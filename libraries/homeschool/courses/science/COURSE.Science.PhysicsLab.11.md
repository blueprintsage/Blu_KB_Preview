# COURSE.Science.PhysicsLab.11

course_id: COURSE.Science.PhysicsLab.11
version: 0.9.1
status: DRAFT
updated: 2026-03-08

title: Physics w Lab
grade_level: 11
subject: Science
credit: 1.0
course_length_days: 180
semester_length_days: 90
block_length_days: 30
packet_mode: TEXTBOOK-SPINED

source_model:
  provider: Easy Peasy
  source_model_url: https://allinonehighschool.com/physics-with-lab-2018/
  source_model_role:
    - primary workflow source
    - day-by-day lesson and lab sequence
    - assignment anchor

textbook_spine:
  primary:
    - TX.SCI.PHYSICS.OPENSTAX.001
    - TX.SCI.PHYSICSLAB.OPENSTAX.002

packet_support:
  sourcebook_ref: libraries/homeschool/packets/science/COURSE.Science.PhysicsLab.11.SOURCEBOOK.md
  workbook_ref: libraries/homeschool/packets/science/COURSE.Science.PhysicsLab.11.WORKBOOK.md
  check_key_ref: libraries/homeschool/packets/science/COURSE.Science.PhysicsLab.11.CHECK_KEY.md
  packet_role:
    - clarify concept-heavy review days
    - support diagram interpretation
    - enforce honest source-bound verification

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

day_resolution_priority:
- First try the Easy Peasy day source for the current instructional day.
- Bind the related textbook/lab material when available.
- If the day has a wired packet checkpoint, bind packet materials for that day as a support bundle.
- Physics concept questions must not be judged without the relevant lesson/review source when the answer depends on it.

daily_resolution_contract:
- Resolve `day_number` against the Easy Peasy source model first.
- Bind the current lesson page, lab page, quiz, or linked review source as needed.
- If the day is packet-wired, bind:
  - sourcebook_ref
  - workbook_ref
  - check_key_ref
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

wired_day_checkpoints:
- day_number: 132
  packetized: true
  packet_bundle:
    - libraries/homeschool/packets/science/COURSE.Science.PhysicsLab.11.SOURCEBOOK.md
    - libraries/homeschool/packets/science/COURSE.Science.PhysicsLab.11.WORKBOOK.md
    - libraries/homeschool/packets/science/COURSE.Science.PhysicsLab.11.CHECK_KEY.md
  lesson_title: Optics Mixed Review + Verification Checkpoint
  source_binding_order:
    1. Easy Peasy lesson/review source if available
    2. linked review source or quiz source
    3. packet workbook
    4. packet sourcebook
    5. packet check key for teacher review only
  evidence_required:
    - visible prompt or review page
    - visible diagram/work
    - short explanation where the question is conceptual
  completion_gate:
    - do not mark COMPLETE without source-bound verification for concept-dependent tasks
    - missing source or missing diagram may force DEFERRED
  gradebook_title: Physics w Lab Block 5 — Day 132 Optics Verification Checkpoint

notes:
- This shell is explicitly wired to prevent the prior physics source-forgetting failure mode.
