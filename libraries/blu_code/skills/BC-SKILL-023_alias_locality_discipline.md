# BC-SKILL-023 — Alias Locality Discipline

## Trigger
Use when adding or modifying Library, Service, Program, or EchoTrace target aliases.

## Failure Pattern
Detached alias registries drift from local Component declarations. EchoTrace resolves stale aliases or the same alias is declared in multiple places.

## Do
1. Put the stable `alias` on the owning Component or Program block.
2. Resolve EchoTrace targets from local declarations.
3. Treat aliases as diagnostic handles only.
4. Keep slash command routing separate from alias resolution.
5. Reject duplicate or missing aliases for ACTIVE Components.

## Do Not
- Do not maintain detached Component Alias Registries.
- Do not maintain detached Program Alias Registries.
- Do not make aliases create slash commands.
- Do not let EchoTrace depend on stale registry residue.

## Validation
- Every ACTIVE Component has exactly one local alias.
- EchoTrace resolves aliases by scanning or consuming local declarations.
- No detached alias registry is required.
- Slash command rows still live only in Commands.

## Example
Bad: Add `program_aliases: [SimCode]` while `PROGRAM.SIMCODE.001` already has `alias: SimCode`.
Good: Keep `alias: SimCode` inside `PROGRAM.SIMCODE.001` and let EchoTrace resolve local declarations.