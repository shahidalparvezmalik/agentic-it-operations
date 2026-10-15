# Architecture

AgenticOps is intentionally designed as a controlled decision pipeline rather than an unrestricted autonomous agent.

## Flow

1. **Signal ingestion** — synthetic infrastructure and ITSM-style events enter the workflow.
2. **Correlation** — events are grouped by host and service.
3. **Diagnosis** — deterministic rules identify operational patterns.
4. **Risk assessment** — severity, recurrence and confidence contribute to a risk score.
5. **Agent planning** — the planner maps the observed pattern to an approved remediation recommendation.
6. **Policy evaluation** — the recommendation is checked against an explicit action allow-list and risk boundary.
7. **Action simulation** — the prototype simulates the action rather than touching production.
8. **Audit** — the complete decision path is recorded for management review.

## Design Principle

The architecture separates:

- what happened,
- what the system believes happened,
- what action is recommended,
- what policy permits,
- what a human approves,
- what was actually executed.

That separation is essential for accountable IT automation.
