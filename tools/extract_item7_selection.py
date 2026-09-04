#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = ["mcpack-evidence"]
# [tool.uv.sources]
# mcpack-evidence = { path = "..", editable = true }
# ///

# How to run:
#   uv run python tools/extract_item7_selection.py PROTOCOL MANIFEST AGGREGATE LABEL OUTPUT

"""Write one renderer-ready Item 7 selection JSONL and receipt."""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Final

from mcpack_evidence.item7_selection_extract import extract_selection

_ARGUMENT_COUNT: Final = 5
_USAGE: Final = "usage: extract_item7_selection.py PROTOCOL MANIFEST AGGREGATE LABEL OUTPUT"


@dataclass(frozen=True, slots=True)
class _Arguments:
    protocol: Path
    manifest: Path
    aggregate: Path
    label: str
    output: Path


def _arguments(argv: tuple[str, ...]) -> _Arguments:
    if len(argv) != _ARGUMENT_COUNT:
        raise SystemExit(_USAGE)
    return _Arguments(Path(argv[0]), Path(argv[1]), Path(argv[2]), argv[3], Path(argv[4]))


def main(argv: tuple[str, ...]) -> int:
    """Run the documented Item 7 selection-extraction CLI boundary."""
    arguments = _arguments(argv)
    receipt = extract_selection(
        arguments.protocol,
        arguments.manifest,
        arguments.aggregate,
        arguments.label,
        arguments.output,
    )
    print(f"extracted {receipt.selected.record_count} chunks to {arguments.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(tuple(sys.argv[1:])))
