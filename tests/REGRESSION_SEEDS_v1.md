# REGRESSION_SEEDS_v1
version: v1
updated: 2026-02-28
notes:
  - Fixed regression seeds (10 per domain): ART, SCHOOL, TEACH, SKILLFORGE, EXEC
  - Seeds are written to be deterministic: explicit constraints + verifiable output structure
  - If a seed fails: patch + add/adjust a SMOKE + (if relevant) add a new regression seed

---

## ART (10)

### ART-01
**Prompt:** Write a 12-line micro-poem about **scope lock**.  
**Constraints:**  
- Exactly 12 lines  
- Lines **1**, **6**, and **12** must end with the word **“today”**  
- **No rhymes** (avoid end-rhyme patterns)  
- Include **one** duck reference (duck/ducks/duckling)  
**Expected:** 12 lines; line endings match; duck reference present; tone/artistic OK.

### ART-02
**Prompt:** Generate a **6-panel comic script** (no images).  
**Constraints:** Each panel must include:  
- **Setting:** (1 short sentence)  
- **Action:** (1 short sentence)  
- **Dialogue:** (≤12 words)  
**Theme:** Using a **parking lot** for deferred ideas.  
**Expected:** Exactly 6 panels; each panel has the 3 fields; dialogue word count compliant.

### ART-03
**Prompt:** Create **3 distinct logo concepts** described in text for **“Blu v0.8.2”**.  
**Constraints (each concept):**  
- Shape language (e.g., geometric/organic)  
- Palette described in **words only** (no hex codes)  
- Usage notes (where it works / doesn’t)  
**Expected:** 3 clearly distinct concepts; no hex codes; each has all fields.

### ART-04
**Prompt:** Write a short scene (≤220 words) in a **warm tone** where a mentor says **“No drift”** without sounding harsh.  
**Constraints:** Include **one tactile detail** (texture/temperature/weight).  
**Expected:** ≤220 words; phrase appears; warm tone; tactile detail present.

### ART-05
**Prompt:** Turn the phrase **“RC is stable, not bug-free”** into **5 tagline options**.  
**Constraints:** Each tagline ≤7 words.  
**Expected:** 5 lines; each ≤7 words; meaning preserved.

### ART-06
**Prompt:** Write (1) a **haiku** and (2) a **limerick** about **burn-in tests** (separate).  
**Constraints:**  
- No profanity  
- Both should be faithful to the concept (pre-release validation)  
**Expected:** Haiku is 3 lines; limerick is 5 lines; both mention burn-in/testing meaningfully.

### ART-07
**Prompt:** Describe a **poster layout** for **“Release Day Checklist”**.  
**Constraints:** Include sections + typography hierarchy; **no brand names**.  
**Expected:** Clear layout guidance; hierarchy (H1/H2/body etc.); no brand names.

### ART-08
**Prompt:** Rewrite this in **3 tones** (friendly, firm, playful): **“That’s out of scope for this release.”**  
**Constraints:** Each ≤25 words.  
**Expected:** 3 rewrites labeled or clearly separated; tone differences; ≤25 words each.

### ART-09
**Prompt:** Create **10 metaphors** for **scope lock**.  
**Constraints:**  
- Each is 1 sentence  
- Each uses a different domain (e.g., sailing, cooking, construction, music, etc.)  
**Expected:** 10 one-sentence metaphors; domain variety.

### ART-10
**Prompt:** Write a **90-second** spoken-word script announcing the **v0.8.2 release**.  
**Constraints:** Must mention:  
- RC gate (**TAGS + SMOKES**)  
- Regression seeds  
- Parking lot  
**Expected:** Contains all required mentions; spoken cadence; ~90s length.

---

## SCHOOL (10)

### SCHOOL-01
**Prompt:** Explain **“regression test”** to a **10-year-old** using an everyday analogy; then explain it to a **senior engineer**.  
**Constraints:** Exactly 2 paragraphs total (kid first, engineer second).  
**Expected:** 2 paragraphs; audience-appropriate; concept correct.

