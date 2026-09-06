# WorldWeaver registration targets

Extractor d9415eaf47b972395f4b8d0280519d34b01199fb. Independent r1 reproduction
matches all ten disassemblies and the identity manifest. Manifest SHA-256:
49c08adb298ff6d87ee15167b56c956274b7b043b1d79f62455cbf697f0602aa

```sh
uv run -m tools.inspect_item8_pool_elements --archive worldweaver-21.0.24.jar --class-name org/betterx/wover/block/impl/predicate/BlockPredicatesImpl.class --class-name org/betterx/wover/core/impl/registry/DatapackRegistryBuilderImpl.class --class-name org/betterx/wover/feature/impl/FeatureManagerImpl.class --class-name org/betterx/wover/feature/impl/placed/modifiers/PlacementModifiersImpl.class --class-name org/betterx/wover/generator/impl/biomesource/BiomeSourceManagerImpl.class --class-name org/betterx/wover/generator/impl/chunkgenerator/ChunkGeneratorManagerImpl.class --class-name org/betterx/wover/generator/impl/preset/PresetRegistryImpl.class --class-name org/betterx/wover/structure/impl/StructureManagerImpl.class --class-name org/betterx/wover/surface/impl/conditions/MaterialConditionRegistryImpl.class --class-name org/betterx/wover/surface/impl/rules/MaterialRuleRegistryImpl.class --output evidence/raw/item8/wover-registration-targets-r1
```

These ten classes are the runtime registration targets exposed by the entry
method handles, excluding StructurePoolElementTypeManagerImpl already retained
in pool-codecs. The initial selection assertion incorrectly assumed that this
previously captured class was also in the explicit CLASSES allowlist. That
assertion failed before changing files. Excluding the existing capture explicitly
resolved the selection; no duplicate pool capture was needed.

FeatureManagerImpl registers reusable place_block, mark_postprocessing,
sequence, condition, pillar and template feature types. StructureManagerImpl
registers random_nbt_structure and piece support (random_nbt_structure_piece
and template_piece); it exposes a consumer BOOTSTRAP_STRUCTURES event.
PlacementModifiersImpl registers placement codecs, including legacy aliases.
Material condition/rule registries supply threshold, volume threshold, rough
noise and switch-rule support. Block predicates, biome sources and chunk
generators are shared registries. PresetRegistryImpl bootstraps normal, large,
amplified, superflat and legacy_17 options. Availability is not evidence of
which preset was selected in the frozen baseline.

DatapackRegistryBuilderImpl accumulates consumer registry entries and invokes
entrypoint initialization before handling the registry event. This is not by
itself proof that its consumers introduce no content. These captures retain
registration bodies, not a complete WorldWeaver membership decision. Reconcile
bootstrap consumers and generation hooks against frozen registry/configuration
and packaged data evidence before closing the provider. Preserve nonverbose
method-handle limitations where external targets remain load-bearing.
