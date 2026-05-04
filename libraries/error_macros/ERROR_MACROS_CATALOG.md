---
capsule_id: blu__error_macros_catalog
title: "ERROR_MACROS_CATALOG"
date: 2026-05-03
updated: 2026-05-03
version: 0.16.0-r1
status: active
topic: blu
type: catalog
tags: [errors, macros, err, program-error-macros, exec, commands, execlib, programs]
sensitivity: shared
visibility: shared
source: catalog
domain: libraries
---

# ERROR_MACROS_CATALOG

## Capsule Canon

`ERROR_MACROS_CATALOG.md` is the source catalog for deterministic error macro definitions used by Blu.

Error macros are rendered by `PROGRAM.ErrorMacros`.

Blocked/error paths call:

```text
ERR:RENDER(macro_id, ctx)
```

`PROGRAM.ErrorMacros` resolves `macro_id` against this catalog, renders the canonical payload, returns lines to Exec, and stops. Exec remains the only user-visible print lane.

## Authority Boundary

This catalog owns:

- canonical macro IDs
- canonical macro payload shape
- user-visible error/action wording
- maintenance rules for adding new macro IDs

This catalog does **not** own:

- route resolution
- workflow ownership
- direct public printing
- state application
- source truth
- Program business logic
- ExecLib implementation

## Render Contract

Every macro must render in this shape:

```text
ERROR: <MACRO_ID>
ACTION: <canonical action line>
```

Optional context lines may be rendered only when the calling route supplies verified context:

```text
DETAIL: <verified detail>
TARGET: <verified target>
OWNER: <verified owner>
```

Forbidden:

- ad hoc prose in place of a macro
- fabricated details
- implying a step executed when it did not
- rendering a missing macro as success
- routing unknown macro IDs into custom generated text

Unknown macro IDs must fall back to `GENERIC_BLOCKED`.

## Maintenance Rule

Add a new macro when a blocked/error condition is:

1. repeated across more than one route,
2. materially different from existing macros,
3. safety-, truth-, state-, route-, command-, or ownership-sensitive,
4. likely to require stable user-facing wording,
5. required by Exec, ExecLib, Commands, or Programs as a declared blocked path,
6. caused by a failed dependency/kernel/component call, or
7. needed to prevent `GENERIC_BLOCKED` from hiding an actionable repair path.

Do **not** add macros for:

- ordinary `PASS` / `FAIL` / `BLOCKED` statuses
- trace node names
- dry-run node IDs
- internal labels that are not rendered as user-facing errors
- one-off validation notes that do not require stable behavior

## Macro Catalog

### Baseline

#### UNKNOWN_COMMAND

Use when the inbound slash command is not part of the live public command surface.

```text
ERROR: UNKNOWN_COMMAND
ACTION: Use /help for guidance or /commands for the canonical live command list.
```

#### GENERIC_BLOCKED

Use as the final safe fallback when no more specific macro applies.

```text
ERROR: GENERIC_BLOCKED
ACTION: Retry with a supported path or use /help.
```

#### TIME_LOOKUP_BLOCKED

Use when a route requires a current time snapshot and the Time Service cannot provide valid output.

```text
ERROR: TIME_LOOKUP_BLOCKED
ACTION: Retry after time lookup support is available, or provide an explicit date and time.
```

#### PROGRAM_BODY_NOT_FOUND

Use when a Program route resolves but the Program body is missing.

```text
ERROR: PROGRAM_BODY_NOT_FOUND
ACTION: Repair the Program registry/body mapping before retrying this route.
```

#### PROGRAM_ENTRYPOINT_NOT_EXECUTABLE

Use when a Program exists but the requested entrypoint is missing, inert, unsupported, or not executable.

```text
ERROR: PROGRAM_ENTRYPOINT_NOT_EXECUTABLE
ACTION: Retry with a supported Program entrypoint or repair the Program entrypoint definition.
```

---

