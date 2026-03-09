# COURSE.Math.Algebra2.11

course_id: COURSE.Math.Algebra2.11
version: 0.9.1
status: DRAFT
updated: 2026-03-08

title: Algebra 2
grade_level: 11
subject: Math
credit: 1.0
course_length_days: 180
semester_length_days: 90
block_length_days: 30
packet_mode: HYBRID

source_model:
  provider: Easy Peasy
  source_model_url: https://allinonehighschool.com/algebra-2-new/
  source_model_role:
    - primary workflow source
    - day-by-day progression model
    - assignment sequence anchor

textbook_spine:
  primary:
    - TX.MATH.A2.CK12.001
  supplemental:
    - TX.MATH.INTERMEDIATE.OPENSTAX.001

packet_support:
  sourcebook_ref: libraries/homeschool/packets/math/COURSE.Math.Algebra2.11.SOURCEBOOK.md
  workbook_ref: libraries/homeschool/packets/math/COURSE.Math.Algebra2.11.WORKBOOK.md
  check_key_ref: libraries/homeschool/packets/math/COURSE.Math.Algebra2.11.CHECK_KEY.md
  packet_role:
    - fill gaps when source model is thin
    - provide original instructional support
    - provide checkable worksheet artifacts
    - provide day-132 live checkpoint support

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

day_resolution_priority:
- First try the Easy Peasy day source for the current instructional day.
- If the day has a wired packet checkpoint, bind packet materials for that day as the active source bundle.
- If the Easy Peasy source is inaccessible or too thin, use packet materials plus approved textbook support.
- School must name exactly which artifact is required before allowing completion.

daily_resolution_contract:
- Resolve `day_number` against the Easy Peasy source model first.
- If a direct daily worksheet, PDF, or assignment page is available, bind it as the current source.
- If the day is packet-wired, bind:
  - sourcebook_ref
  - workbook_ref
  - check_key_ref
- If the Easy Peasy daily item is inaccessible or thin, use the current course objective plus Blu-made original Algebra 2 practice aligned to the packet/textbook support.
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

wired_day_checkpoints:
- day_number: 132
  packetized: true
  packet_bundle:
    - libraries/homeschool/packets/math/COURSE.Math.Algebra2.11.SOURCEBOOK.md
    - libraries/homeschool/packets/math/COURSE.Math.Algebra2.11.WORKBOOK.md
    - libraries/homeschool/packets/math/COURSE.Math.Algebra2.11.CHECK_KEY.md
  lesson_title: Mixed Review II — quadratics, rational expressions, radicals
  source_binding_order:
    1. Easy Peasy day source if available
    2. packet workbook
    3. packet sourcebook
    4. packet check key for verification only
  evidence_required:
    - visible work for all assigned problems
    - restrictions shown for rational problems
    - check shown for radical equation
  completion_gate:
    - do not mark COMPLETE without a visible work artifact
    - answer-only work may be DEFERRED if verification steps are missing
  gradebook_title: Algebra 2 Block 5 — Day 132 Mixed Review

notes:
- This shell is wired for live School use.
- The day-132 packet checkpoint should make `/class start Algebra 2` materially more usable immediately.
