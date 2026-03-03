capsule_id: kb__index_pattern_library_md__dfb401
title: "Pattern Library"
date: 2026-02-24
updated: 2026-02-24
version: 0.1.0
status: draft
topic: blu
type: spec
tags: ['index']
sensitivity: medium
visibility: shared
source: repo
domain: index
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

<!--
Pattern Library (canonical)
Extracted from legacy Interim repo index into a single edit point.
Paste-safe: no YAML front matter.
-->

# Cross-Pack Pattern Library

## PAT-TPL-001 Pattern Template (copy/paste)
- **ID:** PAT-<AREA>-###
- **Use when:** …
- **Schema:** (inputs/constraints)
- **Steps:** 1…2…3…
- **Checks:** 2–5 observable pass criteria
- **Failure-modes:** Symptom → Cause → Fix (3–6)
- **Knobs:** 6–10 user-invokable toggles

## DRL-TPL-001 Drill Template (copy/paste)
- **ID:** DRL-<AREA>-###
- **Tier:** Beginner | Intermediate | Advanced
- **Prompt:** …
- **Timebox:** 5–15 min
- **Pass criteria:** …
- **Common misses:** …
- **Answer sketch (optional):** …


## PAT-CORE-001 Deliverable-First Output
**Use when:** user wants something they can paste/run/ship.  
**Recipe:** Deliverable → Checks → Failure-modes → Knobs → Next.

## PAT-CORE-002 Prompt Delta Iteration
**Use when:** iterating on prompts, prose, or specs.  
**Rule:** change one knob per iteration; show the delta explicitly.

## PAT-CORE-003 Completeness Rule
**Use when:** required section is missing/thin.  
**Rule:** re-export the whole output in the correct structure; don’t patch with one line.

## PAT-CORE-004 Micro-Demo
**Use when:** authoring a new pack.  
**Rule:** include ≤200 words (or ≤40 lines code) example + ≥2 checks.

---

---

module: pl.M99 | name="Maintenance"
## Maintenance
- Canonical source: `index/Pattern_Library.md`
- Keep DP-local working patterns inside their DPs.
- Keep cross-pack templates + core patterns here.
/module

*Last updated:* 2026-02-15
