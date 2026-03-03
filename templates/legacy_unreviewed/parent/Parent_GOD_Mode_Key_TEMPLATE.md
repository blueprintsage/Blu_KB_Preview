capsule_id: kb__templates_parent_parent_god_mode_key_template_md__7e4e74
title: "Parent GOD Mode Key TEMPLATE"
date: 2026-02-24
updated: 2026-02-24
version: 0.1.0
status: draft
topic: blu
type: spec
tags: ['templates', 'parent']
sensitivity: medium
visibility: shared
source: repo
domain: templates
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

# Parent GOD Mode Key (Local-only Cap) — Template

---

module: blu__school_parent.M01 | name="Parent GOD Mode Key (Local-only Cap) — Template | status=active"

**Purpose**
Unlock parent-only controls (reports/config/exports) when child restrictions are enabled.

> **Privacy:** This file is **local-only**. Do **not** commit to any public repo.

---

**Gate Identity (link target)**

# This ID is the *pointer* that child overlays/logs reference.
parent.gate.id: PGK-<STUDENT_OR_FAMILY>-01

---

**Parent Gate Settings**

parent.god_mode: true
parent.gate.enabled: true
parent.gate.method: passphrase
parent.gate.key_policy:            # persistent|single_use (wizard fills; hosted default persistent)

**Key policy notes**
- ttl (recommended): `PARENT:UNLOCK` grants a timed window (default 15 minutes). TTL is evaluated when a protected command is run.
- session: `PARENT:UNLOCK` remains valid until `PARENT:LOCK`.
- Deprecated: one-shot “spent” key behavior is not recommended for hosted chat.
- Reference: `protocols/parent/Parent_Gate_TTL_v1.md`

# Store only a hash (recommended). Do NOT store the plain passphrase here.
# Format: sha256:<HEX>
parent.gate.hash: sha256:<PASTE_HASH_HERE>

parent.allowed_adults:              # e.g., Bob | Mary (user-defined; wizard fills)

---

**Restricted Command Surface (parent-only)**

When locked, Blu must refuse these unless unlocked:

- `REPORT:*`
- `GRADE:*`
- `SCHOOL:CONFIG:*`
- `SCHOOL:EXPORT:*`
- `SCHOOL:RESET:*`

Allowed without unlock (student-safe):
- `SCHOOL:START`
- `CLASS:START <Subject>`
- “Explain / teach / practice” within the current assignment

---

**Unlock Protocol (runtime contract)**

*`PARENT:UNLOCK`*
1) Prompt for parent passphrase.
2) Hash passphrase (UTF-8, SHA-256) and compare to `parent.gate.hash`.
3) Require `parent.gate.id` match between:
   - loaded key, and
   - overlay/log pointer
4) If match → set `runtime.parent_unlocked=true` for session.

*`PARENT:LOCK`*
- set `runtime.parent_unlocked=false`

/module

/module