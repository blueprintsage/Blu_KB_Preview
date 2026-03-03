# SMOKES — PASS:GUT (ART)
**Purpose:** Prevent PASS:GUT behavior regressions.

## Smoke 01 — PASS:GUT outputs all deliverables
Prompt:
- `PASS:GUT (ART) — <PDF>`

Expected:
- Outputs:
  1) GUT Sheet
  2) Drill Set (2 easy, 2 medium, 1 hard) + pass checks
  3) 7-day rep plan (10–20 min/day)

Fail if:
- Any deliverable is missing
- Output is only a summary without drills + rep plan