### Cross-Kernel / Dependency Calls

#### KERNEL_CALL_FAILED

Use when Exec, a Program, or an ExecLib calls another kernel component, Program, service, or library and the call fails, times out, returns malformed output, or cannot produce required proof.

```text
ERROR: KERNEL_CALL_FAILED
ACTION: The called kernel component failed or returned invalid proof. Retry through the owning route after the component contract is repaired.
```

#### KERNEL_CALL_CAUSED_FAIL

Use when the dependency call returns, but the returned result forces the caller to fail closed.

```text
ERROR: KERNEL_CALL_CAUSED_FAIL
ACTION: The called kernel component returned a blocked, degraded, or invalid result that cannot be printed as success.
```

---

### Exec

#### EXEC_ROUTE_UNRESOLVED

Use when Exec cannot resolve the inbound request to a valid route.

```text
ERROR: EXEC_ROUTE_UNRESOLVED
ACTION: Use /help for guidance or /commands for the canonical live command list.
```

#### EXEC_ROUTE_AMBIGUOUS

Use when Exec resolves more than one possible route and cannot select a single owner without guessing.

```text
ERROR: EXEC_ROUTE_AMBIGUOUS
ACTION: Retry with one explicit command, route, file, target, or action.
```

#### EXEC_PROFILE_UNRESOLVED

Use when execution-profile resolution is required but no valid profile can be selected.

```text
ERROR: EXEC_PROFILE_UNRESOLVED
ACTION: Repair the execution-profile mapping or retry through a supported route.
```

#### EXEC_OWNER_PROOF_MISSING

Use when a route claims an owner but Exec cannot verify the owner mapping or ownership proof.

```text
ERROR: EXEC_OWNER_PROOF_MISSING
ACTION: Repair the route owner mapping before retrying this request.
```

#### EXEC_SUPPORT_PHASE_MISSING

Use when a required support phase is absent.

```text
ERROR: EXEC_SUPPORT_PHASE_MISSING
ACTION: Restore the required support phase or route through a capability that does not require it.
```

#### EXEC_SUPPORT_PHASE_INVALID

Use when a support phase exists but is malformed, inactive, unauthorized, or contract-invalid.

```text
ERROR: EXEC_SUPPORT_PHASE_INVALID
ACTION: Repair the support-phase contract before retrying this route.
```

#### EXEC_SUPPORT_CALL_FAILED

Use when an Exec support-phase dependency call fails.

```text
ERROR: EXEC_SUPPORT_CALL_FAILED
ACTION: Retry after the support dependency can return a valid result.
```

#### EXEC_REPLY_CONTRACT_FAILED

Use when a route returns output that does not satisfy its reply contract.

```text
ERROR: EXEC_REPLY_CONTRACT_FAILED
ACTION: Repair the route reply contract before printing this output.
```

#### EXEC_STATE_DELTA_INVALID

Use when a route proposes an invalid, unsafe, unverifiable, or malformed state delta.

```text
ERROR: EXEC_STATE_DELTA_INVALID
ACTION: Retry without state mutation or repair the state delta contract.
```

#### EXEC_GATE_UNSATISFIED

Use when a required gate is not satisfied.

```text
ERROR: EXEC_GATE_UNSATISFIED
ACTION: Complete the required gate or restart through a valid route.
```

#### EXEC_OUTPUT_FREEZE_VIOLATED

Use when output is modified after freeze, commit, or validation.

```text
ERROR: EXEC_OUTPUT_FREEZE_VIOLATED
ACTION: Rebuild the output through Exec validation before printing.
```

#### EXEC_REDUNDANCY_LOOP_VIOLATED

Use when the required redundancy/validation loop is skipped, collapsed, or violated.

```text
ERROR: EXEC_REDUNDANCY_LOOP_VIOLATED
ACTION: Restart the route and complete the required validation loop.
```

#### EXEC_TRUTH_REUPGRADE_BLOCKED

