# COURSE.History.ModernAmericanHistory.11

course_id: COURSE.History.ModernAmericanHistory.11
version: 0.9.0
status: DRAFT
updated: 2026-03-08

title: Modern American History
grade_level: 11
subject: History
credit: 1.0
course_length_days: 180
semester_length_days: 90
block_length_days: 30

source_model:
  provider: Easy Peasy
  source_model_url: https://allinonehighschool.com/modern-american-history/
  source_model_role:
    - primary workflow source
    - day-by-day history sequence
    - prompt and assignment anchor

textbook_spine:
  spine_status: pending_final_selection
  likely_open_spine_types:
    - open U.S. history textbook
    - open primary source packets
    - Blu-made guided notes and checks
  notes:
    - History can run from a blended spine: open survey text + primary source packets + Blu-made note sheets.
    - Exact open spine selection is still pending review.

school_runtime_defaults:
  class_mode: INTERNAL
  tutoring_mode: CHECK_ONLY
  expected_artifacts:
    - outlines
    - short written answers
    - notes
    - timeline / concept summaries
  completion_requires:
    - visible source or prompt
    - student-produced artifact
    - source-grounded review

daily_resolution_contract:
- Resolve `day_number` against the Easy Peasy source model first.
- Bind the daily history page or assignment prompt when available.
- If the daily item relies on linked readings, capture enough of the reading/prompt to verify the student’s work honestly.
- School should remain in CHECK_ONLY mode unless a different block mode is explicitly set.

block_plan:
- block: 1
  days: 1-30
  focus: course setup, background review, early modern American framing
- block: 2
  days: 31-60
  focus: national development, conflict, institutions, and social change
- block: 3
  days: 61-90
  focus: industrialization, reform, foreign policy, and transition
- block: 4
  days: 91-120
  focus: major twentieth-century turning points
- block: 5
  days: 121-150
  focus: late modern period, policy, culture, and contemporary interpretation
- block: 6
  days: 151-180
  focus: synthesis, review, cumulative mastery

grading_artifacts:
- outlines
- short-response sets
- note pages
- map/timeline or concept artifacts when assigned

notes:
- This shell is workflow-ready even before the final open history spine is selected.
