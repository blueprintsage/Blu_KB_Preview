from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
import json
import zipfile
from pathlib import Path

import yaml
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from build_index import build_indexes  # noqa: E402
from preflight_pdf import analyze_extracted_text, inspect_page_images  # noqa: E402
from render_pdf import expected_outputs, parse_page_range, render_command, sibling_direct_renderer  # noqa: E402
from validate import validate_ledgers, validate_library  # noqa: E402
from verify_grounding import parse_receipt, verify_visual_locator  # noqa: E402
from verify_references import reference_failures  # noqa: E402


def base_data(object_id: str = "PAT_valid_pattern", name: str = "Validate Library Object") -> dict:
    return {
        "object_id": object_id,
        "object_type": "pattern",
        "name": name,
        "library_path": ["software_development", "class_design"],
        "stage_binding": "1 skeleton",
        "lane_fit": "skill",
        "foundation_role": "foundation",
        "routing_class": "general",
        "specialization_axis": "none",
        "foundation_object_id": "none",
        "tags": ["testing"],
        "cross_links": [],
        "reference": {
            "source_id": "fixture_source",
            "source_title": "Fixture Source",
            "author": "Tester",
            "publish_date": "2026-07-30",
            "media_type": "archive",
            "locator": "u01, fixture",
            "evidence_type": "text",
        },
        "confidence": "high",
        "references": [],
        "variants": [],
    }


def pattern_body(name: str, if_clause: str = "choosing a fixture", then_clause: str = "write the checked result", do: str = "- Record a distinct implementation detail.", notes: str = "The fixture preserves one source-specific constraint.") -> str:
    return f"""# {name}

## Pattern Rule
**IF** {if_clause}
**THEN** {then_clause}
**ELSE** use the fallback fixture

## Do
{do}

## Don't
- Hide the fixture constraint in a generic wrapper.

## Checklist
- The fixture has an observable result.

## Notes
{notes}
"""


