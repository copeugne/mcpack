from __future__ import annotations

import gzip
import hashlib
import json
import tomllib
from collections import Counter
from io import BytesIO
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_inventory import resource_identity
from mcpack_evidence.item8_resource_selection import runtime_mod_ids
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
    assert resources[prefix + "placed_feature/cave_urns.json"]["feature"] == (
        "supplementaries:urns_patch"
    )
    urn_patch = resources[prefix + "configured_feature/urns_patch.json"]
    assert urn_patch["type"] == "minecraft:random_patch"
    patch_config = cast("dict[str, JsonValue]", urn_patch["config"])
    feature = cast("dict[str, JsonValue]", patch_config["feature"])
    assert feature["feature"] == {
        "type": "minecraft:simple_block", "config": {"to_place": {
            "type": "minecraft:simple_state_provider", "state": {
                "Name": "supplementaries:urn",
                "Properties": {"treasure": "true", "waterlogged": "false"},
            },
        }},
    }
    modifier_prefix = "data/supplementaries/neoforge/biome_modifier/"
    assert {
        path.removeprefix(modifier_prefix): row["features"]
        for path, row in resources.items() if path.startswith(modifier_prefix)
    } == {
        "basalt_ash.json": "supplementaries:basalt_ash",
        "cave_urns.json": "supplementaries:cave_urns",
        "ocean_barnacles.json": "supplementaries:ocean_barnacles",
        "shore_barnacles.json": "supplementaries:shore_barnacles",
        "wild_flax.json": "supplementaries:wild_flax",
    }


def test_supplementaries_generation_sources_and_elevator_inputs() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("supplementaries-"))
    directory = Path("evidence/item-8/sources/supplementaries-generation")
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "0eb64c666c0db4bd45091038bb2b3d622a1e57f896d31fe0df1279f2ff357e5d"
    )
    identities = cast("list[dict[str, str]]", json.loads(raw))
    assert len(identities) == len({row["class"] for row in identities}) == 11
    callback_directory = Path("evidence/item-8/sources/supplementaries-road-sign-callback")
    raw = (callback_directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "a6a99e646dd7b65793defda3168306b20e1a70a901b7d37e024d4aea3f6f5194"
    )
    callback = cast("list[dict[str, str]]", json.loads(raw))
    assert len(callback) == 1
    placement_directory = Path("evidence/item-8/sources/supplementaries-placement-processor")
    raw = (placement_directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "aaae4d5157a42bdff7bc12d048945a324e3c0c45d8e0bf06edf46a06a7264195"
    )
    placement = cast("list[dict[str, str]]", json.loads(raw))
    assert len(placement) == len({row["class"] for row in placement}) == 3
    entry_directory = Path("evidence/item-8/sources/supplementaries-common-entries")
    raw = (entry_directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "7d0fe813b6039a677168e347e9c9d73c4af2aae8d9b2728cab6e9b9783ac2e74"
    )
    entries = cast("list[dict[str, str]]", json.loads(raw))
    assert len(entries) == len({row["class"] for row in entries}) == 7
    setup_captures: list[tuple[Path, list[dict[str, str]]]] = []
    for name, count, expected_sha in (
        ("supplementaries-setup", 1,
         "cbab9d898accfb9bedc9ab98c56e9b85f08747a062353dd8350d5699dbfad049"),
        ("supplementaries-setup-delegates", 2,
         "3a14ffe0a11a67a2cb31b7825dce2fe1bdef83b644754f89816a63558144b58a"),
        ("supplementaries-integrations", 8,
         "1ec5f3694856a3a56bf280d1ceb4bf980a741f63fe7ad1fddba78ea6c7d2b1d3"),
        ("supplementaries-client-entries", 2,
         "b0e1d475ee276f5923a241dcc90190b1c369119fd784f0963ffe67c65cd623c9"),
    ):
        capture_directory = Path("evidence/item-8/sources") / name
        raw = (capture_directory / "identities.json").read_bytes()
        assert hashlib.sha256(raw).hexdigest() == expected_sha
        rows = cast("list[dict[str, str]]", json.loads(raw))
        assert len(rows) == len({row["class"] for row in rows}) == count
        setup_captures.append((capture_directory, rows))
    with ZipFile(source.path) as archive:
        mixins = cast(
            "dict[str, JsonValue]", json.loads(archive.read("supplementaries-common.mixins.json"))
        )
        assert mixins["package"] == "net.mehvahdjukaar.supplementaries.mixins"
        assert {
            "MineshaftCorridorMixin", "MineshaftPiecesMixin",
            "StrongholdCrossingSconceMixin", "StrongholdRoomSconceMixin",
        } <= set(
            cast("list[str]", mixins["mixins"])
        )
        for capture_directory, rows in (
            (directory, identities),
            (callback_directory, callback),
            (placement_directory, placement),
            (entry_directory, entries),
            *setup_captures,
        ):
            for row in rows:
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
                raw = (capture_directory / row["disassembly"]).read_bytes()
                assert hashlib.sha256(raw).hexdigest() == row["disassembly_sha256"]
    raw = Path("evidence/item-6/frozen/config/supplementaries-common.toml").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "14210291891759b831951eba24c65985ed5bd27a7d09b6383aeb9fd3e8f1bc8c"
    )
    config = cast("dict[str, dict[str, dict[str, JsonValue]]]", tomllib.loads(raw.decode()))
    assert config["redstone"]["pulley_block"] == {"enabled": True, "mineshaft_elevator": 0.035}
    assert config["redstone"]["turn_table"]["enabled"] is True
    assert config["functional"]["rope"]["enabled"] is True
    assert config["building"]["sconce"]["enabled"] is True
    log = Path("evidence/raw/item8/registry-r1/debug.log").read_bytes()
    assert hashlib.sha256(log).hexdigest() == (
        "e5b47378d791027242ba28dd36c999c07ae4e01a1b90e1534e66bcd42c1e694b"
    )
    mods = set(runtime_mod_ids(log.decode()))
    assert {"create", "computercraft", "farmersdelight", "quark", "curios"} <= mods
    assert not mods & {
        "soul_fire_d", "shulkerboxtooltip", "decorative_blocks", "endergetic",
        "caverns_and_chasms", "infernalexp", "architects_palette", "trinkets",
    }


