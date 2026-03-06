# Error Macros (Quick Reference) — v1.1.0

CAPSULE HEADER v1.1 (NO-YAML)
capsule_id: blu__error_macros_quickref
title: Error Macros (Quick Reference)
date: 2026-03-05
updated: 2026-03-05
version: 1.2.0
status: active
topic: ops
type: spec
tags: [error-macros, quickref]
sensitivity: high
visibility: shared
source: doc
domain: ops
schema: capsule_header_block_v1.1
body_schema: blu_modular_v1
END CAPSULE HEADER

module: blu__errmacros.Q01 | name="Quick reference"
See: `contracts/ERROR_MACROS_PROGRAM_CATALOG.md` (normative).
/module

# Error Macros — Contract (Kernel-Callable) — v1.0

updated: 2026-03-05
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


module: blu__errmacros.Q02 | name="Macro IDs"
PROGRAM_REQUIRED
CMD_UNKNOWN
PDF_OPEN_FAILED
PDF_EXPIRED
PREFLIGHT_FAIL
GUTLADDER_OUTPUT_LEAK
ZIP_MISSING
PACK_DUAL_LANE_FAILED
SKILLFORGE_SCHEMA_VIOLATION
HEADER_VERSION_STALE
ZIP_NAME_NONUNIFORM
KERNEL_ZIP_VERSION_MISSING
/module

# ERROR_MACROS_PROGRAM_CATALOG — PATCH — v1.2.1
# Add these four macros to ERROR_MACROS_PROGRAM_CATALOG.md
# Insert after macro 12 (ZIP_NAME_NONUNIFORM), before the closing module tag.
# Also add IDs to the Q02 module in error_macros.md quickref.

updated: 2026-03-05
reason: Four macros referenced in PASS pipeline and Program System had no catalog entries.

---

13) ADAPTER_UNKNOWN
```txt
STATUS: BLOCKED
ACTION: ADAPTER_UNKNOWN — rerun with adapter=PDF|NOVEL|COMICZIP|IMAGES|VIDZIP
```

14) SOURCE_EXPIRED
```txt
STATUS: BLOCKED
ACTION: SOURCE_EXPIRED — re-upload the source file and rerun PASS:PREFLIGHT.
```

15) LENS_RESOLUTION_FAILED
```txt
ERROR: LENS_RESOLUTION_FAILED
ACTION: Provide subject= override or verify source title/type is recognizable, then rerun PASS:GUT-LADDER.
```

16) ZIP_ASSEMBLY_FAILED
```txt
ERROR: ZIP_ASSEMBLY_FAILED
ACTION: Check state_delta from PackDualLane for missing content; fix and rerun PASS:GUT-LADDER.
```

---
# Q02 module additions (error_macros.md quickref):
# Add these four IDs to the existing macro ID list:
# ADAPTER_UNKNOWN
# SOURCE_EXPIRED
# LENS_RESOLUTION_FAILED
# ZIP_ASSEMBLY_FAILED