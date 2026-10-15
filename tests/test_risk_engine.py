import unittest

from src.risk_engine import assess_risk


class TestRiskEngine(unittest.TestCase):
    def test_high_failure_pattern(self):
        diagnosis = {
            "max_severity": "high",
            "failure_count": 4,
            "confidence": 0.93,
        }
        result = assess_risk(diagnosis)

        self.assertEqual(result["risk_level"], "high")
        self.assertEqual(result["risk_score"], 50)

    def test_low_risk_pattern(self):
        diagnosis = {
            "max_severity": "low",
            "failure_count": 0,
            "confidence": 0.55,
        }
        result = assess_risk(diagnosis)

        self.assertEqual(result["risk_level"], "low")
        self.assertEqual(result["risk_score"], 5)


if __name__ == "__main__":
    unittest.main()
