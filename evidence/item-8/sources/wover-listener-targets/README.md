# WorldWeaver listener targets

Extractor 2dec51dbe418b4c4e86e604a67754e6dc3a39153. Independent r1 reproduction
matches all thirteen disassemblies and the identity manifest. Manifest SHA-256:
73e67c1b9e5d6563d6884c6c01b80cdf06faf10728a31e6cd138c8d42733e2b3

```sh
uv run -m tools.inspect_item8_pool_elements --archive worldweaver-21.0.24.jar --class-name org/betterx/wover/entrypoint/LibWoverBlock.class --class-name org/betterx/wover/entrypoint/LibWoverCore.class --class-name org/betterx/wover/entrypoint/LibWoverFeature.class --class-name org/betterx/wover/entrypoint/LibWoverItem.class --class-name org/betterx/wover/entrypoint/LibWoverRecipe.class --class-name org/betterx/wover/entrypoint/LibWoverStructure.class --class-name org/betterx/wover/entrypoint/LibWoverSurface.class --class-name org/betterx/wover/entrypoint/LibWoverTag.class --class-name org/betterx/wover/entrypoint/LibWoverWorldGenerator.class --class-name org/betterx/wover/entrypoint/LibWoverWorldPreset.class --class-name org/betterx/wover/entrypoint/client/LibWoverUiClient.class --class-name org/betterx/wover/entrypoint/client/LibWoverWorldGeneratorClient.class --class-name org/betterx/wover/entrypoint/client/ModMenuEntryPoint.class --output evidence/raw/item8/wover-listener-targets-r1
```

This supplies BootstrapMethods targets omitted by the earlier nonverbose
entry/module captures. The thirteen selected classes are exactly those with
invokedynamic instructions in those earlier captures. Preserve the earlier
captures as partial evidence; reproduce them with their recorded extractor.

Runtime registration targets are block predicates, datapack registries,
placement modifiers, features, structure/pool-element types, material
conditions/rules, biome sources and chunk generators. Preset callbacks target
PresetRegistryImpl and the captured local preset-info methods. Other targets
are datagen providers, tag-cache invalidation and client UI/update behavior.
The pool-element registry already has a capture in pool-codecs; reuse it.

The omission is resolved without a new measurement system. Direct generation
registrations and common hooks still require whole-provider reconciliation.
No independent family or provider closure is inferred from listener names.
