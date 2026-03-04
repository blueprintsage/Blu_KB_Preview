[CAPSULE_HEADER_BEGIN]
capsule_id: blu__pel_index
title: "PEL Index"
date: 2026-02-18
updated: 2026-02-21
version: 1.0.1
status: active
topic: pel
type: index
tags: [pel, library, ops, ribbons, burnin]
visibility: shared
[CAPSULE_HEADER_END]

# PEL Index

PEL = **pattern library** + **ops mechanics**.

- **Library** = reusable patterns/playbooks (your modular PEL file).
- **Ops** = ribbon mapping + burn-in drills (mechanics/reference).
## Templates

- `templates/pel/TEMPLATE_PEL_LIBRARY_ENTRY.md`
- `templates/pel/TEMPLATE_PEL_OPS_ENTRY.md`


## Locations

### Library
- `pel/library/Public_Experience_Library.md`

### Ops
- `pel/ops/PEL_Emotion_BurnIn_Suite.md`
- `pel/ops/PEL_Ribbon_PEL_Matrix_Mapping.md`
- `pel/ops/PEL-OPS-001.md`
- `pel/ops/PEL-OPS-002.md`
- `pel/ops/PEL-OPS-003.md`

## Precedence
**Operations Law + Anchors** override any PEL entry that conflicts with safety/OPSEC.

## Auto-light behavior (canonical)
If `prefs.pel.consult=auto_light`:
1) Detect a matching signal
2) Consult PEL library if available
3) Apply only **one small slice** (one drill/step + acceptance checks)
4) Do not dump full entries