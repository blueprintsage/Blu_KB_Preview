# Input Validation Before Conversion

**Object ID:** PAT-CPP-008  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** testing_validation  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** validation, conversion, safety  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp. 25-31, 43-44; evidence: text  

## Pattern Rule

**IF** text input must become numeric data  
**THEN** validate presence and conversion before using it  
**ELSE** call atof/atoi blindly  

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
