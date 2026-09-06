from __future__ import annotations

import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item7_nbt import decode_compound_nbt
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


def test_railways_entry_and_player_assembly_sources() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("railways-"))
    assert source.sha256 == "b7636c8b1b0352ed1a130dfe67f8bb574e2fc08803ed1cda4d3ea00505193914"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    captured: set[str] = set()
    with ZipFile(source.path) as archive:
        for label, digest, count in (
            (
                "railways-provider",
                "7eac52c33ecf6f99967a211eca99697b3730139d77b699c1753e0dcbd0cb07a6",
                13,
            ),
            (
                "railways-assembly",
                "bb9a62a1706f5738e5703a319cc69cd680fdcf08c361d4f6bf5319826df9f86f",
                2,
            ),
        ):
            directory = Path("evidence/item-8/sources") / label
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            rows = cast("list[dict[str, str]]", json.loads(raw))
            assert len(rows) == count
            for row in rows:
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
                assert (
                    hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest()
                    == (row["disassembly_sha256"])
                )
                captured.add(row["class"])
        annotated = {
            n
            for n in archive.namelist()
            if n.endswith(".class")
            and any(
                t in archive.read(n)
                for t in (
                    b"Lnet/neoforged/fml/common/Mod;",
                    b"Lnet/neoforged/fml/common/EventBusSubscriber;",
                )
            )
        }
        assert len(annotated) == 8
        assert annotated <= captured


def test_railways_payload_and_vehicle_template() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("railways-"))
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 14066
        assert Counter("classes" if n.endswith(".class") else n.split("/")[0] for n in names) == {
            "classes": 883,
            "assets": 9927,
            "data": 2735,
            "resourcepacks": 502,
            ".cache": 7,
            "datapacks": 4,
            "META-INF": 2,
            "icon.png": 1,
            "architectury.common.json": 1,
            "pack.mcmeta": 1,
            "railways.accesswidener": 1,
            "railways.mixins.json": 1,
            "railways-common.mixins.json": 1,
        }
        assert Counter(n.split("/")[2] for n in names if n.startswith("data/")) == {
            "recipe": 1071,
            "advancement": 660,
            "loot_table": 615,
            "tags": 387,
            "structures": 1,
            "railways_liquid_fuel": 1,
        }
        assert {n for n in names if n.startswith("datapacks/")} == {
            "datapacks/phantom_track_override/pack.mcmeta",
            *(
                "datapacks/phantom_track_override/data/railways/recipe/sequenced_assembly/"
                + n
                + ".json"
                for n in ("track_phantom", "track_phantom_narrow", "track_phantom_wide")
            ),
        }
        for name in names:
            if name.startswith("datapacks/") and name.endswith(".json"):
                assert json.loads(archive.read(name))["type"] == "create:sequenced_assembly"
        templates = [n for n in names if n.endswith(".nbt") and n.startswith("data/")]
        assert templates == ["data/railways/structures/handcar/assembly.nbt"]
        template = decode_compound_nbt(gzip.decompress(archive.read(templates[0])))
        assert template["size"] == [3, 3, 3]
        assert template["entities"] == []
        assert template["DataVersion"] == 3120
        palette = cast("list[dict[str, JsonValue]]", template["palette"])
        assert {cast("str", p["Name"]) for p in palette} == {
            "minecraft:air",
            "create:lime_seat",
            "create:red_seat",
            "railways:handcar",
        }
        blocks = cast("list[dict[str, JsonValue]]", template["blocks"])
        assert len(blocks) == 27
        assert [b["nbt"] for b in blocks if "nbt" in b] == [
            {
                "BogeyData": {"UpsideDown": 0, "BogeyStyle": "railways:handcar"},
                "id": "railways:bogey",
            }
        ]
