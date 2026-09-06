from __future__ import annotations

import hashlib
import json
from collections import Counter
from io import BytesIO
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_comforts_provider_membership() -> None:  # noqa: PLR0915 - fixed two-archive binding.
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "comforts-neoforge-9.0.5+1.21.1.jar")
    assert source.sha256 == "6b0fd35a1349107e08a45539adbde9683bb203febc43a3305f6fc4ac73e59615"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    member = "META-INF/jarjar/spectrelib-neoforge-0.17.2+1.21.jar"
    with ZipFile(source.path) as outer:
        files = {n for n in outer.namelist() if not n.endswith("/")}
        assert {n for n in files if n.endswith(".jar")} == {member}
        assert Counter("/".join(n.split("/")[:3]) for n in files if n.startswith("data/")) == {
            "data/comforts/advancement": 66, "data/comforts/recipe": 66,
            "data/comforts/loot_table": 33, "data/comforts/tags": 4, "data/c/tags": 1}
        assert all("/loot_table/blocks/" in n for n in files if "/loot_table/" in n)
        nested_raw = outer.read(member)
        nested_hash = hashlib.sha256(nested_raw).hexdigest()
        assert nested_hash == "5be2f580af278c5707679ceb079aee46d13ffbe6c2f5138c86598a8e90ca3969"
        with ZipFile(BytesIO(nested_raw)) as nested:
            for archive, identity, digest, label, manifest, count, services in (
                (outer, source.name, source.sha256, "comforts-provider",
                 "bc8225ebfe7a6c9adb2ae59292190d4be3b3f4a3664e25c6cbf3b31eadc2846c", 64, 4),
                (nested, source.name + "!/" + member, nested_hash, "comforts-spectrelib",
                 "a7bc109634fc422c5e64b85dd7ecd264de17cf9bd1177fdfda251a59078fe02c", 53, 1),
            ):
                entries = {n for n in archive.namelist() if not n.endswith("/")}
                classes = {n for n in entries if n.endswith(".class")}
                assert len(classes) == count
                assert not any(n.endswith(".nbt") for n in entries)
                if archive is nested:
                    assert not any(n.startswith("data/") or n.endswith(".jar") for n in entries)
                service_paths = {n for n in entries if n.startswith("META-INF/services/")}
                assert len(service_paths) == services
                expected = {archive.read(n).decode().strip().replace(".", "/") + ".class"
                            for n in service_paths}
                automatic = {n for n in classes if any(m in archive.read(n) for m in (
                    b"Lnet/neoforged/fml/common/Mod;",
                    b"Lnet/neoforged/fml/common/EventBusSubscriber;"))}
                assert len(automatic) == 1
                expected.update(automatic)
                configs = {n for n in entries if n.endswith(".mixins.json")}
                assert configs == ({"comforts.mixins.json"} if archive is outer else set())
                for name in configs:
                    config = cast("dict[str, object]", json.loads(archive.read(name)))
                    assert not config.get("plugin")
                    assert not config.get("server")
                    assert not config.get("client")
                    hooks = cast("list[str]", config["mixins"])
                    assert len(hooks) == 3
                    package = cast("str", config["package"])
                    expected.update((package + "." + n).replace(".", "/") + ".class"
                                    for n in hooks)
                directory = Path("evidence/item-8/sources") / label
                raw = (directory / "identities.json").read_bytes()
                assert hashlib.sha256(raw).hexdigest() == manifest
                captured: set[str] = set()
                expected_files = {directory / "identities.json", directory / "README.md"}
                for row in cast("list[dict[str, str]]", json.loads(raw)):
                    captured.add(row["class"])
                    assert row["archive"] == identity
                    assert row["archive_sha256"] == digest
                    class_hash = hashlib.sha256(archive.read(row["class"])).hexdigest()
                    assert row["class_sha256"] == class_hash
                    target = directory / row["disassembly"]
                    assert target.resolve().is_relative_to(directory.resolve())
                    assert hashlib.sha256(target.read_bytes()).hexdigest() == row[
                        "disassembly_sha256"]
                    expected_files.add(target)
                assert expected <= captured
                assert len(captured) == (12 if archive is outer else 2)
                assert {p for p in directory.rglob("*") if p.is_file()} == expected_files
