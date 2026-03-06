# KERNEL CAPSULE TEMPLATE

Use this template for runtime kernels that need:
- markdown header outside module
- uniform module structure
- clear human scanability
- explicit ownership boundaries

---

## <SECTION TITLE>

module: <namespace.M00> | name="<Human Name>"
id: <CANONICAL_ID>
name: <Human Name>
version: <x.y.z>
status: DRAFT
purpose: <one sentence>

owns:
- <what this layer/file owns>
- <what this module owns>

does_not_own:
- <what belongs to another layer>
- <what this module must not redefine>

inputs:
- <input_1>
- <input_2>

outputs:
- <output_1>
- <output_2>

rules:
- <rule_1>
- <rule_2>
- <rule_3>

verification:
- test: <one test command or condition>
- expected: <expected result>

/module

---

## <SECTION TITLE>

module: <namespace.M01> | name="<Human Name>"
id: <CANONICAL_ID>
name: <Human Name>
version: <x.y.z>
status: DRAFT
purpose: <one sentence>

owns:
- <what this module owns>

does_not_own:
- <what this module must not own>

inputs:
- <input_1>

outputs:
- <output_1>

rules:
- <rule_1>
- <rule_2>

verification:
- test: <one test command or condition>
- expected: <expected result>

/module

---

## STYLE RULES

- Markdown section header stays OUTSIDE the module.
- One module = one responsibility.
- Keep metadata ordering consistent:
  - module
  - id
  - name
  - version
  - status
  - purpose
  - owns
  - does_not_own
  - inputs
  - outputs
  - rules
  - verification
- Use the same schema style across Exec, Exec_Library, and Program_System.
- Do not let a file claim ownership it does not actually implement.
- Prefer full replacement blocks over patch snippets when editing live kernel files.

## RECOMMENDED NAMESPACES

- Exec: `exec.Mxx`
- Exec_Library: `execlib.Mxx`
- Program_System: `program.Mxx`
- Operations_Law: `ops.Mxx` if modularized later

## HUMAN REVIEW CHECK

Before saving a capsule:
- [ ] Header is outside the module
- [ ] Module name matches ownership
- [ ] Owns / does_not_own are explicit
- [ ] Rules do not redefine another layer
- [ ] Verification is present
- [ ] Schema order matches the rest of the kernel
