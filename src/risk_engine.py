from __future__ import annotations

from typing import Any


SEVERITY_PENALTY = {
    "critical": 40,
    "high": 25,
    "medium": 10,
    "low": 5,
}


def assess_risk(diagnosis: dict[str, Any]) -> dict[str, Any]:
    """Convert diagnosis signals into a 0-100 risk score."""
    score = SEVERITY_PENALTY.get(diagnosis.get("max_severity", "low"), 5)

    if diagnosis.get("failure_count", 0) >= 3:
        score += 15

    if diagnosis.get("confidence", 0.0) >= 0.90:
        score += 10

    score = min(score, 100)

    if score >= 70:
        level = "critical"
    elif score >= 45:
        level = "high"
    elif score >= 25:
        level = "medium"
    else:
        level = "low"

    return {
        "risk_score": score,
        "risk_level": level,
    }
