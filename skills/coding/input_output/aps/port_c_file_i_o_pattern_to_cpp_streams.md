# Port C File I/O Pattern To C++ Streams

**Object ID:** AP-CPP-005  
**Object Type:** ap  
**Category:** coding  
**Subcategory:** input_output  
**Stage Binding:** 3 rough  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** c, cpp, file_io, modernization  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.59-67; evidence: text  

## Objective

Translate a FILE*/fscanf/fprintf pipeline into a C++ stream pipeline.

## Steps / Flow

1. Map fopen to ifstream/ofstream.
2. Map fscanf result check to stream extraction check.
3. Map fprintf formatting to modern formatting or localized stream formatting.
4. Remove explicit fclose when RAII owns files.
5. Retain equivalent error behavior.

## Notes

Compiled as an application pattern for SkillForge execution.

## Modernization

- Use current C++ project/toolchain conventions when executing this AP.
