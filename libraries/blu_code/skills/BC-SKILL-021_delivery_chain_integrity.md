# BC-SKILL-021 — Delivery Chain Integrity

## Trigger
Use when providing code blocks, full-file replacements, nested markdown, command specs, archives, manifests, or other patch handoff material.

## Failure Pattern
The architecture is correct, but the delivered patch is malformed, truncated, incorrectly fenced, or hard to copy. The user cannot safely apply the patch, leaving the kernel half-wired.

## Do
1. Treat formatting correctness as part of completion.
2. Use safe outer fences when embedding markdown that contains code fences.
3. Prefer full-file replacement when the user asks for a complete file.
4. Verify that copy-paste boundaries are unambiguous.
5. If delivery breaks, repair the delivery artifact directly instead of explaining around it.

## Do Not
- Do not nest triple backticks inside triple backticks.
- Do not provide partial fragments when the user needs a complete replacement.
- Do not collapse scope to “minimum changes” after the user has already started applying a fuller patch.
- Do not claim a patch is usable if the handoff format is broken.

## Validation
- The replacement can be copied without fence corruption.
- Internal code fences remain intact.
- The user receives the complete requested artifact or an explicit partial-state label.
- No required patch step is left implicit.

## Example
Bad: Deliver `05_Commands.md` in a broken markdown fence.
Good: Use a four-backtick outer fence or provide an archive/full-file artifact.