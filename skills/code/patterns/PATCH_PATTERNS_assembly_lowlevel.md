# PATCH_APPEND — PATTERNS-CODE (The Art of Assembly Language (2nd Edition))

Append these modules under an appropriate cluster in `skills/code/patterns/PATTERNS-CODE.md`.

---

module_set: PATTERNS_PATCH
status: READY
modules:
  - module: CODE-ASM-001
    severity: HARD
    bind_stage: 2
    law:
      IF: "Writing functions that call/are called"
      THEN: "Preserve required registers/stack discipline; document convention"
    notes: "Calling convention is a contract."
    evidence:
      PASS: "Prologue/epilogue correct; ABI respected"
      FAIL: "Stack imbalance; Clobbered regs"

  - module: CODE-ASM-002
    severity: HARD
    bind_stage: 2
    law:
      IF: "Using pointers/offsets"
      THEN: "Define base+offset invariants; bounds; alignment"
    notes: "Memory addressing must be proven correct."
    evidence:
      PASS: "Offsets documented; No out-of-bounds"
      FAIL: "Random offsets; Corruption"

  - module: CODE-ASM-003
    severity: HARD
    bind_stage: 2
    law:
      IF: "Using instructions that affect flags"
      THEN: "Track flag dependencies; isolate flag-using sequences"
    notes: "Flags and side effects must be accounted for."
    evidence:
      PASS: "Flags used intentionally; No accidental dependence"
      FAIL: "Branch wrong; Heisenbugs"

  - module: CODE-ASM-004
    severity: HARD
    bind_stage: 2
    law:
      IF: "Optimizing assembly"
      THEN: "Benchmark; consider cache; avoid premature micro-opts"
    notes: "Performance claims require measurement."
    evidence:
      PASS: "Bench harness; Measured wins"
      FAIL: "Anecdotal optimization; Regression"

  - module: CODE-ASM-005
    severity: HARD
    bind_stage: 2
    law:
      IF: "Packing/unpacking bits"
      THEN: "Define layout; masks; shifts; endianness; test vectors"
    notes: "Bit-level representations must be explicit."
    evidence:
      PASS: "Test vectors; Layout doc"
      FAIL: "Guesswork; Intermittent bugs"

