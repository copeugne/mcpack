# Compound biome predicate

Captured with the existing extractor at `a91ff8b`. Exact archive, class and
disassembly hashes are recorded in `identities.json`.

```sh
uv run -m tools.inspect_item8_pool_elements --archive Zeta-1.1-40.jar --class-name org/violetmoon/zeta/config/type/CompoundBiomeConfig.class --output evidence/raw/item8/zeta-compound-biome-a91ff8b-reproduction
```

The reproduction matched the captured identities and disassembly byte for byte.
The initial manual hash command mistakenly named `manifest.json`; this extractor
writes `identities.json`. No capture failed or was rewritten.

`canSpawn` rejects a null holder and requires both the tag predicate and the
explicit-biome predicate to pass. `fromBiomeReslocs` constructs an empty tag
blacklist and passes its supplied boolean and names to StrictBiomeConfig.
`onReload` delegates to both component configurations. Their actual predicate
implementations and effective configuration binding still require attribution;
the empty blacklist alone is not accepted as proof of effective applicability.

This capture addresses Item 8's biome constraints for the directly referenced
Spiral Spires configuration. It does not establish runtime generation or add a
family. The next direct dependencies are BiomeTagConfig and StrictBiomeConfig.
