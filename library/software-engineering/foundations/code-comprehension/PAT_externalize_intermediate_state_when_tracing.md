---
object_id: PAT_externalize_intermediate_state_when_tracing
object_type: pattern
name: Externalize Intermediate State When Tracing Code
library_path:
  - software-engineering
  - foundations
  - code-comprehension
stage_binding: 3 rough
lane_fit: skill
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
  - code_comprehension
  - tracing
  - working_memory
  - debugging
cross_links:
  - rel: related_to
    target_object_id: PAT_diagnose_source_of_code_confusion
reference:
  source_id: programmers_brain
  source_title: "The Programmer's Brain: What Every Programmer Needs to Know About Cognition"
  author: Felienne Hermans
  publish_date: 2021
  media_type: PDF
  locator: u01, pp. 6-9
  evidence_type: mixed
confidence: high
references: []
variants: []
---

# Externalize Intermediate State When Tracing Code

## Pattern Rule
**IF** mentally executing code requires tracking more changing values and operations than you can reliably hold at once
**THEN** write each relevant intermediate value beside its line or in a trace table and advance the execution one step at a time.

## Do
- Record a variable immediately after the statement that changes it, so the state and the responsible operation stay adjacent.
- Keep only values that influence the behavior under investigation; use the written trace to free working memory for deciding what the next operation means.
- Treat the urge to scribble down values as evidence that the trace has exceeded working-memory capacity, not as a failure that more concentration will fix.

## Don't
- Don't recompute an earlier value from memory every time a later line needs it; repeated reconstruction consumes the same capacity needed to understand the control flow.
- Don't turn the trace into an indiscriminate dump of every symbol, because irrelevant state recreates the overload on paper.

## Checklist
- Does every recorded state change point to the exact line that produced it?
- Can I resume the trace after an interruption without reconstructing prior values?
- Does the table contain enough state to explain the behavior but omit values unrelated to the question?

## Notes
The BASIC conversion example remains difficult even when its keywords and operations are visible. Hermans annotates the listing with successive values and recommends a pen-and-paper or tabular trace when the small execution steps no longer fit in working memory. The move changes the job of working memory from storing the entire execution to processing one transition at a time.
