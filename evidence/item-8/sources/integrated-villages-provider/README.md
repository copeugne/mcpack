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
  --archive integrated_villages-1.3.3+1.21.1-neoforge.jar \
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

## Placement and existing geometry assessment

The current two-family batch began with18 outstanding attributes: ten village
and eight stronghold. Six are now integrated from existing evidence, without a
new measurement: both dimensions and village footprint, height, placement and
visual discoverability. Twelve remain: five village content attributes and
seven stronghold attributes. Earlier provider-discovery checkpoints above are
historical; provider discovery is closed in provider-scope.md.

All twelve village roots and the Integrated Stronghold root have effective biome
sets intersecting only captured Overworld dimension membership. This dimension
join establishes eligibility, not generation success. Village definitions all
request WORLD_SURFACE_WG projection. Airship start offset is100, pirate is-19,
and the other ten are0. The airship uses generic_structure, pirate uses
biome_facing_structure, Minka uses optional_dependency_structure and other roots
use generic_structure. Preserve these variant-level inputs. The name
sunken_village is not evidence of actual submerged placement.

The existing world-bounds artifact has one distinct full-start village layout,
repeated in run-a and run-b: ordinary seed42, `integrated_villages:airship_village`,
chunk6,23, decoded line14084 of each run's ordinary/chunks.jsonl. Its saved
piece envelope is[-18,138,281,174,203,465], or193x66x185 blocks (X,Y,Z).
This is one layout, not two independent samples. It supplies an approximate
family example without claiming every design, a typical village, occupied volume,
or complete population of all surrounding component chunks.

Buildings and paths provide potential settlement landmarks. Elevated airships
provide an aerial silhouette; lowered pirate components can have reduced exposure
from terrain or water. The airship example lies at Y138..203, but does not prove
visibility for other designs. No sightline or discovery-distance measurement is
required or inferred for this source-based description.

Remaining village content attribution must preserve actual packaged distinctions:
the reachable trace includes696 templates, optional-mod entities, fourteen
processor-list references, and one ordinary spawner in
`mossy_mounds/house/mossy_mounds_armorer_bottom`, block-entity index0 at[24,2,10].
Its SpawnData.entity is empty and SpawnPotentials is empty. Do not infer a hostile
population or silently replace that missing entity ID. Resolve relevant existing
processor and pool-element bindings before finalizing content attributes.
The132 literal loot-table references are already preserved by the trace/inventory;
join and describe them rather than rebuilding the extraction. Existing source
captures and packaged resources remain the first investigation path. No new
schema, validator or measurement system is needed merely to integrate these facts.

## Content assessment

The five remaining village content attributes are now integrated. This resolves
the village family, not Integrated Stronghold's seven remaining attributes.
No new runtime or measurement implementation was added.

The696 reachable-template trace contains civilian, animal, defensive and display
or contraption entities. The31 distinct packaged entity IDs are retained in the
mob_source attribute; these IDs are not31 mobs or an observed population.
The captured registry-r1 debug.log mod list, parsed by existing runtime_mod_ids,
has Create, Quark and Supplementaries, but lacks Alex's Mobs, Cobblemon, Guard
Villagers and Iron's Spellbooks. Consequently their template references are
optional authored candidates, not evidence of enabled entities in this stack.
The log SHA-256 is e5b47378d791027242ba28dd36c999c07ae4e01a1b90e1534e66bcd42c1e694b,
retained under the registry-r1 raw-custody manifest. All twelve village roots have
empty spawn_overrides; natural hazards are not excluded.

The armorer-bottom spawner identified in the previous assessment is configured
by its selected pool element: mossy_mounds/house/armorer_bottom.json uses
minecraft:single_pool_element, rigid projection and mossy_mounds_processor.
Processor index2 is integrated_api:spawner_randomizing_processor and references
integrated_villages:generic. The packaged integrated_structure_spawners/generic.json
contains zombie weight15 and skeleton weight10. These are selection inputs, not
observed population or a guarantee of a spawner in every village.

Direct SpawnerRandomizingProcessor.processBlock inspection shows that SpawnerBlock
inputs obtain fresh NBT from SetMobSpawnerEntity. It writes the selected entity
into SpawnData and one weight1 SpawnPotentials entry, plus delay20, minimum200,
maximum800, count4, nearby limit6, player range16, spawn range4 and block-light
range0..7. The initially empty template entity is therefore not the final
configured mob choice. A null manager selection replaces the block with its
configured replacement state, default air. The source does not prove actual
placement or successful live spawning.

MobSpawnerManager is a JSON reload listener for integrated_structure_spawners;
IntegratedAPI.registerDatapackListener registers its singleton. Loading parses
mobs, resolves entity types, removes zero-weight or unresolved entries, rejects
negative weights and logs parse failures. getSpawnerMob sums weights and selects
from the list. Missing lists log and fall back to the vanilla dungeon mob array;
a zero total returns null; selection exceptions log and return pig. Preserve
those failure branches rather than silently assuming a successful zombie choice.
The referenced zombie/skeleton list has positive weights and vanilla IDs.
Both directly inspected class member hashes are in processor_inspection.

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c \
  -classpath downloads/item3/candidates/integrated_api-1.7.3+1.21.1-neoforge.jar \
  com.craisinlord.integrated_api.world.processors.SpawnerRandomizingProcessor \
  com.craisinlord.integrated_api.misc.mobspawners.MobSpawnerManager
```

The reachable structure-block marker entries comprise15 CORNER,3 LOAD and1 SAVE,
with no DATA marker. They are retained authoring metadata, not additional
mob-spawn marker evidence. The settlement intent remains civilian with a local
hostile-spawner possibility in Mossy Mounds. Contraptions, displays and vehicles
are distinguished from enemies, and optional mod references remain scoped.

All132 literal reachable-template LootTable references have current-path packaged
loot_table definitions. The authoritative attribute lists the exact IDs, and
the preserved pool trace retains the template associations. This identifies
sources without claiming container placement, reward yield or applied changes
from the diagnostic loot-importer map described above. No baseline content was
repaired or enabled as part of this assessment.
