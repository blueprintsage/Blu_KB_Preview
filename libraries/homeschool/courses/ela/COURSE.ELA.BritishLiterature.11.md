# COURSE.ELA.BritishLiterature.11

course_id: COURSE.ELA.BritishLiterature.11
version: 0.9.0
status: DRAFT
updated: 2026-03-08

title: British Literature
grade_level: 11
subject: English
credit: 1.0
course_length_days: 180
semester_length_days: 90
block_length_days: 30

source_model:
  provider: Easy Peasy
  source_model_url: https://allinonehighschool.com/british-literature/
  source_model_role:
    - primary workflow source
    - day-by-day reading and response sequence
    - pacing anchor

textbook_spine:
  spine_status: pending_final_selection
  likely_open_spine_types:
    - public-domain primary texts
    - Blu-made reading guides and response packets
    - open literary criticism or context notes when approved later
  notes:
    - This course can run from source texts + teacher-made packets even before a single formal textbook spine is chosen.
    - Public-domain British literature sources are a likely long-term fit, but the exact canonical spine is still pending.

school_runtime_defaults:
  class_mode: INTERNAL
  tutoring_mode: NO_ANSWERING
  expected_artifacts:
    - written responses
    - paragraph answers
    - short analysis
    - reading notes
  completion_requires:
    - visible assignment prompt or source text section
    - student-authored response artifact
    - verification without ghostwriting

daily_resolution_contract:
- Resolve `day_number` against the Easy Peasy source model first.
- Bind the daily reading / prompt page when available.
- If the day depends on external reading, School should capture the source text or prompt fragment before checking.
- Because this course often uses open-ended writing, School must preserve `NO_ANSWERING` mode and avoid supplying final response content.

block_plan:
- block: 1
  days: 1-30
  focus: early foundations, reading habits, literary response structure
- block: 2
  days: 31-60
  focus: early British texts, comprehension, theme and form
- block: 3
  days: 61-90
  focus: analytical writing, historical context, interpretation
- block: 4
  days: 91-120
  focus: deeper literature study, comparison, evidence use
- block: 5
  days: 121-150
  focus: later texts, sustained response, review of argument quality
- block: 6
  days: 151-180
  focus: cumulative reading and writing mastery, final review

grading_artifacts:
- short-answer responses
- paragraph / essay responses
- reading notes
- revision check artifacts when required

guardrail_note:
- This course is one of the main reasons `NO_ANSWERING` exists in School.
- Verification must stay distinct from content-supply.

notes:
- Open-text and source-text decisions remain pending, but the workflow shell is ready for runtime use.
