#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = ["mcpack-evidence"]
# [tool.uv.sources]
# mcpack-evidence = { path = "..", editable = true }
# ///
# How to run:
#   uv run python tools/compare_item7_control.py --control DIR --pilot DIR \
#     --repeat JSON --output JSON
"""Compare retained-control and Chunky-pilot Item 7 evidence."""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

from mcpack_evidence.item7_control_compare import ControlComparisonInputs, compare_control

_ARGUMENTS = 8
_USAGE = "usage: compare_item7_control.py --control DIR --pilot DIR --repeat JSON --output JSON"


@dataclass(frozen=True, slots=True)
class _Arguments:
    control: Path
    pilot: Path
    repeat: Path
    output: Path


def _parse(argv: tuple[str, ...]) -> _Arguments:
    flags = ("--control", "--pilot", "--repeat", "--output")
    if len(argv) != _ARGUMENTS or tuple(argv[::2]) != flags:
        raise SystemExit(_USAGE)
    return _Arguments(Path(argv[1]), Path(argv[3]), Path(argv[5]), Path(argv[7]))


def main(argv: tuple[str, ...] | None = None) -> int:
    """Run the exact Item 7 retained-control comparison CLI."""
    arguments = _parse(tuple(sys.argv[1:]) if argv is None else argv)
    inputs = ControlComparisonInputs(
        arguments.control, arguments.pilot, arguments.repeat, arguments.output
    )
    _ = compare_control(inputs)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
