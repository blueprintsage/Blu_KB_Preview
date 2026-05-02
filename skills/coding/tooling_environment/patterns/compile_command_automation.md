# Pat-Cpp-013 Compile Command Automation

## Object Type
pattern

## Category
coding

## Subcategory
tooling_environment

## Stage Binding
2 block

## Lane Fit
skill

## Pattern Rule
**IF** the older repo pattern expresses a valid C++ idea but the Stroustrup source gives a stronger modern formulation  
**THEN** replace the base object and absorb useful prior variants  
**ELSE** keep the prior object unchanged

## Do
- Keep the direct C++ concept.
- Prefer type-safe, standard-library-backed, resource-safe expression.
- Preserve useful earlier variants below.

## Don't
- Keep legacy phrasing when the stronger source clarifies the rule.
- Split the same base concept into duplicates.

## Checklist
- Base rule is stronger than prior repo version.
- Prior variants are retained or restated.
- Modern C++ use remains clear.

## Variants

### Variant: Legacy Compatibility
**IF** older C or C++ code must be maintained  
**THEN** isolate the legacy form behind the modern base pattern  
**ELSE** prefer the modern form directly

## Reference
- Source: The C++ Programming Language, 4th Edition
- Author: Bjarne Stroustrup
- Evidence: text
