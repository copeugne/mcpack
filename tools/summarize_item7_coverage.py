#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = ["mcpack-evidence"]
# [tool.uv.sources]
# mcpack-evidence = { path = "..", editable = true }
# ///

# How to run:
#   uv run python tools/summarize_item7_coverage.py --root ROOT --catalog CATALOG \
#     MANIFEST [MANIFEST ...] --output OUTPUT

"""Write strict provider observation coverage from Item 7 decoded evidence."""

from __future__ import annotations

import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Final

from mcpack_evidence.item7_coverage import summarize_coverage
from mcpack_evidence.item7_coverage_models import CoverageError

_MIN_ARGUMENTS: Final = 7
_MIN_OUTPUT_INDEX: Final = 5


@dataclass(frozen=True, slots=True)
class _Arguments:
    root: Path
    catalog: Path
    manifests: tuple[Path, ...]
    output: Path


def _arguments(argv: tuple[str, ...]) -> _Arguments:
    usage = (
        "usage: summarize_item7_coverage.py --root ROOT --catalog CATALOG "
        "MANIFEST [MANIFEST ...] --output OUTPUT"
    )
    if len(argv) < _MIN_ARGUMENTS or argv[:1] != ("--root",) or argv[2:3] != ("--catalog",):
        raise SystemExit(usage)
    if argv.count("--root") != 1 or argv.count("--catalog") != 1 or argv.count("--output") != 1:
        raise SystemExit(usage)
    output_index = argv.index("--output")
    if output_index < _MIN_OUTPUT_INDEX or output_index != len(argv) - 2:
        raise SystemExit(usage)
    return _Arguments(
        root=Path(argv[1]),
        catalog=Path(argv[3]),
        manifests=tuple(Path(value) for value in argv[4:output_index]),
        output=Path(argv[-1]),
    )


def _output_path(root: Path, relative: Path) -> Path:
    if relative.is_absolute() or not relative.parts or ".." in relative.parts:
        detail = f"output path is not relative: {relative}"
        raise CoverageError(detail)
    target = root / relative
    try:
        _ = target.parent.resolve().relative_to(root.resolve())
    except ValueError as error:
        detail = f"output path escapes root: {relative}"
        raise CoverageError(detail) from error
    if target.is_symlink():
        detail = f"output path is a symlink: {relative}"
        raise CoverageError(detail)
    return target


def run(argv: tuple[str, ...]) -> int:
    """Summarize explicit command-line inputs into one atomic JSON output."""
    arguments = _arguments(argv)
    report = summarize_coverage(arguments.root, arguments.catalog, arguments.manifests)
    output = _output_path(arguments.root, arguments.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            "w",
            encoding="utf-8",
            newline="\n",
            prefix=f".{output.name}.",
            dir=output.parent,
            delete=False,
        ) as stream:
            temporary = Path(stream.name)
            _ = stream.write(report.model_dump_json(indent=2) + "\n")
        _ = temporary.replace(output)
    except OSError as error:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
        detail = f"cannot write coverage report: {arguments.output}"
        raise CoverageError(detail) from error
    print(f"summarized {len(report.labels)} provider labels to {arguments.output}")
    return 0


def main() -> int:
    """Run the coverage summarizer from the process argument vector."""
    return run(tuple(sys.argv[1:]))


if __name__ == "__main__":
    raise SystemExit(main())
