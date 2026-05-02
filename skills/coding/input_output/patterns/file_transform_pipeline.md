# File Transform Pipeline

**Object ID:** PAT-CPP-014  
**Object Type:** pattern  
**Category:** coding  
**Subcategory:** input_output  
**Stage Binding:** 2 block  
**Lane Fit:** skill  
**Foundation Role:** foundation  
**Confidence:** high  
**Tags:** file_io, pipeline, transformation  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp. 45-48, 59-64; evidence: text  

## Pattern Rule

**IF** a program transforms records from one file to another  
**THEN** structure the flow as open-read-transform-write-close  
**ELSE** mix transformation logic with resource setup unpredictably  

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


### Variant: Streaming Transform

**Variant Axis:** data size  
**Use When:** the file may be large  
**IF** records can be processed independently  
**THEN** stream one record at a time  
**ELSE** load only when whole-data context is required  

### Variant: Buffered Transform

**Variant Axis:** data size  
**Use When:** whole-file context is needed  
**IF** later records depend on earlier/global data  
**THEN** buffer into a container with validation  
**ELSE** prefer streaming
