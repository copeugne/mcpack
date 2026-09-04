"""Build hash-bound Item 7 stopped-world evidence."""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

from mcpack_evidence.item7_world_manifest import ManifestMode, build_world_manifest


@dataclass(frozen=True, slots=True)
class _Arguments:
    world: Path
    manifest: Path
    decoded: Path
    mode: ManifestMode


def _mode(value: str) -> ManifestMode:
    if value == "control":
        return "control"
    if value == "pilot":
        return "pilot"
    if value == "run":
        return "run"
    detail = f"invalid mode: {value}"
    raise SystemExit(detail)


def _parse(argv: tuple[str, ...]) -> _Arguments:
    expected = ("--manifest", "--decoded", "--mode")
    argument_count = len(expected) * 2 + 1
    if len(argv) != argument_count or tuple(argv[index] for index in range(1, 7, 2)) != expected:
        command = "build_item7_world_manifest.py"
        outputs = "WORLD --manifest JSON --decoded JSONL"
        usage = f"usage: {command} {outputs} --mode control|pilot|run"
        raise SystemExit(usage)
    return _Arguments(
        world=Path(argv[0]),
        manifest=Path(argv[2]),
        decoded=Path(argv[4]),
        mode=_mode(argv[6]),
    )


def _main(argv: tuple[str, ...]) -> int:
    arguments = _parse(argv)
    result = build_world_manifest(
        arguments.world,
        arguments.manifest,
        arguments.decoded,
        mode=arguments.mode,
    )
    print(f"validated {result.record_count} chunks to {arguments.manifest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(_main(tuple(sys.argv[1:])))
