# IDAS treetop tavern assessment

Nine remaining entries for four connected sections. Existing catalogs and
processor inspection suffice; no new runtime or measurement system.

## mob_source

Sections1,2,3 declare villagers; sections1,3,4 declare parrots and optional alexsmobs:toucan. AlexsMobs is absent in the frozen runtime, so toucan declarations are not confirmed inhabitants. Seats and display/painting entities are non-mob data. Each section has one empty entity NBT record; exact unresolved paths remain preserved without invented identities. No physical spawners. All select ticking-only waterlogging_fix_processor, with no mob NBT injection.

## loot_table_source

Four defined idas:chests/treetop_tavern/ sources: treetop_tavern in all four sections, treetop_tavern_bedroom in1,2,4,treetop_tavern_food in3,treetop_tavern_tools in2,4. Selected ticking-only processor assigns no loot NBT. Furnished source contents do not establish measured reward yield or operating machinery.

## generated_spawners

No ordinary/trial spawner blocks or generation markers across the four sections. Selected ticking-only processor introduces no spawner source. Non-mob seats and frames are not spawners.

## authored_or_natural_enemies

Authored villagers and parrots are habitation sources, not an authored hostile roster. Optional toucans have an absent provider; empty entity records supply no identity. Empty root spawn_overrides declares no family-specific natural override; environmental spawning remains separate.

## intended_hostility

Four-section furnished tavern with civilian/bird declarations and no authored hostile mob or spawner source. Preserve source limitations without claiming universally safe generated sites, a hostile dungeon or an Item9 tier.

## visual_discoverability

Elevated tavern architecture across four connected sections provides a broad structural cue. Nominal55 by52 footprint and37 height include padding and supports, not measured visible silhouette or sightlines. Tree cover and terrain can obscure access; no guaranteed visible entrance.

## underground_surface_classification

Surface-associated four-section tavern assembly. Root generic_structure projects WORLD_SURFACE_WG offset0,size4,terrain range12/radius1,biome radius1,ignore_waterlogging. Custom enhanced adaptation declares beards/carves,kernel size20/distance20. All sections rigid with nominal origins sharing y0. Actual terrain alteration, burial and full generated placement are unmeasured.

## Geometry and evidence

Family evidence binds templates-redacted, pool-traces-content and packaged JSON.
Under data/idas/structure/treetop_tavern/, section1 west_up connector0,0,0 meets
section2 east_up29,0,0, giving section2 origin-30,0,0. Section2 north_up28,0,0
meets section3 south_up28,0,25 at adjacent z-1, giving section3 origin-30,0,-26.
Section3 east_up29,0,25 meets section4 west_up0,0,25, giving section4 origin0,0,-26.
Names/targets match numbered next sections; all joints aligned. Template sizes
25,37,26;30,37,26;30,37,26;25,37,26 give union x-30..24,z-26..25,y0..36,
hence55 by52 horizontal and37 vertical. These are nominal complete layout extents,
not observed placement or terrain burial. Corresponding template_pool resources
have one rigid element each. Trace has no missing components or unresolved elements.

All select waterlogging_fix_processor; reuse the pinned ticking-only inspection
in idas-desert-market-assessment. It does not assign entity or loot NBT.
The four literal loot definitions exist under data/idas/loot_table/chests/
treetop_tavern/. Runtime Mod List absence of AlexsMobs is documented with exact
log identity in idas-ruins-of-the-deep-assessment. Optional toucans are not
confirmed generated inhabitants. Section1 /entities/7/nbt,section2 /entities/3/nbt,
section3 /entities/2/nbt,section4 /entities/3/nbt are empty dictionaries, not
unidentified mobs to invent. No spawner or structure-generation marker occurs.
No realized-population, reward-yield or sightline measurement is required here.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-treetop-tavern-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only treetop_tavern and input identity may change.
Final integration, acceptance and PR/review/main remain open.
