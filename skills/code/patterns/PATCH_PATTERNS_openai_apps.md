# PATCH_APPEND — PATTERNS-CODE (Building AI Applications with OpenAI APIs (2nd ed., 2024))

Append these modules under an appropriate cluster in `skills/code/patterns/PATTERNS-CODE.md`.

---

module_set: PATTERNS_PATCH
status: READY
modules:
  - module: CODE-AI-001
    severity: HARD
    bind_stage: 2
    law:
      IF: "Building an AI feature"
      THEN: "Define success metrics and test prompts before prompt/agent tuning"
    notes: "Define evaluation before optimization."
    evidence:
      PASS: "Eval set exists; Metrics defined"
      FAIL: "Tuning by vibes; No regression detection"

  - module: CODE-AI-002
    severity: HARD
    bind_stage: 2
    law:
      IF: "Using external model/tool calls"
      THEN: "Design retries, fallbacks, timeouts, and safe defaults"
    notes: "Handle model/tool failures as expected operations."
    evidence:
      PASS: "Timeout/retry policy; Fallback behavior"
      FAIL: "Random failures; User-facing crashes"

  - module: CODE-AI-003
    severity: HARD
    bind_stage: 2
    law:
      IF: "Using user data and system instructions"
      THEN: "Separate system/developer/user content; sanitize user input; avoid prompt injection paths"
    notes: "Prompt/data boundaries must be explicit."
    evidence:
      PASS: "Boundary rules documented; Input sanitation"
      FAIL: "Instruction leakage; Injection vulnerabilities"

  - module: CODE-AI-004
    severity: HARD
    bind_stage: 2
    law:
      IF: "Running AI apps in production"
      THEN: "Log request IDs, outcomes, errors; redact secrets/PII"
    notes: "Logging must support audits without leaking secrets."
    evidence:
      PASS: "Redaction rules; Traceable outcomes"
      FAIL: "Logs leak data; No traceability"

  - module: CODE-AI-005
    severity: HARD
    bind_stage: 2
    law:
      IF: "Iterating on AI behavior"
      THEN: "Version prompt sets; change logs; rollback plan"
    notes: "Version prompts and workflows like code."
    evidence:
      PASS: "Prompt versions tracked; Rollback possible"
      FAIL: "Untracked changes; Can't reproduce behavior"

