# Configuration event and nested fields

Captured at `b916f24`. Exact identities are in `identities.json`. Verbose output
is required for annotations and callback bootstrap targets. Earlier ordinary
captures remain preserved and reproduce with their recorded extractor revisions.
This capture reproduced byte for byte:

```sh
uv run -m tools.inspect_item8_pool_elements --archive Zeta-1.1-40.jar --class-name org/violetmoon/zetaimplforge/config/ConfigEventDispatcher.class --class-name org/violetmoon/zeta/config/type/DimensionConfig.class --class-name org/violetmoon/zeta/config/type/CompoundBiomeConfig.class --class-name org/violetmoon/zeta/config/type/BiomeTagConfig.class --class-name org/violetmoon/zeta/config/type/StrictBiomeConfig.class --output evidence/raw/item8/zeta-config-event-fields-b916f24
```

## Field mapping

DimensionConfig annotates dimensions and isBlacklist. CompoundBiomeConfig
annotates tags and biomes as nested configuration objects. BiomeTagConfig names
biomeTagStrings as `Biome Tags`; StrictBiomeConfig names biomeStrings as
`Biomes`. Both annotate isBlacklist. The previously captured ConfigObjectMapper
uses an explicit annotation name when present, otherwise splits camel case and
capitalizes words. It recursively processes IConfigType objects. Thus the leaf
names match `Dimensions`, `Is Blacklist`, `Biome Tags` and `Biomes` in the
frozen Quark file. SpiralSpiresModule's rarity and radius similarly map to
`Rarity` and `Radius`. Parent section naming and effective file provenance must
still be reconciled before declaring all frozen values effective.

## Observed initial refresh

ConfigEventDispatcher.commonSetup enqueues the captured lambda. It logs initial
refresh, calls ConfigManager.onReload, fires ForgeZConfigChange, and on the
server side logs that it is waiting for server start. The preserved registry-r1
debug log contains both Quark messages in that order at lines 16583 and 16584.
This establishes passage through the refresh call, not a runtime field dump.

The log is retained through the existing registry-r1 custody archive. Restored
path: `evidence/raw/item8/custody-r1/restored-download/debug.log`; SHA-256:
`e5b47378d791027242ba28dd36c999c07ae4e01a1b90e1534e66bcd42c1e694b`.
Recheck the preserved lines and identity with:

```sh
sha256sum evidence/raw/item8/custody-r1/restored-download/debug.log
sed -n '16583,16584p' evidence/raw/item8/custody-r1/restored-download/debug.log
```

No new runtime or measurement system was used. This closes the initial-refresh
execution gap and leaf annotation mapping only. It does not establish spire
occurrence, full provider coverage or Item 8 completion.
