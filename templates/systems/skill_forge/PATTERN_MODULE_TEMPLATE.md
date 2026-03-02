# PATTERN MODULE TEMPLATE v2

## Header
- id: PAT-<DOMAIN>-<CLUSTER>-<###>
- name: <short name>
- domain: <art|comics|writing|code>
- cluster: <e.g., SPATIAL_INTEGRITY | READABILITY | HANDS | FORESHORTENING>
- severity: <HARD|SOFT>
- bind_stage: <0|1|2|3|4>   # Step Ladder binding
- status: <active|draft|deprecated|merged>
- dedupe_key: <stable key; intent+outcome+constraints signature>
- tags: [domain:<>, topic:<>, phase:<>, context:<>, risk:<>, level:<L0-L4>]

## LAW (IF → THEN)
- IF: <trigger condition (X)>
- THEN: <required constraint/obligation (Y)>

## Scope
- applies_to: <what outputs / subjects / contexts>
- does_not_apply_when: <explicit carve-outs>

## Evidence (PASS / FAIL)
- PASS_condition: <what proves compliance>
- FAIL_condition: <what breaks it>
- failure_signatures:
  - <symptom phrase>
  - <symptom phrase>

## Exceptions / Notes
- exceptions:
  - <unless/except case>
- notes: <short operational notes>

## Ladder Hooks (optional but recommended)
- step_0_intent_lock: <what to decide/avoid>
- step_1_skeleton_check: <what must be true>
- step_2_block_check: <what must be true>
- step_3_rough_check: <what must be true>
- step_4_final_check: <what must be true>

## Merge Metadata
- replaces: [PAT-...]
- variant_of: <PAT-... or null>
- merged_from_sources:
  - <source_id>

## Source Pointer (no quotes)
- source_ptr:
  - <book/pdf title>, p.<#>, section <name>
