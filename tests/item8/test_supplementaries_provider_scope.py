from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_inventory import resource_identity
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_supplementaries_components_and_road_sign_feature_chain() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("supplementaries-"))
    assert source.sha256 == "0dd0445af35aa15ad012833c4b8024d2ed70320d1ace0316d2f5b684b06a997d"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    groups: dict[str, set[str]] = {
        k: set() for k in ("worldgen/structure", "worldgen/template_pool", "structure")
    }
    with ZipFile(source.path) as archive:
        for name in archive.namelist():
            for category, identifiers in groups.items():
                found = resource_identity(
                    name, category, ".nbt" if category == "structure" else ".json"
                )
                if found:
                    identifiers.add(found[0])
    roots = groups["worldgen/structure"]
    assert roots == {"supplementaries:galleon", "supplementaries:road_sign"}
    assert tuple(len(v) for v in groups.values()) == (2, 12, 18)
    raw = Path("evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5"
    )
    document = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    traces = cast("dict[str, dict[str, JsonValue]]", document["structures"])
    assert groups["worldgen/template_pool"] | {"minecraft:empty"} == {
        p for root in roots for p in cast("list[str]", traces[root]["pools"])
    }
    assert groups["structure"] == {
        t for root in roots for t in cast("list[str]", traces[root]["templates"])
    }
    for root in roots:
        assert traces[root]["missing"] == []
        assert traces[root]["unresolved_elements"] == []
    assert traces["supplementaries:road_sign"]["pools"] == [
        "minecraft:empty", "supplementaries:road_sign/feature_pool",
        "supplementaries:road_sign/start_pool",
    ]
    raw = Path("evidence/item-8/sources/packaged-json-redacted.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "a5279d453f32edf7b1adc5c06b09953785b990b4b01c362b1423ed2f88930fdd"
    )
    catalog = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    resources = {
        str(row["path"]): cast("dict[str, JsonValue]", row["document"])
        for row in cast("list[dict[str, JsonValue]]", catalog["resources"])
        if row["archive"] == source.name
    }
    prefix = "data/supplementaries/worldgen/"
    assert resources[prefix + "template_pool/road_sign/feature_pool.json"]["elements"] == [
        {"weight": 1, "element": {"element_type": "minecraft:feature_pool_element",
                                 "feature": "supplementaries:road_sign", "projection": "rigid"}},
    ]
    assert resources[prefix + "placed_feature/road_sign.json"] == {
        "feature": "supplementaries:road_sign", "placement": [],
    }
    assert resources[prefix + "configured_feature/road_sign.json"]["type"] == (
        "supplementaries:road_sign"
    )
