# BetterEnd common entry consumers

Selector 2d22b8e captures eight common entry classes. All nine generated files
(eight disassemblies and identities.json) reproduce byte for byte against the
independent r1 capture. Manifest SHA-256:
6d435ffdd62550e6baaeaf9ba27638701a30938773828ff0a901f5c6d14e373f.

```sh
uv run -m tools.inspect_item8_pool_elements --archive BetterEnd-21.0.31.jar --class-name org/betterx/betterend/registry/EndBiomes.class --class-name org/betterx/betterend/registry/EndPortals.class --class-name org/betterx/betterend/commands/CommandRegistry.class --class-name 'org/betterx/betterend/commands/CommandRegistry$1.class' --class-name org/betterx/betterend/integration/Integrations.class --class-name org/betterx/betterend/integration/EndBiomeIntegration.class --class-name org/betterx/betterend/util/LootTableUtil.class --class-name org/betterx/betterend/api/BetterEndPlugin.class --output evidence/raw/item8/betterend-common-entries-r1
```

CommandRegistry registers portal-location and biome-teleport commands. Its
anonymous Result implementation adapts the selected biome. EndPortals loads
portal destination, item and color settings; these entry methods do not define
another authored structure placement route.

EndBiomes maintains a separate cave-biome picker using EndTags.IS_END_CAVE and
a seeded cave map. The six cave biomes absent from the captured surface biome
source cannot be declared globally unreachable on that absence alone. Cave
feature consumers still require reconciliation.

Integrations.init does not register its packaged guidebook lambda. Static
initialization does register BYGIntegration, FlamboyantRefabricatedIntegration
and DyeDepotIntegration through BCLib. Their concrete activation and consumers
remain separate unresolved inputs. EndBiomeIntegration is an interface, and
BetterEndPlugin supplies empty defaults plus a dispatcher to overriding plugin
methods. Empty defaults do not prove absence of retained service providers.

LootTableUtil.init registers a loot-table listener. Its callback compares the
ResourceKey constants END_CITY_TREASURE and FISHING against the ResourceLocation
returned by the event. Preserve this apparent type mismatch for the later loot
attribute pass; do not assume the advertised modifications are effective or
repair the frozen baseline. The separate biome chest-table selector is not
invalidated by that observation.

This capture closes only these entry interpretations. It does not establish
whole-provider completeness, resolve shared integration activation, or add a
canonical family. The already reconciled 128 packaged templates stay closed.
