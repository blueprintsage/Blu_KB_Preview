# PATCH_APPEND — PATTERNS-CODE (Thinking in Java (4th Edition))

Append these modules under an appropriate cluster in `skills/code/patterns/PATTERNS-CODE.md`.

---

module_set: PATTERNS_PATCH
status: READY
modules:
  - module: CODE-OOP-001
    severity: HARD
    bind_stage: 2
    law:
      IF: "A dependency is introduced between components"
      THEN: "Depend on stable abstractions; hide concrete classes behind interfaces"
    notes: "Program to interfaces, not implementations."
    evidence:
      PASS: "Callers depend on interface; Implementations swappable in tests"
      FAIL: "Concrete types leak everywhere; Hard to mock/replace"

  - module: CODE-OOP-002
    severity: HARD
    bind_stage: 2
    law:
      IF: "Need to reuse behavior across types"
      THEN: "Compose objects; use inheritance only for true substitutability"
    notes: "Favor composition over inheritance for behavior reuse."
    evidence:
      PASS: "Shallow hierarchies; Behavior modular"
      FAIL: "Deep inheritance; Overridden behavior surprises"

  - module: CODE-OOP-003
    severity: HARD
    bind_stage: 2
    law:
      IF: "A class owns state that can drift"
      THEN: "Keep invariants centralized; validate on mutation boundaries"
    notes: "Encapsulation requires controlling mutation."
    evidence:
      PASS: "Invariants checked at setters/mutators; Illegal states unrepresentable"
      FAIL: "Public mutable fields; State changes anywhere"

  - module: CODE-OOP-004
    severity: HARD
    bind_stage: 2
    law:
      IF: "A method can fail"
      THEN: "Define what exceptions can be thrown and what callers must do"
    notes: "Exceptions are part of the contract."
    evidence:
      PASS: "Documented failure behavior; Callers handle or propagate intentionally"
      FAIL: "Random exceptions bubble; Callers guess behavior"

  - module: CODE-OOP-005
    severity: HARD
    bind_stage: 2
    law:
      IF: "Shared state exists across threads"
      THEN: "Define thread-safety policy (immutable, confined, synchronized) and enforce it"
    notes: "Concurrency requires explicit ownership and synchronization strategy."
    evidence:
      PASS: "Policy documented; Tests cover races"
      FAIL: "Ad-hoc synchronized blocks; Heisenbugs"

