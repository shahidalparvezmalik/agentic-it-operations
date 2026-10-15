from __future__ import annotations

import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.action_simulator import simulate_action
from src.agent_planner import recommend_action
from src.audit_logger import create_audit_record
from src.diagnosis_engine import diagnose
from src.event_correlator import correlate_events
from src.policy_engine import evaluate_policy
from src.report import build_report
from src.risk_engine import assess_risk


def load_json(relative_path: str) -> object:
    with (ROOT / relative_path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> None:
    events = load_json("data/events.json")
    policies = load_json("config/policies.json")

    correlations = correlate_events(events)
    if not correlations:
        raise RuntimeError("No event correlations were produced.")

    diagnosis = diagnose(correlations[0])
    risk = assess_risk(diagnosis)
    recommendation = recommend_action(diagnosis, risk)
    policy = evaluate_policy(recommendation, policies)

    # Demonstrate the governed path before human approval.
    action = simulate_action(
        recommendation["action_id"],
        policy,
        approved_by_human=False,
    )
    audit = create_audit_record(
        recommendation=recommendation,
        policy_decision=policy,
        action_result=action,
    )
    report = build_report(
        diagnosis,
        risk,
        recommendation,
        policy,
        action,
        audit,
    )

    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
