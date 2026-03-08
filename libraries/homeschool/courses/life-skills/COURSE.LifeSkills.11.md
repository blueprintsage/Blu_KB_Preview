# COURSE.LifeSkills.11

course_id: COURSE.LifeSkills.11
version: 0.9.0
status: DRAFT
updated: 2026-03-08

title: Life Skills
grade_level: 11
subject: Life Skills
credit: 1.0
course_length_days: 180
semester_length_days: 90
block_length_days: 30

source_model:
  provider: Custom
  source_model_url: none
  source_model_role:
    - Blu/parent-shaped custom course
    - project and checklist driven
    - not tied to Easy Peasy

textbook_spine:
  spine_status: custom_course_pending
  likely_open_spine_types:
    - open personal finance material
    - open civics / consumer materials
    - original Blu-made packets, checklists, and guided practice
  notes:
    - This course needs its own curated open-source packet set.
    - It is intentionally high-school focused in this first pass.

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

daily_resolution_contract:
- Life Skills does not resolve from Easy Peasy.
- Resolve `day_number` from the custom block/unit plan below.
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

grading_artifacts:
- completed checklists
- planning sheets
- screenshots/photos of completed practical tasks when appropriate
- short reflections
- teacher/parent verification note where needed

notes:
- This is the one intentionally custom Aiden course in the first-pass internal curriculum.
- Once stabilized, it can become the model for a broader high-school Life Skills spine.
