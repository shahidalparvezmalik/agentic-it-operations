import unittest

from src.policy_engine import evaluate_policy


class TestPolicyEngine(unittest.TestCase):
    def setUp(self):
        self.policies = {
            "allowed_actions": [
                {
                    "id": "restart-approved-service",
                    "max_risk": "medium",
                    "requires_human_approval": True,
                }
            ]
        }

    def test_requires_human_approval(self):
        recommendation = {
            "action_id": "restart-approved-service",
            "risk_level": "medium",
            "confidence": 0.91,
        }

        result = evaluate_policy(recommendation, self.policies)

        self.assertEqual(result["decision"], "human_approval")
        self.assertTrue(result["requires_human_approval"])

    def test_blocks_excessive_risk(self):
        recommendation = {
            "action_id": "restart-approved-service",
            "risk_level": "high",
            "confidence": 0.91,
        }

        result = evaluate_policy(recommendation, self.policies)

        self.assertEqual(result["decision"], "deny")


if __name__ == "__main__":
    unittest.main()
