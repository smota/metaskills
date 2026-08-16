#!/usr/bin/env python3
"""Generate a complete blank assessment from the canonical Markdown checklist."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

CATEGORY_META = {
    1: ("intent-knowledge", "IK"),
    2: ("environment-initialization", "EI"),
    3: ("security-governance", "SG"),
    4: ("scope-control", "SC"),
    5: ("continuity-authority", "CA"),
    6: ("verification-completion", "VC"),
    7: ("observability-evaluator", "OE"),
    8: ("clean-recovery", "CR"),
    9: ("autonomy-economics", "AE"),
}


def build(skill_root: Path) -> dict[str, object]:
    checklist = skill_root / "checklists" / "harness-assessment.md"
    categories: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    for line in checklist.read_text(encoding="utf-8").splitlines():
        heading = re.match(r"## ([1-9])\. (.+)", line)
        if heading:
            number = int(heading.group(1))
            category_id, check_prefix = CATEGORY_META[number]
            current = {
                "id": category_id,
                "name": heading.group(2),
                "prefix": check_prefix,
                "checks": [],
            }
            categories.append(current)
            continue
        if line.startswith("## "):
            current = None
            continue
        item = re.match(r"- \[ \] (.+)", line)
        if item and current is not None:
            checks = current["checks"]
            assert isinstance(checks, list)
            check_id = f"{current['prefix']}-{len(checks) + 1:02d}"
            checks.append(
                {
                    "id": check_id,
                    "description": item.group(1),
                    "applicability": "recommended",
                    "applicability_reason": "Confirm applicability from project risk and context.",
                    "evidence_state": "unknown",
                    "maturity": 0,
                    "confidence": "low",
                    "risk": {"impact": 3, "likelihood": 3},
                    "effort": "small",
                    "evidence": [],
                    "recommendation": "Assess this capability and implement the smallest effective improvement if needed.",
                    "exception": None,
                }
            )
    for category in categories:
        category.pop("prefix")
    return {
        "target": "path-or-repository",
        "commit": None,
        "environment": None,
        "risk_profile": "medium",
        "evidence_confidence": "low",
        "categories": categories,
        "blockers": [],
        "conflicts": [],
        "gaps": [],
        "over_detailed_controls": [],
        "recommendations": [],
        "not_applicable": [],
        "commands": [],
    }


def main(argv: list[str]) -> int:
    skill_root = Path(__file__).resolve().parents[1]
    output = Path(argv[1]) if len(argv) == 2 else skill_root / "templates" / "assessment.json"
    output.write_text(json.dumps(build(skill_root), indent=2) + "\n", encoding="utf-8")
    print(f"WROTE: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
