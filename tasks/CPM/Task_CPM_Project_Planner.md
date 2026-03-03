capsule_id: kb__tasks_cpm_task_cpm_project_planner_md__331438
title: "Task CPM Project Planner"
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

module: tasks__task_cpm_project_planner.M01 | name="Body"
<!-- REPO-ONLY: This module lives in the repo and is not mounted by default. -->

---
capsule_id: blu__10_task_cpm_project
title: "10 Task — CPM Project Planner"
date: 2026-02-18
updated: 2026-02-18
version: 0.8.1-addon
status: draft  # draft|active|locked
topic: tasks
type: spec
tags: [tasks, cpm, planning, project, v]
sensitivity: high  # low|med|high|critical
visibility: private    # shared|private
source: doc
domain: task
schema: capsule_header_v1.1
body_schema: blu_modular_v1
---

**10 Task — CPM Project Planner**

module: blu__10.M01 | name="Task: CPM_Project_Plan"
name: CPM_Project_Plan
goal: Produce a Critical Path Method (CPM) plan: activities, dependencies, schedule, critical path, risks, and next actions.
cadence: on-demand (triggered)
consent: explicit  # user must opt-in to CPM mode for their project
stop: "stop cpm"
visibility_pref_key: prefs.cpm.visibility  # show|silent
defaults:
  output_mode: show   # show|silent (unless user overrides)
  duration_units: days
  rounding: 0.5       # round durations to nearest 0.5 unless user says otherwise
  schedule_style: simple  # simple|detailed
trigger_rules:
- if user says: "critical path", "CPM", "dependencies", "timeline", "project plan"
- OR user uses command: "CMD:CPM PLAN"
hard_rules:
- CPM never overrides Identity/Operations/OPSEC.
- Ask at most 1 clarifying question unless blocked or user requests deep mode.
- If info missing, assume reasonable defaults and label assumptions.

module: blu__10.M02 | name="CPM_Intent_Gate"
**Minimal gate (one question max)**
If CPM is not explicitly requested:
- Ask: "Do you want a Critical Path (CPM) plan for this? (yes/no)"
If CPM is explicitly requested:
- Proceed without asking.

module: blu__10.M03 | name="CPM_Intake_Minimum"
**Minimum inputs (prefer assumptions if user didn’t provide)**
required_minimum:
- project_goal: what "done" looks like
- major_deliverables: 3–12 items
- constraints: any hard dates / fixed events
optional_if_available:
- team/resources
- working cadence (days/week)
- risk tolerance

**One-question rule (choose the biggest blocker):**
If blocked, ask ONE:
- "What’s the target deadline (or date you want 'done')?"

Otherwise assume:
- target_deadline: none
- cadence: 5 workdays/week

module: blu__10.M04 | name="CPM_Method_Steps"
**Method (deterministic)**
A) Decompose
- Convert goal → deliverables → activities (tasks you can finish in 0.5–5 days).
- If an activity >5 days, split.

B) Dependency graph
- For each activity, define predecessors (what must be done first).
- Use FS (finish-to-start) dependencies by default.

C) Duration estimates
- If user gives durations, use them.
- Else estimate via:
  - small = 0.5–1 day
  - medium = 1–3 days
  - large = 3–5 days
Label as estimates.

D) Forward pass (earliest times)
- ES(activity) = max(EF(predecessors))
- EF(activity) = ES + duration

E) Backward pass (latest times)
- Start from project finish = max(EF)
- LF(activity) = min(LS(successors)) (or project finish if none)
- LS(activity) = LF - duration

F) Slack + critical path
- Slack = LS - ES
- Critical path = all activities with Slack == 0 (or smallest slack bucket if rounding)

G) Milestones + checkpoints
- Promote key deliverables to milestones.
- Add review/QA gates where failure is costly.

H) Risks + mitigations
- Identify top 3–7 risks on critical path.
- Add mitigations or buffer tasks.

module: blu__10.M05 | name="CPM_Output_Format_Show"
**Output (SHOW mode)**
Return in this order:
1) Assumptions (if any)
2) Activity table (ID, activity, duration, predecessors)
3) CPM results summary
   - Project duration
   - Critical path (sequence)
   - Slack notes (top 3 near-critical tasks)
4) Milestones (with target EF)
5) Risks + mitigations (linked to critical tasks)
6) Next actions (3–7 bullets)

Activity table example columns:
- ID | Activity | Dur | Pred | ES | EF | LS | LF | Slack

module: blu__10.M06 | name="CPM_Output_Format_Silent"
**Output (SILENT mode)**
Return only:
- Critical path sequence
- Milestones
- Next actions
(Keep assumptions internal unless user asks.)

module: blu__10.M07 | name="CPM_Quality_Checks"
**QC (run before presenting)**
- No orphan tasks: every non-start task has ≥1 predecessor OR is explicitly marked "parallel start".
- No cycles: dependency graph must be acyclic.
- Durations sane: 0.5–5 days per activity (or explicitly flagged as "long" with split suggestion).
- At least 1 milestone per major deliverable.
- Critical path is contiguous (each item depends on previous) OR explain branches.

module: blu__10.M08 | name="CPM_Command_Hooks"
**Suggested command hooks (to be added in 03_Commands or Operations command section)**
- CMD:CPM ON  → set prefs.cpm.visibility=show (and enable CPM prompting for V if desired)
- CMD:CPM OFF → disable CPM prompting
- CMD:CPM PLAN → run Task: CPM_Project_Plan
- CMD:CPM SILENT → set prefs.cpm.visibility=silent then run CPM plan
/module
