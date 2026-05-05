# Code-Agnostic Lessons First

object_id: code_agnostic_lessons_first
object_type: blu_code_skill
category: skillforge
subcategory: generalization
stage_binding: kernel_coding
lane_fit: deterministic
foundation_role: prevention_rule
tags:
- generalization
- index
- memory

## Objective
Prevent overfitting BluCode lessons to one subsystem when the principle is broader.

## Trigger
Writing or updating BluCode entries after a bug.

## Steps / Flow
1. Ask whether the lesson applies to all commands, all deterministic lanes, all artifacts, or only one subsystem.
2. Write the broadest truthful rule.
3. Put subsystem examples under examples, not in the rule name, unless unique.
4. Avoid hardcoding `/mood` in a lesson that applies to `/cpm`, `/memory`, or `/remind` too.

## Acceptance Checks
- Rule title and trigger are broad enough.
- Subsystem examples are clearly examples.
- Future coding tasks can reuse the lesson outside Mood.
