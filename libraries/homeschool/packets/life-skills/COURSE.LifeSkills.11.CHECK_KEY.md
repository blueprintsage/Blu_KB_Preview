# COURSE.LifeSkills.11.CHECK_KEY

course_id: COURSE.LifeSkills.11
packet_file: CHECK_KEY
version: 0.9.0
status: DRAFT
updated: 2026-03-08
packet_mode: PACKET-SPINED
grade_level: 11
subject: Life Skills
focus_window: Block 5 (Days 121-150) first-pass build
purpose: Teacher/check key for Life Skills guided-practice days.

grading_mode_defaults:
- tutoring_mode: GUIDED_PRACTICE
- objective_workflow: mixed
- proof_required: yes
- reflection_only_completion: no

completion_rules:
- COMPLETE requires:
  - visible task artifact
  - enough specificity to show the task was actually done
  - no major missing component for the day
- DEFERRED if:
  - the artifact is missing
  - the plan/task is too vague to use
  - the student has clearly started but not finished
- REVIEW_REQUIRED if:
  - the artifact exists but is too thin or unrealistic to judge honestly
  - the student appears to have filled the sheet without engaging the task seriously

## Day 132 Check Guide

day_number: 132
lesson_title: Weekly Planning + Time-Blocking Checkpoint

required_parts:
- weekly planning sheet
- one time-blocked day
- one conflict/backup note
- one short reflection

rubric_dimensions:
- realism
- completeness
- usability
- follow-through awareness
- clarity

realism:
- strong:
  - the plan looks like a real week, not a fantasy schedule
- partial:
  - mostly real, but too full or too vague in places
- weak:
  - unrealistic, empty, or not connected to actual obligations

completeness:
- strong:
  - all required parts are present
- partial:
  - one part is thin or incomplete
- weak:
  - multiple required parts are missing

usability:
- strong:
  - the student could actually use this plan tomorrow
- partial:
  - useful in places, but needs tightening
- weak:
  - too vague to function

follow_through_awareness:
- strong:
  - the student identified a real likely failure point and a believable backup plan
- partial:
  - risk or backup is present but weak
- weak:
  - no real awareness of what could go wrong

clarity:
- strong:
  - readable and understandable
- partial:
  - understandable but messy
- weak:
  - hard to interpret

feedback_templates:
- strong:
  - "This is usable. The plan looks real, and the backup thinking shows you’re actually preparing for the week."
- too_vague:
  - "The sheet is filled in, but it is still too vague to be useful. Make the tasks and time blocks more specific."
- unrealistic:
  - "This looks more ideal than real. Tighten it until it matches what your week can actually hold."
- missing_proof:
  - "I still need the actual planning artifact before I can mark this complete."
- weak_backup:
  - "You identified a possible problem, but the backup plan still needs to be more concrete."

grading_guidance:
- complete_and_usable:
  - FINAL
- complete_but_needs_tightening:
  - FINAL with notes or correction suggestion
- too_thin_to_use:
  - DEFERRED
- not honestly reviewable:
  - REVIEW_REQUIRED

gradebook_write_template:
- course_id: COURSE.LifeSkills.11
- title: Life Skills Block 5 — Day 132 Weekly Planning Checkpoint
- entry_type: ASSIGNMENT
- grading_basis: mixed
- status: FINAL only when the artifact is usable and reviewable
- notes:
  - include strongest dimension
  - include weakest dimension
  - include whether a revision pass was advised

notes:
- This key is for guided-practice review, not for fake box-checking.
- School should use it to block completion when the student submits a plan that is too vague to function.
