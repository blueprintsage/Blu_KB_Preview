---
object_id: PAT_follow_a_consistent_coding_style
object_type: pattern
name: Follow a Consistent Coding Style Guide
library_path:
  - software-engineering
  - foundations
  - readability
stage_binding: 3 rough
lane_fit: both
foundation_role: foundation
routing_class: general
specialization_axis: none
foundation_object_id: none
tags:
  - coding_style
  - conventions
  - linters
  - readability
cross_links:
  - rel: related_to
    target_object_id: PAT_make_code_readable
reference:
  source_id: gcbc_think_like_swe
  source_title: "Good Code, Bad Code: Think Like a Software Engineer"
  author: Tom Long
  publish_date: 2021
  media_type: PDF
  locator: u05, pp. 115-117
  evidence_type: text
confidence: high
references: []
variants: []
---

# Follow a Consistent Coding Style Guide

## Pattern Rule
**IF** a stylistic choice is not dictated by the compiler — naming casing, indentation, feature usage, file layout
**THEN** follow the team's agreed coding style guide, because a shared style lets readers rely on conventions to understand code correctly.

## Do
- Lean on convention as information: with PascalCase classes and camelCase variables, `ConnectionManager.terminateAll()` reads unmistakably as a call into a class that likely touches global state.
- Adopt the team or organization style guide as-is where one exists; where none does, take an off-the-shelf one such as a published language style guide rather than inventing conventions.
- Run a linter to catch style-guide violations and some error-prone patterns automatically, as a cheap first pass.

## Don't
- Don't break the convention and let `connectionManager` (camelCase) masquerade as an instance variable when it is actually a class with a static `terminateAll()` — that misreading terminated every chat on the server, not one.
- Don't rely on the linter as a substitute for good code; linters catch only simple issues.

## Checklist
- Does naming casing let a reader tell classes from instances at a glance?
- Are you following the team's style guide rather than a personal style?
- Is a linter enforcing the conventions the guide specifies?

## Notes
The `GroupChat` bug is the cautionary tale: a class named `connectionManager` violates the PascalCase-for-classes convention, so a reader reasonably assumes it is an instance field and that `terminateAll()` affects only their chat, when it is static and terminates every connection on the server. A consistent style is like a whole team speaking one language fluently — it removes a class of misreadings, which is why Long frames adopting and following a style guide (backed by linters) as a readability and bug-prevention measure.
