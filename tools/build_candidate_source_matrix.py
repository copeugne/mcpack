"""Build the complete Item 3 exact-file primary-source matrix."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import cast

from mcpack_evidence.item3_sources import build_source_matrix


def main() -> int:
    """Normalize the two primary-platform discovery results into one matrix."""
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("--inventory", type=Path, required=True)
    _ = parser.add_argument("--modrinth", type=Path, required=True)
    _ = parser.add_argument("--curseforge", type=Path, required=True)
    _ = parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    output = cast("Path", arguments.output)
    matrix = build_source_matrix(
        cast("Path", arguments.inventory),
        cast("Path", arguments.modrinth),
        cast("Path", arguments.curseforge),
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    _ = output.write_text(matrix.model_dump_json(indent=2) + "\n", encoding="utf-8")
    print(f"resolved {matrix.resolved_count}/{matrix.inventory_count} exact candidate files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
