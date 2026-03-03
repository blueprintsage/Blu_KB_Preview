# PASS:GUT-LADDER — Design and Build Great Web APIs: Robust, Reliable, and Resilient
Generated: 2026-03-03T00:57:39.483357

**Disposition:** PASS (patterns + drills extracted)

## Quick Map (outline/headings)
- Cover
- Table of Contents
- Acknowledgments
- Preface
- Your API Journey
- Who Should Read This Book
- How This Book Is Organized
- What’s Covered (And What’s Not)
- About the BigCo, Inc., Sample Project
- Online Resources
- Part I—Getting Started
- 1. Getting Started with API First
- Adopting the API-First Principle
- Exploring APIs with curl
- What’s Next?
- Chapter Exercise
- 2. Understanding HTTP, REST, and APIs
- Understanding Web API Protocols, Practices, and Styles
- Managing Files with Git
- What’s Next?

## Surface Scan (first pages keywords)
- keywords_detected: api, design, http, pattern, resource, security, testing, version

---

module_set: PASS_GUT_LADDER
status: PASSED
domain: code
subject: web_apis_amundsen

modules:
  - gate: CODE-API-001
    standard: "Design the interface before implementation."
    IF: "Starting a service for external consumers"
    THEN: "Write API contract first (resources, operations, errors)"
    PASS_evidence: ['Contract artifact exists', 'Endpoints + errors enumerated']
    FAIL_signals: ['Endpoints emerge ad-hoc', 'Breaking changes mid-build']

  - gate: CODE-API-002
    standard: "Use HTTP semantics deliberately."
    IF: "Using HTTP transport"
    THEN: "Define method/status/header semantics and use consistently"
    PASS_evidence: ['Method/status table exists', 'Caching rules documented']
    FAIL_signals: ['Always-200 errors', 'Non-idempotent GET/PUT']

  - gate: CODE-API-003
    standard: "Errors must be first-class."
    IF: "Requests can fail"
    THEN: "Define consistent error shape, codes, remediation hints"
    PASS_evidence: ['Error schema defined', 'Examples for top failures']
    FAIL_signals: ['Random error payloads', 'No client guidance']

  - gate: CODE-API-004
    standard: "Evolvability: prefer additive change and deprecation policy."
    IF: "API will evolve over time"
    THEN: "Document deprecation/migration; avoid silent breaking changes"
    PASS_evidence: ['Deprecation policy', 'Migration path']
    FAIL_signals: ['Silent breaking', 'No guidance']

  - gate: CODE-API-005
    standard: "Operational reliability is part of the API."
    IF: "API runs in production"
    THEN: "Define timeouts, retries, rate limits, observability expectations"
    PASS_evidence: ['Timeout/retry rules', 'Rate limit behavior', 'Logging/metrics plan']
    FAIL_signals: ['No SLO thinking', 'Hard to debug']

## Drills extracted

module_set: DRILLS_EXTRACT
status: PASSED
modules:
  - module: DRL-CODE-API-001
    name: "Contract-First API"
    steps:
      - "Write resource list"
      - "Define operations + errors"
      - "Only then implement minimal handler"

  - module: DRL-CODE-API-002
    name: "Error Shape Consistency"
    steps:
      - "Define error schema"
      - "Implement 3 failures"
      - "Verify clients can handle uniformly"

