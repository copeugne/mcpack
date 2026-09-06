from __future__ import annotations

import hashlib
import json
from collections import Counter
from io import BytesIO
from pathlib import Path
from typing import cast
from zipfile import ZipFile

import pytest

from mcpack_evidence.item8_sources import retained_sources


def test_fabric_packaged_data_and_modifier_source() -> None:
    source = next(
        s
        for s in retained_sources(Path.cwd())
        if s.name == "forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar"
    )
    assert source.sha256 == "68abf2864e957df26ac0cc3bd5352ee67880e052b47a80f22f28556c1179f18d"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    directory = Path("evidence/item-8/sources/fabric-biome-modifier")
    raw = (directory / "identities.json").read_bytes()
    assert (
        hashlib.sha256(raw).hexdigest()
        == "5c927be105ad9117e051c9263e5b1e4ba39978bd1a423f1a9887afb35150f83f"
    )
    rows = cast("list[dict[str, str]]", json.loads(raw))
    assert len(rows) == 5
    biome_member = "META-INF/jars/fabric-biome-api-v1-13.0.31+1e62d33c19.jar"
    with ZipFile(source.path) as parent:
        names = {n for n in parent.namelist() if not n.endswith("/")}
        jars = {n for n in names if n.endswith(".jar")}
        assert len(jars) == 43
        queue = (
            Path("evidence/item-8/provider-scope.md")
            .read_text()
            .split("### Exact Fabric module queue\n", 1)[1]
        )
        queue_names = [
            line.split("`", 2)[1] for line in queue.splitlines() if line.startswith("| `")
        ]
        assert len(queue_names) == len(set(queue_names)) == 43
        assert set(queue_names) == {member.rsplit("/", 1)[1] for member in jars}
        assert names - jars == {
            "META-INF/MANIFEST.MF",
            "META-INF/neoforge.mods.toml",
            "fabric.mod.json.old",
            "assets/fabric/icon.png",
            "META-INF/jarjar/metadata.json",
        }
        data_counts: Counter[str] = Counter()
        for member in sorted(jars):
            payload = parent.read(member)
            with ZipFile(BytesIO(payload)) as archive:
                files = {n for n in archive.namelist() if not n.endswith("/")}
                if "fabric-transitive-access-wideners-v1-" in member:
                    assert files == {
                        "META-INF/MANIFEST.MF",
                        "META-INF/neoforge.mods.toml",
                        "META-INF/accesstransformer.cfg",
                        "META-INF/architectury-loom-nesting-metadata.json",
                        "assets/fabric-transitive-access-wideners-v1/icon.png",
                    }
                    assert b'modLoader = "lowcodefml"' in archive.read(
                        "META-INF/neoforge.mods.toml"
                    )
                assert not any(n.endswith((".jar", ".nbt")) for n in files)
                data = {n for n in files if n.startswith("data/")}
                if data:
                    data_counts[member] = len(data)
                if member == biome_member:
                    assert data == {
                        "data/fabric_biome_api_v1/neoforge/biome_modifier/fabric_biome_modifier_instance.json"
                    }
                    assert json.loads(archive.read(next(iter(data)))) == {
                        "type": "fabric_biome_api_v1:fabric_biome_modifier"
                    }
                    for row in rows:
                        assert row["archive"] == source.name + "!/" + member
                        assert row["archive_sha256"] == hashlib.sha256(payload).hexdigest()
                        assert (
                            row["class_sha256"]
                            == hashlib.sha256(archive.read(row["class"])).hexdigest()
                        )
                        assert (
                            row["disassembly_sha256"]
                            == hashlib.sha256(
                                (directory / row["disassembly"]).read_bytes()
                            ).hexdigest()
                        )
                elif "fabric-convention-tags-v2-" in member:
                    assert all(n.split("/")[2] == "tags" for n in data)
                elif "fabric-gametest-api-v1-" in member:
                    assert data == {"data/fabric-gametest-api-v1/gametest/structure/empty.snbt"}
        assert data_counts == {
            biome_member: 1,
            "META-INF/jars/fabric-convention-tags-v2-2.11.1+87e5848019.jar": 491,
            "META-INF/jars/fabric-gametest-api-v1-2.0.5+29f188ce19.jar": 1,
        }


