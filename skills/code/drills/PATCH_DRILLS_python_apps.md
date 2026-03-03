# DRILLS PATCH — Programming Python (4th Edition)

Append or merge into an appropriate drills file under `skills/code/drills/`.

---

module_set: DRILLS_PATCH
status: READY
modules:
  - module: DRL-CODE-PYAPP-001
    name: "CLI Wrapper Discipline"
    ladder:
      step_0: {do: ["Define goal + acceptance"], checkpoints: [PAT-CODE-GLOBAL-INTENT]}
      step_1: {do: ["Sketch skeleton"], checkpoints: []}
      step_2: {do: ["Write contracts"], checkpoints: [PAT-CODE-GLOBAL-CONTRACTS]}
      step_3: {do: ["Implement minimal path"], checkpoints: []}
      step_4: {do: ["Add tests"], checkpoints: [PAT-CODE-GLOBAL-TESTING_VALIDATION]}
    steps:
      - "Write core function with no I/O"
      - "Write CLI parsing layer"
      - "Test core separately"

  - module: DRL-CODE-PYAPP-002
    name: "Resource Lifetime Drill"
    ladder:
      step_0: {do: ["Define goal + acceptance"], checkpoints: [PAT-CODE-GLOBAL-INTENT]}
      step_1: {do: ["Sketch skeleton"], checkpoints: []}
      step_2: {do: ["Write contracts"], checkpoints: [PAT-CODE-GLOBAL-CONTRACTS]}
      step_3: {do: ["Implement minimal path"], checkpoints: []}
      step_4: {do: ["Add tests"], checkpoints: [PAT-CODE-GLOBAL-TESTING_VALIDATION]}
    steps:
      - "Open file/socket"
      - "Force exception mid-way"
      - "Prove resource closed (test/log)"

