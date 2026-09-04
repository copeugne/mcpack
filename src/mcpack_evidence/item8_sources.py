"""Deterministic packaged-resource evidence for the retained Item 8 stack."""

from __future__ import annotations

import hashlib
import json
from io import BytesIO
from pathlib import Path, PurePosixPath
from typing import TYPE_CHECKING, Literal, cast
from zipfile import ZipFile

from .item3_acquisition import ArtifactAcquisitionManifest
from .item7_restriction_inputs import (
    MINECRAFT_NESTED,
    MINECRAFT_SHA256,
    NEOFORGE_SHA256,
    ArchiveInput,
)
from .item7_runtime import RETAINED_MANIFEST_SHA256
from .item8_templates import template_summary

if TYPE_CHECKING:
    from pydantic import JsonValue


def retained_sources(root: Path) -> tuple[ArchiveInput, ...]:
    """Bind all retained candidates and platform data to their frozen hashes."""
    retained = root / "evidence/item-3/runtime/retained-server-candidates.txt"
    if hashlib.sha256(retained.read_bytes()).hexdigest() != RETAINED_MANIFEST_SHA256:
        message = "retained candidate manifest identity mismatch"
        raise ValueError(message)
    acquisition = ArtifactAcquisitionManifest.model_validate_json(
        (root / "evidence/item-3/artifact-acquisition-manifest.json").read_bytes()
    )
    by_name = {row.candidate_filename: row for row in acquisition.artifacts}
    if len(by_name) != len(acquisition.artifacts):
        message = "duplicate acquisition candidate"
        raise ValueError(message)
    candidates = tuple(
        ArchiveInput(
            name,
            root / "downloads/item3/candidates" / name,
            by_name[name].identity.computed_sha256,
        )
        for name in retained.read_text().splitlines()
    )
    return (
        ArchiveInput(
            "minecraft-server-1.21.1.jar",
            root / "downloads/item2/minecraft/server.jar",
            MINECRAFT_SHA256,
            MINECRAFT_NESTED,
        ),
        ArchiveInput(
            "neoforge-21.1.249-universal.jar",
            root
            / "instances/pristine-baseline-v0/libraries/net/neoforged/neoforge"
            / "21.1.249/neoforge-21.1.249-universal.jar",
            NEOFORGE_SHA256,
        ),
        *candidates,
    )


def packaged_sources(
    sources: tuple[ArchiveInput, ...], kind: Literal["json", "template"] = "json"
) -> dict[str, JsonValue]:
    """Preserve packaged resources without inferring runtime activation."""
    archives: list[JsonValue] = []
    resources: list[JsonValue] = []
    for source in sources:
        payload = source.path.read_bytes()
        if hashlib.sha256(payload).hexdigest() != source.sha256:
            message = f"archive hash mismatch: {source.name}"
            raise ValueError(message)
        archives.append({"name": source.name, "sha256": source.sha256})
        location = source.name
        if source.nested_archive:
            with ZipFile(BytesIO(payload)) as outer:
                payload = outer.read(source.nested_archive)
            location += "!/" + source.nested_archive
        _collect(payload, location, resources, kind)
    return {"archives": archives, "resources": resources}


def _collect(
    payload: bytes, location: str, resources: list[JsonValue], kind: Literal["json", "template"]
) -> None:
    with ZipFile(BytesIO(payload)) as archive:
        names = archive.namelist()
        if len(names) != len(set(names)):
            message = f"duplicate ZIP member: {location}"
            raise ValueError(message)
        for name in sorted(names):
            path = PurePosixPath(name)
            if path.is_absolute() or ".." in path.parts or "\\" in name:
                message = f"unsafe ZIP member: {location}!/{name}"
                raise ValueError(message)
            if name.endswith(".jar"):
                _collect(archive.read(name), f"{location}!/{name}", resources, kind)
            elif kind == "template" and name.endswith(".nbt") and "data" in path.parts:
                raw = archive.read(name)
                resources.append(
                    {
                        "archive": location,
                        "path": name,
                        "sha256": hashlib.sha256(raw).hexdigest(),
                        "size_bytes": len(raw),
                        "document": template_summary(raw),
                    }
                )
            elif kind == "json" and name.endswith(".json") and "data" in path.parts:
                raw = archive.read(name)
                try:
                    value, parser = _parse_json(raw, f"{location}!/{name}")
                    failure = None
                except ValueError as error:
                    value = None
                    parser = "invalid-json"
                    failure = str(error)
                resources.append(
                    {
                        "archive": location,
                        "path": name,
                        "sha256": hashlib.sha256(raw).hexdigest(),
                        "size_bytes": len(raw),
                        "parser": parser,
                        "document": value,
                        "parse_error": failure,
                        "raw_text": raw.decode("utf-8-sig") if failure else None,
                    }
                )


def _parse_json(raw: bytes, location: str) -> tuple[JsonValue, str]:
    text = raw.decode("utf-8-sig")
    try:
        return cast("JsonValue", json.loads(text)), "json"
    except json.JSONDecodeError:
        # Existing Item 7 providers contain standalone comment lines.
        stripped = "\n".join(
            line for line in text.splitlines() if not line.lstrip().startswith("//")
        )
        try:
            return cast("JsonValue", json.loads(stripped)), "json-with-line-comments-removed"
        except json.JSONDecodeError as error:
            message = f"cannot decode packaged JSON: {location}: {error}"
            raise ValueError(message) from error
