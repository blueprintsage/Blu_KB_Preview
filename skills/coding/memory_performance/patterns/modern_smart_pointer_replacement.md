# Modern Smart Pointer Replacement

**Object ID:** PAT-CPP-073  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** memory_performance  
**Stage Binding:** 1 skeleton  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** smart_pointers, modern_cpp, raii  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp. 82-83; evidence: text  

## Pattern Rule

**IF** shared or unique ownership is needed  
**THEN** use unique_ptr/shared_ptr according to ownership semantics  
**ELSE** use legacy hand-rolled reference counting by default  

## Do

- State the condition before choosing the method.
- Keep the smallest correct implementation path.
- Preserve source lesson while updating stale mechanics.

## Don't

- Do not copy dated syntax blindly.
- Do not let language-specific detail override the general skill.

## Checklist

- Is the condition explicit?
- Is the action current for C++?
- Is the fallback safe?

## Notes

Extracted as a reusable programming pattern.

## Modernization

- Replace dated C++98/C APIs with current C++ idioms when the lesson is about production coding.

## Variants


### Variant: unique_ptr Ownership

**Variant Axis:** ownership cardinality  
**Use When:** one owner exists  
**IF** a resource has one owner  
**THEN** use std::unique_ptr  
**ELSE** do not use shared_ptr by habit  

### Variant: shared_ptr Ownership

**Variant Axis:** ownership cardinality  
**Use When:** shared lifetime is truly required  
**IF** multiple owners must share lifetime  
**THEN** use std::shared_ptr intentionally  
**ELSE** prefer unique ownership


### Variant absorbed: Policy-axis smart pointer audit
Before replacing a custom smart pointer, name the axes it encoded: ownership, null checking, conversion, storage, and threading. Replace ordinary axes with standard smart pointers; keep wrappers only for remaining nonstandard semantics. Source: Modern C++ Design, pp. 152-185.


## PASS Variant Absorption — Boost C++ Application Development Cookbook

- Absorbed variant: Boost smart pointer compatibility layer
- Absorbed as: variant/refinement note
- Source handling: transformed idea only; no source prose copied.
- Modernization: treat Boost-era mechanics as either standard-library migration targets or Boost-specific tools when the standard library still lacks equivalent coverage.
