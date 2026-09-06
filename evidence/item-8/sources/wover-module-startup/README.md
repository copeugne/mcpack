# WorldWeaver module startup

Extractor b190341a99e006bb932b501f772fe09a1b928b10. Independent r1 reproduction
matches all seventeen disassemblies and the identity manifest. Manifest SHA-256:
f2a9d6f8299314df097c55d483033b066a430dc8ef108bcf87afa20acb7c50dc

```sh
uv run -m tools.inspect_item8_pool_elements --archive worldweaver-21.0.24.jar --class-name org/betterx/wover/entrypoint/LibWoverBiome.class --class-name org/betterx/wover/entrypoint/LibWoverBlock.class --class-name org/betterx/wover/entrypoint/LibWoverCommon.class --class-name org/betterx/wover/entrypoint/LibWoverCore.class --class-name org/betterx/wover/entrypoint/LibWoverDatagen.class --class-name org/betterx/wover/entrypoint/LibWoverEvents.class --class-name org/betterx/wover/entrypoint/LibWoverFeature.class --class-name org/betterx/wover/entrypoint/LibWoverItem.class --class-name org/betterx/wover/entrypoint/LibWoverMath.class --class-name org/betterx/wover/entrypoint/LibWoverPottable.class --class-name org/betterx/wover/entrypoint/LibWoverRecipe.class --class-name org/betterx/wover/entrypoint/LibWoverStructure.class --class-name org/betterx/wover/entrypoint/LibWoverSurface.class --class-name org/betterx/wover/entrypoint/LibWoverTag.class --class-name org/betterx/wover/entrypoint/LibWoverUi.class --class-name org/betterx/wover/entrypoint/LibWoverWorldGenerator.class --class-name org/betterx/wover/entrypoint/LibWoverWorldPreset.class --output evidence/raw/item8/wover-module-startup-r1
```

These are exactly the seventeen module constructors invoked by Wover. They
register module/datapack listeners, initialize registry managers and shared
configuration/state APIs, and register datagen providers. Generation-related
modules initialize feature/placement support, structure support, biome codecs
and modifiers, surface rules, chunk/biome-source registries and world presets.
Preset setup includes dimension overrides. It must not be interpreted as proof
that those presets were selected in the frozen Item 6 worlds.

This capture is partial provider evidence. Nonverbose javap preserves direct
invocations and method bodies but does not print BootstrapMethods targets for
external method-reference listeners. Resolve those targets before asserting
that every event registration is covered. Reuse existing pool-codec and biome
modifier captures. The provider remains open; no canonical count changes.
