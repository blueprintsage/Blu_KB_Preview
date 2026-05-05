# Read BluCode Before Kernel Work

object_id: read_blucode_before_kernel_work
object_type: blu_code_skill
category: protocol
subcategory: preflight
stage_binding: kernel_coding
lane_fit: deterministic
foundation_role: prevention_rule
tags:
- preflight
- memory
- source_truth

## Objective
Prevent repeated coding mistakes by consulting the coding-memory library before changing Blu's kernel.

## Trigger
Any request to modify, rewrite, patch, export, debug, or test Blu kernel code.

## Steps / Flow
1. Open `blu_code/INDEX.md` first.
2. Select entries whose triggers match the current task.
3. Read the actual active kernel files next; BluCode never replaces source truth.
4. Choose one strategy: diagnostic, root rewrite, control fix, rollback/recovery, or artifact generation.
5. State the selected strategy in the README or final answer if an artifact is produced.

## Acceptance Checks
- Relevant BluCode entries were consulted or absence was stated.
- Active source files were inspected before exact replacement claims.
- No patch fragments are given when complete replacements are requested.

## Notes
Derived from the PASS pattern of using an index to select applicable patterns before execution.

## Reference Inputs
- Repo libraries/blu_code/INDEX.md
- PASS skill index pattern
