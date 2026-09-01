"""Normalize NeoForge, Forge, Fabric, and JarJar metadata declarations."""

from __future__ import annotations

import json
import tomllib
from dataclasses import dataclass
from typing import ClassVar

from pydantic import BaseModel, ConfigDict, Field, JsonValue

from mcpack_evidence.item3_jar_models import DependencyDeclaration, ModDeclaration

TOML_PATHS = ("META-INF/neoforge.mods.toml", "META-INF/mods.toml")
FABRIC_PATH = "fabric.mod.json"
JARJAR_PATH = "META-INF/jarjar/metadata.json"


@dataclass(frozen=True)
class ParsedMetadata:
    """Normalized declarations from one supported metadata document."""

    mods: tuple[ModDeclaration, ...]
    dependencies: tuple[DependencyDeclaration, ...]
    mod_loader: str
    loader_range: str
    fabric_environment: str | None
    embedded_paths: tuple[str, ...]


@dataclass(frozen=True)
class JarCoordinate:
    """Normalized coordinates for one JarJar metadata entry."""

    identifier: str
    artifact_version: str
    version_range: str


class _TomlMod(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="ignore")

    mod_id: str = Field(alias="modId")
    version: str
    display_name: str | None = Field(default=None, alias="displayName")


class _TomlDependency(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="ignore")

    mod_id: str = Field(alias="modId")
    type: str | None = None
    mandatory: bool | None = None
    version_range: str = Field(default="", alias="versionRange")
    side: str = "BOTH"
    ordering: str = "NONE"


class _TomlDocument(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="ignore")

    mod_loader: str = Field(default="", alias="modLoader")
    loader_version: str = Field(default="", alias="loaderVersion")
    mods: tuple[_TomlMod, ...] = ()
    dependencies: JsonValue = Field(default_factory=dict)


class _FabricJar(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="ignore")

    file: str


class _FabricDocument(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="ignore")

    id: str
    version: str
    name: JsonValue | None = None
    environment: str = "*"
    depends: dict[str, JsonValue] = Field(default_factory=dict)
    recommends: dict[str, JsonValue] = Field(default_factory=dict)
    suggests: dict[str, JsonValue] = Field(default_factory=dict)
    breaks: dict[str, JsonValue] = Field(default_factory=dict)
    conflicts: dict[str, JsonValue] = Field(default_factory=dict)
    jars: tuple[_FabricJar, ...] = ()


class _JarIdentifier(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="ignore")

    group: str
    artifact: str


class _JarVersion(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="ignore")

    range: str
    artifact_version: str = Field(alias="artifactVersion")


class _JarEntry(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="ignore")

    identifier: _JarIdentifier
    version: _JarVersion
    path: str


class _JarJarDocument(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(extra="ignore")

    jars: tuple[_JarEntry, ...] = ()


def parse_toml_metadata(body: bytes, path: str) -> ParsedMetadata:
    """Parse one NeoForge or Forge TOML metadata document."""
    document = _TomlDocument.model_validate(tomllib.loads(body.decode()))
    mods = tuple(
        ModDeclaration(
            mod_id=mod.mod_id,
            version=mod.version,
            display_name=mod.display_name,
            source_path=path,
        )
        for mod in document.mods
    )
    groups = _dependency_groups(document.dependencies)
    dependencies = tuple(
        DependencyDeclaration(
            owner_mod_id=owner,
            mod_id=row.mod_id,
            kind=row.type or ("required" if row.mandatory is not False else "optional"),
            mandatory=row.mandatory,
            version_ranges=(row.version_range,) if row.version_range else (),
            side=row.side,
            ordering=row.ordering,
            source_path=path,
        )
        for owner, declarations in groups
        for row in declarations
    )
    return ParsedMetadata(
        mods=mods,
        dependencies=dependencies,
        mod_loader=document.mod_loader,
        loader_range=document.loader_version,
        fabric_environment=None,
        embedded_paths=(),
    )


def parse_fabric_metadata(body: bytes) -> ParsedMetadata:
    """Parse one top-level Fabric metadata document."""
    document = _FabricDocument.model_validate_json(body)
    mod = ModDeclaration(
        mod_id=document.id,
        version=document.version,
        display_name=document.name if isinstance(document.name, str) else None,
        source_path=FABRIC_PATH,
    )
    sections = (
        ("required", document.depends),
        ("recommended", document.recommends),
        ("suggested", document.suggests),
        ("incompatible", document.breaks),
        ("conflicting", document.conflicts),
    )
    dependencies = tuple(
        DependencyDeclaration(
            owner_mod_id=document.id,
            mod_id=mod_id,
            kind=kind,
            mandatory=kind == "required",
            version_ranges=_fabric_ranges(value),
            side=document.environment,
            ordering="NONE",
            source_path=FABRIC_PATH,
        )
        for kind, rows in sections
        for mod_id, value in rows.items()
    )
    return ParsedMetadata(
        mods=(mod,),
        dependencies=dependencies,
        mod_loader="fabric",
        loader_range="",
        fabric_environment=document.environment,
        embedded_paths=tuple(entry.file for entry in document.jars),
    )


def parse_jarjar_metadata(body: bytes) -> dict[str, JarCoordinate]:
    """Parse JarJar paths and coordinates keyed by embedded path."""
    document = _JarJarDocument.model_validate_json(body)
    return {
        entry.path: JarCoordinate(
            identifier=f"{entry.identifier.group}:{entry.identifier.artifact}",
            artifact_version=entry.version.artifact_version,
            version_range=entry.version.range,
        )
        for entry in document.jars
    }


def _fabric_ranges(value: JsonValue) -> tuple[str, ...]:
    if isinstance(value, str):
        return (value,)
    if isinstance(value, list) and all(isinstance(row, str) for row in value):
        return tuple(row for row in value if isinstance(row, str))
    return (json.dumps(value, sort_keys=True, separators=(",", ":")),)


def _dependency_groups(
    value: JsonValue,
    prefix: tuple[str, ...] = (),
) -> tuple[tuple[str, tuple[_TomlDependency, ...]], ...]:
    if isinstance(value, list):
        return (
            (
                ".".join(prefix),
                tuple(_TomlDependency.model_validate(row) for row in value),
            ),
        )
    if isinstance(value, dict):
        return tuple(
            group
            for key, nested in value.items()
            for group in _dependency_groups(nested, (*prefix, key))
        )
    return ()
