from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable


def load_channel_rules(path: str | Path) -> dict[str, Any]:
    """Load a vendor-neutral channel mapping configuration."""
    rules = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(rules.get("channels"), dict):
        raise ValueError("channel rules must contain a 'channels' object")
    if not str(rules.get("metric_basis") or "").strip():
        raise ValueError("channel rules must define metric_basis")
    return rules


def apply_channel_rules(
    records: Iterable[dict[str, Any]],
    rules: dict[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Aggregate payment fields into channels and return an audit summary."""
    channel_map: dict[str, list[str]] = rules["channels"]
    metric_basis = str(rules["metric_basis"])
    residual_channel = str(rules.get("residual_channel") or "").strip()
    mapped_channels = [
        channel for channel in channel_map if channel != residual_channel
    ]
    missing_fields: set[str] = set()
    output: list[dict[str, Any]] = []

    for source in records:
        row = dict(source)
        mapped_total = 0.0
        for channel in mapped_channels:
            total = 0.0
            for field in channel_map[channel]:
                if field not in source:
                    missing_fields.add(field)
                total += float(source.get(field) or 0)
            row[channel] = round(total, 2)
            mapped_total += total

        if residual_channel:
            basis = float(source.get(metric_basis) or 0)
            row[residual_channel] = round(basis - mapped_total, 2)
        output.append(row)

    return output, {
        "metric_basis": metric_basis,
        "residual_channel": residual_channel or None,
        "missing_fields": sorted(missing_fields),
        "record_count": len(output),
    }
