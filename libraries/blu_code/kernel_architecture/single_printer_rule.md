# Single Printer Rule

object_id: single_printer_rule
object_type: blu_code_skill
category: kernel_architecture
subcategory: print
stage_binding: kernel_coding
lane_fit: deterministic
foundation_role: prevention_rule
tags:
- printer
- ownership
- exec

## Objective
Avoid split-brain output by assigning exactly one public printer.

## Trigger
Any feature with multiple support libraries or expressive layers.

## Steps / Flow
1. Identify all candidate producers of public text.
2. Choose one printer at Exec or the owning Program.
3. Make other layers structured/propose-only.
4. Add validation that blocks public-shaped text from non-printers.
5. Test that fallback/persona/humor cannot mutate the line.

## Acceptance Checks
- Exactly one printer exists.
- Support layers cannot emit public line shapes.
- Observed output cannot come from a non-printer without being blocked.
