# Control Fix vs Root Rewrite

object_id: control_fix_vs_root_rewrite
object_type: blu_code_skill
category: kernel_architecture
subcategory: strategy
stage_binding: kernel_coding
lane_fit: deterministic
foundation_role: prevention_rule
tags:
- strategy
- recovery
- scope

## Objective
Choose one recovery strategy before editing.

## Trigger
A subsystem is broken and multiple possible fixes exist.

## Steps / Flow
1. Classify the goal: immediate hard-stop/control fix, root rewrite, rollback, diagnostic, or full replacement.
2. Do not mix control hard-stops with root rewrites unless the plan explicitly sequences them.
3. For overwhelmed Admin or risky state, prefer complete files and a recoverable baseline.
4. Document the chosen strategy in README.

## Acceptance Checks
- One strategy is selected.
- Files touched match the strategy.
- No scope bounce between layers during the same repair.
