# Template Generalization

**Object ID:** PAT-CPP-060  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** language_contexts/cpp/cpp_stl  
**Stage Binding:** 1 skeleton  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** templates, generic_programming, reuse  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp. 210-250; evidence: text  

## Pattern Rule

**IF** the same algorithm works for multiple types  
**THEN** parameterize the type with templates/generics  
**ELSE** duplicate the algorithm per type  

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
