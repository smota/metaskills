#!/usr/bin/env python3
"""Run deterministic contract evals for the harness-validator skill package."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def run(skill_root: Path) -> dict[str, object]:
    cases_path = skill_root / "evals" / "cases.json"
    data = json.loads(cases_path.read_text(encoding="utf-8"))
    fixture_outputs = json.loads(
        (skill_root / "evals" / "fixture-outputs.json").read_text(encoding="utf-8")
    )
    corpus = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (
            skill_root / "SKILL.md",
            skill_root / "checklists" / "harness-assessment.md",
            skill_root / "references" / "lecture-traceability.md",
            skill_root / "templates" / "assessment.json",
            skill_root / "templates" / "harness-validation-report.md",
        )
    ).lower()
    results: list[dict[str, object]] = []
    seen: set[str] = set()
    for index, case in enumerate(data.get("cases", [])):
        errors: list[str] = []
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id:
            errors.append("id must be non-empty")
            case_id = f"case-{index}"
        elif case_id in seen:
            errors.append("id must be unique")
        seen.add(case_id)
        for field in ("prompt",):
            if not isinstance(case.get(field), str) or not case[field].strip():
                errors.append(f"{field} must be non-empty")
        for field in ("expected", "must_not", "contract_terms"):
            values = case.get(field)
            if not isinstance(values, list) or not values or not all(isinstance(v, str) and v.strip() for v in values):
                errors.append(f"{field} must be a non-empty string array")
        for term in case.get("contract_terms", []):
            if isinstance(term, str) and term.lower() not in corpus:
                errors.append(f"contract term not found in skill assets: {term}")
        output = fixture_outputs.get(case_id)
        if not isinstance(output, str) or not output.strip():
            errors.append("fixture-backed output is missing")
            output = ""
        lowered_output = output.lower()
        for expected in case.get("expected", []):
            if isinstance(expected, str) and expected.lower() not in lowered_output:
                errors.append(f"expected behavior missing from fixture output: {expected}")
        for prohibited in case.get("must_not", []):
            if isinstance(prohibited, str) and prohibited.lower() in lowered_output:
                errors.append(f"prohibited behavior present in fixture output: {prohibited}")
        results.append({"id": case_id, "passed": not errors, "errors": errors})
    if len(results) < 7:
        results.append({"id": "suite-size", "passed": False, "errors": ["at least seven eval cases are required"]})
    return {
        "skill": data.get("skill"),
        "evaluation_mode": "fixture-backed behavioral contract",
        "passed": all(result["passed"] for result in results),
        "case_count": len(results),
        "results": results,
    }


def main(argv: list[str]) -> int:
    root = Path(argv[1]) if len(argv) == 2 else Path(__file__).resolve().parents[1]
    try:
        result = run(root)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"EVAL ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
