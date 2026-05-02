# Smart Pointer Policy Matrix

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
- smart_pointers
- ownership
- policy_based_design

## Pattern Rule
**IF** a pointer abstraction has multiple independent semantics,  
**THEN** name each semantic axis before implementing,  
**ELSE** the pointer type becomes a bundle of surprising behavior.

## Do
- Prefer `std::unique_ptr`, `std::shared_ptr`, and `std::weak_ptr` for ordinary ownership.
- Use custom policies only for unusual storage, checking, or ownership constraints.
- Make implicit conversion to raw pointers an explicit design decision.

## Don't
- Do not build a smart pointer just because templates make it possible.
- Do not combine ownership transfer and null-checking behavior without tests.

## Checklist
- Ownership is named.
- Null behavior is named.
- Conversion behavior is named.
- Threading expectations are named.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 152, 153, 157, 160, 166, 178, 185
