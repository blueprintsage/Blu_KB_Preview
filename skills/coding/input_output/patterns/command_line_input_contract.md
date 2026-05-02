# Command-Line Input Contract

**Object ID:** PAT-CPP-007  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** input_output  
**Stage Binding:** 1 skeleton  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** cli, input, validation  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp. 25-29, 46-48; evidence: text  

## Pattern Rule

**IF** a program requires runtime input  
**THEN** define argc/argv contract and validate argument count  
**ELSE** read argv blindly  

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


### Variant: Optional Argument Default

**Variant Axis:** argument contract  
**Use When:** a program has a safe default  
**IF** an argument is optional  
**THEN** document the default and branch explicitly  
**ELSE** emit usage and stop  

### Variant: Required Argument Fail Fast

**Variant Axis:** argument contract  
**Use When:** missing input would corrupt execution  
**IF** a required argument is missing  
**THEN** print usage and return failure  
**ELSE** continue only with validated values
