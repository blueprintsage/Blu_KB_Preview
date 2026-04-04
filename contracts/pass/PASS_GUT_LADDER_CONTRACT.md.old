# PASS GUT-LADDER Contract (Rewrite) — v1.0

updated: 2026-03-04
tz: America/Chicago
status: canon (preview)
version: 1.0

**Goal:** Stabilize PASS behavior with strict contract compliance, fail-closed errors, and DROP-IN ZIP outputs.  
**Scope:** PASS:PREFLIGHT, PASS:GUT-LADDER, optional PASS:MODERNIZE (OVERLAY).  
**Non-Goals:** Repo restructuring, content recommendations during PREFLIGHT, “helpful” previews.

## Command Surface (character-exact)

- `PASS:PREFLIGHT`
- `PASS:GUT-LADDER`
- `PASS:MODERNIZE (OVERLAY)` *(optional; only after asking; overlay-only)*

---

## 1) Global Laws (Hard)

### 1.1 Fail-Closed
If a requirement is not met, **STOP** and return **BLOCKED** (or ERR) with **one** action line.  
No “best effort” extraction, no partial ladders, no structure guesses.

### 1.2 Output Discipline
Each command has a **hard output schema**.  
Any output outside schema = **command FAIL**.

### 1.3 No Copyright Spill
Do not reproduce copyrighted pages. PASS extracts **mechanics only**.

---

## 2) PASS:PREFLIGHT (Validation Only) — STRICT

### 2.1 Purpose
PREFLIGHT performs **ingest validation only**.  
It MUST NOT extract, summarize, sample, infer structure, or recommend next steps.

### 2.2 Allowed Outputs (ONLY)
PREFLIGHT may output **only** the following lines (no extras):

- `OCR_TYPE: TEXT | OCR | SCAN`
- `PARSE_QUALITY: low | medium | high`
- `DATED: YES | NO | UNKNOWN`
- `DATED_REASON: <short reason>` *(optional; only if known)*
- `STATUS: READY | BLOCKED`
- `ACTION: <one line>` *(required only if STATUS=BLOCKED)*
- `REGISTRY: NEW | DUP | UNKNOWN`

That’s it.

### 2.3 Forbidden During PREFLIGHT (Hard)
If any of these appear, mark **PREFLIGHT FAIL** (and return BLOCKED):

- TOC/structure lists (chapters, appendices, “front matter”, etc.)
- page sampling (“sampled pages”, “rendered previews”, “spreads detected”, etc.)
- “rules/heuristics found”
- recommendations (“good extraction targets”, “you might want drills next”, etc.)
- any content extraction, quotes, summaries, or topic analysis
- any question like “What do you want me to do with this file?” (selection prompting)

### 2.4 Registry Rule (Hard)
If `REGISTRY: DUP` → PREFLIGHT must set:
- `STATUS: BLOCKED`
- `ACTION: Confirm rerun? (Y/N)`
…and STOP. No further work until user confirms.

### 2.5 Block Conditions (Examples)
PREFLIGHT returns `STATUS: BLOCKED` when:
- file unreadable / corrupted / missing
- parse quality too low for reliable PASS runs
- scan requires OCR but OCR not available/enabled
- registry shows DUP without explicit rerun confirmation

---

## 3) PASS:GUT-LADDER (PASS 1–4) — REQUIRED

### 3.1 Preconditions (Hard)
`PASS:GUT-LADDER` must not run unless PREFLIGHT has produced:
- `STATUS: READY`
- and `REGISTRY != DUP` (or DUP has been confirmed)

### 3.2 When STATUS=READY
GUT-LADDER must execute PASS 1–4 **per ladder** and produce the required outputs below.

### 3.3 Required Outputs (Hard)
GUT-LADDER must always emit:

1) **Counts line (tight, exact keys):**
- `patterns=<n> drills=<n> gates=<n> variants=<n> rejected=<n>`

2) **DROP-IN ZIP**
- Always produce a DROP-IN ZIP that is **extract-safe at repo root**.
- The ZIP must contain only PASS outputs (mechanics-only), with deterministic naming, and no absolute paths.

3) **Registry Update Rule**
- Update `PASS_BOOK_REGISTRY.md` **only after successful completion** of PASS 1–4 **and** DROP-IN ZIP creation.

### 3.4 Failure Handling (Hard)
If any ladder stage fails:
- Do **not** update registry.
- Do **not** produce a “partial success” ZIP unless explicitly permitted by an error macro (default: no).
- Return a fail-closed error with one recovery action.

---

## 4) DATED + MODERNIZE Overlay

### 4.1 DATED Field
PREFLIGHT must set:
- `DATED: YES | NO | UNKNOWN`
- `DATED_REASON` optional

### 4.2 Overlay Ask Rule (One Question Only)
If `DATED=YES` **and** the topic is time-sensitive:
Ask exactly once:

**“Run modern overlay now? (Y/N)”**

- If **N** or no answer: proceed with base GUT-LADDER only.
- If **Y**: run `PASS:MODERNIZE (OVERLAY)` **after** base GUT-LADDER succeeds.

### 4.3 Overlay-Only Constraint (Hard)
`PASS:MODERNIZE (OVERLAY)` must:
- be an **overlay**, not a rewrite
- not modify base outputs
- produce overlay artifacts separately (and optionally a separate overlay ZIP, if defined)

---

## 5) Regression Gates (Minimum)

### 5.1 PREFLIGHT Schema Gate
Test asserts:
- PREFLIGHT output contains **only** allowed keys
- values match allowed enums
- if extra lines exist → FAIL

### 5.2 Leak Test (Known Failure Case)
Feed PREFLIGHT a “TOC/structure summary” or “what do you want me to do?” style output:
- expected result: `STATUS: BLOCKED` + 1-line `ACTION` (PREFLIGHT FAIL)

### 5.3 Registry DUP Gate
When registry indicates DUP:
- must stop with `STATUS: BLOCKED`
- must ask for rerun confirmation (Y/N)
- must not run GUT-LADDER

### 5.4 Registry Update Gate
Registry update occurs only when:
- PASS 1–4 succeeded
- DROP-IN ZIP created successfully

---

## 6) Reference Outputs (Normative)

### 6.1 Canonical PREFLIGHT Example (READY)
```txt
OCR_TYPE: OCR
PARSE_QUALITY: medium
DATED: YES
STATUS: READY
REGISTRY: UNKNOWN
```

### 6.2 Canonical PREFLIGHT Example (BLOCKED)
```txt
OCR_TYPE: SCAN
PARSE_QUALITY: low
DATED: UNKNOWN
STATUS: BLOCKED
ACTION: Enable OCR or provide a text-layer PDF.
REGISTRY: NEW
```

### 6.3 Canonical GUT-LADDER Counts Line
```txt
patterns=12 drills=8 gates=3 variants=4 rejected=19
```
