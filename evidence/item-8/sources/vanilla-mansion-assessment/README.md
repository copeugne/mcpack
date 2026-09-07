# Retained-stack mansion assessment

Seven remaining attributes are integrated in minecraft:mansion. Geometry is
already accepted in the vanilla-outpost-trail-assessment report. This increment
uses existing source and packaged artifacts, without a new capture or tool.

## Direct code inspection

Use pinned Temurin javap -p -c -v on the mapped server archive
server-1.21.1-20240808.144430-srg.jar, SHA-256
26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71.
Classes are under net.minecraft.world.level.levelgen.structure.structures.

| Class | SHA-256 |
| --- | --- |
| WoodlandMansionStructure | dad41680dee0985c252fedfb0b1c6e36ad5ff80473bef41ca17a7b81fae03af5 |
| WoodlandMansionPieces$WoodlandMansionPiece | f1d2cd100e5459a1ec1512fd437480c6a69ab522e9cad77eaed1baf7db1d7f1b |
| WoodlandMansionPieces$MansionPiecePlacer | ff7a9f7673284897d253c4668de5e66b774e5beaa965463d85f0d6248032506a |
| WoodlandMansionPieces$FirstFloorRoomCollection | 65f88ce27080eb8784bf96cf6d595fc1f5e9528b6faa2170df42ea1da9761e29 |
| WoodlandMansionPieces$SecondFloorRoomCollection | 3fcb2695d61d55239814172742d9cfca553840b94f6b1c4594b2b41bd5b21b4e |
| WoodlandMansionPieces$ThirdFloorRoomCollection | 0783bcf3bce919d4e6fcdeb1dbb5acf2471685b996d3acdf701146357fa19e71 |

First-floor concatenation recipes select 1x1_a1..5, 1x1_as1..4, 1x2_a1..9,
1x2_b1..5, 1x2_s1..2, 2x2_a1..4 and 2x2_s1. Second floor selects 1x1_b1..4,
1x1_as1..4, 1x2_c1..4, 1x2_d1..5, 1x2_se1, 2x2_b1..5, 2x2_s1 and the two
1x2_c_stairs/1x2_d_stairs alternatives. Third floor inherits second-floor methods.
Placer literals add walls, doors, carpets, corridors, roofs and entrance pieces.
Together these reference 72 packaged component IDs, with none missing.

Frozen config/lithostitched.json has breaks_seed_parity=true. The already retained
lithostitched-provider-hooks source captures show its mansion entry/room hooks
selecting registry template lists. The packaged lists under
 data/lithostitched/lithostitched/template_list/woodland_mansion/
include 1x1_b5 for second/third floor, giving 73 unique possible components.
The selected lithostitched:woodland_mansion processor list is empty. These hooks
are reconciled rather than treating vanilla nextInt(4) as the frozen selection.

The template catalog contains 73 vanilla rows and 13 same-ID Illager Invasion
replacements. Recorded mod_data priority selects those replacements. There are
86 packaged rows, not 86 components or families. All selected entities lists are
empty. makeSettings ignores template entities and uses STRUCTURE_BLOCK ignoring;
DATA markers are interpreted by the piece handler. Family attributes retain the
marker-to-template mapping from the selected rows.

## Effective content

Vanilla handleDataMarker creates evoker for Mage, vindicator for Warrior and
1..3 allay creation attempts for Group of Allays. Chest prefix calls createChest
with BuiltInLootTables.WOODLAND_MANSION; the directional suffix controls facing.
The existing vanilla-end-city-code capture includes BuiltInLootTables and its
woodland_mansion mapping. Creation requests do not prove generated population.

The existing illagerinvasion-provider capture's WoodlandMansionPieceMixin
intercepts Provoker, Archivist and invoker with the corresponding mod entities.
For Warrior, nextInt(2)==0 selects basher; the other branch returns null and leaves
the vanilla handler to create a vindicator. A selected mod entity type follows
persistence, STRUCTURE finalization, insertion and cancellation of vanilla handling.
Thus Warrior is not always a vindicator or always a basher. Mage and allay handling
remain vanilla. Source manifests for these existing captures are hash-bound in
the family evidence map.

Secret room woodland_mansion/1x1_as2 contains an ordinary spider spawner at [4,1,3].
The palette is minecraft:spawner; legacy NBT ID minecraft:mob_spawner is retained.
SpawnData and sole positive potential name spider. Delay0, min200, max800,
count4, nearby6, player range16 and spawn range4 are packaged settings, not counts
of spawned spiders. No selected template palette contains a trial spawner.

Chest markers use minecraft:chests/woodland_mansion. Replacement 2x2_b1 also has
that literal table; 1x2_c4 and 2x2_b3 reference minecraft:chests/stronghold_library.
Both definitions exist under data/minecraft/loot_table/chests/. Other chests have
literal Items or empty inventories rather than table references. Mod loot
injections can change contents; no reward quantity or probability is claimed.

Authored illager encounters and the conditional spider room establish hostility.
Empty root spawn overrides leave ordinary biome spawning possible. Allays are
non-hostile authored content. findGenerationPoint uses a rotated terrain base
and rejects Y below60. This supports surface-rooted placement, not exposed height
of every piece or foundation. The large wall/window/roof/entrance form supports a
qualitative visibility description; no sightline or population measurement is added.

## Rebuild and focused validation

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/mansion-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use an unused output path for reproduction. Only mansion and input identity change.
The source inspection supports descriptive judgments; tests validate integration
and source boundaries rather than certify prose or Item 8 completion.
