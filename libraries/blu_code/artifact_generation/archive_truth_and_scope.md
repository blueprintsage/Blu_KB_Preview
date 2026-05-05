# Archive Truth And Scope

object_id: archive_truth_and_scope
object_type: blu_code_skill
category: artifact_generation
subcategory: delivery
stage_binding: kernel_coding
lane_fit: deterministic
foundation_role: prevention_rule
tags:
- archive
- truth
- scope

## Objective
Make generated archives honest and easy to apply.

## Trigger
Any generated zip, full-file package, patch package, or memory-library archive.

## Steps / Flow
1. Generate files before describing them.
2. Include README with purpose, contents, replacement/reference status, and scope.
3. Do not include files outside requested scope.
4. Do not claim source inspection beyond what was actually read.
5. Link the generated archive.

## Acceptance Checks
- Archive exists at linked path.
- README matches contents.
- No unauthorized files such as `00_Instructions.md` are included when excluded.
