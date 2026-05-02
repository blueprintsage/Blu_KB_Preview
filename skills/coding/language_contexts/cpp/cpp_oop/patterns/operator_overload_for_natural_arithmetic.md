# Operator Overload For Natural Arithmetic

**Object ID:** PAT-CPP-055  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** language_contexts/cpp/cpp_oop  
**Stage Binding:** 1 skeleton  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** operators, numeric_types, cpp  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp. 145-205; evidence: text  

## Pattern Rule

**IF** a numeric type has natural operations  
**THEN** overload operators to express domain arithmetic clearly  
**ELSE** force awkward function-call notation everywhere  

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
