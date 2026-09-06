from __future__ import annotations

import hashlib
import json
import tomllib
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

import pytest

from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue


@pytest.mark.parametrize(("name", "count", "manifest", "other_files", "entry_classes"), [
    ("ai-improvements", 20,
     "15b2c2a5826ddbfea4b8befab50ba609ac1ec17de1540a169fac968c08b06bbd",
     {"META-INF/accesstransformer.cfg", "pack.mcmeta"},
     {"com/builtbroken/ai/improvements/AIImprovements.class"}),
    ("attributefix", 5,
     "6b5f5497616109f88376d894557a498edcf9b97bccb58e8e639702dca1d9206b",
     {"attributefix.neoforge.mixins.json", "attributefix.mixins.json",
      "logo_attributefix.png", "pack.mcmeta", "license_attributefix.txt"},
     {"net/darkhax/attributefix/impl/NeoForgeMod.class"}),
    ("leavesbegone", 12,
     "19cc43de2ea86c8bc0f3f6212f49903de293517fe1d78ddef0c805e3f0584af4",
     {"CHANGELOG.md", "LICENSE-ASSETS.md", "LICENSE.md", "META-INF/accesstransformer.cfg",
      "leavesbegone.common.mixins.json", "leavesbegone.common.refmap.json",
      "leavesbegone.neoforge.mixins.json", "mod_banner.png", "mod_logo.png", "pack.mcmeta"},
     {"fuzs/leavesbegone/neoforge/LeavesBeGoneNeoForge.class",
      "fuzs/leavesbegone/neoforge/client/LeavesBeGoneNeoForgeClient.class"}),
    ("letmedespawn", 6,
     "57020da079e8b92682e1bf9e6b7328b281a034c4c543966bd8c2e126d96a90bc",
     {"META-INF/accesstransformer.cfg", "architectury.common.json",
      "letmedespawn-1.21.x-common-common-refmap.json", "letmedespawn.accesswidener",
      "letmedespawn.mixins.json", "lmd.png"},
     {"com/frikinjay/letmedespawn/neoforge/LetMeDespawnNeoForge.class"}),
    ("sparsestructures", 14,
     "33d153974364c484e57da384dc44729b0d61cb3628dc529f4020f62e97337c54",
     {"sparsestructures.mixins.json", "sparse-structures-default-config.json5",
      "META-INF/services/io.github.maxencedc.sparsestructures.platform.services.IPlatformHelper",
      "sparsestructures.png", "pack.mcmeta", "sparsestructures.neoforge.mixins.json",
      "LICENSE_SparseStructures"},
     {"io/github/maxencedc/sparsestructures/SparseStructuresNeoForge.class"}),
    ("structure-pool-api", 12,
     "0c401d9a9c6234c9dceb36d6d5e108c1eb0daf90c7d6dc0c4fa8fbddc6837538",
     {"META-INF/accesstransformer.cfg", "icon.png", "structure_pool.mixins.json",
      "structure_pool_api-common-common-refmap.json"},
     {"net/fabric_extras/structure_pool/neoforge/NeoForgeMod.class"}),
    ("almanac", 13,
     "846bc2adbd79f5625a83d1fd71ea8be43843b42b3ce16e7b001035f0c9fe6bb1",
     {"Almanac-1.21.1-2-common-common-refmap.json", "almanac.mixins.json", "almanac.png"},
     {"com/frikinjay/almanac/neoforge/AlmanacNeoForge.class"}),
    ("libraryferret", 9,
     "818982bd379cd4f31dc2ece2b16bd22cdbc1332cac40de8a56c87f34b4b60e65",
     {"assets/libraryferret/lang/en_us.json", "pack.mcmeta", "changelog.md",
      "license_libraryferret.txt", "icon.png", "pack.png",
      *(f"assets/libraryferret/{kind}/item/{coin}_coins_jtl.{ext}"
        for kind, ext in (("models", "json"), ("textures", "png"))
        for coin in ("diamond", "emerald", "gold", "iron", "netherite")),
      *(f"data/libraryferret/recipes/{kind}/{coin}_coins_jtl.json"
        for kind in ("blasting", "smelting")
        for coin in ("diamond", "emerald", "gold", "iron", "netherite"))},
     {"com/jtorleonstudios/libraryferret/LibraryFerret.class"}),
    ("structure-layout-optimizer", 16,
     "3a24a425f1eae35abdb77547922cedf22f9212c09a69043b4f6baf95b1e5d197",
     {"assets/structure_layout_optimizer/lang/en_us.json",
      "META-INF/services/telepathicgrunt.structure_layout_optimizer.services.PlatformService",
      "structure_layout_optimizer.mixins.json", "structure_layout_optimizer.png",
      "LICENSE_Structure Layout Optimizer.txt"},
     {"telepathicgrunt/structure_layout_optimizer/neoforge/entrypoints/Main.class"}),
    ("bundle-api", 19,
     "761564dccceb00a1ee3e781dd8380987076f885d8d14d011d03e172522d0f59a",
     {"bundle-api-common-common-refmap.json", "bundleapi.mixins.json", "icon.png"},
     {"com/github/theredbrain/neoforge/NeoForgeMod.class"}),
    ("shield-api", 11,
     "d713942af83a5e1f30c824e2cef9b04cde23d2024ba46d7955b57ec3d457cd2b",
     {"icon.png", "shield_api-common-common-refmap.json", "shield_api.mixins.json"},
     {"net/fabric_extras/neoforge/NeoForgeMod.class"}),
    ("projectile-library", 34,
     "7ee4ba1c377fb21900a6a47e8ac3a041ab29128fd250f97bbdb611d4b77656a1",
     {"icon.png", "pack.mcmeta", "ritchiesprojectilelib-forge.mixins.json",
      "ritchiesprojectilelib.accesswidener", "ritchiesprojectilelib.mixins.json"},
     {"rbasamoyai/ritchiesprojectilelib/neoforge/RitchiesProjectileLibNeoForge.class"}),
    ("fastasyncworldsave", 6,
     "4b60ee73ab2950958e58b4d5cede24ab5055d75693f3434ddec4e6438fd5d9a2",
     {"fastasyncworldsave.mixins.json", "META-INF/accesstransformer.cfg", "pack.mcmeta"},
     {"com/fastasyncworldsave/FastAsyncWorldSave.class"}),
    ("structureessentials", 26,
     "2cb92ed499c3a7fa07688426be09e5a59b0939adb21ce7151a102982a203a6a5",
     {"structureessentials.mixins.json", "META-INF/accesstransformer.cfg",
      "assets/modid/icon.png", "pack.mcmeta"},
     {"com/structureessentials/StructureEssentials.class"}),
    ("cupboard", 18,
     "f8d8e32b71dd0c3bc4c112b4a11c074563d2368e59b2cfe12ee755bbfb9bd022",
     {"cupboard.mixins.json", "META-INF/accesstransformer.cfg", "pack.mcmeta"},
     {"com/cupboard/Cupboard.class"}),
    ("alternate-current", 30,
     "8838261bd796edf444cfbf312d9f6bd8f779d09deae3472b68ed510a4c78ec7f",
     {"alternate-current.mixins.json", "assets/alternate/current/icon.png"},
     {"alternate/current/AlternateCurrentMod.class"}),
    ("lootintegrations", 9,
     "0f49a269c6f23ed70f832752833a5c8c0d00a18f33737d147644015c5fe0c137",
     {"lootintegrations.mixins.json", "META-INF/accesstransformer.cfg", "pack.mcmeta",
      "data/lootintegrations/tags/item/ignored.json",
      "data/lootintegrations/loot/dungeonloot_no_overflow.json",
      *("data/lootintegrations/loot/lootintegrations_" + name + ".json" for name in (
          "easy_dungeon", "easy_mineshaft", "easy_pillager", "easy_pyramid",
          "hard_ancientcity", "hard_endcity", "hard_mansion", "hard_stronghold",
          "medium_jungletemple", "medium_mansion", "medium_pyramid",
          "medium_strongholdcorridor", "medium_strongholdcrossing", "medium_strongholdlibrary",
          "nether_bastion_bridge", "nether_bastion_hoglin_stable", "nether_bastion_other",
          "nether_bastion_treasure", "nether_bridge", "nether_portal", "village_armorer",
          "village_butcher", "village_cartographer", "village_desert_house", "village_fisher",
          "village_fletcher", "village_mason", "village_plains_house", "village_savanna_house",
          "village_sheperd", "village_snowy_house", "village_taiga_house", "village_tannery",
          "village_temple", "village_toolsmith", "village_weaponsmith", "water_buried_treasure",
          "water_ruin_big", "water_ruin_small", "water_shipwreck_map", "water_shipwreck_supply",
          "water_shipwreck_treasure",
      )),
      *("data/lootintegrations/loot_table/chests/" + name + ".json" for name in (
          "easy", "empty", "hard", "medium", "nether", "village", "water"))},
     {"com/lootintegrations/LootintegrationsMod.class"}),
])
def test_complete_small_utility_payload_and_entry_binding(  # noqa: C901, PLR0912, PLR0915
    name: str, count: int, manifest: str, other_files: set[str], entry_classes: set[str],
) -> None:
    directory = Path(f"evidence/item-8/sources/{name}-provider")
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == manifest
    identities = cast("list[dict[str, str]]", json.loads(raw))
    source = next(s for s in retained_sources(Path.cwd()) if s.name == identities[0]["archive"])
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    assert len(identities) == count
    with ZipFile(source.path) as archive:
        names = archive.namelist()
        assert len(names) == len(set(names))
        classes = {r["class"] for r in identities}
        assert len(classes) == count
        assert {n for n in names if not n.endswith("/")} == classes | other_files | {
            "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml",
        }
        # Full explicit accounting excludes nested archives, data packs, templates,
        # extra entry metadata and generation resources. Code roles are inspected
        # in source README files, not inferred from search absence.
        for row in identities:
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
            assert hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest() == (
                row["disassembly_sha256"]
            )
        assert {c for c in classes if b"Lnet/neoforged/fml/common/Mod;" in archive.read(c)} == (
            entry_classes
        )
        subscribers = {
            c for c in classes
            if b"Lnet/neoforged/fml/common/EventBusSubscriber;" in archive.read(c)
        }
        expected: set[str] = entry_classes if name == "attributefix" else set()
        if name == "ai-improvements":
            expected = entry_classes | {
                "com/builtbroken/ai/improvements/modifier/ModifierSystem.class",
            }
        elif name == "almanac":
            expected = {"com/frikinjay/almanac/config/neoforge/AlmanacConfigNeoforge.class"}
        elif name in {"bundle-api", "shield-api"}:
            expected = {c for c in classes if c.endswith("/client/NeoForgeClientMod.class")}
        elif name == "alternate-current":
            expected = {"alternate/current/AlternateCurrentMod$ModEvents.class"}
        elif name == "projectile-library":
            expected = {
                "rbasamoyai/ritchiesprojectilelib/neoforge/RPLNeoForgeClient.class",
                "rbasamoyai/ritchiesprojectilelib/network/neoforge/RPLNetworkImpl.class",
            }
        assert subscribers == expected
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert metadata["modLoader"] == "javafml"
        declarations = cast("list[dict[str, str]]", metadata.get("mixins", []))
        mixin_files = {n for n in other_files if n.endswith(".mixins.json")}
        if name == "projectile-library":
            assert not declarations
            assert archive.read("META-INF/MANIFEST.MF") == b"Manifest-Version: 1.0\r\n\r\n"
        else:
            assert {r["config"] for r in declarations} == mixin_files
        for config in sorted(mixin_files):
            mixin = cast("dict[str, JsonValue]", json.loads(archive.read(config)))
            if name == "structureessentials":
                assert mixin["plugin"] == "com.structureessentials.mixin.MixinConfig"
                assert "com/structureessentials/mixin/MixinConfig.class" in classes
            else:
                assert "plugin" not in mixin
            for side in ("mixins", "client", "server"):
                for member in cast("list[str]", mixin.get(side, [])):
                    path = f"{mixin['package']}.{member}".replace(".", "/") + ".class"
                    assert path in classes
        for service in sorted(n for n in other_files if n.startswith("META-INF/services/")):
            implementation = archive.read(service).decode().strip().replace(".", "/") + ".class"
            assert implementation in classes
        if name == "libraryferret":
            for path in sorted(n for n in other_files if n.startswith("data/")):
                recipe = cast("dict[str, JsonValue]", json.loads(archive.read(path)))
                assert recipe["type"] in {"minecraft:blasting", "minecraft:smelting"}
        if name == "structureessentials":
            raw_config = Path("evidence/item-6/frozen/config/structureessentials.json").read_bytes()
            assert hashlib.sha256(raw_config).hexdigest() == (
                "54826c1ce55156e6a3d19a22949d733668806c7ed4a77218cc1d26bb6c5fa7bd"
            )
            config = cast("dict[str, dict[str, JsonValue]]", json.loads(raw_config))
            assert config["autoBiomeCompat"]["enableBiomeCompat"] is False
            assert config["minimumStructureDistance"]["enabled"] is False
            assert config["spacingSeparationModifier"]["spacingSeparationModifier"] == 1.0
            assert config["disableLegacyRandomCrashes"]["disableLegacyRandomCrashes"] is True


