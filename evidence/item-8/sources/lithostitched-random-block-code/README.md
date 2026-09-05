# Random block provider contribution

Executed successfully using existing tool `5ae4555`, into an absent directory:

```sh
uv run -m tools.inspect_item8_pool_elements --archive lithostitched-1.7.10+beta4-neoforge-21.1.jar --class-name dev/worldgen/lithostitched/worldgen/stateprovider/RandomBlockProvider.class --output evidence/item-8/sources/lithostitched-random-block-code
```

The extractor verified the retained archive and recorded the class and
disassembly hashes. Identities SHA-256:
`03ae09f76ee50c52058b4cb0818fab9ab2a2ffbe458676a3a4020f9bed127c8d`.
Both `getState` overloads choose a member of the configured block holder set
and return its default state, or air if selection is empty. The observed swamp
composite config supplies green and blue bioshroom blocks. This provider does
not add another feature, template, entity, spawner or loot source.

Scoped Ruff and basedpyright passed. This is the last unresolved custom state
provider in the 34 selected feature-modifier paths, not a new measurement
system or a proof of coverage outside those paths.
