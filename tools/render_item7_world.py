#!/usr/bin/env python3
"""Render one decoded Item 7 JSONL selection into an offline SVG gallery."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import ClassVar, Literal

from pydantic import BaseModel, ConfigDict, ValidationError

from mcpack_evidence.item6_json import StrictJsonError, parse_strict_json
from mcpack_evidence.item7_render import RenderInputError, RenderMetadata, render_jsonl
from mcpack_evidence.item7_repeat import RepeatWorldManifest


class _Arguments(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid", frozen=True, strict=True)

    chunks: Path
    output: Path
    run_id: str
    seed_role: str
    seed: str
    dimension: str
    selection: Literal["overworld", "nether", "end-central", "end-outer"]
    world_manifest: Path
    expected_chunks_sha256: str | None

    def run(self) -> int:
        metadata = RenderMetadata(
            self.run_id,
            self.seed_role,
            self.seed,
            self.dimension,
            self.selection,
            read_region_hashes(self.world_manifest, self.dimension),
        )
        render_jsonl(
            self.chunks,
            self.output,
            metadata,
            expected_chunks_sha256=self.expected_chunks_sha256,
        )
        print(f"rendered Item 7 gallery: {self.output}")
        return 0


def read_region_hashes(path: Path, dimension: str) -> dict[str, str]:
    """Read region identities for one dimension from a strict stopped-world manifest."""
    try:
        document = parse_strict_json(path.read_bytes())
        encoded = json.dumps(document, separators=(",", ":"))
        manifest = RepeatWorldManifest.model_validate_json(encoded, strict=True)
    except (OSError, StrictJsonError, ValidationError) as error:
        message = f"invalid Item 7 world manifest: {path}"
        raise RenderInputError(message) from error
    hashes = {row.path: row.sha256 for row in manifest.regions if row.dimension == dimension}
    if not hashes:
        message = f"world manifest has no regions for dimension: {dimension}"
        raise RenderInputError(message)
    return hashes


def main() -> int:
    """Parse render inputs and create one deterministic gallery."""
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("--chunks", type=Path, required=True)
    _ = parser.add_argument("--output", type=Path, required=True)
    _ = parser.add_argument("--run-id", required=True)
    _ = parser.add_argument("--seed-role", required=True)
    _ = parser.add_argument("--seed", required=True)
    _ = parser.add_argument("--dimension", required=True)
    _ = parser.add_argument(
        "--selection", choices=("overworld", "nether", "end-central", "end-outer"), required=True
    )
    _ = parser.add_argument("--world-manifest", type=Path, required=True)
    _ = parser.add_argument("--expected-chunks-sha256")
    arguments = _Arguments.model_validate(vars(parser.parse_args()), strict=True)
    return arguments.run()


if __name__ == "__main__":
    raise SystemExit(main())