@pytest.mark.parametrize(
    ("module", "label", "digest", "count", "consumers"),
    [
        (
            "fabric-events-interaction-v0-0.7.13+86e0887119",
            "fabric-events-interaction-v0-entry",
            "614f8f550bebcc2f4247a0be3905dbafc49647536eb93c547efac92c4f26bbd3",
            2,
            {"org/sinytra/fabric/events_interaction/generated/GeneratedEntryPoint.class",
             "net/fabricmc/fabric/impl/event/interaction/InteractionEventHooks.class"},
        ),
        (
            "fabric-item-api-v1-11.2.0+0c57911319",
            "fabric-item-api-v1-entry",
            "079c11a09085ddb9668c75ede629e2222a0485498ba7f8bb896c28a4cf3ece8a",
            13,
            {"org/sinytra/fabric/item_api/generated/GeneratedEntryPoint.class",
             "net/fabricmc/fabric/impl/item/DefaultItemComponentImpl.class",
             "net/fabricmc/fabric/impl/client/item/ClientItemEventHooks.class"},
        ),
        (
            "fabric-object-builder-api-v1-15.2.1+cc242efd19",
            "fabric-object-builder-api-v1-entry",
            "d7a0bf493eb787b68c5ec8df4170657dbd74f1686d1a6b4fa58b22059570e393",
            11,
            {"org/sinytra/fabric/object_builder_api/generated/GeneratedEntryPoint.class"},
        ),
        (
            "fabric-resource-conditions-api-v1-4.3.0+5bdd099819",
            "fabric-resource-conditions-api-v1-entry",
            "1b89585428466581c618936da06eef4e7dc4684c64a150080ccf2ba02dda9c21",
            10,
            {"org/sinytra/fabric/resource_conditions_api/generated/GeneratedEntryPoint.class"},
        ),
        (
            "fabric-message-api-v1-6.0.14+6a754fce19",
            "fabric-message-api-v1-entry",
            "9222255dfc0fe5fdf7b15eab08a4d6c45db376e76a6299bcc4629a08ca9a7f96",
            2,
            {"org/sinytra/fabric/message_api/generated/GeneratedEntryPoint.class"},
        ),
        (
            "fabric-screen-handler-api-v1-1.3.90+8dbc56dd19",
            "fabric-screen-handler-api-v1-entry",
            "9bf373c6282c1559ecaa14733d3b04568f1d5460e4131b7fb0c84b23601f9eb0",
            2,
            {"org/sinytra/fabric/screen_handler_api/generated/GeneratedEntryPoint.class"},
        ),
        (
            "fabric-data-attachment-api-v1-1.4.5+26d408aa19",
            "fabric-data-attachment-entry",
            "bee13b060b3c64abbb8d20e4da62404f7b4d1ee1d2e12b21e7dce2bd490daf9d",
            4,
            {"org/sinytra/fabric/data_attachment_api/generated/GeneratedEntryPoint.class",
             "net/fabricmc/fabric/impl/attachment/AttachmentModImpl.class"},
        ),
        (
            "fabric-content-registries-v0-8.0.19+5e0d320019",
            "fabric-content-registries-entry",
            "9f1c23a98141bc5449ee93e4f103ba67a7d15f5e333ab85a56712e27661d20d0",
            13,
            {"org/sinytra/fabric/content_registries/generated/GeneratedEntryPoint.class",
             "net/fabricmc/fabric/api/registry/TillableBlockRegistry.class",
             "net/fabricmc/fabric/impl/content/registry/FuelRegistryImpl.class"},
        ),
        (
            "fabric-data-generation-api-v1-20.2.34+a4c3605619",
            "fabric-data-generation-entry",
            "005d5198b431bd5f83257d280cead53e562acb126ce11f94285bc0dcf397022d",
            10,
            {"org/sinytra/fabric/data_generation_api/generated/GeneratedEntryPoint.class"},
        ),
        (
            "fabric-item-group-api-v1-4.1.7+e324903319",
            "fabric-item-group-entry",
            "b7ad297470f753293f94ea1519ca76b23e352c0952946b6452d43a52410cd5d3",
            1,
            {"org/sinytra/fabric/item_group_api/generated/GeneratedEntryPoint.class"},
        ),
        (
            "fabric-command-api-v2-2.2.28+36d727be19",
            "fabric-command-entry",
            "2905c60a6b616efc27154aa9fb5cf2768184f535238df1cbaf8d406d1a72a3f5",
            1,
            {"org/sinytra/fabric/command_api/generated/GeneratedEntryPoint.class"},
        ),
        (
            "fabric-lifecycle-events-v1-2.6.0+e40d8add19",
            "fabric-lifecycle-entry",
            "81ff99421170db72fbeeb1e0bb07befbddf71c8dae57b6a037860883a83409b6",
            7,
            {"org/sinytra/fabric/lifecycle_events/generated/GeneratedEntryPoint.class"},
        ),
        (
            "fabric-entity-events-v1-1.8.0+5ede667619",
            "fabric-entity-events-entry",
            "f856b1bc1999cd9d480f5d8142b5561d05e62796bc6febf77d22588847531798",
            9,
            {"org/sinytra/fabric/entity_events/generated/GeneratedEntryPoint.class",
             "net/fabricmc/fabric/impl/entity/event/EntityEventHooks.class"},
        ),
        (
            "fabric-game-rule-api-v1-1.0.53+36d727be19",
            "fabric-game_rule_api-entry",
            "e4413cde1f7946aaabaedd73db4fcbe27ab5c7285cb3eb9d2017071e2ca7702d",
            5,
            {"org/sinytra/fabric/game_rule_api/generated/GeneratedEntryPoint.class"},
        ),
        (
            "fabric-loot-api-v2-3.0.15+a3ee712d19",
            "fabric-loot_api_v2-entry",
            "39948838d282ea95917661b003571449b503449615810c9e78d61eb0ca95ed67",
            2,
            {"org/sinytra/fabric/loot_api_v2/generated/GeneratedEntryPoint.class"},
        ),
        (
            "fabric-loot-api-v3-1.0.3+333dfad919",
            "fabric-loot_api-entry",
            "651e7b5dc634205e9dd736041958177205b0ebf3b5e0ff97991d7ed1ff6a7371",
            6,
            {"org/sinytra/fabric/loot_api/generated/GeneratedEntryPoint.class"},
        ),
        (
            "fabric-recipe-api-v1-5.0.15+59440bcc19",
            "fabric-recipe_api-entry",
            "1778fbf2dcb132483978c5333401a7b5dcd77cc4bc6879ce057d1a05a0c96ab5",
            2,
            {"org/sinytra/fabric/recipe_api/generated/GeneratedEntryPoint.class"},
        ),
        (
            "fabric-api-lookup-api-v1-1.6.71+c290471319",
            "fabric-api_lookup_api-entry",
            "7fdd492bfcaf9f4d3840f9c7d238f2a2db88d94979b29a84f4592ae3d5aae0c9",
            1,
            {"org/sinytra/fabric/api_lookup_api/generated/GeneratedEntryPoint.class"},
        ),
        (
            "fabric-block-api-v1-1.1.0+b0c22bb819",
            "fabric-block_api-entry",
            "3378c30e4764b45310fd52494bfb1d88ad4f8e7ff250e7a58232388d4c7f705d",
            3,
            {"org/sinytra/fabric/block_api/generated/GeneratedEntryPoint.class"},
        ),
        (
            "fabric-block-view-api-v2-1.0.11+e9036fd419",
            "fabric-block_view_api-entry",
            "24fb28fc00e6da4260ca6a0aec22aa5520f73b3a20b0c441eb8956c236ca3ca4",
            3,
            {"org/sinytra/fabric/block_view_api/generated/GeneratedEntryPoint.class"},
        ),
        (
            "fabric-rendering-data-attachment-v1-0.3.49+73761d2e19",
            "fabric-rendering_data_attachment_v1-entry",
            "1563f045f7690ab90e53d9e9ae5e126d657b09fece385ba2414a03f08c6eadd4",
            2,
            {"org/sinytra/fabric/rendering_data_attachment_v1/generated/GeneratedEntryPoint.class"},
        ),
        (
            "fabric-resource-loader-v0-1.3.1+4ea8954419",
            "fabric-resource-loading",
            "4030af446b6db49bce752d0d87cc98fb1e937c611c7a483b8fd8fe9dc199d57f",
            13,
            {
                "net/fabricmc/fabric/impl/resource/loader/ResourceManagerHelperImpl.class",
                "org/sinytra/fabric/resource_loader/generated/GeneratedEntryPoint.class",
            },
        ),
        (
            "fabric-biome-api-v1-13.0.31+1e62d33c19",
            "fabric-biome-selection",
            "de014a8e4cb7983f0b7dee3f690487f1d7a0fe016dea4855f91d42202331cd73",
            6,
            {
                "net/fabricmc/fabric/impl/biome/NetherBiomeData.class",
                "net/fabricmc/fabric/impl/biome/TheEndBiomeData.class",
            },
        ),
        (
            "fabric-gametest-api-v1-2.0.5+29f188ce19",
            "fabric-gametest-consumers",
            "3013cd1a423391736354782d30a6614077c99583ca0afd0be07b432b45d27a71",
            5,
            {
                "net/fabricmc/fabric/impl/gametest/FabricGameTestModInitializer.class",
                "org/sinytra/fabric/gametest_api/generated/GeneratedEntryPoint.class",
                "org/sinytra/fabric/gametest_api_v1/FabricGameTestApiV1.class",
            },
        ),
    ],
)
def test_fabric_sources_cover_declared_mixins(  # noqa: PLR0915 - explicit source and payload bindings.
    module: str, label: str, digest: str, count: int, consumers: set[str]
) -> None:
    source = next(
        s
        for s in retained_sources(Path.cwd())
        if s.name == "forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar"
    )
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    member = f"META-INF/jars/{module}.jar"
    directory = Path("evidence/item-8/sources") / label
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == digest
    rows = cast("list[dict[str, str]]", json.loads(raw))
    with ZipFile(source.path) as parent:
        payload = parent.read(member)
        with ZipFile(BytesIO(payload)) as archive:
            config = cast(
                "dict[str, object]",
                json.loads(archive.read(module.rsplit("-", 1)[0].replace(
                    "fabric-object-builder-api-v1", "fabric-object-builder-v1") + ".mixins.json")),
            )
            prefix = cast("str", config["package"]).replace(".", "/") + "/"
            declared = {prefix + name.replace(".", "/") + ".class"
                        for name in cast("list[str]", config["mixins"])}
            server = cast("list[str]", config.get("server", []))
            assert server == (["server.WorldChunkMixin"]
                              if module.startswith("fabric-lifecycle-events-v1-") else [])
            declared.update(prefix + item.replace(".", "/") + ".class" for item in server)
            assert len(declared) == count
            assert not config.get("plugin")
            assert {r["class"] for r in rows} == declared | consumers
            name = module.rsplit("-", 1)[0]
            if name == "fabric-api-lookup-api-v1":
                for capture, identity, target in (
                    ("fabric-lookup-init",
                     "feb6c7996b8b362e2aacc07549301ad0e44c23c02b6e9a4a79ee5f1f08b904be",
                     "ApiLookupImpl"),
                    ("fabric-lookup-entity-check",
                     "fea7a06fabe1eea4364d75c4cbc4c7d272033a5af585f44296fa5d1aeebfbd60",
                     "entity/EntityApiLookupImpl"),
                ):
                    extra_dir = Path("evidence/item-8/sources") / capture
                    extra_raw = (extra_dir / "identities.json").read_bytes()
                    assert hashlib.sha256(extra_raw).hexdigest() == identity
                    extra_rows = cast("list[dict[str, str]]", json.loads(extra_raw))
                    assert len(extra_rows) == 1
                    extra = extra_rows[0]
                    assert extra["class"] == "net/fabricmc/fabric/impl/lookup/" + target + ".class"
                    assert extra["archive"] == source.name + "!/" + member
                    assert extra["archive_sha256"] == hashlib.sha256(payload).hexdigest()
                    assert extra["class_sha256"] == hashlib.sha256(
                        archive.read(extra["class"])).hexdigest()
                    assert extra["disassembly_sha256"] == hashlib.sha256(
                        (extra_dir / extra["disassembly"]).read_bytes()).hexdigest()
            initializer_sources = {
                "fabric-events-interaction-v0": [(
                    "fabric-interaction-router",
                    "1f6918e1d747541523585d23f29310ceb4a298516a221e80e05251cfa02d41e3",
                    {"net/fabricmc/fabric/impl/event/interaction/InteractionEventsRouter.class"},
                )],
                "fabric-item-api-v1": [(
                    "fabric-item-enchantment",
                    "d653028574d440be486250233dd9364855a141a5da678dbc6f3ff23338104e31",
                    {"net/fabricmc/fabric/impl/item/EnchantmentUtil.class"},
                )],
                "fabric-resource-conditions-api-v1": [(
                    "fabric-resource-condition-delegates",
                    "e6103740fe144f96a30b6d57d87bc672b35fffa3b9553f52b2a4cb4188bb6697",
                    {"net/fabricmc/fabric/impl/resource/conditions/ResourceConditionsImpl.class",
                     "net/fabricmc/fabric/impl/resource/conditions/OverlayConditionsMetadata.class"},
                )],
                "fabric-data-attachment-api-v1": [(
                    "fabric-attachment-registration",
                    "e5d85879d444086c19fa15921336c7e711185d212564b35501e8bc8eb58dda67",
                    {"net/fabricmc/fabric/impl/attachment/AttachmentModImpl.class",
                     "net/fabricmc/fabric/impl/attachment/AttachmentRegistryImpl.class"},
                ), (
                    "fabric-attachment-init",
                    "9add3414f670243af4701ec42e118c410479a35c8064e2691745ad0bc2dcc7e4",
                    {"net/fabricmc/fabric/impl/attachment/AttachmentEntrypoint.class"},
                )],
                "fabric-content-registries-v0": [(
                    "fabric-content-data-map",
                    "ba7fcec72be79425015cea676ff60b645990ed84d277c9b237358cd1fa8fa9df",
                    {"net/fabricmc/fabric/impl/content/registry/DataMapModifications.class"},
                )],
                "fabric-command-api-v2": [(
                    "fabric-command-init",
                    "54cc77ba015cd890542609a6a8a98742763b3bde85eef35c857ad253445205a4",
                    {"org/sinytra/fabric/command_api/FabricCommandApiV2.class"},
                )],
                "fabric-lifecycle-events-v1": [(
                    "fabric-lifecycle-init",
                    "1abb7ebad9fe2aee3ce06b5d23c59aec1beb4509d798793e9717f66f324826fe",
                    {"net/fabricmc/fabric/impl/event/lifecycle/LifecycleEventsImpl.class"},
                )],
                "fabric-loot-api-v2": [(
                    "fabric-loot-v2-init",
                    "fdd70793358e39363a47a89dea1e357a60bbc26f051d182c66c7fd97c7be0d6e",
                    {"net/fabricmc/fabric/impl/loot/v2/LootInitializer.class"},
                )],
                "fabric-recipe-api-v1": [(
                    "fabric-recipe-init",
                    "284be5d480faf7950a489a9134fa4db894a3ed59174e3e3c28b07dcb4c2c98ae",
                    {"net/fabricmc/fabric/impl/recipe/ingredient/CustomIngredientInit.class",
                     "org/sinytra/fabric/recipe_api/FabricRecipeApiV1.class"},
                )],
            }
            for capture, identity, expected_classes in initializer_sources.get(name, []):
                extra_dir = Path("evidence/item-8/sources") / capture
                extra_raw = (extra_dir / "identities.json").read_bytes()
                assert hashlib.sha256(extra_raw).hexdigest() == identity
                extra_rows = cast("list[dict[str, str]]", json.loads(extra_raw))
                assert {r["class"] for r in extra_rows} == expected_classes
                for row in extra_rows:
                    assert row["archive"] == source.name + "!/" + member
                    assert row["archive_sha256"] == hashlib.sha256(payload).hexdigest()
                    assert row["class_sha256"] == hashlib.sha256(
                        archive.read(row["class"])).hexdigest()
                    assert row["disassembly_sha256"] == hashlib.sha256(
                        (extra_dir / row["disassembly"]).read_bytes()).hexdigest()
            block_modules = {
                "fabric-events-interaction-v0": (36, 3),
                "fabric-item-api-v1": (43, 1),
                "fabric-object-builder-api-v1": (44, 0),
                "fabric-resource-conditions-api-v1": (31, 0),
                "fabric-message-api-v1": (32, 2),
                "fabric-screen-handler-api-v1": (9, 0),
                "fabric-data-attachment-api-v1": (20, 1),
                "fabric-content-registries-v0": (39, 0),
                "fabric-data-generation-api-v1": (53, 0),
                "fabric-item-group-api-v1": (15, 1),
                "fabric-command-api-v2": (16, 1),
                "fabric-lifecycle-events-v1": (73, 5),
                "fabric-entity-events-v1": (47, 0),
                "fabric-game-rule-api-v1": (27, 3),
                "fabric-loot-api-v2": (14, 0),
                "fabric-loot-api-v3": (17, 0),
                "fabric-recipe-api-v1": (27, 0),
                "fabric-api-lookup-api-v1": (29, 0),
                "fabric-block-api-v1": (8, 0),
                "fabric-block-view-api-v2": (12, 2),
                "fabric-rendering-data-attachment-v1": (8, 1),
            }
            if name in block_modules:
                class_count, client_count = block_modules[name]
                files = {n for n in archive.namelist() if not n.endswith("/")}
                classes = {n for n in files if n.endswith(".class")}
                assert len(classes) == class_count
                extras: set[str] = set()
                if client_count:
                    extras.add(f"{name}.client.mixins.json")
                    client = cast("dict[str, object]", json.loads(archive.read(
                        f"{name}.client.mixins.json")))
                    assert len(cast("list[str]", client["client"])) == client_count
                    assert not client.get("mixins")
                    assert not client.get("server")
                    assert not client.get("plugin")
                if name in {"fabric-block-view-api-v2", "fabric-game-rule-api-v1",
                            "fabric-recipe-api-v1", "fabric-command-api-v2",
                            "fabric-lifecycle-events-v1", "fabric-item-group-api-v1",
                            "fabric-content-registries-v0", "fabric-data-generation-api-v1",
                            "fabric-screen-handler-api-v1", "fabric-resource-conditions-api-v1",
                            "fabric-object-builder-api-v1"}:
                    extras.add("META-INF/accesstransformer.cfg")
                extras.update({
                    "fabric-data-attachment-api-v1": {
                        "assets/fabric-data-attachment-api-v1/lang/en_us.json"},
                }.get(name, set()))
                if name == "fabric-item-group-api-v1":
                    extras.add("assets/fabric/textures/gui/creative_buttons.png")
                    extras.update(f"assets/fabric/lang/{locale}.json" for locale in (
                        "bg_bg", "de_de", "el_gr", "en_us", "eo_uy", "es_cl", "es_es",
                        "es_mx", "et_ee", "fa_ir", "fi_fi", "fr_fr", "is_is", "it_it",
                        "ja_jp", "ko_kr", "ms_my", "nl_nl", "pl_pl", "pt_br", "ru_ru",
                        "sv_se", "tok", "tr_tr", "tt_ru", "uk_ua", "vi_vn", "zh_cn", "zh_tw",

                    ))
                assert files - classes == extras | {
                    "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml",
                    "META-INF/architectury-loom-nesting-metadata.json",
                    f"assets/{name}/icon.png",
                    name.replace("fabric-object-builder-api-v1",
                                 "fabric-object-builder-v1") + ".mixins.json",
                }
                assert {n for n in classes if any(marker in archive.read(n) for marker in (
                    b"Lnet/neoforged/fml/common/Mod;",
                    b"Lnet/neoforged/fml/common/EventBusSubscriber;",
                ))} == consumers
            for row in rows:
                assert row["archive"] == source.name + "!/" + member
                assert row["archive_sha256"] == hashlib.sha256(payload).hexdigest()
                assert row["class_sha256"] == hashlib.sha256(archive.read(row["class"])).hexdigest()
                assert (
                    row["disassembly_sha256"]
                    == hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest()
                )


