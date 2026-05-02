# Modernize Raw Dynamic Array Code

**Object ID:** AP-CPP-008  
**Object Type:** ap  
**Category:** coding  
**Subcategory:** memory_performance  
**Stage Binding:** 3 rough  
**Lane Fit:** skill  
**Foundation Role:** specialization  
**Confidence:** high  
**Tags:** raii, memory, modern_cpp  
**Reference:** Introduction to C++ (and C) Programming; Hans Petter Langtangen; 2006-01; pp.74-84; evidence: text  

## Objective

Replace manual C/C++ dynamic memory examples with RAII-owned containers.

## Steps / Flow

1. Identify each raw allocation.
2. Identify ownership and lifetime.
3. Choose std::vector/std::array/unique_ptr as appropriate.
4. Rewrite loops without changing semantics.
5. Remove manual deallocation.
6. Add small regression check.

## Notes

Compiled as an application pattern for SkillForge execution.

## Modernization

- Use current C++ project/toolchain conventions when executing this AP.
