# Exec — State Schema v2 (Draft)

---

module: kb__protocols_exec_exec_state_schema_v2.M01 | name="Content"
[CAPSULE_HEADER_BEGIN]
mem_id: 2026_02_28__blu__exec-state-schema-v2
title: Exec — State Schema v2 (Draft)
date: 2026-02-28
status: draft
topic: blu
type: spec
tags: exec, state, schema, kernel, determinism
sensitivity: medium
visibility: private
source: roadmap
domain: ops
authority: canon
[CAPSULE_HEADER_END]

## Goal

Make regressions hard by making **state shape explicit**, versioned, and validated.

**Rule:** modules may *read* state; they may only *propose* deltas. Exec is the only writer/applier.

## Top-level objects

### EXEC_META (kernel)

```yaml
EXEC_META:
  schema_version: "2.0"
  kernel_version: "<exec_version>"
  mode: "NORMAL"              # NORMAL | DEBUG
  flow_state: "OPEN"          # OPEN | FOCUS | SCHOOL | MIDWORK
  last_tick_utc: "<iso8601>"
  suppress:
    window_seconds: 300
    seen:
      - key: "<suppress_key>"
        last_emit_utc: "<iso8601>"
```

### SCHEDULER_STATE (reminders)

```yaml
SCHEDULER_STATE:
  schema_version: "2.0"
  tz_default: "America/Chicago"
  reminders:
    - id: "<uuid_or_shortid>"
      title: "<string>"
      due_local: "2026-03-01 12:00"
      tz: "America/Chicago"
      status: "OPEN"          # OPEN | PAUSED | DONE
      stage:
        warn_60_sent: false
        warn_10_sent: false
      due:
        is_due: false
        first_due_utc: null
        acknowledged_due: false
      last_mutation_utc: "<iso8601>"
```

## Required invariants

- `schema_version` must be present and parseable.
- `flow_state` gates what kinds of proposals may interrupt.
- `suppress.seen` is append-only within a session; Exec may prune by time window.
- Reminder **DUE persists** until explicit user action: DONE / MOVE / PAUSE / DELETE.

## Migration notes (v1.x → v2.0)

- Replace any “fire once then clear” DUE semantics with persistent `due.is_due=true`.
- Stage flags (`warn_60_sent`, `warn_10_sent`) remain “fire once” per reminder instance.
