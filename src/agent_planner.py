from __future__ import annotations

from typing import Any


def recommend_action(diagnosis: dict[str, Any], risk: dict[str, Any]) -> dict[str, Any]:
    """Create a deterministic, explainable action recommendation."""
    if "service failure" in diagnosis.get("diagnosis", "").lower():
        action_id = "restart-approved-service"
        reason = "Service availability is degraded and the correlated pattern supports a controlled restart recommendation."
    else:
        action_id = "none"
        reason = "No approved remediation playbook matches the observed pattern."

    return {
        "action_id": action_id,
        "reason": reason,
        "risk_level": risk["risk_level"],
        "confidence": diagnosis.get("confidence", 0.0),
    }
