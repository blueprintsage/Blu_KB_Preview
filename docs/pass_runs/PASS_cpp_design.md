# PASS:GUT-LADDER — Modern C++ Design: Generic Programming and Design Patterns Applied
Generated: 2026-03-03T00:57:25.388882

**Disposition:** PASS (patterns + drills extracted)

## Quick Map (outline/headings)
- sample.pdf
- sterling.com
- Welcome to Sterling Software
- Modern C++ Design.pdf
- Table of Content
- Copyright
- Foreword
- Foreword
- Preface
- Audience
- Loki
- Organization
- Acknowledgments
- Part I: Techniques
- Chapter 1. Policy-Based Class Design
- 1.1 The Multiplicity of Software Design
- 1.2 The Failure of the Do-It-All Interface
- 1.3 Multiple Inheritance to the Rescue?
- 1.4 The Benefit of Templates
- 1.5 Policies and Policy Classes

## Surface Scan (first pages keywords)
- keywords_detected: api, design, eval, http, interface, logging, memory, pattern, template, types

---

module_set: PASS_GUT_LADDER
status: PASSED
domain: code
subject: cpp_design

modules:
  - gate: CODE-DESIGN-CPP-001
    standard: "Policies encode invariants at compile time when feasible."
    IF: "Designing a reusable component with invariants"
    THEN: "Prefer types/policies to enforce invariants early; document runtime fallbacks"
    PASS_evidence: ['Policy/type contract exists', 'Misuse fails fast (compile-time or early runtime)']
    FAIL_signals: ['Invariants enforced only by comments', 'Silent misuse possible']

  - gate: CODE-DESIGN-CPP-002
    standard: "Separate variability from mechanism."
    IF: "A design has multiple interchangeable strategies"
    THEN: "Isolate variability behind a stable interface; avoid scattering conditionals"
    PASS_evidence: ['Single variability seam exists', 'Strategies swappable without touching callers']
    FAIL_signals: ['Conditionals spread across codebase', 'Callers depend on concrete types']

  - gate: CODE-DESIGN-CPP-003
    standard: "Prefer generic composition over inheritance for reuse."
    IF: "Reuse is needed across unrelated types"
    THEN: "Use templates/composition to reuse behavior; keep inheritance for substitutability"
    PASS_evidence: ['Reuse achieved without deep hierarchies', 'Behavior testable in isolation']
    FAIL_signals: ['Inheritance used solely to share code', 'Fragile base class symptoms']

  - gate: CODE-DESIGN-CPP-004
    standard: "Type lists / registries must have explicit ownership and boundaries."
    IF: "Metaprogramming constructs aggregate types/components"
    THEN: "Define the boundary (what is in/out) and how new items are added; avoid hidden coupling"
    PASS_evidence: ['Registry entry process documented', 'Compile-time errors are legible']
    FAIL_signals: ['Mystery types appear via includes', 'Errors are untraceable']

  - gate: CODE-DESIGN-CPP-005
    standard: "Error messages are part of the developer experience."
    IF: "Template-heavy systems are exposed to users"
    THEN: "Provide static assertions / constraints with actionable messages"
    PASS_evidence: ['Failure points explain required shape', 'Docs point to fixes']
    FAIL_signals: ['Raw template spew', 'No guidance on constraints']

## Drills extracted

module_set: DRILLS_EXTRACT
status: PASSED
modules:
  - module: DRL-CODE-DESIGN-CPP-001
    name: "Policy First Sketch"
    steps:
      - "Pick one invariant (e.g., bounds, ownership)"
      - "Write a type/policy to encode it"
      - "List misuse cases and how the type stops them"

  - module: DRL-CODE-DESIGN-CPP-002
    name: "Variability Seam Refactor"
    steps:
      - "Find 3 conditionals scattered across code"
      - "Introduce one seam (strategy/policy)"
      - "Rewrite callers to depend only on seam"

