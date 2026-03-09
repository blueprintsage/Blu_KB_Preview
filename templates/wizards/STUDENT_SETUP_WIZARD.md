# student_setup

wizard_id: student_setup
name: Student Setup Wizard
version: 0.9.0
updated: 2026-03-08

purpose:
- Set up a new student or roll a returning student into a new school year.
- Build the active course load inside the student school record.
- Use prior school records to suggest courses, review course history, and surface prerequisite warnings.
- Allow parent override for recommended prerequisite gaps.

notes:
- This wizard is designed for Wizard Library.
- It asks one question at a time.
- It writes propose-only state deltas; Exec still commits.

steps:
- step_id: student_name
  prompt: "What is the student's name?"
  input_type: text
  store_key: wizard.student.name
  required: true
  min_len: 1

- step_id: grade_level
  prompt: "What grade is the student entering?"
  input_type: text
  store_key: wizard.student.grade_level
  required: true

- step_id: school_year
  prompt: "What school year are we setting up?"
  input_type: text
  store_key: wizard.student.school_year
  required: true

- step_id: prior_record
  prompt: "Do you have a prior school record to use for history and course suggestions? (yes/no)"
  input_type: choice
  choices:
    - yes
    - no
  store_key: wizard.prior_record.use
  required: true

- step_id: prior_record_path
  prompt: "Load or name the prior school record to review."
  input_type: text
  store_key: wizard.prior_record.path
  required: false
  next: course_goal_mode

- step_id: course_goal_mode
  prompt: "Are we building a full default grade load or a custom course load? (default/custom)"
  input_type: choice
  choices:
    - default
    - custom
  store_key: wizard.course_goal_mode
  required: true

- step_id: desired_courses
  prompt: "List the courses you want active for this student this year."
  input_type: text
  store_key: wizard.desired_courses.raw
  required: true

- step_id: external_courses
  prompt: "Which of those courses are external or proof-based only? (list or none)"
  input_type: text
  store_key: wizard.external_courses.raw
  required: true

- step_id: prereq_review
  prompt: "Would you like prerequisite warnings surfaced before finalizing the course load? (yes/no)"
  input_type: choice
  choices:
    - yes
    - no
  store_key: wizard.prereq_review
  required: true

- step_id: prereq_override_policy
  prompt: "If a course has only recommended prerequisites missing, should the wizard warn only or treat it like a hard stop? (warn/hard-stop)"
  input_type: choice
  choices:
    - warn
    - hard-stop
  store_key: wizard.prereq_policy
  required: true

- step_id: parent_override
  prompt: "If the wizard finds a recommended prerequisite gap, do you want parent override enabled? (yes/no)"
  input_type: choice
  choices:
    - yes
    - no
  store_key: wizard.parent_override_allowed
  required: true

- step_id: schedule_start
  prompt: "What time should the school day start?"
  input_type: text
  store_key: wizard.schedule.start_time_local
  required: true

- step_id: schedule_lengths
  prompt: "What are the default class length, break length, and lunch length?"
  input_type: text
  store_key: wizard.schedule.lengths
  required: true

- step_id: finalize
  prompt: "Ready to write the active course load, course history notes, prerequisite warnings, and override notes into the student school record? (yes/no)"
  input_type: choice
  choices:
    - yes
    - no
  store_key: wizard.finalize
  required: true


