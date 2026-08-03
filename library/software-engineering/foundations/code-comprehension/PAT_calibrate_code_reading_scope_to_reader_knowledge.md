---
object_id: PAT_calibrate_code_reading_scope_to_reader_knowledge
object_type: pattern
name: Calibrate Code-Reading Scope to Reader Knowledge
library_path:
  - software-engineering
  - foundations
  - code-comprehension
stage_binding: 0 design
lane_fit: teach
foundation_role: foundation
routing_class: teaching
specialization_axis: none
foundation_object_id: none
tags:
  - onboarding
  - teaching
  - code_comprehension
  - cognitive_load
cross_links:
  - rel: related_to
    target_object_id: DRILL_reproduce_code_to_diagnose_knowledge
reference:
  source_id: programmers_brain
  source_title: "The Programmer's Brain: What Every Programmer Needs to Know About Cognition"
  author: Felienne Hermans
  publish_date: 2021
  media_type: PDF
  locator: u02, pp. 22-23
  evidence_type: mixed
confidence: high
references: []
variants: []
---

# Calibrate Code-Reading Scope to Reader Knowledge

## Pattern Rule
**IF** someone is reading a codebase, language, or domain whose key concepts are not yet in their long-term memory
**THEN** reduce the amount of code they must process at once and supply the missing concepts before expecting expert-sized comprehension.

## Do
- Choose a small coherent function or path whose behavior can be explained without chasing many dependencies.
- Identify unfamiliar keywords, structures, algorithms, and domain terms before increasing the size of the reading task.
- Compare progress on meaningful code, where learned concepts can form chunks, rather than on scrambled or arbitrary lines.

## Don't
- Don't assume strong performance in another language or domain gives immediate access to this codebase's chunks; unfamiliar local knowledge returns an expert to low-level reading.
- Don't interpret fewer recalled lines as lower general ability when the reader has had less opportunity to organize the relevant concepts.

## Checklist
- What language, algorithm, and domain knowledge does this reading slice assume?
- Can the reader explain each assumed concept before tackling the whole slice?
- Is the next increment in scope small enough to reuse concepts already learned?

## Notes
McKeithen's experiments found that experts recalled more meaningful ALGOL code than intermediates, who recalled more than beginners, but the groups performed similarly on scrambled programs. Hermans draws the onboarding lesson directly: a newcomer can process less code because fewer local chunks are available, even when that person is capable elsewhere. The teaching response is to adjust scope and prerequisites, not lower the learner's ceiling.
