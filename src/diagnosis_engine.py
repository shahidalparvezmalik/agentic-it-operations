from __future__ import annotations

from typing import Any


SEVERITY_ORDER = {"low": 1, "medium": 2, "high": 3, "critical": 4}


def diagnose(correlation: dict[str, Any]) -> dict[str, Any]:
    """Produce a deterministic operational diagnosis from correlated signals."""
    events = correlation.get("events", [])
    types = {event.get("type") for event in events}
    failures = sum(
        1 for event in events if event.get("type") in {"service_unavailable", "service_repeated_failure"}
    )

    diagnosis = "No significant pattern detected"
    confidence = 0.55

    if "service_unavailable" in types and "service_repeated_failure" in types:
        diagnosis = "Repeated service failure with elevated host resource pressure"
        confidence = 0.93
    elif "service_unavailable" in types:
        diagnosis = "Service availability failure"
        confidence = 0.82

    max_severity = max(
        (event.get("severity", "low") for event in events),
        key=lambda value: SEVERITY_ORDER.get(value, 1),
        default="low",
    )

    return {
        "host": correlation["host"],
        "service": correlation["service"],
        "diagnosis": diagnosis,
        "confidence": confidence,
        "max_severity": max_severity,
        "failure_count": failures,
        "event_ids": correlation.get("event_ids", []),
    }
