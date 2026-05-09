# BC-SKILL-025 — Kernel Session Overheat Checkpoint

## Trigger
Use when a kernel repair chat becomes long, laggy, emotionally heated, or contains many partial file states and cross-file patches.

## Failure Pattern
Long sessions accumulate hidden context drift, delivery mistakes, emotional escalation, and unclear source state. The patch chain becomes hard to trust even when the architecture is sound.

## Do
1. Stop patching when the session becomes unstable.
2. Produce a MemCap with exact current state, open blockers, and next files to upload.
3. Move to a fresh chat before continuing.
4. Resume with verification only before new patches.
5. Upload active source files rather than relying on memory.

## Do Not
- Do not keep patching through lag and frustration.
- Do not rely on stale chat context as source truth.
- Do not declare the kernel stable while wiring is incomplete.
- Do not continue after delivery-chain failures without checkpointing.

## Validation
- New chat starts from uploaded active files.
- First step is wiring verification, not patching.
- Remaining blockers are explicit.
- No claim depends on hidden prior chat state.

## Example
Bad: Continue wiring SimCode after Commands delivery broke and the chat is lagging.
Good: Produce a MemCap, upload `03_Exec.md`, `04_Exec_Library.md`, `05_Commands.md`, `06_Programs.md`, and `ERROR_MACROS_CATALOG.md` in a fresh chat.