# Error Macros

CAPSULE HEADER v1.1 (NO-YAML)
capsule_id: blu__error_macros_catalog
title: Error Macros — Program Catalog (System-Wide)
date: 2026-03-05
updated: 2026-04-05
version: 1.2.0
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
---

# Error Macros — Program Catalog

## Capsule Canon

module: blu__errmacros.M01 | name="Capsule Canon"
status: ACTIVE
version: 0.12.0
date: 2026-04-05
updated: 2026-04-05

purpose:
- Define the canonical deterministic error macros for the active kernel.

rules:
- Error macros are rendered by `PROGRAM.ErrorMacros`.
- Exec may use built-in fallback error output only if `PROGRAM.ErrorMacros` is unavailable.
- No other component may print ad hoc failure prose for fail-closed runtime errors.
- Error output must be compact, deterministic, and uniform.
- Catalog review is mandatory whenever new Programs, ExecLibs, routes, or fail-closed conditions are added, changed, or removed.
/module

## Rendering Rules

module: blu__errmacros.M02 | name="Rendering rules"
status: ACTIVE
version: 0.12.0
date: 2026-04-05
updated: 2026-04-05

rules:
- Output is 1–2 lines only.
- Canonical shape is:
  - ERROR: <MACRO_ID>
  - ACTION: <one-line next step>
- Exactly one ACTION line.
- No debug stacks.
- No internal implementation details.
- No helpful essay fallback.
/module

## Exec Rule

module: blu__errmacros.M03 | name="Exec rule"
status: ACTIVE
version: 0.12.0
date: 2026-04-05
updated: 2026-04-05

rules:
- If any gate, route, owner, or validation step returns BLOCKED, ERR, or macro_id, Exec must:
  1. call ERR:RENDER(macro_id, ctx)
  2. print returned lines
  3. stop the turn
- Unknown slash commands must fail through this lane.
- No fallthrough to ordinary conversation.
/module

## Program Interface

module: blu__errmacros.M04 | name="Program interface"
status: ACTIVE
version: 0.12.0
date: 2026-04-05
updated: 2026-04-05

inputs:
- macro_id (string, required)
- ctx (dict, optional; sanitized)

outputs:
- lines[] (1–2 strings)
- stop=true

rules:
- PROGRAM.ErrorMacros must be pure and deterministic.
- Same macro_id and same relevant ctx shape must produce the same output.
- No side effects.
/module

## Canonical Macro Table

module: blu__errmacros.M05 | name="Canonical macro table"
status: ACTIVE
version: 0.12.0
date: 2026-04-05
updated: 2026-04-05

UNKNOWN_COMMAND
ERROR: UNKNOWN_COMMAND
ACTION: Use /help to see available commands.
/module

## Maintenance Rule

module: blu__errmacros.M06 | name="Maintenance rule"
status: ACTIVE
version: 0.12.0
date: 2026-04-05
updated: 2026-04-05

rules:
- When a new Program, ExecLib, or Exec fail-closed path is added, check whether it introduces a new canonical user-visible error condition.
- If it does, update this macro catalog in the same change pass.
- Do not add a new workflow owner or library fail-closed path without reviewing error coverage.
- Macro additions must stay minimal and tied to real active failure surfaces only.
- Removed workflows must have their stale macros removed in the same cleanup pass.
/module