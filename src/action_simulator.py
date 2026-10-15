from __future__ import annotations

from typing import Any


def simulate_action(
    action_id: str,
    policy_decision: dict[str, Any],
    approved_by_human: bool = False,
) -> dict[str, Any]:
    """Simulate action execution without touching real infrastructure."""
    decision = policy_decision.get("decision")

    if action_id == "none":
        return {"status": "skipped", "message": "No action requested."}

    if decision == "deny":
        return {"status": "blocked", "message": policy_decision.get("reason", "Blocked by policy.")}

    if decision == "human_approval" and not approved_by_human:
        return {
            "status": "pending_approval",
            "message": "Explicit human approval is required before execution.",
        }

    return {
        "status": "simulated_success",
        "message": f"Simulated execution completed for {action_id}.",
    }
