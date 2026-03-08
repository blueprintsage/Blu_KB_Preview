# Error Macros — Program Catalog (System-Wide) — v1.2.1

CAPSULE HEADER v1.1 (NO-YAML)
capsule_id: blu__error_macros_catalog
title: Error Macros — Program Catalog (System-Wide)
date: 2026-03-05
updated: 2026-03-07
version: 1.2.1
status: active
topic: ops
type: spec
tags: [error-macros, programs, exec, uniformity]
sensitivity: high
visibility: shared
source: doc
domain: ops
schema: capsule_header_block_v1.1
body_schema: blu_modular_v1
END CAPSULE HEADER

module: blu__errmacros.M01 | name="Purpose (HARD)"
Provide deterministic, fail-closed, system-wide error output. Error macros are rendered by:
- `PROGRAM.ErrorMacros.v1` (primary)
- Exec fallback (if the Program is unavailable)

No other component may print ad-hoc failure prose. Errors must be uniform across PASS/SkillForge/ART/SCHOOL/etc.
/module

module: blu__errmacros.M02 | name="Rendering rules (HARD)"
- Output is 1–3 lines.
- Use one of two shapes:

Shape A (preferred):
`ERROR: <MACRO_ID>`
`ACTION: <one line>`

Shape B (BLOCKED):
`STATUS: BLOCKED`
`ACTION: <one line>`

- Exactly one ACTION line.
- No internal implementation details. No thoughts. No debugging stacks.
- Context is allowed only if it fits on a single line and is stable (e.g., run_id).
/module

module: blu__errmacros.M03 | name="System-wide Exec rule (HARD)"
If any gate/program returns `BLOCKED` or `ERR` (or returns a macro_id), Exec MUST:
1) call `ERR:RENDER(macro_id, ctx)`
2) print the returned lines
3) STOP the turn

No fallback helpful flows. No silent hangs.
/module

module: blu__errmacros.M04 | name="PROGRAM.ErrorMacros.v1 interface (HARD)"
Inputs:
- `macro_id` (string, required)
- `ctx` (dict, optional; sanitized)

Output:
- `lines[]` (1–3 strings)
- `stop=true`

The Program MUST be pure/deterministic: same macro_id + ctx shape ⇒ same output.
No side effects.
/module

module: blu__errmacros.M05 | name="Canonical macro table (HARD)"
All macro IDs are UPPER_SNAKE. The rendered text must match exactly.

1) PROGRAM_REQUIRED
```txt
ERROR: PROGRAM_REQUIRED
ACTION: Add Program registry mapping + command dispatch for this capability, then rerun.
```

2) CMD_UNKNOWN
```txt
ERROR: CMD_UNKNOWN
ACTION: Use HELP to see valid commands, or run the nearest suggested command.
```

3) PDF_OPEN_FAILED
```txt
ERROR: PDF_OPEN_FAILED
ACTION: Re-upload the file or provide a different copy (prefer text-layer PDF).
```

4) PDF_EXPIRED
```txt
ERROR: PDF_EXPIRED
ACTION: Re-upload the PDF (or provide a stable local path) and rerun PASS:PREFLIGHT.
```

5) PREFLIGHT_FAIL
```txt
STATUS: BLOCKED
ACTION: PREFLIGHT FAIL — non-schema output detected. Rerun PASS:PREFLIGHT.
```

6) GUTLADDER_OUTPUT_LEAK
```txt
ERROR: GUTLADDER_OUTPUT_LEAK
ACTION: GUT-LADDER must be artifact-only (counts+ZIP+registry). Suppress inline logs and rerun PASS:GUT-LADDER.
```

7) ZIP_MISSING
```txt
ERROR: ZIP_MISSING
ACTION: Ensure DROP-IN ZIP is created before printing results or updating registry, then rerun.
```

8) PACK_DUAL_LANE_FAILED
```txt
ERROR: PACK_DUAL_LANE_FAILED
ACTION: Fix SkillForge dual-lane packing (skills/ + teaching/), then rerun PASS:GUT-LADDER.
```

9) SKILLFORGE_SCHEMA_VIOLATION
```txt
ERROR: SKILLFORGE_SCHEMA_VIOLATION
ACTION: Fix patterns/drills/APs to the uniform schema (IF/THEN/BECAUSE/CHECK; Drill rubric; AP procedure), then rerun.
```

10) HEADER_VERSION_STALE
```txt
ERROR: HEADER_VERSION_STALE
ACTION: Update updated/date/version per Uniformity Standard, then rerun.
```

11) KERNEL_ZIP_VERSION_MISSING
```txt
ERROR: KERNEL_ZIP_VERSION_MISSING
ACTION: Kernel ZIP must include package version (<YYYY-MM-DD>_<HHMM>_Name_version.zip). Rename and rerun.
```

12) ZIP_NAME_NONUNIFORM
```txt
ERROR: ZIP_NAME_NONUNIFORM
ACTION: Name the ZIP <YYYY-MM-DD>_<HHMM>_<Name>(_<version>).zip per Uniformity Standard, then rerun.
```

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

17) QUOTE_DUMP_DETECTED
```txt
ERROR: QUOTE_DUMP_DETECTED
ACTION: Normalize to mechanics (IF/THEN/BECAUSE/CHECK). Reject quote/OCR dumps, then rerun.
```
/module

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
KERNEL_ZIP_VERSION_MISSING
ZIP_NAME_NONUNIFORM
ADAPTER_UNKNOWN
SOURCE_EXPIRED
LENS_RESOLUTION_FAILED
ZIP_ASSEMBLY_FAILED
QUOTE_DUMP_DETECTED
/module

module: blu__errmacros.Q99 | name="Merge note"
This file supersedes the split between `error_macros.md` and `ERROR_MACROS_PROGRAM_CATALOG.md`.
`error_macros.md` should be retired or reduced to a one-line pointer to this canonical catalog.
Patch macros formerly carried in the quickref are merged here.
 /module