def test_fabric_pack_discovery_consumer_sources() -> None:
    source = next(
        s
        for s in retained_sources(Path.cwd())
        if s.name == "forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar"
    )
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    member = "META-INF/jars/fabric-resource-loader-v0-1.3.1+4ea8954419.jar"
    with ZipFile(source.path) as parent:
        payload = parent.read(member)
        with ZipFile(BytesIO(payload)) as archive:
            for label, digest, classes in (
                (
                    "fabric-pack-activation",
                    "3f4e27140b27fb0d7f009370d126338ffdc1c43bdc2508041ca94cc13f32ad5a",
                    {"ModResourcePackUtil", "ModNioResourcePack"},
                ),
                (
                    "fabric-pack-discovery",
                    "7bf8e338a6020383713752059acca9d36a8678c9a8f5b7fdbec1db280a65afda",
                    {"ModResourcePackCreator"},
                ),
                (
                    "fabric-fixed-pack",
                    "ecf4b1a13f7b850275c43454bcb9aa90f549983b6c6b36d3794a266fcc9d9134",
                    {"PlaceholderResourcePack", "PlaceholderResourcePack$Factory"},
                ),
            ):
                directory = Path("evidence/item-8/sources") / label
                raw = (directory / "identities.json").read_bytes()
                assert hashlib.sha256(raw).hexdigest() == digest
                rows = cast("list[dict[str, str]]", json.loads(raw))
                assert {r["class"] for r in rows} == {
                    "net/fabricmc/fabric/impl/resource/loader/" + c + ".class" for c in classes
                }
                for row in rows:
                    assert row["archive"] == source.name + "!/" + member
                    assert row["archive_sha256"] == hashlib.sha256(payload).hexdigest()
                    assert (
                        row["class_sha256"]
                        == hashlib.sha256(archive.read(row["class"])).hexdigest()
                    )
                    assert (
                        row["disassembly_sha256"]
                        == hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest()
                    )


