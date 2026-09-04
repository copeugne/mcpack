from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

import pytest
from tools.build_item8_inventory import assemble

from mcpack_evidence.item8_inventory import resource_identity, size_variant_groups
from mcpack_evidence.item8_registry import read_registry

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_mineshaft_group_covers_its_runtime_variants_and_preserved_specialized_generator() -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast(
        "dict[str, JsonValue]",
        json.loads((root / "evidence/item-8/family-decisions.json").read_bytes()),
    )
    decision = cast("list[dict[str, JsonValue]]", decisions["groups"])[0]
    evidence = cast("dict[str, str]", decision["evidence"])
    for path, digest in evidence.items():
        assert hashlib.sha256((root / path).read_bytes()).hexdigest() == digest
    registry = read_registry(
        root / "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    )
    members = cast("list[str]", decision["structure_ids"])
    assert len(members) == len(set(members))
    assert set(members) == {
        identifier for identifier in registry if identifier.startswith("bettermineshafts:")
    }
    raw = (root / "evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
    catalog = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    definitions: dict[str, dict[str, JsonValue]] = {}
    for resource in cast("list[dict[str, JsonValue]]", catalog["resources"]):
        identity = resource_identity(str(resource["path"]), "worldgen/structure")
        if identity is not None and identity[0] in members:
            assert identity[1] == ""
            assert identity[0] not in definitions
            definitions[identity[0]] = cast("dict[str, JsonValue]", resource["document"])
    assert set(definitions) == set(members)
    for document in definitions.values():
        assert {
            key: value for key, value in document.items() if key not in {"biomes", "config"}
        } == {
            "type": "bettermineshafts:mineshaft",
            "spawn_overrides": {},
            "step": "underground_structures",
        }
    code_root = root / "evidence/item-8/sources/mineshafts-code"
    identities = cast(
        "list[dict[str, str]]", json.loads((code_root / "identities.json").read_bytes())
    )
    for row in identities:
        assert (
            hashlib.sha256((code_root / row["disassembly"]).read_bytes()).hexdigest()
            == row["disassembly_sha256"]
        )


def test_ctov_size_decisions_exactly_cover_source_proven_variant_groups() -> None:
    root = Path(__file__).resolve().parents[2]
    decisions = cast(
        "dict[str, JsonValue]",
        json.loads((root / "evidence/item-8/family-decisions.json").read_bytes()),
    )
    groups = [
        row
        for row in cast("list[dict[str, JsonValue]]", decisions["groups"])
        if str(row["family_id"]).startswith("ctov:")
    ]
    registry = read_registry(
        root / "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    )
    raw = (root / "evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
    catalog = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    proven = size_variant_groups(registry, cast("list[JsonValue]", catalog["resources"]))
    expected = {
        tuple(str(member["structure_id"]) for member in cast("list[dict[str, JsonValue]]", group))
        for group in proven
    }
    actual = [tuple(cast("list[str]", row["structure_ids"])) for row in groups]
    assert len(actual) == len(set(actual))
    assert set(actual) == expected
    members = [identifier for group in actual for identifier in group]
    assert len(members) == len(set(members))
    assert set(members) == {
        identifier
        for identifier in registry
        if identifier.startswith(("ctov:small/", "ctov:medium/", "ctov:large/"))
    }
    for row in groups:
        assert {
            identifier.split("/", 1)[1] for identifier in cast("list[str]", row["structure_ids"])
        } == {str(row["family_id"]).split(":", 1)[1]}
        for path, digest in cast("dict[str, str]", row["evidence"]).items():
            assert hashlib.sha256((root / path).read_bytes()).hexdigest() == digest


def test_working_inventory_keeps_unassigned_ids_and_rejects_double_counting() -> None:
    decision: dict[str, JsonValue] = {
        "family_id": "example:family",
        "name": "Example",
        "structure_ids": ["example:a"],
    }
    sources: dict[str, JsonValue] = {"structure_biomes": {"example:a": {"biomes": []}}}
    traces: dict[str, JsonValue] = {
        "structures": {},
        "untraced_structures": {"example:a": {"reason": "custom"}},
    }
    bounds: dict[str, JsonValue] = {"observations": []}
    result = assemble(("example:a", "example:b"), [decision], sources, traces, bounds)
    assert result["status"] == "INCOMPLETE"
    assert result["unassigned_registry_ids"] == ["example:b"]
    conflicting = dict(decision, family_id="example:second")
    with pytest.raises(ValueError, match="multiply assigned"):
        _ = assemble(("example:a",), [decision, conflicting], sources, traces, bounds)
    with pytest.raises(ValueError, match="unregistered"):
        _ = assemble(("example:b",), [decision], sources, traces, bounds)
    decision["attributes"] = {"intended_hostility": {"value": "hostile", "basis": "source"}}
    result = assemble(("example:a",), [decision], sources, traces, bounds)
    families = cast("dict[str, dict[str, JsonValue]]", result["families"])
    assert families["example:family"]["intended_hostility"] == {
        "value": "hostile",
        "basis": "source",
    }
    assert families["example:family"]["status"] == "INCOMPLETE"
    decision["attributes"] = {"status": "COMPLETE"}
    with pytest.raises(ValueError, match="protected family attribute"):
        _ = assemble(("example:a",), [decision], sources, traces, bounds)