def test_cupboard_and_loot_integrations_frozen_roles() -> None:
    for name, digest, expected in (
        ("cupboard", "937698438af081495eebab187013f66570218e1443f35db8a2ca0b4cb6d9638b", {
            "skipErrorOnEntityLoad": False, "debugChunkloadAttempts": False,
            "logOffthreadEntityAdd": True, "forceHeapDumpOnOOM": False,
        }),
        ("lootintegrations", "898873bac11398a75f7faddeb31410246d43be578868ba58d390b58667b44d31", {
            "skipMapItems": True, "skipExistingItems": False, "moddedItemWeight": 3,
            "showcontainerloottable": False, "debugOutput": False,
        }),
    ):
        raw = Path("evidence/item-6/frozen/config", name + ".json").read_bytes()
        assert hashlib.sha256(raw).hexdigest() == digest
        config = cast("dict[str, dict[str, JsonValue]]", json.loads(raw))
        for key, value in expected.items():
            assert config[key][key] == value
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "lootintegrations-1.21.1-4.7.jar")
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        definitions = {
            n: cast("dict[str, JsonValue]", json.loads(archive.read(n)))
            for n in archive.namelist()
            if n.startswith("data/lootintegrations/loot/") and n.endswith(".json")
        }
        assert len(definitions) == 43
        for definition in definitions.values():
            assert set(definition) == {
                "loot_table", "integrated_loot_tables", "max_result_itemcount",
            }
            assert isinstance(definition["loot_table"], str)
            assert isinstance(definition["integrated_loot_tables"], dict)
        for name, weight in {
            "easy": 1, "empty": 1, "hard": 1, "medium": 5, "nether": 1, "village": 10, "water": 2,
        }.items():
            path = "data/lootintegrations/loot_table/chests/" + name + ".json"
            entry: dict[str, JsonValue] = {"type": "minecraft:empty", "weight": weight}
            if name == "empty":
                entry = {"type": "minecraft:item", "name": "minecraft:bone", "weight": 1}
            assert json.loads(archive.read(path)) == {
                "pools": [{"rolls": 1, "entries": [entry]}],
            }
        assert json.loads(archive.read("data/lootintegrations/tags/item/ignored.json")) == {
            "values": ["minecraft:barrier"],
        }


