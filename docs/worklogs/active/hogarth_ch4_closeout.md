# Hogarth Chapter 4 Closeout

status: complete
owner: GPT
last_reviewed: 2026-08-03

## Scope

Close the guided PASS run for *Dynamic Figure Drawing*, Chapter 4, printed pp. 105-134, and preserve the later correction that the visual-portability experiment used the wrong test environment.

## Shipped

- one Chapter 4 AP;
- four Chapter 4 Patterns;
- three Chapter 4 Drills;
- one absorbed hand-construction variant;
- Chapter 4 guided memcap;
- ledger unit, source summary, registry count, and generated indexes;
- Stage 2 lock and rollback revisions to the mass-construction card;
- thumbnail/registration and fail-closed visual-edit revisions to the onion-skinning AP;
- matching visual continuity requirements in `AGENTS.md` and both SkillForge adapters;
- tooling environment-correction and next-step records;
- validator correction so non-object `memcap/` documents are not parsed as PASS objects.

## Critical finding — corrected 2026-08-03

The hosted project chat had the SkillForge repository as accessible source material, not as an installed or automatically discovered runtime skill. That environment could generate images without invoking the resolver or loading the selected cards. Consequently, the Chapter 4 render sequence was not a valid test of SkillForge portability, and its drift must not be recorded as a SkillForge failure.

The drift remains a useful observation about that particular hosted image workflow, but it is not evidence about SkillForge. A valid retest must first prove that SkillForge is active and log the selected cards; only then should image-to-image registration be judged as a separate success criterion.

## Validation

Run from the combined repository state after applying the SkillForge discovery overlay:

```bash
python tools/validate.py
python tools/build_index.py
python tools/build_index.py
python -m unittest discover -s tests -v
python tools/verify_grounding.py --source burne_hogarth_dynamic_figure_drawing_ocr
```

The final command requires the source image archives at the locators recorded in the Chapter 4 reading receipt.
