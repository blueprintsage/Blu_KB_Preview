# PATCH_APPEND — PATTERNS-CODE (Modern C++ Design: Generic Programming and Design Patterns Applied)

Append these modules under an appropriate cluster in `skills/code/patterns/PATTERNS-CODE.md`.

---

module_set: PATTERNS_PATCH
status: READY
modules:
  - module: CODE-DESIGN-CPP-001
    severity: HARD
    bind_stage: 2
    law:
      IF: "Designing a reusable component with invariants"
      THEN: "Prefer types/policies to enforce invariants early; document runtime fallbacks"
    notes: "Policies encode invariants at compile time when feasible."
    evidence:
      PASS: "Policy/type contract exists; Misuse fails fast (compile-time or early runtime)"
      FAIL: "Invariants enforced only by comments; Silent misuse possible"

  - module: CODE-DESIGN-CPP-002
    severity: HARD
    bind_stage: 2
    law:
      IF: "A design has multiple interchangeable strategies"
      THEN: "Isolate variability behind a stable interface; avoid scattering conditionals"
    notes: "Separate variability from mechanism."
    evidence:
      PASS: "Single variability seam exists; Strategies swappable without touching callers"
      FAIL: "Conditionals spread across codebase; Callers depend on concrete types"

  - module: CODE-DESIGN-CPP-003
    severity: HARD
    bind_stage: 2
    law:
      IF: "Reuse is needed across unrelated types"
      THEN: "Use templates/composition to reuse behavior; keep inheritance for substitutability"
    notes: "Prefer generic composition over inheritance for reuse."
    evidence:
      PASS: "Reuse achieved without deep hierarchies; Behavior testable in isolation"
      FAIL: "Inheritance used solely to share code; Fragile base class symptoms"

  - module: CODE-DESIGN-CPP-004
    severity: HARD
    bind_stage: 2
    law:
      IF: "Metaprogramming constructs aggregate types/components"
      THEN: "Define the boundary (what is in/out) and how new items are added; avoid hidden coupling"
    notes: "Type lists / registries must have explicit ownership and boundaries."
    evidence:
      PASS: "Registry entry process documented; Compile-time errors are legible"
      FAIL: "Mystery types appear via includes; Errors are untraceable"

  - module: CODE-DESIGN-CPP-005
    severity: HARD
    bind_stage: 2
    law:
      IF: "Template-heavy systems are exposed to users"
      THEN: "Provide static assertions / constraints with actionable messages"
    notes: "Error messages are part of the developer experience."
    evidence:
      PASS: "Failure points explain required shape; Docs point to fixes"
      FAIL: "Raw template spew; No guidance on constraints"

