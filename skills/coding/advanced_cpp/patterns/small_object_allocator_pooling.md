# Small Object Allocator Pooling

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
- memory_performance
- allocators
- profiling

## Pattern Rule
**IF** profiling shows allocator overhead from many tiny objects,  
**THEN** use a small-object allocator or modern memory resource,  
**ELSE** custom allocation adds risk without evidence.

## Do
- Measure allocation pressure before optimizing.
- Group by size class and alignment.
- Prefer `std::pmr` or proven allocator libraries in modern C++.
- Keep deallocation paths simple and testable.

## Don't
- Do not replace general allocation because it feels lower level.
- Do not mix ownership policy and allocator policy unless the host explicitly coordinates them.

## Checklist
- Profiling identifies allocation as a bottleneck.
- Object size and lifetime distribution fit pooling.
- Threading and cleanup rules are documented.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 82, 83, 84, 85, 86, 87, 88
