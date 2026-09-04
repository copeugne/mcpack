"""Link runtime IDs to packaged sources with uv run -m tools.build_item8_structure_inputs."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import tomllib
from pathlib import Path
from typing import TYPE_CHECKING, cast

from mcpack_evidence.item8_biomes import structure_biomes, supplementaries_tag_inputs
from mcpack_evidence.item8_inventory import biome_tag_inputs, size_variant_groups, structure_inputs
from mcpack_evidence.item8_registry import read_registry

if TYPE_CHECKING:
    from pydantic import JsonValue

ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = "evidence/item-8/sources/packaged-json-redacted.json.gz"
SOURCE_SHA256 = "a5279d453f32edf7b1adc5c06b09953785b990b4b01c362b1423ed2f88930fdd"
REGISTRY_PATH = (
    "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
)
REGISTRY_SHA256 = "9d245430730173e9ce5304317a7476e7ecd4267d208b25a16a0d7b2cf3f16941"
BIOMES_PATH = "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_biome.txt"
BIOMES_SHA256 = "0970c5296980495640901e3ba7fd44fa90e97da4774900368fa924a263446713"
SUPPLEMENTARIES_CONFIG = "evidence/item-6/frozen/config/supplementaries-common.toml"
SUPPLEMENTARIES_CODE = "evidence/item-8/sources/supplementaries-tags-code/identities.json"
CONTEXT = "evidence/item-8/runtime/registry-r1/world-context.json"
DYNAMIC_INPUTS = {
    SUPPLEMENTARIES_CONFIG: "14210291891759b831951eba24c65985ed5bd27a7d09b6383aeb9fd3e8f1bc8c",
    SUPPLEMENTARIES_CODE: "1b6470427cc06bc41e6d3e690b0475568c0ef274d1101ea05a912eeb87edc30d",
    CONTEXT: "0615a2dcdeb2120a467648df95f69aa9f1ef53e8989ae8c2191028d6f5c1aca2",
}


RUNTIME_LOG = "evidence/raw/item8/registry-r1/debug.log"
INSPECTION = "evidence/item-3/jar-inspection.json"
ORDER_INPUTS = {
    RUNTIME_LOG: "e5b47378d791027242ba28dd36c999c07ae4e01a1b90e1534e66bcd42c1e694b",
    INSPECTION: "4f888ae07fd72daaf057833904aa1fd37e3b6d3c24f00071e15b99c6b197b64e",
}
ORDER_ARCHIVES = (
    "BiomesOPlenty-neoforge-1.21.1-21.1.0.13.jar",
    "Terralith_1.21.1_v2.6.2_Neoforge.jar",
    "regions-unexplored-0.6.1-neoforge-21.1.jar",
    "t_and_t-neoforge-fabric-1.13.9+1.21.1.jar",
)


def runtime_order(log: str, archive_packs: dict[str, str]) -> dict[str, JsonValue]:
    """Retain the final expanded sorting record and order the inspected contributors."""
    marker = "[net.fabricmc.fabric.impl.resource.loader.ModResourcePackUtil/]: "
    marker += "[Fabric] Final sorting result: "
    records = [(number, line) for number, line in enumerate(log.splitlines(), 1) if marker in line]
    if not records:
        message = "runtime log lacks final expanded resource pack sorting"
        raise ValueError(message)
    number, line = records[-1]
    payload = line.split(marker, 1)[1]
    if not payload.startswith("[") or not payload.endswith("]"):
        message = "malformed expanded resource pack sorting record"
        raise ValueError(message)
    packs = payload[1:-1].split(", ")
    if len(packs) != len(set(packs)) or not set(archive_packs.values()) <= set(packs):
        message = "expanded sorting has duplicate packs or lacks an inspected contributor"
        raise ValueError(message)
    archives = sorted(archive_packs, key=lambda archive: packs.index(archive_packs[archive]))
    return {
        "source": RUNTIME_LOG,
        "source_sha256": ORDER_INPUTS[RUNTIME_LOG],
        "line": number,
        "record": line,
        "archive_packs": dict(archive_packs),
        "archives": cast("JsonValue", archives),
    }


def inspected_archive_packs() -> dict[str, str]:
    """Bind the four competing contributors to their inspected NeoForge mod IDs."""
    inspection = cast("dict[str, JsonValue]", json.loads((ROOT / INSPECTION).read_bytes()))
    candidates = cast("list[dict[str, JsonValue]]", inspection["candidates"])
    archive_packs = {
        "minecraft-server-1.21.1.jar!/META-INF/versions/1.21.1/server-1.21.1.jar": "vanilla"
    }
    for archive in ORDER_ARCHIVES:
        row = next(row for row in candidates if row["candidate_filename"] == archive)
        mods = cast("list[dict[str, str]]", row["mods"])
        identifiers = {
            mod["mod_id"] for mod in mods if mod["source_path"] == "META-INF/neoforge.mods.toml"
        }
        if len(identifiers) != 1:
            message = f"ambiguous inspected mod pack identity: {archive}"
            raise ValueError(message)
        archive_packs[archive] = f"mod/{identifiers.pop()}"
    return archive_packs


def main() -> None:
    """Read the delivered source identities and write the deterministic relationship index."""
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("--output", type=Path, required=True)
    output = cast("Path", parser.parse_args().output)
    inputs = {
        SOURCE_PATH: SOURCE_SHA256,
        REGISTRY_PATH: REGISTRY_SHA256,
        BIOMES_PATH: BIOMES_SHA256,
        **DYNAMIC_INPUTS,
        **ORDER_INPUTS,
    }
    for relative, digest in inputs.items():
        if hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() != digest:
            message = f"source identity mismatch: {relative}"
            raise ValueError(message)
    code = cast("list[dict[str, str]]", json.loads((ROOT / SUPPLEMENTARIES_CODE).read_bytes()))
    for row in code:
        relative = str(Path(SUPPLEMENTARIES_CODE).parent / row["disassembly"])
        if hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() != row["disassembly_sha256"]:
            message = f"dynamic tag code identity mismatch: {relative}"
            raise ValueError(message)
        inputs[relative] = row["disassembly_sha256"]
    context = cast("dict[str, JsonValue]", json.loads((ROOT / CONTEXT).read_bytes()))
    packs = cast("dict[str, JsonValue]", context["DataPacks"])
    if "supplementaries:generated_pack" not in cast("list[str]", packs["Enabled"]):
        message = "captured runtime does not enable Supplementaries generated resources"
        raise ValueError(message)
    catalog = cast(
        "dict[str, JsonValue]", json.loads(gzip.decompress((ROOT / SOURCE_PATH).read_bytes()))
    )
    resources = catalog["resources"]
    if not isinstance(resources, list):
        message = "packaged source catalog has no resources list"
        raise TypeError(message)
    registry = read_registry(ROOT / REGISTRY_PATH)
    result = structure_inputs(registry, resources)
    result["size_variant_groups"] = size_variant_groups(registry, resources)
    order = runtime_order((ROOT / RUNTIME_LOG).read_text(), inspected_archive_packs())
    result["biome_archive_order"] = order
    tags = biome_tag_inputs(resources, tuple(cast("list[str]", order["archives"])))
    config = cast(
        "dict[str, JsonValue]", tomllib.loads((ROOT / SUPPLEMENTARIES_CONFIG).read_text())
    )
    dynamic_tags = supplementaries_tag_inputs(config, DYNAMIC_INPUTS)
    if tags.keys() & dynamic_tags.keys():
        message = "dynamic biome tags now have packaged competitors; resolve precedence"
        raise ValueError(message)
    tags.update(dynamic_tags)
    result["biome_tags"] = tags
    constraints = structure_biomes(
        registry, resources, tags, frozenset(read_registry(ROOT / BIOMES_PATH))
    )
    result["structure_biomes"] = constraints
    result["inputs"] = dict(inputs)
    with output.open("x", encoding="utf-8") as stream:
        _ = stream.write(json.dumps(result, indent=2, sort_keys=True) + "\n")
    resolved = sum(
        isinstance(row, dict) and row["biomes"] is not None for row in constraints.values()
    )
    print(
        f"Source-derived biome constraints: {resolved} resolved of {len(constraints)} registry IDs"
    )


if __name__ == "__main__":
    main()
