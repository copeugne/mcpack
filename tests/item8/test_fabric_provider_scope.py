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
def test_fabric_sources_cover_declared_mixins(
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
                json.loads(archive.read(module.rsplit("-", 1)[0] + ".mixins.json")),
            )
            prefix = cast("str", config["package"]).replace(".", "/") + "/"
            declared = {prefix + name + ".class" for name in cast("list[str]", config["mixins"])}
            assert len(declared) == count
            assert not config.get("plugin")
            assert not config.get("server")
            assert {r["class"] for r in rows} == declared | consumers
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


def test_fabric_base_module_membership() -> None:
    source = next(
        s
        for s in retained_sources(Path.cwd())
        if s.name == "forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar"
    )
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    member = "META-INF/jars/fabric-api-base-0.4.42+d1308ded19.jar"
    directory = Path("evidence/item-8/sources/fabric-base-entry")
    raw = (directory / "identities.json").read_bytes()
    assert (
        hashlib.sha256(raw).hexdigest()
        == "d587a46473ff9c81c44c1567e4bc236bf01cd2f5e7afeaec02dc34275290384e"
    )
    rows = cast("list[dict[str, str]]", json.loads(raw))
    assert len(rows) == 1
    row = rows[0]
    with ZipFile(source.path) as parent:
        payload = parent.read(member)
        with ZipFile(BytesIO(payload)) as archive:
            files = {n for n in archive.namelist() if not n.endswith("/")}
            classes = {n for n in files if n.endswith(".class")}
            assert len(classes) == 17
            assert files - classes == {
                "META-INF/MANIFEST.MF",
                "META-INF/neoforge.mods.toml",
                "assets/fabric-api-base/icon.png",
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
            } == {row["class"]}
            assert row["archive"] == source.name + "!/" + member
            assert row["archive_sha256"] == hashlib.sha256(payload).hexdigest()
            assert row["class_sha256"] == hashlib.sha256(archive.read(row["class"])).hexdigest()
            assert (
                row["disassembly_sha256"]
                == hashlib.sha256((directory / row["disassembly"]).read_bytes()).hexdigest()
            )
