# AP-CODE-SYSTEMS-001

**Scope:** Language-agnostic spine for building software systems using the Step Ladder (0–4).

- status: ACTIVE
- domain: code
- subject: systems
- role: spine
- notes: Patterns are law. Languages come later as modules.

---

module_set: AP
status: ACTIVE
domain: code
subject: systems
role: spine

modules:
  - module: AP.BASE
    purpose: "Build software deterministically from intent to validated completion."
    governing_patterns:
      - PAT-CODE-GLOBAL-INTENT
      - PAT-CODE-GLOBAL-CONTRACTS
      - PAT-CODE-GLOBAL-FAILURE_HANDLING
      - PAT-CODE-GLOBAL-TESTING_VALIDATION
      - PAT-CODE-GLOBAL-SECURITY_HYGIENE
      - PAT-CODE-GLOBAL-OBSERVABILITY
      - PAT-CODE-GLOBAL-RECOVERY

    ladder_order:
      - step: 0
        name: Intent Lock
        outputs:
          - "Problem statement"
          - "Constraints (time/memory/security)"
          - "I/O expectations"
          - "Acceptance criteria"
        checks:
          - "Success criteria explicit"
          - "Non-goals explicit"

      - step: 1
        name: Skeleton (Architecture)
        outputs:
          - "Component sketch (modules/functions)"
          - "Data flow sketch"
          - "Risk list (top 3)"
        checks:
          - "Minimal viable path exists"
          - "Dependencies identified"

      - step: 2
        name: Block (Contracts)
        outputs:
          - "Interfaces/contracts"
          - "Schemas/types (even informal)"
          - "Edge cases + failure modes list"
        checks:
          - "Contracts define error behavior"
          - "Input validation planned"

      - step: 3
        name: Rough (Implementation)
        outputs:
          - "Working implementation of minimal path"
          - "Instrumentation/logging where relevant"
          - "Explicit error handling for known failures"
        checks:
          - "No silent failure"
          - "Behavior matches contracts"

      - step: 4
        name: Final (Validation + Packaging)
        outputs:
          - "Tests (unit/integration/acceptance as appropriate)"
          - "Run instructions"
          - "Minimal docs"
        checks:
          - "Evidence of completion exists"
          - "Regression-safe baseline"

    failure_modes:
      - signature: "Implementation starts with unclear requirements"
        prescribe:
          - step: 0
          - apply: PAT-CODE-GLOBAL-INTENT
      - signature: "Bugs at component boundaries"
        prescribe:
          - step: 2
          - apply: PAT-CODE-GLOBAL-CONTRACTS
      - signature: "Patch spiral / unstable system"
        prescribe:
          - step: 1
          - apply: PAT-CODE-GLOBAL-RECOVERY

  - module: AP.MOD.SCRIPT
    when: "Single-run tool or batch job"
    step_deltas:
      step_1_add:
        - "Decide CLI args / config inputs"
      step_4_add:
        - "Usage examples"
    notes:
      - "Keep contracts lightweight but explicit."

  - module: AP.MOD.LIBRARY
    when: "Reusable library/API intended for others"
    step_deltas:
      step_2_add:
        - "Public API surface definition"
      step_4_add:
        - "Versioning notes + changelog stub"
    notes:
      - "Stability and compatibility are first-class."

  - module: AP.MOD.SERVICE
    when: "Long-lived service (web API, daemon)"
    step_deltas:
      step_2_add:
        - "Reliability requirements (timeouts/retries)"
        - "Security boundary notes"
      step_3_add:
        - "Observability hooks"
      step_4_add:
        - "Health checks + runbook stub"
    notes:
      - "Failure modes must be explicitly designed."
