# PROGRAM.Pass.Normalizer.v1 — Spec — v1.0.0

CAPSULE HEADER v1.1 (NO-YAML)
capsule_id: blu__pass_normalizer_v1
title: PROGRAM.Pass.Normalizer.v1 — Spec
date: 2026-03-05
updated: 2026-03-05
version: 1.0.0
status: active
topic: pass
type: spec
tags: [pass, normalize, mechanics, uniformity, quote-ban]
sensitivity: high
visibility: shared
source: doc
domain: pass
schema: capsule_header_block_v1.1
body_schema: blu_modular_v1
END CAPSULE HEADER

module: blu__passnorm.M01 | name="Purpose (HARD)"
Convert raw PASS findings (which may include paraphrases, OCR noise, or quotes) into **uniform mechanics objects**:

- PATTERN: IF / THEN / BECAUSE / CHECK
- DRILL: GOAL / INPUTS / STEPS / OUTPUT / RUBRIC_PASS
- AP: TRIGGER / PROCEDURE / DONE_DEFINITION

No domain exceptions. Works for cooking, writing, art, programming, manuals, etc.
/module

module: blu__passnorm.M02 | name="Quote ban (HARD)"
- Patterns/Drills/APs MUST NOT contain verbatim quotes.
- If the raw extraction includes quoted spans or OCR fragments, the normalizer must:
  1) translate into mechanics (preferred), or
  2) reject the item with REASON: QUOTE_DUMP_DETECTED
- Provenance allowed only as SOURCE_REF in ledger (no quotes required).
/module

module: blu__passnorm.M03 | name="Inputs / outputs (HARD)"
Input:
- `raw_findings` (PASS 1–4 internal results)
- `source_meta` (title/author/date/pages)
- `domain`, `subskill`, `run_id`

Output:
- `objects` grouped by: patterns, drills, APs, variants, rejected
- Each object MUST have a stable `ID` and the required fields.
- Provide `counts` for each group.
/module

module: blu__passnorm.M04 | name="Failure mode (HARD)"
If the normalizer cannot produce at least:
- 1 pattern with IF/THEN/BECAUSE/CHECK, and
- 1 drill with RUBRIC_PASS, and
- 1 AP with PROCEDURE

then it must fail-closed with `ERR:SKILLFORGE_SCHEMA_VIOLATION` (do not pack, do not zip, do not update registry).
/module