@pytest.mark.parametrize(
    ("module", "label", "digest", "class_count", "source_count"),
    [
        (
            "fabric-api-base-0.4.42+d1308ded19",
            "fabric-base-entry",
            "d587a46473ff9c81c44c1567e4bc236bf01cd2f5e7afeaec02dc34275290384e",
            17,
            1,
        ),
        (
            "fabric-convention-tags-v1-2.1.5+7f945d5b19",
            "fabric-v1-tags",
            "989e88abd8f912faef93b28c7172fdc6766dc109f747f3a50c6be653e1f8ab93",
            12,
            3,
        ),
    ],
)
def test_fabric_small_library_membership(
    module: str, label: str, digest: str, class_count: int, source_count: int
) -> None:
    source = next(
        s
        for s in retained_sources(Path.cwd())
        if s.name == "forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar"
    )
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    member = f"META-INF/jars/{module}.jar"
    directory = Path("evidence/item-8/sources") / label
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == digest
    rows = cast("list[dict[str, str]]", json.loads(raw))
    assert len(rows) == source_count
    with ZipFile(source.path) as parent:
        payload = parent.read(member)
        with ZipFile(BytesIO(payload)) as archive:
            files = {n for n in archive.namelist() if not n.endswith("/")}
            classes = {n for n in files if n.endswith(".class")}
            assert len(classes) == class_count
            assert files - classes == {
                "META-INF/MANIFEST.MF",
                "META-INF/neoforge.mods.toml",
                f"assets/{module.rsplit('-', 1)[0]}/icon.png",
                "META-INF/architectury-loom-nesting-metadata.json",
            }
            assert {
                n
                for n in classes
                if any(
                    marker in archive.read(n)
                    for marker in (
                        b"Lnet/neoforged/fml/common/Mod;",
                        b"Lnet/neoforged/fml/common/EventBusSubscriber;",
                    )
                )
            } == {r["class"] for r in rows if r["class"].endswith("/GeneratedEntryPoint.class")}
            for row in rows:
                assert row["archive"] == source.name + "!/" + member
                assert row["archive_sha256"] == hashlib.sha256(payload).hexdigest()
                assert row["class_sha256"] == hashlib.sha256(archive.read(row["class"])).hexdigest()
                assert (
                    row["disassembly_sha256"]
                    == hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest()
                )


