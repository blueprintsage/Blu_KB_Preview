# Visitor Dispatch Tradeoff Drill

## Object Type
drill

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
- practice
- visitor
- dispatch

## Practice Task
Given a hierarchy and a set of operations, choose between virtual functions, classic Visitor, acyclic Visitor, and double dispatch.

## Target Skill
Match dispatch design to the axes of change.

## Setup
Use shapes, AST nodes, game entities, or UI controls.

## Instructions
1. Count runtime objects needed for the decision.
2. Mark whether types or operations change more often.
3. Choose the dispatch pattern.
4. Write the missing-handler behavior.
5. Explain why one alternative was rejected.

## Success Check
- The chosen pattern follows the change axis.
- Missing cases cannot fail silently.
- The design does not add extra dispatch layers without need.

## Common Failures
- Using Visitor when one virtual function would do.
- Using type switches without centralizing missing cases.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 219, 225, 230, 242
