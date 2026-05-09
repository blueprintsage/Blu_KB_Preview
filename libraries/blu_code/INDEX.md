# BluCode Skill Cards Index

date: 2026-05-07
status: active
purpose: PASS-style coding skill cards for Blu kernel work after Exec RuntimeGate collapse.

## Use Rule

Before modifying Blu kernel code, consult the relevant BluCode skill cards.

When a bug is found:

1. identify the failure pattern
2. apply the matching skill card
3. validate with the listed tests
4. add a new card only when the lesson is reusable beyond one patch

BluCode is coding memory, not runtime source. It constrains patch discipline and self-coding behavior; active kernel source still controls implementation.

## Architecture Rule

Exec is the runtime spine only:

`RuntimeGate.Ingress -> Exec.Scheduler -> RuntimeGate.Egress`

Programs, services, and libraries are sandboxed packet machines:

`entry -> validate -> branch -> dependencies -> packet -> stop`

Every deterministic boundary must terminate as success, failure, or BLOCKED. No owner may print directly. No failed branch may fall through into ordinary completion.

## Skill Cards

### Runtime / Architecture

- [BC-SKILL-001 Runtime Spine Purity](skills/BC-SKILL-001_runtime_spine_purity.md)
- [BC-SKILL-002 Component Sandbox Contract](skills/BC-SKILL-002_component_sandbox_contract.md)
- [BC-SKILL-003 Branch Totality](skills/BC-SKILL-003_branch_totality.md)
- [BC-SKILL-004 Alias Lead Owner](skills/BC-SKILL-004_alias_lead_owner.md)

### Routing / Dispatch

- [BC-SKILL-005 Slash Command First-Read Lock](skills/BC-SKILL-005_slash_command_first_read_lock.md)
- [BC-SKILL-006 Dependency Chain Stop Rule](skills/BC-SKILL-006_dependency_chain_stop_rule.md)

### Ownership / Rendering

- [BC-SKILL-007 Renderer Owner Boundary](skills/BC-SKILL-007_renderer_owner_boundary.md)
- [BC-SKILL-008 EchoTrace / Diag Unification](skills/BC-SKILL-008_echotrace_diag_unification.md)

### Validation / Tests

- [BC-SKILL-009 Probe-First SimCode](skills/BC-SKILL-009_probe_first_simcode.md)
- [BC-SKILL-010 Live Route Matrix Required](skills/BC-SKILL-010_live_route_matrix_required.md)
- [BC-SKILL-014 Spec Presence Is Not Runtime Proof](skills/BC-SKILL-014_spec_presence_not_runtime_proof.md)

### Patch Discipline

- [BC-SKILL-011 High-Authority File Friction](skills/BC-SKILL-011_high_authority_file_friction.md)
- [BC-SKILL-012 Preserve Proven Baseline](skills/BC-SKILL-012_preserve_proven_baseline.md)
- [BC-SKILL-013 Full-File Replacement Discipline](skills/BC-SKILL-013_full_file_replacement_discipline.md)
- [BC-SKILL-015 Error Macro Fail-Closed](skills/BC-SKILL-015_error_macro_fail_closed.md)
- [BC-SKILL-016 Artifact Claim Proof](skills/BC-SKILL-016_artifact_claim_proof.md)
