# BC-SKILL-004 Single Renderer Ownership

status: active
updated: 2026-05-08
category: ownership/rendering

## Pattern

A route recognizes the correct owner but another layer emits or decorates user-visible text.

## Rule

Exactly one selected owner may provide the packet for a deterministic lane. Support libraries, Persona, diagnostics, and ordinary prose must not substitute, summarize, decorate, or rescue that packet.

Aliases belong on the owning Library, Service, or Program block. Do not create detached alias registries that duplicate ownership truth.

## Checks

- Does the selected owner match the terminal packet owner?
- Did any support layer add public text after packet construction?
- Is alias metadata declared on the owning block?

## Tests

- Auth success cannot become a semantic acknowledgement.
- OPSEC hardwall cannot append helpful alternatives.
- EchoTrace can trace a target without executing that target.
