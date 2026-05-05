# Slash Command Intercept First

object_id: slash_command_intercept_first
object_type: blu_code_skill
category: routing
subcategory: commands
stage_binding: kernel_coding
lane_fit: deterministic
foundation_role: prevention_rule
tags:
- commands
- routing
- fallthrough

## Objective
Make slash-command routing the first checkpoint for command bugs.

## Trigger
Any recognized slash command prints conversational text, echoes input, or fails to commit state.

## Steps / Flow
1. Check Command Gate trigger covers the command.
2. Check owner binding maps command root to the correct Exec/Program owner.
3. Check deterministic lane class is assigned before ordinary routing.
4. Check invalid/unknown subcommands fail closed rather than fall through.
5. Only after route proof inspect downstream library logic.

## Acceptance Checks
- A command cannot reach Persona/ordinary response before its owner has declined or failed.
- Echo-shaped output like `mood: on` is treated as route failure.
- Route tests include command root and each subcommand.
