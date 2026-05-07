# BC-SKILL-004 — Alias Lead Owner

## Trigger

Use when adding `/echotrace {ALIAS}`, route aliases, chain diagnostics, or owner maps.

## Failure Pattern

Every internal helper gets a public alias, or the wrong helper becomes the apparent owner of a user-facing request.

## Do

1. Assign public aliases only to request-to-print chain leaders.
2. Keep internal dependencies visible inside the parent trace, not as public aliases unless independently routable.
3. Bind each alias to exactly one lead owner.
4. Show dependency steps under the lead alias trace.

## Do Not

- Do not give every library a public alias.
- Do not let an internal dependency claim the chain's terminal packet.
- Do not let aliases bypass auth, route lock, or Egress.
- Do not use source/static trace as live runtime proof.

## Validation

- `/echotrace Mood` traces the full Mood chain, including RibbonLib and PersonaLib as internal steps.
- `RibbonLib` and `PersonaLib` are not public aliases unless they become direct request owners.
- Alias resolution reports one lead owner and one terminal packet path.
- Unknown aliases fail closed.

## Example

Bad: `/echotrace RibbonLib` is public even though RibbonLib only supports Mood.

Good: `/echotrace Mood` shows `RibbonLib -> MoodLib -> SERVICE.MOOD.001 -> Egress`.
