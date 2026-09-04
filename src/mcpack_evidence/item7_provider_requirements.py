"""The exact retained components required for Item 7 provider coverage."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final

from .item7_provider_models import ProviderRole


@dataclass(frozen=True, slots=True)
class RequiredComponent:
    """An exact retained archive and its expected primary metadata identifier."""

    candidate_filename: str
    mod_id: str
    role: ProviderRole


@dataclass(frozen=True, slots=True)
class LabelRequirement:
    """The retained components required by one named Item 7 target."""

    label: str
    role: ProviderRole
    components: tuple[RequiredComponent, ...]


def components(
    role: ProviderRole, entries: tuple[tuple[str, str], ...]
) -> tuple[RequiredComponent, ...]:
    """Bind exact candidate filenames to expected metadata identifiers."""
    return tuple(RequiredComponent(filename, mod_id, role) for filename, mod_id in entries)


REQUIREMENTS: Final[tuple[LabelRequirement, ...]] = (
    LabelRequirement(
        "Tectonic",
        ProviderRole.TERRAIN_BIOME,
        components(
            ProviderRole.TERRAIN_BIOME, (("tectonic-3.0.22-neoforge-21.1.jar", "tectonic"),)
        ),
    ),
    LabelRequirement(
        "Terralith",
        ProviderRole.TERRAIN_BIOME,
        components(
            ProviderRole.TERRAIN_BIOME, (("Terralith_1.21.1_v2.6.2_Neoforge.jar", "terralith"),)
        ),
    ),
    LabelRequirement(
        "Biomes O' Plenty",
        ProviderRole.TERRAIN_BIOME,
        components(
            ProviderRole.TERRAIN_BIOME,
            (("BiomesOPlenty-neoforge-1.21.1-21.1.0.13.jar", "biomesoplenty"),),
        ),
    ),
    LabelRequirement(
        "Regions Unexplored",
        ProviderRole.TERRAIN_BIOME,
        components(
            ProviderRole.TERRAIN_BIOME,
            (("regions-unexplored-0.6.1-neoforge-21.1.jar", "regions_unexplored"),),
        ),
    ),
    LabelRequirement(
        "TerraBlender",
        ProviderRole.LIBRARY,
        components(
            ProviderRole.LIBRARY, (("TerraBlender-neoforge-1.21.1-4.1.0.8.jar", "terrablender"),)
        ),
    ),
    LabelRequirement(
        "Lithostitched",
        ProviderRole.LIBRARY,
        components(
            ProviderRole.LIBRARY,
            (("lithostitched-1.7.10+beta4-neoforge-21.1.jar", "lithostitched"),),
        ),
    ),
    LabelRequirement(
        "BetterEnd",
        ProviderRole.TERRAIN_BIOME,
        components(ProviderRole.TERRAIN_BIOME, (("BetterEnd-21.0.31.jar", "betterend"),)),
    ),
    LabelRequirement(
        "YUNG",
        ProviderRole.DIRECT_STRUCTURE,
        components(ProviderRole.LIBRARY, (("YungsApi-1.21.1-NeoForge-5.1.6.jar", "yungsapi"),))
        + components(
            ProviderRole.TERRAIN_BIOME,
            (
                ("YungsBetterCaves-1.21.1-NeoForge-3.1.4.jar", "bettercaves"),
                ("YungsCaveBiomes-1.21.1-NeoForge-3.1.1.jar", "yungscavebiomes"),
            ),
        )
        + components(
            ProviderRole.DIRECT_STRUCTURE,
            (
                ("YungsBetterDesertTemples-1.21.1-NeoForge-4.1.5.jar", "betterdeserttemples"),
                ("YungsBetterDungeons-1.21.1-NeoForge-5.1.4.jar", "betterdungeons"),
                ("YungsBetterEndIsland-1.21.1-NeoForge-3.1.2.jar", "betterendisland"),
                ("YungsBetterJungleTemples-1.21.1-NeoForge-3.1.2.jar", "betterjungletemples"),
                ("YungsBetterMineshafts-1.21.1-NeoForge-5.1.1.jar", "bettermineshafts"),
                ("YungsBetterNetherFortresses-1.21.1-NeoForge-3.1.5.jar", "betterfortresses"),
                ("YungsBetterOceanMonuments-1.21.1-NeoForge-4.1.2.jar", "betteroceanmonuments"),
                ("YungsBetterStrongholds-1.21.1-NeoForge-5.1.3.jar", "betterstrongholds"),
                ("YungsBetterWitchHuts-1.21.1-NeoForge-4.1.1.jar", "betterwitchhuts"),
                ("YungsBridges-1.21.1-NeoForge-5.1.1.jar", "yungsbridges"),
                ("YungsExtras-1.21.1-NeoForge-5.1.1.jar", "yungsextras"),
            ),
        ),
    ),
    LabelRequirement(
        "WDA",
        ProviderRole.DIRECT_STRUCTURE,
        components(
            ProviderRole.DIRECT_STRUCTURE,
            (
                ("DungeonsArise-1.21.1-2.1.68-release.jar", "dungeons_arise"),
                ("DungeonsAriseSevenSeas-1.21.x-1.0.4-neoforge.jar", "dungeons_arise_seven_seas"),
            ),
        ),
    ),
    LabelRequirement(
        "IDAS",
        ProviderRole.DIRECT_STRUCTURE,
        components(ProviderRole.DIRECT_STRUCTURE, (("idas-1.13.7+1.21.1-neoforge.jar", "idas"),)),
    ),
    LabelRequirement(
        "Integrated structures",
        ProviderRole.DIRECT_STRUCTURE,
        components(
            ProviderRole.LIBRARY, (("integrated_api-1.7.3+1.21.1-neoforge.jar", "integrated_api"),)
        )
        + components(
            ProviderRole.DIRECT_STRUCTURE,
            (
                ("integrated_stronghold-1.1.4+1.21.1-neoforge.jar", "integrated_stronghold"),
                ("integrated_villages-1.3.3+1.21.1-neoforge.jar", "integrated_villages"),
            ),
        ),
    ),
    LabelRequirement(
        "Moog",
        ProviderRole.DIRECT_STRUCTURE,
        components(
            ProviderRole.DIRECT_STRUCTURE,
            (
                ("MoogsEndStructures-1.21-2.0.3.jar", "mes"),
                ("MoogsNetherStructures-1.21-3.0.0-alpha.2.jar", "mns"),
                ("MoogsSoaringStructures-1.21-2.1.2.jar", "mss"),
                ("MoogsVoyagerStructures-1.21-5.0.11.jar", "mvs"),
                ("moogs_structures-neoforge-1.21.1-alpha-3.0.0.jar", "moogs_structures"),
            ),
        ),
    ),
    LabelRequirement(
        "Explorify",
        ProviderRole.DIRECT_STRUCTURE,
        components(ProviderRole.DIRECT_STRUCTURE, (("Explorify v1.6.5.mod.jar", "explorify"),)),
    ),
    LabelRequirement(
        "Explorations",
        ProviderRole.DIRECT_STRUCTURE,
        components(
            ProviderRole.DIRECT_STRUCTURE,
            (("explorations-neoforge-1.21.1-1.6.2.jar", "explorations"),),
        ),
    ),
    LabelRequirement(
        "Repurposed Structures",
        ProviderRole.DIRECT_STRUCTURE,
        components(
            ProviderRole.DIRECT_STRUCTURE,
            (("repurposed_structures-7.5.21+1.21.1-neoforge.jar", "repurposed_structures"),),
        ),
    ),
    LabelRequirement(
        "CTOV",
        ProviderRole.DIRECT_STRUCTURE,
        components(ProviderRole.DIRECT_STRUCTURE, (("[Neoforge]ctov-3.6.3.jar", "ctov"),)),
    ),
    LabelRequirement(
        "Towns & Towers",
        ProviderRole.DIRECT_STRUCTURE,
        components(
            ProviderRole.DIRECT_STRUCTURE,
            (("t_and_t-neoforge-fabric-1.13.9+1.21.1.jar", "t_and_t"),),
        ),
    ),
)
