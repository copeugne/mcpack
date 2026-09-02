"""Deterministically process Item 5 long-form CSV samples."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import cast

from mcpack_evidence.item5 import analyze_csv


def main() -> int:
    """Process the requested CSV."""
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("--input", required=True, type=Path)
    _ = parser.add_argument("--output", required=True, type=Path)
    arguments = parser.parse_args()
    analyze_csv(cast("Path", arguments.input), cast("Path", arguments.output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
