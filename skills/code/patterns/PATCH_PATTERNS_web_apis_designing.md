# PATCH_APPEND — PATTERNS-CODE (Designing Web APIs: Building APIs That Developers Love (2018))

Append these modules under an appropriate cluster in `skills/code/patterns/PATTERNS-CODE.md`.

---

module_set: PATTERNS_PATCH
status: READY
modules:
  - module: CODE-API-101
    severity: HARD
    bind_stage: 2
    law:
      IF: "API is for third-party developers"
      THEN: "Provide predictable naming, examples, onboarding path"
    notes: "Developer experience is a requirement."
    evidence:
      PASS: "Examples exist; Consistent naming"
      FAIL: "Sparse docs; Inconsistent resources"

  - module: CODE-API-102
    severity: HARD
    bind_stage: 2
    law:
      IF: "Adding new endpoints/features"
      THEN: "Reuse existing patterns; avoid one-off behaviors"
    notes: "Consistency beats cleverness."
    evidence:
      PASS: "Style guide followed; Patterns reused"
      FAIL: "Snowflake endpoints; Client complexity"

  - module: CODE-API-103
    severity: HARD
    bind_stage: 2
    law:
      IF: "Operations can be retried"
      THEN: "Define which operations are safe to retry; provide idempotency keys when needed"
    notes: "Idempotency must be designed."
    evidence:
      PASS: "Idempotency strategy documented; Keys supported where relevant"
      FAIL: "Double charges; Duplicate side effects"

  - module: CODE-API-104
    severity: HARD
    bind_stage: 2
    law:
      IF: "Returning collections"
      THEN: "Define pagination and filtering parameters; stable ordering"
    notes: "Pagination/filtering must be explicit and stable."
    evidence:
      PASS: "Pagination spec exists; Stable sort key"
      FAIL: "Shifting pages; Client bugs"

  - module: CODE-API-105
    severity: HARD
    bind_stage: 2
    law:
      IF: "Authentication/authorization required"
      THEN: "Define auth mechanism, scopes/roles, error responses, rate limits"
    notes: "Security model must be explicit."
    evidence:
      PASS: "Auth docs; Scope model; Threat notes"
      FAIL: "Ad-hoc auth; Leaky access"

