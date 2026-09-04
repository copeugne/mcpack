"""Prepare and verify isolated Item 7 world-generation instances."""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import ClassVar, Final, Literal, final, override

from pydantic import BaseModel, ConfigDict, Field, model_validator

from mcpack_evidence.item6_validation import validate
from mcpack_evidence.item7_selections import PILOT_SELECTIONS, RUN_SELECTIONS, WorldgenSelection

CHUNKY_FILENAME: Final = "Chunky-NeoForge-1.4.23.jar"
CHUNKY_SIZE_BYTES: Final = 340572
CHUNKY_SHA256: Final = "d72f235cf1f56f2c374f52c00bdda5034524b28142305a84cfc123a3f92ad274"
RETAINED_COUNT: Final = 136
RETAINED_MANIFEST_SHA256: Final = "78e5bdc0697299782a535400ad5b313c088e8db10cfe075085ae4c8a531e30cb"
FROZEN_MANIFEST_SHA256: Final = "2e0aaeb0f84747a3cb17146eb435d34cc7d6703b9372211e8fc8cff2df2b436f"
CONFIG_AUDIT_SHA256: Final = "181e0c299f44ded319d93c84f7b983738364b4090286251b00421fa041b989dd"
SEED_SUITE_SHA256: Final = "de5e5e89bd04b6f75dac4eab2e84524956f46faa91660b5315c8eade269d39ae"
TEMURIN_BUILD: Final = "Temurin-21.0.12.1+1-LTS"
_TEMURIN_PATTERN: Final = re.compile(r"Temurin-21\.0\.12\.1\+1(?=$|[\s)])")
_TEMURIN_BUILD_PATTERN: Final = re.compile(r"build 21\.0\.12\.1\+1-LTS(?=$|[,\s)])")
_REPOSITORY_ROOT: Final = Path(__file__).parents[2]
_PREFLIGHT_STAGE: Final = "preflight"


@final
class Item7RuntimeError(Exception):
    """One typed Item 7 preflight or capture failure."""

    def __init__(self, stage: Literal["preflight", "capture", "lifecycle"], detail: str) -> None:
        """Initialize a failure with its boundary and machine-readable detail."""
        super().__init__(stage, detail)
        self.stage = stage
        self.detail = detail

    @override
    def __str__(self) -> str:
        return f"{self.stage}: {self.detail}"


class WorldgenRequest(BaseModel):
    """Validated paths and controls for one disposable seed run."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    pristine: Path
    artifact_manifest: Path
    retained_manifest: Path
    seed_suite: Path
    frozen_config: Path
    frozen_manifest: Path
    config_audit: Path
    java_home: Path
    role: str
    target: Path
    log_path: Path
    captured_config: Path
    mode: Literal["pilot", "run"] = "pilot"
    selections: tuple[WorldgenSelection, ...]
    timeout_seconds: int = Field(ge=0)

    @model_validator(mode="after")
    def require_fixed_selections(self) -> WorldgenRequest:
        """Reject selection drift from the declared pilot or run geometry."""
        expected = PILOT_SELECTIONS if self.mode == "pilot" else RUN_SELECTIONS
        if self.selections != expected:
            detail = f"{self.mode} selections differ from the fixed Item 7 geometry"
            raise ValueError(detail)
        return self


class _ArtifactIdentity(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore")

    size_bytes: int = Field(ge=0)
    computed_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")


class _Artifact(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore")

    candidate_filename: str
    local_path: Path
    identity: _ArtifactIdentity


class _AcquisitionManifest(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore")

    artifacts: tuple[_Artifact, ...]


class _MaterializationReceipt(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore")

    seed: str


class ArtifactHash(BaseModel):
    """One preserved runtime artifact identity."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)

    path: str
    sha256: str


