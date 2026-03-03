# PATCH_APPEND — PATTERNS-CODE (Design and Build Great Web APIs: Robust, Reliable, and Resilient)

Append these modules under an appropriate cluster in `skills/code/patterns/PATTERNS-CODE.md`.

---

module_set: PATTERNS_PATCH
status: READY
modules:
  - module: CODE-API-001
    severity: HARD
    bind_stage: 2
    law:
      IF: "Starting a service for external consumers"
      THEN: "Write API contract first (resources, operations, errors)"
    notes: "Design the interface before implementation."
    evidence:
      PASS: "Contract artifact exists; Endpoints + errors enumerated"
      FAIL: "Endpoints emerge ad-hoc; Breaking changes mid-build"

  - module: CODE-API-002
    severity: HARD
    bind_stage: 2
    law:
      IF: "Using HTTP transport"
      THEN: "Define method/status/header semantics and use consistently"
    notes: "Use HTTP semantics deliberately."
    evidence:
      PASS: "Method/status table exists; Caching rules documented"
      FAIL: "Always-200 errors; Non-idempotent GET/PUT"

  - module: CODE-API-003
    severity: HARD
    bind_stage: 2
    law:
      IF: "Requests can fail"
      THEN: "Define consistent error shape, codes, remediation hints"
    notes: "Errors must be first-class."
    evidence:
      PASS: "Error schema defined; Examples for top failures"
      FAIL: "Random error payloads; No client guidance"

  - module: CODE-API-004
    severity: HARD
    bind_stage: 2
    law:
      IF: "API will evolve over time"
      THEN: "Document deprecation/migration; avoid silent breaking changes"
    notes: "Evolvability: prefer additive change and deprecation policy."
    evidence:
      PASS: "Deprecation policy; Migration path"
      FAIL: "Silent breaking; No guidance"

  - module: CODE-API-005
    severity: HARD
    bind_stage: 2
    law:
      IF: "API runs in production"
      THEN: "Define timeouts, retries, rate limits, observability expectations"
    notes: "Operational reliability is part of the API."
    evidence:
      PASS: "Timeout/retry rules; Rate limit behavior; Logging/metrics plan"
      FAIL: "No SLO thinking; Hard to debug"

