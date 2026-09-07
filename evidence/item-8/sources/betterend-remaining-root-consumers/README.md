# BetterEnd remaining root consumers

Selector 95997cf captures eighteen classes for remaining custom-root generators,
the cave-biome feature consumers, village keys and three concrete integrations.
The complete generated capture reproduces byte for byte against fresh r1 output.
This is an isolated generated-source increment. No new measurement mechanism,
world experiment or baseline modification is involved.

Manifest SHA-256: eb0d8ea37b2766dc0081c0e84035d9c37168758023bb33400d3028ef73363dbd.

```sh
uv run -m tools.inspect_item8_pool_elements --archive BetterEnd-21.0.31.jar --class-name org/betterx/betterend/integration/DyeDepotIntegration.class --class-name org/betterx/betterend/integration/FlamboyantRefabricatedIntegration.class --class-name org/betterx/betterend/integration/byg/BYGIntegration.class --class-name org/betterx/betterend/world/features/terrain/caves/CaveChunkPopulatorFeature.class --class-name org/betterx/betterend/world/features/terrain/caves/EndCaveFeatures.class --class-name 'org/betterx/betterend/world/structures/features/EndBridgeStructure$Anchor.class' --class-name org/betterx/betterend/world/structures/features/EndBridgeStructure.class --class-name org/betterx/betterend/world/structures/features/EndSulphuricCaveStructure.class --class-name org/betterx/betterend/world/structures/features/GiantIceStarStructure.class --class-name org/betterx/betterend/world/structures/features/GiantMossyGlowshroomStructure.class --class-name org/betterx/betterend/world/structures/features/SDFStructureFeature.class --class-name 'org/betterx/betterend/world/structures/features/SmallIslandStructure$IslandGeometry.class' --class-name org/betterx/betterend/world/structures/features/SmallIslandStructure.class --class-name org/betterx/betterend/world/structures/piece/CavePiece.class --class-name org/betterx/betterend/world/structures/piece/EndBridgePiece.class --class-name org/betterx/betterend/world/structures/piece/SulphuricCavePiece.class --class-name org/betterx/betterend/world/structures/piece/VoxelPiece.class --class-name org/betterx/betterend/world/structures/village/VillagePools.class --output evidence/raw/item8/betterend-remaining-root-consumers-r1
```

The five newly bound custom roots are end_bridge, sulphuric_cave,
giant_ice_star, giant_mossy_glowshroom and small_island. Existing registration
source and packaged definitions supply their identities; these are existing
runtime roots, not five newly discovered families.

EndBridgeStructure selects terrain anchors and creates an EndBridgePiece.
The piece writes an end-stone-brick deck and walls with material variation.
Its anchor search can return without a piece. Preserve one bridge-design
candidate; anchors, span variation and piece serialization are not families.

EndSulphuricCaveStructure creates SulphuricCavePiece, whose placement concerns
cave air, water, sulphuric rock, vents, brimstone, crystals and tube worms.
GiantIceStarStructure fills an SDF with snow and emerald ice materials.
GiantMossyGlowshroomStructure fills a fungal SDF. SmallIslandStructure builds
terrain with flower/vine or waterfall/stalactite treatments. These are named
terrain/vegetation root candidates; final family grouping must reconcile them
with the previously preserved formation decisions. Shared SDFStructureFeature
and VoxelPiece construct and serialize the selected geometry, not more designs.
No detailed geometry or world-occurrence claim follows from this capture.

VillagePools creates keys for the already accounted village pools and the
village_chorus placed feature. The latter's packaged definition uses vanilla
chorus_plant, not another settlement generator.

EndCaveFeatures consumes EndBiomes.getCaveBiome, sets cave biome information and
dispatches selected cave floor/ceiling features. CaveChunkPopulatorFeature also
uses selected cave floor/ceiling features. This establishes a consumer for the
separate cave-biome path; it does not prove every feature attached to a surface
biome also runs in caves.

BYGIntegration delegates blocks, features and biomes to BYG-specific registries.
Flamboyant's init is empty and its explicit block registration concerns colors;
DyeDepot supplies colored crafting recipes. Preserve actual conditional dispatch
through BCLib as an unresolved shared input. Do not recursively inspect inactive
compatibility trees merely because they exist in the archive.

Remaining provider work: reconcile other feature registration consumers,
remaining common mixin generation hooks and shared integration/modifier
activation. Do not reopen the completed 128-template partition. Whole-provider
coverage and canonical family totals remain incomplete.

## Bridge assessment

Provider discovery above is historical and is now closed. This increment assesses
the nine remaining bridge attributes using the already captured EndBridgeStructure,
its Anchor, EndBridgePiece and the existing full-start observations. No new
capture, source extractor or measurement system is needed.

The packaged root has empty spawn_overrides and surface_structures generation
step. Its custom findGenerationPoint supplies a stub at Y0, then generatePieces
samples terrain heights and chooses two anchors. The stub is not deck elevation.
Candidate endpoints require horizontal separation24 to96 and height difference
at most12, with other terrain/island/angular predicates. Missing suitable anchors
can produce no piece; these are placement constraints, not separate families.

EndBridgePiece constructs a deck, railings, landings and supporting columns.
Its write paths use END_STONE_BRICKS, the CRACKED and WEATHERED slots of
END_STONE_BRICK_VARIATIONS, and END_STONE_BRICK_WALL. BlocksHelper is consulted
for replaceability; it is not a content generator. The root/piece path has no
entity creation, template entity loading, container-loot assignment or explicit
spawner configuration. It therefore authors a traversal structure without a
direct encounter or container reward. Empty spawn overrides do not suppress
natural biome enemies. These source statements do not assert complete runtime
absence of external mobs or loot injections.

Deck and railings provide visual cues, with weathered/cracked material variation
and possible railing gaps. Supports extend below the crossing. Exposure and
terrain occlusion are qualitative assessments; no visibility-distance or player
discovery measurement is inferred from source code or structure-start presence.

Five retained full starts represent four distinct layouts:

| Seed | Run and decoded line | Chunk | Saved size X,Y,Z |
| --- | --- | --- | --- |
| 6671238423019257953 | run-a/mountainous:6443 | 88,5 | 35,23,35 |
| 6671238423019257953 | run-a/mountainous:6654 | 91,13 | 24,19,40 |
| 95920844204830198 | run-a/ocean-heavy:8106 | 98,15 | 64,27,80 |
| 95920844204830198 | run-b/ocean-heavy:8106 | 98,15 | 64,27,80 |
| -3503646078644842058 | run-b/biome-diverse:7457 | 97,-9 | 24,23,40 |

Each source is the corresponding chunks.jsonl in preserved Item7 custody, joined
by world-bounds.json.gz. Exact envelopes and references are integrated in the
authoritative attributes. The existing observed_bounds implementation supplies
inclusive spans. makeBoundingBox expands endpoint minima/maxima by six on X/Z,
and uses min(endpointY)-12 to max(endpointY)+6 vertically. Thus the reported
examples include margins and support allowance, not occupied area, deck thickness,
typical dimensions or all-layout maxima. The ocean-heavy record repeats the
same layout; it is not a fifth independent sample. The bridge is now assessed
for all Item8 attributes without claiming Item8 as a whole is complete.
