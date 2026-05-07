# BC-SKILL-011 — High-Authority File Friction

## Trigger

Use before modifying Instructions, Persona, Operations Law, identity anchors, bootloader text, or other high-authority source.

## Failure Pattern

Implementation bugs are patched by widening bootloader/law/persona files, wasting scarce instruction budget and hiding the broken owner.

## Do

1. Patch the broken owner first: Program, service, library, command surface, or Exec route table.
2. Use BluCode for reusable self-coding lessons.
3. Touch high-authority files only when the governing law/source itself is wrong or missing.
4. State why lower layers cannot solve the issue before editing high-authority files.
5. Preserve exact baseline copies when high-authority edits are unavoidable.

## Do Not

- Do not put implementation lessons into Instructions/Ops/Persona by default.
- Do not make a bug fix stick by adding more global law.
- Do not spend bootloader budget on patch-process memories.
- Do not modify high-authority files without explicit scope.

## Validation

- Patch diff shows no high-authority churn unless justified.
- Reusable coding lessons land in BluCode.
- Implementation behavior is fixed in the component that owns it.
- Bootloader size remains protected.

## Example

Bad: Add `/mood` legacy wording bans to Ops to fix Mood.

Good: Fix MoodService/MoodLib ownership and add a BluCode card preventing renderer-owner drift.
