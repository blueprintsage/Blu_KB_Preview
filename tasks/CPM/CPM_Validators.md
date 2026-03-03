capsule_id: kb__tasks_cpm_cpm_validators_md__41e160
title: "CPM Validators"
date: 2026-02-24
updated: 2026-02-24
version: 0.1.0
status: draft
topic: blu
type: spec
tags: ['tasks', 'CPM']
sensitivity: medium
visibility: shared
source: repo
domain: tasks
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

# Untitled

---

module: tasks__cpm_validators.M01 | name="Body"
<!-- REPO-ONLY: This module lives in the repo and is not mounted by default. -->

---
capsule_id: blu__10_cpm_validators
title: "10 Validators — CPM"
date: 2026-02-18
updated: 2026-02-18
version: 0.8.1-addon
status: draft  # draft|active|locked
topic: validators
type: spec
tags: [validators, cpm, qc]
sensitivity: high  # low|med|high|critical
visibility: private
source: doc
domain: qc
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

**10 Validators — CPM**

module: blu__10.V01 | name="QC_CPM_NO_CYCLES"
- Fail if any activity depends (directly or indirectly) on itself.
- Fix: remove cycle by splitting deliverable, inserting dependency gate, or clarifying true predecessor.

module: blu__10.V02 | name="QC_CPM_NO_ORPHANS"
- Warn if a task is neither a start task nor has predecessors.
- Fix: mark as "parallel start" or add missing predecessor.

module: blu__10.V03 | name="QC_CPM_DURATION_BOUNDS"
- Warn if duration > 5 days and not explicitly allowed.
- Fix: split into sub-activities with intermediate deliverables.

module: blu__10.V04 | name="QC_CPM_MILESTONE_COVERAGE"
- Warn if a major deliverable has no milestone/checkpoint.
- Fix: add milestone at deliverable completion + add review gate if needed.

module: blu__10.V05 | name="QC_CPM_NEAR_CRITICAL"
- Identify tasks with slack <= 1 day (or <=10% of project duration) as near-critical.
- Fix: add buffer/mitigation, or re-sequence to reduce risk concentration.
/module
