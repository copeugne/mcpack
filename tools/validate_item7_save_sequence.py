"""Validate the accepted Item 7 lifecycle save ordering in restored raw evidence."""

from __future__ import annotations

import hashlib
import json
import sys
from dataclasses import asdict
from pathlib import Path
from typing import TYPE_CHECKING

from mcpack_evidence.item7_runtime import Item7RuntimeError
from mcpack_evidence.item7_save_sequence import validate_save_sequences

if TYPE_CHECKING:
    from collections.abc import Sequence

_ARGUMENT_COUNT = 4
_USAGE_EXIT = 2


def main(arguments: Sequence[str]) -> int:
    """Print JSON line-order records for every accepted lifecycle console log."""
    if (
        len(arguments) != _ARGUMENT_COUNT
        or arguments[0] != "--core"
        or arguments[2] != "--manifest"
    ):
        print("usage: validate_item7_save_sequence.py --core PATH --manifest JSON")
        return _USAGE_EXIT
    try:
        manifest = Path(arguments[3])
        records = validate_save_sequences(Path(arguments[1]), manifest)
    except Item7RuntimeError as error:
        print(str(error))
        return 1
    payload = {
        "schema_version": "item7-save-sequence-audit-v1",
        "core_manifest": {
            "path": str(manifest),
            "size_bytes": manifest.stat().st_size,
            "sha256": hashlib.sha256(manifest.read_bytes()).hexdigest(),
        },
        "records": [asdict(record) for record in records],
    }
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
