"""Write fixed template voxel diagrams for canonical design inspection."""

from __future__ import annotations

import argparse
import gzip
import hashlib
from html import escape
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item7_nbt import decode_compound_nbt
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def diagram(raw: bytes, title: str, origin_x: int, origin_y: int, *, exposed: bool = False) -> str:
    """Project occupied block cells; preserve material names in SVG tooltips."""
    root = decode_compound_nbt(gzip.decompress(raw))
    palette = cast("list[dict[str, JsonValue]]", root["palette"])
    blocks = cast("list[dict[str, JsonValue]]", root["blocks"])
    result = [f'<text x="{origin_x}" y="{origin_y}" font-size="14">{escape(title)}</text>']
    sx, sy, sz = cast("list[int]", root["size"])
    step = min(12, 240 / (sx + sz), 180 / (sy + (sx + sz) / 2))
    cells: list[tuple[int, int, int, str]] = []
    for block in blocks:
        x, y, z = cast("list[int]", block["pos"])
        name = str(palette[cast("int", block["state"])]["Name"])
        if name not in {"minecraft:air", "minecraft:cave_air", "minecraft:structure_void"}:
            cells.append((x, y, z, name))
    occupied: set[tuple[int, int, int]] = {(x, y, z) for x, y, z, _ in cells} if exposed else set()
    for x, y, z, name in sorted(cells, key=lambda cell: (sum(cell[:3]), cell[1])):
        if exposed and all(p in occupied for p in ((x + 1, y, z), (x, y + 1, z), (x, y, z + 1))):
            continue
        px = origin_x + 110 + (x - z) * step
        py = origin_y + 180 + (x + z) * step / 2 - y * step
        # Green is a visual hint only, not a membership classifier.
        plant = any(word in name for word in ("leaves", "moss", "vine", "grass", "flower"))
        colors = ("#81a98b", "#486c51", "#608169") if plant else (
            "#aac5e4", "#4e7099", "#7595ba")
        faces = (
            ((px, py - step), (px + step, py - step / 2), (px, py), (px - step, py - step / 2)),
            ((px - step, py - step / 2), (px, py), (px, py + step), (px - step, py + step / 2)),
            ((px, py), (px + step, py - step / 2), (px + step, py + step / 2), (px, py + step)),
        )
        for color, face in zip(colors, faces, strict=True):
            points = " ".join(f"{a},{b}" for a, b in face)
            result.append("".join((f'<polygon points="{points}" fill="{color}" stroke="#34495e" ',
                          f'stroke-width="0.2"><title>{escape(name)}',
                          f" ({x},{y},{z})</title></polygon>")))
    return "\n".join(result)


def parse_args() -> argparse.Namespace:
    """Select one existing comparison set and a fresh output directory."""
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("--output", type=Path, required=True)
    selection = parser.add_mutually_exclusive_group()
    for flag in ("--soaring", "--nether", "--nether-houses", "--nether-arenas",
                 "--nether-landmarks", "--voyager-small", "--voyager-buildings",
                 "--voyager-landmarks", "--terralith-buildings"):
        _ = selection.add_argument(flag, action="store_true")
    return parser.parse_args()


