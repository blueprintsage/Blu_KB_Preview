# Use RAII Containers

**Object ID:** PAT-CPP-025  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** memory_performance  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** raii, vector, modern_cpp  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp. 74-84; evidence: text  

## Pattern Rule

**IF** dynamic arrays are needed in modern C++  
**THEN** use std::vector, std::array, or RAII wrappers  
**ELSE** manage raw new/delete directly  

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


### Variant: std::vector Dynamic Array

**Variant Axis:** container choice  
**Use When:** the object is a resizable runtime-length sequence  
**IF** runtime-length contiguous storage is needed  
**THEN** use std::vector<T>  
**ELSE** do not hand-write new/delete arrays  

### Variant: std::array Fixed Array

**Variant Axis:** container choice  
**Use When:** the size is fixed at compile time  
**IF** compile-time fixed contiguous storage is needed  
**THEN** use std::array<T, N>  
**ELSE** avoid raw C arrays unless interoperability requires them
