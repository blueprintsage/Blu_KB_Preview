# Sketch Has Setup And Loop Roles

object_id: sketch_has_setup_and_loop_roles
object_type: pattern
category: coding
subcategory: language_contexts/arduino/core
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
**IF** writing Arduino code  
**THEN** place one-time configuration in setup and repeated behavior in loop  
**ELSE** hardware behavior becomes unstable

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
### Variant: Minimal Blink sketch
Use this variant when the same rule appears in that specific context.
### Variant: Sensor polling sketch
Use this variant when the same rule appears in that specific context.
