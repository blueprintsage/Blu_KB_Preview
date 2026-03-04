---
capsule_id: skill.programming.software_craft.B
title: "Skills — Software Craft (Lane B)"
date: 2026-03-03
updated: 2026-03-03
version: 0.1.0
status: draft
topic: skills
type: skill_lane_b
tags: [programming, software_craft]
visibility: shared
schema: capsule_header_v1.1
body_schema: blu_modular_v1
sources:
  - pragmatic_programmer
  - passionate_programmer
---

# Skills — Software Craft (Lane B)


module: skill.programming.software_craft.b.meta | name="META"
- purpose: canonical law layer for software craft + professional practice
- spine: ["Skeleton","Block","Rough","Final"]
- sources: ["Pragmatic Programmer", "Passionate Programmer (2e)"]
- note: This is a curated nuclear rip (v0.1). Future passes can expand counts.
/module


module: skill.programming.software_craft.b.patterns | name="PATTERNS (LAWS)"
### SC-PAT-001
- IF: you are asked for a decision or estimate
- THEN: provide options with tradeoffs and assumptions instead of excuses
- CHECK: response contains >=2 options + tradeoffs + assumptions
- FAIL: pause work; request missing constraints
- NOTES: Keeps communication actionable.
- REF: PP Tip theme

### SC-PAT-002
- IF: a defect or broken behavior is discovered
- THEN: fix it now or create a tracked, time-bounded repair task before proceeding
- CHECK: defect is fixed OR ticket created with owner+deadline
- FAIL: block merge/release
- NOTES: Broken-window prevention.
- REF: PP broken windows theme

### SC-PAT-003
- IF: you are about to ship code you do not understand
- THEN: stop and reduce uncertainty (read, test, or spike) before shipping
- CHECK: unknowns are enumerated and resolved or explicitly accepted
- FAIL: do not ship
- NOTES: No hidden bombs.
- REF: PP 'think about your work' theme

### SC-PAT-010
- IF: you touch a file or module
- THEN: leave it cleaner than you found it
- CHECK: diff shows net reduction in complexity or improved clarity/tests
- FAIL: revert and refactor properly
- NOTES: Small improvements compound.
- REF: PP craftsmanship theme

### SC-PAT-011
- IF: a workaround is proposed as a permanent solution
- THEN: convert it into a proper fix or mark it as temporary with an expiry
- CHECK: temporary items have expiry + plan OR replaced by proper fix
- FAIL: reject workaround
- NOTES: Prevents entropy.
- REF: PP broken windows theme

### SC-PAT-020
- IF: the same knowledge exists in two places
- THEN: refactor so it has a single authoritative source
- CHECK: one source of truth remains; callers reference it
- FAIL: block merge
- NOTES: Duplication breeds divergence.
- REF: PP DRY theme

### SC-PAT-021
- IF: you must duplicate temporarily to meet a deadline
- THEN: wrap it with a TODO and a removal plan
- CHECK: TODO includes date/owner and removal steps
- FAIL: quarantine change
- NOTES: Controlled debt only.
- REF: PP pragmatic tradeoff theme

### SC-PAT-030
- IF: a repetitive task is performed more than twice
- THEN: automate it (script, make target, CI job)
- CHECK: task becomes one-command repeatable
- FAIL: stop repeating manually
- NOTES: Automation protects consistency.
- REF: PP automation theme

### SC-PAT-031
- IF: a build/test step depends on a human remembering it
- THEN: encode it into CI
- CHECK: CI fails when step omitted
- FAIL: block release
- NOTES: Humans forget; pipelines don't.
- REF: PP automation theme

### SC-PAT-040
- IF: you change behavior
- THEN: add or update a test that would fail if the change regresses
- CHECK: test fails without change and passes with change
- FAIL: rework until test exists
- NOTES: Proof before confidence.
- REF: PP testing theme

### SC-PAT-041
- IF: a bug is fixed
- THEN: add a regression test reproducing the bug
- CHECK: test reproduces old bug and now passes
- FAIL: do not close issue
- NOTES: Lock the door after intrusion.
- REF: PP testing theme

### SC-PAT-050
- IF: a module has more than one reason to change
- THEN: split responsibilities
- CHECK: each module has a single clear purpose
- FAIL: pause feature; refactor
- NOTES: Cohesion reduces complexity.
- REF: PP design principles theme

### SC-PAT-051
- IF: a change requires touching many unrelated files
- THEN: introduce an abstraction/boundary to localize change
- CHECK: change affects fewer modules over time
- FAIL: block new features until boundary exists
- NOTES: Coupling tax.
- REF: PP orthogonality theme

