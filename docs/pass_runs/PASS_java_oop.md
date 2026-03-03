# PASS:GUT-LADDER — Thinking in Java (4th Edition)
Generated: 2026-03-03T00:57:26.286561

**Disposition:** PASS (patterns + drills extracted)

## Quick Map (outline/headings)
- Thinking in Java
- Content

## Surface Scan (first pages keywords)
- keywords_detected: api, design

---

module_set: PASS_GUT_LADDER
status: PASSED
domain: code
subject: java_oop

modules:
  - gate: CODE-OOP-001
    standard: "Program to interfaces, not implementations."
    IF: "A dependency is introduced between components"
    THEN: "Depend on stable abstractions; hide concrete classes behind interfaces"
    PASS_evidence: ['Callers depend on interface', 'Implementations swappable in tests']
    FAIL_signals: ['Concrete types leak everywhere', 'Hard to mock/replace']

  - gate: CODE-OOP-002
    standard: "Favor composition over inheritance for behavior reuse."
    IF: "Need to reuse behavior across types"
    THEN: "Compose objects; use inheritance only for true substitutability"
    PASS_evidence: ['Shallow hierarchies', 'Behavior modular']
    FAIL_signals: ['Deep inheritance', 'Overridden behavior surprises']

  - gate: CODE-OOP-003
    standard: "Encapsulation requires controlling mutation."
    IF: "A class owns state that can drift"
    THEN: "Keep invariants centralized; validate on mutation boundaries"
    PASS_evidence: ['Invariants checked at setters/mutators', 'Illegal states unrepresentable']
    FAIL_signals: ['Public mutable fields', 'State changes anywhere']

  - gate: CODE-OOP-004
    standard: "Exceptions are part of the contract."
    IF: "A method can fail"
    THEN: "Define what exceptions can be thrown and what callers must do"
    PASS_evidence: ['Documented failure behavior', 'Callers handle or propagate intentionally']
    FAIL_signals: ['Random exceptions bubble', 'Callers guess behavior']

  - gate: CODE-OOP-005
    standard: "Concurrency requires explicit ownership and synchronization strategy."
    IF: "Shared state exists across threads"
    THEN: "Define thread-safety policy (immutable, confined, synchronized) and enforce it"
    PASS_evidence: ['Policy documented', 'Tests cover races']
    FAIL_signals: ['Ad-hoc synchronized blocks', 'Heisenbugs']

## Drills extracted

module_set: DRILLS_EXTRACT
status: PASSED
modules:
  - module: DRL-CODE-OOP-001
    name: "Interface Extraction"
    steps:
      - "Pick a concrete dependency"
      - "Extract minimal interface"
      - "Replace usage with interface + mock test"

  - module: DRL-CODE-OOP-002
    name: "Encapsulation Audit"
    steps:
      - "List mutable fields"
      - "Define invariants"
      - "Refactor writes through checked methods + tests"

