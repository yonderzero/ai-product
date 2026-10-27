#!/usr/bin/env python3
"""
Deterministic Risk composite calculator — standalone version for the risk-score skill.

Adapted from VMS-Analyzer's scripts/compute_scores.py (--mode risks), stripped of every
other pipeline mode (moat, maturity, combined, threat). This is the only place the 11
Risk dimension scores are turned into the Risk composite — never eyeball this math.

Usage:
  python3 compute_risk_score.py --scores scores.json --output composite.json

Input scores.json shape:
  {
    "company_name": "...",
    "framework_version": "2.0",
    "scored_at": "...",
    "dimensions": {
      "R1": {"score": 3, "evidence_confidence": "High|Medium|Low", "score_basis": "...", "flags": [...]},
      "...": "... all 11 active Risk dimension IDs: R1-R6, R8-R12 (R7 is retired v2.0 — never include it) ..."
    }
  }

Formula (references/risk-framework-spec.md):
  Risk composite = avg(R1, R2, R3, R4, R5, R6, R8, R9, R10, R11, R12), round to 2 decimals.
  Interpretation: LOWER = safer/more protected. HIGHER = more exposed. (Risk score direction
  is the reverse of Maturity — a 5 on any R dimension means severe exposure, not strength.)
  Borderline flag when composite is within 0.1 of the 3.0 threshold (spec §7.0.1's borderline
  rule, applied here even though this skill has no Mode quadrant to classify into — the 3.0
  midpoint is still the natural "meaningfully risky vs. not" reading of the scale).

Exits 0 on success, 1 on error (missing dimension, malformed input).
"""

import argparse
import json
import sys
from pathlib import Path

# The 11 active Risk dimensions. R7 (AI Labor Displacement Risk) is retired as of
# framework v2.0 — it never diverged from C4 in any prior run, so it was dropped and its
# reading folded into C4's dual-lens note in the Maturity framework. Never include R7 here.
RISK_DIMS = [f"R{i}" for i in range(1, 13) if i != 7]


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

    missing = [d for d in RISK_DIMS if d not in dims]
    if missing:
        print(f"ERROR: missing risk dimension scores: {', '.join(missing)}", file=sys.stderr)
        sys.exit(1)

    if "R7" in dims:
        print("WARNING: R7 is present in scores.json but is retired (v2.0) and is ignored in the composite.", file=sys.stderr)

    risk = round(sum(get_score(dims, d) for d in RISK_DIMS) / len(RISK_DIMS), 2)

    low_conf = sorted(d for d, e in dims.items() if d in RISK_DIMS and e.get("evidence_confidence") == "Low")
    inference_heavy = sorted(
        d for d, e in dims.items()
        if d in RISK_DIMS and (e.get("score_basis") == "inference_heavy" or "inference_heavy" in (e.get("flags") or []))
    )

    result = {
        "company_name": data.get("company_name", ""),
        "framework_version": data.get("framework_version", ""),
        "computed_at": data.get("scored_at", ""),
        "risk_composite": risk,
        "all_dimension_scores": {d: int(get_score(dims, d)) for d in RISK_DIMS},
        "low_confidence_dimensions": low_conf,
        "inference_heavy_dimensions": inference_heavy,
    }

    if abs(risk - 3.0) <= 0.1:
        result["borderline_flag"] = True
        result["borderline_note"] = (
            f"Risk composite {risk:.2f} is within 0.1 of the 3.0 threshold — treat this as a "
            "borderline result. Name the dimension(s) that, if they shifted by one point, would "
            "move the composite meaningfully, and note why that matters for how exposed this "
            "company actually is."
        )

    print("Risk composite:")
    print(f"  {risk} / 5.0  (11 dimensions: {', '.join(RISK_DIMS)})")
    if result.get("borderline_flag"):
        print(f"  Borderline: {result['borderline_note']}")
    if low_conf:
        print(f"  Low confidence: {', '.join(low_conf)}")
    if inference_heavy:
        print(f"  Inference-heavy: {', '.join(inference_heavy)}")

    return result


def main():
    parser = argparse.ArgumentParser(description="Compute the Risk composite deterministically (no Maturity, no Mode).")
    parser.add_argument("--scores", required=True, help="Path to scores.json (all 11 active R-dimension scores)")
    parser.add_argument("--output", required=True, help="Output path for composite.json")
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
