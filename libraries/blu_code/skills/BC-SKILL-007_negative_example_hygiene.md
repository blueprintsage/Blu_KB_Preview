# BC-SKILL-007 — Negative Example Hygiene

## Trigger
Use when writing validation rules, tests, or forbidden-output examples in prompt-executed specs.

## Failure Pattern
Forbidden examples become output anchors because the model sees them repeatedly.

## Do
1. Keep negative examples minimal.
2. Prefer abstract pattern descriptions when possible.
3. Pair any negative example with a clear positive canonical output.
4. Avoid repeating bad literal strings across many sections.
5. Use named error labels instead of full bad outputs when feasible.

## Do Not
- Do not saturate specs with the exact wrong output.
- Do not include decorative wrong examples unless necessary.
- Do not let tests teach the model a bad phrase as normal output.

## Validation
- Bad examples appear only where needed.
- Positive canonical form is more prominent than bad form.
- Live output does not copy forbidden examples.

## Example
Bad:
Repeating `Mood: steady...` throughout multiple modules.

Good:
Define `legacy mood-prefix output` once, then enforce `[MOOD] <Word> <Swatches>`.
