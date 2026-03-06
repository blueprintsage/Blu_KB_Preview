# COLD STORE — PASS:GUT-LADDER + Dual-Lane Standard
Version: v1.0
Date: 2026-03-03
tz: America/Chicago

Scope: repo policy + Skill Forge workflow standardization.
Enforcement: ON

---

## 0) Non‑Negotiables (Repo Safety)
- Do not store/commit third‑party copyrighted source materials (PDFs/scans/rips/page dumps/web scrapes).
- Repo may store: **original outputs we author**, and **metadata/manifests** (filenames, hashes, license notes) without the source content.
- If uncertain: treat as copyrighted → **LOCAL‑ONLY**.

---

## 1) Dual‑Lane Standard (A/B)
Every Skill Forge subject ships in **two lanes**:

### Lane B — Blu Runtime (Canonical)
Machine-first, modular, enforceable.

**Purpose**
- Fast parsing
- Targeted updates
- Deterministic enforcement (patterns/tests)

**Properties**
- Small modules, strict scope
- Semantic IDs (stable once published)
- Patterns expressed as gates/tests
- Ledgers record changes

### Lane A — Teaching Pack (Compiled)
Human-first curriculum compiled from Lane B.

**Purpose**
- Clean instruction
- Ordered syllabus
- Minimal files
- Human-friendly drills & checkpoints

**Authority Rule**
- **Lane B is source-of-truth.**
- Lane A is updated only during **freezes/releases** (v1.x).

---

## 2) PASS Default Mode Update
PASS defaults to:

### PASS:GUT-LADDER (Default)
**Output is always Dual‑Lane:**
- Produce Lane B first (canonical patterns/tests/modules/ledger)
- Then produce Lane A teaching pack (README/SYLLABUS/PATTERNS/DRILLS/TESTS/LEDGER)

**Hard constraint**
- No copy/paste from sources. Convert concepts into original technical language.
- Prefer enforceable gates over vague advice.
- Reject content that is redundant, purely stylistic preference, or non-actionable.

---

## 3) PASS:GUT-LADDER — Deep Gut Routine (Canonical)
When a source document is provided (PDF/book/manual):

### Step 1 — Ingest & Map
- Read end-to-end (include figures/tables when relevant).
- Build an internal map:
  - sections → claims → definitions → requirements → exceptions → examples.
- Identify the “standards layer”:
  - must/shall/required/prohibited/permitted/may/should
  - unless/except/only if/provided that
  - thresholds, tolerances, timelines, roles, artifacts/evidence

### Step 2 — Extract & Normalize
For each actionable standard/lesson:
- Normalize into plain-English “what it really means”
- Detect duplicates and merge
- Resolve conflicts by:
  - picking the more general rule as canonical
  - keeping narrower versions as variants

### Step 3 — Convert to Gates (Patterns)
Every pattern becomes a gate:

**Gate format**
- Gate ID: <SUBJECT>-<CATEGORY>-###
- Standard (plain language)
- IF (Trigger X)
- THEN (Requirement Y)
- PASS condition (evidence that satisfies)
- FAIL condition (what breaks it)
- Notes / exceptions / edge cases
- Source pointer (page/chapter reference — no quotes)

### Step 4 — Build Proof (Tests)
- Scenario tests (real tasks)
- Proof detectors (fast checks: silhouette test, crop tests, tangent hunt, etc.)
- Smoke tests (minimum set to validate the subject stays stable)

### Step 5 — Build Human Drills (Teaching)
- Drills are **practice sequences** to achieve mastery.
- Drills do not “train patterns”; drills **exercise** patterns.
- Each drill should reference which gates it is exercising.

### Step 6 — Compile Dual-Lane Outputs
**Lane B output (canonical)**
- patterns/
- tests/
- (optional) modules/
- (optional) drills/ (battery drills)
- ledger/
- indexes patch

**Lane A output (compiled)**
- README.md
- SYLLABUS.md
- PATTERNS.md (curated + references to Lane B IDs/paths)
- DRILLS.md (human instructions)
- TESTS.md (pass/fail targets)
- LEDGER.md
- indexes patch

### Step 7 — Reject Test (Mandatory)
Before accepting a new source:
- Does it add new enforceable gates or materially improve clarity?
- If not, reject or archive as “low value reference” (no extraction).

---

## 4) Freeze Policy (Release Discipline)
A subject is considered “Complete” when:
- Lane B passes its proof detectors + scenario tests
- Lane A teaches end-to-end without hidden assumptions
- Both lanes have ledgers + index patches
- A “Freeze Pack” is produced (single drop bundle for Lane A and Lane B)

---

## 5) Naming & Placement (Repo Hygiene)
- templates with templates
- tests with tests
- contracts with contracts
- burnins with burnins
- schemas with schemas

Lane A location:
- teaching/<domain>/<subject>_vX.Y/

Lane B location:
- skills/<domain>/<subject>/_core or modules

---

## 6) Commands (Convention)
- PASS:GUT-LADDER  (default)
- PASS:GUT-LADDER subject=<topic>  (override subject)
- PASS:GUT-LADDER output=laneB|laneA|both  (default: both)
- PASS:GUT-LADDER reject_test=on  (default: on)

