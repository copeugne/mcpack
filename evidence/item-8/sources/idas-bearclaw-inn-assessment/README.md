# IDAS Bearclaw Inn assessment

Seven remaining entries integrated for one connected lodge/path/stables family.
Previously accepted sampled geometry in idas-existing-world-geometry is reused.
No new runtime capture, renderer or measurement system is needed.

## mob_source

Lodge authors villagers and non-mob Quark glass frames; stables author horse, mule and pig. Path has no additional authored entity source. No unresolved entity compounds or missing components. Selected waterlogging_fix_processor only schedules dispenser/dropper ticks; it does not substitute entities. Source declarations are not measured populations.

## loot_table_source

Lodge references defined idas:chests/bearclaw_inn/bearclaw_inn_bedroom and idas:chests/bearclaw_inn/bearclaw_inn_food. Path/stables add no literal loot table; selected ticking processor adds no loot NBT. Furnishings and fixed contents are separate from realized table yields.

## generated_spawners

No ordinary or trial spawners across lodge/path/stables. Lodge structure-block marker at block_entities/119, position34,7,21, uses CORNER with empty metadata and name minecraft:bearclaw_inn_path. This authoring marker is not a DATA enemy instruction or additional family. Selected ticking processor introduces no spawner.

## authored_or_natural_enemies

Authored villagers and stable animals are distinguished from non-mob glass frames. No identified authored hostile entity or spawner; root spawn_overrides is empty. Ordinary environmental spawning remains possible, and template inhabitants do not prove runtime population.

## intended_hostility

Furnished inn with connected path/stables, civilian and animal source declarations, and bedroom/food loot. No identified authored hostile encounter source. This does not guarantee a safe settlement, functioning services or a measured combat tier.

## visual_discoverability

Lodge building, connecting path and separate stable yard provide settlement cues distinct from a single isolated house. Terrain and vegetation can hide parts of the assembly. No measured sightline, visible route guarantee or actual service availability is established.

## underground_surface_classification

Surface-associated lodge assembly: generic_structure root projects to WORLD_SURFACE_WG at offset0, size3, beard_thin, terrain range10/radius1 and biome radius1. Accepted sampled piece envelope is separate from measured terrain burial or complete population of every component chunk.

## Evidence

The complete three-template graph has no missing or unresolved components.
The lodge marker is preserved exactly in pool-traces-content.json.gz; its CORNER
mode and empty metadata are authoring data, not a DATA generation command.
No marker is deleted from raw or generated-spawner source records.

All selected elements use idas:waterlogging_fix_processor, whose sole ticking
processor preserves incoming block info. Reuse its direct class identity and
inspection in idas-desert-market-assessment. Both lodge loot-table definitions
exist in packaged-json-redacted.json.gz. Template entity and loot mappings remain
explicit in the authoritative inventory, with non-mob frames distinguished.
Existing rationale and views preserve the connected lodge/path/stable design.
No working services, animal counts, rewards or visibility measurements are inferred.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-bearclaw-inn-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only bearclaw_inn and input identity may change.
Final integration, acceptance and PR/review/main remain open.
