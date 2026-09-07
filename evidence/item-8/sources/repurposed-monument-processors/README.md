# Monument processors

Captured with extractor revision c37898e. All six captures and identities
reproduced byte for byte before this README was added. Reproduce:

```sh
uv run -m tools.inspect_item8_pool_elements --archive repurposed_structures-7.5.21+1.21.1-neoforge.jar --class-name com/telepathicgrunt/repurposedstructures/modinit/RSProcessors.class --class-name com/telepathicgrunt/repurposedstructures/world/predicates/YValuePosRuleTest.class --class-name com/telepathicgrunt/repurposedstructures/world/processors/PillarProcessor.class --class-name com/telepathicgrunt/repurposedstructures/world/processors/CappedStructureSurfaceProcessor.class --class-name com/telepathicgrunt/repurposedstructures/world/processors/NoiseReplaceWithPropertiesProcessor.class --class-name com/telepathicgrunt/repurposedstructures/world/processors/RandomReplaceWithPropertiesProcessor.class --output evidence/raw/item8/repurposed-monument-processors-r1
```

## Direct processor behavior

PillarProcessor matches the complete incoming block state against its trigger
map. Other block info is returned unchanged. For a match it chooses replacement
and optional original-position replacement states. It skips extension outside
the WorldGenRegion center chunk, returning the original-position replacement.
The codec defaults direction to DOWN, pillar_length to 1000 and forced_placement
to false. This length is a configured ceiling, not an observed pillar height.

For nonforced downward extension it obtains a land height through
GeneralUtils.getFirstLandYFromPos, with an early no-land/min-build-height exit.
The extension loop checks replaceability, land height, build bounds and strict
closerThan distance from the trigger position. Forced placement relaxes the
land check and allows nonnegative-hardness blocks under its predicate. The
loop starts at the trigger, moves in the configured direction, and stops at the
first failed check. The caller delegates land-height semantics to GeneralUtils.
Do not treat a template or saved-piece envelope as the full occupied height.

Each extension position may run the referenced processor list's processBlock
methods in order, stopping processing on null. The direct chunk write uses
only the resulting state, not its NBT, at the extension position; the returned
previous state is discarded. It does not run those delegates' finalizeProcessing.
Thus jungle archaeology loot cannot be inferred on pillar extensions merely
because the pillar references jungle_randomize. Successful writes are unmeasured.

CappedStructureSurfaceProcessor supplies STRUCTURE_SURFACE_PROCESSOR from
getType; RSProcessors registers structure_surface_processor under that field
and contains the CappedStructureSurfaceProcessor codec supplier. The capture
preserves these bindings; it is not proof of effective runtime registration.
Its override is finalizeProcessing. For nonempty processed lists it requires
original/processed list sizes to agree; otherwise it logs and returns unchanged.
It indexes positions inside the placement bounds, shuffles them using the
unseeded Collections.shuffle(List) overload, and examines nonair, fluid-empty
blocks. Eligible blocks require an occluding, nonjigsaw block below and either
nonoccluding or jigsaw above. Missing neighbors use its solid-below/air-above
defaults when allow_void_sides permits them. The supplied jungle list enables
that option. It invokes the delegate's processBlock and replaces the processed
list entry only for a nonnull changed result. It does not itself spawn entities.

The unseeded shuffle is a source-level ordering limitation, not a measured
world mismatch. Do not claim fully seed-deterministic processor behavior from
this capture or reopen accepted world evidence without conflicting evidence.

YValuePosRuleTest accepts its second BlockPos argument's Y inclusively between
min_y_value and max_y_value, and rejects construction with min greater than max.
The selected Nether rules specify 0..31 for air-to-lava conversion. The engine
argument mapping and RSPredicates registration remain separate dependencies;
this inspection alone does not establish actual converted blocks.

NoiseReplaceWithPropertiesProcessor and RandomReplaceWithPropertiesProcessor
operate only on their input block. Matching replacement paths delegate property
copying to GeneralUtils and preserve incoming position and NBT. The noise path
uses its seeded noise generator and threshold; the random path reseeds from
position and processor-list index before selection. These callers contain no
entity or loot assignment. Exact noise/material patterns and delegated property
semantics are not reimplemented or claimed measured here.

Next: integrate these direct content/height effects into the monument decision,
keeping engine finalization, registry activation, land-helper semantics and
world observation distinct. Do not repeat template/loot extraction or build a
new measurement system. Scoped extractor Ruff and Basedpyright passed.
