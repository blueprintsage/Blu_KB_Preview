# PATCH_APPEND — PATTERNS-CODE (Programming Python (4th Edition))

Append these modules under an appropriate cluster in `skills/code/patterns/PATTERNS-CODE.md`.

---

module_set: PATTERNS_PATCH
status: READY
modules:
  - module: CODE-PYAPP-001
    severity: HARD
    bind_stage: 2
    law:
      IF: "Building networked/IO-heavy apps"
      THEN: "Choose threads/processes/async and document why; avoid mixed ad-hoc"
    notes: "Concurrency model must be chosen explicitly."
    evidence:
      PASS: "Model documented; No accidental mixing"
      FAIL: "Random threads; Deadlocks"

  - module: CODE-PYAPP-002
    severity: HARD
    bind_stage: 2
    law:
      IF: "Using files/sockets/db connections"
      THEN: "Use context managers; ensure close on failures"
    notes: "Resource lifetimes must be explicit."
    evidence:
      PASS: "with/try-finally used; No leaks"
      FAIL: "Leaks; Hangs"

  - module: CODE-PYAPP-003
    severity: HARD
    bind_stage: 2
    law:
      IF: "Building scripts/tools"
      THEN: "Keep core logic importable; CLI thin wrapper"
    notes: "Separation of concerns: UI/CLI vs core logic."
    evidence:
      PASS: "Core module testable; CLI calls core"
      FAIL: "Logic inside CLI; Hard to reuse"

  - module: CODE-PYAPP-004
    severity: HARD
    bind_stage: 2
    law:
      IF: "Saving/loading data formats"
      THEN: "Define schema, version field, migrations; validate on load"
    notes: "Data serialization must be version-tolerant."
    evidence:
      PASS: "Schema exists; Versioning plan"
      FAIL: "Ad-hoc JSON; Breaks on changes"

  - module: CODE-PYAPP-005
    severity: HARD
    bind_stage: 2
    law:
      IF: "Apps run outside dev machine"
      THEN: "Structured logs; consistent levels; include correlation IDs where relevant"
    notes: "Logging is part of the interface for ops."
    evidence:
      PASS: "Useful logs; Errors traceable"
      FAIL: "Print debugging; No context"

