#!/usr/bin/env python3
"""
Deterministic MOAT composite calculator — standalone version for the moat-scan skill.

Adapted from VMS-Analyzer's scripts/compute_scores.py (--mode moat), stripped of every
other pipeline mode. This is the only place lever scores are turned into pillar scores,
the MOAT composite, the exposure ratio, and the mode letter — never eyeball this math.

Usage:
  python3 compute_moat_score.py --scores scores.json --output composites.json

Input scores.json shape:
  {
    "company_name": "...",
    "framework_version": "1.0",
    "scored_at": "...",
    "levers": {
      "SC1": {"score": 3, ...}, "SC2": {...}, ... all 24 lever IDs ...
    }
  }

Formulas (references/moat-framework-spec.md §4-5):
  Pillar score = avg of lever scores in that pillar, 1 dp.
  Pillar exposure ratio = (count ai_exposed * 1.0 + count partial * 0.5) / lever count, 2 dp.
  MOAT composite = avg(SC, DK, DS, DC) pillar scores, 2 dp.
  Overall exposure ratio = avg of the four pillar exposure ratios, 2 dp.
  Mode: F if composite>=3.5 & exposure<=0.35 | R if composite>=3.5 & exposure<=0.60
        | V if composite<2.5 or exposure>0.65 | T otherwise.
  Boundary flag when composite is within 0.03 of 3.5/2.5, or exposure within 0.03 of 0.35/0.60/0.65.

Exits 0 on success, 1 on error (missing lever, malformed input).
"""

import argparse
import json
import sys
from pathlib import Path

MODE_NAMES = {"F": "Fortress", "R": "Resilient", "T": "Transitional", "V": "Vulnerable"}

# Exposure weight per lever: 0 = structural, 0.5 = partial, 1 = ai_exposed
PILLARS = {
    "SC": {"SC1": 1, "SC2": 1, "SC3": 1, "SC4": 0, "SC5": 0.5, "SC6": 0},
    "DK": {"DK1": 0.5, "DK2": 0.5, "DK3": 0.5, "DK4": 0.5, "DK5": 0, "DK6": 0},
    "DS": {"DS1": 0.5, "DS2": 0.5, "DS3": 0.5, "DS4": 1, "DS5": 0},
    "DC": {"DC1": 0, "DC2": 0, "DC3": 0, "DC4": 0, "DC5": 0, "DC6": 0, "DC7": 0},
}


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


def get_score(levers: dict, key: str) -> float:
    entry = levers.get(key, {})
    try:
        return float(entry.get("score", 0))
    except (TypeError, ValueError):
        return 0.0


def compute(data: dict) -> dict:
    levers = data.get("levers", {})
    if not levers:
        print("ERROR: scores.json contains no 'levers' object", file=sys.stderr)
        sys.exit(1)

    missing = [lid for pillar in PILLARS.values() for lid in pillar if lid not in levers]
    if missing:
        print(f"ERROR: missing lever scores: {', '.join(missing)}", file=sys.stderr)
        sys.exit(1)

    pillar_scores, pillar_exposure = {}, {}
    for pillar, weights in PILLARS.items():
        scores = [get_score(levers, lid) for lid in weights]
        pillar_scores[pillar] = round(sum(scores) / len(scores), 1)
        pillar_exposure[pillar] = round(sum(weights.values()) / len(weights), 2)

    composite = round(sum(pillar_scores.values()) / 4, 2)
    exposure = round(sum(pillar_exposure.values()) / 4, 2)

    if composite < 2.5 or exposure > 0.65:
        mode = "V"
    elif composite >= 3.5:
        mode = "F" if exposure <= 0.35 else "R"
    else:
        mode = "T"

    notes = []
    if composite >= 3.5 and abs(exposure - 0.35) <= 0.03:
        notes.append(f"Exposure {exposure:.2f} is within 0.03 of the Fortress/Resilient boundary (0.35).")
    if composite >= 3.5 and abs(exposure - 0.60) <= 0.03:
        notes.append(f"Exposure {exposure:.2f} is within 0.03 of the Resilient/Vulnerable boundary (0.60).")
    if abs(exposure - 0.65) <= 0.03:
        notes.append(f"Exposure {exposure:.2f} is within 0.03 of the Vulnerable threshold (0.65).")
    if abs(composite - 3.5) <= 0.03:
        notes.append(f"Composite {composite:.2f} is within 0.03 of the F/R vs Transitional boundary (3.5).")
    if abs(composite - 2.5) <= 0.03:
        notes.append(f"Composite {composite:.2f} is within 0.03 of the Transitional vs Vulnerable boundary (2.5).")

    # Judgment-based flags left to the model (spec §5): distribution_only, per-pillar ai_acceleration_risk.
    # This script only computes distribution_only's trigger condition so the model doesn't have to eyeball it.
    non_dc_avg = round((pillar_scores["SC"] + pillar_scores["DK"] + pillar_scores["DS"]) / 3, 2)
    distribution_only = pillar_scores["DC"] >= 3.5 and non_dc_avg < 2.5

    result = {
        "company_name": data.get("company_name", ""),
        "framework_version": data.get("framework_version", ""),
        "computed_at": data.get("scored_at", ""),
        "pillar_scores": pillar_scores,
        "pillar_exposure_ratios": pillar_exposure,
        "moat_composite": composite,
        "overall_exposure_ratio": exposure,
        "mode": mode,
        "mode_name": MODE_NAMES[mode],
        "distribution_only": distribution_only,
    }
    if notes:
        result["boundary_flag"] = True
        result["boundary_note"] = " ".join(notes)

    print("MOAT composites:")
    print(f"  Pillars: SC={pillar_scores['SC']} DK={pillar_scores['DK']} DS={pillar_scores['DS']} DC={pillar_scores['DC']}")
    print(f"  Composite: {composite} | Exposure: {exposure} | Mode: {mode} — {MODE_NAMES[mode]}")
    if distribution_only:
        print("  Flag: distribution_only — moat is primarily relational, product itself is thin")
    return result


def main():
    parser = argparse.ArgumentParser(description="Compute the MOAT composite, exposure ratio, and mode deterministically.")
    parser.add_argument("--scores", required=True, help="Path to scores.json (all 24 lever scores)")
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
