# Probe-First Deterministic Development

## Object Type
pattern

## Category
coding

## Subcategory
testing_validation

## Stage Binding
2 block

## Lane Fit
skill

## Foundation Role
foundation

## Tags
- deterministic_runtime
- testing
- validation
- probes
- diagnostics
- simcode
- contract_testing
- regression_guard

## Cross Links
- related_to: skills/coding/testing_validation/
- related_to: skills/coding/testing_validation/patterns/
- supports: skills/coding/
- supports: skills/coding/tooling_environment/

## Pattern Rule

**IF** adding or modifying a deterministic Program, ExecLib, service, command renderer, artifact route, export route, or pipeline handoff, **THEN** ship a minimal probe pack with the change before calling it complete, **ELSE** a green unit path may hide a broken live path.

## Do

- Add probes at the same time as the deterministic capability.
- Probe the smallest callable contract first.
- Add at least one live or pipeline handoff probe when multiple layers exchange state.
- Add a public render-shape probe for user-visible deterministic output.
- Add forbidden-output checks for known legacy, prose, or fallback formats.
- Add an error-path probe for expected failures.
- Keep probes narrow enough to identify the failing boundary.
- Report PASS, FAIL, BLOCKED, and SKIPPED distinctly.
- Include a failure explanation that names the observed boundary and the next patch target.
- Re-run the probe board after every patch that touches the lane.

## Don't

- Do not treat a passing unit probe as proof that the live pipeline is green.
- Do not patch before tracing the failing boundary when a probe can expose it.
- Do not let a Program, ExecLib, service, or renderer print directly to bypass terminal validation.
- Do not replace exact terminal-contract checks with conversational summaries.
- Do not hide a BLOCKED diagnostic as a PASS.
- Do not claim an artifact, export, rollback, or state mutation worked without proof.
- Do not add broad brittle probes when a smaller boundary probe would isolate the fault.

## Checklist

- Does every new deterministic entrypoint have at least one contract probe?
- Does every multi-layer workflow have a pipeline or handoff probe?
- Does every public renderer have a shape-regression probe?
- Does every artifact route verify file existence and expected contents?
- Does every failure mode return a terminal-valid failure packet?
- Does every probe explain what failed and where to patch next?
- Are forbidden legacy formats explicitly checked?
- Is the probe pack included in the same patch/archive as the feature?
- Can probes be chained without result bleed between commands?
- Is rollback or checkpoint behavior tested before trusting it?

## Probe Pack Minimums

### ExecLib / Library

- contract probe for each primary entrypoint
- invalid-input probe
- forbidden-output probe
- boundary-preservation probe when returning structured fields

### Program

- route probe
- auth probe when gated
- success terminal-packet probe
- failure terminal-packet probe
- dependency-result probe when ExecLib or service calls are required

### Service / Pipeline

- handoff probe for every state boundary
- live-snapshot probe when runtime state is involved
- BLOCKED result when instrumentation is missing

### Renderer

- public shape-regression probe
- forbidden legacy-format probe
- exact-output probe for command confirmations
- no-prose-fallback probe for deterministic lanes

### Artifact / Export Route

- archive/file existence probe
- required-file manifest probe
- checksum or integrity probe when practical
- link-proof probe before claiming creation/export
- OPSEC/redaction probe when sensitive context may be packaged

### Patch System

- load probe
- chain probe
- chain --continue probe
- rollback or checkpoint probe
- patch manifest validation probe

## Variants

### Variant: Live Pipeline Debugging

**IF** isolated probes pass but the observed runtime output remains wrong, **THEN** add a live pipeline probe that records each handoff field in order, **ELSE** do not assume the fault is in the last layer that printed the bad output.

### Variant: Renderer Regression

**IF** a legacy user-visible format reappears, **THEN** add a render probe that forbids the legacy prefix, separators, prose chain, or stale phrase, **ELSE** shape drift can return silently.

### Variant: Artifact Claim

**IF** a route says it created, exported, loaded, or packaged an artifact, **THEN** verify the linked artifact exists and contains the expected files, **ELSE** the route is only a narrative claim.

### Variant: BLOCKED Diagnostic

**IF** a probe cannot inspect the needed field because instrumentation is missing, **THEN** return BLOCKED with the exact missing fields and next instrumentation target, **ELSE** the diagnostic result is ambiguous.

## Notes

This pattern was extracted from the Blu SimCode debugging session where the mood system looked green under isolated probes but failed in a live render path. The successful method was: trace the boundary, add contract probes, add live handoff probes, patch only the proven collapse point, then rerun the board.

Useful operating phrase:

> Unit green is not runtime green. Runtime green is not deploy green.

## Reference

- Source: Blu SimCode debugging session
- Date: 2026-05-06
- Evidence Type: user-observed runtime behavior and generated probe results
