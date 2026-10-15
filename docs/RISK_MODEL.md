# Risk Model

The MVP uses a transparent weighted model.

## Inputs

- Maximum observed severity
- Number of repeated failures
- Diagnosis confidence

## Example scoring logic

- Critical severity: +40
- High severity: +25
- Medium severity: +10
- Low severity: +5
- Three or more repeated failures: +15
- Confidence of 0.90 or higher: +10

The result is capped at 100.

## Risk bands

| Score | Level |
|---:|---|
| 0–24 | Low |
| 25–44 | Medium |
| 45–69 | High |
| 70–100 | Critical |

This is a **prototype model**, not an enterprise risk standard. A production implementation would require calibration against service criticality, business impact, operational history and organizational policy.
