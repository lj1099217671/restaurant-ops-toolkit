"""Vendor-neutral restaurant operations metrics."""

from .channels import apply_channel_rules, load_channel_rules
from .metrics import compare_periods, summarize_records

__all__ = [
    "apply_channel_rules",
    "compare_periods",
    "load_channel_rules",
    "summarize_records",
]
__version__ = "0.1.0"
