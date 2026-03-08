# Parent_GOD_Mode_Key — Template

capsule_id: school__parent_god_mode_key_template
version: 0.9.0
status: DRAFT
scope: family
visibility: local_only
purpose: Parent-only authority capsule for family controls, protected school actions, time restrictions, and future family memcap integration.

privacy:
- This file is local-only.
- Do not commit to a public repo.
- Store only hashes/secrets-safe values here.
- Do not store plaintext passphrases in this file.

module: blu__school_parent.M01 | name="Parent GOD Mode Key — Template | status=active"

family:
  family_id: FAM-<FAMILY_ID>
  household_name: <optional>
  timezone: America/Chicago
  allowed_adults:
    - <adult_name>
  child_profiles:
    - child_id: <child_id>
      child_name: <child_name>
      linked_student_record: <student_record_filename>
      linked_gradebook: <gradebook_filename>

gate_identity:
  parent.gate.id: PGK-<FAMILY_OR_STUDENT>-01
  parent.god_mode: true
  parent.gate.enabled: true
  parent.gate.method: passphrase
  parent.gate.key_policy: persistent   # persistent | timed_session
  parent.gate.ttl_minutes: 15
  parent.gate.hash: sha256:<PASTE_HASH_HERE>

unlock_protocol:
- `PARENT:UNLOCK`
- prompt for passphrase
- hash passphrase with SHA-256 and compare to `parent.gate.hash`
- require `parent.gate.id` match with linked child/student file when relevant
- if valid, set `runtime.parent_unlocked=true`
- if key_policy is `timed_session`, expire after `parent.gate.ttl_minutes`

lock_protocol:
- `PARENT:LOCK`
- set `runtime.parent_unlocked=false`

restricted_command_surface:
  parent_only:
    - REPORT:*
    - GRADE:*
    - SCHOOL:CONFIG:*
    - SCHOOL:EXPORT:*
    - SCHOOL:RESET:*
    - SCHOOL:ATTENDANCE:*
    - SCHOOL:OVERRIDE:*
    - SCHOOL:REOPEN:*
    - FAMILY:MEMCAP:*
    - FAMILY:TIMELOCK:*
  student_safe:
    - SCHOOL:START
    - CLASS:START <Subject>
    - TEACH / explain / practice within current assignment
    - SCHOOL:STATUS
    - SCHOOL:SHOW_DAY

school_controls:
  attendance_overrides_allowed: true
  sick_day_marking_allowed: true
  excuse_absence_allowed: true
  defer_day_allowed: true
  reopen_block_allowed: true
  finalize_grade_allowed: true
  override_grade_allowed: true
  export_reports_allowed: true

attendance_actions:
  allowed:
    - mark_sick_day
    - mark_holiday
    - excuse_absence
    - defer_instructional_day
    - convert_makeup_day
    - adjust_day_count

grade_actions:
  allowed:
    - finalize_grade
    - approve_subjective_grade
    - override_grade
    - void_entry
    - exempt_assignment
    - reopen_entry
    - add_parent_note

family_memcap:
  enabled: false
  storage_mode: local_only    # local_only | repo_private | external
  family_memcap_id: <optional>
  linked_capsules:
    - <optional>
  retention_policy: parent_defined
  notes:
    - future hook for family-wide continuity
    - should not expose private family memory to student lane without parent approval

time_controls:
  enabled: true
  default_child_policy: scheduled
  policy_mode_allowed:
    - unrestricted
    - scheduled
    - quota
    - locked
  child_time_policies:
    - child_id: <child_id>
      mode: scheduled
      allowed_days:
        - Mon
        - Tue
        - Wed
        - Thu
        - Fri
      allowed_windows:
        - start_local: "08:00"
          end_local: "15:30"
          purpose: school_hours
        - start_local: "16:00"
          end_local: "18:00"
          purpose: homework_or_projects
      daily_minutes_cap: <optional>
      hard_lock_windows:
        - start_local: "21:00"
          end_local: "06:30"
          purpose: sleep
      exceptions:
        - <optional>

device_or_use_controls:
  track_hours_of_use: true
  enforce_lockout: false
  warn_before_lock_minutes: 10
  lock_scope:
    - school_commands
    - chat_access
    - elective_access
  notes:
    - future hook for Blu-mediated access windows
    - should remain parent-authorized

reporting:
  parent_reports_enabled: true
  daily_summary_enabled: true
  weekly_summary_enabled: true
  grade_rollup_enabled: true
  attendance_rollup_enabled: true

audit:
  log_parent_actions: true
  action_log:
    - timestamp_iso: <ISO-8601+offset>
      actor: <adult_name>
      action: <action_name>
      target: <student_or_family_target>
      note: <optional>

link_targets:
  linked_school_year_model: <optional>
  linked_student_records:
    - <student_record_filename>
  linked_gradebooks:
    - <gradebook_filename>

future_expansion:
- family memcap storage and retrieval
- child-specific use windows enforced through Blu
- family-wide schedules
- parent dashboards / reports
- sibling-aware policy inheritance
- household quiet-hours / device rules

guardrails:
- This file grants authority; it should not become the student runtime record.
- This file may point to student records and gradebooks, but should not replace them.
- Protected actions require parent unlock.
- Plaintext secrets must never be stored here.

/module