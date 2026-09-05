# Village street processor contribution

The retained Regions Unexplored modifier appends a reference to
`regions_unexplored:village_path_fix` to `minecraft:street_plains`,
`minecraft:street_savanna`, and `minecraft:street_snowy_or_taiga`.
Its two source documents are preserved in `../packaged-json-redacted.json.gz`:

- `data/regions_unexplored/lithostitched/worldgen_modifier/processor_list/village_path_fix.json`,
  SHA-256 `f2ebde73345f097c3f72c5ea36d181092894675a433b44aed23f80d1cf62ce5f`.
- `data/regions_unexplored/worldgen/processor_list/village_path_fix.json`,
  SHA-256 `dbc7bf61408978cf1ea7268cefe5359243be027608a5daec338161d6ec3a17d4`.

Both are from `regions-unexplored-0.6.1-neoforge-21.1.jar`. The processor
document declares silt and peat biome-tag conditions together with the
`custom_dirts` configuration condition. Each true branch swaps only
`minecraft:dirt_path` and `minecraft:grass_block` to the corresponding
Regions Unexplored silt or peat blocks. Both false branches are empty.

`AddProcessorListProcessorsModifier.applyModifier` copies the existing list,
appends the supplied processors and installs the resulting list.
`ReferenceStructureProcessor.processBlock` sequentially delegates to the
referenced lists. `ConditionProcessor.processBlock` selects the true or false
list and delegates to its processors, returning the input outside world
generation. `BlockSwapStructureProcessor.processBlock` replaces a matching
block state while carrying over its position and NBT; unmatched blocks or an
absent target registry entry return the input. It copies compatible state
properties through `Block.withPropertiesOf`.

The companion `../lithostitched-processor-registration-code` disassembly of
`LithostitchedVersion` binds `block_swap`, `reference`, and `condition` to these
exact processor types. `UnboundReferenceProcessor`, mentioned in an earlier
handoff, is not the implementation used by this JSON reference.

This contribution changes the possible village street palette. These branches
add no family, pool, template, authored entity, spawner or loot reference and
do not enlarge the template envelope. This is an implementation and packaged
data disposition, not an observation that a condition activated in a particular
world. No simulation, frequency estimate or runtime capture is required to
establish this limited contribution. The machine-readable modifier disposition
will be updated together with the remaining feature and surface-rule checks.

Executed successfully using tool `c23bbab` for the five processor classes and
`eb0cb28` for registration, into absent output directories:

```sh
uv run -m tools.inspect_item8_pool_elements --archive lithostitched-1.7.10+beta4-neoforge-21.1.jar --class-name dev/worldgen/lithostitched/api/worldgen/processor/LithostitchedProcessors.class --class-name dev/worldgen/lithostitched/worldgen/modifier/AddProcessorListProcessorsModifier.class --class-name dev/worldgen/lithostitched/impl/worldgen/processor/ReferenceStructureProcessor.class --class-name dev/worldgen/lithostitched/impl/worldgen/processor/ConditionProcessor.class --class-name dev/worldgen/lithostitched/impl/worldgen/processor/BlockSwapStructureProcessor.class --output evidence/item-8/sources/lithostitched-street-processor-code
uv run -m tools.inspect_item8_pool_elements --archive lithostitched-1.7.10+beta4-neoforge-21.1.jar --class-name dev/worldgen/lithostitched/impl/LithostitchedVersion.class --output evidence/item-8/sources/lithostitched-processor-registration-code
```

Scoped Ruff and basedpyright passed. The extractor verified the frozen archive
hash; all six disassembly hashes matched their identity records on inspection.
Processor identities SHA-256:
`b813d2393bfb7ff410451e5cee65a6036187abe438405bb2a1d9cd00e5f5cafc`.
Registration identities SHA-256:
`803ac1e2b0d9992d51c5e5246db7ff88683fe0f7de21ec6f4e9881d240da991f`.
