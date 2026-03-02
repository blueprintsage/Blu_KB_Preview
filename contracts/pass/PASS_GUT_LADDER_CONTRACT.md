# PASS:GUT-LADDER CONTRACT v2

## Purpose
PASS:GUT-LADDER ingests a source (e.g., PDF) and emits ladder-bound skill assets:
- Patterns (LAW gates)
- AP proposals/updates (functions)
- Drill lesson proposals/updates (human teaching)

PASS does NOT select runtime APs. PASS is an extractor/generator only.

## Core Principles
- Extract mechanics and constraints. Do not copy text or figures.
- Prefer maximum pattern harvest (patterns prevent drift).
- Enforce merge + reject to avoid library bloat.

## Pipeline
### Stage A — Ingest + Map
1) Read end-to-end (including figures/tables where relevant to mechanics).
2) Build internal map:
   - sections → claims → definitions → requirements → exceptions → failure modes
3) Identify standards/mechanics language:
   - must/shall/required/prohibited/permitted/only if/unless/except/subject to
   - thresholds/tolerances/timelines/roles/evidence

### Stage B — Normalize
For each extractable unit, produce a candidate with:
- type: PATTERN | AP | DRILL
- candidate_id: CAND-<TYPE>-<...>
- disposition: NEW | UPDATE | VARIANT | REJECT
- dedupe_key: <stable signature>
- bind_stage: 0|1|2|3|4 (for PATTERN; AP/DRILL may also tag stage relevance)
- source_ptr: <page/section pointer; no quotes>

### Stage C — Emit (Repo-safe)
PASS emits:
1) PATTERN candidates as IF→THEN gates:
   - scope, evidence, pass/fail, exceptions, failure signatures
   - severity: HARD/SOFT
   - bind_stage
2) AP candidates:
   - what the function is
   - where it plugs into Step Ladder (what to do/check at each step)
   - module suggestions (variants)
3) DRILL candidates:
   - lesson sequences
   - checkpoints using pattern IDs
   - remediation hooks

## Merge Rules (mandatory)
Given a candidate and existing corpus:

1) If dedupe_key matches exactly:
   - UPDATE existing (strengthen clarity, add missing exceptions/evidence)
2) If intent/outcome matches but constraints differ materially:
   - VARIANT module inside the best existing artifact
3) If candidate is weaker or redundant:
   - REJECT (note: “covered by PAT-…”)
4) If candidate conflicts with an existing HARD pattern:
   - escalate to REVIEW (no auto-merge)

## Reject Rules (mandatory)
PASS must mark REJECT if:
- no actionable constraints/mechanics can be extracted, OR
- content is purely inspirational/biographical with no gates/checks/drills, OR
- all extractables are already covered with no meaningful improvements.

## Step Ladder Binding (definition)
- Step 0: intent/goal/constraints/examples of “good”
- Step 1: minimal framework (skeleton/primitives)
- Step 2: structure assembly (block/volumes/components)
- Step 3: stress test (edge cases, failures, exceptions)
- Step 4: production finish (acceptance checks, polish, maintenance)

All PATTERN outputs MUST include bind_stage.

## Outputs (default)
- output=pack → PAT + AP + DRL candidates
- output=patterns → PAT candidates only
- output=aps → AP candidates only
- output=drills → DRL candidates only

## Audit Trail (recommended)
For each PASS run, record:
- source_id
- run_date
- counts: produced NEW/UPDATE/VARIANT/REJECT by type
- top risk gates (highest impact HARD patterns)
