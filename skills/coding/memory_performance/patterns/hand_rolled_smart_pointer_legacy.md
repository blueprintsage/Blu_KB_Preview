# Hand Rolled Smart Pointer Legacy

**Object ID:** PAT-CPP-094  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** memory_performance  
**Stage Binding:** 1 skeleton  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** smart_pointers, legacy, modernization  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp. 82-83; evidence: text  

## Pattern Rule

**IF** encountering legacy Handle-style code  
**THEN** understand the ownership idea then map to standard smart pointers  
**ELSE** copy the old reference-counting class as-is  

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

### Variant absorbed: Loki-era smart pointer as design map
Treat hand-rolled smart pointers as a map of ownership-policy decisions, not as a default implementation recipe. Use them to identify semantics before modern replacement. Source: Modern C++ Design, pp. 152-185.
