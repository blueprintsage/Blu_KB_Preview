# BC-SKILL-022 — Program Wiring Completeness

## Trigger
Use when adding, restoring, or activating a Program such as SimCode, Memory, Mood, CPM, or other slash-command-owned Program behavior.

## Failure Pattern
A Program body exists, but command routing, lane class, scheduler permission, alias resolution, EchoTrace visibility, or Error_Macros are missing. The Program looks active in source but cannot run.

## Do
1. Add the Program body in `06_Programs.md`.
2. Add the Program to `active_programs`.
3. Add the command stem to `05_Commands.md::dispatch_matrix`.
4. Ensure the lane class exists in Exec.
5. Ensure Scheduler may dispatch the Program route.
6. Ensure EchoTrace can resolve the Program alias from the local Program block.
7. Add all Program ERROR_CODES to Error_Macros.
8. Test the route matrix before declaring the Program live.

## Do Not
- Do not treat Program presence as runtime activation.
- Do not update command help without a dispatch row.
- Do not use detached alias registries.
- Do not claim the Program is wired until route, owner, lane, scheduler, trace, and errors all align.

## Validation
- The slash stem resolves to the Program owner.
- The Program is listed in `active_programs`.
- The lane class exists.
- Scheduler can dispatch the selected owner.
- EchoTrace resolves the Program alias.
- Error_Macros contains all Program error codes.

## Example
Bad: Define `PROGRAM.SIMCODE.001` but leave `/simcode` in `not_live_in_boot_build`.
Good: Define `PROGRAM.SIMCODE.001`, activate it, add `/simcode` dispatch, add `sandbox` lane, and catalog SimCode errors.