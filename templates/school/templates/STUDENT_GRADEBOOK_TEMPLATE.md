# Student_Gradebook

record_id: SCHOOL.STUDENT.GRADEBOOK
version: 0.9.0
status: DRAFT
purpose: Authoritative parent-controlled grade ledger for one student for one school year.

ownership:
- PROGRAM.School may write grade events here when grading is completed.
- Parent authorization is required for protected edits, overrides, deletions, and finalization actions.
- Students may view only approved/visible summaries, not modify authoritative entries.

scope:
- assignment grades
- block grades
- quiz/test grades
- rubric-backed subjective grades
- semester rollups
- year rollups
- parent overrides
- audit trail

not_for:
- daily runtime scheduling
- attendance state
- source registry
- live tutoring flow
- full assignment archives

student:
  name: <student_name>
  student_id: <student_id>
  school_year: <yyyy-yyyy>
  grade_level: <grade_or_band>
  timezone: America/Chicago

grading_policy:
  default_scale: percent_letter
  objective_workflow: auto_record
  subjective_workflow: propose_then_review
  allow_parent_override: true
  allow_reopen_after_final: true

grade_status_allowed:
- PROVISIONAL
- REVIEW_REQUIRED
- FINAL
- OVERRIDDEN
- EXEMPT
- VOID

entry_type_allowed:
- ASSIGNMENT
- BLOCK
- QUIZ
- TEST
- PROJECT
- ESSAY
- LAB
- PARTICIPATION
- SEMESTER_ROLLUP
- YEAR_ROLLUP

entries:
  - entry_id: <unique_entry_id>
    date: <YYYY-MM-DD>
    day_number: <1-180>
    semester: <1-2>
    block: <1-6>
    course_id: <course_id>
    subject: <subject>
    title: <assignment_or_block_title>
    entry_type: ASSIGNMENT
    grading_basis: objective
    score_raw: <e.g. 9/10>
    score_percent: <e.g. 90>
    letter: <e.g. A->
    status: FINAL
    source_refs:
      - <source_id_or_label>
    evidence_refs:
      - <evidence_id_or_label>
    rubric_ref: <optional>
    notes: <optional>
    parent_note: <optional>
    created_at_iso: <ISO-8601+offset>
    finalized_at_iso: <ISO-8601+offset>

course_rollups:
  - course_id: <course_id>
    subject: <subject>
    grading_window: semester_1
    included_entry_ids:
      - <entry_id>
    average_percent: <optional>
    letter: <optional>
    status: PROVISIONAL

semester_rollups:
  - semester: 1
    included_course_ids:
      - <course_id>
    status: PROVISIONAL
    notes: <optional>

year_rollup:
  included_semesters:
    - 1
    - 2
  status: PROVISIONAL
  notes: <optional>

parent_actions:
  allowed:
  - finalize_grade
  - override_grade
  - exempt_assignment
  - void_entry
  - reopen_entry
  - add_parent_note
  - approve_subjective_grade

workflow_rules:
- Objective work may be auto-recorded when the evidence and source basis are sufficient.
- Subjective work may be recorded as PROVISIONAL or REVIEW_REQUIRED before finalization.
- A FINAL grade is authoritative unless reopened by parent action.
- OVERRIDDEN must preserve the original score and attach a parent note.
- VOID keeps the audit trail but removes the entry from rollup calculations.
- EXEMPT removes the entry from denominator/weighting calculations.
- A grade entry should reference the block/course context that produced it.

visibility_rules:
- Student-facing summaries may show completion, feedback, and approved scores.
- Internal grading notes and parent notes may remain hidden from the student-facing lane.
- Final report output should derive from this ledger, not from the student runtime record.

audit_trail:
  events:
    - event_id: <event_id>
      entry_id: <entry_id>
      action: created
      actor: SYSTEM
      timestamp_iso: <ISO-8601+offset>
      note: <optional>

migration_note:
- This file stores authoritative grades separately from `Student_School_Record.md`.
- Students should not be able to alter grading truth by editing their runtime school record.