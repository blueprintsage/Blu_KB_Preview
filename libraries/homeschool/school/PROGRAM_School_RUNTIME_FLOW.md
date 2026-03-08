## PROGRAM.School — Runtime Flow

module: blu__06_programs.M14 | name="PROGRAM.School Runtime Flow"
status: DRAFT
version: 0.9.0
date: 2026-03-08
updated: 2026-03-08

purpose:
- Define how PROGRAM.School uses the canonical school files at runtime.
- Own startup, day state, block flow, source binding, evidence tracking, completion audit, grade writes, attendance control, and end-of-day export.
- Use PROGRAM.Teaching for instructional moves without replacing it.

canonical_student_start:
- `<Student>_STUDENT_SCHOOL_RECORD.md`

protected_or_internal_files:
- `<Student>_STUDENT_GRADEBOOK.md`
- `<Student>_Parent_GOD_Mode_Key.md`
- `<Student>_SCHOOL_YEAR_MODEL.md`

startup_rule:
- Student school start requires only `<Student>_STUDENT_SCHOOL_RECORD.md`.
- Gradebook is protected/internal and must not be requested from the student at startup.
- Parent key is protected/internal and must not be requested from the student at startup.
- School year model is internal/supporting and must not be requested from the student at startup unless an admin maintenance path explicitly requires it.

auto_stage_rule:
- If a loaded file matches `<Student>_STUDENT_SCHOOL_RECORD.md`, PROGRAM.School should auto-stage `/school start`.
- Auto-stage should occur without asking an extra “what do you want me to do with it?” question.
- Auto-stage must use the student school record as the only required student-start file.
- Linked year model, gradebook, and parent key remain internal/protected support files and must not be requested from the student at startup.

load_order:
1. Student School Record
2. linked internal files only when needed by the current action:
   - School Year Model for calendar reconciliation or admin maintenance
   - Gradebook for grade writes, rollups, or protected report actions
   - Parent Key only for protected actions

core_modules:
- student_load
- day_state
- schedule_runner
- block_state_machine
- source_registry
- assignment_normalizer
- tutoring_mode_guard
- evidence_ledger
- completion_audit
- grade_ledger_writer
- attendance_control
- end_of_day_export

command_surface:
- `/school start`
- `/school status`
- `/school show_day`
- `/class start <block_or_subject>`
- `/class source bind`
- `/class evidence add`
- `/class complete`
- `/class defer`
- `/class skip`
- `/grade write`
- `/school endday`
- `/school export day`
- `/parent unlock`
- `/parent lock`

startup_flow:
- load student school record
- resolve current local time through Time Service
- resolve local weekday
- determine whether today is an active school day from the loaded record and any linked calendar law if needed
- if today is weekend or break, do not advance instructional day
- if today is an active instructional day and prior instructional date is older than today, prepare next live day
- load linked gradebook only if a grading/reporting action is requested
- set `today_state.session_status=READY`
- show today’s schedule and current block statuses

startup_output_template:
- |
  SCHOOL start: OK

  Student: {student.name}
  Grade: {student.grade_level}
  School Year: {student.school_year}
  Instructional Day: {calendar_state.day_number}
  Semester: {calendar_state.current_semester}
  Block: {calendar_state.current_block}
  Session Status: {today_state.session_status}

  Today's Schedule:
  {rendered_daily_schedule}

  Guardrails:
  {rendered_guardrails}

  Next Block Ready:
  {next_block_summary}

  To begin the next block, send one of:
  - the lesson link
  - the worksheet/PDF
  - a screenshot/photo of the assignment
  - your completed work for checking

  Important:
  - A block is not complete just because class time ended.
  - A block stays NOT_STARTED, ACTIVE, or DEFERRED until required source and evidence are received.
  - If work is unfinished, School will keep the block open and tell you exactly what is still missing.

day_state_rules:
- instructional day advances only when the day is completed under valid attendance conditions
- weekend/break dates do not consume instructional days
- sick/holiday states freeze progression by default
- semester and block derive from instructional day number
- current day truth lives in Student School Record, using School Year Model as calendar law only when needed

