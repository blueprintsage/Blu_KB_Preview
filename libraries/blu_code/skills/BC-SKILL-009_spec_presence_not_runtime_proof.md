# BC-SKILL-009 — Spec Presence Is Not Runtime Proof

## Trigger
Use whenever a correct-looking module, rule, registry entry, or test exists but live behavior is wrong.

## Failure Pattern
A component exists in the spec but is not actually reached or enforced.

## Do
1. Separate source truth from runtime proof.
2. Verify route order and owner binding.
3. Check whether the relevant function/gate is actually called.
4. Use observed output to locate the active path.
5. Treat registry presence as insufficient.

## Do Not
- Do not say “it’s fixed” because the module exists.
- Do not infer execution from architecture.
- Do not debug inside an unused function before proving it is reached.

## Validation
- Live output matches the claimed executing path.
- Trace or output proves the correct owner handled the turn.
- Unused competing paths are blocked.

## Example
Bad:
`M1004A exists, so /mood show is fixed.`

Good:
`/mood show` live output proves whether M1004A actually bound the route.
