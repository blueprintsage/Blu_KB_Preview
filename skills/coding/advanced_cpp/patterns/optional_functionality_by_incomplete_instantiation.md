# Optional Functionality by Incomplete Instantiation

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
- templates
- policy_based_design
- compile_time

## Pattern Rule
**IF** an optional member only matters for specific policy choices,  
**THEN** isolate that member so unused paths do not require richer policies,  
**ELSE** optional behavior becomes a global requirement.

## Do
- Put optional policy calls in optional member functions.
- Keep mandatory host operations free of optional requirements.
- Document which policy surface activates each optional member.

## Don't
- Do not assume unused template code was semantically checked in all useful ways.
- Do not hide critical correctness behind an optional path.

## Checklist
- Basic behavior compiles with a minimal policy.
- Optional behavior fails loudly if the policy cannot support it.
- Tests instantiate the optional path intentionally.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 25, 26
