"""Build the strict Item 7 completion receipt."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import ClassVar, Final

from pydantic import BaseModel, ConfigDict

from mcpack_evidence.item7_completion import CompletionInputs, build_completion

_VISUAL_REVIEWS: Final = 2
_ARCHIVES: Final = 4


class _Arguments(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)

    raw_root: Path
    protocol: Path
    provider_catalog: Path
    provider_coverage: Path
    provider_disposition: Path
    restriction_audit: Path
    world_archive_inventory: Path
    repeat_comparison: Path
    warning_audit: Path
    warning_disposition: Path
    control_comparison: Path
    visual_manifest: Path
    publication: Path
    output: Path
    visual_review: list[Path]
    archive_manifest: list[Path]
    restore_receipt: list[Path]


def build_parser() -> argparse.ArgumentParser:
    """Define the explicit evidence-surface command line."""
    parser = argparse.ArgumentParser()
    for flag in (
        "raw-root",
        "protocol",
        "provider-catalog",
        "provider-coverage",
        "provider-disposition",
        "restriction-audit",
        "world-archive-inventory",
        "repeat-comparison",
        "warning-audit",
        "warning-disposition",
        "control-comparison",
        "visual-manifest",
        "publication",
        "output",
    ):
        _ = parser.add_argument(f"--{flag}", type=Path, required=True)
    _ = parser.add_argument("--visual-review", action="append", type=Path, required=True)
    _ = parser.add_argument("--archive-manifest", action="append", type=Path, required=True)
    _ = parser.add_argument("--restore-receipt", action="append", type=Path, required=True)
    return parser


def run(arguments: tuple[str, ...]) -> int:
    """Validate arguments, build the receipt, and print its binary verdict."""
    values = _Arguments.model_validate(vars(build_parser().parse_args(arguments)), strict=True)
    visual_reviews = tuple(values.visual_review)
    archive_manifests = tuple(values.archive_manifest)
    restore_receipts = tuple(values.restore_receipt)
    if (
        len(visual_reviews) != _VISUAL_REVIEWS
        or len(archive_manifests) != _ARCHIVES
        or len(restore_receipts) != _ARCHIVES
    ):
        message = "exactly 2 visual reviews and 4 archive/restore pairs are required"
        raise SystemExit(message)
    report = build_completion(
        CompletionInputs(
            raw_root=values.raw_root,
            protocol=values.protocol,
            provider_catalog=values.provider_catalog,
            provider_coverage=values.provider_coverage,
            provider_disposition=values.provider_disposition,
            restriction_audit=values.restriction_audit,
            world_archive_inventory=values.world_archive_inventory,
            repeat_comparison=values.repeat_comparison,
            warning_audit=values.warning_audit,
            warning_disposition=values.warning_disposition,
            control_comparison=values.control_comparison,
            visual_manifest=values.visual_manifest,
            output=values.output,
            visual_reviews=(visual_reviews[0], visual_reviews[1]),
            archive_manifests=(
                archive_manifests[0],
                archive_manifests[1],
                archive_manifests[2],
                archive_manifests[3],
            ),
            restore_receipts=(
                restore_receipts[0],
                restore_receipts[1],
                restore_receipts[2],
                restore_receipts[3],
            ),
            publication=values.publication,
        )
    )
    print(report.exit_gate)
    return 0


if __name__ == "__main__":
    raise SystemExit(run(tuple(sys.argv[1:])))
