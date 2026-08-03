# PASS (Pattern Analysis Skill System) Roadmap

## Standing law boundary
These are not roadmap phases. They are always-on rules:

- repo index loads every chat
- repo templates must be used when applicable
- no stub patching presented as real work
- no version numbers in filenames
- full kernel/archive handoff plus changelog for patch deliveries

---

## Phase 0 — Identity and compiler contract
Lock what PASS is.

PASS is:
- a strict compiler
- the heavy-lift system for SkillForge and School
- a media-to-training-content transformer

PASS is not:
- a runtime
- a teacher
- a curriculum runner
- a live registry mutator

Lock the Triumvirate:
- PASS = compiler/content builder
- SkillForge = runtime
- School = curriculum/orchestration

Lock required outputs:
- source record
- candidate artifacts
- reject log
- run summary
- index patches
- Teaching lane pack
- Skill lane pack
- zip bundle

Exit condition:
- PASS identity, ownership, and output obligations are fixed

---

## Phase 1 — Preflight and lens system
Build the front door correctly.

Preflight must determine:
- media type
- OCR/text/image state
- author
- publish date
- category
- subcategory
- modernization flag
- lens selection

Lenses are:
- internal preflight routing aids
- not separate programs

Initial lens families:
- PDF
- comic
- web
- image
- document/text

Web must allow sub-lenses, for example:
- curriculum page
- course page
- lesson/day page
- general article/tutorial

Modernization rule:
- if source is older than 8 years and in programming/application domains, mark for modernization review

Exit condition:
- PASS can classify a source and choose an extraction posture before harvesting

---

## Phase 2 — Harvest engine
Implement the real gutting behavior.

PASS harvests:
- patterns
- drills
- APs
- tags
- variants
- duplicates
- rejects
- source traceability

Pattern rule:
- strict IF x THEN y
- add do’s
- add don’ts
- add checklist

Drill rule:
- short
- repeatable
- experience-building

AP rule:
- lesson/how-to unit
- usable by teaching and school

Exit condition:
- a source can be gutted into raw candidates with source traceability

---

## Phase 3 — Two-pass recovery model
Make the dual-pass behavior explicit and mandatory.

Pass 1:
- extract primary subject matter
- if section has multiple subjects:
  - extract one
  - flag the other for pass 2

Pass 2:
- revisit flagged content
- recover missed material
- revisit ambiguous sections

Exit condition:
- PASS can complete a full two-pass run on one source

---

## Phase 4 — Normalize and dedupe
Stabilize the output shape.

Normalize:
- names
- artifact types
- schema shape
- tags
- categories
- subcategories

Dedupe pass 1:
- exact duplicates
- obvious aliases
- uncertain overlaps flagged

Dedupe pass 2:
- re-run after recovery pass
- resolve collisions surfaced by pass 2

Exit condition:
- all harvested artifacts conform to one stable schema and duplicate rules

---

## Phase 5 — Compare against repo canon
Make PASS decide what belongs.

For each candidate, compare against relevant repo content and decide:
- REJECT
- ADD
- VARIANT
- UPDATE

Rules:
- no silent rejects
- all rejects need explicit reasons
- variants must preserve provenance
- updates must identify what they supersede or improve

Exit condition:
- PASS can classify repo relationship for every candidate

---

## Phase 6 — Export contract
Emit stable artifacts every run.

Required exports:
- source/book markdown
- candidate artifact files
- reject log
- run summary
- Teaching lane pack
- Skill lane pack
- index patches

Packaging:
- zip bundle at end of run

This is the real PASS finish line.

Exit condition:
- a complete repo-ready PASS bundle exists for one source

---

## Phase 7 — AIO / School feed mode
Build the curriculum-specific compiler path.

This is the immediate priority.

PASS must strip All in One Homeschool / Easy Peasy course pages into School-native outputs.

Important rules:
- do not depend on My EP Assignments
- School should consume our own generated records
- day number is progression-based, not calendar-based

AIO course output must include:
- course backbone
- day records
- block/semester bindings
- grade hooks

Course truths already locked:
- 180-day full-year model
- 90-day semester model
- 6 blocks
- 30 school days per block
- daily grades
- 6-week average model
- semester average model

Exit condition:
- one AIO course can be compiled into School-ready files cleanly

---

## Phase 8 — Parser hardening
Fix source reliability before scaling.

Known truth:
- text-marker lesson detection worked
- HTML/link-preserving parser regressed detection and produced broken 118-day output

So the hardening order is:
1. restore the last good text-marker detector behavior
2. re-prove lesson/day detection
3. layer link/resource preservation carefully
4. handle shared lessons with levels.ALL
5. stop footer contamination / end-of-page garbage

Exit condition:
- one course parses correctly with:
  - correct lesson count
  - preserved links/resources
  - no footer junk
  - valid shared-day fallback

---

## Phase 9 — Full AIO crawl
Scale from one course to the full homeschool inventory.

Use:
- CATALOG_SUMMARY.md as class backbone
- AIO course pages as lesson/day source

Build:
- all grades
- all subjects
- all courses
- all 180/90-day structures

Output organization:
- grade → subject/course → day files

Exit condition:
- full AIO curriculum feed exists for School

---

## Phase 10 — School compatibility audit
Confirm PASS output matches real School needs.

Do not rebuild School blindly.

Check:
- course backbone compatibility
- day-record compatibility
- grading bindings
- semester/block bindings
- runtime consumption expectations

Patch only mismatches.

Exit condition:
- PASS output and School input are aligned

---

## Phase 11 — SkillForge feed validation
Confirm both lane packs are usable.

SkillForge depends on:
- Teaching lane
- Skill lane

PASS must always produce both.

Validate:
- Teaching lane is usable for instruction
- Skill lane is usable for execution/creation
- nearest-skillset fallback rules still hold when no exact skillset exists

Exit condition:
- PASS output is runtime-usable by SkillForge

---

## Phase 12 — Promotion
Only after verification.

Promote PASS when:
- all stages work
- one-source runs are real
- AIO compiler path works
- School compatibility is proven
- lane packs are valid
- zip handoff is correct
- changelog reflects real work only

Exit condition:
- PASS is no longer draft/spec-only

---

# Immediate execution priority
Right now the roadmap priority is:

1. Phase 0 lock
2. Phase 1 preflight/lenses
3. Phase 2–6 core compiler path
4. Phase 7–9 AIO school-feed path
5. Phase 10 School compatibility
6. Phase 11 SkillForge validation
7. Phase 12 promotion

# One-line roadmap summary
Build PASS as a strict compiler first, then use it to generate School-ready AIO curriculum feeds and runtime-ready SkillForge lane packs from one stable contract.
