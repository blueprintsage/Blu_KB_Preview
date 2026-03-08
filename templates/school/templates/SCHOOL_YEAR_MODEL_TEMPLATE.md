# SCHOOL_YEAR_MODEL — Template

record_id: SCHOOL.YEAR.MODEL
version: 0.9.0
status: DRAFT
purpose: Canonical school-year calendar and pacing model for PROGRAM.School and Time Service.

ownership:
- This file defines the instructional calendar model.
- PROGRAM.School reads this file to determine day progression, attendance effects, and pacing windows.
- Time Service may use this file to resolve current instructional day, block, semester, and scheduled class windows.
- Parent-authorized actions may modify protected fields.

school_year:
  label: <yyyy-yyyy>
  timezone: America/Chicago
  start_date: <YYYY-MM-DD>
  end_date: <YYYY-MM-DD>
  instructional_days_total: 180

term_model:
  semesters_total: 2
  semester_length_days: 90
  blocks_total: 6
  block_length_days: 30

term_layout:
  - semester: 1
    block: 1
    instructional_day_range: 1-30
  - semester: 1
    block: 2
    instructional_day_range: 31-60
  - semester: 1
    block: 3
    instructional_day_range: 61-90
  - semester: 2
    block: 4
    instructional_day_range: 91-120
  - semester: 2
    block: 5
    instructional_day_range: 121-150
  - semester: 2
    block: 6
    instructional_day_range: 151-180

week_model:
  school_days_per_week: 5
  active_days:
    - Mon
    - Tue
    - Wed
    - Thu
    - Fri
  inactive_days:
    - Sat
    - Sun

daily_time_model:
  start_time_local: "08:00"
  class_minutes_default: 50
  class_minutes_min: 45
  break_minutes_default: 10
  lunch_minutes_default: 30
  transition_buffer_minutes: 5

attendance_status_allowed:
- PRESENT
- SICK_EXCUSED
- ABSENT_UNEXCUSED
- HOLIDAY
- FIELD_TRIP
- MAKEUP

attendance_rules:
- PRESENT may advance instructional day when the day is completed.
- SICK_EXCUSED does not advance instructional day by default.
- HOLIDAY does not advance instructional day.
- FIELD_TRIP may advance instructional day if instructional credit is granted.
- MAKEUP may advance instructional day only when actual instruction occurs.
- ABSENT_UNEXCUSED does not advance instructional day by default.

non_instructional_dates:
  holidays:
    - date: <YYYY-MM-DD>
      label: <holiday_name>
  breaks:
    - start_date: <YYYY-MM-DD>
      end_date: <YYYY-MM-DD>
      label: <break_name>
  teacher_workdays:
    - date: <YYYY-MM-DD>
      label: <optional>

makeup_policy:
  enabled: true
  allow_makeup_days: true
  auto_extend_year_if_needed: false
  max_makeup_days: <optional>
  notes:
    - <optional>

current_state_defaults:
  current_instructional_day: 1
  current_semester: 1
  current_block: 1

time_resolution_rules:
- Current instructional day is based on completed instructional days, not just wall-calendar dates.
- Non-instructional dates do not consume instructional-day count.
- Semester and block are derived from current instructional day.
- Date rollover should be computed in the configured timezone.
- If attendance status prevents advancement, the instructional day remains unchanged.

class_schedule_defaults:
  block_slots:
    - slot: 1
      start_time_local: "08:00"
      end_time_local: "08:50"
    - slot: 2
      start_time_local: "09:00"
      end_time_local: "09:50"
    - slot: 3
      start_time_local: "10:00"
      end_time_local: "10:50"
    - slot: 4
      start_time_local: "11:00"
      end_time_local: "11:50"
    - slot: lunch
      start_time_local: "12:00"
      end_time_local: "12:30"
    - slot: 5
      start_time_local: "12:40"
      end_time_local: "13:30"
    - slot: 6
      start_time_local: "13:40"
      end_time_local: "14:30"

protected_fields:
- school_year.start_date
- school_year.end_date
- school_year.instructional_days_total
- term_model.*
- week_model.*
- attendance_rules
- non_instructional_dates
- makeup_policy

future_expansion:
- half-days
- rotating elective schedules
- semester-specific schedules
- co-op / outside class days
- family-specific alternate calendars
- per-student schedule variants

guardrails:
- This file defines calendar truth; it does not store student runtime state.
- This file does not store authoritative grades.
- Student day progression should be recorded in the student school record, using this model as calendar law.