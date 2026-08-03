# PASS / SkillForge Rewrite Roadmap
Date: 2026-03-11

## Purpose

Rebuild the legacy PASS/SkillForge stack as a declared, stable system instead of a half-preserved organic one.

The goal is not to reinvent the old design. The goal is to recover what actually worked, lock the definitions, separate responsibilities cleanly, and make the system resilient enough that terms and behaviors do not drift again.

---

## High-level architecture

### 1. PASS
**Pattern Analysis Skill System**

PASS is the mining and extraction system.

Its job is to:
- ingest a source
- strip-mine it for reusable artifacts
- run a second-pass recovery sweep
- dedupe and normalize findings
- log rejects and deferred items
- export a structured result set for later placement and canon review

PASS is **not** the canon store and is **not** responsible for reliable live registry mutation.

### 2. SkillForge
SkillForge is the canon and runtime orchestration system.

Its job is to:
- receive PASS candidates
- compare them against canon
- decide reject / add / replace / enrich / variant / alias
- package usable outputs
- load and apply relevant modules during active work

SkillForge is both:
- a **canon engine**
- a **runtime module loader / orchestrator**

### 3. Teach
Teach is the instructional wrapper around SkillForge.

Teach is used when the user wants:
- explanation
- guided learning
- stepwise breakdown
- coached understanding
- educational delivery

Teach wraps SkillForge and exposes it through natural language.

### 4. School
School is the higher-order curriculum/program wrapper around Teach.

School organizes:
- multi-step learning flows
- curricula
- learning paths
- structured teaching programs

### Relationship stack

School  
→ wraps Teach  
→ wraps SkillForge  
→ uses PASS-mined canon and modules

PASS sits beside this stack as the mining/export pipeline that feeds the Forge.

---

## Core definitions to lock

### PASS
**Pattern Analysis Skill System**

Locked meaning:
A source-analysis pipeline that extracts candidate patterns, drills, APs, tests, variants, and enrichments from source material across two review passes, logs rejects and deferred items, dedupes findings, and prepares a normalized candidate set for later canon review and placement.

### AP
**Original meaning: Application Protocols**

Historical drift:
- Application Protocols (original)
- Application Pack (later drift)
- Action Plans (later drift)

Rewrite rule:
- Preserve **AP** as the stable artifact label
- Record **Application Protocols** as the original expansion
- Record the later names as historical aliases
- Do not silently rename AP again

### SkillForge
Locked meaning:
A canon and runtime system that compares mined artifacts against existing canon, resolves their relationship to canon, and loads relevant modules to support execution, teaching, or generation tasks.

### Teach
Locked meaning:
An instructional wrapper that presents SkillForge capabilities through natural language as guided explanation, coaching, or learning support.

### School
Locked meaning:
A curriculum wrapper that organizes Teach flows into structured learning programs.

---

## Artifact classes to preserve

At minimum, the rewrite should preserve these artifact classes:

- Pattern
- Drill
- AP
- Test
- Variant
- Enhancement / Enrichment
- Alias
- Reject record

These classes were tracked in legacy PASS outputs and need explicit schema support.

---

## PASS design

### PASS mission
PASS exists to mine reusable skill/intelligence artifacts from source material.

A source may be:
- markdown
- text
- PDF
- document
- website
- comic
- programming book
- image-heavy book if parseable enough
- other source material containing extractable reusable logic

### PASS operating model

#### Stage 0 — Preflight
PASS should:
- identify source type
- check OCR / text quality if needed
- capture source metadata
- estimate domain/category/subcategory
- determine whether modernization overlay is needed
- prepare output structure

PASS should **not** require a live reliable registry check as a success condition.

Reason:
The old registry update path was not reliable enough. The more durable design is for PASS to emit a structured source/book markdown artifact for later manual placement.

#### Stage 1 — Harvest pass 1
PASS performs a deep first mining pass.

PASS should:
- read the source in context
- extract candidate patterns / drills / APs / tests / variants / enrichments
- capture where each came from
- capture why each was extracted
- capture why any candidate was rejected
- when a paragraph or unit contains multiple extractable topics, extract one cleanly and flag the other for second-pass recovery

This is the initial strip-mining pass.

#### Stage 2 — Normalize
PASS should:
- normalize names
- normalize artifact type
- normalize schema shape
- split mixed findings if needed
- standardize tags/categories
- preserve source traceability

