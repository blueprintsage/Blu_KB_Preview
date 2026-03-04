# PASS GUT-LADDER CONTRACT (NUCLEAR)

Updated: 2026-03-04  
Status: Canon (Preview)
Version: 1.2
depends_on:
  - contracts/Error_handling_contract.md
  - contracts/error_macros.md

---

## Global Law (Fail-Closed)
If any REQUIRED dependency is missing/expired/unreadable at any stage, invoke ERRMAC and STOP (fail-closed).

# Purpose

PASS converts knowledge sources (books, PDFs, documents) into structured skills.

Output is organized into two lanes:

Teaching (Lane A) — human instruction  
Skills (Lane B) — machine execution laws

PASS must always produce **repo-ready artifacts**.

---

# Default Mode

PASS operates in:

PASS:GUT-LADDER (NUCLEAR)

Meaning:

- full document harvest
- multi-pass extraction
- aggressive candidate gathering
- normalization and rejection

PASS does not stop at surface markers.

---

# PASS PREFLIGHT (Required)

Before running PASS:

## OCR Check

Detect PDF type:

TEXT PDF  
OCR PDF  
IMAGE SCAN  

If image scan:

STATUS: BLOCKED  
ACTION: OCR required  

Add entry to:

docs/pass/PASS_OCR_QUEUE.md

---

## Registry Check

Verify book has not already been processed.

File:

docs/pass/PASS_BOOK_REGISTRY.md

If book exists:

STATUS: Already Processed  
ACTION: Ask before rerunning PASS

---

# PASS EXECUTION

PASS runs in four stages.

---

# PASS 1 — Harvest

Extract candidate knowledge units.

Harvest types:

patterns  
drills  
tests  
gates  
application protocols  
principles  
models  
procedures  

Extraction rule:

ONE IDEA PER PATTERN

Compound statements must be split.

Harvest aggressively.

---

# PASS 2 — Normalize + Cluster

Candidates are normalized into repo language.

Steps:

- deduplicate patterns
- cluster similar ideas
- reject vague statements
- separate variants

Variants extend base patterns.

Example:

variant_of: FIG-PAT-012  
variant_style: manga

## Dated-Book Flag (PREFLIGHT + Summary)
PREFLIGHT must output:
- DATED: YES|NO|UNKNOWN
- DATED_REASON: year/edition if detectable
- MODERNIZE_ELIGIBLE: YES|NO

Heuristic:
- If publication year is >= 8 years old → DATED: YES
- If year unknown → DATED: UNKNOWN

## PASS:MODERNIZE (OVERLAY) (Optional)
After PASS:GUT-LADDER completes, offer:
- Run PASS:MODERNIZE (OVERLAY) now
- Or defer and run later by subject

If invoked:
- Use current authoritative sources (web browsing required).
- Do not rewrite base artifacts; produce an overlay only.
- Output overlay under:
  skills/<domain>/<subject>/overlays/modern_<YYYY-MM-DD>/{Skills,Teaching}/...

Metrics must include:
- patterns_added (modern)
- variants_added
- patterns_rejected (deprecated/unsafe)
- drills_added/tests_added/aps_added (if any)

---

# PASS 3 — Dual Lane Compilation

Create structured skill.

Repo layout:

skills/<domain>/<subject>/

  <SUBJECT>_INDEX.md

  Skills/
    <SUBJECT>_B.md

  Teaching/
    <SUBJECT>_A.md

  overlays/

Rules:

Both lanes must exist  
Lane B is the law layer  
Lane A explains the laws

---

# PASS 4 — Validation + Rejection

Final validation pass.

Reject candidates that are:

vague  
motivational  
non-actionable  
redundant  

Patterns must be enforceable.

Pattern schema:

id  
IF  
THEN  
CHECK  
FAIL  
REF  

---

# PASS OUTPUT

Each PASS run must generate:

Teaching file  
Skills file  
subject index  
PASS run report  
index patch  

---

# PASS ZIP PACKAGE (MANDATORY)

Every PASS run must end with a **drop-in ZIP package**.

The zip must contain only the files created or modified by the PASS run.

Example structure:

skills/
  <domain>/
    <subject>/
      <SUBJECT>_INDEX.md
      Skills/
        <SUBJECT>_B.md
      Teaching/
        <SUBJECT>_A.md

reports/
  PASS_RUN_<date>.md

The zip must be **extract-safe at repo root**.

Purpose:

- allows manual repo merges
- prevents partial updates
- supports mobile PASS sessions

---

# PASS METRICS

Every run must report metrics.

patterns_new  
patterns_added  
variants_added  
patterns_rejected  

drills_added  
tests_added  
aps_added  

---

## Rerun Tracking (Optional but Recommended)
Maintain: docs/pass/PASS_RERUN_LOG.md

## Rerun Metric (Recommended)
- novelty_yield = patterns_new / patterns_kept_laneB

Optional:
- rerun_value = patterns_new + variants_added + (drills_added * 0.25)


# Yield Metrics

Evaluate book quality.

patterns_per_page  
signal_ratio  

Signal ratio formula:

patterns_kept / patterns_extracted

Low ratio indicates low-value source material.

---

# PASS BOOK REGISTRY

Every completed run must update:

docs/pass/PASS_BOOK_REGISTRY.md

Entry fields:

title  
author  
date_processed  
subject  
pages  

patterns_new  
patterns_added  
variants_added  
patterns_rejected  

drills_added  
tests_added  
aps_added  

patterns_per_page  
signal_ratio  

---

# OCR Queue

Unreadable books are added to:

docs/pass/PASS_OCR_QUEUE.md

Example:

BOOK  
Writing for Comics & Graphic Novels — Peter David  

PROBLEM  
Image scan PDF  

ACTION  
Run OCR in Acrobat

---

# PASS REPORT

Each run must produce:

reports/PASS_RUN_<date>.md

Report includes:

source  
subject  
metrics  
files created  
indexes patched  

---

# Core PASS Laws

1. One Idea Per Pattern  
2. Patterns Are Laws  
3. Variants Extend, Not Replace  
4. Both Lanes Always Exist  
5. Reject Weak Patterns  
6. Always Record Metrics  
7. Always Update Registry  
8. Every PASS run produces a ZIP package  

---

# PASS Philosophy

PASS prioritizes signal over volume.

Large extraction counts are acceptable.

Final pattern set must remain:

clear  
enforceable  
non-redundant