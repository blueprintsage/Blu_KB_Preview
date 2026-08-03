# PASS - SkillForge Library Contract

status: active
owner: docs/PASS/PASS_LIBRARY.md
last_reviewed: 2026-07-30
superseded_by:
notes: Defines the generated library tree and the package contract consumed by SkillForge.

## Purpose

The library is both a human-browsable skill tree and a set of independently
installable SkillForge packages. This contract defines navigation and loading;
`PASS_SCHEMA.md` remains the source of truth for object shape.

## Placement and packages

Every object owns its location through `library_path`.

```yaml
library_path: [art, drawing, figure-construction]
```

The first segment is the package. Later segments are nested topics. Therefore:

```text
library/art/drawing/figure-construction/
```

is the `art` package, with `drawing` and `figure-construction` as its internal
navigation path. A package may have any number of topic levels after its first
segment; no empty level is invented to satisfy a fixed taxonomy.

## Universal foundation structure

Every package uses the same semantic structure, even though its craft topics
differ. `foundation_role`, `specialization_axis`, `foundation_object_id`, and
`variants` say whether an object is a portable foundation, a method alternative,
or a specialized route. Tags carry cross-cutting retrieval context.

`library_path` may make those relationships easier to browse when a package has
enough material to justify it. For example:

```text
software_development/foundations/error_handling/
software_development/languages/python/error_handling/
art/drawing/foundations/figure_construction/
art/drawing/domains/mechanical_figures/vehicle_construction/
writing/foundations/revision/
writing/domains/resume_writing/achievement_bullets/
```

These are navigation choices, not new object types or a required rigid depth.
The Python, mechanical-figure, and resume routes are discoverable because their
cards remain linked to their foundations and tagged with their contexts. A source
or school name is never, by itself, a path branch; `manga`, `comics`, and life
drawing may be tags, variants, or genuine specializations only when the learner
decision warrants it.

## Bootstrap and loading order

Every SkillForge installation contains the `metaskills` package. Before routing
or loading an optional skill package, SkillForge loads:

```text
AP_plan_and_build_work_from_thumbnail_to_final
```

This is the universal Step 0 plus Skeleton, Block, Rough, and Final construction
workflow. It applies to every requested skill before domain-specific objects are
selected.

After bootstrap, SkillForge loads only the package or packages required for the
request. A drawing-only installation therefore contains `metaskills` and `art`,
but not `software_development`.

## Generated indexes

`tools/build_index.py` generates an `INDEX.md` at the library root and in every
directory that contains objects or child directories. Each generated index:

- states that it is generated and must not be hand-edited;
- lists direct child topics before direct objects;
- lists each object by name, type, stage binding, and relative link;
- lists each absorbed variant by name and basis beneath its foundation object;
- uses deterministic alphabetical ordering;
- identifies package boundaries at the root;
- places the mandatory bootstrap object before optional packages in the root
  index.

The generator derives every listing from validated object frontmatter. It never
relocates objects or accepts a directory that disagrees with `library_path`.

## Package boundaries

A package is a top-level library directory, not a duplicate export tree. Package
installation means copying the `metaskills` directory and the selected top-level
package directories with their generated indexes. An object may cross-link into
another package, but the root index must disclose that package dependency; a
consumer must load the target package before following that link.

No hand-authored package manifest exists. The generator derives package membership
and cross-package dependencies from `library_path` and `cross_links`.
