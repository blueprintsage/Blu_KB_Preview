capsule_id: kb__templates_school_logs_student_log_current_template_md__554818
title: "Student Log Current TEMPLATE"
date: 2026-02-24
updated: 2026-02-24
version: 0.1.0
status: draft
topic: blu
type: spec
tags: ['templates', 'school', 'logs']
sensitivity: medium
visibility: shared
source: repo
domain: templates
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

# Student School Log (Current) — Template

---

module: school.log.current.M01 | name="Student School Log (Current) — Template"

student.name: <StudentName>
student.id: <student_slug>

school.day_total: 180
school.day_number: 1
school.last_date: 2026-02-19
school.tz: America/Chicago


**ExecLib time state (caller-owned)**
clock.home_tz: America/Chicago
clock.active_tz: America/Chicago
clock.last_tick_iso: <optional ISO-8601>
zero_day.date: <YYYY-MM-DD>
**Schedule knobs (copied from School Overlay; treat as read-only unless parent unlocks + re-signs)**
school.start_time: 08:00
school.block_minutes: 45
school.checkpoints: 10, 20, 35
school.exit_ticket: 44
school.strict_checkpoints: true

school.lunch_start: 12:00
school.lunch_minutes: 60

school.day_ends_on: <anchor_subject>

school.electives.enabled: true
school.electives.count: 2
school.electives.list: Life Skills | Game Dev 1 (Udemy)

**Subjects (in order)**
subjects.core: <Subject 1> | <Subject 2> | <Subject 3> | <Subject 4> | <Subject 5>

**Course Loads (per-subject completion rules)**
**mode: INTERNAL (work in-chat; student must draft) | EXTERNAL (off-platform; requires proof artifacts)**
course_loads.count: 5

course_loads.1.subject: <Subject 1>
course_loads.1.mode: INTERNAL
course_loads.1.required_artifacts: typed_work_in_chat

course_loads.2.subject: <Subject 2>
course_loads.2.mode: INTERNAL
course_loads.2.required_artifacts: typed_work_in_chat

course_loads.3.subject: <Subject 3>
course_loads.3.mode: INTERNAL
course_loads.3.required_artifacts: typed_work_in_chat

course_loads.4.subject: <Subject 4>
course_loads.4.mode: INTERNAL
course_loads.4.required_artifacts: typed_work_in_chat

course_loads.5.subject: <Subject 5>
course_loads.5.mode: INTERNAL
course_loads.5.required_artifacts: typed_work_in_chat

**Electives (recommended defaults)**
course_loads.e1.subject: Life Skills
course_loads.e1.mode: INTERNAL
course_loads.e1.required_artifacts: daily_log_lines_5 | photo_if_applicable

course_loads.e2.subject: Game Dev 1 (Udemy)
course_loads.e2.mode: EXTERNAL
course_loads.e2.required_artifacts: screenshot_progress | checkpoint_notes

**Optional / External-only**
course_loads.x1.subject: Spanish
course_loads.x1.mode: EXTERNAL
course_loads.x1.required_artifacts: screenshot_or_photo_of_work

**Gates**
gates.content_access: require_paste_or_upload_if_questions_unseen
gates.no_substitutes: true
gates.submission_artifacts_required: true
gates.no_switch_while_pending: true
gates.fail_on_switch_attempt: true
gates.anti_ghostwriting: student_draft_required


**Grading knobs**
grading.scale: A 90-100 | B 80-89 | C 70-79 | D 60-69 | F <60
grading.wrong_answer_penalty: -2 per incorrect answer (checkable items)

**Parent gate pointer (optional mirror; NO HASH HERE)**
parent.gate.required: true
parent.gate.id: PGK-<STUDENT_OR_FAMILY>-01

runtime.loaded: true
runtime.active_subject: <blank>
runtime.last_saved_at: <optional>

/module


module: school.log.current.M02 | name="Today"

**Today**

today.date: 2026-02-19
today.day_number: 1
today.school_complete: false
today.completed_at: <optional>
today.notes: <optional>

# Life Skills (daily)
lifeskills.daily.log_lines_required: 5

# Life Skills COOK (Mondays)
lifeskills.cook.scheduled: <true|false>
lifeskills.cook.verify_code: <LS-COOK-YYYYMMDD-###>
lifeskills.cook.artifacts: before_photo | during_photo | after_photo_plated | after_photo_clean_kitchen
lifeskills.cook.log_required: true
lifeskills.cook.status: NOT_SCHEDULED

/module


module: school.log.current.M10 | name="Class Records (generic blocks)"

**Class Records (Today)**

*Block 1*
subject: <Subject 1>
status: NOT_STARTED
lesson: <paste lesson title/day>
checkpoints: 10 <❌> | 20 <❌> | 35 <❌> | 44 <❌>
deliverables:
- <...>
incorrect_count: 0
score: <0-100>
letter: <A|B|C|D|F>
deductions:
- <...>
next_fix:
- <...>
carryover:
- <...>

---

*Block 2*
subject: <Subject 2>
status: NOT_STARTED
lesson: <paste lesson title/day>
checkpoints: 10 <❌> | 20 <❌> | 35 <❌> | 44 <❌>
deliverables:
- <...>
incorrect_count: 0
score: <0-100>
letter: <A|B|C|D|F>
deductions:
- <...>
next_fix:
- <...>
carryover:
- <...>

---

*Block 3*
subject: <Subject 3>
status: NOT_STARTED
lesson: <paste lesson title/day>
checkpoints: 10 <❌> | 20 <❌> | 35 <❌> | 44 <❌>
deliverables:
- <...>
incorrect_count: 0
score: <0-100>
letter: <A|B|C|D|F>
deductions:
- <...>
next_fix:
- <...>
carryover:
- <...>

---

*Block 4*
subject: <Subject 4>
status: NOT_STARTED
lesson: <paste lesson title/day>
checkpoints: 10 <❌> | 20 <❌> | 35 <❌> | 44 <❌>
deliverables:
- <...>
incorrect_count: 0
score: <0-100>
letter: <A|B|C|D|F>
deductions:
- <...>
next_fix:
- <...>
carryover:
- <...>

---

*Block 5 (anchor class)*
subject: <Subject 5>
status: NOT_STARTED
lesson: <paste lesson title/day>
checkpoints: 10 <❌> | 20 <❌> | 35 <❌> | 44 <❌>
deliverables:
- <...>
incorrect_count: 0
score: <0-100>
letter: <A|B|C|D|F>
deductions:
- <...>
next_fix:
- <...>
carryover:
- <...>

---

*Block 6 (elective/optional)*
subject: <Art | Game Dev 1 (Udemy)>
status: NOT_STARTED
lesson: <paste lesson title/day>
checkpoints: 10 <❌> | 20 <❌> | 35 <❌> | 44 <❌>
deliverables:
- <...>
incorrect_count: 0
score: <0-100>
letter: <A|B|C|D|F>
deductions:
- <...>
next_fix:
- <...>

/module


module: school.log.current.M90 | name="Auto-Increment Rule"

**Auto-Increment Rule**

On `SCHOOL:START` when this log is loaded:
- If `school.last_date` is not today:
  - increment `school.day_number` by 1
  - set `school.last_date` to today
  - set `today.day_number` to new day number
  - set `today.school_complete=false`
  - reset all blocks to `NOT_STARTED` and clear lesson/deliverables/scores

On completion of the anchor class (`school.day_ends_on`):
- set `today.school_complete=true`
- set `today.completed_at=<time optional>

/module

/module
