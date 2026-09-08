"""Count registry starts directly from a complete rectangle of stopped-world chunks."""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import math
from pathlib import Path
from typing import TYPE_CHECKING, cast

from tools.manage_item4_environment import _world_backup_lock
from tools.validate_item10_trace import BRIDGE_ROOT, SCARECROW_CLASS, URN

from mcpack_evidence.item7_anvil import decode_region_payloads, world_regions
from mcpack_evidence.item7_nbt import _packed, decode_compound_nbt

if TYPE_CHECKING:
    from collections.abc import Mapping

    from mcpack_evidence.item7_nbt_models import ChunkRecord


def chunk_biome_column(
    record: ChunkRecord, min_y: int, height: int, *, anchor: tuple[int, int] | None = None
) -> dict[int, str]:
    """Read saved quart-height biomes at the supplied block X/Z, or chunk center."""
    if anchor is None:
        local_x = local_z = 8
    else:
        if (
            len(anchor) != 2  # noqa: PLR2004 - horizontal coordinate pair
            or any(type(value) is not int for value in anchor)
            or (anchor[0] // 16, anchor[1] // 16) != (record.chunk_x, record.chunk_z)
        ):
            detail = "biome anchor must be integer X/Z within the supplied chunk"
            raise ValueError(detail)
        local_x, local_z = anchor[0] % 16, anchor[1] % 16
    sections = {section.section_y: section for section in record.biome_sections}
    if len(sections) != len(record.biome_sections):
        detail = f"duplicate biome section at chunk {record.chunk_x},{record.chunk_z}"
        raise ValueError(detail)
    column = {}
    section_quarts = 4**3
    for section_y in range(min_y // 16, (min_y + height) // 16):
        section = sections.get(section_y)
        if (
            section is None
            or len(section.indices) != section_quarts
            or any(not 0 <= index < len(section.palette) for index in section.indices)
        ):
            detail = (
                f"missing or invalid biome section {section_y} at {record.chunk_x},{record.chunk_z}"
            )
            raise ValueError(detail)
        for local_quart_y in range(4):
            # Minecraft palette order is X + 4*Z + 16*Y in quart coordinates.
            column[section_y * 4 + local_quart_y] = section.palette[
                section.indices[local_x // 4 + 4 * (local_z // 4) + 16 * local_quart_y]
            ]
    return column


def occurrence_biomes(record: ChunkRecord, column: dict[int, str]) -> list[dict[str, object]]:
    """Attribute starts at chunk center and the midpoint of their complete piece envelope."""
    rows = []
    for start in record.structure_starts:
        if start.start_id == "INVALID":
            continue
        boxes = [box.bounds for box in start.boxes]
        if any(box[axis] > box[axis + 3] for box in boxes for axis in range(3)):
            detail = "inverted structure piece bounds"
            raise ValueError(detail)
        envelope = (
            [min(box[i] for box in boxes) for i in range(3)]
            + [max(box[i] for box in boxes) for i in range(3, 6)]
            if boxes
            else None
        )
        anchor_y = (envelope[1] + envelope[4]) // 2 if envelope else None
        quart_y = anchor_y // 4 if anchor_y is not None else None
        biome = column.get(quart_y) if quart_y is not None else None
        rows.append(
            {
                "registry_id": start.structure_id,
                "chunk_x": record.chunk_x,
                "chunk_z": record.chunk_z,
                "piece_bounds": boxes,
                "envelope": envelope,
                "anchor_x": 16 * record.chunk_x + 8,
                "anchor_y": anchor_y,
                "anchor_z": 16 * record.chunk_z + 8,
                "quart_y": quart_y,
                "biome": biome,
                "unavailable_reason": (
                    "no stored piece bounds"
                    if not boxes
                    else "anchor outside stored biome height"
                    if biome is None
                    else None
                ),
            }
        )
    return rows


def saved_block_at(
    chunk: Mapping[str, object], position: tuple[int, int, int]
) -> dict[str, object] | None:
    """Read a saved palette entry; absent sections remain unavailable, not assumed air."""
    x, y, z = position
    if (chunk.get("xPos"), chunk.get("zPos")) != (x // 16, z // 16):
        detail = "saved block coordinate does not belong to supplied chunk"
        raise ValueError(detail)
    sections = [section for section in chunk["sections"] if section["Y"] == y // 16]
    if not sections:
        return None
    if len(sections) != 1:
        detail = "duplicate saved block section"
        raise ValueError(detail)
    states = sections[0].get("block_states")
    if states is None:
        return None
    palette = states["palette"]
    if not palette or any(not isinstance(entry.get("Name"), str) for entry in palette):
        detail = "invalid saved block palette"
        raise ValueError(detail)
    indices = (
        (0,) * 4096
        if len(palette) == 1
        else _packed(tuple(states["data"]), 4096, max(4, (len(palette) - 1).bit_length()))
    )
    index = indices[x % 16 + 16 * (z % 16) + 256 * (y % 16)]
    if not 0 <= index < len(palette):
        detail = "saved block palette index out of range"
        raise ValueError(detail)
    return cast("dict[str, object]", palette[index])


def saved_content_observations(  # noqa: C901, PLR0912 - one locked manifest-bound world pass
    world: Path,
    requested: dict[str, set[tuple[int, int, int]]],
    world_files: dict[str, str],
    geometry: dict[str, tuple[int, int]],
) -> dict[str, object]:
    """Inspect requested positions in a stopped, manifest-bound world."""
    found = {}
    inputs = {}
    targets: dict[tuple[str, int, int], list[tuple[int, int, int]]] = collections.defaultdict(list)
    for dimension, points in requested.items():
        for position in points:
            targets[(dimension, position[0] // 16, position[2] // 16)].append(position)
    with _world_backup_lock(world):
        for path, context in world_regions(world, dimension_geometry=geometry):
            if context.dimension not in requested:
                continue
            if not path.resolve().is_relative_to(world.resolve()):
                detail = "saved-content region escapes world"
                raise ValueError(detail)
            before = hashlib.sha256(path.read_bytes()).hexdigest()
            if world_files.get(context.relative_path) != before:
                detail = "saved-content region differs from retained world manifest"
                raise ValueError(detail)
            inputs[context.relative_path] = before
            for record, payload in decode_region_payloads(path, context):
                if record.external:
                    external = path.with_name(f"c.{record.chunk_x}.{record.chunk_z}.mcc")
                    name = external.relative_to(world).as_posix()
                    if not external.resolve().is_relative_to(world.resolve()):
                        detail = "saved-content external chunk escapes world"
                        raise ValueError(detail)
                    digest = hashlib.sha256(external.read_bytes()).hexdigest()
                    if world_files.get(name) != digest:
                        detail = "saved-content external chunk differs from retained world manifest"
                        raise ValueError(detail)
                    inputs[name] = digest
                key = (context.dimension, record.chunk_x, record.chunk_z)
                if key not in targets:
                    continue
                chunk = decode_compound_nbt(payload)
                for position in targets[key]:
                    state = saved_block_at(chunk, position)
                    found[(context.dimension, *position)] = {
                        "dimension": context.dimension,
                        "position": list(position),
                        "chunk_status": record.status,
                        "saved_state": state,
                        "unavailable_reason": None
                        if state is not None
                        else "MISSING_BLOCK_SECTION",
                    }
        for name, digest in inputs.items():
            if hashlib.sha256((world / name).read_bytes()).hexdigest() != digest:
                detail = "saved-content input changed during inspection"
                raise ValueError(detail)
    observations = [
        found.get(
            (dimension, *position),
            {
                "dimension": dimension,
                "position": list(position),
                "chunk_status": None,
                "saved_state": None,
                "unavailable_reason": "MISSING_CHUNK",
            },
        )
        for dimension, points in sorted(requested.items())
        for position in sorted(points)
    ]
    return {
        "observations": observations,
        "anvil_inputs": [
            {"path": name, "sha256": digest} for name, digest in sorted(inputs.items())
        ],
    }


def generation_digest(payload: bytes) -> str:
    """Hash the predeclared generation projection without tick or entity movement state."""
    root = decode_compound_nbt(payload, preserve_types=True)
    sections = root["sections"]
    projection = {
        "sections": {
            **sections,
            "value": sorted(
                (
                    {
                        **row,
                        "value": {
                            key: row["value"][key]
                            for key in ("Y", "block_states", "biomes")
                            if key in row["value"]
                        },
                    }
                    for row in sections["value"]
                ),
                key=lambda row: row["value"]["Y"]["value"],
            ),
        },
        "structures": root["structures"],
    }
    if "block_entities" in root:
        entities = root["block_entities"]
        projection["block_entities"] = {
            **entities,
            "value": sorted(
                entities["value"],
                key=lambda row: tuple(row["value"][key]["value"] for key in ("x", "y", "z")),
            ),
        }
    encoded = json.dumps(projection, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(encoded.encode()).hexdigest()


def occurrence_anchor(
    row: dict[str, str | int], bounds: tuple[int, int, int, int]
) -> tuple[int, int]:
    """Use explicit block anchors, retaining the registry start-center convention."""
    min_x, max_x, min_z, max_z = bounds
    chunk_x, chunk_z = row["chunk_x"], row["chunk_z"]
    if type(chunk_x) is not int or type(chunk_z) is not int:
        detail = "occurrence chunk coordinates must be integers"
        raise ValueError(detail)
    if not (min_x <= chunk_x <= max_x and min_z <= chunk_z <= max_z):
        detail = "occurrence outside selected chunk frame"
        raise ValueError(detail)
    if ("anchor_x" in row) != ("anchor_z" in row):
        detail = "occurrence needs both horizontal anchor coordinates"
        raise ValueError(detail)
    x, z = row.get("anchor_x", 16 * chunk_x + 8), row.get("anchor_z", 16 * chunk_z + 8)
    if type(x) is not int or type(z) is not int:
        detail = "occurrence anchors must be integer block coordinates"
        raise ValueError(detail)
    if x // 16 != chunk_x or z // 16 != chunk_z:
        detail = "occurrence anchor disagrees with inclusion chunk"
        raise ValueError(detail)
    return x, z


def spatial_summary(
    occurrences: list[dict[str, str | int]], bounds: tuple[int, int, int, int]
) -> dict[str, object]:
    """Describe fixed-grid density and distances using declared location anchors."""
    min_x, max_x, min_z, max_z = bounds
    points = [occurrence_anchor(row, bounds) for row in occurrences]
    neighbors = []
    for index, (x, z) in enumerate(points):
        boundary = min(x - 16 * min_x, 16 * (max_x + 1) - x, z - 16 * min_z, 16 * (max_z + 1) - z)
        distance = min(
            (math.dist((x, z), other) for i, other in enumerate(points) if i != index), default=None
        )
        exact = distance is not None and distance <= boundary
        neighbors.append(
            {
                **occurrences[index],
                "nearest_observed_blocks": distance,
                "boundary_distance_blocks": boundary,
                "boundary_censored": not exact,
                "nearest_distance_lower_bound_blocks": distance if exact else boundary,
            }
        )
    cells = []
    counts = collections.Counter(
        (int(row["chunk_x"]) // 16, int(row["chunk_z"]) // 16) for row in occurrences
    )
    for cell_z in range(min_z // 16, max_z // 16 + 1):
        for cell_x in range(min_x // 16, max_x // 16 + 1):
            x0, x1 = max(min_x, cell_x * 16), min(max_x, cell_x * 16 + 15)
            z0, z1 = max(min_z, cell_z * 16), min(max_z, cell_z * 16 + 15)
            cells.append(
                {
                    "bounds_chunks": [x0, x1, z0, z1],
                    "full_chunks": (x1 - x0 + 1) * (z1 - z0 + 1),
                    "count": counts[cell_x, cell_z],
                }
            )
    full_cell_chunks = 16 * 16
    full_cells = [cell for cell in cells if cell["full_chunks"] == full_cell_chunks]
    cell_counts = [cell["count"] for cell in full_cells]
    mean = sum(cell_counts) / len(cell_counts) if cell_counts else None
    dispersion = (
        sum((count - mean) ** 2 for count in cell_counts) / len(cell_counts) / mean
        if mean
        else None
    )
    # Maximal all-zero rectangle on the fully observed 16-chunk grid.
    empty = {
        (cell["bounds_chunks"][0] // 16, cell["bounds_chunks"][2] // 16)
        for cell in full_cells
        if cell["count"] == 0
    }
    best_area, best_bounds = 0, None
    for top in range(min_z // 16, max_z // 16 + 1):
        eligible = set(range(min_x // 16, max_x // 16 + 1))
        for bottom in range(top, max_z // 16 + 1):
            eligible &= {x for x in eligible if (x, bottom) in empty}
            left = None
            for right in range(min_x // 16, max_x // 16 + 2):
                if right in eligible:
                    left = right if left is None else left
                    continue
                if left is not None:
                    area = (right - left) * (bottom - top + 1) * 256
                    rectangle = [left * 16, right * 16 - 1, top * 16, (bottom + 1) * 16 - 1]
                    if area > best_area or (area == best_area and rectangle < best_bounds):
                        best_area, best_bounds = area, rectangle
                    left = None
    distances = [row["nearest_observed_blocks"] for row in neighbors]
    return {
        "coordinate_convention": "horizontal centers of authoritative start chunks, in blocks",
        "nearest_neighbors": neighbors,
        "mean_nearest_observed_blocks": (
            sum(distances) / len(distances) if len(distances) > 1 else None
        ),
        "mean_nearest_neighbor_blocks": (
            sum(distances) / len(distances)
            if distances and all(not row["boundary_censored"] for row in neighbors)
            else None
        ),
        "mean_rule": "null if no observations or any boundary-censored neighbor; no dropped cases",
        "grid_cell_side_chunks": 16,
        "cells": cells,
        "full_cell_count": len(full_cells),
        "full_cell_variance_over_mean": dispersion,
        "full_cell_zero_fraction": len(empty) / len(full_cells) if full_cells else None,
        "largest_empty_full_cell_rectangle": {
            "area_chunks": best_area,
            "bounds_chunks": best_bounds,
        },
    }


def category_occurrences(
    rows: list[dict[str, object]],
) -> dict[str, list[dict[str, object]]]:
    """Select overlapping specification categories without duplicating a start within one."""
    categories = {"all_registry": rows}
    categories.update(
        {
            role: [row for row in rows if row["role"] == role]
            for role in ("T0", "C", "T1", "T2", "T3", "T4")
        }
    )
    categories["actionable_candidates"] = [
        row for row in rows if row["role"] in ("C", "T1", "T2", "T3", "T4")
    ]
    categories["encounter_sites"] = [row for row in rows if row["role"] in ("T1", "T2", "T3", "T4")]
    categories["villages"] = [
        row for row in rows if "village" in cast("list[str]", row["comparison_groups"])
    ]
    return categories


def nonregistry_membership() -> dict[str, dict[str, str]]:  # noqa: C901 - direct inventory joins
    """Reuse the frozen forty-family membership, not template filename heuristics."""
    source = Path(__file__).resolve().parents[1] / "evidence/item-8/inventory.json"
    payload = source.read_bytes()
    if (
        hashlib.sha256(payload).hexdigest()
        != "4f7853b7b6531f99d3f0592b2129291d2e0cf24b4ad5d1381b3883dbdcfbc52d"
    ):
        detail = "accepted nonregistry inventory identity changed"
        raise ValueError(detail)
    inventory = json.loads(payload)
    contributions = inventory["non_registry_content"]["contributions"]
    templates: dict[str, str] = {}
    for group in ("betterend:biome_buildings", "betterend:biome_ruins"):
        for family, design in contributions[group]["designs"].items():
            for path in design.get("templates", [design.get("template")]):
                templates["/" + path] = family
    for group in (
        "yungsbridges:bridges",
        "yungsextras:feature_entrypoints",
        "betterendisland:platform_gateway",
    ):
        for family in contributions[group]["families"]:
            for path in family["templates"]:
                if path in templates and templates[path] != family["family"]:
                    detail = "one template belongs to multiple accepted families"
                    raise ValueError(detail)
                templates[path] = family["family"]
    templates["minecraft:end_city/ship"] = "betterend:crashed_ship"
    end_features = "org/betterx/betterend/world/features/"
    quark_generators = "org/violetmoon/quark/content/world/gen/"
    classes = {
        SCARECROW_CLASS: "explorations:scarecrow",
        "biomesoplenty/worldgen/feature/misc/AnomalyFeature": "biomesoplenty:anomaly",
        "biomesoplenty/worldgen/feature/misc/MonolithFeature": "biomesoplenty:monolith",
        quark_generators + "MonsterBoxGenerator": "quark:monster_box",
        quark_generators + "ObsidianSpikeGenerator": "quark:nether_obsidian_spike",
        quark_generators + "SpiralSpireGenerator": "quark:spiral_spire",
        quark_generators + "FairyRingGenerator": "quark:fairy_ring",
        URN: "supplementaries:cave_urn_cache",
        end_features + "CrashedShipFeature": "betterend:crashed_ship",
        end_features + "terrain/FallenPillarFeature": "betterend:ruined_obsidian_pillar",
        end_features + "terrain/ObsidianPillarBasementFeature": "betterend:ruined_obsidian_pillar",
        BRIDGE_ROOT + "feature/BridgeFeature": "yungsbridges:bridge",
    }
    for name, family in {
        "BetterEndGatewayFeature": "gateway",
        "BetterEndSpawnPlatformFeature": "arrival_platform",
        "BetterSpikeFeature": "dragon_arena",
        "BetterEndPodiumFeature": "dragon_arena",
    }.items():
        classes["com/yungnickyoung/minecraft/betterendisland/world/feature/" + name] = (
            "betterendisland:" + family
        )
    for name, family in {
        "desert/ChillzoneDesertFeature": "desert_chillzone",
        "desert/DesertGiantTorchFeature": "desert_giant_torch",
        "desert/DesertSmallRuinsFeature": "desert_small_ruins",
        "desert/DesertObeliskFeature": "desert_obelisk",
        "desert/DesertWellFeature": "desert_well",
        "swamp/SwampArchFeature": "swamp_arch",
        "swamp/SwampDoubleArchFeature": "swamp_arch",
        "swamp/SwampChurchFeature": "swamp_church",
        "swamp/SwampCubbyFeature": "swamp_cubby",
        "swamp/SwampOgreFeature": "swamp_ogre",
        "swamp/SwampPillarFeature": "swamp_pillar",
    }.items():
        classes["com/yungnickyoung/minecraft/yungsextras/world/feature/" + name] = (
            "yungsextras:" + family
        )
    accepted = {
        name for name, family in inventory["families"].items() if not family["structure_ids"]
    }
    if set(templates.values()) | set(classes.values()) != accepted:
        detail = "collector membership does not cover exactly the accepted nonregistry families"
        raise ValueError(detail)
    excluded = {
        "/" + path: disposition["decision"]
        for disposition in contributions["betterend:biome_ruins"]["dispositions"]
        for path in disposition["templates"]
    }
    for contribution in ("betterend:lantern_woods/light_1", "betterend:blossoming_spires/house"):
        entry = contributions[contribution]
        excluded["/" + entry["template"]] = entry["dispositions"][0]["decision"]
    return {"classes": classes, "templates": templates, "excluded": excluded}


def attribute_nonregistry_attempt(
    rows: list[dict[str, object]], membership: dict[str, dict[str, str]]
) -> dict[str, object]:
    """Attribute an already paired attempt without assuming successful placement."""
    feature_rows = [row for row in rows if row["kind"] == "feature"]
    feature = str(feature_rows[0]["class"]).replace(".", "/") if feature_rows else SCARECROW_CLASS
    paths = [str(row["path"]) for row in rows if row["kind"] == "template_begin"]
    family = membership["classes"].get(feature)
    if family is None and feature not in {
        "org/betterx/betterend/world/features/BuildingListFeature",
        "org/betterx/betterend/world/features/NBTFeature",
    }:
        detail = "unmapped nonregistry generator class"
        raise ValueError(detail)
    dispositions = [membership["excluded"].get(path) for path in paths]
    if "DISCONNECTED_TEMPLATE_NOT_ADDITIONAL_ACTIVE_FAMILY" in dispositions:
        detail = "observed disconnected template contradicts accepted active-route inventory"
        raise ValueError(detail)
    if paths and all(value == "AMBIENT_DECORATION_NOT_ADDITIONAL_FAMILY" for value in dispositions):
        if family is not None:
            detail = "accepted generator selected only excluded decoration"
            raise ValueError(detail)
        return {
            "attempt": rows[0]["attempt"],
            "family": None,
            "reason": "AMBIENT_DECORATION_NOT_ADDITIONAL_FAMILY",
            "templates": paths,
        }
    selected = {membership["templates"][path] for path in paths if path in membership["templates"]}
    if any(path not in membership["templates"] for path in paths):
        return {
            "attempt": rows[0]["attempt"],
            "family": None,
            "reason": "UNMAPPED_TEMPLATE",
            "templates": paths,
        }
    if len(selected) > 1 or (family is not None and selected and selected != {family}):
        detail = "observed template and generator family identities disagree"
        raise ValueError(detail)
    if family is None:
        family = next(iter(selected), None)
    if family == "supplementaries:cave_urn_cache":
        parents = [row["placed_feature"] for row in rows if row["kind"] == "urn_parent"]
        if parents != ["supplementaries:cave_urns"]:
            return {
                "attempt": rows[0]["attempt"],
                "family": None,
                "reason": "UNRESOLVED_URN_PARENT",
                "templates": paths,
            }
    return {
        "attempt": rows[0]["attempt"],
        "family": family,
        "reason": "ATTRIBUTED" if family else "NO_DESIGN_SELECTED",
        "templates": paths,
    }


def nonregistry_attempt_outcome(  # noqa: C901, PLR0912, PLR0915 - one ordered provider event pass
    rows: list[dict[str, object]], membership: dict[str, dict[str, str]]
) -> dict[str, object]:
    """Retain observed content and failures for later saved-world location acceptance."""
    result = attribute_nonregistry_attempt(rows, membership)
    family = result["family"]
    origin = cast("list[int]", rows[0]["origin"])
    templates = [row for row in rows if row["kind"] == "template_begin"]
    anchor = origin
    if templates and isinstance(family, str) and not family.startswith("betterendisland:"):
        anchor = cast("list[int]", templates[0]["position"])
    fills = [row for row in rows if row["kind"] == "pillar_fill"]
    if fills:
        anchor = cast("list[int]", fills[0]["position"])
    if family == "betterendisland:dragon_arena":
        anchor = [0, origin[1], 0]
    # A template's support/erosion writes cannot alone establish template content.
    template_family = family in set(membership["templates"].values())
    final_writes: dict[tuple[int, ...], str] = {}
    content_positions: set[tuple[int, ...]] = set()
    in_template = False
    writer_site = None
    refused = 0
    for row in rows:
        kind = row["kind"]
        if kind == "template_begin":
            in_template = True
        elif kind in {"template_end", "template_exception"}:
            in_template = False
        elif kind == "writer":
            writer_site = row["site"]
        elif kind == "write":
            if row["returned"] is False:
                refused += 1
                continue
            position = tuple(cast("list[int]", row["position"]))
            state = str(row["state"])
            if not state.startswith("Block{") or "}" not in state:
                detail = "unrecognized recorded block-state representation"
                raise ValueError(detail)
            block_id = state.split("}", 1)[0][len("Block{") :]
            final_writes[position] = block_id
            eligible = in_template if template_family else True
            if family == "quark:fairy_ring" and writer_site == 193:  # noqa: PLR2004 - cleanup site
                eligible = False
            if family == "supplementaries:cave_urn_cache":
                eligible = block_id == "supplementaries:urn"
            if eligible:
                content_positions.add(position)
    air = {"minecraft:air", "minecraft:cave_air", "minecraft:void_air"}
    surviving = sorted(
        position for position in content_positions if final_writes[position] not in air
    )
    failure = any(str(row["kind"]).endswith("_exception") for row in rows)
    route = "ordinary_generation"
    if isinstance(family, str) and family.startswith("betterendisland:"):
        contexts = [row for row in rows if row["kind"] == "island_context"]
        route = (
            "ordinary_generation"
            if contexts and contexts[0]["worldgen_region"] is True
            else "non_worldgen_accessor"
            if contexts
            else "unresolved"
        )
    return {
        **result,
        "dimension": rows[0]["dimension"],
        "origin": origin,
        "anchor": anchor,
        "route": route,
        "outcome": (
            "EXCEPTION_WITH_CONTENT"
            if failure and surviving
            else "EXCEPTION"
            if failure
            else "CONTENT_OBSERVED"
            if surviving
            else "NO_CONTENT_OBSERVED"
        ),
        "refused_writes": refused,
        "content_positions": [list(position) for position in surviving],
        "last_successful_writes": [
            {"position": list(position), "block_id": block_id}
            for position, block_id in sorted(final_writes.items())
        ],
    }


def nonregistry_location_groups(
    outcomes: list[dict[str, object]],
    frames: dict[str, tuple[str, tuple[int, int, int, int]]],
) -> dict[str, object]:
    """Group one world's candidate sources without accepting uncorroborated density."""
    groups: dict[tuple[object, ...], dict[str, object]] = {}
    owners: dict[tuple[object, ...], set[tuple[object, ...]]] = collections.defaultdict(set)
    unresolved = []
    for outcome in outcomes:
        family = outcome["family"]
        if family is None:
            unresolved.append(outcome["attempt"])
            continue
        dimension = outcome["dimension"]
        x, y, z = cast("list[int]", outcome["anchor"])
        # Arena components have different heights, but represent one central site.
        key = (
            dimension,
            family,
            outcome["route"],
            x,
            None if family == "betterendisland:dragon_arena" else y,
            z,
        )
        if key not in groups:
            matched = [
                name
                for name, (frame_dimension, (min_x, max_x, min_z, max_z)) in frames.items()
                if dimension == frame_dimension
                and min_x <= x // 16 <= max_x
                and min_z <= z // 16 <= max_z
            ]
            if len(matched) > 1:
                detail = "nonregistry location belongs to overlapping sample frames"
                raise ValueError(detail)
            groups[key] = {
                "family": family,
                "dimension": dimension,
                "route": outcome["route"],
                "anchor_x": x,
                "anchor_y": key[4],
                "anchor_z": z,
                "chunk_x": x // 16,
                "chunk_z": z // 16,
                "frame": matched[0] if matched else None,
                "attempts": [],
                "outcomes": collections.Counter(),
                "content_positions": set(),
            }
        group = groups[key]
        cast("list[object]", group["attempts"]).append(outcome["attempt"])
        cast("collections.Counter[str]", group["outcomes"])[str(outcome["outcome"])] += 1
        for position in cast("list[list[int]]", outcome["content_positions"]):
            point = tuple(position)
            cast("set[tuple[int, ...]]", group["content_positions"]).add(point)
            owners[(dimension, *point)].add(key)
    # Overlaps are exposed, not silently converted into extra locations or merged.
    ordered = sorted(groups, key=lambda key: tuple(str(value) for value in key))
    indices = {key: index for index, key in enumerate(ordered)}
    overlaps: dict[tuple[int, int], int] = collections.Counter()
    for keys in owners.values():
        ids = sorted(indices[key] for key in keys)
        for offset, first in enumerate(ids):
            for second in ids[offset + 1 :]:
                overlaps[(first, second)] += 1
    locations = []
    for key in ordered:
        group = groups[key]
        positions = sorted(cast("set[tuple[int, ...]]", group["content_positions"]))
        locations.append(
            {
                **group,
                "candidate_id": indices[key],
                "attempts": sorted(cast("list[int]", group["attempts"])),
                "outcomes": dict(sorted(cast("dict[str, int]", group["outcomes"]).items())),
                "content_positions": [list(point) for point in positions],
            }
        )
    return {
        "status": "CANDIDATES_AWAITING_ACCEPTANCE",
        "locations": locations,
        "unattributed_attempts": sorted(unresolved),
        "overlaps": [
            {"candidates": list(pair), "shared_content_positions": count}
            for pair, count in sorted(overlaps.items())
        ],
    }


def classify_census(result: dict[str, object]) -> dict[str, object]:
    """Join measured starts to the exact accepted inventory and provisional matrix."""
    repository = Path(__file__).resolve().parents[1]
    identities = {
        "evidence/item-8/inventory.json": (
            "4f7853b7b6531f99d3f0592b2129291d2e0cf24b4ad5d1381b3883dbdcfbc52d"
        ),
        "evidence/item-9/classification.md": (
            "dc78d81691401bad9fc646f1fe790b14bbf1341f595db5e6cbec9a4f1111b710"
        ),
    }
    contents = {}
    for name, expected in identities.items():
        contents[name] = (repository / name).read_bytes()
        if hashlib.sha256(contents[name]).hexdigest() != expected:
            detail = f"accepted classification input identity changed: {name}"
            raise ValueError(detail)
    inventory = json.loads(contents["evidence/item-8/inventory.json"])
    family_by_root = {
        root: family
        for family, data in inventory["families"].items()
        for root in data["structure_ids"]
    }
    # Reuse the accepted Item 9 table format. Exact hashes bind its reviewed coverage.
    rows = [
        [cell.strip() for cell in line.split("|")[1:-1]]
        for line in contents["evidence/item-9/classification.md"].decode().splitlines()
        if line.startswith("|")
    ][2:]
    classifications = {row[0]: row[1:] for row in rows}
    occurrences = cast("list[dict[str, str | int]]", result["occurrences"])
    full_chunks = cast("int", result["full_chunks"])
    annotated = []
    counts = dict.fromkeys(("T0", "C", "T1", "T2", "T3", "T4"), 0)
    for occurrence in occurrences:
        root = occurrence["registry_id"]
        if root not in family_by_root:
            detail = f"observed registry start is outside accepted active families: {root}"
            raise ValueError(detail)
        family = family_by_root[root]
        role, confidence, flags, groups, rationale, ambiguity = classifications[family]
        annotated.append(
            {
                **occurrence,
                "family_id": family,
                "role": role,
                "confidence": confidence,
                "flags": flags,
                "comparison_groups": groups.split(","),
                "rationale": rationale,
                "ambiguity": ambiguity,
            }
        )
        counts[role] += 1
    return {
        "scope": "registry occurrences by provisional family role; not observed combat",
        "input_sha256": identities,
        "occurrences": annotated,
        "categories": {
            name: {"count": len(rows), "per_1000_chunks": 1000 * len(rows) / full_chunks}
            for name, rows in category_occurrences(annotated).items()
        },
        "exclusive_roles": {
            role: {"count": count, "per_1000_chunks": 1000 * count / full_chunks}
            for role, count in counts.items()
        },
    }


def start_origins(payload: bytes, chunk: tuple[int, int]) -> list[dict[str, str | int]]:
    """Require the stored start coordinates rather than infer them from a log row."""
    root = decode_compound_nbt(payload)
    starts = root.get("structures", {}).get("starts", {})
    result = []
    for identifier, start in sorted(starts.items()):
        if start["id"] == "INVALID":
            continue
        origin = (start.get("ChunkX"), start.get("ChunkZ"))
        if any(type(value) is not int for value in origin) or origin != chunk:
            detail = f"start {identifier} has missing or inconsistent authoritative chunk: {origin}"
            raise ValueError(detail)
        if start["id"] != identifier:
            detail = f"start key/id mismatch: {identifier}, {start['id']}"
            raise ValueError(detail)
        result.append({"registry_id": identifier, "chunk_x": origin[0], "chunk_z": origin[1]})
    return result


def census(  # noqa: C901, PLR0913 - keep optional metrics in the existing single census pass.
    world: Path,
    dimension: str,
    bounds: tuple[int, int, int, int],
    geometry: dict[str, tuple[int, int]],
    *,
    include_biomes: bool = False,
    include_generation: bool = False,
) -> dict[str, object]:
    """Reject incomplete coverage and retain the actual denominator and occurrences."""
    min_x, max_x, min_z, max_z = bounds
    if min_x > max_x or min_z > max_z:
        detail = "bounds must be inclusive ordered min-x max-x min-z max-z"
        raise ValueError(detail)
    expected = (max_x - min_x + 1) * (max_z - min_z + 1)
    seen = set()
    occurrences = []
    inputs = []
    biome_counts = collections.Counter()
    attributed_biomes = []
    generation = []
    for path, context in world_regions(world, dimension_geometry=geometry):
        if context.dimension != dimension:
            continue
        before = hashlib.sha256(path.read_bytes()).hexdigest()
        external_inputs = {}
        for record, payload in decode_region_payloads(path, context):
            x, z = record.chunk_x, record.chunk_z
            if record.external:
                external_path = path.with_name(f"c.{x}.{z}.mcc")
                external_inputs[external_path.relative_to(world).as_posix()] = hashlib.sha256(
                    external_path.read_bytes()
                ).hexdigest()
            if not (min_x <= x <= max_x and min_z <= z <= max_z):
                continue
            if record.status != "minecraft:full" or (x, z) in seen:
                detail = f"selected chunk is incomplete or duplicated: {dimension} {x},{z}"
                raise ValueError(detail)
            seen.add((x, z))
            if include_biomes:
                column = chunk_biome_column(record, context.min_y, context.build_height)
                biome_counts.update(column.items())
                attributed_biomes.extend(occurrence_biomes(record, column))
            occurrences.extend(start_origins(payload, (x, z)))
            generation.extend(
                [{"chunk_x": x, "chunk_z": z, "sha256": generation_digest(payload)}]
                if include_generation
                else []
            )
        if hashlib.sha256(path.read_bytes()).hexdigest() != before:
            detail = f"region changed during census: {path}"
            raise ValueError(detail)
        inputs.append({"path": context.relative_path, "sha256": before})
        inputs.extend(
            {"path": name, "sha256": digest} for name, digest in sorted(external_inputs.items())
        )
    if len(seen) != expected:
        detail = f"incomplete selected coverage: {len(seen)} of {expected} full chunks"
        raise ValueError(detail)
    counts = collections.Counter(row["registry_id"] for row in occurrences)
    result = {
        "scope": "registry starts only; not all-family density or observed combat",
        "dimension": dimension,
        "bounds_chunks": bounds,
        "full_chunks": len(seen),
        "total_starts": len(occurrences),
        "starts_per_1000_chunks": 1000 * len(occurrences) / len(seen),
        "registry_counts": dict(sorted(counts.items())),
        "occurrences": sorted(
            occurrences, key=lambda row: (row["registry_id"], row["chunk_x"], row["chunk_z"])
        ),
        "anvil_inputs": inputs,
    }
    exposure = {
        "scope": "saved chunk-center column biomes; separate quart-height denominators",
        "local_block_xz": [8, 8],
        "rows": [
            {"quart_y": quart_y, "biome": biome, "full_chunks": count}
            for (quart_y, biome), count in sorted(biome_counts.items())
        ],
    }
    return (
        result
        | (
            {"biome_exposure": exposure, "occurrence_biomes": attributed_biomes}
            if include_biomes
            else {}
        )
        | (
            {
                "generation_encoding": "typed-nbt-v2",
                "generation_content": sorted(
                    generation, key=lambda row: (row["chunk_x"], row["chunk_z"])
                ),
            }
            if include_generation
            else {}
        )
    )


def main() -> None:
    """Run an offline census while holding the existing Java-compatible world lock."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("world", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--dimension", required=True)
    parser.add_argument("--bounds", type=int, nargs=4, required=True)
    parser.add_argument("--dimension-geometry", type=Path)
    parser.add_argument("--classify", action="store_true", help="join accepted Item 8/9 inputs")
    parser.add_argument("--spatial", action="store_true", help="add classified spatial summaries")
    parser.add_argument(
        "--biomes", action="store_true", help="retain biome exposure by quart height"
    )
    parser.add_argument("--generation", action="store_true", help="hash declared generated content")
    args = parser.parse_args()
    if args.output.exists() or args.output.resolve().is_relative_to(args.world.resolve()):
        parser.error("output must be new and outside the input world")
    geometry = json.loads(args.dimension_geometry.read_text()) if args.dimension_geometry else {}
    with _world_backup_lock(args.world):
        result = census(
            args.world,
            args.dimension,
            tuple(args.bounds),
            geometry,
            include_biomes=args.biomes,
            include_generation=args.generation,
        )
    if args.classify or args.spatial:
        result["classification"] = classify_census(result)
    if args.spatial:
        rows = result["classification"]["occurrences"]
        result["spatial"] = {
            category: spatial_summary(selected, tuple(args.bounds))
            for category, selected in category_occurrences(rows).items()
        }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
