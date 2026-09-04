"""Build the exact expected contents of the three Item 7 world archives."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import ClassVar

from pydantic import BaseModel, ConfigDict

from mcpack_evidence.item7_world_archive_inventory import (
    WorldArchiveSource,
    write_world_archive_inventory,
)


class _Arguments(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)

    run_a: Path
    run_a_archive_name: str
    run_b: Path
    run_b_archive_name: str
    auxiliary: Path
    auxiliary_archive_name: str
    output: Path


def main() -> int:
    """Parse explicit stage roots and write their deterministic inventory."""
    parser = argparse.ArgumentParser()
    for flag in ("run-a", "run-b", "auxiliary", "output"):
        _ = parser.add_argument(f"--{flag}", type=Path, required=True)
    for flag in ("run-a-archive-name", "run-b-archive-name", "auxiliary-archive-name"):
        _ = parser.add_argument(f"--{flag}", required=True)
    options = _Arguments.model_validate(vars(parser.parse_args()), strict=True)
    report = write_world_archive_inventory(
        options.output,
        (
            WorldArchiveSource(options.run_a, options.run_a_archive_name),
            WorldArchiveSource(options.run_b, options.run_b_archive_name),
            WorldArchiveSource(options.auxiliary, options.auxiliary_archive_name),
        ),
    )
    print(f"PASS: inventoried {sum(len(row.files) for row in report.archives)} world files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
