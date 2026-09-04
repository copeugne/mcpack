#!/usr/bin/env python3
"""Render one decoded Item 7 JSONL selection into an offline SVG gallery."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import ClassVar

from pydantic import BaseModel, ConfigDict, TypeAdapter

from mcpack_evidence.item6_json import StrictJsonError, parse_strict_json
from mcpack_evidence.item7_render import RenderInputError, RenderMetadata, render_jsonl

_REGION_HASHES: TypeAdapter[dict[str, str]] = TypeAdapter(dict[str, str])


class _Arguments(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="forbid", frozen=True, strict=True)

    chunks: Path
    output: Path
    run_id: str
    seed_role: str
    seed: str
    dimension: str
    region_hashes: Path
    expected_chunks_sha256: str | None

    def run(self) -> int:
        metadata = RenderMetadata(
            self.run_id,
            self.seed_role,
            self.seed,
            self.dimension,
            _read_region_hashes(self.region_hashes),
        )
        render_jsonl(
            self.chunks,
            self.output,
            metadata,
            expected_chunks_sha256=self.expected_chunks_sha256,
        )
        print(f"rendered Item 7 gallery: {self.output}")
        return 0


def _read_region_hashes(path: Path) -> dict[str, str]:
    try:
        document = parse_strict_json(path.read_bytes())
        return _REGION_HASHES.validate_python(document, strict=True)
    except (OSError, StrictJsonError, ValueError) as error:
        message = f"invalid Item 7 region-hash manifest: {path}"
        raise RenderInputError(message) from error


def main() -> int:
    """Parse render inputs and create one deterministic gallery."""
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("--chunks", type=Path, required=True)
    _ = parser.add_argument("--output", type=Path, required=True)
    _ = parser.add_argument("--run-id", required=True)
    _ = parser.add_argument("--seed-role", required=True)
    _ = parser.add_argument("--seed", required=True)
    _ = parser.add_argument("--dimension", required=True)
    _ = parser.add_argument("--region-hashes", type=Path, required=True)
    _ = parser.add_argument("--expected-chunks-sha256")
    arguments = _Arguments.model_validate(vars(parser.parse_args()), strict=True)
    return arguments.run()


if __name__ == "__main__":
    raise SystemExit(main())
