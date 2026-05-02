# DOM Lookup Before Mutation

object_id: dom_lookup_before_mutation
object_type: pattern
category: coding
subcategory: language_contexts/javascript/browser
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
tags:
- beginner_programming
- modernization
- javascript
cross_links:
- related_to: coding/core_mechanics
reference:
- source_title: Programming for Beginners
- author: Matthew Python
- publish_date: Unknown
- media_type: epub
- evidence_type: text
confidence: medium

## Pattern Rule
**IF** code changes page content  
**THEN** locate and verify the target element first  
**ELSE** the mutation may silently fail

## Do
- Keep the primary skill goal intact.
- Use the modernized form in new work.

## Don't
- Preserve outdated syntax or tooling when a current form is safer.

## Checklist
- Input identified
- Output identified
- Failure mode checked

## Modernization
This object has been modernized for current beginner practice. Legacy examples from the source are treated as concept evidence, not final execution form.