def test_wunderlib_membership_payload() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "wunderlib-21.0.10.jar")
    assert source.sha256 == "b49c7a040f87ade1e3f73bd7335e8d68ff7a328919c192a6d2c022bae6786a2f"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/wunderlib-provider")
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "a9790a69dcedb09289d08c302863b4503d5979fa64942117e17bfa55adb80c5c")
    rows = cast("list[dict[str, str]]", json.loads(raw))
    entries = {"de/ambertation/wunderlib/WunderLib.class",
               "de/ambertation/wunderlib/WunderLibClient.class"}
    assert {row["class"] for row in rows} == entries | {
        "de/ambertation/wunderlib/math/Bounds.class"}
    with ZipFile(source.path) as archive:
        files = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in files if n.endswith(".class")}
        assert len(classes) == 142
        assert files - classes == {
            "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml",
            "assets/wunderlib/icon.png", "LICENSE_wunderlib",
        }
        assert {n for n in classes if any(marker in archive.read(n) for marker in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;",
        ))} == entries
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert metadata["modLoader"] == "javafml"
        assert not metadata.get("mixins")
        assert archive.read("META-INF/MANIFEST.MF") == b"Manifest-Version: 1.0\r\n\r\n"
        for row in rows:
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert row["class_sha256"] == hashlib.sha256(archive.read(row["class"])).hexdigest()
            assert row["disassembly_sha256"] == hashlib.sha256(
                (directory / row["disassembly"]).read_bytes()).hexdigest()


