# Baseline Before Destructive Work

object_id: baseline_before_destructive_work
object_type: blu_code_skill
category: protocol
subcategory: source_control
stage_binding: kernel_coding
lane_fit: deterministic
foundation_role: prevention_rule
tags:
- baseline
- rollback
- artifact_truth

## Objective
Always preserve a recoverable source before replacement files or overwrite advice.

## Trigger
Any replacement archive, rewrite, or broad kernel change.

## Steps / Flow
1. Copy uploaded source into `baseline/` inside the generated archive when file size permits.
2. Place changed files in a separate replacement path or clearly mark root replacement files.
3. Make the README say whether files are replacements, reference material, or memory-library entries.
4. Never call a generated file tested unless a real test/trace was run.

## Acceptance Checks
- Baseline present or explicitly impossible.
- Replacement scope is listed.
- Admin can restore previous files if replacement fails.
