#!/usr/bin/env python3
"""
Deterministic Maturity composite calculator — standalone version for the maturity-score skill.

Adapted from VMS-Analyzer's scripts/compute_scores.py (`compute_maturity()`), stripped of every
other pipeline mode (no Risk, no Mode quadrant — see references/maturity-framework-spec.md §5 for
why Mode is out of scope for a standalone skill). This is the only place dimension scores are
turned into section scores and the Maturity composite — never eyeball this math.

Usage:
  python3 compute_maturity_score.py --scores scores.json --output composites.json

Input scores.json shape:
  {
    "company_name": "...",
    "framework_version": "2.0",
    "scored_at": "...",
    "dimensions": {
      "A1": {"score": 3, "evidence_confidence": "High", "score_basis": "direct_evidence", "flags": []},
      "...": "... all 12 active dimension IDs: A1-A6, B1, B3, C1-C4 (no B2 — retired v2.0) ..."
    }
  }

Formulas (references/maturity-framework-spec.md §3):
  Section A avg = (A1+A2+A3+A4+A5+A6) / 6, 2 dp.
  Section B avg = (B1+B3) / 2, 2 dp.                 # B2 retired v2.0 — never scored
  Section C avg = (C1+C2+C3+C4) / 4, 2 dp.
  Maturity composite = (A * 0.40) + (B * 0.35) + (C * 0.25), 2 dp.
  Borderline flag when composite is within 0.1 of the 3.0 reference threshold.

Exits 0 on success, 1 on error (missing dimension, malformed input).
"""

import argparse
import json
import sys
from pathlib import Path

ASSESSMENT_SECTIONS = {
    "A": ["A1", "A2", "A3", "A4", "A5", "A6"],
    "B": ["B1", "B3"],  # B2 retired (framework v2.0) — never scored
    "C": ["C1", "C2", "C3", "C4"],
}
MATURITY_DIMS = ["A1", "A2", "A3", "A4", "A5", "A6", "B1", "B3", "C1", "C2", "C3", "C4"]
MATURITY_WEIGHTS = {"A": 0.40, "B": 0.35, "C": 0.25}


def load_scores(path: str) -> dict:
    p = Path(path)
    if not p.exists():
        print(f"ERROR: scores file not found: {p}", file=sys.stderr)
        sys.exit(1)
    try:
        with open(p) as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: scores file is not valid JSON: {e}", file=sys.stderr)
        sys.exit(1)


def get_score(dims: dict, key: str) -> float:
    entry = dims.get(key, {})
    try:
        return float(entry.get("score", 0))
    except (TypeError, ValueError):
        return 0.0


def compute(data: dict) -> dict:
    dims = data.get("dimensions", {})
    if not dims:
        print("ERROR: scores.json contains no 'dimensions' object", file=sys.stderr)
        sys.exit(1)

    missing = [d for d in MATURITY_DIMS if d not in dims]
    if missing:
        print(f"ERROR: missing dimension scores: {', '.join(missing)}", file=sys.stderr)
        sys.exit(1)

    section_scores = {
        name: round(sum(get_score(dims, d) for d in members) / len(members), 2)
        for name, members in ASSESSMENT_SECTIONS.items()
    }
    maturity = round(sum(section_scores[s] * w for s, w in MATURITY_WEIGHTS.items()), 2)

    low_conf = sorted(d for d, e in dims.items() if d in MATURITY_DIMS and e.get("evidence_confidence") == "Low")
    inference_heavy = sorted(
        d for d, e in dims.items()
        if d in MATURITY_DIMS and (e.get("score_basis") == "inference_heavy" or "inference_heavy" in (e.get("flags") or []))
    )

    result = {
        "company_name": data.get("company_name", ""),
        "framework_version": data.get("framework_version", ""),
        "computed_at": data.get("scored_at", ""),
        "section_scores": section_scores,
        "maturity_composite": maturity,
        "all_dimension_scores": {d: int(get_score(dims, d)) for d in MATURITY_DIMS},
        "low_confidence_dimensions": low_conf,
        "inference_heavy_dimensions": inference_heavy,
    }

    notes = []
    if abs(maturity - 3.0) <= 0.1:
        notes.append(
            f"Maturity composite {maturity:.2f} is within 0.1 of the 3.0 reference threshold — "
            "borderline; note this explicitly in the report rather than treating it as a clean read."
        )
    if notes:
        result["borderline_flag"] = True
        result["borderline_note"] = " ".join(notes)

    print("Maturity composites:")
    print(f"  Sections: A={section_scores['A']} B={section_scores['B']} C={section_scores['C']}")
    print(f"  Maturity composite: {maturity}")
    if notes:
        print(f"  Flag: borderline — {result['borderline_note']}")
    return result


def main():
    parser = argparse.ArgumentParser(description="Compute the Maturity composite deterministically.")
    parser.add_argument("--scores", required=True, help="Path to scores.json (all 12 active dimension scores)")
    parser.add_argument("--output", required=True, help="Output path for composites.json")
    args = parser.parse_args()

    data = load_scores(args.scores)
    result = compute(data)

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"  Written: {out}")


if __name__ == "__main__":
    main()
