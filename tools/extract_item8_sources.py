"""Extract hash-bound packaged JSON with uv run -m tools.extract_item8_sources."""

from __future__ import annotations

import argparse
import gzip
import json
from pathlib import Path
from typing import cast

from mcpack_evidence.item8_sources import packaged_json_sources, retained_sources


def main() -> None:
    """Write deterministic compressed source evidence without overwriting an attempt."""
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    _ = parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = cast("Path", args.root)
    output = cast("Path", args.output)
    result = packaged_json_sources(retained_sources(root))
    raw = (json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n").encode()
    with output.open("xb") as stream:
        _ = stream.write(gzip.compress(raw, mtime=0))


if __name__ == "__main__":
    main()
