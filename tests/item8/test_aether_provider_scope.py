from __future__ import annotations

import hashlib
import io
import json
from collections import Counter
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources

SOURCES = (
    ("aether-bronze",
     "34141e73a72160d007367fd34118d0f7ce68580d0be214e332e018f23555f4b4"),
    ("aether-common-hooks",
     "9c3b21c8bf2eab73550acc646a9c74081c15daac08c941367f298adf0bb8c50f"),
    ("aether-cumulus-entry",
     "78bb4e10beda0be08cf78e0cea85a72ee979a6d3468eda88da9e8f5b3f6018c0"),
    ("aether-cumulus-platform",
     "6d24efec98521b40e946c3fca20f1749c3668d0827efec0d1aee713fe782f707"),
    ("aether-custom-entry",
     "e33ddae6869cc516beafc2eff72976b2db2ee6d7602443d2af389c2778b01954"),
    ("aether-entry-delegates",
     "ee142a691df1c662ddbe2dd642382d40d1801eb85ecb90fc1362ef6920fb0bbf"),
    ("aether-holiday-filter",
     "8bd3d11068bb8ad3118257f19db123ecf37961fdfb5625db475b3def34be130b"),
    ("aether-nitrogen-entry",
     "59c1ee876425079e556752749ae9d957af6927405b26edd14dde6b307f778003"),
    ("aether-nitrogen-world",
     "ed7ad27d398943d86d94bd90bf0e0f0cc88afc32658a19d5459816c2ad48d366"),
    ("aether-piece-binding",
     "659938555001e750eb6f21b84c1b797f9641783d99775916315cab9f68dbb48d"),
    ("aether-placement",
     "14d7c34fe022eaf47cfa324ad56646b2bf4e736b4cfc0a249ddd94b8d1408113"),
    ("aether-provider",
     "917c3ffbb199539bfbe375f4a7381d4498f327a2ce9d5cdc28ad01d978f604ee"),
    ("aether-reload-consumers",
     "5e8b0cfc4241fadf9419c14dc71c1c204ee0b3ccd8a566034497ce9f067e38a1"),
    ("aether-trap-bindings",
     "f2815a15dad2b0e62e2d2db44ce5e27a86476a5ed269a49f186bb18ffa8b1261"),
    ("aether-trapped-block",
     "729a601cbf86cbb65c8e4f7dd16842cc36dfa6ddecf1e86de83b0a00578750c5"),
)


def test_aether_provider_sources_and_payload() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "aether-1.21.1-1.5.10-neoforge.jar")
    assert source.sha256 == "a999a9265eb550a46a0f8eedfee7c3c75371d7f6cf34b7c09ff800e48633e9f8"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        names = {n for n in archive.namelist() if not n.endswith("/")}
        assert Counter(n.split("/")[0] for n in names) == {
            "assets": 1658, "data": 1384, "com": 935, "packs": 526,
            "META-INF": 8, "aether.png": 1, "pack.mcmeta": 1, "aether.mixins.json": 1,
        }
        classes = {n for n in names if n.endswith(".class")}
        assert len(classes) == 935
        assert Counter(n.split("/")[2] for n in names if n.startswith("data/")) == {
            "recipe": 371, "advancement": 343, "tags": 329, "loot_table": 191,
            "worldgen": 75, "structure": 34, "loot_modifiers": 11, "damage_type": 8,
            "jukebox_song": 6, "data_maps": 5, "aether": 3, "trim_material": 3,
            "function": 3, "dimension_type": 1, "dimension": 1,
        }
        assert Counter(n.split("/")[1] for n in names if n.startswith("packs/")) == {
            "classic_base": 342, "classic_b173": 58, "tips": 58, "classic_125": 19,
            "accessories_override": 14, "ruined_portal": 8, "accessories": 7,
            "imm_ptl_compat": 6, "ctm_fix": 5, "colorblind": 4,
            "temporary_freezing": 3, "tooltips": 2,
        }
        functions = {n: archive.read(n).decode() for n in names if n.endswith(".mcfunction")}
        assert functions == {
            "data/aether/function/dev_new_world.mcfunction":
            "# Enter the Aether\nexecute in aether:the_aether run teleport ~ ~ ~\n",
            "data/aether/function/setup_structure_hunt.mcfunction":
            """execute in aether:the_aether run tp @p ~ ~ ~
gamemode spectator @p
effect give @p minecraft:night_vision infinite
""",
            "data/aether/function/dev_powerwash_chunk.mcfunction":
            """execute at @p run fill ~-8 16 ~-8 ~8 128 ~8 minecraft:air replace #minecraft:dirt
execute at @p run fill ~-8 16 ~-8 ~8 128 ~8 minecraft:air replace #c:stones
""",
        }
        assert not any(n.startswith("META-INF/services/") or n.endswith((".js", ".lua", ".py"))
                       for n in names)
        captured: set[str] = set()
        for directory, digest in SOURCES:
            base = Path("evidence/item-8/sources") / directory
            raw = (base / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            for row in cast("list[dict[str, str]]", json.loads(raw)):
                if row["archive"] == source.name:
                    assert row["archive_sha256"] == source.sha256
                    payload = archive.read(row["class"])
                    captured.add(row["class"])
                else:
                    assert row["archive"].startswith(source.name + "!/")
                    nested = archive.read(row["archive"].split("!/", 1)[1])
                    assert hashlib.sha256(nested).hexdigest() == row["archive_sha256"]
                    with ZipFile(io.BytesIO(nested)) as library:
                        payload = library.read(row["class"])
                assert hashlib.sha256(payload).hexdigest() == row["class_sha256"]
                assert hashlib.sha256((base / row["disassembly"]).read_bytes()).hexdigest() == (
                    row["disassembly_sha256"]
                )
        entries = {n for n in classes if b"Lnet/neoforged/fml/common/Mod;" in archive.read(n)}
        assert entries == {"com/aetherteam/aether/Aether.class"}
        assert entries <= captured
        assert not any(b"Lnet/neoforged/fml/common/EventBusSubscriber;" in archive.read(n)
                       for n in classes)
        mixins = cast("dict[str, object]", json.loads(archive.read("aether.mixins.json")))
        common = {"com/aetherteam/aether/mixin/mixins/" + n.replace(".", "/") + ".class"
                  for n in cast("list[str]", mixins["mixins"])}
        assert len(common) == 34
        assert common <= captured
