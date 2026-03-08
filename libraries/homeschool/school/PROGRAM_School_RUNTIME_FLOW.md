# PROGRAM_School_RUNTIME_FLOW

program_id: PROGRAM.School
name: School
version: 0.9.0
status: DRAFT

purpose:
- Run the student school day using the canonical school files.
- Own startup, day state, block flow, source binding, evidence tracking, completion audit, grade writes, attendance control, and end-of-day export.
- Use PROGRAM.Teaching for instruction, not replace it.

student_start_file:
- `<Student>_STUDENT_SCHOOL_RECORD.md`

protected_or_internal_files:
- `<Student>_STUDENT_GRADEBOOK.md`
- `<Student>_Parent_GOD_Mode_Key.md`
- `<Student>_SCHOOL_YEAR_MODEL.md`

student_start_rule:
- Student provides only `<Student>_STUDENT_SCHOOL_RECORD.md`.
- SCHOOL start must work from the student school record alone.
- Gradebook is not a student-start file.
- Parent key is not a student-start file.
- School Year Model is not a student-start file.
- Protected/internal files may be consulted later only when needed.

canonical_inputs:
- required_for_student_start:
  - `<Student>_STUDENT_SCHOOL_RECORD.md`
- optional_internal:
  - `<Student>_SCHOOL_YEAR_MODEL.md`
  - `<Student>_STUDENT_GRADEBOOK.md`
- protected:
  - `<Student>_Parent_GOD_Mode_Key.md`

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
- SCHOOL:START
- SCHOOL:STATUS
- SCHOOL:SHOW_DAY
- CLASS:START <block_or_subject>
- CLASS:SOURCE:BIND
- CLASS:EVIDENCE:ADD
- CLASS:COMPLETE
- CLASS:DEFER
- CLASS:SKIP
- GRADE:WRITE
- SCHOOL:ENDDAY
- SCHOOL:EXPORT:DAY
- PARENT:UNLOCK
- PARENT:LOCK

startup_flow:
- load student school record
- resolve current local time through Time Service
- resolve local weekday
- determine whether today is an active school day from the student record's calendar model and linked schedule data
- if optional School Year Model exists, School may use it for reconciliation or break/holiday lookup
- if today is weekend or break, do not advance instructional day
- if today is an active instructional day and prior instructional date is older than today, prepare the next live day
- do not load or expose the gradebook during student start
- set session_status=READY
- show today's schedule and current block statuses

auto_stage_rule:
- If a loaded file matches `<Student>_STUDENT_SCHOOL_RECORD.md`, PROGRAM.School should auto-stage `SCHOOL:START`.
- Auto-stage should occur without asking an extra “what do you want me to do with it?” question.
- Auto-stage must use the student school record as the only required student-start file.
- Linked year model, gradebook, and parent key remain internal/protected support files and must not be requested from the student at startup.

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
  1. 08:00-08:45 — Algebra 2
  2. 09:00-09:45 — British Literature
  3. 10:00-10:45 — Modern American History
  4. 11:00-11:45 — Life Skills
  Lunch — 12:00-13:00
  5. 13:00-13:45 — Physics w Lab
  6. 14:00-14:45 — Spanish 4
  7. 15:00-15:45 — Game Dev 1 (Udemy)

  Guardrails:
  - Algebra 2 / History / Physics = CHECK_ONLY
  - British Literature = NO_ANSWERING
  - Life Skills = GUIDED_PRACTICE
  - Spanish 4 / Game Dev 1 = external proof required

  Next Block Ready:
  Block 1 — Algebra 2
  To begin Block 1, send one of:
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
- current day truth lives in Student School Record
- School Year Model may refine or reconcile calendar law, but is not required for student start

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
- evidence entries must point back to block_id and, when possible, source_ref

completion_rules:
- block completion is block-scoped, not vague session-scoped
- COMPLETE requires:
  - correct block active
  - sufficient evidence
  - source-grounded verification when needed
  - no unresolved tutoring-mode violation
- SKIPPED requires explicit reason
- DEFERRED requires unresolved blocker or missing proof
- EXTERNAL classes may be marked COMPLETE only after proof artifact review

class_end_rules:
- End of class time does not equal block completion.
- Student request to "end class" or "move on" does not mark the block COMPLETE by itself.
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
- School should consult the gradebook only when writing grades, reading rollups, or generating parent-facing reports
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
- write any pending grade events to the gradebook if needed
- write summary notes to student school record
- if day qualifies as completed and attendance allows advancement:
  - increment instructional day
  - update current semester/block
  - set last_instructional_date=today
- generate structured end-of-day summary
- allow export to memcap format

failure_recovery:
- if source is inaccessible, mark source status=INACCESSIBLE and keep block open or deferred
- if tutoring mode is violated, pause completion and surface conflict
- if block proof is insufficient, do not guess completion
- if linked file is missing, surface the exact missing file and stop only at the smallest blocker

guardrails:
- School owns workflow and state discipline
- Teaching owns instructional moves
- Time owns clock/date resolution
- Gradebook owns grade truth
- Parent key owns protected authority
