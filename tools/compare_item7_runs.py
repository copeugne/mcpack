#!/usr/bin/env python3
"""Compare exact normalized Item 7 Run A and Run B evidence."""

from __future__ import annotations

import sys
from pathlib import Path

from mcpack_evidence.item7_repeat import ComparisonInputs
from mcpack_evidence.item7_repeat_comparison import compare_runs

__all__ = ("compare_runs",)


def _parse(argv: tuple[str, ...]) -> ComparisonInputs:
    flags = ("--protocol", "--run-a", "--run-b", "--output")
    if len(argv) != len(flags) * 2 or tuple(argv[::2]) != flags:
        usage = "usage: compare_item7_runs.py --protocol JSON --run-a DIR --run-b DIR --output JSON"
        raise SystemExit(usage)
    return ComparisonInputs(Path(argv[1]), Path(argv[3]), Path(argv[5]), Path(argv[7]))


def main(argv: tuple[str, ...] | None = None) -> int:
    """Run the shared comparison and return nonzero for semantic inequality."""
    arguments = tuple(sys.argv[1:]) if argv is None else argv
    return 0 if compare_runs(_parse(arguments)) else 1


if __name__ == "__main__":
    raise SystemExit(main())
