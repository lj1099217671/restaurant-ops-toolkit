from __future__ import annotations

from collections import defaultdict
from typing import Any, Iterable


def _number(record: dict[str, Any], field: str) -> float:
    value = record.get(field, 0)
    if value in (None, ""):
        return 0.0
    return float(value)


def _change(current: float, previous: float) -> dict[str, float | None]:
    absolute = current - previous
    rate = absolute / previous if previous else None
    return {
        "current": round(current, 2),
        "previous": round(previous, 2),
        "absolute_change": round(absolute, 2),
        "change_rate": round(rate, 6) if rate is not None else None,
    }


def summarize_records(
    records: Iterable[dict[str, Any]],
    *,
    tolerance: float = 0.01,
) -> dict[str, Any]:
    rows = list(records)
    stores = {
        str(row.get("store_id") or row.get("store_name") or "").strip()
        for row in rows
        if str(row.get("store_id") or row.get("store_name") or "").strip()
    }

    revenue = sum(_number(row, "revenue") for row in rows)
    orders = sum(_number(row, "orders") for row in rows)
    dine_in = sum(_number(row, "dine_in") for row in rows)
    delivery = sum(_number(row, "delivery") for row in rows)
    takeaway = sum(_number(row, "takeaway") for row in rows)

    channel_totals: dict[str, float] = defaultdict(float)
    for row in rows:
        for key in row:
            if key.startswith("channel_"):
                channel_totals[key] += _number(row, key)

    service_total = dine_in + delivery + takeaway
    channel_total = sum(channel_totals.values())
    service_gap = service_total - revenue
    channel_gap = channel_total - revenue

    return {
        "row_count": len(rows),
        "store_count": len(stores),
        "revenue": round(revenue, 2),
        "store_average_revenue": round(revenue / len(stores), 2) if stores else 0.0,
        "orders": round(orders, 2),
        "average_ticket": round(revenue / orders, 2) if orders else 0.0,
        "service_types": {
            "dine_in": round(dine_in, 2),
            "delivery": round(delivery, 2),
            "takeaway": round(takeaway, 2),
            "sum": round(service_total, 2),
            "gap_to_revenue": round(service_gap, 2),
            "closed": abs(service_gap) <= tolerance,
        },
        "channels": {
            "values": {key: round(value, 2) for key, value in sorted(channel_totals.items())},
            "sum": round(channel_total, 2),
            "gap_to_revenue": round(channel_gap, 2),
            "closed": abs(channel_gap) <= tolerance,
        },
    }


def compare_periods(
    current_records: Iterable[dict[str, Any]],
    previous_records: Iterable[dict[str, Any]],
) -> dict[str, Any]:
    current = summarize_records(current_records)
    previous = summarize_records(previous_records)
    return {
        "current": current,
        "previous": previous,
        "comparison": {
            "revenue": _change(current["revenue"], previous["revenue"]),
            "store_average_revenue": _change(
                current["store_average_revenue"],
                previous["store_average_revenue"],
            ),
            "orders": _change(current["orders"], previous["orders"]),
            "average_ticket": _change(
                current["average_ticket"],
                previous["average_ticket"],
            ),
        },
    }
