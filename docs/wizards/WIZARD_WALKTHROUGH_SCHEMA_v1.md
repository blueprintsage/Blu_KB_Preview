# Wizard Walkthrough Schema v1

**Purpose:** Define a uniform, repo-hosted walkthrough format for `EXECLIB.WIZARD` to execute.
**Design:** KISS. One-question-per-tick. Walkthroughs are *data*, not code.

---

## File location

Store walkthroughs at:

- `docs/wizards/<WIZARD_ID>.md`

Examples:
- `docs/wizards/USERPREFS.md`
- `docs/wizards/SCHOOL_SETUP.md`

---

## Required header

At the top of every walkthrough:

```yaml
wizard_id: <WIZARD_ID>          # e.g., USERPREFS
version: 1.0.0
entry_step: <STEP_ID>           # first step
complete_step: <STEP_ID>        # terminal step that returns COMPLETE
state_namespace: <NAMESPACE>     # where answers are stored, e.g., userprefs
```

---

## Step blocks

Each step is a fenced YAML block with `step_id` and `prompt`, plus an input spec.

```yaml
step_id: <STEP_ID>
prompt: "<question to ask>"
input:
  type: choice | text | number | confirm
  required: true | false
  choices:                # only for type=choice
    - id: <ID>
      label: "<display>"
store:
  key: "<state key>"      # stored under state_namespace
  transform: none | trim | lower | upper
validate:
  rule: none | regex | range | one_of
  regex: "<pattern>"      # if rule=regex
  min: <n>                # if rule=range
  max: <n>                # if rule=range
next:
  default: <STEP_ID>
  on_value:               # optional branching
    <CHOICE_ID>: <STEP_ID>
```

**Rules**
- Exactly **one** prompt per step.
- Steps must be deterministic: given state + input → next step.
- No freeform “chatty” responses from the wizard runner; it only emits the prompt (or COMPLETE).

---

## Built-in validation rules (KISS)

- `none`
- `regex`
- `range` (numbers)
- `one_of` (choices)

If a step needs complex validation, reference a Program validator instead of embedding logic:

```yaml
validate:
  rule: program_ref
  program: "PROGRAM.<Name>.v1::<method>"
```

---

## Completion step

The completion step is a normal step with:

```yaml
step_id: <COMPLETE_STEP_ID>
complete: true
```

When reached, the runner returns:
- `status: COMPLETE`
- `state_delta` with accumulated values (namespaced)

---

## Example: USERPREFS (minimal)

```yaml
wizard_id: USERPREFS
version: 1.0.0
entry_step: UP-01
complete_step: UP-DONE
state_namespace: userprefs
```

```yaml
step_id: UP-01
prompt: "Timezone? (e.g., America/Chicago)"
input:
  type: text
  required: true
store:
  key: timezone
  transform: trim
validate:
  rule: regex
  regex: "^[A-Za-z]+/[A-Za-z_]+$"
next:
  default: UP-02
```

```yaml
step_id: UP-02
prompt: "Verbosity? (brief/standard/detailed)"
input:
  type: choice
  required: true
  choices:
    - id: brief
      label: "brief"
    - id: standard
      label: "standard"
    - id: detailed
      label: "detailed"
store:
  key: verbosity
  transform: lower
validate:
  rule: one_of
next:
  default: UP-DONE
```

```yaml
step_id: UP-DONE
complete: true
```

---