#### Stage 3 — Dedupe pass 1
PASS should:
- collapse exact duplicates
- collapse obvious aliases
- mark uncertain overlaps for later review

#### Stage 4 — Recovery pass 2
PASS revisits:
- flagged secondary topics
- ambiguous units
- possible misses from pass 1
- uncertain overlaps
- deferred items

This second pass is mandatory. It was part of what made PASS trustworthy.

#### Stage 5 — Dedupe pass 2
After recovery, PASS should dedupe again.

Why:
The second pass can surface overlaps or collisions that were invisible after pass 1.

#### Stage 6 — Validation + reject check
PASS should validate:
- schema integrity
- category assignment
- duplicate state
- reject reasons
- unresolved flags
- modernization flags if applicable

Nothing should be silently rejected.

#### Stage 7 — Export
PASS should export:
1. source/book markdown
2. candidate artifact markdown
3. reject log
4. run summary
5. optional lane packs / teaching packs / skills packs

This export is the canonical PASS finish line.

---

## PASS output philosophy

### PASS is an extractor/exporter, not a self-updating librarian
The old design ran into trouble when registry mutation was treated as a hard dependency.

The corrected model is:

- PASS proposes
- you place
- SkillForge resolves canon over time

PASS should produce a markdown artifact for the source/book, and the human curator places it into the library/Forge later.

This is slower than full automation, but far more reliable.

---

## Registry / library model

### Manual source insertion
The source/book registry should be updated manually.

PASS should emit enough metadata to make manual placement easy:
- source title
- author if known
- source date
- medium
- subject/domain
- suggested category
- suggested subcategory
- modernization eligibility
- extraction summary
- portability/cross-compatibility note

### Why manual placement won
Because reliable automatic registry mutation was not solved well enough.

The better design:
- PASS emits the book/source markdown
- curator merges it into the library later
- canon structure stays curated and readable

---

## Forge organization model

SkillForge should be organized by:
- **category**
- **subcategory**
- then artifact collections inside those where useful

Example:
- Programming
  - C
  - Java
  - Software Fundamentals
  - Coding Protocols

### Cross-compatibility rule
A mined artifact is not locked forever to the narrow shelf of the source book if the concept is portable.

Example:
- coding structure ideas mined from C
- coding structure ideas mined from Java
- both may contribute upward into a shared subcategory such as **Coding Protocols**

So the Forge should support:
- origin tracking
- functional placement
- cross-source merge
- cross-subcategory compatibility
- higher-order rollup buckets

### Placement rule
Origin and placement are not the same thing.

- origin records where the concept came from
- placement records where it functionally belongs

That distinction should be declared explicitly.

---

## Modernization overlay

### Rule
If PASS mines a programming/code source older than **8 years**, it should run a **modernization overlay**.

### Important constraint
The modernization overlay should be **additive**, not destructive.

It should preserve:
- original source logic
- historical context
- original examples where worth keeping

It should add:
- modern equivalent
- deprecated/outdated element notes
- changed best practice
- compatibility notes
- upgrade warnings
- migration suggestions if relevant

### Suggested modernization fields
- `modernize_eligible`
- `source_age_years`
- `legacy_construct`
- `modern_equivalent`
- `deprecated_status`
- `upgrade_notes`
- `breaking_change_risk`
- `retain_original_examples`

---

## AP operational definition

Even though the wording drifted, the functional role is much clearer.

### Working rewrite definition
**APs are Application Protocols: reusable application/evaluation checks attached to a pattern, drill, process, or structure that help determine whether it is being applied correctly, clearly, and successfully.**

APs can:
- stand alone
- attach to patterns
- attach to drills
- act as evaluation criteria
- act as application guidance
- act as success/failure checks
- function as reusable test prompts during work

This definition fits the surviving examples much better than the later drifted names.

---

## SkillForge design

### SkillForge mission
SkillForge exists to:
- hold canon
- resolve new candidates against canon
- package reusable skill structures
- load relevant modules during actual work

### SkillForge comparison outcomes
For each PASS candidate, SkillForge should decide one of:

- **REJECT**
- **ADD_NEW**
- **REPLACE**
- **ENHANCE / ENRICH**
- **VARIANT**
- **ALIAS**

### Meaning of each outcome

