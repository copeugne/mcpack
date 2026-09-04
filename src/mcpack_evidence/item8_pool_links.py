"""Packaged pool and template links, not claims of actual assembled placement."""

from __future__ import annotations

from typing import TYPE_CHECKING

from .item8_inventory import resource_identity

if TYPE_CHECKING:
    from pydantic import JsonValue

# Codec and registration evidence: evidence/item-8/sources/pool-codecs.
_SINGLE_TYPES = frozenset(
    {
        "minecraft:single_pool_element",
        "minecraft:legacy_single_pool_element",
        "yungsapi:yung_single_element",
        "integrated_api:integrated_api_single_pool_element",
        "wover:single_end_pool_element",
        "illagerinvasion:single_pool_element",
        "moogs_structures:mirroring_single_pool_element",
        "repurposed_structures:legacy_ocean_bottom_single_pool_element",
        "moogs_structures:versioned_single_pool_element",
    }
)


def pool_links(resources: list[JsonValue]) -> list[JsonValue]:
    """Preserve source-specific pool elements, fallback and processor references."""
    result: list[JsonValue] = []
    for row in resources:
        resource = _row(row)
        identity = resource_identity(str(resource["path"]), "worldgen/template_pool")
        if identity is None:
            continue
        document = resource["document"]
        if not isinstance(document, dict) or not isinstance(document.get("elements"), list):
            message = f"invalid template pool: {resource['path']}"
            raise TypeError(message)
        edges: list[JsonValue] = []
        unknown: list[JsonValue] = []
        fallback = document.get("fallback")
        if isinstance(fallback, str):
            edges.append(_edge("pool", fallback, "/fallback"))
        elements = document["elements"]
        assert isinstance(elements, list)  # noqa: S101 - explicit validation above.
        for index, entry in enumerate(elements):
            if not isinstance(entry, dict) or "element" not in entry:
                message = f"pool has an invalid weighted element: {resource['path']}"
                raise TypeError(message)
            _element(entry["element"], f"/elements/{index}/element", edges, unknown)
        result.append(_link_record(resource, identity, edges, unknown))
    return result


def template_links(resources: list[JsonValue]) -> list[JsonValue]:
    """Preserve jigsaw connector pools independently of geometry or assembly feasibility."""
    result: list[JsonValue] = []
    for row in resources:
        resource = _row(row)
        path = str(resource["path"])
        identity = resource_identity(path, "structure", ".nbt")
        if identity is None:
            identity = resource_identity(path, "structures", ".nbt")
        if identity is None:
            message = f"unrecognized template resource path: {path}"
            raise ValueError(message)
        document = resource["document"]
        if not isinstance(document, dict) or not isinstance(document.get("block_entities"), list):
            message = f"template lacks decoded block entities: {path}"
            raise TypeError(message)
        blocks = document["block_entities"]
        assert isinstance(blocks, list)  # noqa: S101 - explicit validation above.
        edges: list[JsonValue] = []
        for index, block in enumerate(blocks):
            if not isinstance(block, dict) or not isinstance(block.get("nbt"), dict):
                message = f"invalid template block entity: {path}"
                raise TypeError(message)
            nbt = block["nbt"]
            assert isinstance(nbt, dict)  # noqa: S101 - explicit validation above.
            if nbt.get("id") == "minecraft:jigsaw" and isinstance(nbt.get("pool"), str):
                edges.append(_edge("pool", str(nbt["pool"]), f"/block_entities/{index}/nbt/pool"))
        result.append(_link_record(resource, identity, edges, []))
    return result


def _row(row: JsonValue) -> dict[str, JsonValue]:
    if not isinstance(row, dict) or not isinstance(row.get("path"), str):
        message = "resource catalog contains an invalid row"
        raise TypeError(message)
    return row


def _edge(kind: str, identifier: str, pointer: str) -> dict[str, JsonValue]:
    return {
        "kind": kind,
        "id": identifier if ":" in identifier else f"minecraft:{identifier}",
        "pointer": pointer,
    }


def _link_record(
    resource: dict[str, JsonValue],
    identity: tuple[str, str],
    edges: list[JsonValue],
    unknown: list[JsonValue],
) -> dict[str, JsonValue]:
    return {
        "id": identity[0],
        "pack_prefix": identity[1],
        "archive": resource["archive"],
        "path": resource["path"],
        "sha256": resource["sha256"],
        "edges": edges,
        "unresolved_elements": unknown,
    }


def _element(  # noqa: C901, PLR0912 - explicit handling of the observed codec variants.
    value: JsonValue, pointer: str, edges: list[JsonValue], unknown: list[JsonValue]
) -> None:
    if not isinstance(value, dict):
        message = f"invalid pool element at {pointer}"
        raise TypeError(message)
    kind = value.get("element_type")
    if isinstance(kind, str) and kind in _SINGLE_TYPES:
        location = value.get("location")
        if isinstance(location, str):
            edges.append(_edge("template", location, pointer + "/location"))
        else:
            unknown.append({"pointer": pointer, "reason": "inline or invalid template location"})
        processors = value.get("processors")
        if isinstance(processors, str):
            edges.append(_edge("processor_list", processors, pointer + "/processors"))
        if kind == "moogs_structures:versioned_single_pool_element":
            locations = value.get("locations")
            if isinstance(locations, dict):
                for version_range, target in locations.items():
                    if not isinstance(target, str):
                        message = f"invalid versioned template location at {pointer}"
                        raise TypeError(message)
                    key = version_range.replace("~", "~0").replace("/", "~1")
                    edge = _edge("template", target, pointer + "/locations/" + key)
                    edge["version_range"] = version_range
                    edges.append(edge)
            unknown.append({"pointer": pointer, "reason": "version selection requires resolution"})
    elif kind == "minecraft:list_pool_element" and isinstance(value.get("elements"), list):
        children = value["elements"]
        assert isinstance(children, list)  # noqa: S101 - explicit validation above.
        for index, child in enumerate(children):
            _element(child, f"{pointer}/elements/{index}", edges, unknown)
    elif kind == "minecraft:feature_pool_element" and isinstance(value.get("feature"), str):
        edges.append(_edge("placed_feature", str(value["feature"]), pointer + "/feature"))
    elif kind == "minecraft:feature_pool_element" and isinstance(value.get("feature"), dict):
        edges.append(
            {
                "kind": "inline_placed_feature",
                "pointer": pointer + "/feature",
                "document": value["feature"],
            }
        )
    elif kind != "minecraft:empty_pool_element":
        unknown.append({"pointer": pointer, "element_type": kind, "reason": "unresolved element"})
