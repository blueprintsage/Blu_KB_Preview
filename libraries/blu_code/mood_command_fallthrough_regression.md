# Mood command fallthrough regression

Date: 2026-05-04
Affected area: `/mood` routes

## Verified symptoms

Observed outputs included:
- `mood: steady, warm, present`
- `mood: on`
- no visible mood line after `/mood on`

## Cause class

Those outputs indicate `/mood` was being handled as ordinary conversational/persona text instead of a deterministic Exec command route.

## Rule

Before rewriting MoodLib, RibbonLib, or swatch mapping, verify the route:
- `/mood on` must be intercepted as a command
- `/mood show` must not fall through to ordinary Persona response
- command confirmation shape must be exact
- only after route proof should render logic be changed

Do not fix render before route.
