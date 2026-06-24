from __future__ import annotations

import csv
from pathlib import Path
from typing import Any


NUMERIC_FIELDS = {
    "revenue",
    "dine_in",
    "delivery",
    "takeaway",
    "orders",
    "guest_count",
}


def read_sales_csv(path: str | Path) -> list[dict[str, Any]]:
    """Read the public sales data contract from CSV."""
    source = Path(path)
    with source.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    normalized: list[dict[str, Any]] = []
    for index, row in enumerate(rows, start=2):
        item: dict[str, Any] = {}
        for key, value in row.items():
            key = str(key or "").strip()
            text = str(value or "").strip()
            if (
                key in NUMERIC_FIELDS
                or key.startswith("channel_")
                or key.startswith("payment_")
            ):
                try:
                    item[key] = float(text or 0)
                except ValueError as exc:
                    raise ValueError(
                        f"{source}:{index}: field {key!r} must be numeric, got {text!r}"
                    ) from exc
            else:
                item[key] = text
        normalized.append(item)
    return normalized
