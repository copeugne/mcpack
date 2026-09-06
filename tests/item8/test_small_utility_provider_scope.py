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
])
def test_complete_small_utility_payload_and_entry_binding(  # noqa: C901 - explicit archive cases.
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
        # in sources/small-utility-providers.md, not inferred from search absence.
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
        assert subscribers == expected
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert metadata["modLoader"] == "javafml"
        declarations = cast("list[dict[str, str]]", metadata.get("mixins", []))
        assert {r["config"] for r in declarations} == {
            n for n in other_files if n.endswith(".mixins.json")
        }
        for row in declarations:
            mixin = cast("dict[str, JsonValue]", json.loads(archive.read(row["config"])))
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
