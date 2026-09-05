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
        "bettervillage-neoforge-1.21.1-3.3.1.jar",
        "regions-unexplored-0.6.1-neoforge-21.1.jar",
        "YungsBetterDesertTemples-1.21.1-NeoForge-4.1.5.jar",
        "YungsBetterJungleTemples-1.21.1-NeoForge-3.1.2.jar",
        "YungsBetterNetherFortresses-1.21.1-NeoForge-3.1.5.jar",
        "YungsBetterOceanMonuments-1.21.1-NeoForge-4.1.2.jar",
        "YungsBetterStrongholds-1.21.1-NeoForge-5.1.3.jar",
        "YungsBetterWitchHuts-1.21.1-NeoForge-4.1.1.jar",
        "integrated_villages-1.3.3+1.21.1-neoforge.jar",
        "idas-1.13.7+1.21.1-neoforge.jar",
        "BetterEnd-21.0.31.jar",
        "YungsBridges-1.21.1-NeoForge-5.1.1.jar",
    }
)
GENERATION_PREFIXES = (
    "com/jtorleonstudios/bettervillage/",
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
    "net/minecraft/world/level/block/entity/trialspawner/TrialSpawner.class",
    "net/minecraft/world/level/block/entity/trialspawner/TrialSpawnerConfig.class",
    "net/minecraft/world/level/block/entity/trialspawner/TrialSpawnerData.class",
    "net/minecraft/world/level/block/entity/trialspawner/TrialSpawnerState.class",
    "net/minecraft/world/level/levelgen/structure/structures/EndCityStructure.class",
    "net/minecraft/world/level/levelgen/structure/structures/EndCityPieces.class",
    "net/minecraft/world/level/levelgen/structure/structures/EndCityPieces$EndCityPiece.class",
    "net/minecraft/world/level/levelgen/structure/structures/EndCityPieces$SectionGenerator.class",
    "net/minecraft/world/level/levelgen/structure/structures/EndCityPieces$1.class",
    "net/minecraft/world/level/levelgen/structure/structures/EndCityPieces$2.class",
    "net/minecraft/world/level/levelgen/structure/structures/EndCityPieces$3.class",
    "net/minecraft/world/level/levelgen/structure/structures/EndCityPieces$4.class",
    "net/minecraft/world/level/storage/loot/BuiltInLootTables.class",
    "net/minecraft/world/level/levelgen/structure/structures/ShipwreckStructure.class",
    "net/minecraft/world/level/levelgen/structure/structures/ShipwreckPieces.class",
    "net/minecraft/world/level/levelgen/structure/structures/ShipwreckPieces$ShipwreckPiece.class",
    "net/minecraft/world/level/levelgen/structure/structures/IglooStructure.class",
    "net/minecraft/world/level/levelgen/structure/structures/IglooPieces.class",
    "net/minecraft/world/level/levelgen/structure/structures/IglooPieces$IglooPiece.class",
    "net/minecraft/world/level/levelgen/structure/structures/NetherFossilStructure.class",
    "net/minecraft/world/level/levelgen/structure/structures/NetherFossilPieces.class",
    "net/minecraft/world/level/levelgen/structure/structures/NetherFossilPieces$NetherFossilPiece.class",
    "net/minecraft/world/level/levelgen/structure/structures/OceanRuinStructure.class",
    "net/minecraft/world/level/levelgen/structure/structures/OceanRuinStructure$Type.class",
    "net/minecraft/world/level/levelgen/structure/structures/OceanRuinPieces.class",
    "net/minecraft/world/level/levelgen/structure/structures/OceanRuinPieces$OceanRuinPiece.class",
    "net/minecraft/world/level/levelgen/structure/structures/OceanRuinPieces$1.class",
    "net/minecraft/world/level/levelgen/structure/structures/RuinedPortalStructure.class",
    "net/minecraft/world/level/levelgen/structure/structures/RuinedPortalStructure$Setup.class",
    "net/minecraft/world/level/levelgen/structure/structures/RuinedPortalPiece.class",
    "net/minecraft/world/level/levelgen/structure/structures/RuinedPortalPiece$Properties.class",
    "net/minecraft/world/level/levelgen/structure/structures/RuinedPortalPiece$VerticalPlacement.class",
    "net/minecraft/world/level/levelgen/structure/structures/BuriedTreasureStructure.class",
    "net/minecraft/world/level/levelgen/structure/structures/BuriedTreasurePieces.class",
    "net/minecraft/world/level/levelgen/structure/structures/BuriedTreasurePieces$BuriedTreasurePiece.class",
    "net/minecraft/world/level/levelgen/structure/structures/SwampHutStructure.class",
    "net/minecraft/world/level/levelgen/structure/structures/SwampHutPiece.class",
    "net/minecraft/world/level/levelgen/structure/ScatteredFeaturePiece.class",
    "net/minecraft/world/level/levelgen/structure/structures/DesertPyramidStructure.class",
    "net/minecraft/world/level/levelgen/structure/structures/DesertPyramidPiece.class",
    "net/minecraft/world/level/levelgen/structure/SinglePieceStructure.class",
    "net/minecraft/world/level/levelgen/structure/structures/JungleTempleStructure.class",
    "net/minecraft/world/level/levelgen/structure/structures/JungleTemplePiece.class",
    "net/minecraft/world/level/levelgen/structure/structures/JungleTemplePiece$MossStoneSelector.class",
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
    "com/yungnickyoung/minecraft/betterdeserttemples/mixin/DisableVanillaPyramidsMixin.class",
    "com/yungnickyoung/minecraft/betterdeserttemples/module/ConfigModuleNeoForge.class",
    "com/yungnickyoung/minecraft/betterdeserttemples/config/ConfigGeneralNeoForge.class",
    "com/yungnickyoung/minecraft/betterjungletemples/mixin/DisableVanillaJungleTempleMixin.class",
    "com/yungnickyoung/minecraft/betterjungletemples/module/ConfigModuleNeoForge.class",
    "com/yungnickyoung/minecraft/betterjungletemples/config/ConfigGeneralNeoForge.class",
    "com/yungnickyoung/minecraft/betterfortresses/mixin/DisableVanillaFortressesMixin.class",
    "com/yungnickyoung/minecraft/betterfortresses/module/ConfigModuleNeoForge.class",
    "com/yungnickyoung/minecraft/betterfortresses/config/ConfigGeneralNeoForge.class",
    "com/yungnickyoung/minecraft/betteroceanmonuments/mixin/DisableVanillaMonumentsMixin.class",
    "com/yungnickyoung/minecraft/betteroceanmonuments/module/ConfigModuleNeoForge.class",
    "com/yungnickyoung/minecraft/betteroceanmonuments/config/ConfigGeneralForge.class",
    "com/yungnickyoung/minecraft/betterstrongholds/mixin/DisableVanillaStrongholdsMixin.class",
    "com/yungnickyoung/minecraft/betterwitchhuts/mixin/DisableVanillaWitchHutsMixin.class",
    "com/yungnickyoung/minecraft/betterwitchhuts/module/ConfigModuleNeoForge.class",
    "com/yungnickyoung/minecraft/betterwitchhuts/config/ConfigGeneralNeoForge.class",
    "LocateVanillaMineshaftCommandMixin.class",
    "com/craisinlord/integrated_villages/mixins/DisableVanillaVillagesMixin.class",
    "com/craisinlord/integrated_villages/config/ConfigGeneralNeoforge.class",
    "com/craisinlord/integrated_villages/config/ConfigModuleNeoforge.class",
    "com/craisinlord/idas/mixins/DisableStructuresMixin.class",
    "com/craisinlord/idas/config/ConfigGeneralNeoforge.class",
    "com/craisinlord/idas/config/ConfigModuleNeoforge.class",
    "dev/worldgen/lithostitched/impl/worldgen/modifier/ModifierManager.class",
    "dev/worldgen/lithostitched/api/worldgen/modifier/WorldgenModifier.class",
    "net/minecraft/resources/RegistryDataLoader.class",
    "net/neoforged/neoforge/common/conditions/ConditionalOps.class",
    "net/neoforged/neoforge/server/command/DumpCommand.class",
    "net/neoforged/neoforge/common/conditions/ConditionalOps$ConditionalDecoder.class",
    "net/neoforged/neoforge/common/conditions/ModLoadedCondition.class",
    "net/neoforged/neoforge/common/conditions/OrCondition.class",
    "dev/worldgen/lithostitched/worldgen/modifier/SetPoolAliasesModifier.class",
    "dev/worldgen/lithostitched/worldgen/poolalias/RandomEntries.class",
    "dev/worldgen/lithostitched/mixin/common/PoolAliasLookupMixin.class",
    "dev/worldgen/lithostitched/worldgen/modifier/internal/CompileRawTemplatesModifier.class",
    "dev/worldgen/lithostitched/mixin/common/StructureTemplatePoolMixin.class",
    "dev/worldgen/lithostitched/worldgen/structure/LithostitchedTemplates.class",
    "dev/worldgen/lithostitched/worldgen/structure/LithostitchedTemplates$WeightedEntry.class",
    "dev/worldgen/lithostitched/api/worldgen/processor/LithostitchedProcessors.class",
    "dev/worldgen/lithostitched/impl/LithostitchedVersion.class",
    "dev/worldgen/lithostitched/worldgen/modifier/AddProcessorListProcessorsModifier.class",
    "dev/worldgen/lithostitched/impl/worldgen/processor/ReferenceStructureProcessor.class",
    "dev/worldgen/lithostitched/impl/worldgen/processor/ConditionProcessor.class",
    "dev/worldgen/lithostitched/impl/worldgen/processor/BlockSwapStructureProcessor.class",
    "dev/worldgen/lithostitched/impl/worldgen/modifier/AddFeaturesModifier.class",
    "dev/worldgen/lithostitched/impl/worldgen/modifier/RemoveFeaturesModifier.class",
    "dev/worldgen/lithostitched/impl/worldgen/surface/rule/ReferenceRule.class",
    "dev/worldgen/lithostitched/worldgen/feature/CompositeFeature.class",
    "dev/worldgen/lithostitched/worldgen/feature/WeightedSelectorFeature.class",
    "dev/worldgen/lithostitched/worldgen/feature/config/WeightedSelectorConfig.class",
    "dev/worldgen/lithostitched/worldgen/modifier/AddSurfaceRuleModifier.class",
    "dev/worldgen/lithostitched/mixin/common/ServerLifecycleHooksMixin.class",
    "dev/worldgen/lithostitched/impl/worldgen/modifier/NeoforgeModifierHolder.class",
    "dev/worldgen/lithostitched/worldgen/surface/SurfaceRuleManager.class",
    "dev/worldgen/lithostitched/worldgen/stateprovider/RandomBlockProvider.class",
    "dev/worldgen/lithostitched/impl/LithostitchedInternalHooks.class",
    "dev/worldgen/lithostitched/mixin/server/DedicatedServerMixin.class",
    "dev/worldgen/lithostitched/impl/worldgen/surface/rule/TransientMergedRule.class",
    "dev/worldgen/lithostitched/impl/worldgen/biomeinjector/internal/InjectorBiomeSource.class",
    "dev/worldgen/lithostitched/impl/worldgen/biomeinjector/internal/BiomeInjectorManager.class",
    "dev/worldgen/lithostitched/api/worldgen/biomeinjector/BiomeInjector.class",
    "net/regions_unexplored/registry/RUFeatureTypes.class",
    "net/regions_unexplored/world/level/feature/GiantLilyPadFeature.class",
    "net/regions_unexplored/world/level/feature/tree/BambooTreeFeature.class",
    "net/regions_unexplored/world/level/feature/tree/PalmTreeFeature.class",
    "net/regions_unexplored/world/level/feature/tree/SaguaroCactusFeature.class",
    "net/regions_unexplored/worldgen/rootplacer/WillowRootPlacer.class",
    "net/regions_unexplored/worldgen/rulesource/ConfigRuleSource.class",
    "net/regions_unexplored/lithostitched/ConfigPredicate.class",
    "net/regions_unexplored/config/state/common/RUCommonConfig.class",
    "net/regions_unexplored/worldgen/stateprovider/RandomizedGroundCoverStateProvider.class",
    "org/betterx/betterend/registry/EndStructures.class",
    "org/betterx/betterend/world/structures/features/FeatureBaseStructure.class",
    "org/betterx/betterend/world/structures/features/EndLakeStructure.class",
    "org/betterx/betterend/world/structures/features/EndLakeNormalStructure.class",
    "org/betterx/betterend/world/structures/features/EndLakeRareStructure.class",
    "org/betterx/betterend/world/structures/features/MegaLakeStructure.class",
    "org/betterx/betterend/world/structures/features/MegaLakeSmallStructure.class",
    "org/betterx/betterend/world/structures/features/MountainStructure.class",
    "org/betterx/betterend/world/structures/features/PaintedMountainStructure.class",
    "org/betterx/betterend/world/structures/piece/BasePiece.class",
    "org/betterx/betterend/world/structures/piece/EndLakePiece.class",
    "org/betterx/betterend/world/structures/piece/LakePiece.class",
    "org/betterx/betterend/world/structures/piece/MountainPiece.class",
    "org/betterx/betterend/world/structures/piece/CrystalMountainPiece.class",
    "org/betterx/betterend/world/structures/piece/PaintedMountainPiece.class",
    "org/betterx/betterend/world/biome/EndBiome.class",
    "org/betterx/betterend/util/BlockFixer.class",
    "com/yungnickyoung/minecraft/yungsbridges/world/feature/AbstractTemplateFeature.class",
    "com/yungnickyoung/minecraft/yungsbridges/world/feature/BridgeFeature.class",
    "com/yungnickyoung/minecraft/yungsbridges/world/feature/MultipleAttemptSingleRandomFeature.class",
    "com/yungnickyoung/minecraft/yungsbridges/world/feature/config/BridgeFeatureConfig.class",
    "com/yungnickyoung/minecraft/yungsbridges/world/placement/BridgePlacement.class",
    "com/yungnickyoung/minecraft/yungsbridges/world/placement/RngInitializerPlacement.class",
    "com/yungnickyoung/minecraft/yungsbridges/YungsBridgesCommon.class",
    "com/yungnickyoung/minecraft/yungsbridges/YungsBridgesNeoForge.class",
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
    _ = parser.add_argument("--class-name", action="append", choices=CLASSES)
    args = parser.parse_args()
    output = cast("Path", args.output)
    selected_archive = cast("str | None", args.archive)
    selected_classes = cast("list[str] | None", args.class_name)
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
            if source.name.startswith("YungsBetter") or source.name in {
                "integrated_villages-1.3.3+1.21.1-neoforge.jar",
                "idas-1.13.7+1.21.1-neoforge.jar",
            }:
                metadata = {
                    name: {
                        "sha256": hashlib.sha256(archive.read(name)).hexdigest(),
                        "text": archive.read(name).decode("utf-8"),
                    }
                    for name in (
                        *sorted(n for n in archive.namelist() if n.endswith(".mixins.json")),
                        "META-INF/neoforge.mods.toml",
                    )
                }
                _ = (destination / "mixin-metadata.json").write_text(
                    json.dumps(metadata, indent=2) + "\n", encoding="utf-8"
                )
            for name in sorted(archive.namelist()):
                if not name.endswith(".class") or (
                    selected_classes is not None and name not in selected_classes
                ):
                    continue
                if source.name == MAPPED_SERVER.name and name not in CLASSES[:48]:
                    continue
                if (
                    source.name == PATCHED_SERVER.name
                    and name != "net/minecraft/resources/RegistryDataLoader.class"
                ) or (
                    source.name == "neoforge-21.1.249-universal.jar" and name not in CLASSES
                ):
                    continue
                payload = archive.read(name)
                if (
                    not name.startswith(GENERATION_PREFIXES)
                    and not name.endswith(CLASSES)
                    and not any(key in payload for key in REGISTRATION_KEYS)
                ):
                    continue
                class_name = name.removesuffix(".class").replace("/", ".")
                verbose = "/mixin/" in name or "/mixins/" in name or name in {
                    CLASSES[0],
                    "org/betterx/betterend/registry/EndStructures.class",
                    "net/minecraft/world/level/levelgen/structure/structures/DesertPyramidStructure.class",
                    "net/minecraft/world/level/levelgen/structure/structures/JungleTempleStructure.class",
                    "net/minecraft/world/level/levelgen/structure/structures/EndCityPieces$EndCityPiece.class",
                }
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
