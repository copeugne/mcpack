# Repurposed Structures mansion entry and piece paths

Captured at extractor revision 0cd0467. Three captures and identities.json
reproduced byte for byte before this README was added:

```sh
uv run -m tools.inspect_item8_pool_elements --archive repurposed_structures-7.5.21+1.21.1-neoforge.jar --class-name com/telepathicgrunt/repurposedstructures/world/structures/MansionStructure.class --class-name com/telepathicgrunt/repurposedstructures/world/structures/pieces/MansionPieces.class --class-name com/telepathicgrunt/repurposedstructures/world/structures/pieces/MansionStructurePiece.class --output evidence/raw/item8/repurposed-mansion-0cd0467
```

MansionStructure records a lowercased mansion_type, foundation_block,
pillar_only_to_land, optional valid_biome_radius_check and liquid_settings.
The codec defaults pillar_only_to_land to true, constrains a supplied biome
radius to 1..100, and defaults liquid settings to the vanilla jigsaw default.
These are codec rules, not a claim about selected per-variant values.

The generation entry seeds its own random from world seed and chunk coordinates
and chooses a rotation. It samples four WORLD_SURFACE_WG heights through
GeneralUtils.getCachedFreeHeight, at the chunk middle and rotation-dependent
five-block offsets. Each returned height minus one must exceed generator minY.
It uses the minimum and starts at that value plus one. An optional biome-radius
check samples chunk-grid biome points at this height and rejects any invalid
biome, except that CheckerboardColumnBiomeSource bypasses this extra check.
The cache helper itself is not claimed audited here.

MansionPieces delegates to MansionParameters and LayoutGenerator.generate.
The returned pool-element pieces are wrapped as MansionStructurePiece while
preserving element, position, rotation, bounds and ground delta, plus mansion
type, foundation state and pillar flag. Other piece types are added unchanged.
The wrapper has no separate content-placement override. Layout component/pool
selection is still unresolved and must be inspected before assigning template
entities, spawners and loot to this custom family.

After placement, MansionStructure uses the first mansion piece's foundation
settings. Within the current chunk and combined piece X/Z bounds it checks a
nonempty base position inside a piece, then extends foundation downward through
air, fluid, REPLACEABLE_BY_TREES or FLOWERS until a stopping condition. It stops
above generator minY and, with pillar_only_to_land, at the helper's land height.
These writes use flag two and discard success booleans. Foundations can extend
below saved piece bounds: those bounds are not a complete occupied vertical
measurement. This direct loop does not widen the piece X/Z envelope.

Next: inspect LayoutGenerator and its component selectors, then reconcile
selected pool resources and templates with the existing inventory. Do not
repeat wrapper serialization or foundation-material details to infer content.
Scoped extractor Ruff and Basedpyright checks passed. No new measurement or
server run; no family completion or successful gameplay claim.
