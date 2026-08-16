import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "harness-validator"
VALIDATOR = SKILL / "scripts" / "validate_assessment.py"
EVAL_RUNNER = SKILL / "scripts" / "run_evals.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_assessment", VALIDATOR)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


class HarnessValidatorPackageTest(unittest.TestCase):
    def test_required_package_files_exist(self):
        required = [
            "SKILL.md",
            "README.md",
            "checklists/harness-assessment.md",
            "references/lecture-traceability.md",
            "templates/harness-validation-report.md",
            "templates/assessment.json",
            "scripts/new_assessment.py",
            "scripts/validate_assessment.py",
            "scripts/run_evals.py",
            "evals/cases.json",
            "evals/fixture-outputs.json",
        ]
        for relative in required:
            self.assertTrue((SKILL / relative).is_file(), relative)

    def test_skill_is_explicitly_read_only_and_evidence_first(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("read-only", text.lower())
        self.assertIn("evidence-first", text.lower())
        self.assertIn("Do not edit", text)
        self.assertIn("not_applicable", text)
        self.assertIn("Never average away", text)

    def test_checklist_has_all_nine_categories_and_cross_review(self):
        text = (SKILL / "checklists" / "harness-assessment.md").read_text(encoding="utf-8")
        headings = [line for line in text.splitlines() if line.startswith("## ")]
        numbered = [line for line in headings if line[3:4].isdigit()]
        self.assertEqual(9, len(numbered))
        for number in range(1, 10):
            self.assertTrue(any(line.startswith(f"## {number}.") for line in numbered))
        self.assertIn("## Cross-category review", text)

    def test_traceability_covers_all_fourteen_lectures(self):
        text = (SKILL / "references" / "lecture-traceability.md").read_text(encoding="utf-8")
        for number in range(1, 15):
            self.assertIn(f"| {number:02d}.", text)
        self.assertIn("Tensions the validator must surface", text)
        self.assertIn("Course gaps extended by this skill", text)
        self.assertIn("Heuristics, not mandates", text)

    def test_report_template_contains_required_sections(self):
        text = (SKILL / "templates" / "harness-validation-report.md").read_text(encoding="utf-8")
        for heading in (
            "## Executive verdict",
            "## Applicability profile",
            "## Maturity by category",
            "## Findings",
            "## Conflicts and contradictions",
            "## Missing capabilities",
            "## Redundant or over-detailed controls",
            "## Stale or unverified evidence",
            "## Prioritized improvement sequence",
            "## Not-applicable checks",
            "## Commands and evidence provenance",
        ):
            self.assertIn(heading, text)

    def test_eval_cases_cover_activation_boundaries_and_output(self):
        data = json.loads((SKILL / "evals" / "cases.json").read_text(encoding="utf-8"))
        ids = {case["id"] for case in data["cases"]}
        self.assertGreaterEqual(len(ids), 7)
        self.assertTrue(
            {
                "activation-harness-audit",
                "small-project-applicability",
                "cross-component-verification",
                "conflicting-state-authority",
                "unsafe-autonomous-loop",
                "over-detailed-instructions",
                "structured-output-validation",
            }.issubset(ids)
        )
        for case in data["cases"]:
            for field in ("expected", "must_not", "contract_terms"):
                self.assertTrue(case[field], f"{case['id']} missing {field}")

        run = subprocess.run(
            [sys.executable, str(EVAL_RUNNER), str(SKILL)],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(0, run.returncode, run.stdout + run.stderr)
        result = json.loads(run.stdout)
        self.assertTrue(result["passed"])
        self.assertGreaterEqual(result["case_count"], 7)

    def test_catalog_documents_skill(self):
        root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
        concepts = (ROOT / "docs" / "concepts" / "skills.md").read_text(encoding="utf-8")
        self.assertIn("--skill harness-validator", root_readme)
        self.assertIn("harness-validator", concepts)


class AssessmentValidatorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validator = load_validator()

    def test_template_is_valid(self):
        data = json.loads((SKILL / "templates" / "assessment.json").read_text(encoding="utf-8"))
        self.assertEqual([], self.validator.validate(data))
        self.assertEqual(78, sum(len(category["checks"]) for category in data["categories"]))

    def test_rejects_missing_canonical_category(self):
        data = json.loads((SKILL / "templates" / "assessment.json").read_text(encoding="utf-8"))
        data["categories"].pop()
        errors = self.validator.validate(data)
        self.assertTrue(any("missing canonical categories" in error for error in errors))

    def test_rejects_missing_or_arbitrary_canonical_check(self):
        data = json.loads((SKILL / "templates" / "assessment.json").read_text(encoding="utf-8"))
        data["categories"][0]["checks"].pop()
        data["categories"][1]["checks"][0]["id"] = "ARBITRARY"
        errors = self.validator.validate(data)
        self.assertTrue(any("missing canonical checks" in error for error in errors))
        self.assertTrue(any("unexpected checks" in error for error in errors))

    def test_rejects_evidenced_state_without_concrete_evidence(self):
        data = json.loads((SKILL / "templates" / "assessment.json").read_text(encoding="utf-8"))
        check = data["categories"][0]["checks"][0]
        check["evidence_state"] = "verified_pass"
        errors = self.validator.validate(data)
        self.assertTrue(any("concrete entries" in error for error in errors))

    def test_rejects_invalid_states_and_ranges(self):
        data = json.loads((SKILL / "templates" / "assessment.json").read_text(encoding="utf-8"))
        check = data["categories"][0]["checks"][0]
        check["applicability"] = "sometimes"
        check["evidence_state"] = "looks_good"
        check["maturity"] = 5
        check["risk"]["impact"] = 0
        errors = self.validator.validate(data)
        self.assertTrue(any("applicability" in error for error in errors))
        self.assertTrue(any("evidence_state" in error for error in errors))
        self.assertTrue(any("maturity" in error for error in errors))
        self.assertTrue(any("risk.impact" in error for error in errors))

    def test_rejects_not_applicable_verified_pass(self):
        data = json.loads((SKILL / "templates" / "assessment.json").read_text(encoding="utf-8"))
        check = data["categories"][0]["checks"][0]
        check["applicability"] = "not_applicable"
        check["evidence_state"] = "verified_pass"
        errors = self.validator.validate(data)
        self.assertTrue(any("cannot be verified_pass" in error for error in errors))

    def test_cli_exit_codes(self):
        valid = SKILL / "templates" / "assessment.json"
        valid_run = subprocess.run(
            [sys.executable, str(VALIDATOR), str(valid)],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(0, valid_run.returncode, valid_run.stderr)
        self.assertIn("VALID:", valid_run.stdout)

        with tempfile.TemporaryDirectory() as directory:
            invalid = Path(directory) / "invalid.json"
            invalid.write_text("{}", encoding="utf-8")
            invalid_run = subprocess.run(
                [sys.executable, str(VALIDATOR), str(invalid)],
                text=True,
                capture_output=True,
                check=False,
            )
        self.assertEqual(1, invalid_run.returncode)
        self.assertIn("ERROR:", invalid_run.stderr)


if __name__ == "__main__":
    unittest.main()
