# Student_School_Record

record_id: SCHOOL.STUDENT.RECORD
version: 0.9.0
status: DRAFT
purpose: Single-file student startup and live school-day record for PROGRAM.School.

startup_rule:
- SCHOOL start requires this file only.
- Parent controls use `Parent_GOD_Mode_Key.md` separately.
- Authoritative grades do not live here.

ownership:
- PROGRAM.School uses this as the canonical student runtime record.
- Time Service may update date/day/block/semester fields.
- Memory may mirror active state, but this file remains the durable source.
- Students may use this record during school flow.
- Protected fields must require parent authorization to change.

student:
  name: <student_name>
  student_id: <student_id>
  grade_level: <grade_or_band>
  timezone: America/Chicago
  school_year: <yyyy-yyyy>

calendar_model:
  year_total_days: 180
  semester_total: 2
  semester_length_days: 90
  block_total: 6
  block_length_days: 30

calendar_state:
  day_number: 1
  current_semester: 1
  current_block: 1
  last_instructional_date: <YYYY-MM-DD>
  last_tick_iso: <ISO-8601+offset>
  attendance_today: PRESENT
  attendance_history:
    - date: <YYYY-MM-DD>
      status: PRESENT
      note: <optional>

attendance_status_allowed:
- PRESENT
- SICK_EXCUSED
- ABSENT_UNEXCUSED
- HOLIDAY
- FIELD_TRIP
- MAKEUP

attendance_rules:
- PRESENT advances instructional day when the day is completed.
- SICK_EXCUSED does not advance instructional day by default.
- HOLIDAY does not advance instructional day.
- MAKEUP advances instructional day only if instruction actually occurs.
- Attendance overrides require parent authorization.

schedule_defaults:
  school_days_per_week: 5
  start_time_local: "08:00"
  class_minutes_default: 50
  class_minutes_min: 45
  break_minutes_default: 10
  lunch_minutes_default: 30
  transition_buffer_minutes: 5

daily_schedule:
  enabled: true
  blocks:
    - slot: 1
      start_time_local: "08:00"
      end_time_local: "08:50"
      kind: class
      course_id: <course_id>
    - slot: 2
      start_time_local: "09:00"
      end_time_local: "09:50"
      kind: class
      course_id: <course_id>

course_load:
  active_courses:
    - course_id: <course_id>
      subject: <subject>
      title: <course_title>
      status: ACTIVE
      course_length_days: 180
      current_course_day: 1
      current_unit: <optional>
      source_model_url: <optional>
      replacement_texts:
        - <optional>
    - course_id: <course_id>
      subject: <subject>
      title: <course_title>
      status: INACTIVE
      course_length_days: 90
      current_course_day: 0

course_status_allowed:
- ACTIVE
- INACTIVE
- PAUSED
- COMPLETE
- DROPPED

today_state:
  session_status: READY
  day_focus: <optional>
  notes: <optional>
  unresolved_flags:
    - <optional>

session_status_allowed:
- READY
- RUNNING
- PAUSED
- COMPLETE
- ABORTED

block_state_machine:
  allowed_status:
  - NOT_STARTED
  - ACTIVE
  - COMPLETE
  - SKIPPED
  - INACTIVE
  - DEFERRED

  blocks_today:
    - block_id: <unique_block_id>
      slot: 1
      subject: <subject>
      course_id: <course_id>
      title: <course_title>
      status: NOT_STARTED
      tutoring_mode: CHECK_ONLY
      source_ids: []
      evidence_ids: []
      completion_notes: <optional>
      unresolved_risks: []
    - block_id: <unique_block_id>
      slot: 2
      subject: <subject>
      course_id: <course_id>
      title: <course_title>
      status: NOT_STARTED
      tutoring_mode: EXPLAIN
      source_ids: []
      evidence_ids: []
      completion_notes: <optional>
      unresolved_risks: []

tutoring_modes_allowed:
- EXPLAIN
- CHECK_ONLY
- NO_ANSWERING
- GUIDED_PRACTICE
- REVIEW

guardrails:
- CHECK_ONLY means verify the student's work without supplying answer content.
- NO_ANSWERING means do not provide final answers or ghostwrite responses.
- If user constraints conflict with assistant behavior, the block must pause and surface a warning.
- A block must not be marked COMPLETE without required evidence.

source_registry:
  sources:
    - source_id: <source_id>
      block_id: <block_id>
      type: pdf
      label: <human_label>
      location: <url_or_file_name>
      status: BOUND
      notes: <optional>

source_status_allowed:
- BOUND
- PENDING
- INACCESSIBLE
- SUPERSEDED

evidence_ledger:
  evidence_items:
    - evidence_id: <evidence_id>
      block_id: <block_id>
      type: pasted_answers
      received_at_iso: <ISO-8601+offset>
      source_ref: <source_id_or_note>
      summary: <short_description>

completion_rules:
- Completion is block-scoped.
- Completion requires bound source(s) when source-based verification is needed.
- Completion requires evidence when the assignment expects proof.
- Completion may remain DEFERRED if source access fails or answers remain unverified.

runtime_memory_mirror:
  active_course_id: <optional>
  active_block_id: <optional>
  active_source_ids: []
  last_action: <optional>

protected_fields:
- calendar_state.day_number
- calendar_state.attendance_today
- calendar_state.attendance_history
- course_load.active_courses[*].status
- block_state_machine.blocks_today[*].status when setting COMPLETE, SKIPPED, or DEFERRED
- any override note that changes instructional truth

student_visible_fields:
- daily_schedule
- course_load
- today_state
- block_state_machine.blocks_today
- source_registry
- evidence_ledger summaries
- feedback and completion notes

not_stored_here:
- authoritative final grades
- parent secrets or auth material
- full textbook bodies
- full assignment archives beyond needed references

migration_note:
- This replaces multi-capsule startup for daily school use.
- Student should not need a separate overlay file to begin school.