def test_fabric_v2_tag_membership() -> None:
    source = next(
        s
        for s in retained_sources(Path.cwd())
        if s.name == "forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar"
    )
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    member = "META-INF/jars/fabric-convention-tags-v2-2.11.1+87e5848019.jar"
    directory = Path("evidence/item-8/sources/fabric-v2-tags")
    raw = (directory / "identities.json").read_bytes()
    assert (
        hashlib.sha256(raw).hexdigest()
        == "4ed85ef4b7306e87cb6c093f14dee2a4d02809ab75b3d7f985829fff663e6588"
    )
    rows = cast("list[dict[str, str]]", json.loads(raw))
    assert len(rows) == 4
    with ZipFile(source.path) as parent:
        payload = parent.read(member)
        with ZipFile(BytesIO(payload)) as archive:
            files = {n for n in archive.namelist() if not n.endswith("/")}
            classes = {n for n in files if n.endswith(".class")}
            data = {n for n in files if n.startswith("data/")}
            lang = {n for n in files if n.startswith("assets/fabric-convention-tags-v2/lang/")}
            assert len(classes) == 16
            assert len(data) == 491
            assert len(lang) == 14
            assert all(n.split("/")[2] == "tags" for n in data)
            assert files - classes - data - lang == {
                "META-INF/MANIFEST.MF",
                "META-INF/neoforge.mods.toml",
                "META-INF/architectury-loom-nesting-metadata.json",
                "fabric-convention-tags-api-v2.mixins.json",
                "assets/fabric-convention-tags-v2/icon.png",
            }
            config = cast(
                "dict[str, object]",
                json.loads(archive.read("fabric-convention-tags-api-v2.mixins.json")),
            )
            assert config["mixins"] == ["TagKeyMixin"]
            assert not config.get("plugin")
            assert not config.get("server")
            for row in rows:
                assert row["archive"] == source.name + "!/" + member
                assert row["archive_sha256"] == hashlib.sha256(payload).hexdigest()
                assert row["class_sha256"] == hashlib.sha256(archive.read(row["class"])).hexdigest()
                assert (
                    row["disassembly_sha256"]
                    == hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest()
                )


