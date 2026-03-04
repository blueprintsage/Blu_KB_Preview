# PASS GUT-LADDER CONTRACT

updated: 2026-03-04
status: canon (preview)
version: 1.3

depends_on:
  - contracts/Error_handling_contract.md
  - contracts/error_macros.md

---

## Global Law (Fail-Closed)
If any REQUIRED dependency is missing/expired/unreadable at any stage, invoke ERRMAC and STOP (fail-closed).

---

# Purpose
PASS converts knowledge sources (books, PDFs, documents) into structured skills.

Output is organized into two lanes:

- Teaching (Lane A) — human instruction
- Skills (Lane B) — machine execution laws

PASS must always produce repo-ready artifacts and a DROP-IN ZIP.

---

# Command Surface (Canonical)

## PASS:PREFLIGHT
Purpose: validate inputs before running PASS.

Required checks:
- OCR_TYPE: TEXT | OCR | SCAN
- PARSE_QUALITY: low | medium | high (best-effort)
- STATUS: READY | BLOCKED
- REGISTRY: NEW | DUP | UNKNOWN (best-effort)

Rules:
- If OCR_TYPE=SCAN and no text layer is available:
  - STATUS: BLOCKED
  - ACTION: OCR required
  - Add entry to docs/pass/PASS_OCR_QUEUE.md (if available)
  - STOP (fail-closed)
- If REGISTRY=DUP:
  - Ask before rerunning PASS (one question max)

PREFLIGHT MUST NOT extract or summarize content. NO TOC, no rules, no heuristics, no prompts. Only ingest/eligibility checks.

If any required dependency is missing/expired/unreadable:
- invoke ERRMAC and STOP.

---

## PASS:GUT-LADDER
Purpose: full extraction pipeline per this contract.

PASS runs in four stages:

1) PASS 1 — Harvest
2) PASS 2 — Normalize + Cluster
3) PASS 3 — Dual Lane Compilation (A/B)
4) PASS 4 — Validation + Rejection + Package

PASS does not stop at surface markers. It must mine the full source unless blocked.

If any required dependency is missing/expired/unreadable:
- invoke ERRMAC and STOP.

---

# PASS Execution Details

## PASS 1 — Harvest
Extract all candidate knowledge units.

Harvest types:
- patterns
- drills
- tests
- gates
- application protocols (APs)
- procedures/models/principles (only if they become enforceable patterns or APs)

Rule: ONE IDEA PER PATTERN
- Compound statements must be split.

Harvest aggressively.

---

## PASS 2 — Normalize + Cluster
Convert candidates into repo language and collapse duplicates.

Steps:
- deduplicate
- cluster near-duplicates
- separate variants
- reject weak candidates (see PASS 4)

Variants:
- Variants extend base patterns; they do not replace them.
- If variants are produced, they must be clearly labeled as variants of a base concept.

---

## PASS 3 — Dual Lane Compilation
Create the structured subject package.

Repo layout:
skills/<domain>/<subject>/

  <SUBJECT>_INDEX.md

  Skills/
    <SUBJECT>_B.md

  Teaching/
    <SUBJECT>_A.md

  overlays/   (optional; only used by modernize overlays)

Rules:
- Both lanes must exist.
- Lane B is the law layer.
- Lane A explains and teaches the laws.

---

## PASS 4 — Validation + Rejection + Package
Reject candidates that are:
- vague
- motivational
- non-actionable
- redundant
- unsafe/outdated when presented as absolute law (unless explicitly tagged and deferred to modernize overlay)

Pattern schema (minimum fields):
- id
- IF
- THEN
- CHECK
- FAIL
- REF (source pointer when possible)

---

# Dated Book Flag + Modernize Option

## DATED Flag (PREFLIGHT + Summary)
PREFLIGHT must output:
- DATED: YES | NO | UNKNOWN
- DATED_REASON: year/edition if detectable

Heuristic:
- If publication year is >= 8 years old → DATED: YES
- If year unknown → DATED: UNKNOWN

## Modernize Option (Ask)
If DATED=YES and topic is time-sensitive:
- Ask once: “Run modern overlay now?” (Y/N)

Modernize is an overlay, not a rewrite of the base extraction.

---

## PASS:MODERNIZE (OVERLAY) (Optional)
If invoked:
- Use current authoritative sources (web browsing required).
- Do not rewrite base artifacts; produce overlay artifacts only.
- Output under:
  skills/<domain>/<subject>/overlays/modern_<YYYY-MM-DD>/

Overlay metrics must include:
- patterns_added (modern)
- variants_added
- patterns_rejected (deprecated/unsafe)

---

# PASS Output (Mandatory)
Each PASS run must generate:
- Teaching lane file (Lane A)
- Skills lane file (Lane B)
- Subject index
- PASS run report
- DROP-IN ZIP package (mandatory)
- Index patch (optional; only if you are asked to patch indexes)

---

# PASS ZIP Package (Mandatory)
Every PASS run must end with a DROP-IN ZIP package.

The zip must contain only files created or modified by the PASS run.

Example structure:
skills/
  <domain>/
    <subject>/
      <SUBJECT>_INDEX.md
      Skills/
        <SUBJECT>_B.md
      Teaching/
        <SUBJECT>_A.md
      overlays/ (optional)

reports/
  PASS_RUN_<YYYY-MM-DD>_<shortname>.md

docs/pass/
  PASS_BOOK_REGISTRY.md (only if updated)
  PASS_OCR_QUEUE.md (only if updated)
  PASS_RERUN_LOG.md (only if updated)

The zip must be extract-safe at repo root.

---

# PASS Metrics (Required)
Every run must report:

patterns_new
patterns_added
variants_added
patterns_rejected

drills_added
tests_added
aps_added

Also emit the tight counts line:
patterns=<n> drills=<n> gates=<n> variants=<n> rejected=<n>

---

# Yield Metrics (Recommended)
- patterns_per_page
- signal_ratio = patterns_kept / patterns_extracted

---

## Rerun Tracking (Optional but Recommended)
Maintain: docs/pass/PASS_RERUN_LOG.md

## Rerun Metric (Recommended)
- novelty_yield = patterns_new / patterns_kept_laneB

Optional:
- rerun_value = patterns_new + variants_added + (drills_added * 0.25)

---

# PASS Book Registry
Every completed run must update:
docs/pass/PASS_BOOK_REGISTRY.md

Registry prevents duplicate PASS runs.

Recommended entry fields:
- title
- author(s)
- year/edition
- date_processed
- subject
- pages
- metrics + yield metrics

---

# OCR Queue
Unreadable sources are added to:
docs/pass/PASS_OCR_QUEUE.md

---

# PASS Report
Each run must produce:
reports/PASS_RUN_<YYYY-MM-DD>_<shortname>.md

Report includes:
- source
- subject
- preflight summary
- metrics (required + yield)
- files created
- zip name

---

# Core PASS Laws
1. Fail-closed via ERRMAC
2. One Idea Per Pattern
3. Patterns Are Laws (IF/THEN enforceable)
4. Variants Extend, Not Replace
5. Both Lanes Always Exist
6. Reject Weak Patterns
7. Always Record Metrics
8. Always Produce DROP-IN ZIP
9. Update Registry After Completion