#### REJECT
Candidate is:
- redundant
- weaker than canon
- invalid
- noisy
- too source-bound
- not canon-worthy

#### ADD_NEW
Candidate is new and deserves its own canon entry.

#### REPLACE
Candidate is superior to an existing canon item and should supersede it.

#### ENHANCE / ENRICH
Candidate improves an existing canon entry without replacing it.

#### VARIANT
Candidate is a meaningful variant of an existing item and should be attached under it.

#### ALIAS
Candidate is effectively the same operator under a different name.

---

## SkillForge runtime role

SkillForge is not just a library. It is also a **runtime orchestrator**.

When active, SkillForge should:
1. classify the task/problem
2. load relevant modules/patterns/APs/drills
3. apply constraints
4. run checks
5. iterate if needed
6. produce a result

This applies to:
- writing
- programming
- art workflows
- structured problem solving
- teaching support
- other module-driven tasks

---

## Teach vs Direct mode

This distinction needs to be locked because it matters.

### Teach mode
Used when the user wants:
- explanation
- teaching
- guided learning
- coaching
- breakdown of principles
- help understanding how to do something

Teach mode wraps SkillForge and exposes module knowledge in a learning-centered way.

### Direct mode
Used when the user wants the work done.

Direct mode includes:
- single-pass execution
- iterative execution
- structured production loops
- light-table style refinement
- drift-control workflows
- applied module use

### Important correction
The **light-table workflow belongs under Direct mode**, not Teach mode.

Why:
The light-table flow is not primarily instructional. It is a production/drift-control method.

Example:
- user requests an elf warrior
- SkillForge loads figure drawing / archetype / anatomy modules
- system offers:
  - iterative direct light-table flow
  - or final single-pass render

Both are Direct mode, even though one is iterative.

---

## Lane model

The old system used Lane A and Lane B.

### Historical behavior
- **Lane A** = Teaching
- **Lane B** = internal/operator/self-use

### Rewrite decision
Keep the lane concept, but do **not** let it define the whole architecture.

Lanes should become:
- output/render/use profiles
- not the core identity of PASS or SkillForge

### Recommended interpretation
- **Teaching lane** = explanatory / instructional / human-readable
- **Skills lane** = compact / operator-use / execution-ready

This preserves what worked without distorting the system into a fake dual-core design.

---

## Natural Language protocol

SkillForge could operate through natural language as a wrapper protocol.

This should be declared explicitly:
- natural language requests can trigger module loading
- module loading can support Teach mode or Direct mode
- the user does not need to know which module names are firing in order to benefit

Examples:
- “Draw me an elf warrior”
- “Help me write a C program”
- “Teach me how to shade cloth folds”
- “Show me the 4-step figure workflow”
- “Help me structure this scene”

All of these should be able to route through natural language into the right module family.

---

## Required schemas

### 1. PASS source record
Suggested fields:
- source_id
- title
- author
- date
- medium
- subject
- domain
- source_type
- OCR_state
- suggested_category
- suggested_subcategory
- modernize_eligible
- portability_notes
- extraction_summary

### 2. PASS candidate record
Suggested fields:
- candidate_id
- artifact_type
- stable_label
- name
- short_definition
- full_body
- source_ref
- extracted_from_unit
- tags
- category
- subcategory
- confidence
- rejection_status
- rejection_reason
- deferred_from_pass1
- recovered_in_pass2
- duplicate_of
- alias_of
- variant_of
- enriches
- modernization_notes

### 3. SkillForge canon record
Suggested fields:
- canon_id
- artifact_type
- stable_label
- name
- definition
- body
- tags
- APs
- checks
- variants
- enrichments
- aliases
- supersedes
- superseded_by
- source_history
- placement_category
- placement_subcategory
- last_updated

### 4. PASS run report
Suggested fields:
- run_id
- source_id
- timestamp
- stages_completed
- candidates_found
- patterns_new
- patterns_added
- variants_added
- patterns_rejected
- drills_added
- tests_added
- aps_added
- deferred_items
- recovered_items
- duplicates_removed
- validator_status
- notes

### 5. Reject log
Suggested fields:
- reject_id
- candidate_id
- artifact_type
- rejected_name
- source_ref
- rejection_reason
- near_match_if_any
- review_notes

---

## Rules that must be explicit

### Rule 1
PASS = Pattern Analysis Skill System

### Rule 2
AP original expansion = Application Protocols

