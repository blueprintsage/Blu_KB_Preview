# Low-Level Detail Awareness

**Object ID:** PAT-CPP-037  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** core_mechanics  
**Stage Binding:** 0 design  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** mental_model, memory, cpp  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp. 5, 74-83; evidence: text  

## Pattern Rule

**IF** working near machine representation  
**THEN** learn the underlying storage and pointer model  
**ELSE** treat high-level syntax as magic  

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