def test_supplementaries_bundled_companion_service() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("supplementaries-"))
    assert source.sha256 == "0dd0445af35aa15ad012833c4b8024d2ed70320d1ace0316d2f5b684b06a997d"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    nested_path = "META-INF/jarjar/sable-companion-common-1.21.1-1.6.0.jar"
    nested_sha = "873633e35046e3761b277ff8a1ecad0d55d9a3014fa81a0b084c9aecba1f3bed"
    directory = Path("evidence/item-8/sources/supplementaries-sable-companion")
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "0e58be3a4ae7cc39891a83c05fd25707e7dafc44831648596ee5ea64dafef660"
    )
    identities = cast("list[dict[str, str]]", json.loads(raw))
    assert len(identities) == len({row["class"] for row in identities}) == 4
    with ZipFile(source.path) as parent:
        raw = parent.read(nested_path)
    assert hashlib.sha256(raw).hexdigest() == nested_sha
    with ZipFile(BytesIO(raw)) as nested:
        names = {n for n in nested.namelist() if not n.endswith("/")}
        classes = {n for n in names if n.endswith(".class")}
        assert len(names) == 19
        assert len(classes) == 14
        service = "META-INF/services/dev.ryanhcode.sable.companion.SableCompanion"
        assert names - classes == {
            "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml",
            "sablecompanion.png", "LICENSE", service,
        }
        assert nested.read(service).decode().strip() == (
            "dev.ryanhcode.sable.companion.impl.DefaultSableCompanion"
        )
        for row in identities:
            assert row["archive"] == source.name + "!/" + nested_path
            assert row["archive_sha256"] == nested_sha
            assert hashlib.sha256(nested.read(row["class"])).hexdigest() == row["class_sha256"]
            raw = (directory / row["disassembly"]).read_bytes()
            assert hashlib.sha256(raw).hexdigest() == row["disassembly_sha256"]


def test_supplementaries_trinkets_class_fallback_is_absent() -> None:
    target = "dev/emi/trinkets/api/TrinketsApi.class"
    for source in retained_sources(Path.cwd()):
        payload = source.path.read_bytes()
        assert hashlib.sha256(payload).hexdigest() == source.sha256
        pending = [(source.name, payload)]
        while pending:
            location, payload = pending.pop()
            with ZipFile(BytesIO(payload)) as archive:
                names = archive.namelist()
                assert not any(n == target or n.endswith("/" + target) for n in names), location
                pending.extend(
                    (location + "!/" + name, archive.read(name))
                    for name in names if name.endswith(".jar")
                )


