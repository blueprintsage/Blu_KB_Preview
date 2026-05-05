# State Commit Before Success

object_id: state_commit_before_success
object_type: blu_code_skill
category: state
subcategory: commit
stage_binding: kernel_coding
lane_fit: deterministic
foundation_role: prevention_rule
tags:
- state
- commit
- commands

## Objective
Prevent state-setting commands from printing success before committed state exists.

## Trigger
Commands that set prefs, modes, reminders, memory state, or continuation state.

## Steps / Flow
1. Define required state_delta.
2. Validate state_delta shape.
3. Apply state before success output.
4. Make success line match committed state exactly.
5. Read commands must read from committed state, not proposal text.

## Acceptance Checks
- Missing or rejected state proof blocks success.
- Confirmation line names the committed value.
- No automatic render occurs from state-only mode commands unless contract explicitly allows it.
