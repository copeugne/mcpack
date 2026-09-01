"""Write a deterministic content manifest for ignored raw evidence."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import cast

from mcpack_evidence.raw_manifest import build_raw_manifest


def main() -> int:
    """Hash a raw evidence tree and persist the machine-readable manifest."""
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("--root", type=Path, required=True)
    _ = parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    root = cast("Path", arguments.root)
    output = cast("Path", arguments.output)
    manifest = build_raw_manifest(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    _ = output.write_text(manifest.model_dump_json(indent=2) + "\n", encoding="utf-8")
    print(f"hashed {manifest.file_count} files ({manifest.total_size_bytes} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
