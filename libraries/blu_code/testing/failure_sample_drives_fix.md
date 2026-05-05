# Failure Sample Drives Fix

object_id: failure_sample_drives_fix
object_type: blu_code_skill
category: testing
subcategory: debugging
stage_binding: kernel_coding
lane_fit: deterministic
foundation_role: prevention_rule
tags:
- debugging
- regression
- sample

## Objective
Use exact observed output to determine the failing layer.

## Trigger
User provides screenshot, trace output, or broken command line.

## Steps / Flow
1. Transcribe exact output.
2. Compare it to the expected contract.
3. Identify the earliest layer capable of producing that shape.
4. Patch/rewrite that layer only.
5. Add the sample as a regression test.

## Acceptance Checks
- Exact sample is preserved.
- Fix reason cites sample shape, not vibes.
- No speculative broad rewrite if sample proves a narrow route failure.
