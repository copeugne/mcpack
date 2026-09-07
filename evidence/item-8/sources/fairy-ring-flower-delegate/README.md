# Fairy Ring flower delegation

The unresolved claim was the geometry/content effect of Fairy Ring's selected
flower. The existing FairyRingGenerator body extracts RandomPatchConfiguration's
inner placed feature. It does not execute the outer flower patch's tries or spread.
Three vanilla class captures resolve selection and placement using the existing
extractor; archive, class and disassembly hashes are retained in identities.json.

```sh
uv run -m tools.inspect_item8_pool_elements --archive server-1.21.1-20240808.144430-srg.jar --class-name net/minecraft/world/level/biome/BiomeGenerationSettings.class --class-name net/minecraft/world/level/levelgen/feature/SimpleBlockFeature.class --class-name net/minecraft/world/level/levelgen/placement/BlockPredicateFilter.class --output evidence/raw/item8/fairy-ring-flower-delegate-reproduction
uv run pytest tests/item8/test_feature_modifier_references.py -k fairy_ring_packaged -q
```

BiomeGenerationSettings.lambda$new$3 selects Feature.FLOWER by identity. The
existing catalog has 76 flower objects, all with an inline simple_block delegate
and one block_predicate_filter. The focused test traverses every catalog document,
including nested objects, and binds that complete packaged set to its catalog hash.
It is a conservative superset of biome choices, not 76 new families or a claim
that every flower is eligible in every biome.

BlockPredicateFilter tests the supplied position. SimpleBlockFeature requests one
state, tests survival, and writes there, or places a double plant if the upper
position is empty. It does not execute the outer patch, spawn entities, assign
container loot or configure spawners. The double-plant branch can extend one block
above the requested position. Fairy Ring's highest flower origin is anchor+6, so
the combined envelope reaches +7; the existing ore lower bound is -45. This gives
7x53x7 rather than the direct-only 7x52x7 conservative envelope. It includes air
and buried ore and must not be reported as visible height or occupied geometry.

The packaged state providers supply flowers, grasses and shrubs. The conservative
set includes wither rose, so absence of authored mobs is not a safety guarantee.
Failed placement can leave air for later copies; no complete visible ring or actual
flower choice is asserted. The integrated attributes now resolve the direct and
packaged delegated contribution, with no specific unanswered mandatory claim left
for Fairy Ring. Reopen only for a demonstrated contradictory or changed input.

This added one focused catalog check and three named class selections to the
existing paths because the earlier generator capture did not establish the
callee's behavior. No new runtime, schema or measurement framework was introduced.
Initial test type annotations were corrected after Basedpyright rejected untyped
JSON; the final scoped checks pass.
