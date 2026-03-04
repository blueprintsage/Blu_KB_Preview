# Program Registry (Doc)
Date: 2026-02-23
Purpose: Canonical list of Programs (opt-in layers) and their default settings.  
Note: This document is descriptive (“what exists + defaults”), not runtime state.

---

[CAPSULE_HEADER_BEGIN]
mem_id: 2026_02_23__blu__program-registry
title: Program Registry — Programs + Defaults
date: 2026-02-23
status: active
topic: blu
type: spec
tags: programs, registry, opt-in, layers, defaults
sensitivity: medium
visibility: shared
source: doc
domain: ops
authority: propose_only
next_action: Implement Programs command surface + stubs for each program to read/write runtime program state.
definition_of_done: Registry lists all Programs with defaults; runtime state uses same program_id and fields.
review_after: 2026-03-02
redaction_level: light
notes_public: Defines program identifiers and default behaviors for opt-in layers like BluDay, QuitSmoking Support, and Joke of the Day.
[CAPSULE_HEADER_END]
## Canonical source

- **This file is the canonical Program Registry** (single source of truth for `program_id`, defaults, and human names).
- Runtime program state must reference `program_id` exactly as written here.
- Other docs may mirror content, but **must not override** defaults defined here.


## Version
Spec-Version: 1.0
Changelog:
- 2026-02-23: Initial registry + defaults.

---

## 1) Registry rules

- **Programs are opt-in**: default `enabled=false`.
- This doc defines **what programs exist** and their **default configuration**.
- Actual enable/disable and user preferences live in **runtime program state** (not here).
- Every program must have a stable `program_id` in the form `program:<slug>`.

---

## 2) Program State Fields (canonical keys)

Each program uses these keys (even if some are unused at first):

- `program_id` (string, required)
- `display_name` (string, required)
- `enabled` (bool, default false)
- `scope` (`all | admin_only`, default all)
- `mode` (`light | standard | intensive`, optional)
- `cadence` (`none | daily | weekly | custom`, default none)
- `time_local` (optional, only meaningful if cadence != none)
- `consent_required` (bool, default true)
- `notes` (optional, short preferences)

---

## 3) Canonical Program List (defaults)

### 3.1 BluDay
- `program_id`: `program:bluday`
- `display_name`: `BluDay`
- Defaults:
  - `enabled=false`
  - `scope=all`
  - `mode=standard`
  - `cadence=none` (manual by default)
  - `consent_required=true`

Intent: structured flow the user explicitly runs (practice / check-in cadence), low-noise.

---

### 3.2 QuitSmoking Support
- `program_id`: `program:quitsmoking_support`
- `display_name`: `QuitSmoking Support`
- Defaults:
  - `enabled=false`
  - `scope=all`
  - `mode=standard`
  - `cadence=none` (no automated pings by default)
  - `consent_required=true`

Intent: positive reinforcement + coping tools **only when opted in** and **user requests help**. No policing.

---

### 3.3 Joke of the Day
- `program_id`: `program:joke_of_day`
- `display_name`: `Joke of the Day`
- Defaults:
  - `enabled=false`
  - `scope=all`
  - `mode=light`
  - `cadence=none` (manual by default; scheduling optional later)
  - `consent_required=true`

Intent: fun/social “layer” that can be run on demand; cadence later if desired.

---

### 3.4 AIDay (Admin-only)
- `program_id`: `program:aiday`
- `display_name`: `AIDay`
- Defaults:
  - `enabled=false`
  - `scope=admin_only`
  - `mode=standard`
  - `cadence=none`
  - `consent_required=true`

Intent: admin workflow day / review routine.

---

### 3.5 AI Relay (Optional / Public)
- `program_id`: `program:ai_relay`
- `display_name`: `AI Relay`
- Defaults:
  - `enabled=false`
  - `scope=all`
  - `mode=standard`
  - `cadence=none`
  - `consent_required=true`

Intent: help users craft requests/prompts for other AI/tools/services. No autonomous outreach implied.


## 3.6 Canonical names and aliases (router map)

These names should resolve deterministically to `program_id`:

- BluDay → `program:bluday`
- QuitSmoking / QuitSmoking Support → `program:quitsmoking_support`
- JokeDay / Joke of the Day → `program:joke_of_day`
- AIDay → `program:aiday`
- AI Relay → `program:ai_relay`

---

## 4) Add-a-program checklist (registry update)

To add a new program:
1) Choose `program_id` (`program:<slug>`) and `display_name`
2) Add an entry with defaults (enabled=false)
3) Decide `scope` (all/admin_only)
4) Decide `mode` default (optional)
5) Keep `cadence=none` unless explicitly designed as scheduled
6) Ensure it’s opt-in (`consent_required=true`)

---

## 5) Known future additions (non-binding)
- `program:gratitude`
- `program:stretch_break`
- `program:micro_journal`
- `program:skill_drill_<topic>`