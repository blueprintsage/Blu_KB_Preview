# DRILLS PATCH — Building AI Applications with OpenAI APIs (2nd ed., 2024)

Append or merge into an appropriate drills file under `skills/code/drills/`.

---

module_set: DRILLS_PATCH
status: READY
modules:
  - module: DRL-CODE-AI-001
    name: "Eval Harness First"
    ladder:
      step_0: {do: ["Define goal + acceptance"], checkpoints: [PAT-CODE-GLOBAL-INTENT]}
      step_1: {do: ["Sketch skeleton"], checkpoints: []}
      step_2: {do: ["Write contracts"], checkpoints: [PAT-CODE-GLOBAL-CONTRACTS]}
      step_3: {do: ["Implement minimal path"], checkpoints: []}
      step_4: {do: ["Add tests"], checkpoints: [PAT-CODE-GLOBAL-TESTING_VALIDATION]}
    steps:
      - "Write 20 test prompts"
      - "Define success rubric"
      - "Run baseline, then change one thing and compare"

  - module: DRL-CODE-AI-002
    name: "Injection Boundary Test"
    ladder:
      step_0: {do: ["Define goal + acceptance"], checkpoints: [PAT-CODE-GLOBAL-INTENT]}
      step_1: {do: ["Sketch skeleton"], checkpoints: []}
      step_2: {do: ["Write contracts"], checkpoints: [PAT-CODE-GLOBAL-CONTRACTS]}
      step_3: {do: ["Implement minimal path"], checkpoints: []}
      step_4: {do: ["Add tests"], checkpoints: [PAT-CODE-GLOBAL-TESTING_VALIDATION]}
    steps:
      - "Create adversarial inputs"
      - "Verify boundaries (system/dev/user separation)"
      - "Add sanitization and re-test"

