#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = ["mcpack-evidence"]
# [tool.uv.sources]
# mcpack-evidence = { path = "..", editable = true }
# ///

# How to run:
#   uv run python tools/close_item7_provider_coverage.py --repository ROOT --raw-root ROOT \
#     --catalog evidence/item-7/provider-catalog.json --coverage run-a/provider-coverage.json \
#     --runtime-log run-a/mountainous/minecraft-latest.log \
#     --gap gap-a/ordinary --gap gap-b/ordinary \
#     --output provider-disposition.json

"""Publish the strict Item 7 provider-disposition closure atomically."""

from __future__ import annotations

import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Final

from mcpack_evidence.item7_provider_disposition import build_disposition
from mcpack_evidence.item7_provider_disposition_gap_evidence import ProviderDispositionError

_USAGE: Final = (
    "usage: close_item7_provider_coverage.py --repository ROOT --raw-root ROOT --catalog RELATIVE "
    "--coverage RELATIVE --runtime-log RELATIVE --gap RELATIVE --gap RELATIVE --output RELATIVE"
)
_ARGUMENT_COUNT: Final = 16


@dataclass(frozen=True, slots=True)
class _Arguments:
    repository: Path
    raw_root: Path
    catalog: Path
    coverage: Path
    runtime_log: Path
    gaps: tuple[Path, Path]
    output: Path


def _arguments(argv: tuple[str, ...]) -> _Arguments:
    if len(argv) != _ARGUMENT_COUNT or argv[::2] != (
        "--repository",
        "--raw-root",
        "--catalog",
        "--coverage",
        "--runtime-log",
        "--gap",
        "--gap",
        "--output",
    ):
        raise SystemExit(_USAGE)
    return _Arguments(
        repository=Path(argv[1]),
        raw_root=Path(argv[3]),
        catalog=Path(argv[5]),
        coverage=Path(argv[7]),
        runtime_log=Path(argv[9]),
        gaps=(Path(argv[11]), Path(argv[13])),
        output=Path(argv[15]),
    )


def _output(raw_root: Path, relative: Path) -> Path:
    if relative.is_absolute() or not relative.parts or ".." in relative.parts:
        detail = f"output path is not relative: {relative}"
        raise ProviderDispositionError(detail)
    output = raw_root / relative
    try:
        _ = output.parent.resolve().relative_to(raw_root.resolve())
    except ValueError as error:
        detail = f"output path escapes root: {relative}"
        raise ProviderDispositionError(detail) from error
    if output.is_symlink():
        detail = f"output path is a symlink: {relative}"
        raise ProviderDispositionError(detail)
    return output


def run(argv: tuple[str, ...]) -> int:
    """Build and atomically publish the one provider closure report."""
    arguments = _arguments(argv)
    report = build_disposition(
        arguments.repository,
        arguments.raw_root,
        catalog_relative=arguments.catalog,
        coverage_relative=arguments.coverage,
        runtime_log_relative=arguments.runtime_log,
        gap_a_relative=arguments.gaps[0],
        gap_b_relative=arguments.gaps[1],
    )
    output = _output(arguments.raw_root, arguments.output)
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
        detail = f"cannot write provider disposition: {arguments.output}"
        raise ProviderDispositionError(detail) from error
    print(f"closed {report.totals.total_components} provider components to {arguments.output}")
    return 0


def main() -> int:
    """Run the provider coverage closure CLI."""
    return run(tuple(sys.argv[1:]))


if __name__ == "__main__":
    raise SystemExit(main())
