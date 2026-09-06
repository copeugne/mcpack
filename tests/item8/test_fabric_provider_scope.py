from __future__ import annotations

import hashlib
import json
from collections import Counter
from io import BytesIO
from pathlib import Path
from typing import cast
from zipfile import ZipFile

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


def test_fabric_biome_selection_sources_cover_declared_mixins() -> None:
    source = next(
        s
        for s in retained_sources(Path.cwd())
        if s.name == "forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar"
    )
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    member = "META-INF/jars/fabric-biome-api-v1-13.0.31+1e62d33c19.jar"
    directory = Path("evidence/item-8/sources/fabric-biome-selection")
    raw = (directory / "identities.json").read_bytes()
    assert (
        hashlib.sha256(raw).hexdigest()
        == "de014a8e4cb7983f0b7dee3f690487f1d7a0fe016dea4855f91d42202331cd73"
    )
    rows = cast("list[dict[str, str]]", json.loads(raw))
    with ZipFile(source.path) as parent:
        payload = parent.read(member)
        with ZipFile(BytesIO(payload)) as archive:
            config = cast(
                "dict[str, object]", json.loads(archive.read("fabric-biome-api-v1.mixins.json"))
            )
            prefix = cast("str", config["package"]).replace(".", "/") + "/"
            declared = {prefix + name + ".class" for name in cast("list[str]", config["mixins"])}
            assert len(declared) == 6
            assert not config.get("plugin")
            assert not config.get("server")
            assert {r["class"] for r in rows} == declared | {
                "net/fabricmc/fabric/impl/biome/NetherBiomeData.class",
                "net/fabricmc/fabric/impl/biome/TheEndBiomeData.class",
            }
            for row in rows:
                assert row["archive"] == source.name + "!/" + member
                assert row["archive_sha256"] == hashlib.sha256(payload).hexdigest()
                assert row["class_sha256"] == hashlib.sha256(archive.read(row["class"])).hexdigest()
                assert (
                    row["disassembly_sha256"]
                    == hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest()
                )
