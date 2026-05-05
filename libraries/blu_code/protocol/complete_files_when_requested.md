# Complete Files When Requested

object_id: complete_files_when_requested
object_type: blu_code_skill
category: protocol
subcategory: delivery
stage_binding: kernel_coding
lane_fit: deterministic
foundation_role: prevention_rule
tags:
- delivery
- admin
- complete_files

## Objective
Respect Admin's requested delivery mode and avoid turning him into a patch integrator.

## Trigger
Admin asks for full files, complete replacements, or says patching/coding is not his thing.

## Steps / Flow
1. Generate complete replacement files or an archive.
2. Do not provide insertion snippets as the primary deliverable.
3. Do not invent headings; build from the uploaded active file structure.
4. Include a concise README naming exact files to replace.

## Acceptance Checks
- No 'put this somewhere' instructions.
- All replacement files are present.
- The archive can be applied by copying files, not editing internals.
