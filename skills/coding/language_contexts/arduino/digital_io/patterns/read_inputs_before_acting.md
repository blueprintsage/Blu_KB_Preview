# Read Inputs Before Acting

object_id: read_inputs_before_acting
object_type: pattern
category: coding
subcategory: language_contexts/arduino/digital_io
stage_binding: 1 skeleton
lane_fit: both
foundation_role: foundation
tags:
- beginner_programming
- modernization
- arduino
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
**IF** hardware output depends on a button or sensor  
**THEN** read input state before writing output  
**ELSE** the sketch acts on stale assumptions

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
