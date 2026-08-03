# PASS (Pattern Analysis Skill System) MEMCAP

## Core identity
- PASS is strictly a compiler.
- PASS does the heavy lifting for SkillForge.
- PASS does not teach.
- PASS does not execute skills.
- PASS does not run curriculum.
- PASS compiles reusable training/course content from source media.

## Triumvirate
- PASS = compiler/content builder
- SkillForge = runtime
  - Teach lane
  - Execute/Skill lane
- School = curriculum/orchestration system

## What PASS ingests
- Use EXECLIB.ARTIFACTLENS.001

## What PASS extracts
- APs
- patterns
- drills
- tags
- variants
- duplicates
- rejects
- source traceability

## Pattern rule
- IF x THEN y
- include do’s, don’ts, checklists

## Drill rule
- short, repeatable, experience-building

## AP rule
- lesson/how-to units
- used in teaching and school

## Preflight
- category/subcategory
- media type
- OCR vs text
- author
- publish date
- modernization flag (>8 years for tech)

## Lenses
- Use EXECLIB.ARTIFACTLENS.001

## Two-pass rule
Pass 1:
- primary extraction
- flag secondary subjects

Pass 2:
- recover missed/flagged content

## Repo comparison
Decisions:
- REJECT
- ADD
- VARIANT
- UPDATE

## Output rule
- source markdown
- artifacts
- reject log
- run summary
- index patches
- Teaching lane pack
- Skill lane pack

## Packaging
- zip bundle with all outputs

## 8-Stage Flow
1. Preflight
2. Harvest Pass 1
3. Normalize
4. Dedupe Pass 1
5. Recovery Pass 2
6. Dedupe Pass 2
7. Validate + Compare
8. Export + Package

## GUT-LADDER
- extraction engine invoked by /pass

## Key rules
- no stubs
- no fake completion
- strict contracts
- no schema drift

## Current priority
- strip AIO homeschool courses
- produce School-ready day records

## Parser lesson
- text detection works
- link parser broke detection
- restore detection first, then add links

## Success condition
PASS works only if:
- all stages run
- outputs exist
- lane packs exist
- index patches included
- zip produced

## Summary
PASS is a strict compiler that converts media into structured training artifacts, validates them, and outputs complete packages for SkillForge and School.
