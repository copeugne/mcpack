"""Decode template attributes without treating pieces as assembled structures."""

from __future__ import annotations

import gzip
from collections import Counter
from typing import TYPE_CHECKING, cast

from .item7_nbt import decode_compound_nbt

if TYPE_CHECKING:
    from pydantic import JsonValue


def template_summary(raw: bytes) -> dict[str, JsonValue]:
    """Preserve geometry, palettes, authored entities and block entity data."""
    payload = gzip.decompress(raw) if raw.startswith(b"\x1f\x8b") else raw
    root = decode_compound_nbt(payload)
    size = root.get("size")
    blocks = root.get("blocks")
    if (
        not isinstance(size, list)
        or len(size) != 3  # noqa: PLR2004 - Minecraft template XYZ dimensions.
        or any(type(value) is not int or value < 0 for value in size)
        or not isinstance(blocks, list)
    ):
        message = "template is missing valid size or blocks"
        raise ValueError(message)
    state_counts: Counter[int] = Counter()
    block_entities: list[JsonValue] = []
    for block in blocks:
        if not isinstance(block, dict) or type(block.get("state")) is not int:
            message = "template block has no integer state"
            raise ValueError(message)
        state = block["state"]
        assert isinstance(state, int)  # noqa: S101 - narrowed by explicit validation above.
        state_counts[state] += 1
        if "nbt" in block:
            block_entities.append(block)
    return {
        "size": size,
        "data_version": root.get("DataVersion"),
        "palette": root.get("palette"),
        "palettes": root.get("palettes"),
        "state_counts": {str(key): count for key, count in sorted(state_counts.items())},
        "block_entities": block_entities,
        "entities": root.get("entities"),
    }


def template_content(document: dict[str, JsonValue]) -> dict[str, JsonValue]:
    """Index authored content, preserving source paths and unprocessed spawner NBT.

    These are packaged references. Data fixing, processors and generator code
    can change them; neither spawn success nor effective loot is inferred here.
    """
    entities: list[JsonValue] = []
    unresolved_entities: list[JsonValue] = []
    spawners: list[JsonValue] = []
    markers: list[JsonValue] = []
    loot: list[JsonValue] = []
    blocks = document["block_entities"]
    authored = document["entities"]
    if not isinstance(blocks, list) or not isinstance(authored, list):
        message = "template content requires block_entities and entities lists"
        raise TypeError(message)
    for index, raw in enumerate(blocks):
        block = cast("dict[str, JsonValue]", raw)
        nbt = cast("dict[str, JsonValue]", block["nbt"])
        identifier = nbt.get("id")
        row: dict[str, JsonValue] = {
            "path": f"/block_entities/{index}",
            "position": block["pos"],
            "nbt": nbt,
        }
        if identifier in {
            "minecraft:mob_spawner",
            "minecraft:trial_spawner",
            "iceandfire:dread_spawner",
        }:
            spawners.append(row)
        elif identifier in {"minecraft:structure_block", "moonlight:spawn_box"}:
            markers.append(row)
    pending = [
        (f"/entities/{index}/nbt", cast("dict[str, JsonValue]", row)["nbt"])
        for index, row in enumerate(authored)
    ]
    while pending:
        path, raw = pending.pop()
        entity = cast("dict[str, JsonValue]", raw)
        if not isinstance(entity.get("id"), str):
            unresolved_entities.append({"path": path, "reason": "authored entity lacks an ID"})
        else:
            entities.append({"path": path, "id": entity["id"]})
        for index, passenger in enumerate(cast("list[JsonValue]", entity.get("Passengers", []))):
            pending.append((f"{path}/Passengers/{index}", passenger))
    _loot_references(document, "", loot)
    return {
        "authored_entities": entities,
        "unresolved_entities": unresolved_entities,
        "spawner_blocks": spawners,
        "generation_markers": markers,
        "loot_references": loot,
    }


def _loot_references(value: JsonValue, path: str, result: list[JsonValue]) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            pointer = f"{path}/{key.replace('~', '~0').replace('/', '~1')}"
            if key in {"LootTable", "DeathLootTable", "loot_table", "loot_tables_to_eject"}:
                result.append({"path": pointer, "value": child})
            else:
                _loot_references(child, pointer, result)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _loot_references(child, f"{path}/{index}", result)


def spawner_entity_sources(nbt: dict[str, JsonValue]) -> list[dict[str, JsonValue]]:
    """Read explicit base entity IDs without inventing defaults or custom-spawner semantics."""
    identifier = nbt.get("id")
    rows: list[dict[str, JsonValue]] = []
    sections: list[tuple[str, str, dict[str, JsonValue], str, str]] = []
    if identifier == "minecraft:mob_spawner":
        sections.append(("ordinary", "", nbt, "SpawnData", "SpawnPotentials"))
    elif identifier == "minecraft:trial_spawner":
        if "spawn_data" in nbt:
            sections.append(("trial_current", "", nbt, "spawn_data", ""))
        for mode in ("normal_config", "ominous_config"):
            config = nbt.get(mode)
            if isinstance(config, dict):
                sections.append((mode, f"/{mode}", config, "", "spawn_potentials"))
            else:
                rows.append(
                    {
                        "mode": mode,
                        "path": f"/{mode}",
                        "unresolved": "missing or referenced trial configuration",
                        "source_value": config,
                    }
                )
    else:
        return [
            {
                "mode": "custom",
                "path": "",
                "unresolved": "custom spawner semantics",
                "source_value": identifier,
            }
        ]
    for section in sections:
        rows.extend(_spawner_section_sources(*section))
    return rows


def _spawner_section_sources(
    mode: str, prefix: str, section: dict[str, JsonValue], initial_key: str, potentials_key: str
) -> list[dict[str, JsonValue]]:
    rows: list[dict[str, JsonValue]] = []
    candidates: list[tuple[str, JsonValue]] = []
    if initial_key:
        candidates.append((f"{prefix}/{initial_key}", section.get(initial_key)))
    if potentials_key:
        potentials = section.get(potentials_key)
        if not isinstance(potentials, list):
            rows.append(
                {
                    "mode": mode,
                    "path": f"{prefix}/{potentials_key}",
                    "unresolved": "missing or non-list spawn potentials",
                }
            )
        else:
            for index, potential in enumerate(potentials):
                pointer = f"{prefix}/{potentials_key}/{index}"
                entry = cast("dict[str, JsonValue]", potential)
                weight = entry.get("weight")
                if type(weight) is not int or weight < 0:
                    rows.append(
                        {
                            "mode": mode,
                            "path": pointer,
                            "unresolved": "invalid or missing potential weight",
                        }
                    )
                elif weight > 0:
                    candidates.append((f"{pointer}/data", entry.get("data")))
    for pointer, data in candidates:
        entity = data.get("entity") if isinstance(data, dict) else None
        entity_id = entity.get("id") if isinstance(entity, dict) else None
        row: dict[str, JsonValue] = {"mode": mode, "path": f"{pointer}/entity/id"}
        if isinstance(entity_id, str) and entity_id:
            row["entity_id"] = entity_id
        else:
            row["unresolved"] = "missing or empty explicit entity ID"
        rows.append(row)
    return rows