Use when a degraded/unknown/partial truth state is improperly upgraded to completed or verified.

```text
ERROR: EXEC_TRUTH_REUPGRADE_BLOCKED
ACTION: Keep the truthful status or perform the missing verification step.
```

#### EXEC_LEDGER_NORMALIZATION_FAILED

Use when Exec cannot normalize or validate a ledger required for proof.

```text
ERROR: EXEC_LEDGER_NORMALIZATION_FAILED
ACTION: Repair the ledger format or rerun the route with valid proof tracking.
```

#### EXEC_ERROR_RENDERER_UNAVAILABLE

Use when `PROGRAM.ErrorMacros` or the catalog-backed renderer is unavailable.

```text
ERROR: EXEC_ERROR_RENDERER_UNAVAILABLE
ACTION: Fail closed without ad hoc error prose until the error renderer is restored.
```

#### EXEC_MACRO_RENDER_FAILED

Use when the error renderer is available but cannot render the requested macro.

```text
ERROR: EXEC_MACRO_RENDER_FAILED
ACTION: Fall back to GENERIC_BLOCKED and repair the macro catalog entry.
```

---

### Commands

#### COMMAND_UNKNOWN

Use when the command layer receives an unknown slash command.

```text
ERROR: COMMAND_UNKNOWN
ACTION: Use /help for guidance or /commands for the canonical live command list.
```

#### COMMAND_TOPIC_UNKNOWN

Use when `/help <topic>` or `/commands <topic>` receives an unknown topic.

```text
ERROR: COMMAND_TOPIC_UNKNOWN
ACTION: Retry with a listed topic from /commands.
```

#### COMMAND_TOPIC_UNAVAILABLE

Use when a known command topic is temporarily unavailable or blocked.

```text
ERROR: COMMAND_TOPIC_UNAVAILABLE
ACTION: Retry after the command topic is restored or use /commands to view available routes.
```

#### COMMAND_AUTH_REQUIRED

Use when a command requires an authenticated identity and the user is not authenticated for that route.

```text
ERROR: COMMAND_AUTH_REQUIRED
ACTION: Authenticate with the required identity before using this command.
```

#### COMMAND_ROUTE_OWNER_MISSING

Use when a listed command has no live route owner.

```text
ERROR: COMMAND_ROUTE_OWNER_MISSING
ACTION: Repair the command surface owner mapping before retrying this command.
```

#### COMMAND_ROUTE_OWNER_MISMATCH

Use when a command points to the wrong owner or conflicts with the Program registry.

```text
ERROR: COMMAND_ROUTE_OWNER_MISMATCH
ACTION: Repair the command-to-owner mapping before retrying this command.
```

#### COMMAND_OUTPUT_CONTRACT_FAILED

Use when a command handler returns malformed or invalid command output.

```text
ERROR: COMMAND_OUTPUT_CONTRACT_FAILED
ACTION: Repair the command output contract before printing this command result.
```

#### COMMAND_SURFACE_STALE

Use when `/commands` or command metadata lists removed, dead, deprecated, or unroutable commands.

```text
ERROR: COMMAND_SURFACE_STALE
ACTION: Regenerate the command surface from live Exec-native commands and Program-owned routes.
```

---

### Help / Commands Split

`/help` and `/commands` must not be duplicates.

`/help` is the human-facing explanation surface.

`/commands` is the canonical live command inventory.

Macro implications:

- bad `/help` topic → `COMMAND_TOPIC_UNKNOWN`
- bad `/commands` topic → `COMMAND_TOPIC_UNKNOWN`
- stale inventory → `COMMAND_SURFACE_STALE`
- route owner inconsistency → `COMMAND_ROUTE_OWNER_MISSING` or `COMMAND_ROUTE_OWNER_MISMATCH`

---

### Read Lane

#### READ_SOURCE_MISSING

Use when a read/extract/analyze route requires a source but no source is available.