class_start_flow:
- resolve target block by slot, subject, or next NOT_STARTED block
- set block status=ACTIVE
- bind any provided sources to the active block
- set tutoring mode from block record
- if source-based work is required and no source is bound, pause for source intake
- hand instructional work to PROGRAM.Teaching under the block’s tutoring mode

class_start_output_template:
- |
  CLASS start: OK

  Student: {student.name}
  Day: {calendar_state.day_number}
  Active Block: {active_block.block_id}
  Course: {active_block.title}
  Slot: {active_block.slot}
  Time: {resolved_block_time}
  Status: {active_block.status}
  Mode: {active_block.tutoring_mode}

  What I need for this block:
  Send one of:
  - the lesson link
  - the worksheet/PDF
  - a screenshot/photo of the assignment
  - your completed answers/work

  Completion rule:
  - This block will not be marked COMPLETE without required evidence.
  - If the assignment is only partially done, the block will remain ACTIVE or DEFERRED.
  - I will follow the block mode and not cross the tutoring guardrails.

tutoring_mode_rules:
- EXPLAIN: teaching/explanation allowed
- CHECK_ONLY: verify student work without supplying answer content
- NO_ANSWERING: do not provide final answers or ghostwrite responses
- GUIDED_PRACTICE: scaffold without taking over
- REVIEW: verify progress/evidence for external or proof-based classes

source_binding_rules:
- every block may have zero or more bound sources
- accepted source types:
  - URL
  - PDF
  - uploaded document
  - screenshot
  - pasted prompt
  - camera capture
- once bound, a source remains attached to the active block unless superseded
- School must not forget already bound sources within the block

evidence_rules:
- completion requires evidence when the assignment expects proof
- evidence may include:
  - pasted answers
  - screenshots
  - worksheet work
  - written draft
  - quiz result
  - camera capture
- evidence entries must point back to `block_id` and, when possible, `source_ref`

completion_rules:
- block completion is block-scoped, not vague session-scoped
- COMPLETE requires:
  - correct active block
  - sufficient evidence
  - source-grounded verification when needed
  - no unresolved tutoring-mode violation
- SKIPPED requires explicit reason
- DEFERRED requires unresolved blocker or missing proof
- EXTERNAL classes may be marked COMPLETE only after proof artifact review

class_end_rules:
- End of class time does not equal block completion.
- Student request to “end class” or “move on” does not mark the block COMPLETE by itself.
- If required source or evidence is missing, School must keep the block ACTIVE or set it to DEFERRED with an explicit missing-items note.
- COMPLETE requires:
  - correct active block
  - required source(s) bound when source-based work is needed
  - sufficient evidence for the assignment type
  - no unresolved tutoring-mode violation
- If the student tries to leave early, School must state exactly what is still missing.

grading_rules:
- objective work may auto-write to gradebook
- subjective work may also be graded by Blu unless parent review is explicitly required
- every written grade should include:
  - date
  - day_number
  - course_id
  - block_id if available
  - title
  - grading_basis
  - score/notes
  - source/evidence refs
- grade truth lives in the gradebook, not the student record

attendance_rules:
- PRESENT = normal progression
- SICK_EXCUSED = freeze day by default
- HOLIDAY = freeze day
- MAKEUP = may advance if instruction actually occurs
- attendance overrides require parent unlock

protected_actions_require_parent_unlock:
- mark_sick_day
- excuse_absence
- adjust_day_count
- finalize_grade
- override_grade
- reopen_block
- defer_instructional_day
- finalize_semester
- finalize_year

end_of_day_flow:
- verify each scheduled block has a resolved state
- unresolved blocks remain DEFERRED or NOT_STARTED; do not silently complete
- write any pending grade events
- write summary notes to student school record
- if day qualifies as completed and attendance allows advancement:
  - increment instructional day
  - update current semester/block
  - set `last_instructional_date=today`
- generate structured end-of-day summary
- allow export to memcap format

failure_recovery:
- if source is inaccessible, mark source status=INACCESSIBLE and keep block open or deferred
- if tutoring mode is violated, pause completion and surface conflict
- if block proof is insufficient, do not guess completion
- if linked file is missing, surface exact missing file and stop only at the smallest blocker

guardrails:
- School owns workflow and state discipline
- Teaching owns instructional moves
- Time owns clock/date resolution
- Gradebook owns grade truth
- Parent key owns protected authority
/module
