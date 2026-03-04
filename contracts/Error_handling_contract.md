# ERROR HANDLING CONTRACT — UNIVERSAL (Guru Meditation)
version: 0.1.0
updated: 2026-03-04
status: interim-canon
scope: all systems (PASS, SkillForge, RepoOps, PEL, Homeschool, Wizards, etc.)
principle: fail-closed

---

## Purpose
Provide a single, consistent failure protocol across all systems so errors are:
- deterministic
- compact (low tokens)
- recoverable
- non-contaminating (no “success” artifacts when dependencies are missing)

---

## Core Law: FAIL-CLOSED
If any REQUIRED dependency is missing, unreadable, expired, or invalid:
- emit a **GURU_MEDITATION** block (format below)
- stop immediately
- do NOT generate “success” artifacts
- do NOT mutate registries/indexes/state

---

## Required Error Block (GURU_MEDITATION)
On any failure, output exactly one block in this format:

GURU_MEDITATION: <ERROR_CODE>
SYSTEM: <SYSTEM_NAME>
STAGE: <STAGE_NAME>
CAUSE: <1-line cause>
DEPENDENCIES:
- <dep_1>: <OK|MISSING|EXPIRED|UNREADABLE|INVALID>
- <dep_2>: <OK|MISSING|EXPIRED|UNREADABLE|INVALID>
ARTIFACTS: <none|list created paths>
RECOVERY: <1-line recovery action>
NEXT_ACTION: <exact command to run after recovery>

Notes:
- Keep CAUSE/RECOVERY to one line each.
- DEPENDENCIES must include every REQUIRED input for that stage.

---

## Error Codes (Canonical Prefixes)
Use stable codes so logs can be searched and aggregated.

### PASS_
- PASS_E_CONTRACT_MISSING
- PASS_E_CONTRACT_EXPIRED
- PASS_E_REGISTRY_MISSING
- PASS_E_SOURCE_UNREADABLE
- PASS_E_SOURCE_EXPIRED
- PASS_E_OCR_REQUIRED
- PASS_E_PARSE_FAILED
- PASS_E_PACKAGE_FAILED

### SKILLFORGE_
- SF_E_TEMPLATE_MISSING
- SF_E_SKILL_INDEX_MISSING
- SF_E_ROUTE_FAILED
- SF_E_VALIDATION_FAILED
- SF_E_PACKAGE_FAILED

### REPOOPS_
- RO_E_INDEX_MISSING
- RO_E_PATCH_CONFLICT
- RO_E_VERIFY_FAILED
- RO_E_PACKAGE_FAILED

### GLOBAL_
- G_E_PERMISSION
- G_E_INVALID_COMMAND
- G_E_ENV_FILE_LIFECYCLE (expired uploads / invalidated handles)
- G_E_TIMEOUT
- G_E_UNKNOWN

---

## Stage Declaration (Per System)
Each system MUST declare a stage map. Minimum recommended:

### PASS stages
PREFLIGHT
HARVEST
NORMALIZE
CLUSTER
COMPILE
PACKAGE

### SkillForge stages
ROUTE
ASSEMBLE
GENERATE
VALIDATE
PACKAGE

### RepoOps stages
SCAN
PLAN
PATCH
VERIFY
PACKAGE

If a system lacks a stage map, default STAGE=UNKNOWN and emit GLOBAL error.

---

## Dependency Rules
A dependency is REQUIRED if the current stage cannot proceed without it.

Examples:
- PASS:PREFLIGHT requires the SOURCE file
- PASS:GUT-LADDER requires CONTRACT + SOURCE (+ registry if updating)
- PACKAGE requires write access and artifact list

Mark dependencies explicitly in the error block.

---

## No Partial Success
If failure occurs mid-run:
- ARTIFACTS must list what was created (if anything)
- mark run as aborted
- do not claim “PASS SUCCESS”
- do not update registries/indexes

---

## Recovery Rules
RECOVERY must be actionable and minimal:
- “Re-upload <file>” / “Run OCR and re-upload” / “Re-run command”
- If multiple items needed, list them in one line separated by semicolons.

NEXT_ACTION must be the exact command to resume safely:
- PASS:PREFLIGHT
- PASS:GUT-LADDER (NUCLEAR)
- PASS:MODERNIZE (OVERLAY)
- etc.

---

## Logging (Repo)
If repo write is available, create an error log file:

reports/errors/<SYSTEM>_ERROR_<YYYY-MM-DD>_<short_id>.md

Content:
- the exact GURU_MEDITATION block
- optional: 3–6 bullet “context notes” (no long prose)

If repo write is NOT available, output the block only.

---

## Minimal “Expired Upload” Handling
If the environment reports expired uploads or file handles invalidate mid-run:
- ERROR_CODE: G_E_ENV_FILE_LIFECYCLE (or PASS_E_SOURCE_EXPIRED if in PASS)
- fail-closed
- RECOVERY: re-upload required dependencies
- NEXT_ACTION: rerun from PREFLIGHT

---

## Compliance Test
A system is compliant if:
1) It emits the exact error block on failure
2) It stops (no success artifacts)
3) It provides a valid RECOVERY + NEXT_ACTION