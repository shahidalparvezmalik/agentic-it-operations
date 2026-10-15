from __future__ import annotations

from typing import Any


def build_report(
    diagnosis: dict[str, Any],
    risk: dict[str, Any],
    recommendation: dict[str, Any],
    policy: dict[str, Any],
    action: dict[str, Any],
    audit: dict[str, Any],
) -> dict[str, Any]:
    """Build a management-oriented report."""
    return {
        "summary": {
            "host": diagnosis.get("host"),
            "service": diagnosis.get("service"),
            "diagnosis": diagnosis.get("diagnosis"),
            "risk_level": risk.get("risk_level"),
            "risk_score": risk.get("risk_score"),
            "recommended_action": recommendation.get("action_id"),
            "policy_decision": policy.get("decision"),
            "action_status": action.get("status"),
        },
        "diagnosis": diagnosis,
        "risk": risk,
        "recommendation": recommendation,
        "policy": policy,
        "action": action,
        "audit": audit,
    }
