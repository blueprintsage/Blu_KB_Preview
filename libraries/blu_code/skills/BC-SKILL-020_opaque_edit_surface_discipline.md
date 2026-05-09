# BC-SKILL-020 — Opaque Edit Surface Discipline

## Trigger
Use when modifying Blu kernel files, command files, ExecLibs, Programs, Error_Macros, repo indexes, archives, or other deterministic runtime surfaces.

## Failure Pattern
Canvas, hidden document state, partial patch tools, or broad rewrite surfaces cause the active file state to diverge from the expected patch state. The model believes a mutation happened cleanly, while the user is left with unclear or broken source.

## Do
1. Prefer raw markdown, explicit diffs, full-file replacements, or archive outputs for kernel work.
2. Use visible source text when exact placement matters.
3. Preserve delivery shape for requested file replacements.
4. Treat hidden or opaque edit state as untrusted until verified.
5. If patch placement fails, stop and return to explicit raw text or full-file replacement.

## Do Not
- Do not use canvas for kernel work unless the user explicitly requests it.
- Do not assume a hidden document patch succeeded.
- Do not continue patching after document state becomes ambiguous.
- Do not mix opaque edit surfaces with phase-gated kernel repair.

## Validation
- The user can see or download the exact changed source.
- The patch target and changed lines are auditable.
- No hidden document state is required to reconstruct the patch.
- The final artifact can be reloaded and verified.

## Example
Bad: Patch `05_Commands.md` through canvas during active kernel wiring.
Good: Provide a raw full-file replacement or explicit diff for `05_Commands.md`.