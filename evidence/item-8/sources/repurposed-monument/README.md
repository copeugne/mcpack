# Repurposed Structures monument entry and assembly

Captured with extractor revision 04ec955. All four disassemblies and their
identities reproduced byte for byte before this README was added:

```sh
uv run -m tools.inspect_item8_pool_elements --archive repurposed_structures-7.5.21+1.21.1-neoforge.jar --class-name com/telepathicgrunt/repurposedstructures/world/structures/MonumentStructure.class --class-name com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces.class --class-name 'com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$MonumentBuilding.class' --class-name 'com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$MonumentPiece.class' --output evidence/raw/item8/repurposed-monument-04ec955
```

The entry seeds its random from world seed and chunk coordinates. A supplied
fixed_y_spawn takes priority. Otherwise, let C be the central WORLD_SURFACE_WG
height minus one and M the minimum of C and the four diagonal samples at X/Z
offsets of plus or minus 29, each minus one. The selected Y is
C + Java-int((M - C) / center_terrain_height_weight), with absent weight default
one. Sampling delegates to GeneralUtils.getCachedFreeHeight. This documents
the caller, not a new validation of that helper or measured terrain.

Y must exceed generator minY. If valid_biome_radius_check is present, the entry
checks chunk-grid biome samples at the selected height against validBiome;
CheckerboardColumnBiomeSource bypasses this additional check. The entry then
assembles pieces, chooses a rotation, rotates positions about the origin and
applies a rotated (-29, 0, -29) shift. Single-element bounding boxes are reset
using the template and selected rotation. This is source behavior, not occupied
world geometry or successful placement.

MonumentPieces constructs MonumentBuilding, adds its main body and child pieces,
then moves the resulting pieces with GeneralUtils.movePieceProperly. Its pool
lookup selects getRandomTemplate directly. Missing/empty pools log a warning
and substitute an empty rigid element. The method creates ordinary
PoolElementStructurePiece instances; it is not a recursive jigsaw expansion.

MonumentBuilding's direct pool names are bound by verbose concatenation recipes
under repurposed_structures:monuments/{monument_type}/:

- rooms/core;
- openings/entrance_wall, openings/wall_1 and openings/floor;
- body/ne_corner, body/nw_corner, body/se_corner and body/sw_corner.

These are direct call-site candidates, not the complete component set. The
constructor builds a room graph and considers fitters in order: DoubleXY,
DoubleYZ, DoubleZ, DoubleX, DoubleY, SimpleTop, SimplePillar and Simple. For an
unclaimed, nonspecial graph node it uses the first fitting rule, then delegates
both room and opening creation. Their pool names/content remain to be captured
and reconciled before claiming complete custom component attribution.

The base MonumentPiece is a graph/index helper, not the placed template piece.
Do not infer entity placement, loot, spawners, full dimensions or player
discoverability from these captures alone. Reuse the selected JSON/template
catalogs for the next component join. No new world measurement, framework or
runtime acceptance claim. Scoped extractor Ruff and Basedpyright passed.
