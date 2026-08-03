# Runtime Bridge Degradation Boundary

**Object ID:** PAT-CPP-runtime-bridge-degradation-boundary  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** architecture_design  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** cpp, runtime_bridge, legacy_bridge, data_migration, modding, diagnostics, strict_compile  

## Pattern Rule

**IF** a runtime bridge replaces a legacy data path, **THEN** allow legacy fallback only when the replacement catalog is absent, and keep loaded-but-incomplete catalogs loud, **ELSE** compatibility fallback hides real data loss.

## Use When

- Replacing a legacy DLL, binary table, resource file, or hardcoded table with a data-backed loader.
- Adding a modder-facing data layer while old runtime assets still exist.
- Preserving stock-install boot compatibility during staged migration.
- Building a bridge where tests must expose missing replacement records.

## Do

- Treat **absent replacement data** and **incomplete replacement data** as different states.
- Preserve legacy fallback only for the whole-catalog absent case when compatibility requires it.
- Emit loud missing markers, diagnostics, or validation errors for missing entries after the replacement catalog has loaded.
- Leave a breadcrumb diagnostic when falling back to the legacy path.
- Validate bridge code under strict compiler settings.
- Prefer reference-safe signatures at string/path seams.
- Route future file loads through the project file abstraction when archive, overlay, or mod precedence matters.

## Don't

- Do not silently fall back per missing entry after the replacement catalog has loaded.
- Do not treat a bridge proof as the final loader architecture.
- Do not rely on permissive compiler behavior at bridge seams.
- Do not hide incomplete replacement data behind legacy behavior.
- Do not mix compatibility fallback with data validation semantics.

## Checklist

- The bridge has an explicit absent-catalog path.
- The bridge has an explicit loaded-but-missing-entry path.
- Missing entries remain visible in test artifacts.
- The fallback rule is documented for stock installs.
- Strict compiler validation covers the bridge code.
- Path construction accepts the argument types actually passed by call sites.
- Future mod or overlay precedence has a documented loader seam.

## Example

```text
catalog absent or empty
→ fall back to legacy DLL/resource path
→ emit a breadcrumb diagnostic

catalog loaded, requested ID missing
→ return a loud missing marker
→ do not ask the legacy DLL/resource path for that one ID
```

## Bad Example

```text
catalog loaded, requested ID missing
→ silently ask the old legacy system
```

This makes tests pass while the replacement data is incomplete.

## Variant: Legacy Data Replacement

**IF** legacy data remains packaged for compatibility, **THEN** use it only as a whole-catalog fallback when replacement data is absent, **ELSE** use loud missing markers to expose incomplete migration records.

## Variant: Mod Overlay Loader

**IF** the replacement data is meant to be modder-facing, **THEN** route loads through the project file abstraction or overlay-aware loader, **ELSE** loose-file, archive, and mod precedence may diverge from the rest of the engine.

## Variant: Strict Toolchain Bridge

**IF** a bridge compiles under one permissive toolchain only, **THEN** tighten signatures and path/string APIs until it compiles under strict mode, **ELSE** the migration carries hidden portability debt.

## Reference

- Source: MC2R mc2res.dll FIT bridge Phase 1 integration feedback
- Evidence Type: implementation result
- Result: bridge landed with one MSVC `/permissive-` compile fix and a validated stock-install fallback rule
- Lesson: absent replacement data may degrade to legacy; loaded-but-incomplete replacement data must stay loud