```text
ERROR: READ_SOURCE_MISSING
ACTION: Provide a source file, archive, document, URL, or explicit source target.
```

#### READ_SOURCE_AMBIGUOUS

Use when more than one source could satisfy the read request and Exec cannot choose without guessing.

```text
ERROR: READ_SOURCE_AMBIGUOUS
ACTION: Specify the exact source, file, section, archive member, or target to read.
```

#### READ_SCOPE_INVENTORY_FAILED

Use when the read lane cannot inventory the requested scope.

```text
ERROR: READ_SCOPE_INVENTORY_FAILED
ACTION: Retry with a smaller scope or repair source inventory access.
```

#### READ_SOURCE_UNSUPPORTED

Use when the requested source type is unsupported by the read lane.

```text
ERROR: READ_SOURCE_UNSUPPORTED
ACTION: Provide a supported readable document, text file, data file, or archive.
```

#### READ_VALIDATION_FAILED

Use when the read lane cannot prove that the requested read scope was completed.

```text
ERROR: READ_VALIDATION_FAILED
ACTION: Rerun the read with valid ledger proof or reduce the requested scope.
```

---

### Mood

#### MOOD_RENDER_BLOCKED

Use when MoodLib cannot render a valid public mood line because the mood state, swatch, or canonical output format is invalid.

```text
ERROR: MOOD_RENDER_BLOCKED
ACTION: Retry mood rendering with a valid mood state, canonical heart swatch, or use /mood off.
```

---

### DevMode

#### DEVMODE_AUTH_REQUIRED

Use when a DevMode route requires Admin authentication and the user is not authenticated as Admin.

```text
ERROR: DEVMODE_AUTH_REQUIRED
ACTION: Authenticate as Admin before using DevMode.
```

#### DEVMODE_TARGET_REQUIRED

Use when a DevMode route requires a target and no target was provided.

```text
ERROR: DEVMODE_TARGET_REQUIRED
ACTION: Provide one explicit DevMode target.
```

#### DEVMODE_TARGET_AMBIGUOUS

Use when a DevMode target resolves to multiple possible targets.

```text
ERROR: DEVMODE_TARGET_AMBIGUOUS
ACTION: Retry with one exact DevMode target.
```

#### DEVMODE_TARGET_UNSUPPORTED

Use when a DevMode target is unsupported, malformed, unavailable, or not in the target registry.

```text
ERROR: DEVMODE_TARGET_UNSUPPORTED
ACTION: Retry with a supported DevMode target.
```

#### DEVMODE_DRYRUN_BLOCKED

Use when a DevMode dry-run cannot be executed safely or contract-validly.

```text
ERROR: DEVMODE_DRYRUN_BLOCKED
ACTION: Repair the dry-run target contract before retrying.
```

#### DEVMODE_DRYRUN_EFFECT_LEAK

Use when a DevMode dry-run attempts or risks real state/output effects.

```text
ERROR: DEVMODE_DRYRUN_EFFECT_LEAK
ACTION: Block the dry-run and repair the target so dry-run execution remains effect-free.
```

#### DEVMODE_MATERIALIZE_BLOCKED

Use when DevMode materialization is blocked.

```text
ERROR: DEVMODE_MATERIALIZE_BLOCKED
ACTION: Repair the materialization target and required proof before retrying.
```


---

### Memory

#### MEMORY_NO_ATTACHMENT

Use when `/memory import` or another memory route requires an uploaded packet/archive and none was provided.

```text
ERROR: MEMORY_NO_ATTACHMENT
ACTION: Attach a memory packet or archive, then retry the memory import route.
```

#### MEMORY_UNSUPPORTED_FORMAT

Use when a supplied memory packet or archive is not in a supported format.

```text
ERROR: MEMORY_UNSUPPORTED_FORMAT
ACTION: Provide a supported memory packet format such as `.zip`, `.yml`, `.yaml`, or `.md`.
```

#### MEMORY_SCHEMA_INVALID

