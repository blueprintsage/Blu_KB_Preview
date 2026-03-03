# PASS:GUT-LADDER — The Art of Assembly Language (2nd Edition)
Generated: 2026-03-03T00:57:38.544308

**Disposition:** PASS (patterns + drills extracted)

## Quick Map (outline/headings)
- Contents in Detail
- Acknowledgements
- Chapter 1: Hello, World of Assembly Language
- 1.1: The Anatomy of an HLA Program
- 1.2: Running Your First HLA Program
- 1.3: Some Basic HLA Data Declarations
- 1.4: Boolean Values
- 1.5: Character Values
- 1.6: An Introduction to the Intel 80x86 CPU Family
- 1.7: The Memory Subsystem
- 1.8: Some Basic Machine Instructions
- 1.9: Some Basic HLA Control Structures
- 1.10: Introduction to the HLA Standard Library
- 1.11: Additional Details About try..endtry
- 1.12: High-Level Assembly Language vs. Low-Level Assembly Language
- 1.13: For More Information
- Chapter 2: Data Representation
- 2.1: Numbering Systems
- 2.2: The Hexadecimal Numbering System
- 2.3: Data Organization

## Surface Scan (first pages keywords)
- keywords_detected: assembly, design, eval, memory, types

---

module_set: PASS_GUT_LADDER
status: PASSED
domain: code
subject: assembly_lowlevel

modules:
  - gate: CODE-ASM-001
    standard: "Calling convention is a contract."
    IF: "Writing functions that call/are called"
    THEN: "Preserve required registers/stack discipline; document convention"
    PASS_evidence: ['Prologue/epilogue correct', 'ABI respected']
    FAIL_signals: ['Stack imbalance', 'Clobbered regs']

  - gate: CODE-ASM-002
    standard: "Memory addressing must be proven correct."
    IF: "Using pointers/offsets"
    THEN: "Define base+offset invariants; bounds; alignment"
    PASS_evidence: ['Offsets documented', 'No out-of-bounds']
    FAIL_signals: ['Random offsets', 'Corruption']

  - gate: CODE-ASM-003
    standard: "Flags and side effects must be accounted for."
    IF: "Using instructions that affect flags"
    THEN: "Track flag dependencies; isolate flag-using sequences"
    PASS_evidence: ['Flags used intentionally', 'No accidental dependence']
    FAIL_signals: ['Branch wrong', 'Heisenbugs']

  - gate: CODE-ASM-004
    standard: "Performance claims require measurement."
    IF: "Optimizing assembly"
    THEN: "Benchmark; consider cache; avoid premature micro-opts"
    PASS_evidence: ['Bench harness', 'Measured wins']
    FAIL_signals: ['Anecdotal optimization', 'Regression']

  - gate: CODE-ASM-005
    standard: "Bit-level representations must be explicit."
    IF: "Packing/unpacking bits"
    THEN: "Define layout; masks; shifts; endianness; test vectors"
    PASS_evidence: ['Test vectors', 'Layout doc']
    FAIL_signals: ['Guesswork', 'Intermittent bugs']

## Drills extracted

module_set: DRILLS_EXTRACT
status: PASSED
modules:
  - module: DRL-CODE-ASM-001
    name: "ABI Checklist"
    steps:
      - "Pick target ABI"
      - "Write a function stub"
      - "Verify saved regs/stack alignment with tests or emulator"

  - module: DRL-CODE-ASM-002
    name: "Bit Layout Test Vectors"
    steps:
      - "Define bitfield layout"
      - "Write pack/unpack"
      - "Create 10 test vectors including edge cases"

