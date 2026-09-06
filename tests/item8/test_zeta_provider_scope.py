from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING, cast
from zipfile import ZipFile

from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_sources import retained_sources

if TYPE_CHECKING:
    from pydantic import JsonValue

SOURCES = (
    ("quark-enablement-callers",
     "10046ea0375f2b2bca63749954b6316c177282bf17631320ad2f69329569280e"),
    ("zeta-biome-modifier",
     "4f0d0886dc653d4ba70c935a66fb2bbd17488286b6ee8462dffe4a428f41ddd3"),
    ("zeta-component-biomes",
     "16a0b7d4dc4bb3610428052193941a97a401556dfe1a60fee01c7cd020dfc922"),
    ("zeta-compound-biome",
     "a65d7c83d0c1ce02d1d4526b9d199862c60cc7d6047acc96eb4d2f3b936de890"),
    ("zeta-config-binding",
     "16802f7394df715f82bd4d14f4f2ce36154d7db6b7ae21e6585050ffe1d92d5e"),
    ("zeta-config-event-fields",
     "05201729f592b83a7129df6bc7eb29b2fde19d1e1c191fc2e24a9e8dba9115a3"),
    ("zeta-deferred-feature",
     "809590b4bbe55e382e7dc391d846cd6eb71183846b9aa200ebd90eccf394bd2e"),
    ("zeta-dynamic-registration",
     "57fec3b7ea3952e0ece732fa29d13960a59ccfb7ace26c3daa4eb5a9d32c375c"),
    ("zeta-dynamic-registry",
     "a36377227dbb20649ef7b39f6f08c2c59afbbdf793117946a94251c2f867b77f"),
    ("zeta-enablement-inputs",
     "296a18f820faacbcd149a7f42fae453122fc01eafb28184bc275e12a241c011a"),
    ("zeta-generation-applicability",
     "b1668715f596ff4149c5cd17af2e49f95d65b173db9a6d9705bb35dfca25b62a"),
    ("zeta-generation-spawn",
     "ace51ef9a5c0f9a983ed951fac529bc0a662e5c9cb286dcd1828eee4f39789f3"),
    ("zeta-generator-dispatch",
     "406a4dd62827c7419ee2ff380a5f626206ed850e480c9e5b9e04862edc8606c5"),
    ("zeta-horizontal-directions",
     "d1fe1dd3ec67af3303fbee2b9b688b9191c82a19ea2d38d39b95f5b9ede28950"),
    ("zeta-module-assignment",
     "e2c01f2e58f5c3df5e4619862fb4ca1887c6bb815b80c2697dd00a1e55aee9fc"),
    ("zeta-module-name",
     "be6109c7d9ee30f6174e6ea384e7d5f2b6ddad186e66aa784b8fc7bffae4ed08"),
    ("zeta-module-section",
     "1ebf92172aa8dc1f01ecc7ea2908fa53d90740828f2db5eac284aa000302a830"),
    ("zeta-provider",
     "735e88c82e649abe73822a432ba2e9a71c1c67387e0236aaa0ca88bbfea94099"),
    ("zeta-stone-ore",
     "98fa51e258190480cfb4505c4d2c2ec36d3a524953e55ba8862ef73eeed8bf0a"),
)


def test_zeta_provider_payload_and_dispatch_sources() -> None:
    # Reuse existing module, configuration and generation evidence for this shared provider.
    source = next(s for s in retained_sources(Path.cwd()) if s.name == "Zeta-1.1-40.jar")
    assert source.sha256 == "4f17d1a2b9fd6d18ddb7697aa451db7fb154053b8648f79de279ae0d7e68a2fa"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    captured: set[str] = set()
    with ZipFile(source.path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        assert len(names) == len(set(names)) == 627
        classes = {n for n in names if n.endswith(".class")}
        assert len(classes) == 616
        assert Counter("/".join(n.split("/")[:2]) for n in classes) == {
            "org/violetmoon": 609, "math/fast": 7,
        }
        assert set(names) - classes == {
            "META-INF/MANIFEST.MF", "META-INF/accesstransformer.cfg",
            "META-INF/neoforge.mods.toml", "assets/zeta/textures/gui/general_icons.png",
            "assets/zeta/lang/ru_ru.json", "assets/zeta/lang/zh_cn.json",
            "assets/zeta/lang/en_us.json", "zeta.mixins.json", "pack.mcmeta",
            "zeta_forge.mixins.json", "data/zeta/neoforge/biome_modifier/biome_modifier.json",
        }
        assert json.loads(archive.read(
            "data/zeta/neoforge/biome_modifier/biome_modifier.json"
        )) == {"type": "zeta:biome_modifier"}
        for directory, digest in SOURCES:
            base = Path("evidence/item-8/sources") / directory
            raw = (base / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            for row in cast("list[dict[str, str]]", json.loads(raw)):
                if row["archive"] != source.name:
                    continue
                assert row["archive_sha256"] == source.sha256
                assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
                assert hashlib.sha256((base / row["disassembly"]).read_bytes()).hexdigest() == (
                    row["disassembly_sha256"]
                )
                captured.add(row["class"])
        assert len(captured) == 49
        for filename, prefix, count in (
            ("zeta.mixins.json", "org/violetmoon/zeta/mixin/mixins/", 14),
            ("zeta_forge.mixins.json", "org/violetmoon/zetaimplforge/mixin/mixins/", 4),
        ):
            doc = cast("dict[str, JsonValue]", json.loads(archive.read(filename)))
            entries = cast("list[str]", doc["mixins"])
            assert len(entries) == count
            assert {prefix + n.replace(".", "/") + ".class" for n in entries} <= captured
            if filename == "zeta.mixins.json":
                assert "plugin" not in doc
                assert doc["client"] == []
            else:
                assert doc["plugin"] == (
                    "org.violetmoon.zeta.mixin.plugin.InterfaceDelegateMixinPlugin"
                )
                assert doc["client"] == [
                    "client.AccessorBlockColors", "client.AccessorItemColors",
                    "client.GameRenderMixin",
                ]
        assert {n for n in classes if b"Lnet/neoforged/fml/common/Mod;" in archive.read(n)} == {
            "org/violetmoon/zetaimplforge/mod/ZetaModForge.class",
        }
        assert not {n for n in classes if b"EventBusSubscriber;" in archive.read(n)}
    registry = read_registry(Path(
        "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    ))
    assert not {n for n in registry if n.startswith("zeta:")}
