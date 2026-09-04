"""Validate the accepted Item 7 lifecycle save ordering in restored raw evidence."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import TYPE_CHECKING

from mcpack_evidence.item7_runtime import Item7RuntimeError
from mcpack_evidence.item7_save_sequence import build_save_sequence_audit

if TYPE_CHECKING:
    from collections.abc import Sequence

_ARGUMENT_COUNT = 6
_USAGE_EXIT = 2


def main(arguments: Sequence[str]) -> int:
    """Print the source-bound audit for every accepted recovery lifecycle."""
    if (
        len(arguments) != _ARGUMENT_COUNT
        or arguments[0] != "--core"
        or arguments[2] != "--manifest"
        or arguments[4] != "--world-inventory"
    ):
        usage = (
            "usage: validate_item7_save_sequence.py --core PATH "
            "--manifest JSON --world-inventory JSON"
        )
        print(usage)
        return _USAGE_EXIT
    try:
        manifest = Path(arguments[3])
        payload = build_save_sequence_audit(Path(arguments[1]), manifest, Path(arguments[5]))
    except Item7RuntimeError as error:
        print(str(error))
        return 1
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
