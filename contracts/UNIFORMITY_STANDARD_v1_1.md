# Uniformity Standard (Repo + Kernel) — v1.2.0

CAPSULE HEADER v1.1 (NO-YAML)
capsule_id: blu__uniformity_standard
title: Uniformity Standard (Repo + Kernel)
date: 2026-03-05
updated: 2026-03-05
version: 1.2.0
status: active
topic: blu
type: spec
tags: [uniformity, schema, modules, headers, pass, skillforge]
sensitivity: high
visibility: shared
source: doc
domain: ops
schema: capsule_header_block_v1.1
body_schema: blu_modular_v1
END CAPSULE HEADER

module: blu__uniformity.M00 | name="Non-negotiable rule (HARD)"
**Everything is uniform.** Directories may differ by purpose, but **structure + schema** are consistent everywhere.

This is a permanent standard. No “special cases” without an explicit versioned override contract.
/module

module: blu__uniformity.M01 | name="Document Structure (HARD)"
**All markdown artifacts** (contracts, docs, protocols, reports, templates, tests, indexes, skills) MUST:

1) Start with a **CAPSULE HEADER block** (NO-YAML) as shown below.
2) Use **module blocks** for body content.

**Important:** The human-readable markdown title/header (`# Title`) and the CAPSULE HEADER block must appear
**outside** any module, at the very top of the file, so humans can find it fast.

CAPSULE HEADER v1.1 (NO-YAML) — template
```txt
CAPSULE HEADER v1.1 (NO-YAML)
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

Module blocks — template
```txt
module: <stable_module_id> | name="<human name>"
<content>
/module
```
/module

module: blu__uniformity.M02 | name="Header + version bump (HARD)"
When the body changes, update **all three**:
- `updated: YYYY-MM-DD` (America/Chicago; set to today)
- `version:` bump (SemVer)
- `status:` only if lifecycle changes

Version bump rules (SemVer):
- PATCH (x.y.z+1): wording/formatting/clarity; no requirement changes
- MINOR (x.y+1.0): new required sections/fields/constraints/commands/validators/macros
- MAJOR (x+1.0.0): breaking changes to schemas, keys, required file sets, layouts, or command surfaces
/module

module: blu__uniformity.M03 | name="Zip naming (HARD)"
All generated archives must follow:

Base: `<YYYY-MM-DD>_<HHMM>_<Name>`

- Kernels: `<YYYY-MM-DD>_<HHMM>_<Name>_<version>.zip`
- Repos/KBs/Skill packs: `<YYYY-MM-DD>_<HHMM>_<Name>.zip`

Notes:
- HHMM is local (America/Chicago).
- No spaces. Use underscores.
/module

module: blu__uniformity.M04 | name="Exceptions + file classes (HARD)"
Not every file needs a CAPSULE HEADER. Exceptions are explicit by file class:

**A) Non-markdown / binary**
- Images (`.png .jpg .gif .svg`), audio/video, `.pdf`, `.zip`, etc. — no header.

**B) Markdown that may omit header**
Allowed to omit CAPSULE HEADER only if one of these is true:
1) It is a pure **asset README** under `assets/` and has a sibling `README.meta.md` containing the header.
2) It is a generated **index shard** that is machine-generated and explicitly tagged as generated in its first line:
   `GENERATED FILE — DO NOT EDIT` (recommended: still include a header).
3) It is a legacy KB document explicitly listed in a legacy exception list:
   `contracts/UNIFORMITY_LEGACY_EXCEPTIONS.md`

**C) Default**
If a markdown file is not covered by A/B, it MUST include the CAPSULE HEADER block and modules.
/module

module: blu__uniformity.M05 | name="SkillForge Dual-Lane Output (HARD)"
All skills content lives under SkillForge dual-lane:

Lane B (canonical primitives):
- `skills/<domain>/<subskill>/...`

Lane A (compiled teaching pack):
- `teaching/<domain>/<subskill>/...`

**No flat bundles** at repo root for Skill outputs.

Uniform Lane B files (canonical set):
- `patterns.md`
- `drills.md`
- `aps.md`
- `variants.md`
- `rejected.md`
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

module: blu__uniformity.M06 | name="Uniform Skill Object Schema (HARD)"
All domains (art, cooking, writing, programming, manuals, etc.) MUST emit the same object shapes.

PATTERN required fields:
- id
- IF
- THEN
- BECAUSE
- CHECK

DRILL required fields:
- id
- GOAL
- INPUTS (list)
- STEPS (list)
- OUTPUT
- RUBRIC.PASS (list)

AP required fields:
- id
- TRIGGER
- PROCEDURE (list)
- DONE_DEFINITION (list)

Quote ban (HARD):
- No verbatim quotes in patterns/drills/APs. Use mechanics only.
- Provenance allowed only as `SOURCE_REF` (book + page/section) in ledger or metadata (no quotes required).
/module

module: blu__uniformity.M07 | name="PASS Output Contract (HARD)"
PASS is an ingest/extraction pipeline that MUST produce SkillForge dual-lane outputs (for all books/docs).

PASS:PREFLIGHT
- validation only; schema-locked keys

PASS:GUT-LADDER
- artifact-first; user-facing output is minimal:
  1) `patterns=<n> drills=<n> APs=<n> variants=<n> rejected=<n>`
  2) `DROP-IN ZIP: <link>`
  3) `Registry updated: PASS_BOOK_REGISTRY.md (entry run_id <id>).`

ZIP naming (HARD):
- Skill pack ZIP filename:
  `<YYYY-MM-DD>_<HHMM>_<domain>_<subskill>_run_<run_id>.zip`
/module

module: blu__uniformity.M09 | name="Package vs File versions (HARD)"
**File versions are local and independent.** Every headered file has its own `version` and `updated`.

Definitions:
- **File version**: the SemVer in the file’s CAPSULE HEADER block.
- **Package version**: the version in a kernel ZIP filename (when applicable).

Rules (HARD):
1) No file inherits the kernel/KB/package version.
2) Changing a file requires bumping that file’s `updated` and `version` (per SemVer rules).
3) Kernel ZIP naming includes a package version:
   `<YYYY-MM-DD>_<HHMM>_<Name>_<version>.zip`
4) Repo/KB/skills ZIP naming has **no** package version:
   `<YYYY-MM-DD>_<HHMM>_<Name>.zip`

Optional enforcement (recommended):
- `GURU:PACKAGE_LINT` validates package naming rules.
- `GURU:HEADER_LINT` validates per-file header/version/updated compliance.
/module


module: blu__uniformity.M08 | name="System-Wide Enforcement (HARD)"
- Anything requiring stable command surface, system-wide behavior, schema-locking, or deterministic artifacts MUST be a Program.
- Exec must fail-closed with `ERR:PROGRAM_REQUIRED` when a contract-only path is invoked without a Program mapping.
- Exec must enforce `ERR:GUTLADDER_OUTPUT_LEAK` if PASS prints inline logs/mechanics.
- Before ZIP + registry update, run `SKILLFORGE:VALIDATE_UNIFORM_SCHEMA`.
  On failure: emit `ERR:SKILLFORGE_SCHEMA_VIOLATION`, do not zip, do not update registry.
/module
