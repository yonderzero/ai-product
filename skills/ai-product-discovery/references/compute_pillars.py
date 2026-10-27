#!/usr/bin/env python3
"""Compute the four discovery pillars and the move from the three scripts' outputs.

Protection     = the moat composite.
Strength       = the mean of the business quality (A) and customer strength (B) section scores.
AI opportunity = the mean of AI today (C1), AI revenue (C3) and work AI could take off customers (C4).
                 Urgency (C2) is left out: its scale is inverted (1 = immediate urgency), so averaging it
                 in would make a product under heavy AI pressure look like a smaller opportunity.
                 It is reported on its own instead.
Exposure       = the risk composite (1 safest, 5 most exposed). It already counts AI disruption and its timing.

The move places AI opportunity against exposure, with 3.0 as the line on both.
A score within 0.2 of the line is borderline: the product manager decides which side.
"""
import argparse
import json

LINE = 3.0
BORDER = 0.2
URGENCY = {1: "immediate", 2: "high", 3: "moderate", 4: "low", 5: "minimal"}


def load(path):
    with open(path) as f:
        return json.load(f)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--protection", required=True, help="protection composites.json")
    ap.add_argument("--strength", required=True, help="strength composites.json")
    ap.add_argument("--exposure", required=True, help="exposure composite.json")
    ap.add_argument("--output", required=True, help="where to write pillars.json")
    a = ap.parse_args()

    p, s, e = load(a.protection), load(a.strength), load(a.exposure)
    dims = s["all_dimension_scores"]
    sec = s["section_scores"]

    opportunity = round((dims["C1"] + dims["C3"] + dims["C4"]) / 3, 2)
    exposure = e["risk_composite"]
    out = {
        "pillars": {
            "protection": p["moat_composite"],
            "strength": round((sec["A"] + sec["B"]) / 2, 2),
            "ai_opportunity": opportunity,
            "exposure": exposure,
        },
        "ai_urgency": {"score": dims["C2"], "meaning": URGENCY.get(dims["C2"], "")},
        "borderline": {
            "ai_opportunity": abs(opportunity - LINE) < BORDER,
            "exposure": abs(exposure - LINE) < BORDER,
        },
    }
    high_opp, high_risk = opportunity >= LINE, exposure >= LINE
    out["move"] = {
        (True, False): "Build on it",
        (True, True): "Move first",
        (False, False): "Optimise",
        (False, True): "Defend",
    }[(high_opp, high_risk)]

    with open(a.output, "w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
