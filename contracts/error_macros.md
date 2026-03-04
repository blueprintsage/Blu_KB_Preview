# Error Macros — Contract (Kernel-Callable) — v1.0

updated: 2026-03-04
tz: America/Chicago
status: active (kernel-callable)
scope: system-wide

**Purpose**
Provide deterministic, fail-closed, user-visible error output in chat. Macros are **rendered by `PROGRAM.ErrorMacros.v1`**
and/or Exec fallback. Macros must not leak internal implementation details.

**Format (normative)**
- Each macro renders as 1–6 lines (keep tight).
- First line MUST start with `ERROR:` OR `STATUS: BLOCKED` (caller chooses style).
- Must include exactly **one** `ACTION:` line with a single next step.

---

## Macro: ERR:PROGRAM_REQUIRED

**When**
A capability meets the PROGRAM-FIRST checklist (stable command surface / system-wide / schema-locked / deterministic artifacts)
but the command path is not wired to a Program registry mapping.

**Render (normative)**
```txt
ERROR: PROGRAM_REQUIRED
ACTION: Add Program registry mapping + command dispatch for this capability, then rerun.
```

**Notes**
- Do not fall back to “helpful” alternate flows.
- Do not attempt auto-creation. Program creation is Admin-gated and explicit.

---

## Macro: ERR:CMD_UNKNOWN

**When**
User invokes an unrecognized command token.

**Render (example)**
```txt
ERROR: CMD_UNKNOWN
ACTION: Use HELP to see valid commands, or run the nearest suggested command.
```

---

## Macro: ERR:PDF_OPEN_FAILED

**When**
PDF/file open fails (corrupt file, unsupported type, missing file, etc.).

**Render (example)**
```txt
ERROR: PDF_OPEN_FAILED
ACTION: Re-upload the file or provide a different copy (prefer text-layer PDF).
```

---

## Macro: ERR:PREFLIGHT_FAIL

**When**
PASS:PREFLIGHT emits non-schema output (TOC/structure lists, page sampling, recommendations, “what do you want me to do?”, etc.).

**Render (example)**
```txt
STATUS: BLOCKED
ACTION: PREFLIGHT FAIL — non-schema output detected. Rerun PASS:PREFLIGHT.
```

---

## Macro: ERR:DUP_CONFIRM_REQUIRED

**When**
Registry indicates a duplicate run. The system must stop and ask for confirmation.

**Render (example)**
```txt
STATUS: BLOCKED
ACTION: Confirm rerun? (Y/N)
```
