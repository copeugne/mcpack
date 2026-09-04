from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

from mcpack_evidence.item8_inventory import resource_identity
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