def main() -> None:
    """Render fixed comparison sets from their frozen archive."""
    args = parse_args()
    output = cast("Path", args.output)
    soaring = cast("bool", args.soaring)
    voyager = (cast("bool", args.voyager_small) or cast("bool", args.voyager_buildings)
               or cast("bool", args.voyager_landmarks))
    nether_houses = cast("bool", args.nether_houses)
    nether_arenas = cast("bool", args.nether_arenas)
    nether_landmarks = cast("bool", args.nether_landmarks)
    nether = cast("bool", args.nether) or nether_houses or nether_arenas or nether_landmarks
    archive_name = "MoogsSoaringStructures-1.21-2.1.2.jar" if soaring else "BetterEnd-21.0.31.jar"
    archive_name = "MoogsNetherStructures-1.21-3.0.0-alpha.2.jar" if nether else archive_name
    archive_name = "MoogsVoyagerStructures-1.21-5.0.11.jar" if voyager else archive_name
    archive_name = ("Terralith_1.21.1_v2.6.2_Neoforge.jar"
                    if cast("bool", args.terralith_buildings) else archive_name)
    compressed = soaring or nether or voyager or cast("bool", args.terralith_buildings)
    source = next(s for s in retained_sources(Path.cwd()) if s.name == archive_name)
    if hashlib.sha256(source.path.read_bytes()).hexdigest() != source.sha256:
        message = f"Archive identity mismatch: {archive_name}"
        raise ValueError(message)
    output.mkdir(parents=True, exist_ok=False)
    with ZipFile(source.path) as archive:
        sheets = {
            biome: [f"biome/{biome}/ruins_{i + 1}" for i in range(count)]
            for biome, count in {
                "blossoming_spires": 8, "chorus_forest": 8, "foggy_mushroomland": 3,
                "lantern_woods": 2, "shadow_forest": 8, "umbrella_jungle": 6,
            }.items()
        }
        if soaring:
            sheets = {
                "houses": ["calcite_house", "diorite_house", "small_deepslate_house",
                           "small_oak_house", "spruce_huts", "white_house"],
                "towers": ["castle_ruin", "castle_tower", "large_tower", "small_tower"],
                "landscapes": ["frozen_pond", "muddy_water_hole", "small_pond", "jungle",
                               "leaf_hollow", "mangrove"],
                "islands": ["mushroom", "palm_island", "red_sand", "taiga", "volcano"],
                "monuments": ["desert_pyramid", "desert_pyramid_side", "desert_pyramid_top",
                              "desert_well", "nether_portal"],
            }
        namespace = "mss" if soaring else "betterend"
        if nether:
            namespace = "mns"
            sheets = {
                "skulls_shrines_towers": ["giant_skull", "sandy_skull", "shrine",
                                         "smoking_shrine", "copper_tower", "nether_tower"],
                "pools": ["lava_pool", "lava_pool_lower", "warped_pool", "warped_pool_lower"],
            }
        if nether_houses:
            sheets = {
                "house_comparison": ["houses/medium_house_1", "houses/medium_house_2",
                                     "houses/large_house_1", "crimson_forge"],
                "warped_houses": [f"houses/warped_house_{i}" for i in range(1, 7)],
            }
        if nether_arenas:
            sheets = {
                "small_arena": [f"small_arena/{n}" for n in ("middle", "front", "back", "left")],
                "large_arena": [f"large_arena/{n}" for n in ("r1", "r2", "r3", "l1", "l2", "l3")],
                "dragon_upper": [f"dragon_arena/{n}" for n in
                                 ("head", "c1", "c2", "l1", "l2", "r1", "r2")],
                "dragon_lower": [f"dragon_arena/lower_{i}" for i in range(1, 14)],
            }
        if nether_landmarks:
            sheets = {
                "landmarks": ["grave_yard", "nether_wart_farm", "ruins/ruined_portal", "soul_fire",
                              "sword", "train", "warped_dome"],
                "well_ruin_comparison": ["wells/crimson_lava_well", "wells/medium_crimson_well",
                                        "wells/medium_crimson_well_lower",
                                        "wells/medium_warped_well",
                                        "wells/medium_warped_well_lower",
                                        "ruins/circle_blackstone", "ruins/circle_nether_brick"],
            }
        if voyager:
            namespace = "mvs"
            sheets = {
                "benches": [f"other_decoration/{n}" for n in
                            ("large_bench", "medium_bench", "small_bench_1",
                             "small_bench_2", "small_bench_3")],
                "harvest_heaps": [f"other_decoration/{n}" for n in
                                  ("haystack", "small_haystack", "mixed_pile",
                                   "pumpkin_pile", "small_pumpkin_pile")],
                "paths": ["nature/long_oak_pathway", "nature/short_oak_pathway"],
            } if cast("bool", args.voyager_small) else {
                "houses": [f"houses/{n}" for n in
                           ("azelea_house", "deepslate_house", "desert_house", "flower_hole",
                            "house", "small_swamp_house", "tall_house", "warped_house")],
                "outbuildings": ["houses/barn", "shed", "out_house/out_house",
                                 "out_house/out_house_lower"],
                "towers": ["cartographer_tower/base", "cartographer_tower/top",
                           "jungle_tower/base", "jungle_tower/bottom", "jungle_tower/top",
                           "ocean_tower", "small_pillager_tower"],
                "nether_towers": ["houses/large_warped_tower", "houses/large_warped_tower_top",
                                  "houses/red_tower", "houses/red_tower_top"],
            } if cast("bool", args.voyager_buildings) else {
                "facilities": ["beach_bar", "other_decoration/crimson_enchanting_table",
                               "other_decoration/desert_pump", "horse_pen",
                               "other_decoration/lamp_chest", "other_decoration/lecturn_garden",
                               "other_decoration/wheat_grain_bin",
                               "other_decoration/wooden_wheat_farm"],
                "ruins": [f"ruins/{n}" for n in
                          ("castle_ruins", "log_ruin", "ruined_beacon", "small_ruin",
                           "statue_ruins", "stone_pillars", "tree_monument")],
                "sculptures": [f"other_decoration/{n}" for n in
                               ("duck", "mushroom_statue", "nether_devil", "snowy_medium_fossil",
                                "villager_statue")],
                "shelters": ["other_decoration/bee_dome", "other_decoration/fox_hut",
                             "other_decoration/snowy_dog_hut", "nature/large_mushroom"],
                "landmarks": ["crystal/base", "crystal/lower", "gallows", "railway",
                              "small_ship", "stone_fountain", "sunzi_gate",
                              "other_decoration/small_windmill"],
            }
        namespace = "terralith" if cast("bool", args.terralith_buildings) else namespace
        sheets = {
            "surface": ["regular/desert_outpost", "regular/valley_lodge",
                        "regular/igloo", "regular/glacial/interior1",
                        "regular/glacial/interior2", "regular/glacial/interior216"],
            "underground": [f"underground/{n}" for n in
                            ("small_ruined_oak_cabin", "large_ruined_oak_cabin",
                             "smallminingoutpost", "largeminingoutpost",
                             "old_refinery", "sunken_tower")],
            "mage_towers": [f"mage/{n}" for n in
                            ("tower", "spring_tower", "summer_tower",
                             "autumn_tower", "winter_tower")],
            "mage_complex": [f"mage/{n}" for n in
                             ("complex", "barracks", "house", "house2", "house3",
                              "road_straight", "road_crosswalk")],
        } if cast("bool", args.terralith_buildings) else sheets
        for biome, names in sheets.items():
            count = len(names)
            pieces: list[str] = []
            for index, name in enumerate(names):
                raw = archive.read(f"data/{namespace}/structure/{name}.nbt")
                title = name if compressed else name.rsplit("/", 1)[1]
                pieces.append(diagram(raw, title, 20 + index % 2 * 300,
                                      35 + index // 2 * 300, exposed=compressed))
            height = ((count + 1) // 2) * 300
            svg = "".join((
                f'<svg xmlns="http://www.w3.org/2000/svg" width="620" height="{height}">',
                   '<rect width="100%" height="100%" fill="white"/>',
                   "\n".join(pieces), "</svg>"))
            payload = (svg + "\n").encode()
            payload = gzip.compress(payload, mtime=0) if compressed else payload
            suffix = ".svg.gz" if compressed else ".svg"
            _ = (output / f"{biome}{suffix}").write_bytes(payload)


if __name__ == "__main__":
    main()
