# Exec — Debug Arbitration Trace (v2)

---

module: kb__protocols_exec_exec_debug_trace_v2.M01 | name="Content"
[CAPSULE_HEADER_BEGIN]
mem_id: 2026_02_28__blu__exec-debug-trace-v2
title: Exec — Debug Arbitration Trace (v2)
date: 2026-02-28
status: draft
topic: blu
type: spec
tags: exec, debug, trace, arbitration
sensitivity: medium
visibility: private
source: roadmap
domain: ops
authority: canon
[CAPSULE_HEADER_END]

## Command surface

- `EXEC DEBUG ON`
- `EXEC DEBUG OFF`

When `EXEC_META.mode=DEBUG`, Exec may emit a compact trace block **after** the single interrupt line,
or on-demand via `EXEC:TRACE` (optional).

## Trace shape (compact)

```text
[EXEC TRACE]
now_utc=<iso>
flow_state=<OPEN|FOCUS|SCHOOL|MIDWORK>
candidates=<N>
selected=<proposal_id> kind=<kind> prio=<p> suppress_key=<k>
suppressed=[<k1>, <k2>]
rejected=[(<proposal_id>, reason), ...]
```

## Rules

- Trace output must remain **deterministic** and **bounded**.
- Never print secrets or raw user content beyond proposal identifiers/titles already surfaced.
- In NORMAL mode, no trace is emitted.
