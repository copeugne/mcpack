#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = ["mcpack-evidence"]
# [tool.uv.sources]
# mcpack-evidence = { path = "..", editable = true }
# ///

# How to run:
#   uv run python tools/disposition_item7_warnings.py --root ROOT --audit AUDIT \
#     --output RELATIVE_OUTPUT

"""Write strict Item 7 per-signature warning dispositions atomically."""

from __future__ import annotations

import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Final, NoReturn

from mcpack_evidence.item7_warning_disposition import (
    WarningDispositionError,
    disposition_audit,
)


@dataclass(frozen=True, slots=True)
class _Arguments:
    root: Path
    audit: Path
    output: Path


_ARGUMENT_COUNT: Final = 6


def _fail(detail: str) -> NoReturn:
    raise WarningDispositionError(detail)


def _arguments(argv: tuple[str, ...]) -> _Arguments:
    usage = "usage: disposition_item7_warnings.py --root ROOT --audit AUDIT --output OUTPUT"
    if (
        len(argv) != _ARGUMENT_COUNT
        or argv[0:1] != ("--root",)
        or argv[2:3] != ("--audit",)
        or argv[4:5] != ("--output",)
    ):
        raise SystemExit(usage)
    return _Arguments(root=Path(argv[1]), audit=Path(argv[3]), output=Path(argv[5]))


def _output_path(root: Path, relative: Path) -> Path:
    if relative.is_absolute() or not relative.parts or ".." in relative.parts:
        detail = f"output path is not relative: {relative}"
        _fail(detail)
    target = root / relative
    try:
        _ = target.parent.resolve().relative_to(root.resolve())
    except ValueError:
        detail = f"output path escapes root: {relative}"
        _fail(detail)
    if target.is_symlink():
        detail = f"output path is a symlink: {relative}"
        _fail(detail)
    return target


def run(argv: tuple[str, ...]) -> int:
    """Write the complete strict report only after all validation succeeds."""
    arguments = _arguments(argv)
    report = disposition_audit(arguments.root, arguments.audit)
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
    except OSError:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
        detail = f"cannot write warning disposition: {output}"
        _fail(detail)
    print(f"dispositioned {report.signature_count} warning signatures")
    return 0


def main() -> int:
    """Run the disposition command from the process argument vector."""
    return run(tuple(sys.argv[1:]))


if __name__ == "__main__":
    raise SystemExit(main())
