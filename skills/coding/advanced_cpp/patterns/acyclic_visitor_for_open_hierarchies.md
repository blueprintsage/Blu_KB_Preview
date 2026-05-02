# Acyclic Visitor for Open Hierarchies

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
- visitor
- dispatch
- oop

## Pattern Rule
**IF** both operations and visited types change over time,  
**THEN** avoid a brittle cyclic visitor dependency,  
**ELSE** every new type forces broad visitor edits.

## Do
- Use classic Visitor for stable type sets and changing operations.
- Use acyclic visitor or pattern matching alternatives when the hierarchy is more open.
- Keep fallback handling explicit.

## Don't
- Do not add catch-all handlers that silently swallow unsupported types.
- Do not use Visitor when a virtual function on the object is enough.

## Checklist
- You know which axis changes more often.
- Unsupported type behavior is visible.
- The dispatch path remains testable.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 219, 220, 225, 226, 230
