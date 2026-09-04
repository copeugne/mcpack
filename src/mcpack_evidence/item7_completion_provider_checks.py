"""Provider evidence-shape and input-identity checks for Item 7 completion."""

from __future__ import annotations

from pathlib import Path  # noqa: TC003
from typing import TYPE_CHECKING, Final

from mcpack_evidence.item7_completion_io import fail, portable_path, sha256_file

if TYPE_CHECKING:
    from pydantic import JsonValue

    from mcpack_evidence.item7_completion_models import ProviderDisposition

_FINAL_PROVIDER_COUNT: Final = 37
_TARGETED_RUN_COUNT: Final = 2
_EXPECTED_PROVIDER_IDS: Final = {
    "direct_observed": frozenset(
        {
            "betterdungeons",
            "betterend",
            "betterfortresses",
            "betterjungletemples",
            "bettermineshafts",
            "betteroceanmonuments",
            "biomesoplenty",
            "ctov",
            "dungeons_arise",
            "dungeons_arise_seven_seas",
            "explorations",
            "explorify",
            "idas",
            "integrated_villages",
            "mes",
            "mns",
            "mss",
            "mvs",
            "regions_unexplored",
            "repurposed_structures",
            "t_and_t",
            "terralith",
            "yungscavebiomes",
        }
    ),
    "targeted_observed": frozenset(
        {
            "betterdeserttemples",
            "betterstrongholds",
            "betterwitchhuts",
            "integrated_stronghold",
        }
    ),
    "observed_generation_failure": frozenset({"bettercaves"}),
    "indirect_observed": frozenset(
        {
            "betterendisland",
            "integrated_api",
            "lithostitched",
            "moogs_structures",
            "tectonic",
            "terrablender",
            "yungsapi",
        }
    ),
    "not_observed_with_limit": frozenset({"yungsbridges", "yungsextras"}),
}
_EXPECTED_TARGETS: Final = {
    "betterdeserttemples": ("betterdeserttemples:desert_temple", -46, -289),
    "betterstrongholds": ("betterstrongholds:stronghold", 41, -320),
    "betterwitchhuts": ("betterwitchhuts:witch_hut", 65, -870),
    "integrated_stronghold": ("integrated_stronghold:stronghold", -112, -662),
}


def validate_provider_evidence_shape(
    report: ProviderDisposition,
    path: Path,
    expected_count: int,
) -> None:
    """Require each disposition to carry its matching evidence shape and final identity."""
    components = tuple(component for label in report.labels for component in label.components)
    for component in components:
        direct = component.disposition == "direct_observed"
        targeted = component.disposition == "targeted_observed"
        action_required = component.disposition in {
            "observed_generation_failure",
            "not_observed_with_limit",
        }
        if (
            bool(component.direct_observations) != direct
            or bool(component.targeted_starts) != targeted
            or (targeted and len(component.targeted_starts) != _TARGETED_RUN_COUNT)
            or (action_required and not component.downstream_action)
            or not component.limitation
        ):
            fail("provider disposition evidence shape", component.mod_id)
    if expected_count != _FINAL_PROVIDER_COUNT:
        return
    actual_ids = {
        status: frozenset(
            component.mod_id for component in components if component.disposition == status
        )
        for status in _EXPECTED_PROVIDER_IDS
    }
    if actual_ids != _EXPECTED_PROVIDER_IDS:
        fail("provider final disposition identities", path)
    targeted_starts = {
        component.mod_id: tuple(
            _target_identity(path, value) for value in component.targeted_starts
        )
        for component in components
        if component.disposition == "targeted_observed"
    }
    expected_starts = {
        mod_id: tuple((run, *target) for run in ("gap-a", "gap-b"))
        for mod_id, target in _EXPECTED_TARGETS.items()
    }
    if targeted_starts != expected_starts:
        fail("provider targeted start identities", path)


def validate_provider_inputs(
    report: ProviderDisposition,
    catalog_path: Path,
    coverage_path: Path,
    raw_root: Path,
    report_path: Path,
) -> None:
    """Bind every provider closure input to the exact preserved file bytes."""
    expected = {
        "repository/evidence/item-7/provider-catalog.json": catalog_path,
        "raw/run-a/provider-coverage.json": coverage_path,
        "raw/run-a/mountainous/minecraft-latest.log": (
            raw_root / "run-a/mountainous/minecraft-latest.log"
        ),
        "raw/gap-a/ordinary/run-receipt.json": raw_root / "gap-a/ordinary/run-receipt.json",
        "raw/gap-a/ordinary/chunks.jsonl": raw_root / "gap-a/ordinary/chunks.jsonl",
        "raw/gap-a/ordinary/gap-minecraft-latest.log": (
            raw_root / "gap-a/ordinary/gap-minecraft-latest.log"
        ),
        "raw/gap-b/ordinary/run-receipt.json": raw_root / "gap-b/ordinary/run-receipt.json",
        "raw/gap-b/ordinary/chunks.jsonl": raw_root / "gap-b/ordinary/chunks.jsonl",
        "raw/gap-b/ordinary/gap-minecraft-latest.log": (
            raw_root / "gap-b/ordinary/gap-minecraft-latest.log"
        ),
    }
    bindings: dict[str, tuple[str, int]] = {}
    for value in report.inputs:
        if not isinstance(value, dict) or set(value) != {
            "path",
            "sha256",
            "size_bytes",
            "record_count",
        }:
            fail("provider input binding shape", report_path)
        logical_path = value["path"]
        digest = value["sha256"]
        size = value["size_bytes"]
        if (
            not isinstance(logical_path, str)
            or not isinstance(digest, str)
            or not isinstance(size, int)
            or isinstance(size, bool)
            or logical_path in bindings
        ):
            fail("provider input binding value", report_path)
        bindings[portable_path(logical_path)] = (digest, size)
    if set(bindings) != set(expected):
        fail("provider input binding accounting", report_path)
    for logical_path, source in expected.items():
        if bindings[logical_path] != (sha256_file(source), source.stat().st_size):
            fail("provider input binding identity", logical_path)


def _target_identity(path: Path, value: JsonValue) -> tuple[str, str, int, int]:
    if not isinstance(value, dict) or set(value) != {
        "run",
        "structure_id",
        "chunk_x",
        "chunk_z",
    }:
        fail("provider targeted start shape", path)
    run = value["run"]
    structure_id = value["structure_id"]
    chunk_x = value["chunk_x"]
    chunk_z = value["chunk_z"]
    if (
        not isinstance(run, str)
        or not isinstance(structure_id, str)
        or not isinstance(chunk_x, int)
        or isinstance(chunk_x, bool)
        or not isinstance(chunk_z, int)
        or isinstance(chunk_z, bool)
    ):
        fail("provider targeted start value", path)
    return run, structure_id, chunk_x, chunk_z
