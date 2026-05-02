# Validate External Input Before Use

object_id: validate_external_input_before_use
object_type: pattern
category: coding
subcategory: input_output/user_input
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
tags:
- beginner_programming
- modernization
- coding
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
**IF** data enters from user, file, browser, serial, or sensor  
**THEN** validate shape and range before acting  
**ELSE** bad input drives bad behavior

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

## Variants
### Variant: JavaScript text input
Use this variant when the same rule appears in that specific context.
### Variant: Arduino analog sensor range
Use this variant when the same rule appears in that specific context.
