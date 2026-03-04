# PASS — Lockdown (Nuclear GUT-LADDER Default)
updated: 2026-03-03
status: interim-canon
tz: America/Chicago

## Purpose
PASS converts sources into a structured, dual-lane skill package:
- Teaching (Lane A): human-facing
- Skills (Lane B): machine-facing (anti-drift laws + execution support)

PASS must produce an extract-and-drop zip with updated indexes at the end of a run.

---

## Canon Folder Layout (Interim)
For every subject:

skills/<domain>/<subject>/
  <SUBJECT>_INDEX.md

  Skills/
    <SUBJECT>_B.md     # Lane B (modules)

  Teaching/
    <SUBJECT>_A.md     # Lane A (modules)

  overlays/ (only if needed)
    <overlay_id>/
      Skills/<SUBJECT>_B_<OVERLAY>.md
      Teaching/<SUBJECT>_A_<OVERLAY>.md

Rules:
- Always output BOTH lanes.
- No inbox/staging/dump folders.
- Overlays are organized (folder-per-overlay), never dumped.

---

## Default Mode (Nuclear)
PASS defaults to:
- mode: GUT-LADDER
- intensity: NUCLEAR (full harvest)
- output: BOTH lanes + zip + index patch
- reporting: FULL unless user requests COUNTS_ONLY

NUCLEAR means:
- do not stop at marker counts
- do not rely on headings alone
- scan end-to-end, extract everything that can become law/procedure/practice
- multi-pass allowed/expected when needed

---

## Multi-Pass Rule (Mandatory)
PASS may require multiple passes. Label them explicitly.

### PASS 1 — Harvest
- Extract all candidates:
  - Patterns (laws)
  - Drills (practice actions)
  - Gates (enforcement wrapper)
  - Tests (proof checks)
  - APs (application protocols)
  - Models/Principles (FULL mode only)
- Tag candidates with source pointers (page/section) without quoting text.

### PASS 2 — Normalize + Dedupe
- Normalize wording into repo-native language.
- Merge duplicates and near-duplicates.
- Resolve conflicts:
  - keep base law in Skills (Lane B)
  - move style/medium/language differences into overlays
  - reject destabilizing/inferior techniques

### PASS 3 — Compile Dual Lane
- Lane B (Skills): laws first, then proof + execution.
- Lane A (Teaching): explanations + progression + human drills, referencing Lane B IDs.

### PASS 4 — Validate + Reject Test
- Enforce schema requirements (below).
- If new content does not add enforceable value, reject it.

---

## Artifact Definitions (Interim Canon)
### Patterns (Laws)
Primary “IF X THEN Y” rules. Patterns are carried as law.

Pattern constraint: “A pattern must encode a single rule; compound statements must be split; clustering happens before promotion.”

### Gates
Interim mapping: 1 gate per pattern (wrapper used for enforcement tracking).
(We keep the term “Gate” for accounting and validation, but “Pattern” remains the law interface.)

### Tests
Proof checks tied to gates/patterns. Interim mapping: 1 test per gate (minimum viable proof).

### Drills
Practice loops that build mastery. Each drill targets pattern IDs.

### APs
Callable procedures used during execution/teaching requests.

---

## Lane B Required Module Groups (Single File)
Skills/<SUBJECT>_B.md MUST contain modules for:
- meta
- patterns (laws)
- gates (optional group module; items still keyed to pattern ids)
- tests
- drills
- aps
- ledger

Patterns MUST be explicit:
- id
- IF
- THEN
- CHECK
- FAIL
- NOTES (optional)
- REF (source pointer; no quotes)

Drills MUST include:
- id
- targets [pattern_ids]
- procedure (or steps)
- scoring OR pass/fail
- stop

---

## Lane A Required Module Groups (Single File)
Teaching/<SUBJECT>_A.md MUST contain modules for:
- meta
- lesson_map
- core_explanations
- patterns (human-facing; may reference Lane B IDs)
- drills (human)
- aps (usage/how-to)
- ledger

---

## Report Modes
### FULL (default)
PASS writes/updates artifacts (A + B) and emits zip.

### COUNTS_ONLY (user request)
PASS may report only totals for:
- patterns, drills, gates, tests, aps
…but still performs the full gut ladder internally if explicitly commanded.

---

## Output Packaging (Always)
At end of run produce a zip containing:
- only the subject folder(s) touched
- updated index files required (e.g., indexes/INDEX_SKILLS.md)
- a run report: reports/PASS_RUN_<YYYY-MM-DD>.md listing:
  - counts added/updated/rejected
  - files changed
  - indexes touched

PASS must NOT modify indexes/MASTER_INDEX.md unless a new chapter folder is introduced (rare, explicit).

---

## “When in doubt, ask”
If an instruction is unclear or would require invention:
- ask ONE clarifying question
- otherwise fail closed (do not guess).