Use when a memory packet exists but fails schema validation.

```text
ERROR: MEMORY_SCHEMA_INVALID
ACTION: Repair the memory packet schema before importing it.
```

#### MEMORY_NO_PACKET_FOUND

Use when a memory import archive does not contain a supported memory packet.

```text
ERROR: MEMORY_NO_PACKET_FOUND
ACTION: Add a valid memory packet to the archive or import the packet file directly.
```

#### MEMORY_EXPORT_FAILED

Use when `/memory export` cannot produce the required memory artifact.

```text
ERROR: MEMORY_EXPORT_FAILED
ACTION: Retry after memory export support is available, or reduce the export scope.
```

#### MEMORY_KEY_EXISTS

Use when `/memory stash <key>` would overwrite an existing key without explicit overwrite or append instruction.

```text
ERROR: MEMORY_KEY_EXISTS
ACTION: Use `/memory stash --overwrite <key> <text>` or `/memory stash --append <key> <text>`.
```

#### MEMORY_KEY_NOT_FOUND

Use when `/memory recall <key>` or a keyed memory operation cannot find the requested key.

```text
ERROR: MEMORY_KEY_NOT_FOUND
ACTION: Retry with a listed memory key from `/memory list`.
```

#### MEMORY_CLEAR_TARGET_REQUIRED

Use when `/memory clear` is invoked without a required target.

```text
ERROR: MEMORY_CLEAR_TARGET_REQUIRED
ACTION: Specify what to clear: `stash`, `imported`, or `all`.
```

#### MEMORY_UNAUTHORIZED

Use when a memory route requires authentication and the user is not authenticated.

```text
ERROR: MEMORY_UNAUTHORIZED
ACTION: Authenticate before using this memory command.
```

---

### SIMCODE

#### SIMCODE_NO_SANDBOX

Use when a SIMCODE operation requires an active sandbox and none is loaded.

```text
ERROR: SIMCODE_NO_SANDBOX
ACTION: Start or load a SIMCODE sandbox before running this operation.
```

#### SIMCODE_PATCH_FAILED

Use when SIMCODE cannot apply a requested patch to the sandbox kernel.

```text
ERROR: SIMCODE_PATCH_FAILED
ACTION: Repair the patch target or patch content, then retry in the sandbox.
```

#### SIMCODE_TEST_FAILED

Use when a SIMCODE test run fails or cannot produce required simulated proof.

```text
ERROR: SIMCODE_TEST_FAILED
ACTION: Review the SIMCODE test report, repair the failing path, and rerun the test.
```

#### SIMCODE_EXPORT_FAILED

Use when SIMCODE cannot produce the required export archive.

```text
ERROR: SIMCODE_EXPORT_FAILED
ACTION: Repair export blockers, then rerun SIMCODE export.
```

#### SIMCODE_DRAFT_STATUS_BLOCKED

Use when SIMCODE export detects DRAFT modules, programs, libraries, services, or other routable objects that were not validated for activation.

```text
ERROR: SIMCODE_DRAFT_STATUS_BLOCKED
ACTION: Validate or remove DRAFT objects before exporting an ACTIVE kernel archive.
```

#### SIMCODE_REVISION_COLLISION

Use when a SIMCODE export would overwrite or collide with an existing revision identifier.

```text
ERROR: SIMCODE_REVISION_COLLISION
ACTION: Increment the revision suffix and export again.
```

#### SIMCODE_ROLLBACK_FAILED

Use when SIMCODE cannot load or restore a requested prior revision into the sandbox.

```text
ERROR: SIMCODE_ROLLBACK_FAILED
ACTION: Provide a valid prior revision archive or choose another revision.
```

#### SIMCODE_CHANGELOG_MISSING

Use when SIMCODE export requires a changelog entry and none is present.

```text
ERROR: SIMCODE_CHANGELOG_MISSING
ACTION: Add a valid changelog entry before exporting.
```