### SC-PAT-052
- IF: an API is unclear to a new reader
- THEN: improve names and add examples/tests until intent is obvious
- CHECK: a fresh reader can describe intent correctly
- FAIL: rewrite interface
- NOTES: Readability is a feature.
- REF: PP readability theme

### SC-PAT-060
- IF: you are unsure whether a refactor is safe
- THEN: write tests / characterization checks first
- CHECK: baseline behavior captured
- FAIL: do not refactor yet
- NOTES: Safety net first.
- REF: PP refactor theme

### SC-PAT-061
- IF: you need to make a large change
- THEN: do it in small reversible steps with checkpoints
- CHECK: each step is buildable/testable
- FAIL: stop and reduce step size
- NOTES: Stone-soup incrementalism.
- REF: PP incremental change theme

### SC-PAT-070
- IF: you are stagnant in a role
- THEN: schedule deliberate practice and ship learning artifacts
- CHECK: monthly artifact exists (blog, repo, notes, talk)
- FAIL: pick one focus and start
- NOTES: Learning is part of the job.
- REF: PP2 knowledge portfolio theme

### SC-PAT-071
- IF: you choose a technology path
- THEN: evaluate it against market demand + personal fit + opportunity cost
- CHECK: written rationale exists
- FAIL: delay decision until rationale exists
- NOTES: Career is product strategy.
- REF: PP2 career strategy theme

### SC-PAT-072
- IF: you rely on a single skill/tech for your livelihood
- THEN: diversify with adjacent skills
- CHECK: portfolio includes >=3 complementary competencies
- FAIL: set learning plan
- NOTES: Avoid single-point career failure.
- REF: PP2 portfolio theme

### SC-PAT-080
- IF: requirements are ambiguous
- THEN: write down assumptions and confirm them
- CHECK: assumptions confirmed in writing
- FAIL: stop and ask
- NOTES: Kills rework.
- REF: PP pragmatic communication theme

### SC-PAT-081
- IF: a team disagreement stalls progress
- THEN: propose a small experiment with success criteria
- CHECK: experiment run; criteria met/unmet
- FAIL: escalate with evidence
- NOTES: Evidence beats opinions.
- REF: PP/PP2 experimentation theme

### SC-PAT-100
- IF: you are about to merge
- THEN: run full local checks (format/lint/tests)
- CHECK: checks pass
- FAIL: block merge
- NOTES: Baseline quality gate.
- REF: PP/PP2 general practice

### SC-PAT-101
- IF: you handle secrets or credentials
- THEN: store and access them via approved secret management
- CHECK: no secrets in repo/logs
- FAIL: revoke and rotate secrets
- NOTES: Security hygiene.
- REF: PP/PP2 general practice

### SC-PAT-102
- IF: you change hot-path code
- THEN: measure before/after with a benchmark
- CHECK: benchmark shows expected impact
- FAIL: revert or optimize
- NOTES: No perf myths.
- REF: PP/PP2 general practice

### SC-PAT-103
- IF: you add a non-obvious behavior
- THEN: document it near the code and in user-facing docs if needed
- CHECK: docs updated
- FAIL: reject change
- NOTES: Future you is a user.
- REF: PP/PP2 general practice

### SC-PAT-104
- IF: you catch or suppress an error
- THEN: either handle it or propagate with context; never swallow silently
- CHECK: errors logged/handled with context
- FAIL: fix handling
- NOTES: Silent failure is debt.
- REF: PP/PP2 general practice

### SC-PAT-105
- IF: you add a dependency
- THEN: justify it and pin/lock versions
- CHECK: rationale + lockfile updated
- FAIL: reject dep
- NOTES: Dependency is a liability.
- REF: PP/PP2 general practice

### SC-PAT-106
- IF: you ship a new feature
- THEN: add logs/metrics/traces adequate to debug failures
- CHECK: signals exist and are useful
- FAIL: pause release
- NOTES: You can't fix what you can't see.
- REF: PP/PP2 general practice

### SC-PAT-107
- IF: you cut a release
- THEN: use a checklist and rollback plan
- CHECK: checklist + rollback exist
- FAIL: stop release
- NOTES: Discipline prevents incidents.
- REF: PP/PP2 general practice

/module

