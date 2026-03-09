# COURSE.LifeSkills.11

course_id: COURSE.LifeSkills.11
version: 0.9.1
status: DRAFT
updated: 2026-03-08

title: Life Skills
grade_level: 11
subject: Life Skills
credit: 1.0
course_length_days: 180
semester_length_days: 90
block_length_days: 30
packet_mode: PACKET-SPINED

source_model:
  provider: Custom
  source_model_url: none
  source_model_role:
    - Blu/parent-shaped custom course
    - project and checklist driven
    - not tied to Easy Peasy

textbook_spine:
  primary:
    - TX.LIFESKILLS.CUSTOM.001

packet_support:
  sourcebook_ref: libraries/homeschool/packets/life-skills/COURSE.LifeSkills.11.SOURCEBOOK.md
  workbook_ref: libraries/homeschool/packets/life-skills/COURSE.LifeSkills.11.WORKBOOK.md
  check_key_ref: libraries/homeschool/packets/life-skills/COURSE.LifeSkills.11.CHECK_KEY.md
  packet_role:
    - primary instructional spine
    - guided-practice tasks
    - proof-based completion support

school_runtime_defaults:
  class_mode: INTERNAL
  tutoring_mode: GUIDED_PRACTICE
  expected_artifacts:
    - checklists
    - short reflections
    - planning sheets
    - practical proof artifacts
  completion_requires:
    - visible task or prompt
    - student-produced artifact or demonstrated completion proof
    - guided-practice review

day_resolution_priority:
- Life Skills does not resolve from Easy Peasy.
- Resolve the current instructional day from the custom block plan and wired packet checkpoints.
- Bind packet materials as the active source bundle for packetized days.
- School must require a visible practical artifact, not just a statement that the task was done.

daily_resolution_contract:
- Life Skills does not resolve from Easy Peasy.
- Resolve `day_number` from the custom block/unit plan below.
- Bind:
  - sourcebook_ref
  - workbook_ref
  - check_key_ref
- Each day should bind a task prompt, checklist, worksheet, or practical assignment artifact.
- School should keep this lane in GUIDED_PRACTICE unless a more specific mode is declared.

block_plan:
- block: 1
  days: 1-30
  focus: personal systems
  themes:
    - calendar use
    - task planning
    - daily routines
    - self-management
- block: 2
  days: 31-60
  focus: home and self-care
  themes:
    - laundry
    - cleaning
    - food basics
    - health / appointment habits
- block: 3
  days: 61-90
  focus: money and consumer life
  themes:
    - budgeting
    - banking basics
    - comparing prices
    - bills and subscriptions
- block: 4
  days: 91-120
  focus: communication and citizenship
  themes:
    - email / phone etiquette
    - form filling
    - basic civics
    - respectful disagreement
- block: 5
  days: 121-150
  focus: work and digital life
  themes:
    - resumes
    - interviews
    - online accounts
    - digital safety
- block: 6
  days: 151-180
  focus: independence capstone
  themes:
    - planning a week
    - planning a budget
    - solving common life problems
    - adulting simulation tasks

wired_day_checkpoints:
- day_number: 132
  packetized: true
  packet_bundle:
    - libraries/homeschool/packets/life-skills/COURSE.LifeSkills.11.SOURCEBOOK.md
    - libraries/homeschool/packets/life-skills/COURSE.LifeSkills.11.WORKBOOK.md
    - libraries/homeschool/packets/life-skills/COURSE.LifeSkills.11.CHECK_KEY.md
  lesson_title: Weekly Planning + Time-Blocking Checkpoint
  source_binding_order:
    1. packet workbook
    2. packet sourcebook
    3. packet check key for teacher review only
  evidence_required:
    - completed weekly plan
    - one time-blocked day
    - one conflict/backup note
    - short reflection tied to the real plan
  completion_gate:
    - do not mark COMPLETE without a usable plan artifact
    - vague or unusable plans may be DEFERRED or REVIEW_REQUIRED
  gradebook_title: Life Skills Block 5 — Day 132 Weekly Planning Checkpoint

notes:
- This shell is wired to make Life Skills practical and checkable instead of vague.
