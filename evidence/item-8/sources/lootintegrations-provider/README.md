# Loot Integrations provider contribution

Selector ec856af captures all nine packaged classes. The ten generated files
reproduce exactly against independent r1 output. Manifest SHA-256:
0f49a269c6f23ed70f832752833a5c8c0d00a18f33737d147644015c5fe0c137.

```sh
uv run -m tools.inspect_item8_pool_elements --archive lootintegrations-1.21.1-4.7.jar --output evidence/raw/item8/lootintegrations-provider-r1
```

The mod registers EventHandler, which adds LootModifierManager as a resource
reload listener. The manager reads the loot resource directory and indexes
integration definitions. LootTableLootIntegrations invokes applyTo on generated
loot lists; the manager guards recursive application and calls doApply.
GlobalLootModifierIntegration combines/selects loot stacks with configured item
weighting, duplicate handling and item-count limits. These are modifications of
existing loot sources, not another generated building or encounter layout.

LootContextMixin carries the no-map flag. ExplorationFunctionMixin returns an
empty item for map generation when that flag is set, avoiding additional map
searches in the integration path. Original loot and integrated additional loot
must remain distinguished. The context flag is not a blanket ban on all maps.

The 43 packaged integration definitions use loot_table, integrated_loot_tables
and max_result_itemcount. Seven packaged chest tables are integration targets;
the ignored-item tag names barrier. Addon definitions already inventoried remain
attribute inputs through this loader. This closes the core contribution route,
not empirical reward-frequency, loot-economy or family-attribute completion.
