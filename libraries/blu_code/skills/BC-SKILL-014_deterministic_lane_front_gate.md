# BC-SKILL-014 — Deterministic Lane Front Gate

## Trigger
Use when modifying, debugging, or executing any Blu kernel path where an elastic prose answer could masquerade as completion.

Common triggers:
- artifact creation or export
- repo/index mutation
- BluCode skill export
- command execution
- Program or ExecLib routing
- PASS/SIMCODE-style structured output
- tests, verification, or runtime proof claims
- memory import/export state changes

## Failure Pattern
A deterministic task is understood semantically but not route-locked. The model then emits plausible prose, YAML, partial instructions, or a success-shaped answer instead of entering the required execution lane and producing the required artifact, patch, state delta, or terminal packet.

## Do
1. Classify the turn before composing ordinary prose.
2. If the task requires exact source truth, mutation, validation, command routing, state change, or artifact output, lock the deterministic lane.
3. Bind the lane to one owner and one source/contract.
4. Disable conversational fallback after deterministic ownership is assigned.
5. Require source lookup before assigning IDs, file paths, command status, or repo/index mutations.
6. Require artifact proof before claiming export, creation, patching, or delivery.
7. Require a terminal packet or equivalent validation record before printing deterministic output.
8. Fail closed if the required source, owner, artifact, or validation proof is unavailable.

## Do Not
- Do not treat deterministic work as a writing prompt.
- Do not output skill cards, patches, manifests, or exports as prose when the user requested an archive or repo-shaped artifact.
- Do not infer the next ID from memory or naming pattern.
- Do not accept routed success text as runtime proof.
- Do not let Persona warmth, source-grounded prose, or ordinary explanation complete a deterministic lane.
- Do not continue after a deterministic route is recognized unless the required output contract can be satisfied.

## Validation
- The task is classified as elastic or deterministic before output.
- Deterministic tasks have an owner, source/contract, executed action, validation result, and terminal state.
- Required source/index lookup occurs before ID assignment or mutation.
- Artifact requests produce a real downloadable file before completion is claimed.
- Mutation requests include the changed file(s) and index/manifest updates when required.
- No conversational substitute appears in place of the deterministic output.
- If proof is missing, the output is a failure/blocker, not a completion claim.

## Example
Bad:
`export this for BluCode` returns a Markdown skill card in chat.

Good:
`export this for BluCode` routes to the BluCode artifact lane, reads the current index and an existing skill-card exemplar, assigns the next valid ID from source, writes `skills/BC-SKILL-###_<slug>.md`, updates `INDEX.md`, packages the update archive, verifies the archive exists, and returns the download link.
