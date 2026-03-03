# DRILLS-CODE-FOUNDATIONS

**Scope:** Human teaching drills for the Code Step Ladder (0–4). Patterns are checkpoints.

- status: ACTIVE
- domain: code
- storage_mode: hybrid
- split_rule: drills>7 or lines>1200

---

module_set: DRILLS
status: ACTIVE
domain: code

modules:
  - module: DRL-CODE-FOUND-001
    name: "Step 0 Spec From Prompt"
    tags: [domain:code, phase:core, level:L0]
    lesson_goal: "Produce a Step 0 spec that blocks ambiguity."
    ladder:
      step_0:
        do:
          - "Write goal in 1–2 sentences"
          - "List constraints (time/memory/security)"
          - "Define inputs/outputs"
          - "Define acceptance checks"
        checkpoints:
          - PAT-CODE-GLOBAL-INTENT
      step_1:
        do: ["Sketch minimal components (3 boxes max)"]
        checkpoints: []
      step_2:
        do: ["List top 5 edge cases"]
        checkpoints: []
      step_3:
        do: ["Implement only the minimal happy path (stub ok)"]
        checkpoints: []
      step_4:
        do: ["Write 3 acceptance tests (even pseudo-tests)"]
        checkpoints: [PAT-CODE-GLOBAL-TESTING_VALIDATION]
    pass:
      - "Acceptance criteria are measurable"
      - "Constraints are explicit"
    fail:
      - "Vague success definition"
      - "No I/O defined"

  - module: DRL-CODE-FOUND-002
    name: "Contracts Before Code"
    tags: [domain:code, phase:core, level:L1]
    lesson_goal: "Define contracts (inputs/outputs/errors) for each component."
    ladder:
      step_0:
        do: ["Identify component boundaries"]
        checkpoints: []
      step_1:
        do: ["List components and responsibilities"]
        checkpoints: []
      step_2:
        do:
          - "Write contracts for each boundary"
          - "Define error behavior"
        checkpoints: [PAT-CODE-GLOBAL-CONTRACTS]
      step_3:
        do: ["Implement stubs that enforce contracts"]
        checkpoints: []
      step_4:
        do: ["Write tests that assert contract behavior"]
        checkpoints: [PAT-CODE-GLOBAL-TESTING_VALIDATION]
    pass:
      - "Error behaviors defined"
    fail:
      - "Contracts implied but not written"

  - module: DRL-CODE-FOUND-003
    name: "Failure Modes Table"
    tags: [domain:code, phase:integration, level:L1]
    lesson_goal: "Enumerate failures and choose explicit handling."
    ladder:
      step_0:
        do: ["List dependencies (files, network, user input)"]
        checkpoints: []
      step_1:
        do: ["Map where failures can occur"]
        checkpoints: []
      step_2:
        do: ["Write failure table: trigger → behavior → evidence"]
        checkpoints: [PAT-CODE-GLOBAL-FAILURE_HANDLING]
      step_3:
        do: ["Implement handling for top 3 failures"]
        checkpoints: []
      step_4:
        do: ["Test failure handling"]
        checkpoints: [PAT-CODE-GLOBAL-TESTING_VALIDATION]