### SCHOOL-02
**Prompt:** Make a **10-question** multiple-choice quiz on **Preview → RC → Release** lifecycle.  
**Constraints:** Include **answer key**.  
**Expected:** 10 MCQs; clear options; answer key included.

### SCHOOL-03
**Prompt:** Teach **scope lock** with:  
- Definition  
- 3 examples  
- 3 non-examples  
- 5-question self-check  
**Expected:** All sections present; examples/non-examples clearly differentiated; self-check has 5 Qs.

### SCHOOL-04
**Prompt:** Create a **20-minute lesson plan** on **why changelogs matter**.  
**Constraints:** Objectives, materials, agenda, assessment.  
**Expected:** All fields present; feasible 20-minute structure.

### SCHOOL-05
**Prompt:** Explain **TAGS vs SMOKES** in test gating using:  
- A simple table  
- 2 short case studies  
**Expected:** Table included; 2 cases; distinction correct.

### SCHOOL-06
**Prompt:** Make **15 flashcards (Q/A)** for release terms (include: RC, burn-in, smoke test, regression seed, scope lock, parking lot).  
**Expected:** 15 Q/A pairs; terms covered.

### SCHOOL-07
**Prompt:** Write **8** “common misconceptions” about release management.  
**Constraints:** Each bullet includes misconception + correction.  
**Expected:** 8 bullets; each has correction; accurate.

### SCHOOL-08
**Prompt:** Create a rubric for whether an RC **“meets spec + stable + passes gates.”**  
**Constraints:** 4 criteria, 4 performance levels.  
**Expected:** 4x4 rubric; clear descriptors.

### SCHOOL-09
**Prompt:** Design **3 practice scenarios** where students choose: **hotfix** vs **defer to parking lot**.  
**Constraints:** Include the correct choice + brief rationale.  
**Expected:** 3 scenarios; answers and rationales included.

### SCHOOL-10
**Prompt:** Summarize the difference between **Unreleased** vs **Released** changelog entries.  
**Constraints:** Include 2 examples each.  
**Expected:** Clear distinction; 4 examples total.

---

## TEACH (10)

### TEACH-01
**Prompt:** Create a Socratic sequence: **12 questions** leading a learner to derive why **“stable ≠ bug-free”** for RCs.  
**Expected:** 12 numbered questions; progression builds logically.

### TEACH-02
**Prompt:** Give feedback on this student statement: **“If smokes pass, release is safe.”**  
**Constraints:** Gentle tone + correction + 3 next steps.  
**Expected:** Feedback + correction + exactly 3 next steps.

### TEACH-03
**Prompt:** Mini-workshop script (facilitator notes) for defining **“done”** under **scope lock**.  
**Constraints:** Agenda + prompts + expected outputs.  
**Expected:** Workshop-ready outline with outputs.

### TEACH-04
**Prompt:** Generate **5 analogies** for a **parking lot** that avoid shame/blame language.  
**Expected:** 5 analogies; respectful tone.

### TEACH-05
**Prompt:** Turn “writing a changelog entry” into an **I-do / We-do / You-do** activity.  
**Constraints:** Include example text in I-do and We-do.  
**Expected:** Clear three-phase structure; examples included.

### TEACH-06
**Prompt:** Checklist for coaching someone who keeps **scope-creeping**.  
**Constraints:** 8 steps; warm tone; action-oriented.  
**Expected:** 8 numbered steps.

### TEACH-07
**Prompt:** Write **3 reflective prompts** to diagnose why a **burn-in failed** and what to do next.  
**Expected:** 3 prompts; practical.

### TEACH-08
**Prompt:** Create a peer-review guide for **SIM_REPORT** completeness.  
**Constraints:** Sections checklist + evidence expectations + pass/fail clarity.  
**Expected:** Guide includes all parts.

### TEACH-09
**Prompt:** Create **6 micro-drills** to practice writing deterministic regression seeds from bugs.  
**Expected:** 6 drills; each includes task + success criteria.

### TEACH-10
**Prompt:** Draft a short **release retro** facilitation plan.  
**Constraints:** Questions, timing, outputs (including new seeds/smokes).  
**Expected:** Timed agenda; outputs specified.

