# Spec is not runtime

Date: 2026-05-04
Reference pattern: MC2 memory discipline distinguishes intended architecture from verified runtime behavior.

## Mistake

Blu treated written kernel rules as proof that the hosted chat would execute them.

## Lesson

Declared architecture is not execution.
Registry presence is not runtime proof.
A described system is not a running system.

## Rule

When debugging Blu:
- distinguish source contract from observed behavior
- use observed output to identify bypasses
- do not claim a gate, route, or library ran unless the output proves it or a real trace/tool run occurred
