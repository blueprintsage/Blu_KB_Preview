# DRILLS PATCH — The Art of Assembly Language (2nd Edition)

Append or merge into an appropriate drills file under `skills/code/drills/`.

---

module_set: DRILLS_PATCH
status: READY
modules:
  - module: DRL-CODE-ASM-001
    name: "ABI Checklist"
    ladder:
      step_0: {do: ["Define goal + acceptance"], checkpoints: [PAT-CODE-GLOBAL-INTENT]}
      step_1: {do: ["Sketch skeleton"], checkpoints: []}
      step_2: {do: ["Write contracts"], checkpoints: [PAT-CODE-GLOBAL-CONTRACTS]}
      step_3: {do: ["Implement minimal path"], checkpoints: []}
      step_4: {do: ["Add tests"], checkpoints: [PAT-CODE-GLOBAL-TESTING_VALIDATION]}
    steps:
      - "Pick target ABI"
      - "Write a function stub"
      - "Verify saved regs/stack alignment with tests or emulator"

  - module: DRL-CODE-ASM-002
    name: "Bit Layout Test Vectors"
    ladder:
      step_0: {do: ["Define goal + acceptance"], checkpoints: [PAT-CODE-GLOBAL-INTENT]}
      step_1: {do: ["Sketch skeleton"], checkpoints: []}
      step_2: {do: ["Write contracts"], checkpoints: [PAT-CODE-GLOBAL-CONTRACTS]}
      step_3: {do: ["Implement minimal path"], checkpoints: []}
      step_4: {do: ["Add tests"], checkpoints: [PAT-CODE-GLOBAL-TESTING_VALIDATION]}
    steps:
      - "Define bitfield layout"
      - "Write pack/unpack"
      - "Create 10 test vectors including edge cases"

