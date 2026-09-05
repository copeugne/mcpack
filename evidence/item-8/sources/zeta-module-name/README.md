# Module name derivation

Captured at `b38d3f4`; identities are in `identities.json`. Reproduction matched:

```sh
uv run -m tools.inspect_item8_pool_elements --archive Zeta-1.1-40.jar --class-name org/violetmoon/zeta/module/TentativeModule.class --output evidence/raw/item8/zeta-module-name-b38d3f4
```

TentativeModule.from derives the display name from the class simple name when
the annotation name is empty: remove trailing Module, split camel case, then
capitalize words. It always derives lowercaseName from the resulting display
name using Locale.ROOT lowercasing and space-to-underscore replacement.
Spiral Spires therefore maps to spiral_spires. The preserved registry-r1 debug
log confirms that the manager constructed the module under that display name:

```sh
rg -n 'Constructing module Spiral Spires' evidence/raw/item8/custody-r1/restored-download/debug.log
```

The debug-log hash and custody are recorded in
`../zeta-config-event-fields/README.md`. The manager assignment, ConfigManager
section construction, module's world category annotation, nested mapper naming,
leaf annotations, loaded frozen-file identity and observed initial refresh are
preserved in the adjacent configuration captures. Together these resolve the
section-name gap for world.spiral_spires. This does not prove world occurrence
or natural mob composition.
