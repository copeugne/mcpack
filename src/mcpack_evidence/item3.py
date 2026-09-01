"""Item 3 exact-candidate audit contracts and discovery helpers."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING, ClassVar, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence
    from pathlib import Path

AuditStatus = Literal["pass", "fail", "unverified", "not_applicable"]
Disposition = Literal[
    "retain_candidate",
    "replace_candidate",
    "client_only_exclude_from_server",
    "reject_unsupported",
    "reject_design_conflict",
    "defer_not_admitted",
]


class ExactFileMatch(BaseModel):
    """An exact filename occurrence in one Modrinth version record."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    version_id: str
    filename: str
    file_index: int = Field(ge=0)


class _ModrinthFileRecord(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore")

    filename: str


class _ModrinthVersionRecord(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore")

    id: str
    files: tuple[_ModrinthFileRecord, ...]


class SourceRecord(BaseModel):
    """Primary file-record source for one candidate."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    platform: Literal["modrinth", "curseforge", "unresolved"]
    project_id: str | None
    version_id: str | None
    file_id: int | None
    source_url: str
    retrieved_at: str


class ArtifactIdentity(BaseModel):
    """Publisher and optional local identity for an exact candidate file."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    exact_filename: str
    size_bytes: int | None = Field(default=None, ge=0)
    publisher_hashes: dict[str, str]
    computed_sha256: str | None = Field(default=None, pattern=r"^[0-9a-f]{64}$")


class DependencyRecord(BaseModel):
    """One declared dependency edge from publisher or embedded metadata."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    dependency_type: Literal["required", "optional", "incompatible", "embedded"]
    project_id: str | None
    version_id: str | None
    mod_id: str | None = None
    version_range: str | None = None


class DeclaredMetadata(BaseModel):
    """Platform-declared compatibility metadata."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    game_versions: tuple[str, ...]
    loaders: tuple[str, ...]
    client_side: str
    server_side: str
    dependencies: tuple[DependencyRecord, ...]


class EmbeddedMetadata(BaseModel):
    """Normalized metadata extracted from a downloaded candidate JAR."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    metadata_paths: tuple[str, ...]
    mod_ids: tuple[str, ...]
    minecraft_ranges: tuple[str, ...]
    neoforge_ranges: tuple[str, ...]
    dependencies: tuple[DependencyRecord, ...]
    embedded_libraries: tuple[str, ...]


class CompatibilityResult(BaseModel):
    """Independent compatibility conclusions for one candidate."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    minecraft: AuditStatus
    loader: AuditStatus
    dependencies: AuditStatus
    side: AuditStatus
    embedded_overlap: AuditStatus


class CandidateAuditRow(BaseModel):
    """One exact candidate artifact and its conservative disposition."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    candidate_filename: str
    proposed_state: Literal["enabled", "disabled"]
    source: SourceRecord
    artifact: ArtifactIdentity
    declared: DeclaredMetadata
    embedded: EmbeddedMetadata | None
    hazards: tuple[str, ...]
    compatibility: CompatibilityResult
    disposition: Disposition
    rationale: str
    limitations: tuple[str, ...]


class AuditTarget(BaseModel):
    """Pinned platform target for the exact audit."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    minecraft: Literal["1.21.1"]
    loader: Literal["neoforge"]


class CandidateMatrix(BaseModel):
    """Complete Item 3 candidate matrix."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    schema_version: Literal["item3-compatibility-matrix-v1"]
    target: AuditTarget
    baseline_enabled_artifacts: tuple[str, ...]
    candidates: tuple[CandidateAuditRow, ...]


class AuditIssue(BaseModel):
    """One deterministic matrix acceptance failure."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    code: str
    path: str
    detail: str


_VERSION_TOKEN = re.compile(
    r"^(?:v|mc)?\d+(?:\.\d+)+(?:[-+._]?[a-z0-9]+)*$",
    re.IGNORECASE,
)
_NOISE_TOKEN = re.compile(
    r"^(?:neo(?:forge)?|neoforge|forge|fabric|release|all|bundled)$",
    re.IGNORECASE,
)
_CAMEL_BOUNDARY = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")
_ACRONYM_BOUNDARY = re.compile(r"(?<=[A-Z])(?=[A-Z][a-z])")


def build_search_queries(candidate_filename: str) -> tuple[str, ...]:
    """Build stable Modrinth search queries from a noisy candidate filename."""
    stem = candidate_filename.removesuffix(".disabled").removesuffix(".jar")
    stem = stem.removesuffix(".mod").strip()
    stem = re.sub(r"^\[[^]]+\]", "", stem)
    tokens = tuple(token for token in re.split(r"[-_ +]+", stem) if token)
    project_tokens: list[str] = []
    for token in tokens:
        if _VERSION_TOKEN.fullmatch(token) or _NOISE_TOKEN.fullmatch(token):
            break
        project_tokens.append(token)
    if not project_tokens:
        project_tokens = [tokens[0]] if tokens else [stem]
    compact = " ".join(project_tokens)
    camel = " ".join(
        _CAMEL_BOUNDARY.sub(" ", _ACRONYM_BOUNDARY.sub(" ", token)) for token in project_tokens
    )
    return tuple(dict.fromkeys((compact, camel)))


def find_exact_modrinth_file(
    candidate_filename: str,
    versions: Sequence[Mapping[str, object]],
) -> ExactFileMatch | None:
    """Return a match only when a version record names the exact upstream file."""
    expected = candidate_filename.removesuffix(".disabled")
    for version in versions:
        version_record = _ModrinthVersionRecord.model_validate(version)
        for index, file_record in enumerate(version_record.files):
            if file_record.filename == expected:
                return ExactFileMatch(
                    version_id=version_record.id,
                    filename=expected,
                    file_index=index,
                )
    return None


def validate_candidate_matrix(
    matrix_path: Path,
    inventory_path: Path,
) -> tuple[AuditIssue, ...]:
    """Validate complete coverage and the no-unverified-enabled exit gate."""
    matrix = CandidateMatrix.model_validate_json(matrix_path.read_text(encoding="utf-8"))
    inventory = tuple(
        line.strip()
        for line in inventory_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    )
    matrix_names = tuple(row.candidate_filename for row in matrix.candidates)
    issues: list[AuditIssue] = []
    if len(matrix_names) != len(set(matrix_names)) or set(matrix_names) != set(inventory):
        issues.append(
            AuditIssue(
                code="candidate_set_mismatch",
                path="candidates",
                detail="matrix must contain every inventory filename exactly once",
            )
        )
    by_name = {row.candidate_filename: row for row in matrix.candidates}
    for filename in matrix.baseline_enabled_artifacts:
        row = by_name.get(filename)
        if row is None or any(
            status != "pass"
            for status in (
                row.compatibility.minecraft if row else "unverified",
                row.compatibility.loader if row else "unverified",
                row.compatibility.dependencies if row else "unverified",
            )
        ):
            issues.append(
                AuditIssue(
                    code="unsupported_enabled",
                    path=filename,
                    detail=(
                        "enabled artifact lacks verified Minecraft, loader, or dependency support"
                    ),
                )
            )
    return tuple(issues)
