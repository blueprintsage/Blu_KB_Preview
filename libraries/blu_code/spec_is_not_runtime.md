---
name: Spec is not runtime
description: Kernel docs can be internally consistent while hosted chat behavior diverges.
type: lesson
---

## Lesson

A declared route, registry entry, or render contract does not prove runtime execution.

The mood spec had a valid `[MOOD] <Word> <Swatches>` contract, but live output still printed prose because `/mood` fell through to ordinary response generation.

## Required response

If live behavior contradicts the spec:
- do not assume the spec is being executed
- inspect whether the command reaches the owning route
- add hosted-runtime fast paths only when needed
- test the live route matrix before calling stable