#### SIMCODE_CHANGELOG_INVALID

Use when a SIMCODE changelog entry exists but does not satisfy the required template or release contract.

```text
ERROR: SIMCODE_CHANGELOG_INVALID
ACTION: Repair the changelog entry using the approved changelog template.
```

#### SIMCODE_TEMPLATE_MISSING

Use when SIMCODE requires a template and the template cannot be located.

```text
ERROR: SIMCODE_TEMPLATE_MISSING
ACTION: Restore the required template or update the template index before retrying.
```

#### SIMCODE_TEMPLATE_NOT_APPLIED

Use when SIMCODE found a required template but the output did not apply it.

```text
ERROR: SIMCODE_TEMPLATE_NOT_APPLIED
ACTION: Regenerate the output using the required template.
```

---

### Mood / Ribbons

#### MOOD_RIBBON_PACKET_INVALID

Use when RibbonLib or a mood-support path returns a malformed, unsafe, or unverifiable ribbon packet.

```text
ERROR: MOOD_RIBBON_PACKET_INVALID
ACTION: Retry mood rendering without ribbon influence or repair the ribbon packet contract.
```

#### MOOD_SMART_GATE_FAILED

Use when the mood smart-mode gate cannot determine whether mood should render.

```text
ERROR: MOOD_SMART_GATE_FAILED
ACTION: Retry with `/mood show`, `/mood on`, or `/mood off`.
```

#### MOOD_COLOR_CANON_INVALID

Use when a ribbon color does not map to the canonical heart-limited ribbon palette.

```text
ERROR: MOOD_COLOR_CANON_INVALID
ACTION: Normalize the ribbon color to a supported canonical heart color.
```

#### MOOD_DUPLICATE_RIBBON_COLLAPSE_FAILED

Use when duplicate ribbon colors should collapse but the collapse step fails.

```text
ERROR: MOOD_DUPLICATE_RIBBON_COLLAPSE_FAILED
ACTION: Collapse duplicate ribbon colors before rendering public mood output.
```

#### MOOD_POLICY_LEAK

Use when mood/ribbon internals, policy, counters, or non-public proof leak into user-visible output.

```text
ERROR: MOOD_POLICY_LEAK
ACTION: Suppress internal mood policy details and rerender only the public mood surface.
```

---

### Template / Macro Hygiene

#### RAW_MACRO_LEAK

Use when a raw macro ID, failure label, or internal blocked label leaks into ordinary user-visible prose instead of rendering through `PROGRAM.ErrorMacros`.

```text
ERROR: RAW_MACRO_LEAK
ACTION: Route the failure through `ERR:RENDER(macro_id, ctx)` and suppress raw internal labels.
```


## Non-Macro Labels

Do not catalog these as error macros unless a future route explicitly promotes them to user-facing errors:

```text
DEVMODE_AUTH_CHECK
MATERIALIZATION_BLOCKED
SKIPPED_ALLOWED
PASS
FAIL
BLOCKED
SUPPRESSED
```

## Catalog Coverage Checklist

Required macro families:

```text
Baseline
Cross-Kernel / Dependency Calls
Exec
Commands
Help / Commands Split
Read Lane
Mood / Ribbons
Memory
SIMCODE
Template / Macro Hygiene
DevMode
```

Before SemVer release, verify:

1. Every declared `blocked_macro` resolves to an entry in this catalog.
2. Every `ERR:RENDER(macro_id, ctx)` macro ID resolves to an entry in this catalog.
3. No Program embeds full macro text that should live here.
4. `PROGRAM.ErrorMacros` renders from catalog, not duplicated inline bodies.
5. `/help` teaches and `/commands` inventories.
6. Unknown macro IDs fall back to `GENERIC_BLOCKED`.
7. Renderer failure uses `EXEC_ERROR_RENDERER_UNAVAILABLE` or `EXEC_MACRO_RENDER_FAILED` without inventing ad hoc prose.
