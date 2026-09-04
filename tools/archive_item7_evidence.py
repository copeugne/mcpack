"""Create and verify external Item 7 raw-evidence archives."""

from __future__ import annotations

import sys
from enum import StrEnum
from pathlib import Path
from typing import TYPE_CHECKING, Final

from mcpack_evidence.item7_archive import (
    ArchiveRequest,
    RestoreRequest,
    create_archive,
    restore_archive,
)

if TYPE_CHECKING:
    from collections.abc import Mapping

_USAGE: Final = (
    "usage: archive_item7_evidence.py create --root ROOT --archive ARCHIVE "
    "--manifest MANIFEST --revision REVISION\n"
    "   or: archive_item7_evidence.py restore --archive ARCHIVE --manifest MANIFEST "
    "--target TARGET --receipt RECEIPT"
)
_CREATE_FLAGS: Final = frozenset({"--root", "--archive", "--manifest", "--revision"})
_RESTORE_FLAGS: Final = frozenset({"--archive", "--manifest", "--target", "--receipt"})


class _Command(StrEnum):
    CREATE = "create"
    RESTORE = "restore"


def _parse_options(arguments: tuple[str, ...]) -> Mapping[str, str]:
    if len(arguments) % 2 != 0:
        raise SystemExit(_USAGE)
    options: dict[str, str] = {}
    for index in range(0, len(arguments), 2):
        flag, value = arguments[index : index + 2]
        if not flag.startswith("--") or flag in options or not value:
            raise SystemExit(_USAGE)
        options[flag] = value
    return options


def _require_flags(options: Mapping[str, str], expected: frozenset[str]) -> None:
    if frozenset(options) != expected:
        raise SystemExit(_USAGE)


def run(arguments: tuple[str, ...]) -> int:
    """Execute one archive or restore command."""
    if not arguments:
        raise SystemExit(_USAGE)
    try:
        command = _Command(arguments[0])
    except ValueError:
        raise SystemExit(_USAGE) from None
    options = _parse_options(arguments[1:])
    handlers = {_Command.CREATE: _create, _Command.RESTORE: _restore}
    handlers[command](options)
    return 0


def _create(options: Mapping[str, str]) -> None:
    _require_flags(options, _CREATE_FLAGS)
    manifest = create_archive(
        ArchiveRequest(
            root=Path(options["--root"]),
            archive=Path(options["--archive"]),
            manifest=Path(options["--manifest"]),
            revision=options["--revision"],
        )
    )
    print(f"archived {manifest.file_count} files as {manifest.archive_name}")


def _restore(options: Mapping[str, str]) -> None:
    _require_flags(options, _RESTORE_FLAGS)
    receipt = restore_archive(
        RestoreRequest(
            archive=Path(options["--archive"]),
            manifest=Path(options["--manifest"]),
            target=Path(options["--target"]),
            receipt=Path(options["--receipt"]),
        )
    )
    print(f"verified and restored {receipt.file_count} files")


if __name__ == "__main__":
    raise SystemExit(run(tuple(sys.argv[1:])))
