from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


def create_audit_record(
    *,
    recommendation: dict[str, Any],
    policy_decision: dict[str, Any],
    action_result: dict[str, Any],
) -> dict[str, Any]:
    """Create a structured, UTC audit event."""
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "action_id": recommendation.get("action_id"),
        "risk_level": recommendation.get("risk_level"),
        "confidence": recommendation.get("confidence"),
        "policy_decision": policy_decision.get("decision"),
        "policy_reason": policy_decision.get("reason"),
        "action_status": action_result.get("status"),
        "action_message": action_result.get("message"),
    }
