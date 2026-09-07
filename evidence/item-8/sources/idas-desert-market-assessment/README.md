# IDAS desert market assessment

Seven remaining attributes integrated for one family/three alternatives. Existing
17 by16 by17 template dimensions are reused. No new runtime or tool is needed.

## mob_source

Each of three independent templates declares guardvillagers:guard. The frozen runtime Mod List lacks guardvillagers; preserve the authored reference without asserting successful guard creation. No unresolved entity compounds, generation markers or missing graph components. The selected processor schedules dispenser/dropper ticks and returns the incoming block info, not an entity substitution.

## loot_table_source

All three alternatives reference defined idas:chests/bazaar/bazaar and idas:chests/bazaar/bazaar_food. The selected waterlogging_fix_processor contains only tick_blocks_processor for dispensers/droppers, with no appended loot-table NBT. Shared bazaar loot does not merge this single-template market family with the separate assembled bazaar. Container references do not establish reward quantities or working waystone interactions.

## generated_spawners

No ordinary or trial spawner blocks and no generation markers in the three templates. The selected ticking processor does not add spawner blocks or mutate incoming NBT. No successful guard population or exclusion of natural spawning is inferred.

## authored_or_natural_enemies

Only authored entity identifier is guardvillagers:guard, whose mod is absent from the frozen runtime list. No authored hostile entity or physical spawner is identified. All three roots have empty spawn_overrides, so they declare no family-specific natural spawn rule; ordinary environmental spawning remains possible.

## intended_hostility

Market/stall design with food and supply loot and an authored guard reference, but no demonstrated guard creation in the retained stack. No identified authored hostile encounter source or spawner. Do not describe the site as reliably guarded, uniformly safe or a measured combat encounter.

## visual_discoverability

Multi-level framed stalls, shaded planted upper details and17-by17 template footprint with16-block height provide architectural cues. Desert material and ladder differences remain variants. Terrain can obscure the structure; no measured discovery distance, visible-entrance guarantee or tested navigation claim.

## underground_surface_classification

Surface-associated market variants use integrated_api:generic_structure, WORLD_SURFACE_WG projection, start offset0, size1, beard_thin adaptation and biome radius1. Red additionally declares terrain-height range10 and radius1. Nominal single-template dimensions do not establish final terrain relief or foundation burial.

## Source inspection

The existing runtime_mod_ids reader applied to the hash-bound registry-r1
Mod List confirms guardvillagers is absent. This supports the absent-provider
limitation, not an assertion about a measured entity population. No substitute
entity is invented. All three traces have no missing or unresolved components.

Selected idas:waterlogging_fix_processor contains only
integrated_api:tick_blocks_processor with blocks_to_tick dispenser and dropper.
Direct immutable class inspection in the pinned Integrated API candidate:
com/craisinlord/integrated_api/world/processors/TickBlocksProcessor.class,
SHA-256 1b9eb557b99da6f121c5c245893b3e8c34df250c352be5c2deceb5cc183b78ab.
processBlock checks selected block membership, WorldGenRegion center chunk and
build-height bounds, schedules a block tick with delay0, then returns the input
StructureBlockInfo. It does not replace entity sources, spawners or loot NBT.
Scheduled ticks are not a claim of working container interactions.

Both bazaar and bazaar_food table definitions exist in the preserved JSON
catalog; exact references and templates remain in inventory.json. Prior complete
variant views and decisions retain stall geometry, containers and furnishings.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-desert-market-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c -classpath downloads/item3/candidates/integrated_api-1.7.3+1.21.1-neoforge.jar com.craisinlord.integrated_api.world.processors.TickBlocksProcessor
```

Use a fresh output path. Only desert_market and input identity may change.
Final Item8 integration, acceptance and PR/review/main remain open.
