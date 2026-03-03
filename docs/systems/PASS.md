# PASS — Pattern Analysis Support System
Version: v1.0
Baseline: Preview Track
Date: 2026-03-03

## Definition
PASS is a deterministic extraction engine that converts source material into enforceable patterns, gates, and merge-ready artifacts.

PASS does:
- Strip-mine structured material
- Extract laws (patterns)
- Convert rules into IF/THEN gates
- Output merge-ready artifacts

PASS does NOT:
- Select APs
- Execute skills
- Teach (Drills teach)
- Store copyrighted source material

---

## Modes

### PASS:GUT
Full extraction at maximum depth.

### PASS:GUT-LADDER
Full extraction structured through Step Ladder:
0 — Concept constraints
1 — Structural systems
2 — Mechanics
3 — Refinement logic
4 — Production standards

### PASS:MERGE
Integrates extracted gates into canonical AP/Pattern system.

### PASS:REJECT
Rejects material if redundant, inferior, unverifiable, or stylistic noise.

---

## Output Schema (Non‑Negotiable)

Every gate must include:
- Gate ID
- Domain
- IF (Trigger)
- THEN (Requirement)
- PASS condition
- FAIL condition
- Evidence artifact
- Exceptions
- Source reference note (no verbatim text)

---

## Merge Law

Patterns:
- One canonical pattern per rule.
- Variants must be labeled.
- No duplicates.

APs:
- May reference patterns.
- May not redefine patterns.

Drills:
- Teach application.
- Do not redefine laws.

---

## Rejection Law

Reject if:
- Already covered by stronger canonical pattern
- Stylistic preference disguised as rule
- Redundant phrasing
- No testable condition
- No evidence requirement

---

## Canon Placement

Patterns → skills/.../patterns/
AP updates → skills/.../aps/
Drills → skills/.../drills/
PASS runs → docs/pass_runs/
Ledger → docs/ledger/