class ToolFixture(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = Path(tempfile.mkdtemp())
        self.library = self.temp / "library"
        self.ledger = self.temp / "ledger"
        (self.ledger / "fixture_source").mkdir(parents=True)
        (self.ledger / "fixture_source" / "UNITS.md").write_text(
            "| unit_id | label | locator | status | objects | notes |\n|---|---|---|---|---|---|\n| u01 | Fixture | p. 1 | processed | 0 | |\n",
            encoding="utf-8",
        )

    def make_visual_source(self) -> None:
        (self.ledger / "fixture_source" / "SOURCE.md").write_text("visual: true\n", encoding="utf-8")

    def add_visual_reference(self, data: dict, *, copied: bool = False) -> None:
        image_rel = Path("library", *data["library_path"], "assets", "fixture.png")
        source = self.temp / "source-render.png"
        reference = self.temp / image_rel
        source.parent.mkdir(parents=True, exist_ok=True)
        reference.parent.mkdir(parents=True, exist_ok=True)
        source_image = Image.new("L", (64, 64), 255)
        ImageDraw.Draw(source_image).line((0, 0, 63, 63), fill=0, width=8)
        source_image.save(source)
        if copied:
            shutil.copyfile(source, reference)
        else:
            generated = Image.new("L", (64, 64), 255)
            ImageDraw.Draw(generated).rectangle((16, 8, 48, 56), outline=0, width=8)
            generated.save(reference)
        data["references"] = [{
            "image_path": image_rel.as_posix(), "caption": "Fixture construction image.",
            "derived_from": "u01 p. 1", "origin": "generated", "review": "passed",
        }]
        Path(str(reference) + ".meta.json").write_text(json.dumps({
            "origin": "generated", "generator_model": "fixture-image-model",
            "generated_at": "2026-07-31", "source_renders": ["source-render.png"],
            "review": {"verdict": "passed", "reviewer": "Fixture reviewer", "reviewed_at": "2026-07-31", "method": "human visual inspection"},
        }), encoding="utf-8")

    def tearDown(self) -> None:
        shutil.rmtree(self.temp)

    def write_object(self, data: dict | None = None, body: str | None = None, relative: Path | None = None, raw: str | None = None) -> Path:
        data = data or base_data()
        relative = relative or Path(*data["library_path"]) / f"{data['object_id']}.md"
        path = self.library / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if raw is None:
            body = body or pattern_body(data["name"])
            raw = "---\n" + yaml.safe_dump(data, sort_keys=False) + "---\n\n" + body
        path.write_text(raw, encoding="utf-8")
        return path

    def errors(self) -> list[str]:
        return [error for record in validate_library(self.library, self.ledger) for error in record.errors]

    def ledger_errors(self) -> list[str]:
        return [issue.error for issue in validate_ledgers(self.ledger)]

    def write_v2_ledger(self, candidate_count: int, rows: list[list[str]]) -> None:
        header = "| candidate | type | disposition | object_id | grounding | learner_decision | variant_basis | method_or_policy | tradeoff | note |"
        divider = "|---|---|---|---|---|---|---|---|---|---|"
        table_rows = ["| " + " | ".join(row) + " |" for row in rows]
        unit = self.ledger / "fixture_source" / "units" / "u01.md"
        unit.parent.mkdir(parents=True, exist_ok=True)
        unit.write_text(
            "\n".join(["ledger_format: 2", f"candidate_count: {candidate_count}", "", header, divider, *table_rows, ""]),
            encoding="utf-8",
        )

    def assert_rule(self, number: int) -> None:
        self.assertTrue(any(error.startswith(f"rule {number}:") for error in self.errors()), self.errors())

    def test_valid_fixture_passes_every_rule(self) -> None:
        self.write_object()
        self.assertEqual(self.errors(), [])


    def test_non_object_memcap_documents_are_ignored(self) -> None:
        memcap = self.library / "art" / "drawing" / "memcap" / "MEMCAP_fixture.md"
        memcap.parent.mkdir(parents=True, exist_ok=True)
        memcap.write_text("# Apprenticeship memory, not a PASS object\n", encoding="utf-8")
        self.write_object()
        self.assertEqual(self.errors(), [])

    def test_rule_1_frontmatter(self) -> None:
        self.write_object(raw="# invalid\n")
        self.assert_rule(1)

    def test_rule_2_keys(self) -> None:
        data = base_data(); data.pop("tags")
        self.write_object(data)
        self.assert_rule(2)

    def test_rule_3_reference_shape(self) -> None:
        data = base_data(); data["reference"].pop("author")
        self.write_object(data)
        self.assert_rule(3)

    def test_rule_4_enums_and_path(self) -> None:
        data = base_data(); data["stage_binding"] = "bad stage"
        self.write_object(data)
        self.assert_rule(4)

    def test_rule_5_routing_consistency(self) -> None:
        data = base_data(); data["specialization_axis"] = "language"
        self.write_object(data)
        self.assert_rule(5)

    def test_rule_6_headings(self) -> None:
        data = base_data(); self.write_object(data, pattern_body(data["name"]).replace("## Checklist", "## Check"))
        self.assert_rule(6)

    def test_rule_7_h1(self) -> None:
        data = base_data(); self.write_object(data, pattern_body("Wrong Heading"))
        self.assert_rule(7)

    def test_rule_8_placeholders(self) -> None:
        data = base_data(); self.write_object(data, pattern_body(data["name"]) + "<unfinished>")
        self.assert_rule(8)

    def test_rule_9_filename(self) -> None:
        data = base_data(); self.write_object(data, relative=Path(*data["library_path"]) / "bad.md")
        self.assert_rule(9)

    def test_rule_10_name(self) -> None:
        data = base_data(name="One"); self.write_object(data)
        self.assert_rule(10)

    def test_rule_11_links(self) -> None:
        data = base_data(); data["cross_links"] = [{"rel": "supports", "target_object_id": "PAT_missing"}]
        self.write_object(data)
        self.assert_rule(11)

    def test_rule_12_duplicate_ids(self) -> None:
        data = base_data(); self.write_object(data)
        self.write_object(data, relative=Path("art", "drawing", "PAT_valid_pattern.md"))
        self.assert_rule(12)

    def test_rule_13_processed_unit(self) -> None:
        data = base_data(); data["reference"]["locator"] = "missing, fixture"
        self.write_object(data)
        self.assert_rule(13)

    def test_rule_14_variants(self) -> None:
        data = base_data(); data["variants"] = [{"variant_id": "v1"}]
        self.write_object(data)
        self.assert_rule(14)

    def test_rule_15_shared_sentences(self) -> None:
        for number in range(4):
            data = base_data(f"PAT_shared_{number}", f"Shared Fixture {number}")
            data["library_path"] = ["software_development", f"topic_{number}"]
            self.write_object(data, pattern_body(data["name"], do="- Shared source-specific sentence."))
        self.assert_rule(15)

    def test_rule_16_shared_if(self) -> None:
        for number in range(4):
            data = base_data(f"PAT_if_{number}", f"If Fixture {number}")
            data["library_path"] = ["software_development", f"topic_{number}"]
            self.write_object(data, pattern_body(data["name"], if_clause="the same decision moment"))
        self.assert_rule(16)

    def test_rule_17_recycling(self) -> None:
        data = base_data(); self.write_object(data, pattern_body(data["name"], then_clause="record the unique checked result", do="- Record the unique checked result."))
        self.assert_rule(17)

    def test_rule_18_duplicate_items(self) -> None:
        data = base_data(); body = pattern_body(data["name"]).replace("- The fixture has an observable result.", "- Repeat this item.\n- Repeat this item.")
        self.write_object(data, body)
        self.assert_rule(18)

    def test_rule_19_name_in_body(self) -> None:
        data = base_data(); self.write_object(data, pattern_body(data["name"], notes=f"{data['name']} is repeated here."))
        self.assert_rule(19)

    def test_rule_20_source_dependent_phrase(self) -> None:
        data = base_data(); self.write_object(data, pattern_body(data["name"], notes="See page 4 for the missing action."))
        self.assert_rule(20)

    def test_rule_21_ledger_accounting(self) -> None:
        self.write_v2_ledger(2, [["Candidate", "pattern", "new", "PAT_candidate", "p. 1", "", "", "", "", ""]])
        self.assertTrue(any(error.startswith("rule 21:") for error in self.ledger_errors()), self.ledger_errors())

    def test_rule_22_variant_rationale(self) -> None:
        self.write_v2_ledger(1, [["Candidate", "pattern", "variant", "PAT_foundation", "p. 1", "", "", "", "", ""]])
        self.assertTrue(any(error.startswith("rule 22:") for error in self.ledger_errors()), self.ledger_errors())

    def test_visual_reference_valid_fixture_passes(self) -> None:
        self.make_visual_source()
        data = base_data(); self.add_visual_reference(data)
        path = self.write_object(data)
        record = validate_library(self.library, self.ledger)[0]
        self.assertEqual(record.errors, [])
        self.assertEqual(reference_failures(record, self.library, self.ledger), [])

    def test_visual_reference_missing_image_fails(self) -> None:
        self.make_visual_source()
        data = base_data(); data["references"] = [{"image_path": "library/software_development/class_design/assets/missing.png", "caption": "Missing fixture.", "derived_from": "u01 p. 1", "origin": "generated", "review": "passed"}]
        self.write_object(data)
        self.assert_rule(23)

    def test_visual_reference_reproduced_origin_fails(self) -> None:
        self.make_visual_source()
        data = base_data(); self.add_visual_reference(data); data["references"][0]["origin"] = "reproduced"
        self.write_object(data)
        self.assert_rule(23)

    def test_first_party_reference_without_rights_fails(self) -> None:
        self.make_visual_source()
        data = base_data(); self.add_visual_reference(data); data["references"][0]["origin"] = "first_party_source"
        self.write_object(data)
        self.assert_rule(23)

    def test_visual_reference_pending_review_fails(self) -> None:
        self.make_visual_source()
        data = base_data(); self.add_visual_reference(data); data["references"][0]["review"] = "pending"
        self.write_object(data)
        self.assert_rule(23)

    def test_visual_reference_similarity_gate_fails_copy(self) -> None:
        self.make_visual_source()
        data = base_data(); self.add_visual_reference(data, copied=True)
        self.write_object(data)
        record = validate_library(self.library, self.ledger)[0]
        self.assertTrue(any("suspected reproduction" in issue for issue in reference_failures(record, self.library, self.ledger)))

    def test_valid_v2_ledger_passes(self) -> None:
        self.write_v2_ledger(1, [[
            "Candidate", "pattern", "variant", "PAT_foundation", "p. 1",
            "Choose the fixture route", "method_sequence", "Use the alternate method",
            "Trades speed for a checked result", "",
        ]])
        self.assertEqual(self.ledger_errors(), [])

    def test_render_page_range_and_command(self) -> None:
        self.assertEqual(parse_page_range("44-51"), (44, 51))
        with self.assertRaises(ValueError):
            parse_page_range("51-44")
        command = render_command(Path("pdftoppm"), Path("source.pdf"), 44, 51, Path("out/page"), 150)
        self.assertEqual(command, ["pdftoppm", "-f", "44", "-l", "51", "-png", "-r", "150", "-cropbox", "source.pdf", str(Path("out") / "page")])
        media_command = render_command(
            Path("pdftoppm"), Path("source.pdf"), 1, 1, Path("out/page"), 72, cropbox=False,
        )
        self.assertNotIn("-cropbox", media_command)
        self.assertEqual(expected_outputs(Path("out/page"), 44, 45), [Path("out/page-044.png"), Path("out/page-045.png")])
        wrapper = Path("runtime/dependencies/bin/override/pdftoppm.cmd")
        self.assertEqual(sibling_direct_renderer(wrapper), Path("runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe"))

    def test_pdf_text_preflight_flags_empty_and_accepts_mixed_ocr(self) -> None:
        empty = analyze_extracted_text("\f\f")
        self.assertEqual(empty.status, "none")
        prose = "This is a complete sentence with enough words to establish a usable OCR text layer. " * 3
        mixed = analyze_extracted_text(f"{prose}\f\f\f{prose}\f")
        self.assertEqual(mixed.page_count, 4)
        self.assertEqual(mixed.status, "mixed")
        self.assertEqual(mixed.weak_pages, (2, 3))

    def test_page_image_zip_preflight_checks_alignment_and_decoding(self) -> None:
        archive_path = self.temp / "page images.zip"
        image_dir = self.temp / "page_images"
        image_dir.mkdir()
        for page in range(1, 4):
            Image.new("RGB", (32, 32), (page, page, page)).save(image_dir / f"page_{page:03}.jpg")
        with zipfile.ZipFile(archive_path, "w") as archive:
            for image_path in image_dir.iterdir():
                archive.write(image_path, f"book/{image_path.name}")
        report = inspect_page_images(archive_path, expected_pages=3)
        self.assertTrue(report.ready, report.detail)
        self.assertEqual(report.count, 3)
        self.assertFalse(inspect_page_images(archive_path, expected_pages=4).ready)

    def test_grounding_accepts_direct_and_zipped_page_images_with_spaces(self) -> None:
        image_path = self.temp / "page image 001.png"
        Image.new("RGB", (16, 16), "white").save(image_path)
        relative = image_path.relative_to(self.temp).as_posix()
        self.assertIsNone(verify_visual_locator(self.temp, relative))

        archive_path = self.temp / "source pages.zip"
        with zipfile.ZipFile(archive_path, "w") as archive:
            archive.write(image_path, "pages/page 001.png")
        locator = f"{archive_path.name}::pages/page 001.png"
        self.assertIsNone(verify_visual_locator(self.temp, locator))
        self.assertIn("not found", verify_visual_locator(self.temp, f"{archive_path.name}::pages/missing.png"))

        receipt = self.temp / "u01.md"
        receipt.write_text(
            "## Reading receipt\n\n| page | evidence |\n|---|---|\n"
            f"| 1 | image: {locator} | observed: a blocked figure |\n",
            encoding="utf-8",
        )
        rows = parse_receipt(receipt)
        self.assertEqual(rows[0]["kind"], "image")
        self.assertEqual(rows[0]["locator"], locator)

    def test_index_generation_is_deterministic_and_bootstrapped(self) -> None:
        meta = base_data("AP_plan_and_build_work_from_thumbnail_to_final", "Plan and Build Work From Thumbnail to Final")
        meta.update({"object_type": "ap", "library_path": ["metaskills", "iterative-construction"], "lane_fit": "both", "stage_binding": "0 design"})
        self.write_object(meta, "# Plan and Build Work From Thumbnail to Final\n\n## Objective\nBuild work in stages.\n\n## Steps / Flow\n1. Start small.\n\n## Notes\nThe fixture has a staged workflow.", Path("metaskills", "iterative-construction", "AP_plan_and_build_work_from_thumbnail_to_final.md"))
        data = base_data()
        data["variants"] = [{
            "variant_id": "v1",
            "variant_name": "Fixture Alternative",
            "variant_basis": "method_sequence",
            "source_id": "fixture_source",
            "source_title": "Fixture Source",
            "locator": "u01, fixture",
            "difference_from_foundation": "Uses a distinct fixture method.",
            "when_to_use": "Use when the fixture needs the alternative method.",
            "when_not_to_use": "Do not use when the foundation method is required.",
            "absorbed_from_object_id": "none",
        }]
        self.write_object(data, pattern_body(data["name"], notes="The v1 route uses a different fixture method."))
        self.assertEqual(build_indexes(self.library, self.ledger), 0)
        first = (self.library / "INDEX.md").read_text(encoding="utf-8")
        self.assertEqual(build_indexes(self.library, self.ledger), 0)
        self.assertEqual(first, (self.library / "INDEX.md").read_text(encoding="utf-8"))
        self.assertIn("## Load First", first)
        self.assertTrue((self.library / "software_development" / "class_design" / "INDEX.md").exists())
        index = (self.library / "software_development" / "class_design" / "INDEX.md").read_text(encoding="utf-8")
        self.assertIn("Fixture Alternative", index)


if __name__ == "__main__":
    unittest.main()
