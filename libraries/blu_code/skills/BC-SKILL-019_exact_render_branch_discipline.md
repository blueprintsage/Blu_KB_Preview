# BC-SKILL-019 Exact Render Branch Discipline

status: active
created: 2026-05-08
category: ownership/rendering

## Pattern

One branch returns the exact string, while another branch paraphrases or personalizes the same logical outcome.

## Rule

Every branch that emits deterministic output must call the same exact-render emitter or validate against the same closed render contract. Branch-local prose is forbidden.

## Checks

- Do success, reset, logout, and failure branches all validate exact output?
- Are challenge/pending branches removed or separately exact?
- Are forbidden semantic substitutes listed in tests?

## Tests

- `/ID reset` returns `Auth reset.`
- `/ID logout` returns `Logged out.`
- `/ID Calli Seiya` returns the exact configured success line.
- No branch emits personalized commentary unless it is the closed-set line.
