# Command fallthrough regression
Date: 2026-05-04
Example area: `/mood` routes

## Verified symptoms
Observed outputs included:
- `mood: steady, warm, present`
- `mood: on`
- no visible mood line after `/mood on`

## Generalized cause class
If a slash command prints conversational or echo-shaped text like `<command>: <value>`, the command did not complete through its deterministic owner.

## Rule
Before rewriting downstream libraries, verify the route:
- command root is intercepted
- correct owner is selected
- state-setting command confirmation shape is exact
- read/render command does not fall through to ordinary Persona response
- only after route proof should payload/render logic be changed
