# BluCode Skill Cards Index

date: 2026-05-08
status: active
purpose: PASS-style coding skill cards for Blu kernel work.

## Use Rule

Before modifying Blu kernel code, consult the relevant BluCode skill cards.

When a bug is found:
1. identify the failure pattern
2. apply the matching skill card
3. validate with the listed tests
4. add a new card only when the lesson is reusable beyond one patch

BluCode is coding memory and patch discipline. It is not a runtime owner, public command, printer, or substitute for source binding.

## Skill Cards

### Routing / Dispatch
- [BC-SKILL-001 Slash Command First-Read Lock](skills/BC-SKILL-001_slash_command_first_read_lock.md)
- [BC-SKILL-002 Subcommand Dispatch Before Generic Handling](skills/BC-SKILL-002_subcommand_dispatch_before_generic.md)
- [BC-SKILL-003 Status-Readback Contamination Guard](skills/BC-SKILL-003_status_readback_contamination_guard.md)

### Ownership / Rendering
- [BC-SKILL-004 Single Renderer Ownership](skills/BC-SKILL-004_single_renderer_ownership.md)
- [BC-SKILL-005 Source-Only Boundary Enforcement](skills/BC-SKILL-005_source_only_boundary_enforcement.md)
- [BC-SKILL-006 Structured Support Payloads](skills/BC-SKILL-006_structured_support_payloads.md)
- [BC-SKILL-019 Exact Render Branch Discipline](skills/BC-SKILL-019_exact_render_branch_discipline.md)

### Validation / Tests
- [BC-SKILL-007 Negative Example Hygiene](skills/BC-SKILL-007_negative_example_hygiene.md)
- [BC-SKILL-008 Live Route Matrix Required](skills/BC-SKILL-008_live_route_matrix_required.md)
- [BC-SKILL-009 Spec Presence Is Not Runtime Proof](skills/BC-SKILL-009_spec_presence_not_runtime_proof.md)
- [BC-SKILL-015 Error Macro Catalog Law](skills/BC-SKILL-015_error_macro_catalog_law.md)

### Patch Discipline
- [BC-SKILL-010 Full-File Replacement Discipline](skills/BC-SKILL-010_full_file_replacement_discipline.md)
- [BC-SKILL-011 One-Seam Fix Discipline](skills/BC-SKILL-011_one_seam_fix_discipline.md)
- [BC-SKILL-012 Backup Before Mutation](skills/BC-SKILL-012_backup_before_mutation.md)
- [BC-SKILL-016 Source Binding Before Patch or Build](skills/BC-SKILL-016_source_binding_before_patch_build.md)
- [BC-SKILL-020 Mandatory Changelog for Kernel Archives](skills/BC-SKILL-020_mandatory_changelog_kernel_archives.md)

### Containment / Safety
- [BC-SKILL-017 DeliveryShape Source Markdown Lock](skills/BC-SKILL-017_deliveryshape_source_markdown_lock.md)
- [BC-SKILL-018 OPSEC First-Read Hardwall](skills/BC-SKILL-018_opsec_first_read_hardwall.md)
