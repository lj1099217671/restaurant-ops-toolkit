from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from .channels import apply_channel_rules, load_channel_rules
from .io import read_sales_csv
from .metrics import compare_periods, summarize_records


def write_json(payload: dict[str, Any], output: str | None) -> None:
    text = json.dumps(payload, ensure_ascii=False, indent=2)
    if output:
        path = Path(output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text + "\n", encoding="utf-8")
        print(path)
    else:
        print(text)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="restaurant-ops",
        description="Summarize and compare standardized restaurant sales exports.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    summarize = subparsers.add_parser("summarize")
    summarize.add_argument("--input", required=True)
    summarize.add_argument("--output")

    compare = subparsers.add_parser("compare")
    compare.add_argument("--current", required=True)
    compare.add_argument("--previous", required=True)
    compare.add_argument("--output")

    channels = subparsers.add_parser("channels")
    channels.add_argument("--input", required=True)
    channels.add_argument("--rules", required=True)
    channels.add_argument("--output")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.command == "summarize":
        payload = summarize_records(read_sales_csv(args.input))
    elif args.command == "compare":
        payload = compare_periods(
            read_sales_csv(args.current),
            read_sales_csv(args.previous),
        )
    else:
        rows, audit = apply_channel_rules(
            read_sales_csv(args.input),
            load_channel_rules(args.rules),
        )
        payload = {
            "audit": audit,
            "summary": summarize_records(rows),
            "records": rows,
        }
    write_json(payload, args.output)


if __name__ == "__main__":
    main()
