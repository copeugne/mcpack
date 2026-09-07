# IDAS Tudor pub assessment

Nine remaining entries for two connected sections. Existing catalogs and
processor inspection suffice; no new runtime or measurement system.

## mob_source

Main authors villagers, Create seats and guardvillagers:guard; bottom has no authored entities. GuardVillagers is absent from the frozen runtime, so its guard declaration is not a confirmed inhabitant. Main /entities/6/nbt is empty and supplies no recoverable identity. Seats are not mobs. Selected generic_processor schedules dispenser ticks and randomizes existing ordinary spawners, but neither template has a spawner input.

## loot_table_source

Five defined tables under idas:chests/tudor_pub/: tudor_pub_barrel in bottom, tudor_pub_bedroom and tudor_pub_kitchen in main, tudor_pub_storage and tudor_pub_treasure in both. Selected processor assigns no container loot NBT. These are source attributions, not measured reward yield or operating pub machinery.

## generated_spawners

Neither template has physical ordinary/trial spawners or generation markers. Both select generic_processor, whose ordinary spawner randomizer acts on existing spawner blocks. With no spawner input, its idas:generic list does not establish generated spawners or enemies here. Dispenser ticking is a separate processor action.

## authored_or_natural_enemies

No authored hostile mob or spawner source identified. Villagers and non-mob seats remain distinct from the absent-provider guard declaration and empty entity record. Empty root spawn_overrides declares no family-specific natural override; ordinary environmental spawning remains possible.

## intended_hostility

Furnished civilian pub with bedroom,kitchen,storage and lower-section loot sources. No authored hostile entity or physical spawner source supports a hostile dungeon claim. Preserve the absent guard limitation without assigning an Item9 tier or guaranteeing every generated site is safe.

## visual_discoverability

Surface-associated pub architecture offers a building cue while the lower component can remain concealed. Nominal35 by25 horizontal and32 vertical extents include the lower section and template padding, not a measured silhouette or sightline. Terrain and vegetation may obscure the entrance.

## underground_surface_classification

Surface-associated pub with attached lower section. Root generic_structure projects WORLD_SURFACE_WG offset0,size2,beard_thin adaptation,terrain range10/radius1,biome radius1,ignore_waterlogging. Rigid lower component has nominal origin eleven blocks below main; actual terrain burial and full generated placement are not measured.

## Geometry and evidence

Family evidence binds templates-redacted, pool-traces-content and packaged JSON.
Under data/idas/structure/tudor_pub/, tudor_pub.nbt is35,21,25 with down_south
aligned connector at1,0,24; tudor_pub_bottom.nbt is19,11,25 with up_south aligned
connector at1,10,24. Both name/target idas:tudor_pub. Adjacent connection gives
bottom origin0,-11,0 relative to main0,0,0. Inclusive union x0..34,z0..24,y-11..20
is35 by25 horizontal and32 vertical. This describes the nominal complete assembly,
not measured generated extent or guaranteed bottom placement. Corresponding
worldgen/template_pool/tudor_pub resources each contain one rigid element and
empty fallback. Trace contains no missing components or unresolved elements.

Both pools select data/idas/worldgen/processor_list/generic_processor.json. It
contains dispenser ticking and ordinary spawner randomization only. Reuse the
pinned TickBlocksProcessor inspection in idas-desert-market-assessment and the
SpawnerRandomizingProcessor inspection in integrated-villages-provider: the
latter requires an existing SpawnerBlock input. None exists in either template;
a configured randomizer is not an encounter source by itself. The five literal
loot definitions exist under data/idas/loot_table/chests/tudor_pub/.

Main /entities/6/nbt is an empty dictionary, not an unidentified mob to invent.
Existing registry-r1 Mod List inspection confirms Create and excludes
GuardVillagers; see idas-ruins-of-the-deep-assessment for exact log identity.
No content repair, reward-yield measurement or new runtime capture is needed.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-tudor-pub-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only tudor_pub and input identity may change.
Final integration, acceptance and PR/review/main remain open.
