# IDAS farmhouse assessment

Nine remaining entries for two alternatives and an ordinary-only path. Existing
catalogs and processor inspection suffice; no new runtime or measurement system.

## mob_source

Ordinary farmhouse authors villagers and pigs, plus non-mob seats,armor stand and Quark glass frames. Six ordinary entity records have empty NBT compounds and supply no recoverable identity. Abandoned farmhouse and path have no authored entities. Abandoned separately has two ordinary zombie-villager spawners. All select ticking-only waterlogging_fix_processor, with no mob NBT injection or spawner randomization.

## loot_table_source

Four defined idas:chests/farmhouse/ sources: farmhouse in both building alternatives, farmhouse_bedroom,farmhouse_food,farmhouse_mill only in ordinary. Path has no literal loot reference. Selected ticking-only processor assigns no loot NBT. Sources do not measure yields or prove operating farm/mill machinery.

## generated_spawners

Abandoned farmhouse contains two ordinary spawners with SpawnData entity minecraft:zombie_villager and empty SpawnPotentials; selected ticking-only processor does not randomize these. Ordinary farmhouse and path have no spawners; no trial spawners. Ordinary /block_entities/42 is a CORNER marker with empty metadata, not a DATA enemy instruction. Two source blocks are not measured successful spawners.

## authored_or_natural_enemies

Ordinary alternative has civilian villagers and pigs, with non-mob furnishings; abandoned has authored zombie-villager spawner sources. Do not average these alternatives into one uniform hostility claim. Empty root spawn_overrides declares no family-specific natural override; environmental spawning remains separate.

## intended_hostility

One farmhouse design with inhabited and abandoned alternatives, weighted4 and1 in the start pool. Civilian ordinary contents differ from abandoned zombie-villager spawners. Preserve this contrast without assigning an Item9 tier or treating weights as measured encounter frequencies.

## visual_discoverability

Farmhouse building and tower provide architectural cues, with an attached path only for the ordinary variant. Nominal extents are ordinary52 by40,height44 and abandoned48 by40,height47, including padding rather than measured visible silhouette. Terrain and vegetation may obscure access; no sightline measurement.

## underground_surface_classification

Surface-associated farmhouse. Root generic_structure projects WORLD_SURFACE_WG offset0,size2,beard_thin adaptation,terrain range10/radius1,biome radius1,ignore_waterlogging. All pool elements rigid. Ordinary path shares nominal origin height; abandoned has no path connector. Actual terrain burial and complete placement are unmeasured.

## Geometry and evidence

Family evidence binds templates-redacted, pool-traces-content and packaged JSON.
Under data/idas/structure/farmhouse/, farmhouse.nbt is48,44,40 with west_up aligned
connector at0,1,25; farmhouse_path.nbt is4,6,23 with east_up aligned connector
at3,1,14. Both name/target idas:farmhouse_path. Adjacent connection yields path
origin-4,0,11 relative to building0,0,0, hence union x-4..47,z0..39,y0..43.
abandoned_farmhouse.nbt is48,47,40 and has no jigsaw connector. Its extent is
independent and does not acquire the ordinary path merely because that path is
reachable elsewhere in the family graph. Both are nominal layouts, not observed
placement or terrain burial.

worldgen/template_pool/farmhouse/farmhouse.json has ordinary weight4 and
abandoned weight1; farmhouse_path.json has one element. All rigid, empty fallback,
waterlogging_fix_processor. No missing components or unresolved pool elements.
Reuse the pinned ticking-only processor inspection in idas-desert-market-assessment;
it does not randomize abandoned spawners or assign entity/container-loot NBT.
The four literal loot definitions exist under data/idas/loot_table/chests/farmhouse/.

Ordinary /entities/9,11,13,15,17,19/nbt are empty dictionaries; retain raw paths
without inventing identities. /block_entities/42 is CORNER with empty metadata.
Abandoned spawners both declare zombie_villager in SpawnData and empty potentials.
This source assessment does not prove realized spawns, operation of machinery,
reward yields or the start-pool weights as observed frequencies.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-farmhouse-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only farmhouse and input identity may change.
Final integration, acceptance and PR/review/main remain open.
