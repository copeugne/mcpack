from __future__ import annotations

import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

from mcpack_evidence.item7_anvil import decode_region, world_regions


@dataclass(frozen=True, slots=True)
class _Arguments:
    world: Path
    output: Path


def _parse_args(argv: tuple[str, ...]) -> _Arguments:
    if len(argv) != 3 or argv[1] != "--output":
        raise SystemExit("usage: decode_item7_world.py WORLD --output OUTPUT")
    return _Arguments(world=Path(argv[0]), output=Path(argv[2]))


def _main(argv: tuple[str, ...]) -> int:
    args = _parse_args(argv)
    if not args.world.is_dir():
        parser_error = f"world directory does not exist: {args.world}"
        raise SystemExit(parser_error)
    count = 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        newline="\n",
        prefix=f".{args.output.name}.",
        dir=args.output.parent,
        delete=False,
    ) as stream:
        temporary = Path(stream.name)
        try:
            for region, context in world_regions(args.world):
                for record in decode_region(region, context):
                    _ = stream.write(record.model_dump_json())
                    _ = stream.write("\n")
                    count += 1
        except Exception:
            temporary.unlink(missing_ok=True)
            raise
    _ = temporary.replace(args.output)
    print(f"decoded {count} chunks to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(_main(tuple(sys.argv[1:])))
