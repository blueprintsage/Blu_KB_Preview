# PATCH_APPEND — PATTERNS-CODE (Ultimate Beginner’s Guide to C# Programming (Step-by-step))

Append these modules under an appropriate cluster in `skills/code/patterns/PATTERNS-CODE.md`.

---

module_set: PATTERNS_PATCH
status: READY
modules:
  - module: CODE-CSHARP-001
    severity: HARD
    bind_stage: 2
    law:
      IF: "Reading user/external input"
      THEN: "Validate and sanitize before use; fail with clear errors"
    notes: "Inputs must be validated at boundaries."
    evidence:
      PASS: "Validation present; Bad input handled gracefully"
      FAIL: "Assumes valid input; Crashes on edge cases"

  - module: CODE-CSHARP-002
    severity: HARD
    bind_stage: 2
    law:
      IF: "Designing functions/objects"
      THEN: "Use appropriate types (enums, structs, classes) instead of magic numbers/strings"
    notes: "Use types to communicate intent."
    evidence:
      PASS: "No magic constants; Intent readable from signatures"
      FAIL: "Stringly typed state; Magic values"

  - module: CODE-CSHARP-003
    severity: HARD
    bind_stage: 2
    law:
      IF: "A function grows beyond one responsibility"
      THEN: "Split into cohesive units; name by responsibility"
    notes: "Keep functions small and single-purpose."
    evidence:
      PASS: "Functions have one reason to change; Tests target units"
      FAIL: "God functions; Hard to test"

  - module: CODE-CSHARP-004
    severity: HARD
    bind_stage: 2
    law:
      IF: "Iterating over collections"
      THEN: "Prefer clarity; guard bounds; avoid off-by-one"
    notes: "Collections and loops must be correct before clever."
    evidence:
      PASS: "Bounds safe; Clear iteration"
      FAIL: "Index errors; Hidden assumptions"

  - module: CODE-CSHARP-005
    severity: HARD
    bind_stage: 2
    law:
      IF: "Catching errors"
      THEN: "Catch expected exceptions; avoid blanket catches that hide bugs"
    notes: "Exception handling must be specific."
    evidence:
      PASS: "Specific catches; Errors logged/returned"
      FAIL: "catch-all hides issues; Silent failure"

