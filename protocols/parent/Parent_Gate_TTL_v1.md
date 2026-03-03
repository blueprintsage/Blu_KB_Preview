# Parent Gate — Unlock TTL + Lock Hygiene (v1) --- module: kb__protocols_parent_parent_gate_ttl_v1.M01 | name="Content"
[CAPSULE_HEADER_BEGIN]
mem_id: 2026_02_28__blu__parent-gate-ttl-v1
title: Parent Gate — Unlock TTL + Lock Hygiene (v1)
date: 2026-02-28
status: draft
topic: blu
type: spec
tags: parent_gate, school, opsec, ttl, lock
sensitivity: medium
visibility: private
source: roadmap
domain: ops
authority: canon
[CAPSULE_HEADER_END]

## Purpose
Define canonical behavior for Parent Gate unlock lifetimes (session vs TTL window) and immediate relock behavior.

This is written to avoid:
- “spent keyfile” style persistence (not reliable in hosted chat)
- stale unlocks lingering longer than intended
- mismatched docs across engine / exec / wizards

## Terms
- **Protected command**: any command that requires parent privileges when School/Parent Gate is enabled.
- **Unlock**: a temporary state allowing protected commands.
- **TTL unlock**: unlock that expires automatically after a fixed duration.
- **Session unlock**: unlock that lasts until explicitly relocked.

## Canonical states
- `PARENT_LOCKED`
- `PARENT_UNLOCKED_TTL` (expires after `unlock_expires_at`)
- `PARENT_UNLOCKED_SESSION` (no expiry; explicit lock ends)

## Commands

### `PARENT:UNLOCK`
Effects:
- Validates the user-provided passphrase against stored hash (never prints secret).
- Sets unlock state to either TTL or session per policy.

Policy defaults (recommended):
- Hosted chat: **TTL unlock** (default 15 minutes)
- Local runtime: TTL or session allowed; TTL still recommended

### `PARENT:LOCK`
Effects:
- Immediately sets `PARENT_LOCKED` regardless of current unlock type.
- Clears any stored `unlock_expires_at`.

This command always wins (highest priority).

## Evaluation rule (critical)
Unlock validity is evaluated **at time of protected command**:
- If `now >= unlock_expires_at` for TTL unlock → treat as locked.
- Session unlock remains unlocked until `PARENT:LOCK`.

No background timers are assumed.

## Re-lock hygiene
- Expired TTL unlocks should be treated as locked without requiring an additional write.
- Implementations may optionally emit a single informational line: “Parent Gate relocked (TTL expired).”
- Do not write “SPENT” or one-shot state into public or shared files.

## Test matrix
1) TTL expiry:
- Unlock TTL 1m
- Advance time beyond expiry
- Protected command must be blocked

2) Session unlock:
- Unlock session
- Protected command allowed
- After `PARENT:LOCK`, blocked

3) Lock override:
- Unlock (either type)
- Immediately `PARENT:LOCK`
- Protected command blocked

[/module]
