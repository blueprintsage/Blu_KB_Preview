# PASS:GUT-LADDER — Learning Python (5th Edition)
Generated: 2026-03-03T00:57:33.348329

**Disposition:** PASS (patterns + drills extracted)

## Quick Map (outline/headings)
- Table of Contents
- Preface
- This Book’s “Ecosystem”
- About This Fifth Edition
- The Python 2.X and 3.X Lines
- The 2.X/3.X Story Today
- Coverage for Both 3.X and 2.X
- Which Python Should I Use?
- This Book’s Prerequisites and Effort
- This Book’s Structure
- What This Book Is Not
- It’s Not a Reference or a Guide to Specific Applications
- It’s Not the Short Story for People in a Hurry
- It’s as Linear as Python Allows
- This Book’s Programs
- Python Versions
- Platforms
- Fetching This Book’s Code
- Using This Book’s Code
- Font Conventions

## Surface Scan (first pages keywords)
- keywords_detected: api, design, http, interface, prompt, types

---

module_set: PASS_GUT_LADDER
status: PASSED
domain: code
subject: python_fundamentals

modules:
  - gate: CODE-PY-001
    standard: "Prefer explicit over implicit for public APIs."
    IF: "Exposing functions/classes for reuse"
    THEN: "Document expectations and edge cases; keep names clear"
    PASS_evidence: ['Docstring/spec exists', 'Edge cases enumerated']
    FAIL_signals: ['Ambiguous behavior', 'Surprise defaults']

  - gate: CODE-PY-002
    standard: "Manage mutability deliberately."
    IF: "Using mutable defaults or shared state"
    THEN: "Avoid mutable default args; isolate shared state; copy when needed"
    PASS_evidence: ['No mutable defaults', 'State changes localized']
    FAIL_signals: ['Shared state leaks', 'Weird cross-call behavior']

  - gate: CODE-PY-003
    standard: "Iteration protocol must be correct."
    IF: "Building iterables/generators"
    THEN: "Define iteration semantics; ensure termination; test with large inputs"
    PASS_evidence: ['Generator ends correctly', 'Works with for/iter()']
    FAIL_signals: ['Infinite loop', 'Resource leaks']

  - gate: CODE-PY-004
    standard: "Exception boundaries should be narrow."
    IF: "Handling errors"
    THEN: "Wrap only what can fail; preserve traceback; raise meaningful exceptions"
    PASS_evidence: ['Narrow try blocks', 'Meaningful errors']
    FAIL_signals: ['Huge try blocks', 'Masked errors']

  - gate: CODE-PY-005
    standard: "Packaging and environment separation are part of 'done'."
    IF: "Delivering code to others"
    THEN: "Define dependencies and runnable entrypoints; avoid env bleed"
    PASS_evidence: ['Requirements declared', 'Repro run steps']
    FAIL_signals: ['Works only locally', 'Hidden deps']

## Drills extracted

module_set: DRILLS_EXTRACT
status: PASSED
modules:
  - module: DRL-CODE-PY-001
    name: "Mutability Trap Drill"
    steps:
      - "Create a function with default args"
      - "Observe bug with mutable default"
      - "Fix and write regression test"

  - module: DRL-CODE-PY-002
    name: "Generator Contract Drill"
    steps:
      - "Write generator for big input"
      - "Define termination and backpressure rules"
      - "Test with large N and edge cases"

