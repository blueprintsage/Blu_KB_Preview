# BluCode Index

status: active
purpose: Reusable coding-memory skillset for Blu kernel work.
scope: Guidance for modifying Blu’s own kernel/spec/runtime files without repeating known failure patterns.

## Use Rule

Before working on Blu kernel code, consult this index first.

When a kernel-code change breaks, add the reusable lesson here after the failure is understood. Lessons should be code-agnostic when possible, so they apply across commands, libraries, routing, rendering, artifacts, and future SkillForge domains.

## Core Operating Rules

### Full-file discipline
- When the user asks for replacement files, provide complete replacement files, not patch fragments.
- Do not give vague “insert somewhere” instructions to a non-coder user.
- If exact placement matters and a full file is not provided, the instruction is not safe enough.
- Do not mix patch fragments, replacement files, and architectural commentary in the same deliverable.

### Source-first discipline
- Read the actual active files before diagnosing kernel behavior.
- Do not assume section names, module names, or file structure.
- Do not treat spec presence as runtime proof.
- Do not call a build “working” because a module exists; live behavior or a route matrix must prove it.

### One failure seam at a time
- Identify whether the break is in routing, dispatch, library output, render mapping, validation, state, or print.
- Do not patch multiple layers until the failure seam is isolated.
- If the diagnosis changes, stop and restate the highest verified truth before producing another artifact.

### No blind patch churn
- Do not stack patches over patches when live behavior is worsening or cycling.
- If a patch does not change the observed output class, stop patching and inspect the active files/path.
- If a working state is lost, recover or rebuild from source rather than continuing ad hoc changes.

## Category: Command Routing

### Slash-command first-read lock
- Slash commands must be intercepted before source-grounded answering, Persona prose, ordinary fallback, or documentation-style response modes.
- If a slash command produces a “Sources” affordance or summarizes spec files, it did not execute through the command owner.
- Fix the command intercept/route priority before changing downstream libraries.

### Command dispatch / status-readback contamination
- A slash command can be correctly intercepted but still execute the wrong subroute if its name resembles a status/readback command.
- Failure example: `/mood show` reached `EXEC.MOOD` but generated status prose such as “Mood display is currently set to smart” instead of executing the render path.
- Cause: model generalized from another command’s readback pattern, especially `/verbosity`-style output.
- Rule: subcommands with unique execution profiles must be hard-bound before generic readback/status branches.
- Prevention:
  - resolve exact subcommand first
  - route unique actions before generic status/readback branches
  - add forbidden-output tests for plausible fabricated status lines
  - require deterministic owner output shape before print
- Canonical lesson: If a command is intercepted but prints the wrong kind of valid-looking response, check entrypoint dispatch before changing the downstream library.

### State-setting vs render commands
- State-setting commands must not accidentally render.
- Render commands must not accidentally report configuration state.
- Command families should explicitly separate:
  - state setters
  - status readers
  - render/display commands
  - destructive/mutating commands
- `/mood show` is a render command, not a status query.

### Invalid singular/plural commands
- If the public command surface defines `/mood circles`, singular `/mood circle` should fail closed as invalid unless explicitly listed.
- Do not silently normalize undocumented aliases unless the command contract permits it.

## Category: Ownership Boundaries

### Exec as final renderer
- If output shape matters, Exec must be the final renderer or final validator.
- Libraries should return structured payloads when the render contract belongs to Exec.
- A library returning display-ready text can bypass the intended output gate.

### Persona boundary
- Persona may shape internal state, posture, ribbons, and mood semantics.
- Persona must not directly print command output, public mood output, validation output, or deterministic workflow lines.
- If output looks like “steady — warm, present” or mood prose chains, check whether Persona or PersonaLib is leaking renderable text.

### Library boundary
- RibbonLib should normalize ribbon/color tokens.
- MoodLib should resolve structured mood payloads.
- Exec should map color tokens to public glyphs and print the final line when Exec owns the render.
- Do not let multiple layers map, decorate, or print the same concept.

## Category: Rendering

### Render authority
- Decide exactly one owner for final public render.
- If two layers can render, they will eventually disagree.
- For Mood R4, the intended chain is:
  - Persona = state/source only
  - RibbonLib = color tokens only
  - MoodLib = structured mood payload only
  - Exec = `[MOOD] <MoodWord> <Swatches>` renderer

### Negative examples can become anchors
- In hosted prompt-runtime specs, repeated forbidden examples can become output anchors.
- Use forbidden examples sparingly and frame them as invalid tests, not as reusable prose.
- Prefer positive output contracts and exact validation rules.
- If a bad literal keeps appearing, search for the literal or close variants in all active prompt/spec files.

### Symbol output must be explicit
- If symbolic output is required, specify the exact canonical symbol table.
- Do not rely on “circle” or “square” descriptions; models may choose text glyphs like `•` or `■`.
- If emoji are required, explicitly ban text-shape fallbacks unless a text-only mode is intentionally defined.

### Render freeze
- Once the deterministic line is built, final render must not paraphrase, decorate, lowercase, add emoji, or change prefixes.
- A validated line should be printed literally.
- If a command output changes from `[MOOD] Steady 💙` to `Mood: steady 💙`, the final print/freeze boundary failed.