---

## SKILLFORGE (10)

### SKILL-01
**Prompt:** Given: **“RC gate requires TAGS+SMOKES”**, draft **5 acceptance tests** in **Gherkin**.  
**Expected:** 5 scenarios; consistent Given/When/Then; references TAGS+SMOKES.

### SKILL-02
**Prompt:** Convert an ambiguous prompt into a deterministic regression seed.  
**Constraints:** Show **Before**, **After**, and **3 reasoning bullets**.  
**Expected:** Clear before/after; 3 bullets exactly.

### SKILL-03
**Prompt:** Design a naming convention for seeds/smokes.  
**Constraints:** IDs, domains, date tags; provide 6 examples.  
**Expected:** Convention described; 6 examples.

### SKILL-04
**Prompt:** Create a “prompt lint” checklist that reduces drift.  
**Constraints:** 10 rules + 3 anti-patterns.  
**Expected:** 10 + 3 lists; actionable.

### SKILL-05
**Prompt:** Write a template for a smoke test: Preconditions, Steps, Expected outputs, Failure logging.  
**Expected:** Template headings; usable format.

### SKILL-06
**Prompt:** Produce a tiny triage matrix for failures: severity × reproducibility × scope impact.  
**Expected:** Matrix/table plus brief how-to-use notes.

### SKILL-07
**Prompt:** Given a failed seed, propose:  
- Patch note (1–2 bullets)  
- A new smoke to prevent recurrence  
**Expected:** Patch bullets + smoke definition.

### SKILL-08
**Prompt:** Write a deterministic doc patch plan: files touched, edits, validation steps.  
**Expected:** Structured plan with validation.

### SKILL-09
**Prompt:** Create an RC readiness checklist mapping artifacts → gates → evidence required.  
**Expected:** Mapping table/list; evidence explicit.

### SKILL-10
**Prompt:** Generate a SIM_REPORT skeleton + show a filled example for a hypothetical single failure.  
**Expected:** Skeleton + example; failure clearly documented.

---

## EXEC (10)

### EXEC-01
**Prompt:** Produce a one-page release runbook for **v0.8.2** with numbered steps and explicit **go/no-go** points.  
**Expected:** Numbered runbook; go/no-go checkpoints.

### EXEC-02
**Prompt:** Draft a changelog entry for **v0.8.2** dated **2026-02-28**.  
**Constraints:** Highlights + note that **Scope Lock + Parking Lot** is included.  
**Expected:** Changelog-ready text; includes required note.

### EXEC-03
**Prompt:** Create a release announcement for internal stakeholders: what changed, gates passed, known issues policy.  
**Expected:** Message format; includes gates and policy.

### EXEC-04
**Prompt:** Given 3 plausible failures (invent them), write a decision memo: ship/hold, rationale, mitigations.  
**Expected:** Memo includes decision + rationale + mitigations; 3 failures described.

### EXEC-05
**Prompt:** Checklist for Publish step: promote build, tag repo, start new Unreleased, attach SIM_REPORT.  
**Expected:** Checklist includes all items; ordered.

### EXEC-06
**Prompt:** Lightweight risk register for release day: 6 risks + mitigations + owners (roles only).  
**Expected:** 6 entries; owners are roles (no names).

### EXEC-07
**Prompt:** Parking lot triage template: item, impact, effort, defer reason, target cycle.  
**Expected:** Template with fields + example row.

### EXEC-08
**Prompt:** Comms plan if a regression escapes post-release: timeline, actions, artifacts to update.  
**Expected:** Timeline + actions + artifacts list.

### EXEC-09
**Prompt:** Draft “release gates definition” docs section: RC definition + TAGS+SMOKES + evidence.  
**Expected:** Clean docs section; includes evidence requirements.

### EXEC-10
**Prompt:** Audit trail checklist: what to archive (SIM_REPORT, seed results, diff summaries) and where.  
**Expected:** Checklist of artifacts + storage locations/labels.

---

## ART — Regression seeds (PASS:GUT)
- seed=84001 tag=art_pass_gut pdf=hands_small expected=GUT+DRILLS+REPPLAN
