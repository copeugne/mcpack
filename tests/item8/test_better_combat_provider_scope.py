from __future__ import annotations

import hashlib
import json
import tomllib
from collections import Counter
from io import BytesIO
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_better_combat_membership_payload() -> None:
    sources = {s.name: s for s in retained_sources(Path.cwd())}
    source = sources["bettercombat-neoforge-2.3.2+1.21.1.jar"]
    assert source.sha256 == "afb1f28271ee3b622947f533aa754bb22ed67edd4940a3e9fdf2cca1edb7b8a9"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    prefix = "net/bettercombat/"
    entries = {prefix + "neoforge/" + n + ".class" for n in (
        "NeoForgeEvents", "NeoForgeMod", "client/NeoForgeClientEvents",
        "client/NeoForgeClientMod", "network/NetworkEvents")}
    with ZipFile(source.path) as archive:
        files = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in files if n.endswith(".class")}
        assert len(classes) == 158
        assets = {n for n in files if n.startswith("assets/")}
        assert Counter("/".join(n.split("/")[:3]) for n in assets) == {
            "assets/bettercombat/textures": 76, "assets/bettercombat/player_animations": 31,
            "assets/bettercombat/sounds": 26, "assets/bettercombat/lang": 14,
            "assets/bettercombat/particles": 12, "assets/bettercombat/icon.png": 1,
            "assets/bettercombat/sounds.json": 1}
        data = {n for n in files if n.startswith("data/")}
        assert len(data) == 41
        assert all(n.endswith(".json") and n.split("/")[2] == "weapon_attributes"
                   and n.split("/")[1] in {"bettercombat", "minecraft"} for n in data)
        member = "META-INF/jars/tiny-config-3.1.0-neoforge.jar"
        assert files - classes - assets - data == {
            "META-INF/MANIFEST.MF", "META-INF/jarjar/metadata.json", member,
            "META-INF/neoforge.mods.toml", "bettercombat-common-common-refmap.json",
            "bettercombat.mixins.json", "logo.png"}
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert metadata["modLoader"] == "javafml"
        assert metadata["mixins"] == [{"config": "bettercombat.mixins.json"}]
        assert {n for n in classes if any(marker in archive.read(n) for marker in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;",
        ))} == entries
        config = cast("dict[str, object]", json.loads(archive.read("bettercombat.mixins.json")))
        assert config["package"] == "net.bettercombat.mixin"
        assert config["plugin"] == "net.bettercombat.mixin.BetterCombatMixinPlugin"
        assert not config.get("server")
        hooks = cast("list[str]", config["mixins"])
        assert len(hooks) == 10
        assert len(cast("list[str]", config["client"])) == 9
        expected = entries | {prefix + "mixin/" + n.replace(".", "/") + ".class" for n in hooks}
        expected.update(prefix + n + ".class" for n in (
            "BetterCombatMod", "mixin/BetterCombatMixinPlugin", "logic/WeaponRegistry",
            "compat/CompatFeatures", "compat/FTBTeamsCompat"))
        captured: set[str] = set()
        for label, digest in (
            ("better-combat-provider",
             "7f90725b678a3a3965742f31d2939b4ee5c56e35b3e40bbbc4afed3d25c22b00"),
            ("better-combat-resources",
             "b6b66cb55ed1fc68c07a3370a6e2d4bbd56a83b5d61befc8279d91a0d7a52645"),
            ("better-combat-team-compat",
             "ece6a78c110821304a3fabfc806c5d7885f8f42612a9c09af83a1f8d47bbdfbf"),
        ):
            directory = Path("evidence/item-8/sources") / label
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            rows = cast("list[dict[str, str]]", json.loads(raw))
            for row in rows:
                captured.add(row["class"])
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert row["class_sha256"] == hashlib.sha256(archive.read(row["class"])).hexdigest()
                assert row["disassembly_sha256"] == hashlib.sha256(
                    (directory / row["disassembly"]).read_bytes()).hexdigest()
        assert captured == expected


def test_better_combat_reuses_tiny_config_payload() -> None:
    sources = {s.name: s for s in retained_sources(Path.cwd())}
    source = sources["bettercombat-neoforge-2.3.2+1.21.1.jar"]
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    member = "META-INF/jars/tiny-config-3.1.0-neoforge.jar"
    with ZipFile(source.path) as archive:
        nested = archive.read(member)
        assert hashlib.sha256(nested).hexdigest() == (
            "eef9a1d8b3fa561b08cb7b765ba15f2055277d44399cb1261cec0296550c6e3c")
        tavern = sources["village_taverns-neoforge-1.1.5+1.21.1.jar"]
        assert hashlib.sha256(tavern.path.read_bytes()).hexdigest() == tavern.sha256
        with ZipFile(tavern.path) as other:
            reused = other.read(member)
        assert hashlib.sha256(reused).hexdigest() == (
            "1587ed9848881e7b677da5b8c85e0f35719315eb5f6571592d31840cf1421f63")
        with ZipFile(BytesIO(nested)) as a, ZipFile(BytesIO(reused)) as b:
            names = {n for n in a.namelist() if not n.endswith("/")}
            assert names == {n for n in b.namelist() if not n.endswith("/")}
            assert all(a.read(n) == b.read(n) for n in names)
