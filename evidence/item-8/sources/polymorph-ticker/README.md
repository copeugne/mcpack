# Polymorph watched-block ticker

Extractor 5b9df861. Independent r1 reproduction matches source and manifest
bytes. Manifest SHA-256:
4c2aec52aa80a246dfbaf8db7c24aebc2cd91c8de42cce63cc76cd5d3ca66602

```sh
uv run -m tools.inspect_item8_pool_elements --archive polymorph-neoforge-1.1.0+1.21.1.jar --class-name com/illusivesoulworks/polymorph/common/util/BlockEntityTicker.class --output evidence/raw/item8/polymorph-ticker-r1
```

The ticker starts with an empty map of existing block entities and recipe-data
objects. It removes invalid entries and ticks the registered recipe data. This
is consumer recipe-state maintenance, not a generation registry or placement
path. Do not expand membership into generic recipe-data implementation tracing.