@pytest.mark.parametrize(
    ("module", "label", "digest", "class_count", "client_count"),
    [
        (
            "fabric-rendering-v1-5.1.0+1a09bd5a19",
            "fabric-rendering-v1-entry",
            "adb9d93ad3ff1cf27a2299424fe89e188fd41e24d8bede1957c9bb4db9b5f4e7",
            73,
            15,
        ),
        (
            "fabric-model-loading-api-v1-2.1.0+6e8f52c719",
            "fabric-model_loading_api-entry",
            "2cb25059a4bba8b4638ba8716fc2fec8cef40bb44bfc0cc54fd69eb88094755e",
            39,
            5,
        ),
        (
            "fabric-particles-v1-4.0.2+824f924c19",
            "fabric-particles-entry",
            "a0b59940d7e1991761a4f4ceb66df00b00b2b16907e6215dedbb52be62f11ab8",
            20,
            3,
        ),
        (
            "fabric-renderer-indigo-1.7.1+9125b6dc19",
            "fabric-renderer_indigo-entry",
            "6dfed069d59ffc725aec5a0e6e5cfb8df092bf0a7f17277fe217cf410fddbfe8",
            58,
            5,
        ),
        (
            "fabric-screen-api-v1-2.0.25+0ae1214819",
            "fabric-screen_api-entry",
            "26c940bebeaf35260b92164b7b8c736bf981a4b8bf4de0daffc709f3aa83813d",
            36,
            3,
        ),
        (
            "fabric-client-tags-api-v1-1.1.15+e053909619",
            "fabric-client_tags_api-entry",
            "c21d8171de5516eadbedab75ab654617416551609d47d38c667bccc6d483bbd2",
            7,
            0,
        ),
        (
            "fabric-renderer-api-v1-3.4.1+9125b6dc19",
            "fabric-renderer_api-entry",
            "cf785b7b3847dfffba0113e5805331b67d6d5ea866d2c9e20a30fa8e596a7f55",
            35,
            5,
        ),
        (
            "fabric-rendering-fluids-v1-3.1.6+a51883b219",
            "fabric-rendering_fluids-entry",
            "fced898b4d81ad78a18d99dc2e36d482b63dd3105d049363b8abb9bb59e14908",
            20,
            3,
        ),
        (
            "fabric-blockrenderlayer-v1-1.1.52+c290471319",
            "fabric-blockrenderlayer-entry",
            "aaa25c57988927d612eb93dcbdd02fac7495d20eb470b27ba724ea0a69830e14",
            9,
            2,
        ),
        (
            "fabric-key-binding-api-v1-1.0.47+62cc7ce119",
            "fabric-key_binding_api-entry",
            "853035c0f876eeeea756b49418af6623846bfaebbfb5654a4b6272650feac16c",
            7,
            1,
        ),
        (
            "fabric-sound-api-v1-1.0.23+10b84f8419",
            "fabric-sound_api-entry",
            "56cc3df95af643d82137bc4e03d36566d6ed6d50e36d627a8fa9f26a4e5e2d13",
            4,
            1,
        ),
    ],
)
def test_fabric_client_utility_membership(
    module: str, label: str, digest: str, class_count: int, client_count: int
) -> None:
    source = next(
        s
        for s in retained_sources(Path.cwd())
        if s.name == "forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar"
    )
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    member = f"META-INF/jars/{module}.jar"
    directory = Path("evidence/item-8/sources") / label
    raw = (directory / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == digest
    rows = cast("list[dict[str, str]]", json.loads(raw))
    name = module.rsplit("-", 1)[0]
    with ZipFile(source.path) as parent:
        payload = parent.read(member)
        with ZipFile(BytesIO(payload)) as archive:
            files = {n for n in archive.namelist() if not n.endswith("/")}
            classes = {n for n in files if n.endswith(".class")}
            assert len(classes) == class_count
            extras: set[str] = (
                {f"assets/{name}/sounds/empty.ogg"} if name == "fabric-sound-api-v1" else set()
            )
            if name in {"fabric-particles-v1", "fabric-renderer-indigo"}:
                extras.add("META-INF/accesstransformer.cfg")
            mixins: set[str] = {f"{name}.mixins.json"} if client_count else set()
            if name == "fabric-particles-v1":
                mixins = {f"{name}.client.mixins.json"}
            plugin = ("net.fabricmc.fabric.impl.client.indigo.IndigoMixinConfigPlugin"
                      if name == "fabric-renderer-indigo" else None)
            if name == "fabric-renderer-api-v1":
                mixins.add(f"{name}.debughud.mixins.json")
            assert files - classes == extras | mixins | {
                "META-INF/MANIFEST.MF",
                "META-INF/neoforge.mods.toml",
                "META-INF/architectury-loom-nesting-metadata.json",
                f"assets/{name}/icon.png",
            }
            clients = 0
            for mixin in mixins:
                config = cast("dict[str, object]", json.loads(archive.read(mixin)))
                clients += len(cast("list[str]", config["client"]))
                assert not config.get("mixins")
                assert not config.get("server")
                assert config.get("plugin") == plugin
            assert clients == client_count
            annotated = {
                n
                for n in classes
                if any(
                    marker in archive.read(n)
                    for marker in (
                        b"Lnet/neoforged/fml/common/Mod;",
                        b"Lnet/neoforged/fml/common/EventBusSubscriber;",
                    )
                )
            }
            captured = {row["class"] for row in rows}
            assert len(rows) == len(captured)
            assert captured == annotated | ({plugin.replace(".", "/") + ".class"}
                                             if plugin else set())
            assert len(annotated) == (2 if name in {"fabric-particles-v1",
                                                    "fabric-screen-api-v1"} else 1)
            for row in rows:
                assert row["archive"] == source.name + "!/" + member
                assert row["archive_sha256"] == hashlib.sha256(payload).hexdigest()
                assert row["class_sha256"] == hashlib.sha256(archive.read(row["class"])).hexdigest()
                assert (
                    row["disassembly_sha256"]
                    == hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest()
                )
