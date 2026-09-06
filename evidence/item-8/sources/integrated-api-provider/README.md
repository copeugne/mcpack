# Integrated API contribution sources

Extractor df8d1dd. The manifest and all 30 disassemblies independently
reproduce byte for byte. Manifest SHA-256:
fa79c4ec7cb6bc0ec4b3c537a36d1ef725a89189d1cc4ae1762fbf5a39310f5e

```sh
uv run -m tools.inspect_item8_pool_elements --archive integrated_api-1.7.3+1.21.1-neoforge.jar --class-name com/craisinlord/integrated_api/IntegratedAPI.class --class-name com/craisinlord/integrated_api/datagen/StructureNbtUpdaterDatagen.class --class-name com/craisinlord/integrated_api/mixins/blocks/StructureBlockUnlimit.class --class-name com/craisinlord/integrated_api/mixins/blocks/UpdateStructureBlockUnlimit.class --class-name com/craisinlord/integrated_api/mixins/entities/BlockAttachedEntityMixin.class --class-name com/craisinlord/integrated_api/mixins/entities/MerchantOfferAccessor.class --class-name com/craisinlord/integrated_api/mixins/entities/ShulkerEntityInvoker.class --class-name com/craisinlord/integrated_api/mixins/features/DungeonFeatureAccessor.class --class-name com/craisinlord/integrated_api/mixins/features/NoGeodesInStructuresMixin.class --class-name com/craisinlord/integrated_api/mixins/items/MapItemAccessor.class --class-name com/craisinlord/integrated_api/mixins/neoforge/structures/StructurePoolMixin.class --class-name com/craisinlord/integrated_api/mixins/resources/LootContextAccessor.class --class-name com/craisinlord/integrated_api/mixins/resources/NamespaceResourceManagerAccessor.class --class-name com/craisinlord/integrated_api/mixins/resources/ReloadableResourceManagerImplAccessor.class --class-name com/craisinlord/integrated_api/mixins/structures/BeardifierAccessor.class --class-name com/craisinlord/integrated_api/mixins/structures/BeardifierMixin.class --class-name com/craisinlord/integrated_api/mixins/structures/DisableStructuresMixin.class --class-name com/craisinlord/integrated_api/mixins/structures/JigsawJunctionAccessor.class --class-name com/craisinlord/integrated_api/mixins/structures/JigsawPlacementUnlimit.class --class-name com/craisinlord/integrated_api/mixins/structures/ListPoolElementAccessor.class --class-name com/craisinlord/integrated_api/mixins/structures/LocateCommandMixin.class --class-name com/craisinlord/integrated_api/mixins/structures/PoolElementStructurePieceAccessor.class --class-name com/craisinlord/integrated_api/mixins/structures/SinglePoolElementAccessor.class --class-name com/craisinlord/integrated_api/mixins/structures/StructureManagerAccessor.class --class-name com/craisinlord/integrated_api/mixins/structures/StructurePieceAccessor.class --class-name com/craisinlord/integrated_api/mixins/structures/StructurePoolAccessor.class --class-name com/craisinlord/integrated_api/mixins/structures/StructureProcessorAccessor.class --class-name com/craisinlord/integrated_api/mixins/structures/StructureTemplateManagerAccessor.class --class-name com/craisinlord/integrated_api/mixins/structures/TemplateAccessor.class --class-name com/craisinlord/integrated_api/neoforge/IntegratedAPINeoforge.class --output evidence/raw/item8/integrated-api-provider-r1
```

This generated increment preserves common and NeoForge initialization, the
data-generation entry and all 27 declared common hooks as one contribution
boundary. Existing pool-codecs sources remain authoritative for the previously
captured pool element and piece registration; they are not duplicated here.

The entry registers shared type, placement, processor, rule and condition
registries. Hooks modify existing generation, lookup and structure-block tools.
Reload listeners consume spawner, map-trade, piece-count and workstation data.
No independent authored layout is present in this capture. Provider closure
requires the separate complete payload and source binding check.
