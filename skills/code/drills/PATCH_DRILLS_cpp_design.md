# DRILLS PATCH — Modern C++ Design: Generic Programming and Design Patterns Applied

Append or merge into an appropriate drills file under `skills/code/drills/`.

---

module_set: DRILLS_PATCH
status: READY
modules:
  - module: DRL-CODE-DESIGN-CPP-001
    name: "Policy First Sketch"
    ladder:
      step_0: {do: ["Define goal + acceptance"], checkpoints: [PAT-CODE-GLOBAL-INTENT]}
      step_1: {do: ["Sketch skeleton"], checkpoints: []}
      step_2: {do: ["Write contracts"], checkpoints: [PAT-CODE-GLOBAL-CONTRACTS]}
      step_3: {do: ["Implement minimal path"], checkpoints: []}
      step_4: {do: ["Add tests"], checkpoints: [PAT-CODE-GLOBAL-TESTING_VALIDATION]}
    steps:
      - "Pick one invariant (e.g., bounds, ownership)"
      - "Write a type/policy to encode it"
      - "List misuse cases and how the type stops them"

  - module: DRL-CODE-DESIGN-CPP-002
    name: "Variability Seam Refactor"
    ladder:
      step_0: {do: ["Define goal + acceptance"], checkpoints: [PAT-CODE-GLOBAL-INTENT]}
      step_1: {do: ["Sketch skeleton"], checkpoints: []}
      step_2: {do: ["Write contracts"], checkpoints: [PAT-CODE-GLOBAL-CONTRACTS]}
      step_3: {do: ["Implement minimal path"], checkpoints: []}
      step_4: {do: ["Add tests"], checkpoints: [PAT-CODE-GLOBAL-TESTING_VALIDATION]}
    steps:
      - "Find 3 conditionals scattered across code"
      - "Introduce one seam (strategy/policy)"
      - "Rewrite callers to depend only on seam"

