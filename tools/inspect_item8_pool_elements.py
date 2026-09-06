"""Inspect pool codecs and generation with uv run -m tools.inspect_item8_pool_elements."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from contextlib import ExitStack
from pathlib import Path
from tempfile import NamedTemporaryFile
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
        "Zeta-1.1-40.jar",
        "Quark-4.1-480.jar",
        "explorations-neoforge-1.21.1-1.6.2.jar",
        "integrated_api-1.7.3+1.21.1-neoforge.jar",
        "moogs_structures-neoforge-1.21.1-alpha-3.0.0.jar",
        "IllagerInvasion-v21.1.6-1.21.1-NeoForge.jar",
        "repurposed_structures-7.5.21+1.21.1-neoforge.jar",
        "aether-1.21.1-1.5.10-neoforge.jar",
        "chefsdelight-1.0.5-neoforge-1.21.1.jar",
        "village_taverns-neoforge-1.1.5+1.21.1.jar",
        "DungeonsAriseSevenSeas-1.21.x-1.0.4-neoforge.jar",
        "DungeonsArise-1.21.1-2.1.68-release.jar",
        "t_and_t-neoforge-fabric-1.13.9+1.21.1.jar",
        "mcw-doors-1.1.5-mc1.21.1neoforge.jar",
        "mcw-lights-1.1.5-mc1.21.1neoforge.jar",
        "mcw-mcwfences-1.2.1-mc1.21.1neoforge.jar",
        "mcw-mcwpaths-1.1.1-mc1.21.1neoforge.jar",
        "mcw-mcwstairs-1.0.2-mc1.21.1neoforge.jar",
        "mcw-mcwwindows-2.4.2-mc1.21.1neoforge.jar",
        "mcw-paintings-1.1.0-mc1.21.1neoforge.jar",
        "mcw-roofs-2.3.2-mc1.21.1neoforge.jar",
        "mcw-trapdoors-1.1.5-mc1.21.1neoforge.jar",
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
        "integrated_stronghold-1.1.4+1.21.1-neoforge.jar",
        "adorabuild-structures-2.11.0-neoforge-1.21.3.jar",
        "[Neoforge]ctov-3.6.3.jar",
        "AI-Improvements-1.21-0.5.3.jar",
        "Almanac-1.21.1-2-neoforge-1.5.2.jar",
        "libraryferret-neoforge-1.21.1-4.0.0.jar",
        "structure_layout_optimizer-neoforge-1.0.12.jar",
        "attributefix-neoforge-1.21.1-21.1.3.jar",
        "LeavesBeGone-v21.1.1-1.21.1-NeoForge.jar",
        "letmedespawn-1.21.x-neoforge-1.5.0.jar",
        "sparsestructures-neoforge-1.21.1-3.0.jar",
        "structure_pool_api-neoforge-1.2.1+1.21.1.jar",
        "idas-1.13.7+1.21.1-neoforge.jar",
        "BetterEnd-21.0.31.jar",
        "BiomesOPlenty-neoforge-1.21.1-21.1.0.13.jar",
        "deep_aether-1.21.1-1.1.5.1.jar",
        "YungsBridges-1.21.1-NeoForge-5.1.1.jar",
        "YungsExtras-1.21.1-NeoForge-5.1.1.jar",
        "YungsBetterEndIsland-1.21.1-NeoForge-3.1.2.jar",
    }
)
GENERATION_PREFIXES = (
    "com/frikinjay/almanac/",
    "architectury_inject_almanac_",
    "com/jtorleonstudios/libraryferret/",
    "telepathicgrunt/structure_layout_optimizer/",
    "com/builtbroken/ai/improvements/",
    "net/darkhax/attributefix/",
    "fuzs/leavesbegone/",
    "architectury_inject_LeavesBeGone",
    "com/frikinjay/letmedespawn/",
    "architectury_inject_letmedespawn_",
    "io/github/maxencedc/sparsestructures/",
    "net/fabric_extras/structure_pool/",
    "architectury_inject_structure_pool_api_",
    "net/choicetheorem/ctov/",
    "architectury_inject_ChoiceTheoremsoverhauledvillage_common_",
    "net/adorabuild/structures/",
    "com/craisinlord/integrated_stronghold/",
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
CLASSES: tuple[str, ...] = (
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
    "com/yungnickyoung/minecraft/yungsbridges/module/FeatureProcessorModule.class",
    "com/yungnickyoung/minecraft/yungsbridges/world/processor/ITemplateFeatureProcessor.class",
    "com/yungnickyoung/minecraft/yungsbridges/world/processor/DynamicLegProcessor.class",
    "com/yungnickyoung/minecraft/yungsbridges/world/processor/FenceBiomeProcessor.class",
    "com/yungnickyoung/minecraft/yungsbridges/world/processor/LanternRotProcessor.class",
    "com/yungnickyoung/minecraft/yungsbridges/world/processor/LogBiomeProcessor.class",
    "com/yungnickyoung/minecraft/yungsbridges/world/processor/OptionalBlockProcessor.class",
    "com/yungnickyoung/minecraft/yungsbridges/world/processor/OptionalSlabProcessor.class",
    "com/yungnickyoung/minecraft/yungsbridges/world/processor/OptionalStairProcessor.class",
    "com/yungnickyoung/minecraft/yungsbridges/world/processor/OptionalWallProcessor.class",
    "com/yungnickyoung/minecraft/yungsbridges/world/processor/PlanksBiomeProcessor.class",
    "com/yungnickyoung/minecraft/yungsbridges/world/processor/SlabBiomeProcessor.class",
    "com/yungnickyoung/minecraft/yungsbridges/world/processor/StairBiomeProcessor.class",
    "com/yungnickyoung/minecraft/yungsbridges/world/processor/StoneVariationProcessor.class",
    "com/yungnickyoung/minecraft/yungsextras/module/FeatureModule.class",
    "com/yungnickyoung/minecraft/yungsextras/world/feature/AbstractNbtFeature.class",
    "com/yungnickyoung/minecraft/yungsextras/world/feature/desert/ChillzoneDesertFeature.class",
    "com/yungnickyoung/minecraft/yungsextras/world/feature/desert/DesertGiantTorchFeature.class",
    "com/yungnickyoung/minecraft/yungsextras/world/feature/desert/DesertSmallRuinsFeature.class",
    "com/yungnickyoung/minecraft/yungsextras/world/feature/desert/DesertObeliskFeature.class",
    "com/yungnickyoung/minecraft/yungsextras/world/feature/desert/DesertWellFeature.class",
    "com/yungnickyoung/minecraft/yungsextras/world/feature/swamp/AbstractSwampFeature.class",
    "com/yungnickyoung/minecraft/yungsextras/world/feature/swamp/SwampArchFeature.class",
    "com/yungnickyoung/minecraft/yungsextras/world/feature/swamp/SwampChurchFeature.class",
    "com/yungnickyoung/minecraft/yungsextras/world/feature/swamp/SwampCubbyFeature.class",
    "com/yungnickyoung/minecraft/yungsextras/world/feature/swamp/SwampDoubleArchFeature.class",
    "com/yungnickyoung/minecraft/yungsextras/world/feature/swamp/SwampOgreFeature.class",
    "com/yungnickyoung/minecraft/yungsextras/world/feature/swamp/SwampPillarFeature.class",
    "com/yungnickyoung/minecraft/yungsextras/world/processor/DesertWellProcessor.class",
    "com/yungnickyoung/minecraft/yungsextras/world/processor/INbtFeatureProcessor.class",
    "com/yungnickyoung/minecraft/yungsextras/world/processor/SwampFeatureProcessor.class",
    "com/yungnickyoung/minecraft/yungsextras/module/FeatureProcessorModule.class",
    "com/yungnickyoung/minecraft/yungsextras/YungsExtrasCommon.class",
    "com/yungnickyoung/minecraft/yungsextras/YungsExtrasNeoForge.class",
    "com/yungnickyoung/minecraft/yungsextras/services/NeoForgeModulesLoader.class",
    "com/yungnickyoung/minecraft/yungsbridges/services/NeoForgeModulesLoader.class",
    "com/yungnickyoung/minecraft/yungsextras/services/IModulesLoader.class",
    "com/yungnickyoung/minecraft/yungsbridges/services/IModulesLoader.class",
    "com/yungnickyoung/minecraft/betterendisland/mixin/EndPlatformFeatureMixin.class",
    "com/yungnickyoung/minecraft/betterendisland/mixin/EndGatewayFeatureMixin.class",
    "com/yungnickyoung/minecraft/betterendisland/world/feature/BetterEndSpawnPlatformFeature.class",
    "com/yungnickyoung/minecraft/betterendisland/world/feature/BetterEndGatewayFeature.class",
    "com/yungnickyoung/minecraft/betterendisland/world/processor/ObsidianProcessor.class",
    "com/yungnickyoung/minecraft/betterendisland/world/processor/DragonEggProcessor.class",
    "com/yungnickyoung/minecraft/betterendisland/config/BEIConfigNeoForge.class",
    "com/yungnickyoung/minecraft/betterendisland/module/ConfigModule.class",
    "com/yungnickyoung/minecraft/betterendisland/module/ConfigModuleNeoForge.class",
    "com/yungnickyoung/minecraft/betterendisland/mixin/SpikeFeatureMixin.class",
    "com/yungnickyoung/minecraft/betterendisland/world/feature/BetterSpikeFeature.class",
    "com/yungnickyoung/minecraft/betterendisland/world/feature/BetterEndPodiumFeature.class",
    "com/yungnickyoung/minecraft/betterendisland/mixin/EndSpikeMixin.class",
    "com/yungnickyoung/minecraft/betterendisland/mixin/EndDragonFightMixin.class",
    "com/yungnickyoung/minecraft/betterendisland/world/SpikeCacheLoader.class",
    "com/yungnickyoung/minecraft/betterendisland/world/processor/BlockReplaceProcessor.class",
    "com/yungnickyoung/minecraft/betterendisland/BetterEndIslandCommon.class",
    "com/yungnickyoung/minecraft/betterendisland/world/util/ExitPortalUtils.class",
    "com/yungnickyoung/minecraft/betterendisland/world/DragonRespawnStage.class",
    "com/yungnickyoung/minecraft/betterendisland/world/DragonRespawnStage$3.class",
    "com/yungnickyoung/minecraft/betterendisland/world/DragonRespawnStage$5.class",
    "com/yungnickyoung/minecraft/betterendisland/world/util/WorldgenUtils.class",
    "com/yungnickyoung/minecraft/betterendisland/BetterEndIslandNeoForge.class",
    "com/yungnickyoung/minecraft/betterendisland/services/Services.class",
    "com/yungnickyoung/minecraft/betterendisland/services/NeoForgePlatformHelper.class",
    "com/yungnickyoung/minecraft/betterendisland/services/NeoForgeModulesLoader.class",
    "net/minecraft/world/level/levelgen/feature/EndPlatformFeature.class",
    "org/violetmoon/zetaimplforge/world/ZetaBiomeModifier.class",
    "org/violetmoon/zeta/world/WorldGenHandler.class",
    "org/violetmoon/zetaimplforge/world/ZetaSpawnModifier.class",
    "org/violetmoon/zeta/world/DeferredFeature.class",
    "org/violetmoon/quark/content/world/module/ChorusVegetationModule.class",
    "org/violetmoon/quark/content/world/module/SpiralSpiresModule.class",
    "org/violetmoon/quark/content/world/gen/ChorusVegetationGenerator.class",
    "org/violetmoon/quark/content/world/gen/SpiralSpireGenerator.class",
    "org/violetmoon/zeta/world/generator/multichunk/MultiChunkFeatureGenerator.class",
    "org/violetmoon/zeta/config/type/DimensionConfig.class",
    "org/violetmoon/zeta/world/generator/Generator.class",
    "org/violetmoon/zeta/config/type/CompoundBiomeConfig.class",
    "org/violetmoon/zeta/config/type/BiomeTagConfig.class",
    "org/violetmoon/zeta/config/type/StrictBiomeConfig.class",
    "org/violetmoon/zeta/config/ConfigObjectMapper.class",
    "org/violetmoon/zeta/config/ConfigManager.class",
    "org/violetmoon/zetaimplforge/config/ForgeBackedConfig.class",
    "org/violetmoon/zetaimplforge/config/ConfigEventDispatcher.class",
    "org/violetmoon/zeta/module/ZetaModule.class",
    "org/violetmoon/zeta/module/ZetaCategory.class",
    "org/violetmoon/zeta/util/MiscUtil.class",
    "org/violetmoon/quark/base/proxy/CommonProxy.class",
    "org/violetmoon/zetaimplforge/module/ModFileScanDataModuleFinder.class",
    "org/violetmoon/zeta/module/ZetaLoadModuleAnnotationData.class",
    "org/violetmoon/zeta/module/ZetaModuleManager.class",
    "org/violetmoon/zeta/module/TentativeModule.class",
    "org/violetmoon/quark/content/world/module/FallenLogsModule.class",
    "org/violetmoon/quark/content/world/module/FairyRingsModule.class",
    "org/violetmoon/quark/content/world/module/MonsterBoxModule.class",
    "org/violetmoon/quark/content/world/module/NetherObsidianSpikesModule.class",
    "org/violetmoon/quark/content/world/module/CorundumModule.class",
    "org/violetmoon/quark/content/world/module/PermafrostModule.class",
    "org/violetmoon/quark/content/world/module/BlossomTreesModule.class",
    "org/violetmoon/quark/content/world/module/BigStoneClustersModule.class",
    "org/violetmoon/quark/content/world/module/NewStoneTypesModule.class",
    "org/violetmoon/quark/content/experimental/module/VanillaStoneClustersModule.class",
    "org/violetmoon/quark/content/world/gen/BigStoneClusterGenerator.class",
    "org/violetmoon/zeta/world/generator/OreGenerator.class",
    "com/tristankechlo/explorations/worldgen/structures/SlimeCaveStructure.class",
    "com/tristankechlo/explorations/worldgen/structures/pieces/SlimeCaveStructurePiece.class",
    "com/tristankechlo/explorations/worldgen/structures/processors/DeepslateProcessor.class",
    "com/mcwdoors/kikoz/MacawsDoors.class",
    "com/mcwlights/kikoz/MacawsLights.class",
    "com/mcwfences/kikoz/MacawsFences.class",
    "com/mcwpaths/kikoz/MacawsPaths.class",
    "com/mcwstairs/kikoz/MacawsStairs.class",
    "com/mcwwindows/kikoz/MacawsWindows.class",
    "com/mcwpaintings/kikoz/MacawsPaintings.class",
    "com/mcwroofs/kikoz/MacawsRoofs.class",
    "com/mcwtrpdoors/kikoz/MacawsTrapdoors.class",
    "org/betterx/betterend/registry/EndFeatures.class",
    "org/betterx/betterend/world/features/BuildingListFeature.class",
    "org/betterx/betterend/world/features/CrashedShipFeature.class",
    "biomesoplenty/worldgen/feature/misc/AnomalyFeature.class",
    "biomesoplenty/worldgen/feature/misc/MonolithFeature.class",
    "biomesoplenty/worldgen/feature/misc/BoneSpineFeature.class",
    "io/github/razordevs/deep_aether/world/feature/features/TotemFeature.class",
    "com/tristankechlo/explorations/worldgen/features/ScarecrowFeature.class",
    "net/redstonegames/chefsdelight/ChefsDelight.class",
    "net/redstonegames/chefsdelight/ChefsDelight$ClientModEvents.class",
    "net/redstonegames/chefsdelight/Config.class",
    "net/redstonegames/chefsdelight/villager/ModEvents.class",
    "net/redstonegames/chefsdelight/villager/ModVillagers.class",
    "net/redstonegames/chefsdelight/worldgen/village/VillageStructures.class",
    "net/village_taverns/neoforge/NeoForgeMod.class",
    "net/village_taverns/TavernsMod.class",
    "net/village_taverns/TavernVillagers.class",
    "net/village_taverns/config/Defaults.class",
    "net/village_taverns/block/TavernBlocks.class",
    "net/village_taverns/block/TavernBlocks$Entry.class",
    "net/village_taverns/block/BrewTapBlock.class",
    "net/village_taverns/block/BrewTapBlock$1.class",
    "net/village_taverns/client/TavernsModClient.class",
    "net/village_taverns/compat/RangedWeaponCompat.class",
    "net/village_taverns/compat/SpellPowerCompat.class",
    "net/village_taverns/neoforge/client/NeoForgeClientMod.class",
    "architectury_inject_village_taverns_common_9feb1bb9f94a4fa08c0c87b571be378b_a8fac20701f86f005801059a650cef1ec65724e970fe2c13ffa0269f8465b11bvillage_tavernscommon1151211devjar/PlatformMethods.class",
    "net/tiny_config/neoforge/ExampleModNeoForge.class",
    "net/tiny_config/ExampleMod.class",
    "net/tiny_config/ConfigManager.class",
    "net/aurelj/dungeons_arise_seven_seas/DungeonsAriseSevenSeasMain.class",
    "net/aurelj/dungeons_arise/DungeonsAriseMain.class",
    "net/aurelj/dungeons_arise/WDAStructures.class",
    "net/aurelj/dungeons_arise/structures/WDAGenericStructures.class",
    "net/aurelj/dungeons_arise/structures/ModifiedJigsawPlacement.class",
    "net/aurelj/dungeons_arise/structures/ModifiedJigsawPlacement$PieceState.class",
    "net/aurelj/dungeons_arise/structures/ModifiedJigsawPlacement$Placer.class",
    "de/cristelknight/tt/neoforge/TTNeoForge.class",
    "de/cristelknight/tt/TT.class",
    "architectury_inject_t_and_t_common_b1bac1484a1a4061b2d8c001fcdc6f6c_6ee4bb9e6149ef4d3806f6303bcca590484a471d1c7a66108587bc4193b4c700t_and_tcommon1132devjar/PlatformMethods.class",
    "net/village_taverns/mixin/PotionsMixin.class",
    "net/village_taverns/mixin/VillagerMixin.class",
    "com/aetherteam/aether/world/structure/BronzeDungeonStructure.class",
    "com/aetherteam/aether/world/structure/SilverDungeonStructure.class",
    "com/aetherteam/aether/world/structure/GoldDungeonStructure.class",
    "com/aetherteam/aether/world/structure/LargeAercloudStructure.class",
    "com/aetherteam/aether/world/structurepiece/LargeAercloudChunk.class",
    "com/aetherteam/aether/world/structurepiece/AetherTemplateStructurePiece.class",
    "com/aetherteam/aether/world/processor/BossRoomProcessor.class",
    "com/aetherteam/aether/world/processor/DoubleDropsProcessor.class",
    "com/aetherteam/aether/loot/AetherLoot.class",
    "com/aetherteam/aether/block/dungeon/ChestMimicBlock.class",
    "com/aetherteam/aether/block/dungeon/TrappedBlock.class",
    "com/aetherteam/aether/block/AetherBlocks.class",
    "com/aetherteam/aether/event/AetherEventDispatch.class",
    "com/aetherteam/aether/event/TriggerTrapEvent.class",
    "com/aetherteam/aether/blockentity/ChestMimicBlockEntity.class",
    "com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeDungeonBuilder.class",
    "com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeDungeonBuilder$Connection.class",
    "com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeDungeonBuilder$RoomProvider.class",
    "com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeDungeonRoom.class",
    "com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeDungeonSurfaceRuins.class",
    "com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeTunnel.class",
    "com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeBossRoom.class",
    "com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeProcessorSettings.class",
    "com/aetherteam/aether/world/structurepiece/bronzedungeon/BronzeDungeonPiece.class",
    "com/telepathicgrunt/repurposedstructures/world/structures/MansionStructure.class",
    "com/telepathicgrunt/repurposedstructures/world/structures/MonumentStructure.class",
    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces.class",
    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$MonumentBuilding.class",
    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$MonumentPiece.class",
    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$FitDoubleXYRoom.class",
    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$FitDoubleYZRoom.class",
    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$FitDoubleZRoom.class",
    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$FitDoubleXRoom.class",
    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$FitDoubleYRoom.class",
    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$FitSimpleTopRoom.class",
    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$FitSimplePillarRoom.class",
    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$FitSimpleRoom.class",
    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$MonumentRoomFitter.class",
    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MansionPieces.class",
    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MansionPieces$LayoutGenerator.class",
    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MansionPieces$RoomCollection.class",
    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MansionPieces$FirstFloor.class",
    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MansionPieces$SecondFloor.class",
    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MansionPieces$ThirdFloor.class",
    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MansionStructurePiece.class",
    "com/telepathicgrunt/repurposedstructures/world/processors/ForcePlaceMushroomBlocksProcessor.class",
    "com/telepathicgrunt/repurposedstructures/modinit/RSProcessors.class",
    "com/telepathicgrunt/repurposedstructures/world/predicates/YValuePosRuleTest.class",
    "com/telepathicgrunt/repurposedstructures/world/processors/PillarProcessor.class",
    "com/telepathicgrunt/repurposedstructures/world/processors/CappedStructureSurfaceProcessor.class",
    "com/telepathicgrunt/repurposedstructures/world/processors/NoiseReplaceWithPropertiesProcessor.class",
    "com/telepathicgrunt/repurposedstructures/world/processors/RandomReplaceWithPropertiesProcessor.class",
    "com/telepathicgrunt/repurposedstructures/world/processors/SpawnerRandomizingProcessor.class",
    "com/telepathicgrunt/repurposedstructures/misc/mobspawners/MobSpawnerManager.class",
    "com/telepathicgrunt/repurposedstructures/misc/mobspawners/MobSpawnerObj.class",
    "org/violetmoon/quark/content/world/gen/BigStoneClusterGenerator$1.class",
    "org/violetmoon/quark/content/world/module/CherryGroveWaterPetalsModule.class",
    "org/violetmoon/quark/content/world/gen/BlossomTreeGenerator.class",
    "org/violetmoon/quark/content/world/gen/CherryGroveWaterPetalsGenerator.class",
    "org/violetmoon/quark/content/world/undergroundstyle/CorundumStyle.class",
    "org/violetmoon/quark/content/world/undergroundstyle/PermafrostStyle.class",
    "org/violetmoon/quark/content/world/undergroundstyle/base/UndergroundStyleGenerator.class",
    "org/violetmoon/quark/content/world/undergroundstyle/base/UndergroundStyleGenerator$Context.class",
    "org/violetmoon/quark/content/world/undergroundstyle/base/BasicUndergroundStyle.class",
    "org/violetmoon/quark/content/world/undergroundstyle/base/UndergroundStyle.class",
    "org/violetmoon/quark/content/world/gen/ObsidianSpikeGenerator.class",
    "org/violetmoon/quark/content/world/gen/FallenLogGenerator.class",
    "org/violetmoon/quark/content/world/gen/FallenLogGenerator$Decor.class",
    "org/violetmoon/quark/content/world/gen/FairyRingGenerator.class",
    "org/violetmoon/quark/content/world/gen/MonsterBoxGenerator.class",
    "org/violetmoon/quark/content/world/block/MonsterBoxBlock.class",
    "org/violetmoon/quark/content/world/block/be/MonsterBoxBlockEntity.class",
    "org/violetmoon/quark/mixin/mixins/accessor/AccessorLivingEntity.class",
    "com/yungnickyoung/minecraft/yungsbridges/mixin/SuppressLogMixin.class",
    "com/yungnickyoung/minecraft/yungsbridges/module/FeatureModule.class",
    "com/yungnickyoung/minecraft/yungsbridges/module/PlacementModifierTypeModule.class",
    "com/yungnickyoung/minecraft/yungsbridges/services/IPlatformHelper.class",
    "com/yungnickyoung/minecraft/yungsbridges/services/NeoForgePlatformHelper.class",
    "com/yungnickyoung/minecraft/yungsbridges/services/Services.class",
    "com/yungnickyoung/minecraft/yungsbridges/world/feature/config/MultipleAttemptSingleRandomFeatureConfig.class",
    "com/yungnickyoung/minecraft/yungsextras/module/PlacementModifierTypeModule.class",
    "com/yungnickyoung/minecraft/yungsextras/services/IPlatformHelper.class",
    "com/yungnickyoung/minecraft/yungsextras/services/NeoForgePlatformHelper.class",
    "com/yungnickyoung/minecraft/yungsextras/services/Services.class",
    "com/yungnickyoung/minecraft/yungsextras/world/config/DesertWellFeatureConfiguration.class",
    "com/yungnickyoung/minecraft/yungsextras/world/config/ResourceLocationFeatureConfiguration.class",
    "com/yungnickyoung/minecraft/yungsextras/world/placement/RngInitializerPlacement.class",
    "com/finndog/moogs_structures/MoogsStructuresCommon.class",
    "com/finndog/moogs_structures/neoforge/MoogsStructuresNeoforge.class",
    "com/finndog/moogs_structures/modinit/MoogsStructuresConditionsRegistry.class",
    "com/finndog/moogs_structures/modinit/MoogsStructuresPlacements.class",
    "com/finndog/moogs_structures/modinit/MoogsStructuresProcessors.class",
    "com/finndog/moogs_structures/modinit/MoogsStructuresStructurePlacementType.class",
    "com/finndog/moogs_structures/modinit/MoogsStructuresStructures.class",
    "com/finndog/moogs_structures/modinit/MoogsStructuresTags.class",
    "com/finndog/moogs_structures/commands/DebugCommand.class",
    "com/finndog/moogs_structures/misc/trialspawnerconfig/TrialSpawnerConfigManager.class",
    "com/finndog/moogs_structures/mixins/neoforge/structures/StructurePoolMixin.class",
    "com/finndog/moogs_structures/mixins/features/NoBasaltColumnsInStructuresMixin.class",
    "com/finndog/moogs_structures/mixins/features/NoDeltasInStructuresMixin.class",
    "com/finndog/moogs_structures/mixins/resources/NamespaceResourceManagerAccessor.class",
    "com/finndog/moogs_structures/mixins/structures/JigsawReplacementProcessorMixin.class",
    "com/finndog/moogs_structures/mixins/structures/ListPoolElementAccessor.class",
    "com/finndog/moogs_structures/mixins/structures/LocateCommandMixin.class",
    "com/finndog/moogs_structures/mixins/structures/PoolElementStructurePieceAccessor.class",
    "com/finndog/moogs_structures/mixins/structures/SinglePoolElementAccessor.class",
    "com/finndog/moogs_structures/mixins/structures/StructurePieceAccessor.class",
    "com/finndog/moogs_structures/mixins/structures/StructurePoolAccessor.class",
    "com/finndog/moogs_structures/mixins/structures/StructureProcessorAccessor.class",
    "com/finndog/moogs_structures/mixins/structures/StructureTemplateManagerAccessor.class",
    "com/finndog/moogs_structures/mixins/structures/TemplateAccessor.class",
    "com/finndog/moogs_structures/mixins/terrainadaptation/BeardifierAccessor.class",
    "com/finndog/moogs_structures/mixins/terrainadaptation/BeardifierMixin.class",
    "com/finndog/moogs_structures/utils/MixinUtils.class",
    "com/finndog/moogs_structures/utils/DebugFlags.class",
    "com/finndog/moogs_structures/world/structures/terrainadaptation/beardifier/EnhancedBeardifierHelper.class",
    "com/finndog/moogs_structures/platform/Services.class",
    "com/finndog/moogs_structures/platform/IRegistryPlatform.class",
    "com/finndog/moogs_structures/modinit/registry/neoforge/ResourcefulRegistriesImpl.class",
    "com/finndog/moogs_structures/modinit/registry/neoforge/NeoForgeResourcefulRegistry.class",
    "com/finndog/moogs_structures/modinit/registry/ResourcefulRegistries.class",
    "com/finndog/moogs_structures/utils/AsyncLocator.class",
    "com/finndog/moogs_structures/utils/neoforge/PlatformHooksImpl.class",
    "com/finndog/moogs_structures/datagen/StructureNbtUpdaterDatagen.class",
    "architectury_inject_IntegratedStronghold_common_dac55d1c3d7c43d0b24fcf81e4608720_3415319371a0be83cfe6c4f3244ac2ed779cd7573f518ebf3d404884c005522cintegrated_stronghold1141211commondevjar/PlatformMethods.class",
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


def main() -> None:  # noqa: C901, PLR0912, PLR0915 - explicit verified archive capture.
    """Retain disassembly and exact class/archive identities for the observed custom types."""
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("--output", type=Path, required=True)
    _ = parser.add_argument("--archive", choices=sorted(ARCHIVES))
    _ = parser.add_argument("--class-name", action="append", choices=CLASSES)
    _ = parser.add_argument("--nested-archive", choices=[
        "META-INF/jars/tiny-config-3.1.0-neoforge.jar"])
    args = parser.parse_args()
    output = cast("Path", args.output)
    selected_archive = cast("str | None", args.archive)
    selected_classes = cast("list[str] | None", args.class_name)
    nested = cast("str | None", args.nested_archive)
    if nested and selected_archive != "village_taverns-neoforge-1.1.5+1.21.1.jar":
        parser.error("the selected nested archive requires the frozen Village Taverns parent")
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
        with ZipFile(source.path) as parent, ExitStack() as stack:
            archive = parent
            classpath = source.path
            archive_name, archive_sha = source.name, source.sha256
            if nested:
                nested_payload = parent.read(nested)
                archive_sha = hashlib.sha256(nested_payload).hexdigest()
                if archive_sha != (
                    "1587ed9848881e7b677da5b8c85e0f35719315eb5f6571592d31840cf1421f63"
                ):
                    message = "bundled Tiny Config identity mismatch"
                    raise ValueError(message)
                temporary = stack.enter_context(NamedTemporaryFile(suffix=".jar"))
                _ = temporary.write(nested_payload)
                temporary.flush()
                classpath = Path(temporary.name)
                archive = stack.enter_context(ZipFile(classpath))
                archive_name += "!/" + nested
                destination /= Path(nested).name
                destination.mkdir()
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
                        *sorted(
                            n for n in archive.namelist()
                            if n.startswith(
                                "META-INF/services/com.yungnickyoung.minecraft.betterendisland."
                            )
                        ),
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
                if (
                    source.name == MAPPED_SERVER.name and name not in CLASSES[:48]
                    and name != (
                        "net/minecraft/world/level/levelgen/feature/EndPlatformFeature.class"
                    )
                ):
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
                verbose = source.name.startswith((
                    "mcw-", "AI-Improvements-", "attributefix-", "LeavesBeGone-",
                    "Almanac-", "libraryferret-", "structure_layout_optimizer-",
                    "letmedespawn-", "sparsestructures-", "structure_pool_api-",
                ))
                verbose |= "/mixin/" in name or "/mixins/" in name or name in {
                    "net/choicetheorem/ctov/CTOV.class",
                    "net/choicetheorem/ctov/neoforge/ctovNeo.class",
                    "net/adorabuild/structures/AdorabuildStructuresMod.class",
                    "com/craisinlord/integrated_stronghold/IntegratedStronghold.class",
                    "com/craisinlord/integrated_stronghold/neoforge/IntegratedStrongholdNeoforge.class",
                    "com/finndog/moogs_structures/MoogsStructuresCommon.class",
                    "com/finndog/moogs_structures/neoforge/MoogsStructuresNeoforge.class",
                    "org/betterx/betterend/registry/EndFeatures.class",
                    "net/redstonegames/chefsdelight/ChefsDelight.class",
                    "net/redstonegames/chefsdelight/worldgen/village/VillageStructures.class",
                    "com/aetherteam/aether/block/AetherBlocks.class",
                    "com/aetherteam/aether/world/structurepiece/AetherTemplateStructurePiece.class",
                    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$MonumentBuilding.class",
                    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$MonumentPiece.class",
                    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$FitDoubleXYRoom.class",
                    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$FitDoubleYZRoom.class",
                    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$FitDoubleZRoom.class",
                    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$FitDoubleXRoom.class",
                    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$FitDoubleYRoom.class",
                    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$FitSimpleTopRoom.class",
                    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$FitSimplePillarRoom.class",
                    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$FitSimpleRoom.class",
                    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$MonumentRoomFitter.class",
                    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MansionPieces$LayoutGenerator.class",
                    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MansionPieces$FirstFloor.class",
                    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MansionPieces$SecondFloor.class",
                    "com/telepathicgrunt/repurposedstructures/world/structures/pieces/MansionPieces$ThirdFloor.class",
                    "org/violetmoon/quark/content/world/module/NetherObsidianSpikesModule.class",
                    "org/violetmoon/quark/content/world/gen/ObsidianSpikeGenerator.class",
                    "org/violetmoon/quark/base/proxy/CommonProxy.class",
                    "org/violetmoon/zetaimplforge/module/ModFileScanDataModuleFinder.class",
                    "org/violetmoon/quark/content/world/module/MonsterBoxModule.class",
                    "org/violetmoon/quark/content/world/block/MonsterBoxBlock.class",
                    "org/violetmoon/quark/content/world/block/be/MonsterBoxBlockEntity.class",
                    "org/violetmoon/quark/content/world/module/SpiralSpiresModule.class",
                    "org/violetmoon/zeta/config/ConfigObjectMapper.class",
                    "org/violetmoon/zeta/config/ConfigManager.class",
                    "org/violetmoon/zeta/config/type/DimensionConfig.class",
                    "org/violetmoon/zeta/config/type/CompoundBiomeConfig.class",
                    "org/violetmoon/zeta/config/type/BiomeTagConfig.class",
                    "org/violetmoon/zeta/config/type/StrictBiomeConfig.class",
                    "org/violetmoon/zetaimplforge/config/ConfigEventDispatcher.class",
                    CLASSES[0],
                    "org/betterx/betterend/registry/EndStructures.class",
                    "com/yungnickyoung/minecraft/yungsextras/module/FeatureModule.class",
                    "com/yungnickyoung/minecraft/betterendisland/world/feature/BetterSpikeFeature.class",
                    "com/yungnickyoung/minecraft/betterendisland/world/feature/BetterEndPodiumFeature.class",
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
                        str(classpath),
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
                        f"Classfile {archive_name}!/{name}\n".encode()
                        + disassembly.partition(b"\n")[2]
                    )
                target = destination / f"{class_name}.txt"
                _ = target.write_bytes(disassembly)
                identities.append(
                    {
                        "archive": archive_name,
                        "archive_sha256": archive_sha,
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
