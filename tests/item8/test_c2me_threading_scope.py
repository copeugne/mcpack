from __future__ import annotations

import hashlib
import json
from io import BytesIO
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_c2me_worldgen_threading_membership_evidence() -> None:
    """Bind this module's entire declared hook set, not whole C2ME coverage."""
    source = next(s for s in retained_sources(Path.cwd())
                  if s.name == "c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar")
    assert source.sha256 == "2735b16e136e51c03c9a8211fbecaf9d571a28475981223c60662465664f5322"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    member = "META-INF/jars/c2me-fixes-worldgen-threading-issues-mc1.21.1-0.3.0+alpha.0.93.jar"
    digest = "7f780a5be2f877117870543b08805e4fee9fec852571fae08e51fc244be22f65"
    with ZipFile(source.path) as parent:
        payload = parent.read(member)
    assert hashlib.sha256(payload).hexdigest() == digest
    with ZipFile(BytesIO(payload)) as archive:
        files = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in files if n.endswith(".class")}
        assert len(classes) == 52
        assert files - classes == {
            "META-INF/MANIFEST.MF", "LICENSE", "META-INF/neoforge.mods.toml",
            "META-INF/architectury-loom-nesting-metadata.json",
            "c2me-fixes-worldgen-threading-issues.mixins.json",
            "c2me-fixes-worldgen-threading-issues-mc1.21.1-c2me-fixes-worldgen-threading-issues-refmap.json",
        }
        assert not any(marker in archive.read(n) for n in classes for marker in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;"))
        config = cast("dict[str, object]", json.loads(
            archive.read("c2me-fixes-worldgen-threading-issues.mixins.json")))
        hooks = cast("list[str]", config["mixins"])
        assert len(hooks) == 36
        assert not config.get("server")
        assert not config.get("client")
        package = cast("str", config["package"])
        expected = {(package + "." + name).replace(".", "/") + ".class" for name in hooks}
        expected.add(cast("str", config["plugin"]).replace(".", "/") + ".class")
        expected.add("com/ishland/c2me/fixes/worldgen/threading_issues/ModuleEntryPoint.class")
        captured: set[str] = set()
        for label, identity_digest in (
            ("c2me-worldgen-threading",
             "879eedbffccb03e2ae738fbf1971ab3db075557bce0b4a0126e088c8e9540fe9"),
            ("c2me-threading-boundaries",
             "d5fa087330c5a7c3f210efe1e2cb06debcff3447009f470a6cdcaa1b2b6c2174"),
        ):
            directory = Path("evidence/item-8/sources") / label
            raw = (directory / "identities.json").read_bytes()
            assert hashlib.sha256(raw).hexdigest() == identity_digest
            for row in cast("list[dict[str, str]]", json.loads(raw)):
                captured.add(row["class"])
                assert row["archive"] == source.name + "!/" + member
                assert row["archive_sha256"] == digest
                assert row["class_sha256"] == hashlib.sha256(archive.read(row["class"])).hexdigest()
                assert row["disassembly_sha256"] == hashlib.sha256(
                    (directory / row["disassembly"]).read_bytes()).hexdigest()
        assert expected <= captured
        assert len(captured) == 43
