# DRILLS PATCH — Thinking in Java (4th Edition)

Append or merge into an appropriate drills file under `skills/code/drills/`.

---

module_set: DRILLS_PATCH
status: READY
modules:
  - module: DRL-CODE-OOP-001
    name: "Interface Extraction"
    ladder:
      step_0: {do: ["Define goal + acceptance"], checkpoints: [PAT-CODE-GLOBAL-INTENT]}
      step_1: {do: ["Sketch skeleton"], checkpoints: []}
      step_2: {do: ["Write contracts"], checkpoints: [PAT-CODE-GLOBAL-CONTRACTS]}
      step_3: {do: ["Implement minimal path"], checkpoints: []}
      step_4: {do: ["Add tests"], checkpoints: [PAT-CODE-GLOBAL-TESTING_VALIDATION]}
    steps:
      - "Pick a concrete dependency"
      - "Extract minimal interface"
      - "Replace usage with interface + mock test"

  - module: DRL-CODE-OOP-002
    name: "Encapsulation Audit"
    ladder:
      step_0: {do: ["Define goal + acceptance"], checkpoints: [PAT-CODE-GLOBAL-INTENT]}
      step_1: {do: ["Sketch skeleton"], checkpoints: []}
      step_2: {do: ["Write contracts"], checkpoints: [PAT-CODE-GLOBAL-CONTRACTS]}
      step_3: {do: ["Implement minimal path"], checkpoints: []}
      step_4: {do: ["Add tests"], checkpoints: [PAT-CODE-GLOBAL-TESTING_VALIDATION]}
    steps:
      - "List mutable fields"
      - "Define invariants"
      - "Refactor writes through checked methods + tests"

