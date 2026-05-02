# Policy-Based Class Design

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
- policy_based_design
- templates
- architecture
- modernization

## Pattern Rule
**IF** a type needs many independent behavioral choices,  
**THEN** make each choice a policy and compose them in a host class,  
**ELSE** adding options multiplies branches and weakens static guarantees.

## Do
- Name the host’s stable job before naming policies.
- Keep each policy focused on one behavioral or structural dimension.
- Use defaults for common cases, but leave advanced choices replaceable.
- Validate combinations where incompatible policies can be selected.

## Don't
- Do not turn policy design into ceremony for a one-off class.
- Do not hide runtime state changes behind compile-time vocabulary.
- Do not preserve Loki-era syntax when modern facilities express the same idea safely.

## Checklist
- Variation points are orthogonal.
- Each policy has a small expected interface.
- The host owns orchestration, not every detail.
- Modern alternatives were considered before custom templates were kept.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 16, 17, 21, 26, 27
