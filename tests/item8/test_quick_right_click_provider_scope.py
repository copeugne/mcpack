from __future__ import annotations

import hashlib
import json
import tomllib
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources


def test_quick_right_click_membership_payload() -> None:
    sources = {s.name: s for s in retained_sources(Path.cwd())}
    source = sources["quickrightclick-1.21.1-1.9.jar"]
    assert source.sha256 == "b9a6e5f5dfd562ee2302899019ea2b65de1f23422a4f4a4cc5e1603d9de075bd"
    assert hashlib.sha256(source.path.read_bytes()).hexdigest() == source.sha256
    entry = "com/natamus/quickrightclick/ModNeoForge.class"
    prefix = "com/natamus/quickrightclick_common_neoforge/"
    plugin = "com/natamus/collective/neoforge/mixin/plugin/NeoForgeMixinConfigPlugin.class"
    with ZipFile(source.path) as archive:
        files = {n for n in archive.namelist() if not n.endswith("/")}
        classes = {n for n in files if n.endswith(".class")}
        assert len(classes) == 79
        assert files - classes == {
            "META-INF/MANIFEST.MF", "META-INF/mods.toml", "META-INF/neoforge.mods.toml",
            "quickrightclick_forge.mixins.json", "quickrightclick_fabric.mixins.json",
            "quickrightclick_fabric.refmap.json", "quickrightclick_neoforge.mixins.json",
            "pack.mcmeta", "icon.png", "fabric.mod.json"}
        metadata = tomllib.loads(archive.read("META-INF/neoforge.mods.toml").decode())
        assert metadata["modLoader"] == "javafml"
        assert metadata["mixins"] == [{"config": "quickrightclick_neoforge.mixins.json"}]
        config = cast("dict[str, object]",
                      json.loads(archive.read("quickrightclick_neoforge.mixins.json")))
        assert config["package"] == "com.natamus.quickrightclick_common_neoforge.mixin"
        assert config["plugin"] == plugin.removesuffix(".class").replace("/", ".")
        assert not any(config.get(k) for k in ("client", "server"))
        assert set(cast("list[str]", config["mixins"])) == {
            "LivingEntityMixin", "ServerPlayerMixin", "ShulkerBoxBlockEntityMixin"}
        assert {n for n in classes if any(marker in archive.read(n) for marker in (
            b"Lnet/neoforged/fml/common/Mod;", b"Lnet/neoforged/fml/common/EventBusSubscriber;",
        ))} == {entry}
    expected = {entry, "com/natamus/quickrightclick/neoforge/events/NeoForgeQuickEvent.class"}
    expected.update(prefix + n + ".class" for n in (
        "ModCommon", "events/QuickEvent", "mixin/LivingEntityMixin",
        "mixin/ServerPlayerMixin", "mixin/ShulkerBoxBlockEntityMixin",
        "features/BedBlockFeature", "features/ShulkerBoxFeature", "util/Util"))
    expected.add(plugin)
    collective = sources["collective-1.21.1-8.25.jar"]
    assert collective.sha256 == "f66daf378f7a6747ac3b8e601d62ff571fc9f7f2d11b9fb6fae69de33b39f62e"
    assert hashlib.sha256(collective.path.read_bytes()).hexdigest() == collective.sha256
    captured: set[str] = set()
    for label, digest in (
        ("quick-right-click-provider",
         "4f9724746eeee02ac4eca0bf9fd2971528211b78efd60f550bfcc3325f129649"),
        ("quick-right-click-placement",
         "b38d77a4eb459495d5a4addd2db144d784a797d69ac40996e7dc830b6c7484dd"),
        ("collective-mixin-plugin",
         "17633f917be4a00d30225d1efbb2f7b7a2e7ccd5237e3db2e1a5d4fa623b3e14"),
    ):
        directory = Path("evidence/item-8/sources") / label
        raw = (directory / "identities.json").read_bytes()
        assert hashlib.sha256(raw).hexdigest() == digest
        for row in cast("list[dict[str, str]]", json.loads(raw)):
            captured.add(row["class"])
            expected_source = collective if row["class"] == plugin else source
            assert row["archive"] == expected_source.name
            assert row["archive_sha256"] == expected_source.sha256
            with ZipFile(expected_source.path) as archive:
                assert row["class_sha256"] == hashlib.sha256(archive.read(row["class"])).hexdigest()
            assert row["disassembly_sha256"] == hashlib.sha256(
                (directory / row["disassembly"]).read_bytes()).hexdigest()
    assert captured == expected
