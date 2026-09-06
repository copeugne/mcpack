from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_cbc_provider_sources() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "createbigcannons-5.11.6+mc.1.21.1.jar")
    assert source.sha256 == "9345e8773aa8be0f33bbf633796124e70d84c0c299aac94d8d252086f8712ffe"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        entries = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in entries if n.endswith(".class")}
        assert len(classes) == 855
        assert not any(n.endswith(".jar") or n.startswith("META-INF/services/") for n in entries)
        assert Counter("/".join(n.split("/")[:3]) for n in entries if n.startswith("data/")) == {
            "data/c/block_armor": 1,
            "data/c/fluid_casting_time": 3,
            "data/c/tags": 21,
            "data/copycats/block_armor": 42,
            "data/create/block_armor": 4,
            "data/create/fluid_drag": 2,
            "data/create/tags": 1,
            "data/createbigcannons/advancement": 69,
            "data/createbigcannons/big_cannon_breech_strength": 14,
            "data/createbigcannons/big_cannon_propellant_compatibility": 2,
            "data/createbigcannons/block_armor": 4,
            "data/createbigcannons/cannon_mounts": 12,
            "data/createbigcannons/createbigcannons": 68,
            "data/createbigcannons/damage_type": 9,
            "data/createbigcannons/fluid_casting_time": 1,
            "data/createbigcannons/loot_table": 163,
            "data/createbigcannons/munition_properties": 20,
            "data/createbigcannons/recipe": 148,
            "data/createbigcannons/tags": 36,
            "data/curios/curios": 1,
            "data/curios/tags": 1,
            "data/example_createbigcannons/autocannon_materials": 1,
            "data/example_createbigcannons/big_cannon_materials": 1,
            "data/forge/fluid_casting_time": 3,
            "data/framedblocks/block_armor": 234,
            "data/minecraft/advancement": 3,
            "data/minecraft/block_armor": 3,
            "data/minecraft/block_impact_transforms": 84,
            "data/minecraft/dimension_munition_properties": 3,
            "data/minecraft/fluid_drag": 2,
            "data/minecraft/recipe": 3,
            "data/minecraft/tags": 8,
            "data/ritchiesprojectilelib/tags": 1,
            "data/sable/tags": 1,
        }
        templates = {n for n in entries if n.endswith(".nbt")}
        assert len(templates) == 29
        assert all(n.startswith("assets/createbigcannons/ponder/") for n in templates)
        expected = {n for n in classes if any(m in archive.read(n) for m in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;"))}
        assert len(expected) == 4
        assert {n for n in entries if n.endswith(".mixins.json")} == {
            "createbigcannons.mixins.json"}
        config = cast("dict[str, object]", json.loads(archive.read("createbigcannons.mixins.json")))
        assert not config.get("server")
        assert config["plugin"] == "rbasamoyai.createbigcannons.mixin.CBCMixinPlugin"
        expected.add("rbasamoyai/createbigcannons/mixin/CBCMixinPlugin.class")
        hooks = cast("list[str]", config["mixins"])
        assert len(hooks) == 32
        assert len(cast("list[str]", config["client"])) == 15
        package = cast("str", config["package"])
        expected.update((package + "." + n).replace(".", "/") + ".class" for n in hooks)
        captured: set[str] = set()
        for label, digest in (
            ("cbc-entries",
             "34084f6b095fa3a365fd9eb4d5dc6546196bad204cc0696d4e7e22a2745fbd03"),
            ("cbc-hooks",
             "cfd48271f17ea88276511132b9414c8aae446a331f0e192beb447551985e2b3d"),
            ("cbc-startup",
             "77b90977e315c3ddbcfb5c30700f93b77b364885a81ff6e314d040df7ef643ca"),
            ("cbc-common-events",
             "a8899d3cba54bb5c7e0da30952234cc3c540eb4df9aa4851bceeefacaaf5ad83"),
            ("cbc-damage-lifecycle",
             "fc3bb447345adec09fbd181d9c43b2490d69e17931a464c80545ad5ad0d3e0dc"),
            ("cbc-registrations",
             "94c69321a38866c013862a5bd80184b821395b990f060894554002224d25fb84"),
            ("cbc-construction-integration",
             "d6757c318a5b47fa8a69dad0f22f266078fada6307470a154d1203a41b827faa"),
        ):
            directory = Path("evidence/item-8/sources") / label
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            expected_files = {directory / "identities.json", directory / "README.md"}
            for row in cast("list[dict[str, str]]", json.loads(raw)):
                captured.add(row["class"])
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert row["class_sha256"] == hashlib.sha256(archive.read(row["class"])).hexdigest()
                target = directory / row["disassembly"]
                assert target.resolve().is_relative_to(directory.resolve())
                assert hashlib.sha256(target.read_bytes()).hexdigest() == row["disassembly_sha256"]
                expected_files.add(target)
            assert {p for p in directory.rglob("*") if p.is_file()} == expected_files
        assert expected <= captured
        assert len(captured) == 62
