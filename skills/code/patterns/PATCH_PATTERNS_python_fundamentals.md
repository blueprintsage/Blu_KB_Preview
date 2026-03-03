# PATCH_APPEND — PATTERNS-CODE (Learning Python (5th Edition))

Append these modules under an appropriate cluster in `skills/code/patterns/PATTERNS-CODE.md`.

---

module_set: PATTERNS_PATCH
status: READY
modules:
  - module: CODE-PY-001
    severity: HARD
    bind_stage: 2
    law:
      IF: "Exposing functions/classes for reuse"
      THEN: "Document expectations and edge cases; keep names clear"
    notes: "Prefer explicit over implicit for public APIs."
    evidence:
      PASS: "Docstring/spec exists; Edge cases enumerated"
      FAIL: "Ambiguous behavior; Surprise defaults"

  - module: CODE-PY-002
    severity: HARD
    bind_stage: 2
    law:
      IF: "Using mutable defaults or shared state"
      THEN: "Avoid mutable default args; isolate shared state; copy when needed"
    notes: "Manage mutability deliberately."
    evidence:
      PASS: "No mutable defaults; State changes localized"
      FAIL: "Shared state leaks; Weird cross-call behavior"

  - module: CODE-PY-003
    severity: HARD
    bind_stage: 2
    law:
      IF: "Building iterables/generators"
      THEN: "Define iteration semantics; ensure termination; test with large inputs"
    notes: "Iteration protocol must be correct."
    evidence:
      PASS: "Generator ends correctly; Works with for/iter()"
      FAIL: "Infinite loop; Resource leaks"

  - module: CODE-PY-004
    severity: HARD
    bind_stage: 2
    law:
      IF: "Handling errors"
      THEN: "Wrap only what can fail; preserve traceback; raise meaningful exceptions"
    notes: "Exception boundaries should be narrow."
    evidence:
      PASS: "Narrow try blocks; Meaningful errors"
      FAIL: "Huge try blocks; Masked errors"

  - module: CODE-PY-005
    severity: HARD
    bind_stage: 2
    law:
      IF: "Delivering code to others"
      THEN: "Define dependencies and runnable entrypoints; avoid env bleed"
    notes: "Packaging and environment separation are part of 'done'."
    evidence:
      PASS: "Requirements declared; Repro run steps"
      FAIL: "Works only locally; Hidden deps"