def test_target_dummy_membership_payload() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "dummmmmmy-1.21-2.0.12-neoforge.jar")
    assert source.sha256 == "4d35c6cdc7a17d6175f116ec8b31ce5ebc740e5d1412ce32cc721b042b2f5298"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/dummy-provider")
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "a8985f1a1ebcf35bdde52c8efdf335ebd6fbd12fc09eb6f42f6ef19e9e44568e")
    rows = cast("list[dict[str, str]]", json.loads(raw))
    prefix = "net/mehvahdjukaar/dummmmmmy/"
    entry = prefix + "neoforge/DummmmmmyForge.class"
    hooks = {"ArmorStandFIxMixin", "EnchantmentMixin", "LivingEntityMixin",
             "PlayerMixin", "SwordItemMixin", "ToolItemMixin"}
    assert {r["class"] for r in rows} == {entry} | {
        prefix + "mixins/" + name + ".class" for name in hooks
    } | {prefix + name + ".class" for name in (
        "Dummmmmmy", "Dummmmmmy$SpawnDummyBehavior", "common/ModEvents", "common/TargetDummyItem")}
    with ZipFile(source.path) as archive:
        files = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in files if n.endswith(".class")}
        assert len(classes) == 45
        content = {n for n in files if n.startswith(("data/", "assets/"))}
        categories = {"assets/dummmmmmy/lang": 14, "assets/dummmmmmy/textures": 10,
                      "assets/dummmmmmy/particles": 2, "assets/dummmmmmy/models": 1,
                      "assets/dummmmmmy/sounds.json": 1, "data/dummmmmmy/tags": 9,
                      "data/dummmmmmy/damage_type": 2, "data/minecraft/tags": 2,
                      "data/dummmmmmy/advancements": 1, "data/dummmmmmy/recipe": 1}
        observed = ["/".join(n.split("/")[:3]) for n in content]
        assert {key: observed.count(key) for key in set(observed)} == categories
        assert all(n.endswith((".json", ".png")) for n in content)
        assert files - classes - content == {
            "META-INF/MANIFEST.MF", "META-INF/accesstransformer.cfg",
            "META-INF/neoforge.mods.toml", "dummmmmmy-common-refmap.json",
            "dummmmmmy-common.mixins.json", "dummmmmmy.mixins.json", "icon.png", "pack.mcmeta"}
        assert archive.read("META-INF/MANIFEST.MF") == b"Manifest-Version: 1.0\r\n\r\n"
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert metadata["modLoader"] == "javafml"
        declarations = cast("list[dict[str, str]]", metadata["mixins"])
        assert {r["config"] for r in declarations} == {
            "dummmmmmy-common.mixins.json", "dummmmmmy.mixins.json"}
        for filename in ("dummmmmmy-common.mixins.json", "dummmmmmy.mixins.json"):
            config = cast("dict[str, JsonValue]", json.loads(archive.read(filename)))
            assert set(cast("list[str]", config["mixins"])) == (
                hooks if filename == "dummmmmmy-common.mixins.json" else set())
            assert not any(config.get(k) for k in ("plugin", "server", "client"))
        assert {n for n in classes if any(marker in archive.read(n) for marker in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;",
        ))} == {entry}
        for row in rows:
            assert row["archive"] == source.name
            assert row["archive_sha256"] == source.sha256
            assert row["class_sha256"] == hashlib.sha256(archive.read(row["class"])).hexdigest()
            assert row["disassembly_sha256"] == hashlib.sha256(
                (directory / row["disassembly"]).read_bytes()).hexdigest()
