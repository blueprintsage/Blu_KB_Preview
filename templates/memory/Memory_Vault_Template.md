[CAPSULE_HEADER_BEGIN]
capsule_id: blu__memory_vault_template
title: "Blu Memory Vault Template"
date: 2026-02-13
updated: 2026-02-15
version: 0.8.1
status: active
topic: blu
type: template
tags: [memory, vault, template, memlog_v1, privacy, portability, continuity]
sensitivity: high
visibility: shared
source: doc
domain: ops
[CAPSULE_HEADER_END]

# Blu Memory Vault Template

## 0) Purpose

Provides a portable, privacy-forward template for saving user/collab context and continuity notes.

## 1) Scope

Used when creating or updating a Memory Vault entry; not for storing sensitive secrets.

## 2) Interfaces

### Inputs
- User-provided memories / preferences / stable facts.
- Sanitized context only.

### Outputs
- A structured markdown/yaml note usable across chats/tools.

### Defaults
- Append-only. Minimal PII.

### Overrides / precedence
- Regulation Matrix + Anchors govern privacy/safety.

## TOC
- 01. Preamble
- 02. Uniform schema: memlog_v1
- 03. Save protocol (fast)
- 04. How to use in a new chat
- 05. Index (optional, lightweight)
- 06. Entries (paste new memlog_v1 blocks below)

## 3) Modules

module: blu__memory_vault_template.M00 | name="Preamble"


# Blu Memory Vault (External Capsules) — Template (v0.8.1)

This file is **yours**. Keep it offline (notes, Obsidian, repo, etc.).
When you want Blu to have continuity in a new chat, paste **only the relevant entries** (or a short index + the 1–3 entries that matter).

---

/module

module: blu__memory_vault_template.M01 | name="Uniform schema: memlog_v1"

## Uniform schema: memlog_v1

- memlog_v1.id: snake_case_unique_id
- memlog_v1.created: YYYY-MM-DD
- memlog_v1.tz: America/Chicago
- memlog_v1.scope: family_private        # family_private|user_private|public_safe
- memlog_v1.domain: dev|writing|career|life|health|relationships|finance
- memlog_v1.tags: [tag1, tag2]
- memlog_v1.sensitivity: low|medium|high
- memlog_v1.disclosure: anonymized_case_pattern
- memlog_v1.signal[]: "What was going on / what the user was experiencing"
- memlog_v1.pattern[]: "The reusable dynamic (what tends to happen)"
- memlog_v1.what_helped[]: "Steps, reframes, or checks that worked"
- memlog_v1.scripts[]: "Optional: words to say / a short rule / a prompt"
- memlog_v1.next_step[]: "The smallest next action (if any)"
- memlog_v1.redactions[]: "Anything removed or generalized"
- memlog_v1.notes[]: "Optional extra details (still non-identifying)"


**Rule:** If `scope` is `family_private` or `user_private`, never include names/locations/dates that could identify someone.
Prefer composites and generalization.

---

/module

module: blu__memory_vault_template.M02 | name="Save protocol (fast)"

## Save protocol (fast)

Blu may ask:
> **Memory-save request:** Save this as a memlog?

You reply with one of:
- `SAVE: YES`
- `SAVE: NO`
- `SAVE: YES, REDACT <what to remove>`
- `SAVE: FORCE, REDACT <what to remove>` *(family override / “yes anyway”)*

Blu responds with a `memlog_v1` block to paste under **Entries** below.

---

/module

module: blu__memory_vault_template.M03 | name="How to use in a new chat"

## How to use in a new chat

1) Paste your **USERCAP** at the top (prefs).
2) Paste either:
   - **Index only** (if all you need is “what’s going on”), or
   - **Index + 1–3 memlogs** that matter for the session.

Suggested one-liner:
> “Use these memlogs as context; don’t restate them unless needed.”

---

/module

module: blu__memory_vault_template.M04 | name="Index (optional, lightweight)"

## Index (optional, lightweight)

- mem_index_v1.updated: 2026-02-13
- mem_index_v1.highlights[]: "Dev: UE troubleshooting patterns"
- mem_index_v1.highlights[]: "Writing: voice-preserving edits"
- mem_index_v1.highlights[]: "Career: resume/cover tailoring workflow"
- mem_index_v1.active_threads[]: "Project: ____"


---

/module

module: blu__memory_vault_template.M05 | name="Entries (paste new memlog_v1 blocks below)"

## Entries (paste new memlog_v1 blocks below)

# --- entries start ---

/module

module: blu__memory_vault_template.M20 | name="Family Gate (no-secret storage)"

## Family Gate (no-secret storage)

Store only status, never the passphrase.

Fields:
- family_gate.enabled: true|false
- family_gate.method: passphrase
- family_gate.last_unlocked_at: <optional>
- family_gate.notes: Passphrase stored outside vault (parent-only)

/module

module: blu__memory_vault_template.M21 | name="School Day Log (portable, parent-readable)"

## School Day Log (portable, parent-readable)

Header:
- day_number: 1–180
- date: YYYY-MM-DD
- schedule: Spanish IV / Algebra 2 / British Lit / Modern Am Hist / Physics w Lab / Game Dev (optional)
- school_complete: true|false

Per-class record (repeat):
- subject:
- lesson:
- checkpoints: 10 ✅/❌, 20 ✅/❌, 35 ✅/❌, 44 ✅/❌
- deliverables:
- incorrect_count:
- score (0–100):
- letter (A–F):
- deductions:
- next_fix:
- carryover:

/module

module: blu__memory_vault_template.M22 | name="Weekly Summary (report-card safe)"

## Weekly Summary (report-card safe)

Fields:
- week_of: YYYY-MM-DD
- days_completed: #
- subject_avgs: (Spanish IV, Algebra 2, British Lit, Modern Am Hist, Physics)
- wins:
- struggles:
- next_week_focus:

/module

## 9) Changelog

- 2026-02-15 — Modular wrapper added (no content removed); modules tagged for parse.

- 2026-02-15 — Version bumped 0.8.0 → 0.8.1 (structural refactor, patch).

# Appendix: AI↔AI Session MemCap (AI2AI_v1.1)

Use this when Admin is bridging a cross-model session via copy/paste relay.

```text
---
SOURCE: <Model/Org/Version>
TARGET: <Model/Org/Version>
PROTOCOL: AI2AI_v1.1
MODE: <Workshop|Hangout|Relay>
PHASE: <A|B|complete>
TURN: <n|final>
TOPIC: <short>
---

<core content — no greetings/signoffs; code blocks preferred>

---
STATE:
  turn: <n|final>
  phase: <A|B|complete>
  mode: <Workshop|Hangout|Relay>
  active_topic: <short>
  decisions: [<≤6>]
  artifacts: [<ids/paths>]
  next: [<≤3 prompts>]
---

INTEGRITY: chars≈<n> | lines=<n> | first32="<...>" | last32="<...>"
```

## Thread Rotation
Every ~20–30 turns, emit a one-screen recap (STATE + artifacts) and start a new chat seeded with that recap.
