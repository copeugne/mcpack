"""Parse exact Chunky completion output for Item 7 gap targets."""

from __future__ import annotations

from typing import Final

from mcpack_evidence.item7_runtime import Item7RuntimeError

_COMPLETE = "Task finished for minecraft:overworld. Processed: 81 chunks (100.00%)"
_LIFECYCLE_STAGE: Final = "lifecycle"
_MARKER_ERROR: Final = "completion marker differs from requested target"


def parse_completion(line: str, target_structure: str) -> str:
    """Return the completed target after matching its exact Chunky marker."""
    if _COMPLETE not in line:
        raise Item7RuntimeError(_LIFECYCLE_STAGE, _MARKER_ERROR)
    return target_structure
