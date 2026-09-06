from __future__ import annotations

import hashlib
import json
from contextlib import ExitStack
from io import BytesIO
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


# Keep the fixed archive topology and evidence join together without a new helper layer.
def test_c2me_provider_membership_evidence() -> None:  # noqa: C901, PLR0912, PLR0915
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar")
    assert source.sha256 == "2735b16e136e51c03c9a8211fbecaf9d571a28475981223c60662465664f5322"
    parent_bytes = source.path.read_bytes()
    assert hashlib.sha256(parent_bytes).hexdigest() == source.sha256
    with ExitStack() as stack:
        parent = stack.enter_context(ZipFile(BytesIO(parent_bytes)))
        payloads = {source.name: parent_bytes}
        for name in parent.namelist():
            if name.endswith(".jar"):
                payloads[source.name + "!/" + name] = parent.read(name)
        assert len(payloads) == 27
        outer = source.name + "!/META-INF/jars/mixinsquared-neoforge-0.2.0-beta.6.jar"
        wrapper = stack.enter_context(ZipFile(BytesIO(payloads[outer])))
        inner = "META-INF/jars/MixinSquared-0.2.0-beta.6.jar"
        payloads[outer + "!/" + inner] = wrapper.read(inner)
        archives = {name: stack.enter_context(ZipFile(BytesIO(raw)))
                    for name, raw in payloads.items()}
        expected: set[str] = set()
        null_hooks = 0
        for name, archive in archives.items():
            files = {n for n in archive.namelist() if not n.endswith("/")}
            assert not any(n.startswith("data/") or n.endswith(".nbt") for n in files)
            for member in files:
                if member.endswith(".jar"):
                    assert name + "!/" + member in archives
                if member.startswith("META-INF/services/"):
                    assert name == outer + "!/" + inner
                    assert member == "META-INF/services/javax.annotation.processing.Processor"
                if member.endswith(".class") and any(
                    marker in archive.read(member) for marker in (
                        b"Lnet/neoforged/fml/common/Mod;",
                        b"Lnet/neoforged/fml/common/EventBusSubscriber;",
                    )
                ):
                    expected.add(member)
                if member == "fabric.mod.json":
                    metadata = cast("dict[str, object]", json.loads(archive.read(member)))
                    assert not metadata.get("entrypoints")
                if member.endswith(".mixins.json"):
                    config = cast("dict[str, object]", json.loads(archive.read(member)))
                    package = cast("str", config["package"])
                    hooks = cast("list[str | None]", config.get("mixins", []))
                    hooks += cast("list[str | None]", config.get("server", []))
                    for hook in hooks:
                        if hook is None:
                            assert member == "c2me-opts-scheduling.mixins.json"
                            null_hooks += 1
                        else:
                            target = (package + "." + hook).replace(".", "/") + ".class"
                            assert target in files
                            expected.add(target)
                    if config.get("plugin"):
                        expected.add(cast("str", config["plugin"]).replace(".", "/") + ".class")
            if not name.startswith(source.name + "!/META-INF/jars/c2me-") and name not in (
                source.name, outer, outer + "!/" + inner,
            ):
                assert not any(b"net/minecraft/" in archive.read(n)
                               for n in files if n.endswith(".class"))
                assert not any(n.endswith((".mixins.json", "mods.toml")) for n in files)
        assert null_hooks == 1
        manifests = sorted(Path("evidence/item-8/sources").glob("c2me-*/identities.json"))
        assert len(manifests) == 52
        identity_hash = hashlib.sha256()
        captured: set[str] = set()
        rows_seen = 0
        for manifest in manifests:
            raw = manifest.read_bytes()
            identity_hash.update(str(manifest).encode() + b"\0" + raw)
            directory = manifest.parent
            expected_files = {manifest, directory / "README.md"}
            for row in cast("list[dict[str, str]]", json.loads(raw)):
                assert set(row) == {"archive", "archive_sha256", "class", "class_sha256",
                                    "disassembly", "disassembly_sha256"}
                assert row["archive_sha256"] == hashlib.sha256(payloads[row["archive"]]).hexdigest()
                assert row["class_sha256"] == hashlib.sha256(
                    archives[row["archive"]].read(row["class"])).hexdigest()
                target = directory / row["disassembly"]
                assert target.resolve().is_relative_to(directory.resolve())
                assert hashlib.sha256(target.read_bytes()).hexdigest() == row["disassembly_sha256"]
                expected_files.add(target)
                captured.add(row["class"])
                rows_seen += 1
            assert {p for p in directory.rglob("*") if p.is_file()} == expected_files
        assert identity_hash.hexdigest() == (
            "4373d579c97ac5903560652e3544e597dccb75ed28557e5dbb39747b1dc1b0f0")
        assert rows_seen == 259
        assert expected <= captured
