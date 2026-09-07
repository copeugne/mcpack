# Component biome filters

Captured using the existing extractor at `972de0e`. Archive, class and output
hashes are preserved in `identities.json`. Reproduction matched both captures
and their identities byte for byte:

```sh
uv run -m tools.inspect_item8_pool_elements --archive Zeta-1.1-40.jar --class-name org/violetmoon/zeta/config/type/BiomeTagConfig.class --class-name org/violetmoon/zeta/config/type/StrictBiomeConfig.class --output evidence/raw/item8/zeta-component-biomes-972de0e-reproduction
```

BiomeTagConfig rejects a null holder. It lazily builds tag keys from its string
list, returns the inverse of isBlacklist for a matching tag, and returns
isBlacklist when none matches. Consequently an empty tag blacklist passes every
non-null holder. Reload rebuilds the tag-key list.

StrictBiomeConfig unwraps the holder and maps its two alternatives. Its
ResourceKey lambda compares the key's location string with biomeStrings and
returns membership XOR isBlacklist. Its direct Biome lambda returns false.
CompoundBiomeConfig, preserved in `../zeta-compound-biome`, requires both
component predicates and rejects null before invoking either.

For the already preserved SpiralSpiresModule constructor defaults, the tag
component is an empty blacklist and the named-biome component is an allowlist
containing minecraft:end_highlands. This source-derived filter admits that
registered biome and excludes other registered biome names. The frozen Quark
file records the same values. Effective configuration binding remains open;
matching defaults and file values do not themselves prove the runtime fields.
The generator's existing Y=256 sample and End Stone search remain separate
placement conditions. This capture does not establish observed generation.
