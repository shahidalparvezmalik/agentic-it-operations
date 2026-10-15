from __future__ import annotations

from typing import Any


RISK_ORDER = {"low": 1, "medium": 2, "high": 3, "critical": 4}


def evaluate_policy(
    recommendation: dict[str, Any],
    policies: dict[str, Any],
) -> dict[str, Any]:
    """Apply allow-list and risk controls to a recommendation."""
    action_id = recommendation.get("action_id", "none")

    if action_id == "none":
        return {
            "decision": "deny",
            "reason": "No action recommended.",
            "requires_human_approval": False,
        }

    allowed = next(
        (item for item in policies.get("allowed_actions", []) if item.get("id") == action_id),
        None,
    )

    if not allowed:
        return {
            "decision": "deny",
            "reason": "Action is not on the approved playbook allow-list.",
            "requires_human_approval": True,
        }

    actual_risk = RISK_ORDER.get(recommendation.get("risk_level", "critical"), 4)
    maximum_risk = RISK_ORDER.get(allowed.get("max_risk", "low"), 1)

    if actual_risk > maximum_risk:
        return {
            "decision": "deny",
            "reason": "Risk level exceeds the playbook's maximum permitted risk.",
            "requires_human_approval": True,
        }

    if allowed.get("requires_human_approval", True):
        return {
            "decision": "human_approval",
            "reason": "Approved playbook matched, but policy requires explicit human approval.",
            "requires_human_approval": True,
        }

    return {
        "decision": "allow",
        "reason": "Approved low-risk action may proceed under policy.",
        "requires_human_approval": False,
    }