module: skill.programming.software_craft.b.tests | name="TESTS"
### SC-TST-001
- targets: ['SC-PAT-001']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (response contains >=2 options + tradeoffs + assumptions).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-002
- targets: ['SC-PAT-002']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (defect is fixed OR ticket created with owner+deadline).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-003
- targets: ['SC-PAT-003']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (unknowns are enumerated and resolved or explicitly accepted).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-010
- targets: ['SC-PAT-010']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (diff shows net reduction in complexity or improved clarity/tests).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-011
- targets: ['SC-PAT-011']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (temporary items have expiry + plan OR replaced by proper fix).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-020
- targets: ['SC-PAT-020']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (one source of truth remains; callers reference it).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-021
- targets: ['SC-PAT-021']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (TODO includes date/owner and removal steps).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-030
- targets: ['SC-PAT-030']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (task becomes one-command repeatable).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-031
- targets: ['SC-PAT-031']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (CI fails when step omitted).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-040
- targets: ['SC-PAT-040']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (test fails without change and passes with change).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-041
- targets: ['SC-PAT-041']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (test reproduces old bug and now passes).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-050
- targets: ['SC-PAT-050']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (each module has a single clear purpose).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-051
- targets: ['SC-PAT-051']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (change affects fewer modules over time).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-052
- targets: ['SC-PAT-052']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (a fresh reader can describe intent correctly).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-060
- targets: ['SC-PAT-060']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (baseline behavior captured).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-061
- targets: ['SC-PAT-061']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (each step is buildable/testable).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-070
- targets: ['SC-PAT-070']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (monthly artifact exists (blog, repo, notes, talk)).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-071
- targets: ['SC-PAT-071']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (written rationale exists).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-072
- targets: ['SC-PAT-072']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (portfolio includes >=3 complementary competencies).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-080
- targets: ['SC-PAT-080']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (assumptions confirmed in writing).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-081
- targets: ['SC-PAT-081']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (experiment run; criteria met/unmet).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-100
- targets: ['SC-PAT-100']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (checks pass).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-101
- targets: ['SC-PAT-101']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (no secrets in repo/logs).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-102
- targets: ['SC-PAT-102']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (benchmark shows expected impact).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-103
- targets: ['SC-PAT-103']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (docs updated).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-104
- targets: ['SC-PAT-104']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (errors logged/handled with context).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-105
- targets: ['SC-PAT-105']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (rationale + lockfile updated).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-106
- targets: ['SC-PAT-106']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (signals exist and are useful).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

### SC-TST-107
- targets: ['SC-PAT-107']
- setup: Given a change request in scope of the pattern.
- steps: Attempt to proceed without satisfying the CHECK; then satisfy the CHECK.
- pass: Fails when CHECK not met; passes when CHECK met (checklist + rollback exist).
- fail: Proceeds despite CHECK not met, or cannot be validated.
- notes: Minimum viable proof test.

/module

module: skill.programming.software_craft.b.drills | name="DRILLS (MACHINE)"
### SC-DRILL-B-001
- targets: ['SC-PAT-030', 'SC-PAT-031']
- inputs: Pick one repetitive task from your last week.
- procedure: Automate it into a one-command script; wire into CI if applicable.
- scoring: PASS if task is one-command and CI-enforced where relevant.
- stop: Stop after 60 minutes; log next steps.
- notes: Automation muscle.

### SC-DRILL-B-002
- targets: ['SC-PAT-020']
- inputs: Find one duplication instance in current codebase.
- procedure: Refactor to single source of truth; add tests.
- scoring: PASS if duplication removed and tests cover.
- stop: Stop if scope expands beyond one module; reduce.
- notes: DRY discipline.

### SC-DRILL-B-003
- targets: ['SC-PAT-060', 'SC-PAT-061']
- inputs: Select a messy module.
- procedure: Write characterization tests; refactor in 3 reversible steps.
- scoring: PASS if behavior preserved and each step is buildable/testable.
- stop: Stop after 90 minutes; commit partial improvements.
- notes: Safe refactor.

/module

module: skill.programming.software_craft.b.aps | name="APs"
### SC-AP-001
- trigger: Need to respond to uncertainty/ambiguity
- inputs: Question + context
- procedure: List unknowns; write assumptions; propose 2 options with tradeoffs; ask for confirmation on constraints.
- checks: Assumptions confirmed in writing; option chosen.
- fails: Pause implementation; escalate with written summary.
- targets: ['SC-PAT-001', 'SC-PAT-080']

### SC-AP-002
- trigger: Fixing a bug
- inputs: Bug report + reproduction steps
- procedure: Reproduce; write failing test; fix; verify; add regression test; update notes.
- checks: Regression test exists and passes.
- fails: Do not close issue.
- targets: ['SC-PAT-041']

### SC-AP-003
- trigger: Preparing to merge
- inputs: Branch + CI pipeline
- procedure: Run format/lint/tests; update docs if needed; ensure checklist complete.
- checks: All checks pass; checklist complete.
- fails: Block merge.
- targets: ['SC-PAT-100', 'SC-PAT-031']

/module

module: skill.programming.software_craft.b.ledger | name="LEDGER"
- 2026-03-03: initial curated nuclear rip (v0.1) from Pragmatic Programmer + Passionate Programmer
/module
