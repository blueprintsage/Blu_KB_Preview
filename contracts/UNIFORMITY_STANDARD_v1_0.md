# Uniformity Standard (Repo + Kernel)

## 0) Non-negotiable rule
**Everything is uniform.** Directories may differ by purpose, but **structure + schema** are consistent everywhere.

This is a permanent standard. No “special cases” without an explicit versioned override contract.

---

module: blu__uniformity.M01 | name="Document Structure (HARD)"
**All markdown artifacts** (contracts, docs, protocols, reports, templates, tests, indexes, skills) MUST:
1) Start with a **capsule header block** (NO-YAML), using `capsule_header_block_v1.1`.
2) Use **module blocks** for body content:
   - `module: <id> | name="<human name>"`
   - body
   - `/module`

**Capsule header block v1.1 (NO-YAML) — template**
```txt
CAPSULE HEADER v1.1
capsule_id: <id>
title: <title>
date: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
version: <semver>
status: <draft|active|locked>
topic: <topic>
type: <spec|doc|protocol|report|template|test|index|skill>
tags: [<tag>, ...]
sensitivity: <low|med|high|critical>
visibility: <shared|private>
source: <doc|runtime>
domain: <ops|core|teach|task|pass|skillforge|other>
schema: capsule_header_block_v1.1
body_schema: blu_modular_v1
END CAPSULE HEADER
```

Allowed exception:
- `README.md` may omit the header only if a sibling `README.meta.md` contains the header.

/module`

Allowed exception:
- `README.md` may omit header block **only** if a sibling `README.meta.md` contains the header (recommended: still include header).

/module

module: blu__uniformity.M02 | name="Naming + IDs (HARD)"
- `capsule_id` is required and stable.
- Every module has a stable `module:` id.
- Files must be named deterministically:
  - contracts: `contracts/<area>/<NAME>_v<MAJOR>_<MINOR>.md`
  - protocols: `protocols/<NAME>_v<MAJOR>_<MINOR>.md`
  - reports: `reports/<YYYY-MM-DD>_<NAME>.md`
  - indexes: `indexes/INDEX_<AREA>.md`
/module

module: blu__uniformity.M03 | name="SkillForge Dual-Lane Output (HARD)"
All skills content lives under SkillForge dual-lane:

Lane B (canonical primitives):
- `skills/<domain>/<subskill>/...`

Lane A (compiled teaching pack):
- `teaching/<domain>/<subskill>/...`

**No flat bundles** at repo root for Skill outputs.

Uniform Lane B files (canonical set):
- `patterns.yaml`
- `drills.yaml`
- `aps.yaml`
- `variants.yaml`
- `rejected.yaml`
- `ledger/run_<run_id>.md`
- `ingest_manifest.json`

Uniform Lane A files (canonical set):
- `README.md`
- `SYLLABUS.md`
- `PATTERNS.md`
- `DRILLS.md`
- `APS.md`
- `TESTS.md` (compiled from checks/rubrics when applicable)

/module

module: blu__uniformity.M04 | name="Uniform Skill Object Schema (HARD)"
All domains (art, cooking, writing, programming, manuals, etc.) MUST emit the same object shapes.

### PATTERN (If–Then + Because + Check)
Required fields:
- `id`
- `if`
- `then`
- `because`
- `check`

### DRILL (Inputs → Steps → Output → Rubric)
Required fields:
- `id`
- `goal`
- `inputs[]`
- `steps[]`
- `output`
- `rubric.pass[]`
Optional: `rubric.fail[]`, `timebox_minutes`, `difficulty`

### AP (Application Protocol)
Required fields:
- `id`
- `trigger`
- `procedure[]`
- `done_definition[]`
Optional: `artifacts[]`

**Quote ban (HARD):**
- No verbatim quotes in patterns/drills/APs. Use mechanics only.
- Provenance allowed only as `source_ref` (book + page/section) in ledger or object metadata (no quotes required).

/module

module: blu__uniformity.M05 | name="PASS Output Contract (HARD)"
PASS is an ingest/extraction pipeline that MUST produce SkillForge dual-lane outputs.

### PASS:PREFLIGHT
Validation only; schema-locked keys.

### PASS:GUT-LADDER
Artifact-first; user-facing output is minimal:
1) `patterns=<n> drills=<n> APs=<n> variants=<n> rejected=<n>`
2) `DROP-IN ZIP: <link>`
3) `Registry updated: PASS_BOOK_REGISTRY.md (entry run_id <id>).`

All extracted mechanics go **inside** the dual-lane bundle.

### ZIP naming (HARD)
ZIP filename must be:
`<YYYY-MM-DD>_<HHMMSS>_<domain>_<subskill>_run_<run_id>.zip`

/module

module: blu__uniformity.M06 | name="System-Wide Enforcement (HARD)"
- Anything requiring stable command surface, system-wide behavior, schema-locking, or deterministic artifacts MUST be a Program.
- Exec must fail-closed with `ERR:PROGRAM_REQUIRED` when a contract-only path is invoked without a Program mapping.
- Exec must enforce `ERR:GUTLADDER_OUTPUT_LEAK` if PASS prints inline logs/mechanics.

Validator requirement:
- Before ZIP + registry update, run `SKILLFORGE:VALIDATE_UNIFORM_SCHEMA`.
- On failure: emit `ERR:SKILLFORGE_SCHEMA_VIOLATION`, do not zip, do not update registry.

/module
