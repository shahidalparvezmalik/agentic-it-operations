# Action Policy

The policy engine uses explicit allow-listed playbooks.

## Example

```json
{
  "id": "restart-approved-service",
  "max_risk": "medium",
  "requires_human_approval": true
}
```

A recommendation is permitted only when:

1. The action exists on the allow-list.
2. The observed risk does not exceed the playbook maximum.
3. Any required human approval is satisfied.

Unknown or unrestricted actions are denied.

## Blocked Patterns

The project intentionally blocks concepts such as:

- arbitrary shell execution
- credential changes
- firewall disabling
- destructive data operations

These are examples of activities that should never become accidental side effects of an AI recommendation workflow.
