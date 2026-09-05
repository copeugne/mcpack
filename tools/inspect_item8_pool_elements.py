"""Inspect pool codecs and generation with uv run -m tools.inspect_item8_pool_elements."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item7_restriction_inputs import ArchiveInput
from mcpack_evidence.item8_sources import retained_sources

ROOT = Path(__file__).resolve().parents[1]
MAPPED_SERVER = ArchiveInput(
    "server-1.21.1-20240808.144430-srg.jar",
    ROOT
    / "instances/pristine-baseline-v0/libraries/net/minecraft/server"
    / "1.21.1-20240808.144430/server-1.21.1-20240808.144430-srg.jar",
    "26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71",
)
PATCHED_SERVER = ArchiveInput(
    "neoforge-21.1.249-server.jar",
    ROOT
    / "instances/pristine-baseline-v0/libraries/net/neoforged/neoforge"
    / "21.1.249/neoforge-21.1.249-server.jar",
    "1808fab692dc44b2d474295d1cdd9f1fe8a7dceab4f594210873646fafdf1359",
)
ARCHIVES = frozenset(
    {
        MAPPED_SERVER.name,
        PATCHED_SERVER.name,
        "neoforge-21.1.249-universal.jar",
        "YungsApi-1.21.1-NeoForge-5.1.6.jar",
        "integrated_api-1.7.3+1.21.1-neoforge.jar",
        "moogs_structures-neoforge-1.21.1-alpha-3.0.0.jar",
        "IllagerInvasion-v21.1.6-1.21.1-NeoForge.jar",
        "repurposed_structures-7.5.21+1.21.1-neoforge.jar",
        "worldweaver-21.0.24.jar",
        "lithostitched-1.7.10+beta4-neoforge-21.1.jar",
        "YungsBetterMineshafts-1.21.1-NeoForge-5.1.1.jar",
        "YungsBetterDungeons-1.21.1-NeoForge-5.1.4.jar",
        "supplementaries-neoforge-1.21.1-3.6.8.jar",
    }
)
GENERATION_PREFIXES = (
    "com/finndog/moogs_structures/world/structures/GenericJigsawStructure",
    "com/finndog/moogs_structures/world/structures/GenericNetherJigsawStructure",
    "com/finndog/moogs_structures/world/structures/codecs/YRangeAllowance",
    "com/yungnickyoung/minecraft/betterdungeons/world/structure/spider_dungeon/",
    "com/yungnickyoung/minecraft/betterdungeons/world/structure/SmallNetherDungeonStructure",
    "com/yungnickyoung/minecraft/bettermineshafts/world/",
    "com/yungnickyoung/minecraft/bettermineshafts/config/",
    "com/yungnickyoung/minecraft/bettermineshafts/module/ConfigModule",
    "com/yungnickyoung/minecraft/bettermineshafts/module/StructureTypeModule",
    "net/mehvahdjukaar/supplementaries/dynamicpack/ModServerDynamicResources",
    "net/mehvahdjukaar/supplementaries/reg/ModTags",
    "net/mehvahdjukaar/supplementaries/configs/CommonConfigs$Building",
    "net/mehvahdjukaar/supplementaries/configs/CommonConfigs$Functional",
)
CLASSES = (
    "net/minecraft/world/level/levelgen/structure/pools/SinglePoolElement.class",
    "net/minecraft/world/level/levelgen/structure/pools/JigsawPlacement$Placer.class",
    "net/minecraft/world/level/levelgen/structure/templatesystem/StructureTemplateManager.class",
    "net/minecraft/world/level/levelgen/structure/templatesystem/StructureTemplate.class",
    "net/mehvahdjukaar/supplementaries/configs/CommonConfigs.class",
    "YungJigsawSinglePoolElement.class",
    "IASinglePoolElement.class",
    "VersionAwareSinglePoolElement.class",
    "VersionResolver.class",
    "VersionResolver$VersionRange.class",
    "VersionResolver$VersionEntry.class",
    "VersionResolver$VersionNumber.class",
    "MirroringSingleJigsawPiece.class",
    "SingleNoLiquidPoolElement.class",
    "LegacySingleNoLiquidPoolElement.class",
    "LegacyOceanBottomSinglePoolElement.class",
    "SingleEndPoolElement.class",
    "BreaksSeedParityCondition.class",
    "dev/worldgen/lithostitched/worldgen/poolelement/legacy/LimitedPoolElement.class",
    "dev/worldgen/lithostitched/worldgen/poolelement/DelegatingPoolElement.class",
    "dev/worldgen/lithostitched/worldgen/modifier/AddTemplatePoolElementsModifier.class",
    "DisableVanillaMineshaftsMixin.class",
    "LocateVanillaMineshaftCommandMixin.class",
    "dev/worldgen/lithostitched/impl/worldgen/modifier/ModifierManager.class",
    "dev/worldgen/lithostitched/api/worldgen/modifier/WorldgenModifier.class",
    "net/minecraft/resources/RegistryDataLoader.class",
    "net/neoforged/neoforge/common/conditions/ConditionalOps.class",
    "net/neoforged/neoforge/common/conditions/ConditionalOps$ConditionalDecoder.class",
    "net/neoforged/neoforge/common/conditions/ModLoadedCondition.class",
    "net/neoforged/neoforge/common/conditions/OrCondition.class",
)
REGISTRATION_KEYS = (
    b"yung_single_element",
    b"integrated_api_single_pool_element",
    b"versioned_single_pool_element",
    b"mirroring_single_pool_element",
    b"single_end_pool_element",
    b"legacy_ocean_bottom_single_pool_element",
    b"single_pool_element",
    b"breaks_seed_parity",
)


def main() -> None:  # noqa: C901 - explicit archive selection and portable verbose output.
    """Retain disassembly and exact class/archive identities for the observed custom types."""
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("--output", type=Path, required=True)
    _ = parser.add_argument("--archive", choices=sorted(ARCHIVES))
    args = parser.parse_args()
    output = cast("Path", args.output)
    selected_archive = cast("str | None", args.archive)
    output.mkdir(parents=True, exist_ok=False)
    javap = ROOT / "downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap"
    identities: list[dict[str, str]] = []
    for source in (*retained_sources(ROOT), MAPPED_SERVER, PATCHED_SERVER):
        if source.name not in ARCHIVES:
            continue
        if selected_archive is not None and source.name != selected_archive:
            continue
        if hashlib.sha256(source.path.read_bytes()).hexdigest() != source.sha256:
            message = f"custom pool source hash mismatch: {source.name}"
            raise ValueError(message)
        destination = output / source.name
        destination.mkdir()
        with ZipFile(source.path) as archive:
            if source.name == "YungsBetterMineshafts-1.21.1-NeoForge-5.1.1.jar":
                metadata = {
                    name: {
                        "sha256": hashlib.sha256(archive.read(name)).hexdigest(),
                        "text": archive.read(name).decode("utf-8"),
                    }
                    for name in ("bettermineshafts.mixins.json", "META-INF/neoforge.mods.toml")
                }
                _ = (destination / "mixin-metadata.json").write_text(
                    json.dumps(metadata, indent=2) + "\n", encoding="utf-8"
                )
            for name in sorted(archive.namelist()):
                if not name.endswith(".class"):
                    continue
                if source.name == MAPPED_SERVER.name and name not in CLASSES[:4]:
                    continue
                if source.name in {
                    PATCHED_SERVER.name, "neoforge-21.1.249-universal.jar"
                } and name not in CLASSES:
                    continue
                payload = archive.read(name)
                if (
                    not name.startswith(GENERATION_PREFIXES)
                    and not name.endswith(CLASSES)
                    and not any(key in payload for key in REGISTRATION_KEYS)
                ):
                    continue
                class_name = name.removesuffix(".class").replace("/", ".")
                verbose = "/mixin/" in name or name == CLASSES[0]
                result = subprocess.run(  # noqa: S603 - pinned javap and verified retained JAR.
                    [
                        str(javap),
                        "-p",
                        "-c",
                        "-constants",
                        *(["-v"] if verbose else []),
                        "-classpath",
                        str(source.path),
                        class_name,
                    ],
                    check=True,
                    capture_output=True,
                )
                disassembly = result.stdout
                if verbose:
                    if not disassembly.startswith(b"Classfile "):
                        message = f"verbose javap lacks expected classfile header: {name}"
                        raise ValueError(message)
                    # Preserve archive/member identity without publishing a local host path.
                    disassembly = (
                        f"Classfile {source.name}!/{name}\n".encode()
                        + disassembly.partition(b"\n")[2]
                    )
                target = destination / f"{class_name}.txt"
                _ = target.write_bytes(disassembly)
                identities.append(
                    {
                        "archive": source.name,
                        "archive_sha256": source.sha256,
                        "class": name,
                        "class_sha256": hashlib.sha256(payload).hexdigest(),
                        "disassembly": target.relative_to(output).as_posix(),
                        "disassembly_sha256": hashlib.sha256(disassembly).hexdigest(),
                    }
                )
    _ = (output / "identities.json").write_text(
        json.dumps(identities, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
