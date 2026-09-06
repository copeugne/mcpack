# Integrated Villages remaining provider code

Extractor dcff873 captures the eleven previously uncaptured classes. Together
with integrated-village-suppression, this covers all fourteen packaged classes.
The independent r1 extraction reproduced all generated files byte for byte
before this README was added. Manifest SHA-256:
b7edce7fe258c480a4b60ad5869b379a9501ea9f7d02e5ed287519f4122334c9.
Archive SHA-256:
b53a485828da352b1a6a24cd2796aacf5d8360632b98c7dfba295f235d41ec00.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --class-name architectury_inject_IntegratedVillages_common_dac55d1c3d7c43d0b24fcf81e4608720_81a8cfc75ab7849b22873acf463ab0d4326a7a023946e85fdc1fb3c982d0127bintegrated_villages1331211commondevjar/PlatformMethods.class \
  --class-name com/craisinlord/integrated_villages/IntegratedVillages.class \
  --class-name 'com/craisinlord/integrated_villages/config/ConfigModule$General.class' \
  --class-name com/craisinlord/integrated_villages/config/ConfigModule.class \
  --class-name com/craisinlord/integrated_villages/config/IntegratedVillagesConfigNeoforge.class \
  --class-name com/craisinlord/integrated_villages/lootmanager/StructureModdedLootImporter.class \
  --class-name com/craisinlord/integrated_villages/mixins/LocateVillagesCommandMixin.class \
  --class-name com/craisinlord/integrated_villages/neoforge/IntegratedVillagesNeoforge.class \
  --class-name 'com/craisinlord/integrated_villages/pooladditions/PoolAdditionMergerManager$AdditionalStructureTemplatePool$ExpandedPoolEntry.class' \
  --class-name 'com/craisinlord/integrated_villages/pooladditions/PoolAdditionMergerManager$AdditionalStructureTemplatePool.class' \
  --class-name com/craisinlord/integrated_villages/pooladditions/PoolAdditionMergerManager.class \
  --output evidence/raw/item8/integrated-villages-provider-r1
```

The NeoForge constructor calls common initialization and configuration setup.
Common initialization calls createMap (discarding its result) and registers the
server-start callback. That callback invokes the pool merger and, only in a
development environment, loot diagnostics. Neither entry registers a resource
reload listener. The generated platform bridge identifies NeoForge. Configuration
classes expose village suppression and Create contraption activation settings.
Reuse the prior frozen configuration and suppression evidence.

The pool merger consumes integrated_villages_pool_additions. Its apply method
sets cachedMap; the server-start merger parses only when that map is non-null.
Parsing reads target_pool before its codec exception handler. The pool codec
requires target_pool, fallback and elements; each expanded entry reads element,
weight and an optional condition resource ID. The condition ID looks up an
Integrated API condition supplier. Missing suppliers log an error and return
true, as do absent conditions. required_mod is not that condition field.

The four packaged addition declarations instead use name and required_mod.
They cannot be accepted as shaped by the captured parser. Their intended targets
are the Mediterranean bakery, pirate market, tavern market and tavern well.
They are existing-village component declarations, not independent roots. Do not
claim they are simply disabled by absent Bakery, Sawmill or Waystones mods.
No listener activation or observed runtime parse failure is established by this
capture; preserve the field mismatch separately from activation. Do not repair
the frozen input or invent successful injections.

LocateVillagesCommandMixin rejects direct locate keys for the same five vanilla
and two Terralith villages addressed by the existing suppression evidence when
disableVanillaVillages is enabled. This does not create a family. Keep direct-key
behavior distinct from tag lookup and actual generation.

StructureModdedLootImporter builds tavern and blacksmith mappings to vanilla
village loot, plus two Better Strongholds mappings when that mod is loaded.
Its table-checking path is diagnostic. The inspected entry does not register a
loot mutation callback; a map declaration alone does not prove applied loot.
Shared Integrated API consumers remain a separate open provider row.

This is an isolated source-evidence increment. Root/component accounting and the
provider disposition are not closed by this capture alone.

The generated ExpandedPoolEntry disassembly retains javap's final blank line.
The resulting diff-check whitespace warning is preserved with the raw bytes.
