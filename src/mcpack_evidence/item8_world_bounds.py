"""Observed piece envelopes from the preserved Item 7 decoded starts."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pydantic import JsonValue

    from .item7_nbt_models import ChunkRecord


def observed_bounds(record: ChunkRecord) -> list[JsonValue]:
    """Retain starts with inclusive piece envelopes, not occupied-block footprints."""
    result: list[JsonValue] = []
    for start in record.structure_starts:
        if any(box.bounds[axis] > box.bounds[axis + 3] for box in start.boxes for axis in range(3)):
            message = f"reversed piece bounds: {start.structure_id}"
            raise ValueError(message)
        envelope = (
            [min(box.bounds[axis] for box in start.boxes) for axis in range(3)]
            + [max(box.bounds[axis + 3] for box in start.boxes) for axis in range(3)]
            if start.boxes
            else None
        )
        result.append(
            {
                "structure_id": start.structure_id,
                "start_id": start.start_id,
                "dimension": record.dimension,
                "chunk_x": record.chunk_x,
                "chunk_z": record.chunk_z,
                "chunk_status": record.status,
                "chunk_full": record.full,
                "piece_boxes": [list(box.bounds) for box in start.boxes],
                "envelope": list(envelope) if envelope is not None else None,
                "size_xyz": (
                    [envelope[axis + 3] - envelope[axis] + 1 for axis in range(3)]
                    if envelope is not None
                    else None
                ),
            }
        )
    return result
