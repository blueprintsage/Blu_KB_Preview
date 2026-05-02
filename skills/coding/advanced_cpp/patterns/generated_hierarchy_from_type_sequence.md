# Generated Hierarchy from Type Sequence

## Object Type
pattern

## Category
coding

## Subcategory
advanced_cpp

## Stage Binding
3 rough

## Lane Fit
skill

## Foundation Role
advanced

## Tags
- typelists
- code_generation
- architecture

## Pattern Rule
**IF** many classes repeat the same shell over different types,  
**THEN** generate the shell from a static type sequence,  
**ELSE** manual hierarchies drift and duplicate bugs.

## Do
- Reserve generated hierarchies for stable repetitive structure.
- Keep the generated base interface small.
- Prefer modern pack expansion and inheritance utilities over Loki-era recursion.

## Don't
- Do not generate a hierarchy just to avoid naming two simple classes.
- Do not hide ownership or virtual dispatch rules inside the generator.

## Checklist
- The repeated structure is real.
- The type list is the source of truth.
- The generated hierarchy is easier to audit than the hand-written alternative.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 68, 69, 70, 71, 72, 73
