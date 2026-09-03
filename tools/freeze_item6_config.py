#!/usr/bin/env python3
# ruff: noqa: EM101, EM102, TRY003
"""Freeze and validate the untouched Item 6 generated configuration baseline."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any, cast


def sha256(path: Path) -> str:
    """Return a file's SHA-256 digest."""
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate(root: Path, manifest_path: Path, audit_path: Path) -> None:  # noqa: C901, PLR0912
    """Fail unless the frozen tree, manifest, and audit agree exactly."""
    manifest = cast("dict[str, Any]", json.loads(manifest_path.read_text(encoding="utf-8")))
    audit = cast("dict[str, Any]", json.loads(audit_path.read_text(encoding="utf-8")))
    if manifest["schema_version"] != "item6-frozen-config-manifest-v1":
        raise ValueError("unsupported manifest schema")
    if audit["schema_version"] != "item6-config-audit-v1":
        raise ValueError("unsupported audit schema")
    if audit["tuning_performed"] is not False:
        raise ValueError("baseline must not contain tuning")
    identity = f"sha256:{sha256(manifest_path)}"
    if audit["configuration_identity"] != identity:
        raise ValueError("audit configuration identity does not match manifest")

    rows = manifest["files"]
    expected = {row["path"] for row in rows}
    actual = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file()}
    if expected != actual or manifest["file_count"] != len(rows):
        raise ValueError("frozen file inventory does not match manifest")
    for row in rows:
        path = root / row["path"]
        if path.stat().st_size != row["size_bytes"] or sha256(path) != row["sha256"]:
            raise ValueError(f"frozen file identity mismatch: {row['path']}")
        if row["generation_stage"] not in {
            "installation",
            "first_startup",
            "world_creation",
            "shutdown",
        }:
            raise ValueError(f"invalid generation stage: {row['path']}")

    covered: set[str] = set()
    for system in audit["systems"]:
        for relative in system["files"]:
            if relative not in expected:
                raise ValueError(f"system cites an unpreserved file: {relative}")
            covered.add(relative)
    for setting in audit["settings"]:
        relative = setting["file"]
        if relative not in expected:
            raise ValueError(f"setting cites an unpreserved file: {relative}")
        content = (root / relative).read_text(encoding="utf-8")
        if setting["evidence"] not in content:
            raise ValueError(f"setting evidence does not match preserved content: {relative}")
        covered.add(relative)
    for finding in audit["findings"]:
        for relative in finding["files"]:
            if relative not in expected:
                raise ValueError(f"finding cites an unpreserved file: {relative}")
    if any(setting["non_default"] for setting in audit["settings"]):
        raise ValueError("untouched generated baseline unexpectedly reports tuning")
    if not covered:
        raise ValueError("audit has no preserved-file coverage")


def capture(instance: Path, output: Path) -> None:
    """Copy configuration-bearing paths without altering the source instance."""
    if output.exists():
        raise FileExistsError(f"output already exists: {output}")
    output.mkdir(parents=True)
    sources = {
        instance / "config": output / "config",
        instance / "defaultconfigs": output / "defaultconfigs",
        instance / "world" / "serverconfig": output / "world-serverconfig",
    }
    for source, target in sources.items():
        if source.is_dir():
            shutil.copytree(source, target)
    shutil.copy2(instance / "server.properties", output / "server.properties")


def main() -> int:
    """Run capture or validation."""
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    capture_parser = subparsers.add_parser("capture")
    capture_parser.add_argument("--instance", type=Path, required=True)
    capture_parser.add_argument("--output", type=Path, required=True)
    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("--root", type=Path, required=True)
    validate_parser.add_argument("--manifest", type=Path, required=True)
    validate_parser.add_argument("--audit", type=Path, required=True)
    arguments = parser.parse_args()
    if arguments.command == "capture":
        capture(arguments.instance, arguments.output)
    else:
        validate(arguments.root, arguments.manifest, arguments.audit)
        print("validated Item 6 frozen configuration and audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
