"""Frozen Item 7 world-generation audit protocol boundary."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, ClassVar, Final, Literal, Self

from pydantic import BaseModel, ConfigDict, model_validator
from pydantic_core import PydanticCustomError

from mcpack_evidence.item6_json import parse_strict_json

if TYPE_CHECKING:
    from pathlib import Path


class _FrozenModel(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)


class _FrozenConfigSeal(_FrozenModel):
    path: Literal["evidence/item-6/generated-config-manifest.json"]
    sha256: Literal["2e0aaeb0f84747a3cb17146eb435d34cc7d6703b9372211e8fc8cff2df2b436f"]


class _ConfigAuditSeal(_FrozenModel):
    path: Literal["evidence/item-6/config-audit.json"]
    sha256: Literal["181e0c299f44ded319d93c84f7b983738364b4090286251b00421fa041b989dd"]


class _SeedSuiteSeal(_FrozenModel):
    path: Literal["test-environment/seed-suite.json"]
    sha256: Literal["de5e5e89bd04b6f75dac4eab2e84524956f46faa91660b5315c8eade269d39ae"]
    schema_version: Literal["item4-seed-suite-v1"]


class _RetainedManifestSeal(_FrozenModel):
    path: Literal["evidence/item-3/runtime/retained-server-candidates.txt"]
    sha256: Literal["78e5bdc0697299782a535400ad5b313c088e8db10cfe075085ae4c8a531e30cb"]
    count: Literal[136]


class _FrozenIdentity(_FrozenModel):
    minecraft_version: Literal["1.21.1"]
    neoforge_version: Literal["21.1.249"]
    java_build: Literal["Temurin-21.0.12.1+1-LTS"]
    java_archive_sha256: Literal["ce79869e1307ed8ee1e2baa86a412b1eb5b75d10a01006d788a6f968bcfaee94"]
    configuration_version: Literal["test-environment-v0.1"]
    frozen_config_manifest: _FrozenConfigSeal
    config_audit: _ConfigAuditSeal
    retained_manifest: _RetainedManifestSeal
    seed_suite: _SeedSuiteSeal


class _Seed(_FrozenModel):
    role: Literal["ordinary", "mountainous", "ocean-heavy", "biome-diverse"]
    seed: str


class _Selection(_FrozenModel):
    label: Literal["overworld", "nether", "end-central", "end-outer"]
    dimension: Literal["minecraft:overworld", "minecraft:the_nether", "minecraft:the_end"]
    coordinate_unit: Literal["block"]
    center_x: int
    center_z: int
    radius_chunks: int
    expected_chunk_count: int


class _GenerationLimits(_FrozenModel):
    maximum_passes_per_selection: Literal[3]
    maximum_provider_gap_targets: Literal[24]


class _ProviderTarget(_FrozenModel):
    label: str
    observation_role: Literal["direct", "library"]


class _NormalizationPolicy(_FrozenModel):
    chunk_compare_fields: tuple[str, ...]
    excluded_transport_fields: tuple[str, ...]
    raw_region_hash_treatment: Literal["preserve_and_explain_not_compare"]


class _RegionPolicy(_FrozenModel):
    account_every_chunk_region_mca_file: Literal[True]
    kinds: tuple[Literal["anvil", "empty_placeholder"], ...]
    empty_placeholder_size_bytes: Literal[0]
    anvil_sector_bytes: Literal[4096]
    unexplained_files_allowed: Literal[False]


class _ArchivePolicy(_FrozenModel):
    storage: Literal["external_immutable_archive"]
    committed_receipts_root: Literal["evidence/item-7"]
    required_contents: tuple[str, ...]
    forbidden_contents: tuple[str, ...]
    required_identity_fields: tuple[str, ...]
    restore_required: Literal[True]


_SEEDS: Final = (
    ("ordinary", "42"),
    ("mountainous", "6671238423019257953"),
    ("ocean-heavy", "95920844204830198"),
    ("biome-diverse", "-3503646078644842058"),
)
_SELECTIONS: Final = (
    ("overworld", "minecraft:overworld", 0, 0, 31, 3969),
    ("nether", "minecraft:the_nether", 0, 0, 15, 961),
    ("end-central", "minecraft:the_end", 0, 0, 15, 961),
    ("end-outer", "minecraft:the_end", 1536, 0, 15, 961),
)
_PROVIDERS: Final = (
    ("Tectonic", "direct"),
    ("Terralith", "direct"),
    ("Biomes O' Plenty", "direct"),
    ("Regions Unexplored", "direct"),
    ("TerraBlender", "library"),
    ("Lithostitched", "library"),
    ("BetterEnd", "direct"),
    ("YUNG", "direct"),
    ("WDA", "direct"),
    ("IDAS", "direct"),
    ("Integrated structures", "direct"),
    ("Moog", "direct"),
    ("Explorify", "direct"),
    ("Explorations", "direct"),
    ("Repurposed Structures", "direct"),
    ("CTOV", "direct"),
    ("Towns & Towers", "direct"),
)
_ANOMALIES: Final = (
    "fragmented_biomes",
    "tiny_biomes",
    "unnatural_terrain_transitions",
    "buried_structures",
    "floating_structures",
    "cliff_intersections",
    "bad_underwater_placement",
    "overlapping_structures",
    "overlapping_villages",
    "failed_placements",
    "impossible_biome_restrictions",
    "excessive_terrain_modification",
)
_CLASSIFICATIONS: Final = (
    "cosmetic",
    "gameplay",
    "performance",
    "outright_generation_failure",
)
_COMPARE_FIELDS: Final = (
    "schema_version",
    "dimension",
    "slot",
    "chunk_x",
    "chunk_z",
    "data_version",
    "status",
    "full",
    "heightmaps",
    "biome_sections",
    "structure_starts",
)
_EXCLUDED_FIELDS: Final = ("region", "timestamp", "compression", "external")
_ARCHIVE_REQUIRED: Final = (
    "region_files",
    "logs",
    "run_manifests",
    "decoded_jsonl",
    "render_sources",
    "galleries",
    "screenshots",
    "failed_attempts",
)
_ARCHIVE_FORBIDDEN: Final = (
    "instances",
    "jar_files",
    "minecraft_or_neoforge_binaries",
    "credentials",
    "session_lock",
    "player_data",
    "caches",
)
_ARCHIVE_IDENTITY: Final = (
    "archive_name",
    "sha256",
    "size_bytes",
    "file_count",
    "commit",
    "tag",
    "durable_location",
    "restore_receipt",
)


def _mismatch(field: str) -> PydanticCustomError:
    return PydanticCustomError(
        "frozen_protocol_mismatch", "protocol {field} differs from frozen value", {"field": field}
    )


class Item7Protocol(_FrozenModel):
    """The exact, closed Item 7 experiment contract."""

    schema_version: Literal["item7-worldgen-audit-v1"]
    identity: _FrozenIdentity
    runs: tuple[Literal["run-a"], Literal["run-b"]]
    seeds: tuple[_Seed, ...]
    selections: tuple[_Selection, ...]
    generation: _GenerationLimits
    providers: tuple[_ProviderTarget, ...]
    anomaly_classes: tuple[str, ...]
    primary_classifications: tuple[str, ...]
    normalization: _NormalizationPolicy
    regions: _RegionPolicy
    archive: _ArchivePolicy

    @model_validator(mode="after")
    def require_frozen_collections(self) -> Self:
        """Reject omissions, duplicates, reordering, and cross-field drift."""
        checks = (
            ("seeds", tuple((row.role, row.seed) for row in self.seeds), _SEEDS),
            (
                "selections",
                tuple(
                    (
                        row.label,
                        row.dimension,
                        row.center_x,
                        row.center_z,
                        row.radius_chunks,
                        row.expected_chunk_count,
                    )
                    for row in self.selections
                ),
                _SELECTIONS,
            ),
            (
                "providers",
                tuple((row.label, row.observation_role) for row in self.providers),
                _PROVIDERS,
            ),
            ("anomaly_classes", self.anomaly_classes, _ANOMALIES),
            ("primary_classifications", self.primary_classifications, _CLASSIFICATIONS),
            (
                "normalization.chunk_compare_fields",
                self.normalization.chunk_compare_fields,
                _COMPARE_FIELDS,
            ),
            (
                "normalization.excluded_transport_fields",
                self.normalization.excluded_transport_fields,
                _EXCLUDED_FIELDS,
            ),
            ("regions.kinds", self.regions.kinds, ("anvil", "empty_placeholder")),
            ("archive.required_contents", self.archive.required_contents, _ARCHIVE_REQUIRED),
            ("archive.forbidden_contents", self.archive.forbidden_contents, _ARCHIVE_FORBIDDEN),
            (
                "archive.required_identity_fields",
                self.archive.required_identity_fields,
                _ARCHIVE_IDENTITY,
            ),
        )
        for field, actual, expected in checks:
            if actual != expected:
                raise _mismatch(field)
        return self


def load_protocol(path: Path) -> Item7Protocol:
    """Parse one strict Item 7 protocol JSON boundary."""
    document = parse_strict_json(path.read_bytes())
    return Item7Protocol.model_validate_json(json.dumps(document, separators=(",", ":")))