def test_supplementaries_mixinsquared_library_entries() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("supplementaries-"))
    assert source.sha256 == "0dd0445af35aa15ad012833c4b8024d2ed70320d1ace0316d2f5b684b06a997d"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    outer_path = "META-INF/jarjar/mixinsquared-forge-0.3.3.jar"
    inner_path = "META-INF/jars/MixinSquared-0.3.3.jar"
    with ZipFile(source.path) as parent:
        wrapper_raw = parent.read(outer_path)
    with ZipFile(BytesIO(wrapper_raw)) as wrapper:
        core_raw = wrapper.read(inner_path)
        plugin = cast(
            "dict[str, JsonValue]", json.loads(wrapper.read("mixinsquared.init.mixins.json"))
        )
        assert plugin["plugin"] == (
            "com.bawnorton.mixinsquared.platform.forge.MixinSquaredMixinConfigPlugin"
        )
        assert not {"mixins", "client", "server"} & plugin.keys()
    for label, payload, member, count, archive_sha, manifest_sha in (
        ("wrapper", wrapper_raw, outer_path, 11,
         "e5f1afc19c38005b03615d7c3af65df6b9150cb25150ac5267b587a116f425e3",
         "6a7cbdcfb28d23625a5a4468a982f9d5011767bc226793639d02532001fc47c2"),
        ("core", core_raw, outer_path + "!/" + inner_path, 63,
         "0eaa67fa937cc65ab78a981cd9e4e741d03eaf7236983d7e30818ac99da0632f",
         "a46ec939d8f5fba8cbb02ca91e76e87d25d830ebc7be3711056659e04a14d673"),
    ):
        assert hashlib.sha256(payload).hexdigest() == archive_sha
        directory = Path("evidence/item-8/sources/supplementaries-mixinsquared-" + label)
        raw = (directory / "identities.json").read_bytes()
        assert hashlib.sha256(raw).hexdigest() == manifest_sha
        rows = cast("list[dict[str, str]]", json.loads(raw))
        assert len(rows) == len({row["class"] for row in rows}) == 4
        with ZipFile(BytesIO(payload)) as archive:
            names = {n for n in archive.namelist() if not n.endswith("/")}
            assert len(names) == count
            assert not any(n.startswith(("data/", "assets/")) for n in names)
            for row in rows:
                assert row["archive"] == source.name + "!/" + member
                assert row["archive_sha256"] == archive_sha
                assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
                raw = (directory / row["disassembly"]).read_bytes()
                assert hashlib.sha256(raw).hexdigest() == row["disassembly_sha256"]


def test_supplementaries_complete_parent_payload_partition() -> None:
    source = next(s for s in retained_sources(Path.cwd()) if s.name.startswith("supplementaries-"))
    assert source.sha256 == "0dd0445af35aa15ad012833c4b8024d2ed70320d1ace0316d2f5b684b06a997d"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        names = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in names if n.endswith(".class")}
        assets = {n for n in names if n.startswith("assets/")}
        data = {n for n in names if n.startswith("data/")}
        other = names - classes - assets - data
        assert len(names) == 6364
        assert (len(classes), len(assets), len(data), len(other)) == (1179, 3577, 1589, 19)
        assert len(names) == len(classes) + len(assets) + len(data) + len(other)
        assert Counter(n.split("/")[2] for n in data) == {
            "advancement": 322, "banner_pattern": 1, "catchable_mobs_properties": 102,
            "curios": 1, "damage_type": 7, "data_maps": 3, "enchantment": 1, "entities": 2,
            "flute_songs": 31, "hourglass_dusts": 12, "jukebox_song": 2, "loot_modifiers": 6,
            "loot_table": 221, "moonlight": 164, "neoforge": 5, "painting_variant": 2,
            "recipe": 308, "recipes": 5, "slots": 2, "structure": 18, "supplementaries": 6,
            "tags": 327, "trim_pattern": 1, "unused_songs": 10, "weapon_attributes": 1,
            "worldgen": 29,
        }
        assert Counter(n.split("/")[3] for n in data if n.split("/")[2] == "moonlight") == {
            "soft_fluid": 109, "map_marker": 34, "villager_trade": 21,
        }
        assert {n for n in data if not n.endswith((".json", ".nbt"))} == {
            "data/minecraft/moonlight/villager_trade/cartographer/example.json.disabled",
            "data/supplementaries/flute_songs/midi_converter.py",
            "data/supplementaries/flute_songs/revenge.json1",
        }
        pack = "resourcepacks/darker_ropes/"
        assert {n.removeprefix(pack) for n in other if n.startswith(pack)} == {
            "pack.mcmeta", "pack.png", "assets/supplementaries/textures/block/pulley_side_rope.png",
            "assets/supplementaries/textures/block/rope.png",
            "assets/supplementaries/textures/block/rope_knot_10.png",
            "assets/supplementaries/textures/block/rope_knot_6.png",
            "assets/supplementaries/textures/block/rope_knot_8.png",
            "assets/supplementaries/textures/item/rope.png",
            "assets/supplementaries/textures/item/rope_arrow.png",
        }
        assert {n for n in other if not n.startswith(pack)} == {
            "META-INF/MANIFEST.MF", "META-INF/accesstransformer.cfg",
            "META-INF/neoforge.mods.toml", "META-INF/jarjar/metadata.json",
            "META-INF/jarjar/mixinsquared-forge-0.3.3.jar",
            "META-INF/jarjar/sable-companion-common-1.21.1-1.6.0.jar",
            "supplementaries-common.mixins.json", "supplementaries.mixins.json",
            "icon.png", "LICENSE_Supplementaries.md",
        }
        assert {
            n for n in classes if any(marker in archive.read(n) for marker in (
                b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;",
            ))
        } == {
            "net/mehvahdjukaar/supplementaries/platform/SupplementariesForge.class",
            "net/mehvahdjukaar/supplementaries/platform/SupplementariesForgeClient.class",
            "net/mehvahdjukaar/supplementaries/client/renderers/platform/PicklePlayer.class",
        }
