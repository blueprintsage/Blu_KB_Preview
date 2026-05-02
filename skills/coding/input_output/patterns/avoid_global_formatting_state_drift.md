# Avoid Global Formatting State Drift

**Object ID:** PAT-CPP-045  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** input_output  
**Stage Binding:** 3 rough  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** formatting, state, output  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp. 48, 51; evidence: text  

## Pattern Rule

**IF** formatting streams repeatedly  
**THEN** localize formatting decisions near the output  
**ELSE** leave stream state changed for distant code  

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
