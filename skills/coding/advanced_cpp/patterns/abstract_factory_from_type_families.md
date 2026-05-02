# Abstract Factory from Type Families

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
- abstract_factory
- typelists
- families

## Pattern Rule
**IF** products must be created in compatible families,  
**THEN** make the family boundary part of the factory interface,  
**ELSE** clients can mix products that were never meant to collaborate.

## Do
- Use abstract factories when family consistency matters.
- Represent the product set explicitly.
- Modernize generated factory interfaces with packs or simpler templates where possible.

## Don't
- Do not use abstract factory for one product type.
- Do not hide incompatible product combinations behind casts.

## Checklist
- The family has more than one related product.
- The factory prevents cross-family creation errors.
- The client receives products through stable interfaces.

## Modernization
- Treat Loki-era machinery as a design lesson first and an implementation recipe second.
- Prefer standard C++ facilities when they express the same intent with less risk.
- Keep custom template machinery only when it buys a real type-system constraint, performance boundary, or extension point.

## Reference
- Source: Modern C++ Design: Generic Programming and Design Patterns Applied
- Author: Andrei Alexandrescu
- Publish Date: 2001-02-01
- Evidence Type: text-layer pdf
- Evidence Pages: 205, 206, 210, 214, 216
