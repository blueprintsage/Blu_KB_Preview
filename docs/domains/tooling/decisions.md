# Tooling Decisions

status: active
owner: docs/domains/tooling
last_reviewed: 2026-08-01

Dated, newest first. A decision belongs here once it would be expensive to
re-litigate. Record the REASON, not just the choice - the reason is what tells a
future reader whether the decision still holds.

## 2026-08-01 - Preflight visual PDFs before source admission

- `tools/preflight_pdf.py` checks the real PDF text layer before hashing. Empty
  or extremely sparse extraction fails as `NEEDS_OCR`; OCR is performed before
  the final SHA-256 enters the registry.
- A visual run additionally requires an explicit vision-capability confirmation
  and either a renderer that successfully produces a decodable CropBox page or a
  contiguous page-image directory/ZIP whose first, middle, and last images
  decode. Executable discovery alone is not readiness.
- Source page images are grounding evidence through `image:` receipt locators,
  including exact ZIP-member locators. They do not relax the requirement to
  inspect the images or generate and review original shippable references.
- Poppler rendering defaults to CropBox because scanner MediaBoxes can contain
  large blank margins that consume visual context without teaching anything.
  `--media-box` remains an explicit escape hatch.

## 2026-07-30 - Fail closed on rendered output and ledger v2 accounting

- `tools/render_pdf.py` accepts a PDF, inclusive page range, and output prefix. A
  renderer is successful only when it exits zero **and** every requested PNG was
  created. The tool rejects pre-existing expected outputs and stops after a
  partial render, so stale or mixed files cannot satisfy visual review.
- A new or revised unit ledger uses `ledger_format: 2` and `candidate_count`.
  The validator checks count-to-row reconciliation. Variant rows record the
  foundation object plus learner decision, variant basis, method or policy, and
  tradeoff in dedicated columns.
- Generated indexes list variants beneath their foundation because an alternative
  method that cannot be found cannot influence a practitioner's choice.
- Legacy v1 ledgers remain readable during incremental migration. The known TCPL
  Chapter 19 mismatch remains visible rather than being rewritten to a false
  reconciled count.

## 2026-07-30 - Validate before recursively generating SkillForge indexes

- **Decided.** `tools/build_index.py` runs the PASS validator before generating
  anything and refuses an invalid library. It writes a root `INDEX.md` and one
  index at every `library_path` directory.
- **Why.** Indexes are navigation authority. Letting a malformed object enter one
  makes a broken card look installed and discoverable, which is the silent failure
  the generated-index rule exists to avoid.
- **Bootstrap.** The root index names
  `AP_plan_and_build_work_from_thumbnail_to_final` first and lists its
  `metaskills` package before optional packages.
- **What this forbids.** Hand-edited `INDEX.md` files, generation against
  unvalidated cards, and fixed-depth assumptions in the generator.

## 2026-07-29 - <decision>

- What was decided.
- Why (the constraint or evidence that forced it).
- What was rejected, and why.
- What this now forbids.
