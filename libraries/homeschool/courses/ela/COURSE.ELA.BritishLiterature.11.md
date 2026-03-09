# COURSE.ELA.BritishLiterature.11

course_id: COURSE.ELA.BritishLiterature.11
version: 0.9.1
status: DRAFT
updated: 2026-03-08

title: British Literature
grade_level: 11
subject: English
credit: 1.0
course_length_days: 180
semester_length_days: 90
block_length_days: 30
packet_mode: PACKET-SPINED

source_model:
  provider: Easy Peasy
  source_model_url: https://allinonehighschool.com/british-literature/
  source_model_role:
    - primary workflow source
    - day-by-day reading and response sequence
    - pacing anchor

textbook_spine:
  primary:
    - TX.ELA.BRITLIT.PUBLICDOMAIN.001

packet_support:
  sourcebook_ref: libraries/homeschool/packets/ela/COURSE.ELA.BritishLiterature.11.SOURCEBOOK.md
  workbook_ref: libraries/homeschool/packets/ela/COURSE.ELA.BritishLiterature.11.WORKBOOK.md
  check_key_ref: libraries/homeschool/packets/ela/COURSE.ELA.BritishLiterature.11.CHECK_KEY.md
  packet_role:
    - primary instructional support
    - response structure support
    - originality-preserving check support

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

day_resolution_priority:
- First try the Easy Peasy day source for the current instructional day.
- If the day has a wired packet checkpoint, bind packet materials as the active support bundle.
- If the daily item relies on outside reading, capture the source text section or prompt before checking.
- School must preserve NO_ANSWERING and never convert packet support into ghostwriting.

daily_resolution_contract:
- Resolve `day_number` against the Easy Peasy source model first.
- Bind the daily reading / prompt page when available.
- If the day is packet-wired, bind:
  - sourcebook_ref
  - workbook_ref
  - check_key_ref
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

wired_day_checkpoints:
- day_number: 132
  packetized: true
  packet_bundle:
    - libraries/homeschool/packets/ela/COURSE.ELA.BritishLiterature.11.SOURCEBOOK.md
    - libraries/homeschool/packets/ela/COURSE.ELA.BritishLiterature.11.WORKBOOK.md
    - libraries/homeschool/packets/ela/COURSE.ELA.BritishLiterature.11.CHECK_KEY.md
  lesson_title: Mixed Response Practice II — evidence, explanation, revision
  source_binding_order:
    1. Easy Peasy day source if available
    2. visible reading/prompt
    3. packet workbook
    4. packet sourcebook
    5. packet check key for teacher review only
  evidence_required:
    - visible prompt or copied prompt text
    - student-authored response
    - enough writing to judge claim, evidence, and reasoning
  completion_gate:
    - do not mark COMPLETE without a student-authored response artifact
    - thin or vague responses may be DEFERRED or REVIEW_REQUIRED
  gradebook_title: British Literature Block 5 — Day 132 Mixed Response Practice II

notes:
- This shell is wired to preserve the literature guardrail that the system previously violated.
