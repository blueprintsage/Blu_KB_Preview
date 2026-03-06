# Skill Forge Dual-Lane Contract
Version: v1.1
Date: 2026-03-05
depends_on:
  - contracts/Error_handling_contract.md
  - contracts/error_macros.md

## Purpose
Skill Forge subjects must ship in **two lanes**:
- **Lane B (Blu Runtime)**: canonical “laws” in **markdown capsule form** for reliable indexing + human audit.
- **Lane A (Teaching Pack)**: compiled teaching capsule derived from Lane B.

**Optional:** A raw object store may be produced for diagnostics or future automation, but it is not the primary shipped artifact unless explicitly requested.

---

## Global Law (Fail-Closed)
If any REQUIRED dependency is missing/expired/unreadable at any stage, invoke ERRMAC and STOP (no partial packs, no “best effort” dumps).

---

## Identity Law (REQUIRED)
SkillForge output MUST be keyed by **skill tree identity**, not book slug:
- `top_skill` (e.g., programming, art, writing)
- `subskill` (snake_case node; e.g., algorithms, software_craft)
- `book_slug` (kebab-case; for registry only; MUST NOT be used as the directory key)
- `lens_subject` (coarse key for lens selection only)

If `top_skill` or `subskill` is missing, STOP.

---

## Folder & File Requirements (Canonical)

### Canonical capsule layout (REQUIRED)
skills/<top_skill>/<subskill>/
    Skills/
        <SUBSKILL>_B.md      (required)
    Teaching/
        <SUBSKILL>_A.md      (required)
    INDEX.md                (required; links to A/B + ledgers)
    ledger/                 (optional)
        ledger.json         (optional)
        action_plans.json   (optional)
        variants.json       (optional)

### Optional raw object store (ALLOWED)
skills/<top_skill>/<subskill>/_raw/
    patterns.jsonl          (optional)
    drills.jsonl            (optional)
    tests.jsonl             (optional)

---

## Rendering Law (REQUIRED)
- Lane B markdown MUST be generated from the normalized objects (patterns/APs/variants/drills/tests).
- Lane A markdown MUST be compiled from Lane B (IDs, titles, sequencing) and may embed or summarize.

---

## Backward-compatibility note (NON-AUTHORITY)
Older packs may have used:
- skills/<domain>/<subject>/patterns|tests|drills|ledger
- teaching/<domain>/<subject>/*.md

These layouts are not canonical under v1.1. If emitted at all, they must live under `_raw/` within the canonical skill-tree node.

