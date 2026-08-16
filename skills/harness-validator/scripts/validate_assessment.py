#!/usr/bin/env python3
"""Validate the portable machine-readable harness assessment format."""

from __future__ import annotations

import json
import sys
from pathlib import Path

APPLICABILITY = {"required", "recommended", "not_applicable"}
EVIDENCE_STATES = {
    "verified_pass",
    "verified_fail",
    "present_unverified",
    "missing",
    "unknown",
}
CONFIDENCE = {"low", "medium", "high"}
EFFORT = {"small", "medium", "large"}
RISK_PROFILES = {"low", "medium", "high", "critical"}
CATEGORY_CHECKS = {
    "intent-knowledge": {f"IK-{number:02d}" for number in range(1, 8)},
    "environment-initialization": {f"EI-{number:02d}" for number in range(1, 9)},
    "security-governance": {f"SG-{number:02d}" for number in range(1, 9)},
    "scope-control": {f"SC-{number:02d}" for number in range(1, 8)},
    "continuity-authority": {f"CA-{number:02d}" for number in range(1, 10)},
    "verification-completion": {f"VC-{number:02d}" for number in range(1, 11)},
    "observability-evaluator": {f"OE-{number:02d}" for number in range(1, 9)},
    "clean-recovery": {f"CR-{number:02d}" for number in range(1, 11)},
    "autonomy-economics": {f"AE-{number:02d}" for number in range(1, 12)},
}
CATEGORY_IDS = set(CATEGORY_CHECKS)
REQUIRED_TOP_LEVEL = {
    "target",
    "risk_profile",
    "evidence_confidence",
    "categories",
    "blockers",
    "conflicts",
    "gaps",
    "over_detailed_controls",
    "recommendations",
    "not_applicable",
    "commands",
}


def validate(data: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["assessment must be a JSON object"]

    missing = sorted(REQUIRED_TOP_LEVEL - data.keys())
    if missing:
        errors.append("missing top-level fields: " + ", ".join(missing))
    if data.get("risk_profile") not in RISK_PROFILES:
        errors.append(f"risk_profile must be one of {sorted(RISK_PROFILES)}")
    if data.get("evidence_confidence") not in CONFIDENCE:
        errors.append(f"evidence_confidence must be one of {sorted(CONFIDENCE)}")
    if not isinstance(data.get("target"), str) or not data.get("target"):
        errors.append("target must be a non-empty string")

    categories = data.get("categories")
    if not isinstance(categories, list) or not categories:
        errors.append("categories must be a non-empty array")
        return errors

    seen_categories: set[str] = set()
    seen_checks: set[str] = set()
    checks_by_category: dict[str, set[str]] = {}
    for category_index, category in enumerate(categories):
        prefix = f"categories[{category_index}]"
        if not isinstance(category, dict):
            errors.append(f"{prefix} must be an object")
            continue
        category_id = category.get("id")
        if not isinstance(category_id, str) or not category_id:
            errors.append(f"{prefix}.id must be a non-empty string")
        elif category_id in seen_categories:
            errors.append(f"duplicate category id: {category_id}")
        else:
            seen_categories.add(category_id)
        if not isinstance(category.get("name"), str) or not category["name"]:
            errors.append(f"{prefix}.name must be a non-empty string")

        checks = category.get("checks")
        if not isinstance(checks, list) or not checks:
            errors.append(f"{prefix}.checks must be a non-empty array")
            continue
        for check_index, check in enumerate(checks):
            cp = f"{prefix}.checks[{check_index}]"
            if not isinstance(check, dict):
                errors.append(f"{cp} must be an object")
                continue
            check_id = check.get("id")
            if not isinstance(check_id, str) or not check_id:
                errors.append(f"{cp}.id must be a non-empty string")
            elif check_id in seen_checks:
                errors.append(f"duplicate check id: {check_id}")
            else:
                seen_checks.add(check_id)
                if isinstance(category_id, str):
                    checks_by_category.setdefault(category_id, set()).add(check_id)
            if check.get("applicability") not in APPLICABILITY:
                errors.append(f"{cp}.applicability must be one of {sorted(APPLICABILITY)}")
            if not isinstance(check.get("applicability_reason"), str) or not check["applicability_reason"]:
                errors.append(f"{cp}.applicability_reason must be non-empty")
            if check.get("evidence_state") not in EVIDENCE_STATES:
                errors.append(f"{cp}.evidence_state must be one of {sorted(EVIDENCE_STATES)}")
            maturity = check.get("maturity")
            if not isinstance(maturity, int) or isinstance(maturity, bool) or not 0 <= maturity <= 4:
                errors.append(f"{cp}.maturity must be an integer from 0 to 4")
            if check.get("confidence") not in CONFIDENCE:
                errors.append(f"{cp}.confidence must be one of {sorted(CONFIDENCE)}")
            if check.get("effort") not in EFFORT:
                errors.append(f"{cp}.effort must be one of {sorted(EFFORT)}")
            risk = check.get("risk")
            if not isinstance(risk, dict):
                errors.append(f"{cp}.risk must be an object")
            else:
                for field in ("impact", "likelihood"):
                    value = risk.get(field)
                    if not isinstance(value, int) or isinstance(value, bool) or not 1 <= value <= 5:
                        errors.append(f"{cp}.risk.{field} must be an integer from 1 to 5")
            evidence = check.get("evidence")
            if not isinstance(evidence, list):
                errors.append(f"{cp}.evidence must be an array")
            elif check.get("evidence_state") in {"verified_pass", "verified_fail", "present_unverified"}:
                if not evidence or not all(isinstance(item, str) and item.strip() for item in evidence):
                    errors.append(f"{cp}.evidence must contain concrete entries for evidenced states")
            recommendation = check.get("recommendation")
            if not isinstance(recommendation, str) or not recommendation.strip():
                errors.append(f"{cp}.recommendation must be non-empty")
            if check.get("applicability") == "not_applicable" and check.get("evidence_state") == "verified_pass":
                errors.append(f"{cp} cannot be verified_pass when not_applicable")

    missing_categories = sorted(CATEGORY_IDS - seen_categories)
    unexpected_categories = sorted(seen_categories - CATEGORY_IDS)
    if missing_categories:
        errors.append("missing canonical categories: " + ", ".join(missing_categories))
    if unexpected_categories:
        errors.append("unexpected category ids: " + ", ".join(unexpected_categories))
    for category_id, expected_checks in CATEGORY_CHECKS.items():
        actual_checks = checks_by_category.get(category_id, set())
        missing_checks = sorted(expected_checks - actual_checks)
        unexpected_checks = sorted(actual_checks - expected_checks)
        if missing_checks:
            errors.append(f"{category_id} missing canonical checks: " + ", ".join(missing_checks))
        if unexpected_checks:
            errors.append(f"{category_id} has unexpected checks: " + ", ".join(unexpected_checks))

    for field in (
        "blockers",
        "conflicts",
        "gaps",
        "over_detailed_controls",
        "recommendations",
        "not_applicable",
        "commands",
    ):
        if field in data and not isinstance(data[field], list):
            errors.append(f"{field} must be an array")

    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_assessment.py <assessment.json>", file=sys.stderr)
        return 2
    path = Path(argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1
    errors = validate(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    check_count = sum(len(category["checks"]) for category in data["categories"])
    print(f"VALID: {len(data['categories'])} categories, {check_count} checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
