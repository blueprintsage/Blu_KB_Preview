# ERROR MACROS (ERRMAC) — UNIVERSAL
version: 0.1.0
updated: 2026-03-04
status: interim-canon
scope: all systems + kernel capsules
depends_on: contracts/error_handling_contract.md
If any REQUIRED dependency is missing/expired/unreadable at any stage, invoke ERRMAC and STOP (fail-closed).
---

## Macro: ERRMAC (FATAL, FAIL-CLOSED)

Use when a required dependency is missing/expired/unreadable or an invariant fails.

Invocation (conceptual):
ERRMAC(code, system, stage, cause, deps[], artifacts, recovery, next_action)

Required output format (exact):

GURU_MEDITATION: <ERROR_CODE>
SYSTEM: <SYSTEM_NAME>
STAGE: <STAGE_NAME>
CAUSE: <1-line cause>
DEPENDENCIES:
- <dep>: <OK|MISSING|EXPIRED|UNREADABLE|INVALID>
ARTIFACTS: <none|paths>
RECOVERY: <1-line recovery action>
NEXT_ACTION: <exact command>

Behavior:
- stop immediately
- no “success” artifacts
- no registry/index mutations

---

## Macro: CHECK_DEPS (GUARD)

Purpose: validate dependencies before running a stage.
If any required dep is not OK → call ERRMAC.

---

## Macro: ASSERT_STATE (INVARIANT)

Purpose: internal sanity check.
If false → call ERRMAC with GLOBAL or system error code.

---

## Macro: WARNMAC (NON-FATAL)

Purpose: record recoverable issues without aborting.
Format:
WARNING: <CODE> | <1-line message>
Continue execution.

---

## Logging Rule (Repo)

If repo write is available:
- write error log to: reports/errors/<SYSTEM>_ERROR_<YYYY-MM-DD>_<shortid>.md
- contents = the exact GURU_MEDITATION block (+ optional 3 bullets max)