# Governance

Governance is a first-class component of AgenticOps.

## Core Controls

### Human-in-the-loop

High-impact actions require explicit approval. The prototype demonstrates an approval gate before simulated execution.

### Allow-listed actions

Only predefined playbooks may be recommended for execution. Unknown actions are denied.

### Risk boundaries

Every playbook has a maximum permitted risk level.

### Safe execution model

The MVP performs simulated actions only. It does not connect to remote hosts, execute arbitrary shell commands, change credentials, disable controls, or modify production systems.

### Auditability

The decision, policy result and action outcome are stored in a structured audit record.

### Explainability

The recommendation includes a deterministic reason so the operator can understand why an action was selected.

## Governance Objective

The project treats AI autonomy as a controlled operating capability, not as an unrestricted permission.

A useful enterprise pattern is:

**AI proposes → policy evaluates → human authorizes when required → controlled action executes → outcome is audited**
