from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_registry import read_registry
from mcpack_evidence.item8_sources import retained_sources


def test_mineshaft_provider_entries_and_payload() -> None:
    # Bind reused entry evidence and the bounded remainder in one archive check.
    source = next(
        s for s in retained_sources(Path.cwd()) if s.name.startswith("YungsBetterMineshafts-")
    )
    assert source.sha256 == "5625930dfb3240820d6e4ecf55fff0c39f70ce782fad117a4d418251184c7be0"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    captured: set[str] = set()
    manifests = (
        ("mineshafts-code",
         "5e78a733f4198752de93fb640557a87fae13334a92a3fbad422cd33bb5d41127"),
        ("mineshafts-provider",
         "5fe961b0858c511f20ec7d8e5a858ded64899576f6685e721c4e3113d914a707"),
    )
    with ZipFile(source.path) as archive:
        names = {n for n in archive.namelist() if not n.endswith("/")}
        assert len(names) == 95
        for folder, digest in manifests:
            base = Path("evidence/item-8/sources") / folder
            raw = (base / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == digest
            for row in cast("list[dict[str, str]]", json.loads(raw)):
                assert row["archive"] == source.name
                assert row["archive_sha256"] == source.sha256
                assert hashlib.sha256(archive.read(row["class"])).hexdigest() == row["class_sha256"]
                assert hashlib.sha256((base / row["disassembly"]).read_bytes()).hexdigest() == (
                    row["disassembly_sha256"]
                )
                captured.add(row["class"])
        prefix = "com/yungnickyoung/minecraft/bettermineshafts/"
        classes = {n for n in names if n.endswith(".class")}
        assert len(classes) == 51
        assert classes == captured
        mixins = cast(
            "dict[str, list[str]]", json.loads(archive.read("bettermineshafts.mixins.json"))
        )
        assert {prefix + "mixin/" + n.replace(".", "/") + ".class"
                for n in mixins["mixins"]} <= captured
        services = "com.yungnickyoung.minecraft.bettermineshafts.services."
        for interface, implementation in (
            ("IModulesLoader", "NeoForgeModulesLoader"),
            ("IPlatformHelper", "NeoForgePlatformHelper"),
        ):
            assert archive.read("META-INF/services/" + services + interface).decode().strip() == (
                services + implementation
            )
        for name in names - classes:
            if name.startswith(("assets/bettermineshafts/lang/", "data/bettermineshafts/tags/",
                                "data/minecraft/tags/", "data/morevillagers/tags/")):
                assert name.endswith(".json"), name
            elif name.startswith("data/bettermineshafts/worldgen/"):
                assert name.endswith(".json"), name
                assert name.split("/")[3] in {"structure", "structure_set"}, name
            else:
                assert name in {
                    "META-INF/MANIFEST.MF", "META-INF/neoforge.mods.toml", "pack.mcmeta",
                    "bettermineshafts.mixins.json", "catalogue_background.png",
                    "catalogue_icon.png",
                    "icon.png", "logo.png", "LICENSE_YungsBetterMineshafts",
                    "META-INF/services/" + services + "IModulesLoader",
                    "META-INF/services/" + services + "IPlatformHelper",
                }, name
        roots = {
            "bettermineshafts:" + Path(n).stem for n in names
            if n.startswith("data/bettermineshafts/worldgen/structure/")
        }
        assert len(roots) == 13
        structure_set = cast("dict[str, object]", json.loads(archive.read(
            "data/bettermineshafts/worldgen/structure_set/mineshafts.json"
        )))
        entries = cast("list[dict[str, object]]", structure_set["structures"])
        assert {entry["structure"] for entry in entries} == roots
        assert all(entry["weight"] == 1 for entry in entries)
    registry = read_registry(Path(
        "evidence/item-8/runtime/registry-r1/dumps/registry/minecraft/worldgen_structure.txt"
    ))
    assert roots == {r for r in registry if r.startswith("bettermineshafts:")}
