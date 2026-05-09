# BC-SKILL-008 Live Route Matrix Required

status: active
updated: 2026-05-08
category: validation/tests

## Pattern

A route exists in prose, but the runtime does not execute it in the required order.

## Rule

Route declarations are not runtime proof. The live routing path must show ordered execution, route lock, owner handoff, terminal packet, and Egress validation.

Exec should not maintain a bloated command catalog. Slash command stem rows live in Commands. Program surfaces live with Programs. Exec owns only generic gate mechanics and route locking.

## Checks

- Is the route row in the canonical owner surface?
- Is the ordered ingress step executable, not merely described?
- Does a lock stop all later route admission?

## Tests

- Protected OPSEC requests must not reach ordinary conversation.
- Unknown slash stems must not become ordinary chat.
- Repo bootstrap targets must not fall back to uploaded files.
