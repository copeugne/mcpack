#!/usr/bin/env python3
# pyright: standard
"""Materialize, back up, and restore isolated deterministic Item 4 servers."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
import shutil
import tarfile
import tempfile
from pathlib import Path
from typing import Any, TypedDict


class MaterializationReceipt(TypedDict):
    """Identity of one isolated seed instance."""

    schema_version: str
    configuration_version: str
    seed_role: str
    seed: str
    retained_candidate_count: int
    retained_manifest_sha256: str
    pristine_source: str
    production_state_used: bool


class BackupReceipt(TypedDict):
    """Integrity identity of one world backup."""

    schema_version: str
    archive: str
    archive_size_bytes: int
    archive_sha256: str
    world_file_count: int
    world_files: list[dict[str, Any]]


class RestoreReceipt(TypedDict):
    """Result of one verified restore."""

    schema_version: str
    archive_sha256: str
    restored_world: str
    world_file_count: int


def sha256(path: Path) -> str:
    """Return the SHA-256 of one file."""
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while block := stream.read(1024 * 1024):
            digest.update(block)
    return digest.hexdigest()


def require_absent(path: Path) -> None:
    """Reject destructive reuse of an existing path."""
    if path.exists():
        message = f"target must be absent: {path}"
        raise ValueError(message)


def materialize(  # noqa: PLR0913, PLR0917
    pristine: Path,
    artifact_manifest: Path,
    retained_manifest: Path,
    seed_suite: Path,
    role: str,
    target: Path,
) -> MaterializationReceipt:
    """Clone the pristine platform and install the hash-verified retained set."""
    require_absent(target)
    seeds = json.loads(seed_suite.read_text(encoding="utf-8"))["seeds"]
    seed_row = next((row for row in seeds if row["role"] == role), None)
    if seed_row is None:
        message = f"unknown seed role: {role}"
        raise ValueError(message)
    artifacts = {
        row["candidate_filename"]: row
        for row in json.loads(artifact_manifest.read_text(encoding="utf-8"))["artifacts"]
    }
    retained = retained_manifest.read_text(encoding="utf-8").splitlines()
    missing = sorted(set(retained) - artifacts.keys())
    if missing:
        message = f"retained artifacts absent from acquisition manifest: {missing}"
        raise ValueError(message)
    shutil.copytree(pristine, target, copy_function=shutil.copy2)
    mods = target / "mods"
    mods.mkdir()
    for filename in retained:
        row = artifacts[filename]
        source = Path(row["local_path"])
        identity = row["identity"]
        if (
            source.stat().st_size != identity["size_bytes"]
            or sha256(source) != identity["computed_sha256"]
        ):
            message = f"artifact identity mismatch: {filename}"
            raise ValueError(message)
        os.link(source, mods / filename)
    _set_property(target / "server.properties", "level-name", "world")
    _set_property(target / "server.properties", "level-seed", str(seed_row["seed"]))
    receipt = {
        "schema_version": "item4-materialization-v1",
        "configuration_version": "test-environment-v0.1",
        "seed_role": role,
        "seed": str(seed_row["seed"]),
        "retained_candidate_count": len(retained),
        "retained_manifest_sha256": sha256(retained_manifest),
        "pristine_source": str(pristine),
        "production_state_used": False,
    }
    (target / "item4-materialization.json").write_text(
        json.dumps(receipt, indent=2) + "\n", encoding="utf-8"
    )
    return receipt


def backup(world: Path, archive: Path, receipt_path: Path) -> BackupReceipt:
    """Create a deterministic stopped-world archive and integrity receipt."""
    require_absent(archive)
    if not (world / "level.dat").is_file():
        message = f"world has no level.dat: {world}"
        raise ValueError(message)
    archive.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=archive.parent, delete=False) as temporary:
        temporary_path = Path(temporary.name)
    try:
        with (
            temporary_path.open("wb") as raw,
            gzip.GzipFile(fileobj=raw, mode="wb", filename="", mtime=0) as compressed,
            tarfile.open(fileobj=compressed, mode="w|") as tar,
        ):
            for path in sorted(world.rglob("*")):
                relative = path.relative_to(world)
                info = tar.gettarinfo(str(path), arcname=str(Path("world") / relative))
                info.uid = info.gid = 0
                info.uname = info.gname = ""
                info.mtime = 0
                if path.is_file():
                    with path.open("rb") as stream:
                        tar.addfile(info, stream)
                else:
                    tar.addfile(info)
        temporary_path.replace(archive)
    finally:
        temporary_path.unlink(missing_ok=True)
    files = [_file_row(path, world) for path in sorted(world.rglob("*")) if path.is_file()]
    receipt = {
        "schema_version": "item4-world-backup-v1",
        "archive": str(archive),
        "archive_size_bytes": archive.stat().st_size,
        "archive_sha256": sha256(archive),
        "world_file_count": len(files),
        "world_files": files,
    }
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    return receipt


def restore(archive: Path, expected_sha256: str, target: Path) -> RestoreReceipt:
    """Verify and safely extract one deterministic world archive."""
    require_absent(target)
    actual_sha256 = sha256(archive)
    if actual_sha256 != expected_sha256:
        message = f"archive SHA-256 mismatch: expected {expected_sha256}, got {actual_sha256}"
        raise ValueError(message)
    target.mkdir(parents=True)
    with tarfile.open(archive, "r:gz") as tar:
        members = tar.getmembers()
        if any(
            member.name == "world"
            or not member.name.startswith("world/")
            or member.issym()
            or member.islnk()
            for member in members
        ):
            message = "archive contains an unsafe member"
            raise ValueError(message)
        tar.extractall(target, filter="data")
    restored = target / "world"
    return {
        "schema_version": "item4-world-restore-v1",
        "archive_sha256": actual_sha256,
        "restored_world": str(restored),
        "world_file_count": sum(path.is_file() for path in restored.rglob("*")),
    }


def _set_property(path: Path, key: str, value: str) -> None:
    rows = path.read_text(encoding="utf-8").splitlines()
    prefix = f"{key}="
    replaced = False
    output = []
    for row in rows:
        if row.startswith(prefix):
            output.append(f"{prefix}{value}")
            replaced = True
        else:
            output.append(row)
    if not replaced:
        output.append(f"{prefix}{value}")
    path.write_text("\n".join(output) + "\n", encoding="utf-8")


def _file_row(path: Path, root: Path) -> dict[str, Any]:
    return {
        "path": str(path.relative_to(root)),
        "size_bytes": path.stat().st_size,
        "sha256": sha256(path),
    }


def main() -> int:
    """Run one non-destructive Item 4 environment operation."""
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command", required=True)
    create = commands.add_parser("materialize")
    for name in ("pristine", "artifact-manifest", "retained-manifest", "seed-suite", "target"):
        create.add_argument(f"--{name}", type=Path, required=True)
    create.add_argument("--role", required=True)
    archive = commands.add_parser("backup")
    archive.add_argument("--world", type=Path, required=True)
    archive.add_argument("--archive", type=Path, required=True)
    archive.add_argument("--receipt", type=Path, required=True)
    recover = commands.add_parser("restore")
    recover.add_argument("--archive", type=Path, required=True)
    recover.add_argument("--sha256", required=True)
    recover.add_argument("--target", type=Path, required=True)
    arguments = parser.parse_args()
    if arguments.command == "materialize":
        result = materialize(
            arguments.pristine,
            arguments.artifact_manifest,
            arguments.retained_manifest,
            arguments.seed_suite,
            arguments.role,
            arguments.target,
        )
    elif arguments.command == "backup":
        result = backup(arguments.world, arguments.archive, arguments.receipt)
    else:
        result = restore(arguments.archive, arguments.sha256, arguments.target)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
