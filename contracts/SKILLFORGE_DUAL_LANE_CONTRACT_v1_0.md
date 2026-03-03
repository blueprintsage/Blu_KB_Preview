# Skill Forge Dual-Lane Contract
Version: v1.0
Date: 2026-03-03

## Purpose
Skill Forge subjects must ship in **two lanes**:
- **Lane B (Blu Runtime)**: machine-first modular source-of-truth for parsing and enforcement.
- **Lane A (Teaching Pack)**: human-first compiled curriculum derived from Lane B.

This gives “best of both worlds”: fast internal execution + clean human instruction.

---

## Lane Definitions

### Lane B — Blu Runtime (Canonical)
**Role:** source-of-truth. Blu reads this by default.

**Design goals**
- Modular, small files for fast parsing
- Strict scope per module
- Semantic IDs (stable)
- Patterns expressed as enforceable gates/tests
- Ledgers record completion + version changes

**Must include**
- patterns (rules/gates)
- tests (proof detectors / scenario tests)
- ledger (what shipped, versioned)
- drills (optional; can exist here as “battery drills”)

**May include**
- modules (subcomponents / variants)

### Lane A — Teaching Pack (Compiled)
**Role:** human-facing curriculum. Humans read this by default.

**Design goals**
- Low file count
- Ordered syllabus
- Plain language, examples
- Practice plan and progression
- References back to Lane B module IDs

**Must include**
- README / overview
- SYLLABUS (path through the subject)
- PATTERNS (curated summary)
- DRILLS (human instruction)
- TESTS (clear pass/fail targets)

---

## Canonical Authority Rule
**Lane B is canonical. Lane A is a compiled view.**

- Lane A is updated only during **freezes/releases** (e.g., v1.2, v1.3).
- Lane B may evolve via patches between freezes.
- Every Lane A section should reference the relevant Lane B IDs/paths.

---

## Update & Freeze Workflow (Minimal)
1. Patch Lane B modules/patterns/tests.
2. Run smoke/proof tests (Lane B tests).
3. Freeze Lane A by compiling/curating from Lane B.
4. Write ledger entries for both lanes.
5. Update indexes.

---

## Folder & File Requirements

### Lane B required layout
skills/<domain>/<subject>/
    modules/          (optional)
    patterns/         (required)
    tests/            (required)
    drills/           (optional)
    ledger/           (required)

### Lane A required layout
teaching/<domain>/<subject>/
    README.md         (required)
    SYLLABUS.md       (required)
    PATTERNS.md       (required)
    DRILLS.md         (required)
    TESTS.md          (required)

---

## Indexing & IDs
- Semantic IDs must be stable once published.
- Index patches must be emitted with each pack.
- “One concept per module” is preferred for runtime parsing.

---

## Anti-Entropy Rules
- No duplicate rules with different names in the same lane.
- If two rules conflict, Lane B fixes first; Lane A compiles after.
- Keep fold budgets / line economy as explicit constraints when relevant.

---

## Success Criteria
A subject is “done” when:
- Lane B passes proof detectors and scenario tests
- Lane A teaches the subject end-to-end without relying on hidden knowledge
- Both lanes have ledgers + index patches
