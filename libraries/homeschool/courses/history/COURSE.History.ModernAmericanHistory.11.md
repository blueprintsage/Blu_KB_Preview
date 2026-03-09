# COURSE.History.ModernAmericanHistory.11

course_id: COURSE.History.ModernAmericanHistory.11
version: 0.9.1
status: DRAFT
updated: 2026-03-08

title: Modern American History
grade_level: 11
subject: History
credit: 1.0
course_length_days: 180
semester_length_days: 90
block_length_days: 30
packet_mode: HYBRID

source_model:
  provider: Easy Peasy
  source_model_url: https://allinonehighschool.com/modern-american-history/
  source_model_role:
    - primary workflow source
    - day-by-day history sequence
    - prompt and assignment anchor

textbook_spine:
  supplemental:
    - TX.HIST.USHIST.COREKNOWLEDGE.001

packet_support:
  sourcebook_ref: libraries/homeschool/packets/history/COURSE.History.ModernAmericanHistory.11.SOURCEBOOK.md
  workbook_ref: libraries/homeschool/packets/history/COURSE.History.ModernAmericanHistory.11.WORKBOOK.md
  check_key_ref: libraries/homeschool/packets/history/COURSE.History.ModernAmericanHistory.11.CHECK_KEY.md
  packet_role:
    - guided note support
    - response structure support
    - verification support for subjective short responses

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

day_resolution_priority:
- First try the Easy Peasy day source for the current instructional day.
- If the day has a wired packet checkpoint, bind packet materials as the active support bundle.
- If the daily item relies on linked readings, capture enough of the reading/prompt to verify the student's work honestly.
- School must remain in CHECK_ONLY unless a different block mode is explicitly set.

daily_resolution_contract:
- Resolve `day_number` against the Easy Peasy source model first.
- Bind the daily history page or assignment prompt when available.
- If the day is packet-wired, bind:
  - sourcebook_ref
  - workbook_ref
  - check_key_ref
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

wired_day_checkpoints:
- day_number: 132
  packetized: true
  packet_bundle:
    - libraries/homeschool/packets/history/COURSE.History.ModernAmericanHistory.11.SOURCEBOOK.md
    - libraries/homeschool/packets/history/COURSE.History.ModernAmericanHistory.11.WORKBOOK.md
    - libraries/homeschool/packets/history/COURSE.History.ModernAmericanHistory.11.CHECK_KEY.md
  lesson_title: Mixed Response Practice II — cause, consequence, significance
  source_binding_order:
    1. Easy Peasy day source if available
    2. visible prompt or reading source
    3. packet workbook
    4. packet sourcebook
    5. packet check key for teacher review only
  evidence_required:
    - visible prompt or copied prompt text
    - student-authored response
    - enough writing to judge claim, evidence, and historical reasoning
  completion_gate:
    - do not mark COMPLETE without a visible response artifact
    - vague or too-thin work may be DEFERRED or REVIEW_REQUIRED
  gradebook_title: Modern American History Block 5 — Day 132 Mixed Response Practice II

notes:
- This shell is wired to keep history responses verifiable instead of broadly “looks okay.”