class PreflightReceipt(BaseModel):
    """Exact base and instrumented identities for one fresh instance."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)

    schema_version: Literal["item7-worldgen-preflight-v1"] = "item7-worldgen-preflight-v1"
    seed_role: str
    seed: str
    java_version: str
    retained_candidate_count: Literal[136]
    instrumented_candidate_count: Literal[137]
    retained_runtime_sha256: str
    instrumented_runtime_sha256: str
    retained_manifest_sha256: str
    frozen_manifest_sha256: str
    config_audit_sha256: str
    seed_suite_sha256: str
    chunky_sha256: str


def sha256_file(path: Path) -> str:
    """Return one file's SHA-256."""
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while block := stream.read(1024 * 1024):
            digest.update(block)
    return digest.hexdigest()


def validate_java_runtime(java_home: Path) -> tuple[Path, str]:
    """Require the exact pinned Temurin executable and build."""
    executable = (java_home / "bin/java").resolve()
    if not executable.is_file() or not os.access(executable, os.X_OK):
        detail = f"requested Java runtime is unavailable: {executable}"
        raise Item7RuntimeError(_PREFLIGHT_STAGE, detail)
    completed = subprocess.run(  # noqa: S603 - executable is the validated pinned path.
        [executable, "-version"], capture_output=True, text=True, check=False
    )
    output = completed.stderr + completed.stdout
    version = _TEMURIN_PATTERN.search(output)
    build = _TEMURIN_BUILD_PATTERN.search(output)
    if completed.returncode != 0 or version is None or build is None:
        detail = f"requested Java runtime is not pinned Temurin: {executable}"
        raise Item7RuntimeError(_PREFLIGHT_STAGE, detail)
    return executable, TEMURIN_BUILD


