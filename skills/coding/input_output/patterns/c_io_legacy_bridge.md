# C IO Legacy Bridge

**Object ID:** PAT-CPP-017  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** input_output  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** c, file_io, legacy  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp. 59-67; evidence: text  

## Pattern Rule

**IF** working with legacy C file APIs  
**THEN** model FILE* open/read/write/close explicitly  
**ELSE** mix C and C++ I/O without a reason  

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
