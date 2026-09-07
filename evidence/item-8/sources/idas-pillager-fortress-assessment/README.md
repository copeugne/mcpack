# IDAS pillager fortress assessment

Seven remaining entries for one eight-component family. Accepted geometry is
reused; no runtime capture or measurement system added.

## mob_source

Pieces1 through4 author evokers, pillagers, vindicators, ravagers and a zoglin, alongside villagers, an iron golem and non-mob decorative/Create entities. Seven AlexsMobs entity IDs are declared but that mod is absent from the frozen runtime. Twelve entity compounds lack IDs (four in piece1, eight in piece3); retain their exact source paths without inventing identities or counting successful mobs. Pieces5 through8 have no authored entities. Ordinary spawner sources are assessed separately; no realized population is claimed.

## loot_table_source

Six literal table IDs occur in pieces1 through4. Four definitions exist under idas:chests/pillager_fortress/: pillager_basic, pillager_bedroom, pillager_jail and pillager_library. Legacy idas:chests/idasbasic (piece1) and idas:chests/pillagerjail (piece3) have no definition in the preserved packaged JSON catalog. Keep these dangling references as baseline defects rather than substituting similarly named tables. Pieces5 through8 have no literal loot references. Selected processor declares optional decorative block replacements and spawner randomization, with no loot NBT assignment. Reward yield is not measured.

## generated_spawners

Fourteen physical ordinary pillager spawners across pieces1 through4 (6,1,6,1), none in pieces5 through8 and no trial spawners. All eight pools select idas:pillager_processor; its randomizer uses idas:pillager, containing only minecraft:pillager weight15. Delay20,min200,max800,count4,nearby6,player range16,spawn range4,block-light0..7. Reuse the existing Integrated API spawner/manager inspection and fallback limits. Three structure-block markers, in pieces2,6,8, are CORNER mode with empty metadata, not DATA enemy instructions. Physical source count is not realized spawner population.

## authored_or_natural_enemies

Direct authored illagers, ravagers and zoglin plus processor-selected pillager spawners establish hostile sources. Absent-provider animals and ID-less entity compounds do not establish successful enemies. Villagers, iron golem and non-mob entities remain distinct. Empty root spawn_overrides means no family-specific natural spawning override; ordinary environmental spawning remains possible.

## intended_hostility

Connected fortified illager complex with direct hostile mobs, ordinary pillager spawners and differentiated jail, bedroom and library loot sources. Hostile expedition content is supported by source evidence without assigning an Item9 tier or claiming measured combat intensity, encounter success or complete population.

## visual_discoverability

Large surface-associated fortress assembly provides architectural cues; accepted saved-piece sample spans63 by63 blocks horizontally and89 vertically. These are layout extents, not a visible silhouette or sightline measurement. Terrain and vegetation may conceal parts; no guaranteed visible entrance is claimed.

## underground_surface_classification

Surface-associated integrated_api:generic_structure: WORLD_SURFACE_WG offset0,size8,fixed rotation,beard_thin adaptation,terrain range10/radius3,biome radius1,ignore_waterlogging. Eight connected templates are components of one fortress. Accepted sampled saved-piece bounds are reused; source settings and full start chunk do not prove every component populated or establish burial depth.

## Evidence and dispositions

Use the hash-bound pool-traces-content and templates-redacted catalogs in this
family's evidence map. Root idas:pillager_fortress reaches templates
idas:pillager_fortress/pillager_fortress1 through8 without missing pool components
or unresolved pool elements. The twelve ID-less entity paths remain in
mob_source.unresolved_authored_entities. Direct template inspection shows that
all twelve nbt compounds are empty dictionaries, so they supply no recoverable
entity identity. Their original records are not repaired.
CORNER markers are piece2 /block_entities/44, piece6 /block_entities/7 and
piece8 /block_entities/1, all with empty metadata.

Packaged JSON data/idas/worldgen/processor_list/pillager_processor.json declares
two AlexsMobs-required gray wool/carpet replacements and the ordinary spawner
randomizer. data/idas/integrated_structure_spawners/pillager.json declares the
sole pillager weight15. Reuse integrated-villages-provider/README.md's pinned
SpawnerRandomizingProcessor and MobSpawnerManager inspection. Frozen registry-r1
Mod List has Create and Quark, without AlexsMobs; optional animals are declarations,
not confirmed generated mobs. The two absent legacy loot definitions are preserved
source defects, not requests to tune or repair this frozen baseline. Neither
missing loot nor malformed entities makes the entire family inactive.

Geometry custody and inclusive saved-piece derivation remain in
idas-existing-world-geometry/README.md and the family's bound manifest/restore
references. No sightline, reward yield or realized enemy count is needed here.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-pillager-fortress-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only pillager_fortress and input identity may change.
Final integration, acceptance and PR/review/main remain open.
