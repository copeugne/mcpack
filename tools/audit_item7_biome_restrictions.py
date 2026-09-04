"""Write the retained-provider packaged biome-restriction audit."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import ClassVar

from pydantic import BaseModel, ConfigDict

from mcpack_evidence.item7_restriction_inputs import (
    repository_inputs,
    sha256_path,
)
from mcpack_evidence.item7_restrictions import audit_restrictions


class _Arguments(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)

    repository: Path
    provider_catalog: Path
    output: Path


def main() -> int:
    """Build the deterministic restriction report from frozen archives."""
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("--repository", type=Path, default=Path())
    _ = parser.add_argument("--provider-catalog", type=Path, required=True)
    _ = parser.add_argument("--output", type=Path, required=True)
    options = _Arguments.model_validate(vars(parser.parse_args()), strict=True)
    repository = options.repository.resolve()
    catalog = options.provider_catalog.resolve()
    report = audit_restrictions(repository_inputs(repository, catalog), sha256_path(catalog))
    options.output.parent.mkdir(parents=True, exist_ok=True)
    _ = options.output.write_text(report.model_dump_json(indent=2) + "\n", encoding="utf-8")
    message = (
        f"PASS: inspected {report.structure_count} structures; recorded "
        f"{report.candidate_count} impossible restrictions"
    )
    print(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
