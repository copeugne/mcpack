#!/usr/bin/env python3
"""Generate exact grouped setting evidence from CristelLib JSON5 files."""

import argparse
import json
from pathlib import Path

from pydantic import BaseModel, TypeAdapter

from mcpack_evidence.item6_surface_validation import build_setting_surface


class _Arguments(BaseModel, frozen=True):
    root: Path
    system: str
    files: list[str]


_ARGUMENTS: TypeAdapter[_Arguments] = TypeAdapter(_Arguments)


def generate(root: Path, system: str, files: list[str]) -> str:
    """Return deterministic JSON for the requested source files."""
    surfaces = [build_setting_surface(system, relative, root / relative) for relative in files]
    return json.dumps(surfaces, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    """Run the grouped-surface generator."""
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("--root", type=Path, required=True)
    _ = parser.add_argument("--system", required=True)
    _ = parser.add_argument("--file", dest="files", action="append", required=True)
    arguments = _ARGUMENTS.validate_python(vars(parser.parse_args()), strict=True)
    print(generate(arguments.root, arguments.system, arguments.files), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
