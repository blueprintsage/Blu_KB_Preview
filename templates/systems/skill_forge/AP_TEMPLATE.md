# APPLICATION PACK TEMPLATE v2 (AP)

## Header
- id: AP-<DOMAIN>-<SUBJECT>-<###>
- name: <Hands | Figure Drawing | Perspective Rooms | Fight Beats | etc.>
- domain: <art|comics|writing|code>
- subject: <hands|figure|...>
- status: <active|draft|deprecated|merged>
- tags: [domain:<>, topic:<>, context:<>, level:<L0-L4>]
- links:
  - parent_ap: <AP-... or null>         # e.g., Hands -> Figure Drawing
  - sibling_aps: [AP-..., ...]          # optional

## Governing Patterns (LAW)
- governing_patterns:
  - <PAT-...>   # HARD first, then SOFT
- pattern_clusters:
  - <GLOBAL_READABILITY>
  - <GLOBAL_SPATIAL_INTEGRITY>
  - <SUBJECT_HANDS>
  # (clusters are optional labels; the actual enforcement is via IDs above)

## Function Contract
- purpose: <what this AP accomplishes>
- inputs: <what the user/system provides>
- outputs: <what must be produced>
- done_means: <objective completion definition>

## Step Ladder Binding (universal scaffold)
> The Step Ladder runs by default. This AP specifies WHAT to do and WHAT to check at each step.

### Step 0 — Intent Lock
- decide:
  - <pose intent / target / constraints>
- checks:
  - <pattern IDs or brief check lines>
- outputs:
  - <thumb/plan artifacts>

### Step 1 — Skeleton
- procedure:
  - <minimum framework steps>
- checks:
  - <PAT-... list>
- outputs:
  - <skeleton-level artifact>

### Step 2 — Block
- procedure:
  - <major masses/volumes/dependencies>
- checks:
  - <PAT-... list>
- outputs:
  - <block-level artifact>

### Step 3 — Rough
- procedure:
  - <accuracy, landmarks, edge cases, constraint enforcement>
- checks:
  - <PAT-... list>
- outputs:
  - <rough artifact>

### Step 4 — Final
- procedure:
  - <finish, readability, style compliance, cleanup>
- checks:
  - <PAT-... list>
- outputs:
  - <final artifact(s)>

## Failure Modes (routing anchors)
- failure_modes:
  - signature: <what it looks like>
    likely_cause: <why>
    prescribe:
      - pattern: <PAT-...>
      - drill: <DRL module id or drill file pointer>
      - step: <0|1|2|3|4>

## Modules (VARIANTS + ADD-ONS)
> Prefer modules over spawning new AP files.

### Module format
- module_id: AP.MOD.<NAME>
- when_to_use: <context trigger>
- overrides_allowed:
  - constraints
  - inputs/outputs
  - step_deltas (add/remove/replace specific steps)
  - extra_checks
  - failure_modes_additions
- module_body:
  - step_deltas:
      step_2_add: [...]
      step_3_replace: [...]
  - extra_checks:
      - <PAT-...>
  - notes:

## Merge Metadata
- dedupe_key: <stable signature>
- replaces: [AP-...]
- variant_of: <AP-... or null>
- merged_from_sources:
  - <source_id>

## Source Pointer (no quotes)
- source_ptr:
  - <book/pdf title>, p.<#>, section <name>
