from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_cei_provider_membership() -> None:
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "create-enchantment-industry-2.4.0.jar")
    assert source.sha256 == "3830e27941fe08334217ded82713907a176bd2feb209292da25154e4c082585e"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    with ZipFile(source.path) as archive:
        entries = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in entries if n.endswith(".class")}
        assert len(classes) == 338
        assert Counter("/".join(n.split("/")[:3]) for n in entries if n.startswith("data/")) == {
            "data/create_enchantment_industry/advancement": 45,
            "data/create_enchantment_industry/recipe": 43,
            "data/create_enchantment_industry/loot_table": 15,
            "data/create_enchantment_industry/data_maps": 13,
            "data/create_enchantment_industry/tags": 12, "data/c/tags": 8,
            "data/sable/physics_block_properties": 4, "data/create/tags": 4,
            "data/minecraft/tags": 2, "data/create_enchantment_industry/damage_type": 1}
        templates = {n for n in entries if n.endswith(".nbt")}
        assert len(templates) == 23
        assert all(n.startswith("assets/create_enchantment_industry/ponder/") for n in templates)
        assert all("/loot_table/blocks/" in n for n in entries if "/loot_table/" in n)
        assert not any(n.startswith("META-INF/services/") for n in entries)
        nested = "META-INF/jarjar/conditional-mixin-neoforge-0.6.4.jar"
        assert {n for n in entries if n.endswith(".jar")} == {nested}
        assert hashlib.sha256(archive.read(nested)).hexdigest() == (
            "0ae7b346d87879e81f276e6a590a6af1e723193e6eb3e94c1f71f7ab5b54d59f")
        expected = {n for n in classes if any(m in archive.read(n) for m in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;"))}
        assert len(expected) == 11
        configs = {n for n in entries if n.endswith(".mixins.json")}
        assert len(configs) == 4
        hooks: set[str] = set()
        for name in configs:
            config = cast("dict[str, object]", json.loads(archive.read(name)))
            assert not config.get("server")
            assert not config.get("client")
            assert config.get("plugin") == (
                None if name == "create_enchantment_industry.mixins.json"
                else "plus.dragons.createdragonsplus.mixin.CDPMixinConfigPlugin")
            package = cast("str", config["package"])
            hooks.update((package + "." + n).replace(".", "/") + ".class"
                         for n in cast("list[str]", config["mixins"]))
        assert len(hooks) == 20
        expected.update(hooks)
        captured: set[str] = set()
        for label, digest in (
            ("cei-entries", "fec327e85c331d136cc9e460de13202cb189426d4535baa574c784b5bb943888"),
            ("cei-hooks", "1d37bcd725fde63649bc32b2ea767ad6a31d60bfafbf9d7a6daac6415c18b94d"),
            ("cei-registrations",
             "0bad3e258381b1b53c63185b022ceb24256943b016180c2d778e6dc068c8ecfb"),
            ("cei-world-interaction",
             "7db1f5ca32e9a65bd7794f7034d78a9e9ea19b5d9568c15b05e2ce989d9b5e92"),
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
        assert len(captured) == 47
