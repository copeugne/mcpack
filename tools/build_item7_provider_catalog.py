"""Write a provenance-bound Item 7 provider catalog."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import ClassVar

from pydantic import BaseModel, ConfigDict

from mcpack_evidence.item7_provider import CatalogInputs, build_provider_catalog


class _Arguments(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)

    repository: Path
    output: Path


def _arguments() -> _Arguments:
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("--repository", type=Path, default=Path())
    _ = parser.add_argument("--output", type=Path, required=True)
    return _Arguments.model_validate(vars(parser.parse_args()), strict=True)


def main() -> int:
    """Build the catalog from the exact retained Item 3 evidence boundary."""
    arguments = _arguments()
    catalog = build_provider_catalog(CatalogInputs.from_repository(arguments.repository))
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    _ = arguments.output.write_text(catalog.model_dump_json(indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
