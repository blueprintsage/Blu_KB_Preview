# PATTERNS-CODE (GLOBAL LAW)

**Scope:** Global code constraints (patterns-as-law) bound to the Step Ladder (0–4).

- status: ACTIVE
- domain: code
- role: global_law

---

module_set: PATTERNS
status: ACTIVE
domain: code

modules:
  - module: PAT-CODE-GLOBAL-INTENT
    severity: HARD
    bind_stage: 0
    law:
      IF: "Work begins on a coding task"
      THEN: "Define success criteria, constraints, and I/O expectations before design or implementation"
    evidence:
      PASS: "Step 0 spec exists (goal, constraints, I/O, acceptance)"
      FAIL: "Implementation proceeds with undefined success criteria"
    failure_signatures:
      - "scope creep mid-implementation"
      - "rework due to missing requirements"

  - module: PAT-CODE-GLOBAL-CONTRACTS
    severity: HARD
    bind_stage: 2
    law:
      IF: "A component boundary exists (module/function/service boundary)"
      THEN: "Define contracts: inputs, outputs, invariants, error behavior"
    evidence:
      PASS: "Contracts documented + referenced by implementation/tests"
      FAIL: "Implicit contracts discovered only after bugs"
    failure_signatures:
      - "mismatched expectations between components"
      - "undefined error behavior"

  - module: PAT-CODE-GLOBAL-FAILURE_HANDLING
    severity: HARD
    bind_stage: 3
    law:
      IF: "An operation can fail (I/O, parsing, network, external call)"
      THEN: "Handle failures explicitly (validation, retries where appropriate, graceful errors)"
    evidence:
      PASS: "Known failure modes covered with explicit behavior"
      FAIL: "Unhandled exceptions or silent corruption"
    failure_signatures:
      - "crashes on bad input"
      - "partial writes / inconsistent state"

  - module: PAT-CODE-GLOBAL-TESTING_VALIDATION
    severity: HARD
    bind_stage: 4
    law:
      IF: "Claiming completion"
      THEN: "Provide evidence: tests, checks, or reproducible verification"
    evidence:
      PASS: "Acceptance tests or verification checklist exists + passes"
      FAIL: "Done declared without evidence"
    failure_signatures:
      - "works on my machine"
      - "regression after minor change"

  - module: PAT-CODE-GLOBAL-SECURITY_HYGIENE
    severity: HARD
    bind_stage: 2
    law:
      IF: "Handling external input or secrets"
      THEN: "Validate inputs, never hardcode secrets, and document sensitive flows"
    evidence:
      PASS: "Input validation + secrets handled via env/secret store"
      FAIL: "Secrets in code or unsafe input handling"
    failure_signatures:
      - "injection risk"
      - "keys committed to repo"

  - module: PAT-CODE-GLOBAL-OBSERVABILITY
    severity: SOFT
    bind_stage: 3
    law:
      IF: "Running code in a long-lived or user-facing context"
      THEN: "Add structured logs/metrics sufficient to debug failures"
    evidence:
      PASS: "Logs indicate actions, errors, and key state transitions"
      FAIL: "No visibility when failure occurs"
    failure_signatures:
      - "cannot reproduce failure"
      - "unknown state at crash"

  - module: PAT-CODE-GLOBAL-RECOVERY
    severity: HARD
    bind_stage: 3
    law:
      IF: "System destabilizes (bugs, confusion, drift)"
      THEN: "Return to contracts + minimal skeleton, re-implement incrementally, re-verify"
    evidence:
      PASS: "Recovery steps executed; minimal tests passing"
      FAIL: "Patch-on-patch without re-baselining"
    failure_signatures:
      - "whack-a-mole fixes"
      - "unstable behavior after patches"
