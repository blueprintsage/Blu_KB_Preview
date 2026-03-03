# PASS:GUT-LADDER — Designing Web APIs: Building APIs That Developers Love (2018)
Generated: 2026-03-03T00:57:40.201287

**Disposition:** PASS (patterns + drills extracted)

## Quick Map (outline/headings)
- Cover
- Copyright
- Table of Contents
- Preface
- How This Book Is Organized
- Conventions Used in This Book
- O’Reilly Safari
- How to Contact Us
- Acknowledgments
- Chapter 1. What’s an API?
- Why Do We Need APIs?
- Who Are Our Users?
- The Business Case for APIs
- APIs for Internal Developers First, External Developers Second
- APIs for External Developers First, Internal Developers Second
- APIs as the Product
- What Makes an API Great?
- Closing Thoughts
- Chapter 2. API Paradigms
- Request–Response APIs

## Surface Scan (first pages keywords)
- keywords_detected: api, design, http, resource, security, types

---

module_set: PASS_GUT_LADDER
status: PASSED
domain: code
subject: web_apis_designing

modules:
  - gate: CODE-API-101
    standard: "Developer experience is a requirement."
    IF: "API is for third-party developers"
    THEN: "Provide predictable naming, examples, onboarding path"
    PASS_evidence: ['Examples exist', 'Consistent naming']
    FAIL_signals: ['Sparse docs', 'Inconsistent resources']

  - gate: CODE-API-102
    standard: "Consistency beats cleverness."
    IF: "Adding new endpoints/features"
    THEN: "Reuse existing patterns; avoid one-off behaviors"
    PASS_evidence: ['Style guide followed', 'Patterns reused']
    FAIL_signals: ['Snowflake endpoints', 'Client complexity']

  - gate: CODE-API-103
    standard: "Idempotency must be designed."
    IF: "Operations can be retried"
    THEN: "Define which operations are safe to retry; provide idempotency keys when needed"
    PASS_evidence: ['Idempotency strategy documented', 'Keys supported where relevant']
    FAIL_signals: ['Double charges', 'Duplicate side effects']

  - gate: CODE-API-104
    standard: "Pagination/filtering must be explicit and stable."
    IF: "Returning collections"
    THEN: "Define pagination and filtering parameters; stable ordering"
    PASS_evidence: ['Pagination spec exists', 'Stable sort key']
    FAIL_signals: ['Shifting pages', 'Client bugs']

  - gate: CODE-API-105
    standard: "Security model must be explicit."
    IF: "Authentication/authorization required"
    THEN: "Define auth mechanism, scopes/roles, error responses, rate limits"
    PASS_evidence: ['Auth docs', 'Scope model', 'Threat notes']
    FAIL_signals: ['Ad-hoc auth', 'Leaky access']

## Drills extracted

module_set: DRILLS_EXTRACT
status: PASSED
modules:
  - module: DRL-CODE-API-101
    name: "DX Onboarding"
    steps:
      - "Write 'Hello API' example"
      - "Add auth + first call"
      - "Validate it works end-to-end"

  - module: DRL-CODE-API-102
    name: "Idempotency Simulation"
    steps:
      - "Simulate retry on POST-like operation"
      - "Add idempotency key"
      - "Prove no duplicate side effects"

