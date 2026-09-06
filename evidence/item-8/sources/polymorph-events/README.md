# Polymorph event membership boundary

Extractor ecc5844b. Independent r1 reproduction matches source and manifest
bytes. Manifest SHA-256:
a37f284baa4eff32985d132cc896d54c53141bb0b8e4cd916792fe9a49275a49

```sh
uv run -m tools.inspect_item8_pool_elements --archive polymorph-neoforge-1.1.0+1.21.1.jar --class-name com/illusivesoulworks/polymorph/common/PolymorphCommonEvents.class --class-name com/illusivesoulworks/polymorph/common/integration/fastbench/FastBenchModule.class --output evidence/raw/item8/polymorph-events-r1
```

Common events handle disconnect/container state and call BlockEntityTicker for
watched block entities. FastBench support selects an existing recipe and updates
the result slot and player packet. Remaining runtime membership boundary is
the watched-block ticker, not generic recipe assembly or compatibility APIs.