def prepare_worldgen(request: WorldgenRequest) -> PreflightReceipt:
    """Compose Item 4 materialization with the frozen Item 6 configuration."""
    if request.target.exists() or request.target.is_symlink():
        raise Item7RuntimeError(_PREFLIGHT_STAGE, f"target must be absent: {request.target}")
    retained_manifest_sha = _require_document_identity(
        request.retained_manifest, RETAINED_MANIFEST_SHA256, "retained manifest"
    )
    frozen_manifest_sha = _require_document_identity(
        request.frozen_manifest, FROZEN_MANIFEST_SHA256, "frozen manifest"
    )
    config_audit_sha = _require_document_identity(
        request.config_audit, CONFIG_AUDIT_SHA256, "config audit"
    )
    seed_suite_sha = _require_document_identity(request.seed_suite, SEED_SUITE_SHA256, "seed suite")
    retained = tuple(request.retained_manifest.read_text(encoding="utf-8").splitlines())
    if len(retained) != RETAINED_COUNT or len(set(retained)) != RETAINED_COUNT:
        detail = "retained manifest must contain exactly 136 unique JARs"
        raise Item7RuntimeError(_PREFLIGHT_STAGE, detail)
    _, java_version = validate_java_runtime(request.java_home)
    try:
        validate(request.frozen_config, request.frozen_manifest, request.config_audit)
        acquisition = _AcquisitionManifest.model_validate_json(
            request.artifact_manifest.read_bytes()
        )
        artifacts = {row.candidate_filename: row for row in acquisition.artifacts}
        chunky = artifacts[CHUNKY_FILENAME]
        options = (
            ("--pristine", request.pristine),
            ("--artifact-manifest", request.artifact_manifest),
            ("--retained-manifest", request.retained_manifest),
            ("--seed-suite", request.seed_suite),
            ("--role", request.role),
            ("--target", request.target),
        )
        command = [
            sys.executable,
            str(_REPOSITORY_ROOT / "tools/manage_item4_environment.py"),
            "materialize",
        ]
        for flag, value in options:
            command.extend((flag, str(value)))
        completed = subprocess.run(  # noqa: S603 - command is this repository's Item 4 tool.
            command,
            cwd=_REPOSITORY_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if completed.returncode != 0:
            raise Item7RuntimeError(_PREFLIGHT_STAGE, completed.stderr.strip())
        materialization = _MaterializationReceipt.model_validate_json(completed.stdout)
        _apply_frozen_configuration(request, materialization.seed)
        retained_hashes = _hash_mods(request.target / "mods", retained)
        _install_chunky(request.target, chunky)
    except (KeyError, OSError, ValueError) as error:
        raise Item7RuntimeError(_PREFLIGHT_STAGE, str(error)) from error
    instrumented_hashes = _hash_mods(request.target / "mods", (*retained, CHUNKY_FILENAME))
    return PreflightReceipt(
        seed_role=request.role,
        seed=materialization.seed,
        java_version=java_version,
        retained_candidate_count=RETAINED_COUNT,
        instrumented_candidate_count=RETAINED_COUNT + 1,
        retained_runtime_sha256=_hash_rows(retained_hashes),
        instrumented_runtime_sha256=_hash_rows(instrumented_hashes),
        retained_manifest_sha256=retained_manifest_sha,
        frozen_manifest_sha256=frozen_manifest_sha,
        config_audit_sha256=config_audit_sha,
        seed_suite_sha256=seed_suite_sha,
        chunky_sha256=chunky.identity.computed_sha256,
    )


def _apply_frozen_configuration(request: WorldgenRequest, seed: str) -> None:
    def omit_sanitized_secret(directory: str, names: list[str]) -> set[str]:
        del names
        source_config = request.frozen_config / "config"
        return {"resourceful-config-web.json"} if Path(directory) == source_config else set()

    for name in ("config", "defaultconfigs"):
        destination = request.target / name
        if destination.exists():
            shutil.rmtree(destination)
        _ = shutil.copytree(request.frozen_config / name, destination, ignore=omit_sanitized_secret)
    source_properties = (request.frozen_config / "server.properties").read_bytes()
    properties = replace_property(source_properties, "level-seed", seed)
    _ = request.target.joinpath("server.properties").write_bytes(properties)


def _install_chunky(instance: Path, artifact: _Artifact) -> None:
    if (
        artifact.identity.size_bytes != CHUNKY_SIZE_BYTES
        or artifact.identity.computed_sha256 != CHUNKY_SHA256
        or artifact.local_path.stat().st_size != CHUNKY_SIZE_BYTES
        or sha256_file(artifact.local_path) != CHUNKY_SHA256
    ):
        raise Item7RuntimeError(_PREFLIGHT_STAGE, f"artifact identity mismatch: {CHUNKY_FILENAME}")
    os.link(artifact.local_path, instance / "mods" / CHUNKY_FILENAME)


def _hash_mods(mods: Path, expected_names: tuple[str, ...]) -> tuple[ArtifactHash, ...]:
    observed = tuple(sorted(path.name for path in mods.glob("*.jar")))
    if observed != tuple(sorted(expected_names)):
        detail = "runtime JAR filenames differ from expected identity"
        raise Item7RuntimeError(_PREFLIGHT_STAGE, detail)
    return tuple(ArtifactHash(path=name, sha256=sha256_file(mods / name)) for name in observed)


def _hash_rows(rows: tuple[ArtifactHash, ...]) -> str:
    payload = tuple((row.path, row.sha256) for row in rows)
    return hashlib.sha256(json.dumps(payload, separators=(",", ":")).encode()).hexdigest()


def _require_document_identity(path: Path, expected: str, label: str) -> str:
    try:
        observed = sha256_file(path)
    except OSError as error:
        detail = f"{label} identity could not be read: {error}"
        raise Item7RuntimeError(_PREFLIGHT_STAGE, detail) from error
    if observed != expected:
        detail = f"{label} identity differs from the frozen Item 7 input"
        raise Item7RuntimeError(_PREFLIGHT_STAGE, detail)
    return observed


def replace_property(content: bytes, key: str, value: str) -> bytes:
    """Replace one existing Java properties value."""
    prefix = f"{key}="
    rows = content.decode().splitlines()
    replaced = tuple(f"{prefix}{value}" if row.startswith(prefix) else row for row in rows)
    return ("\n".join(replaced) + "\n").encode()


def materialized_seed(request: WorldgenRequest) -> str:
    """Read the seed bound by the Item 4 materialization receipt."""
    content = request.target.joinpath("item4-materialization.json").read_bytes()
    return _MaterializationReceipt.model_validate_json(content).seed
