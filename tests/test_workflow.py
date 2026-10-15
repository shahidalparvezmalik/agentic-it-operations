import unittest

from src.action_simulator import simulate_action
from src.agent_planner import recommend_action
from src.diagnosis_engine import diagnose
from src.event_correlator import correlate_events
from src.policy_engine import evaluate_policy
from src.risk_engine import assess_risk


class TestWorkflow(unittest.TestCase):
    def test_demo_workflow_reaches_approval_gate(self):
        events = [
            {
                "event_id": "EVT-1",
                "host": "APP-SRV-01",
                "service": "SampleAppService",
                "type": "service_unavailable",
                "severity": "high",
            },
            {
                "event_id": "EVT-2",
                "host": "APP-SRV-01",
                "service": "SampleAppService",
                "type": "service_repeated_failure",
                "severity": "high",
            },
            {
                "event_id": "EVT-3",
                "host": "APP-SRV-01",
                "service": "SampleAppService",
                "type": "resource_pressure",
                "severity": "medium",
            },
        ]

        policies = {
            "allowed_actions": [
                {
                    "id": "restart-approved-service",
                    "max_risk": "critical",
                    "requires_human_approval": True,
                }
            ]
        }

        correlation = correlate_events(events)[0]
        diagnosis = diagnose(correlation)
        risk = assess_risk(diagnosis)
        recommendation = recommend_action(diagnosis, risk)
        policy = evaluate_policy(recommendation, policies)
        action = simulate_action(
            recommendation["action_id"],
            policy,
            approved_by_human=False,
        )

        self.assertEqual(recommendation["action_id"], "restart-approved-service")
        self.assertEqual(policy["decision"], "human_approval")
        self.assertEqual(action["status"], "pending_approval")


if __name__ == "__main__":
    unittest.main()
