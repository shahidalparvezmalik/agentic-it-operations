from __future__ import annotations

from collections import defaultdict
from typing import Any


def correlate_events(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Group events by host and service for operational correlation."""
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)

    for event in events:
        key = (event.get("host", "unknown"), event.get("service", "unknown"))
        grouped[key].append(event)

    correlations: list[dict[str, Any]] = []

    for (host, service), related_events in grouped.items():
        severities = [e.get("severity", "low") for e in related_events]
        correlations.append(
            {
                "host": host,
                "service": service,
                "event_count": len(related_events),
                "event_ids": [e.get("event_id") for e in related_events],
                "severities": severities,
                "events": related_events,
            }
        )

    return correlations