### Rule 3
PASS and SkillForge are separate systems with a handoff, not one blended thing

### Rule 4
Teach wraps SkillForge

### Rule 5
School wraps Teach

### Rule 6
PASS does not rely on reliable automatic registry mutation

### Rule 7
Manual library placement is canonical

### Rule 8
Origin and functional placement are separate fields

### Rule 9
Second pass is mandatory

### Rule 10
Dedupe happens before and after second-pass recovery

### Rule 11
Rejects require explicit reasons

### Rule 12
Modernization overlay is additive, not destructive

### Rule 13
Lanes are output/use profiles, not the architecture itself

### Rule 14
Direct mode includes iterative production loops such as light-table workflows

### Rule 15
Natural language routing can invoke SkillForge modules without exposing internal complexity to the user

---

## Rewrite phases

### Phase 1 — Definition lock
Create one clean definition pass for:
- PASS
- SkillForge
- Teach
- School
- AP
- artifact classes
- comparison outcomes
- lane meaning
- direct vs teach mode
- modernization rule
- registry philosophy

### Phase 2 — Schema lock
Write:
- PASS source schema
- PASS candidate schema
- SkillForge canon schema
- reject log schema
- PASS run report schema

### Phase 3 — PASS flow rebuild
Declare the full PASS flow:
1. preflight
2. harvest pass 1
3. normalize
4. dedupe pass 1
5. recovery pass 2
6. dedupe pass 2
7. validate
8. export

### Phase 4 — SkillForge resolution rebuild
Declare:
1. intake candidate set
2. compare against canon
3. classify relation
4. resolve outcome
5. package final canon-safe output
6. expose driver-ready module structures

### Phase 5 — Teach/Direct routing rebuild
Declare:
- how NL requests trigger module loading
- when Teach mode is used
- when Direct mode is used
- when to offer both
- how iterative direct workflows are handled

### Phase 6 — Library/taxonomy rebuild
Declare:
- category/subcategory model
- cross-compatibility rules
- rollup bucket rules
- origin vs placement
- manual source insertion flow

### Phase 7 — Validation
Write validators for:
- missing fields
- unresolved aliases
- broken supersede chains
- missing reject reasons
- bad modernization records
- malformed lane packs
- malformed module tags

### Phase 8 — Promotion
Only after the above:
- promote PASS definitions out of draft
- promote SkillForge definitions out of draft
- then promote runtime pieces as earned

---

## Critical path

The true blocker is not missing ideas.

The true blocker is:
- missing definitions
- missing contracts
- missing schemas
- missing explicit rules

### Critical path order
1. definition lock
2. schema lock
3. handoff lock
4. comparison logic lock
5. modernization policy lock
6. taxonomy lock
7. teach/direct routing lock
8. then implementation/promotion

---

## Deliverables to create first

Create these files first (Use semver inside program. Do not add version to the filename):

1. `PASS_SPEC_v1.md`
2. `SKILLFORGE_SPEC_v1.md`
3. `TEACH_SPEC_v1.md`
4. `SCHOOL_SPEC_v1.md`
5. `PASS_TO_SKILLFORGE_HANDOFF_v1.md`
6. `PASS_GLOSSARY_v1.md`
7. `FORGE_TAXONOMY_v1.md`
8. `AP_HISTORY_NOTE_v1.md`

---

## Immediate next actions

### Minimum next-action set
1. Lock the definitions in writing
2. Lock AP history in writing
3. Lock PASS export philosophy in writing
4. Lock manual registry/library placement in writing
5. Lock category/subcategory + rollup model in writing
6. Lock Teach vs Direct routing in writing

### After that
Start MMU work and use the rebuilt memory model to support:
- glossary stability
- term lock
- handoff continuity
- taxonomy continuity
- module continuity

---

## Bottom line

The old system was not a bad idea. It was a strong organic system with weak term-locking and unreliable preservation.

The rewrite should preserve what worked:
- PASS mining
- second-pass recovery
- AP tracking
- modernization overlay
- SkillForge canon resolution
- module-based runtime behavior
- NL protocol routing
- Teach wrapper
- School wrapper
- category/subcategory organization
- cross-compatible rollups
- light-table style direct workflows

What needs to change is not the soul of the system.

What needs to change is:
- definitions
- contracts
- schemas
- explicit boundaries
- preservation discipline
