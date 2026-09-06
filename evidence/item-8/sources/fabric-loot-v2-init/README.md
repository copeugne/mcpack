# fabric-loot-v2-init source roles

Captured with extractor fa3226d. Existing independent r1 reproduction matches
the identity manifest and every disassembly byte for byte. Manifest SHA-256:
fdd70793358e39363a47a89dea1e357a60bbc26f051d182c66c7fd97c7be0d6e.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-loot-api-v2-3.0.15+a3ee712d19.jar --class-name net/fabricmc/fabric/impl/loot/v2/LootInitializer.class --output evidence/raw/item8/fabric-loot-v2-init-r1
```

The initializer forwards v3 replace, modify and all-loaded events to registered v2 consumers, converting the source enum. It supplies no structure or loot content of its own. Consumer loot effects remain attribute inputs.

This is source evidence for the existing Fabric provider check, not whole-provider
closure or proof of effective consumer behavior.
