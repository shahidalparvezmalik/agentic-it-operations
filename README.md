# AgenticOps — Governed AI for IT Operations

AgenticOps is a safe, reproducible proof of concept showing how AI-assisted IT Operations can move from technical signals to governed operational action.

The project focuses on a practical operating model:

**Observe → Correlate → Diagnose → Assess Risk → Recommend → Authorize → Simulate Action → Audit**

The prototype does **not** grant unrestricted production access to an AI agent. High-impact actions require explicit human approval, while only predefined low-risk actions may be considered for controlled automation.

## What This Project Demonstrates

- Event correlation across infrastructure and ITSM-style signals
- Deterministic diagnosis and risk assessment
- AI-agent-style planning and action recommendations
- Policy-based autonomy and human-in-the-loop controls
- Safe remediation simulation
- Structured audit trails
- Unit testing and GitHub Actions validation
- Management-oriented operational reporting

## Architecture

```text
              IT OPERATIONS SIGNALS
                       │
        ┌──────────────┼──────────────┐
        │              │              │
     Health         ITSM Events    Service State
     Signals        Incidents       Checks
        │              │              │
        └──────────────┼──────────────┘
                       ↓
              ┌─────────────────┐
              │ Correlation     │
              │ & Diagnosis     │
              └────────┬────────┘
                       ↓
              ┌─────────────────┐
              │ Risk Assessment │
              └────────┬────────┘
                       ↓
              ┌─────────────────┐
              │ Agent Planner   │
              │ Recommendation  │
              └────────┬────────┘
                       ↓
              ┌─────────────────┐
              │ Policy Engine   │
              │ Guardrails      │
              └────────┬────────┘
                       ↓
             ┌─────────┴─────────┐
             │                   │
      LOW-RISK PATH        HUMAN APPROVAL
             │                   │
             └─────────┬─────────┘
                       ↓
              ┌─────────────────┐
              │ Action Simulator│
              └────────┬────────┘
                       ↓
              ┌─────────────────┐
              │ Audit & Report  │
              └─────────────────┘
```

## Autonomy Model

| Level | Operating mode | Example | Approval |
|---|---|---|---|
| L0 | Observe | Collect and classify signals | Not applicable |
| L1 | Recommend | Suggest remediation | Human review |
| L2 | Approved Action | Execute an approved playbook | Explicit approval |
| L3 | Controlled Autonomous | Low-risk predefined action | Policy-controlled |
| L4 | Restricted | High-impact or irreversible action | Human authorization required |

The prototype emphasizes **L1–L2** and safely simulates selected L3 behavior.

## Example Scenario

A service becomes unavailable while host resource utilization is elevated.

```text
Event:
Windows service unavailable

Related signals:
CPU: 82%
Memory: 88%
Network: OK
DNS: OK
Service: FAILED
Recent incidents: 4

Risk:
HIGH

Recommendation:
Restart approved service

Policy:
Human approval REQUIRED

Execution:
SIMULATED

Audit:
Decision + policy + action + result recorded
```

## Repository Structure

```text
agentic-it-operations/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── config/
│   ├── policies.json
│   ├── playbooks.json
│   └── thresholds.json
├── data/
│   ├── events.json
│   ├── incidents.json
│   └── README.md
├── src/
│   ├── event_correlator.py
│   ├── diagnosis_engine.py
│   ├── risk_engine.py
│   ├── agent_planner.py
│   ├── policy_engine.py
│   ├── action_simulator.py
│   ├── audit_logger.py
│   └── report.py
├── examples/
│   └── run_demo.py
├── tests/
│   ├── test_risk_engine.py
│   ├── test_policy_engine.py
│   └── test_workflow.py
├── docs/
│   ├── ARCHITECTURE.md
│   ├── GOVERNANCE.md
│   ├── AUTONOMY_MODEL.md
│   ├── ACTION_POLICY.md
│   ├── RISK_MODEL.md
│   └── LINKEDIN_ARTICLE.md
└── .github/
    └── workflows/
        └── python.yml
```

## Getting Started

Requires Python 3.11+.

```bash
python examples/run_demo.py
python -m unittest discover -s tests -p "test_*.py"
```

The demo is deterministic and does not require an external AI API, cloud account, or production infrastructure access.

## Safety and Governance

This is a portfolio proof of concept, not a production automation framework.

Key controls:

- Human approval for high-risk actions
- Explicit allow-lists for available playbooks
- Confidence and risk thresholds
- Simulated execution by default
- Audit logging of decisions and outcomes
- No unrestricted shell or remote execution
- No real customer, employer, or production data

## Professional Relevance

AgenticOps extends the portfolio's progression:

1. **IT Operations Dashboard** — ITSM data → operational visibility
2. **AI-Assisted IT Service Desk** — AI → governed recommendation and workflow
3. **Infrastructure Health Check** — technical telemetry → operational risk
4. **AgenticOps** — operational signals → governed AI decision → controlled action

The objective is not autonomous action for its own sake. The objective is to improve operational decision quality while preserving accountability, control, and service reliability.

## Project Status

**Phase 1 — Portfolio MVP**

Current scope:

- Synthetic event data
- Deterministic correlation and diagnosis
- Risk scoring
- Policy-controlled recommendations
- Human approval simulation
- Action simulation
- Audit logging
- Tests and CI validation

Future enhancements may include optional LLM-assisted reasoning, CMDB/ITSM integration, observability data, approval APIs, and service-impact mapping.

---

> **Observe intelligently. Decide responsibly. Automate with control.**
