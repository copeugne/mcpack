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


def test_creating_space_packaged_component_partition() -> None:
    # Complements the existing root decisions with all packaged component membership.
    # Does not assert closure of executable generation or disconnected-template consumers.
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("creatingspace-"))
    assert source.sha256 == "a02eb4c17201f2add8343ebe7b4476890ae9b59a7f5af7e0309f6e00b9c65866"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    groups: dict[str, set[str]] = {
        k: set() for k in ("worldgen/structure", "worldgen/template_pool", "structure")
    }
    features: dict[str, str] = {}
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 1645
        for name in names:
            for category, identifiers in groups.items():
                found = resource_identity(
                    name, category, ".nbt" if category == "structure" else ".json"
                )
                if found:
                    identifiers.add(found[0])
            found = resource_identity(name, "worldgen/configured_feature")
            if found:
                data = cast("dict[str, JsonValue]", json.loads(archive.read(name)))
                features[found[0]] = cast("str", data["type"])
    roots = groups["worldgen/structure"]
    assert roots == {
        "creatingspace:mars/underground_outpost_1", "creatingspace:moon/abandoned_outpost",
        "creatingspace:moon/crashed_rocket", "creatingspace:moon/crashed_ship",
    }
    assert tuple(len(v) for v in groups.values()) == (4, 5, 6)
    assert features == {
        "creatingspace:mars/nickel_sulfate_geode": "minecraft:geode",
        "creatingspace:moon/aluminum_ore": "minecraft:ore",
        "creatingspace:moon/cobalt_ore": "minecraft:ore",
        "creatingspace:moon/nickel_ore": "minecraft:ore",
        "creatingspace:nickel_overworld_replacement": "minecraft:ore",
    }
    raw = Path("evidence/item-8/sources/pool-traces-content.json.gz").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5"
    )
    document = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    traces = cast("dict[str, dict[str, JsonValue]]", document["structures"])
    reached_pools = {p for r in roots for p in cast("list[str]", traces[r]["pools"])}
    reached_templates = {t for r in roots for t in cast("list[str]", traces[r]["templates"])}
    assert groups["worldgen/template_pool"] <= reached_pools
    assert groups["structure"] - reached_templates == {"creatingspace:moon/abandoned_outpost"}
    assert reached_templates - groups["structure"] == {
        "minecraft:bastion/bridge/legs/leg_0", "minecraft:bastion/bridge/legs/leg_1",
    }
    assert reached_pools - groups["worldgen/template_pool"] == {
        "minecraft:bastion/bridge/legs", "minecraft:empty",
    }
    for root in roots:
        assert traces[root]["missing"] == []
        assert traces[root]["unresolved_elements"] == []
