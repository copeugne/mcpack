#!/usr/bin/env python3
"""Extract deterministic conservative warning signatures from Item 7 logs."""

from __future__ import annotations

import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

from mcpack_evidence.item7_warnings import WarningAuditError, audit_logs

_MIN_ARGUMENTS_BEFORE_OUTPUT = 3


@dataclass(frozen=True, slots=True)
class _Arguments:
    root: Path
    inputs: tuple[Path, ...]
    output: Path


def _parse_args(argv: tuple[str, ...]) -> _Arguments:
    usage = "usage: audit_item7_warnings.py --root ROOT LOG [LOG ...] --output OUTPUT"
    if argv.count("--root") != 1 or argv.count("--output") != 1 or argv[0] != "--root":
        raise SystemExit(usage)
    output_index = argv.index("--output")
    if output_index < _MIN_ARGUMENTS_BEFORE_OUTPUT or output_index != len(argv) - 2:
        raise SystemExit(usage)
    return _Arguments(
        root=Path(argv[1]),
        inputs=tuple(Path(value) for value in argv[2:output_index]),
        output=Path(argv[-1]),
    )


def run(argv: tuple[str, ...]) -> int:
    """Audit explicit arguments and atomically write strict JSON."""
    arguments = _parse_args(argv)
    audit = audit_logs(arguments.inputs, evidence_root=arguments.root)
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            "w",
            encoding="utf-8",
            newline="\n",
            prefix=f".{arguments.output.name}.",
            dir=arguments.output.parent,
            delete=False,
        ) as stream:
            temporary = Path(stream.name)
            _ = stream.write(audit.model_dump_json(indent=2) + "\n")
        _ = temporary.replace(arguments.output)
    except OSError as error:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
        detail = f"cannot write warning audit: {arguments.output}"
        raise WarningAuditError(detail) from error
    print(f"audited {audit.warning_occurrences + audit.error_occurrences} log events")
    return 0


def main() -> int:
    """Audit command-line log inputs and atomically write strict JSON."""
    return run(tuple(sys.argv[1:]))


if __name__ == "__main__":
    raise SystemExit(main())