## Category: Validation and Gates

### Gate presence is not gate execution
- A gate existing in a file does not prove runtime went through it.
- If the output violates the gate, ask first whether the gate was reached.
- Distinguish:
  - routing failure: owner never reached
  - dispatch failure: wrong entrypoint
  - validation failure: bad output allowed after correct entrypoint
  - print mutation: validated output changed later

### Forbidden-output tests
- Add tests for plausible wrong outputs, not just obviously bad outputs.
- Fabricated but “reasonable” outputs are dangerous because they pass generic filters.
- Example: a status-readback line for a render command.

### Fail closed, not fallback prose
- Deterministic commands should not answer conversationally when their required support path fails.
- Fallback prose hides the real failing layer.
- Prefer explicit invalid/blocked outputs during debugging, then clean user-facing errors once stable.

## Category: State and Smart Behavior

### Force render vs auto render
- A display command may need to force render independently of persistent mode.
- `/mood show` should render on demand even when automatic mood display is off or smart.
- `/mood on` enables automatic display but should not be required for `/mood show`.

### State setters should confirm only
- `/mood on`, `/mood off`, `/mood smart`, `/mood hearts`, `/mood circles`, and `/mood squares` are state-setting commands.
- They should commit state and print confirmation only.
- They should not produce a mood line unless the contract explicitly says so.

### Signature-based smart firing
- Smart mode should fire on materially visible mood change using a visible signature, not arbitrary internal churn.
- Avoid artificial extra ticks when a visible signature-change trigger is cleaner.
- Do not fire smart render for pure command state changes or swatch-mode changes unless explicitly requested.

### Exec-owned heartbeat
- Runtime counters like heartbeat should be owned/committed by Exec or state management.
- Support libraries may request updates but should not be the source of committed state truth.

## Category: File and Archive Hygiene

### Complete artifacts
- If the user will upload/drop files, provide complete files or a complete archive.
- Clearly state what files are included and what files must not be touched.
- Do not include unrelated kernel files in a focused fix archive.

### Instructions are emergency floor only
- Do not patch `00_Instructions.md` for subsystem behavior.
- If a subsystem only works because Instructions forces it, fix Exec or the proper owner.
- Instructions are for pure open runtime and emergency constraints, not ordinary feature repair.

### BluCode index handling
- When updating BluCode, provide a full merged `libraries/blu_code/INDEX.md`, not a one-entry partial index.
- If the user asks for a BluCode archive, include only BluCode files unless they request kernel files too.
- Keep lessons code-agnostic when possible.

### Repo hygiene
- Do not update `INDEX_LIBRARIES.md` unless adding/removing library paths requires it.
- Do not touch repo indexes just because a local lesson was added.
- Keep change scope explicit.

## Category: Debugging Workflow

### Use live output as evidence
- Screenshots/live outputs are evidence of the active runtime path.
- If live output conflicts with the spec, trust the live output as proof of a defect or load mismatch.
- Use the literal output shape to identify the failing layer.

### Compare output classes
- `Sources` affordance: source-grounded answer path captured the command.
- `Mood: ...` prose: legacy/persona/fallback render path.
- `Mood display is currently ...`: status/readback contamination.
- `[MOOD] ...` with wrong glyph: swatch mapping problem.
- Correct command confirmation but no ordinary mood line: auto-render path problem.
- Correct `/mood show` but stale word/swatch: payload/state update problem.

### Stop when the diagnosis changes
- If a new screenshot proves a different failure class, stop the current patch direction.
- Restate the new failure seam before writing another file.
- Do not continue patching the layer that was just disproven.

## Category: User Collaboration

### Respect non-coder workflow
- The user can read and reason about specs but does not want to manually patch complex files.
- Provide replacement-ready artifacts.
- Avoid making the user manage line placement, merge conflicts, or architecture surgery.

### Acknowledge cost of churn
- Patch churn can destroy working states.
- Always preserve or identify a baseline before major changes.
- When uncertain, inspect active files rather than asking the user to keep overwriting.

### External review integration
- External fixes from another model/person can be valid source material.
- Translate external fixes into BluCode lessons when they reveal reusable patterns.
- Do not treat external output as final until checked against live files and user constraints.

## Current Mood Lessons Summary

- The hardest Mood bug was not emoji rendering; it was command routing and dispatch.
- `/mood show` must hard-bind to the render entrypoint.
- `/mood show` must not be interpreted as a status readback.
- `/mood show` must force render independent of automatic mood mode.
- Persona must not render public mood prose.
- Exec must freeze the final `[MOOD] <Word> <Swatches>` line literally.
- Swatch modes must use explicit emoji maps.
- Always-mode ordinary turns must run the ordinary auto-render path, not only command render.
- If a command output is correct once but regresses after another state command, check state branch priority and final render freeze.

## Maintenance Rule

When adding new entries:
1. Make the lesson reusable beyond one bug when possible.
2. Name the failure pattern.
3. Record the symptom.
4. Record the cause.
5. Record the prevention rule.
6. Avoid adding private user details.
7. Keep examples minimal and clearly marked as invalid or expected.
