# WorldWeaver provider entries

Extractor 77ae7c8919636132c4b1186082cc2b207ece6c68. Independent r1 reproduction
matches all thirteen disassemblies and the identity manifest. Manifest SHA-256:
7537c04a2b8eb8e4ddbbd4e01d44c44f30412abede90a2da78660ee7576eaeea

```sh
uv run -m tools.inspect_item8_pool_elements --archive worldweaver-21.0.24.jar --class-name org/betterx/wover/entrypoint/BiomeDatapackRegistryEntrypoint.class --class-name org/betterx/wover/entrypoint/FeatureDatapackRegistryEntrypoint.class --class-name org/betterx/wover/entrypoint/ItemDatapackRegistryEntrypoint.class --class-name org/betterx/wover/entrypoint/PottableDatapackRegistryEntrypoint.class --class-name org/betterx/wover/entrypoint/StructureDatapackRegistryEntrypoint.class --class-name org/betterx/wover/entrypoint/SurfaceDatapackRegistryEntrypoint.class --class-name org/betterx/wover/entrypoint/Wover.class --class-name org/betterx/wover/entrypoint/client/LibWoverBlockClient.class --class-name org/betterx/wover/entrypoint/client/LibWoverCommonClient.class --class-name org/betterx/wover/entrypoint/client/LibWoverEventsClient.class --class-name org/betterx/wover/entrypoint/client/LibWoverUiClient.class --class-name org/betterx/wover/entrypoint/client/LibWoverWorldGeneratorClient.class --class-name org/betterx/wover/entrypoint/client/ModMenuEntryPoint.class --output evidence/raw/item8/wover-provider-entry-r1
```

This capture retains the seven automatic entries and all six providers declared
by the DatapackRegistryEntrypoint service. Wover installs the datapack listener,
block/item registry hooks, version tracking and seventeen module initializers.
The service providers initialize biome/data/modification, configured/placed
feature, enchantment, pottable plant/soil, structure/pool/set and surface-rule
registries. Client entries handle UI/configuration and preset selection.

These are entry boundaries, not yet a whole-provider disposition. Follow the
module initializers and generation registry registrations, reusing the existing
pool-codec and biome-modifier captures. Do not count codecs or reusable registry
managers as independent families merely because they support generation.
