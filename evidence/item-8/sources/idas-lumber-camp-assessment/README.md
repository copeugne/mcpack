# IDAS lumber camp assessment

Eight remaining entries integrated for one family/ten variants. Prior nominal
geometry remains valid independently of variant biome eligibility. No new runtime
or tool is needed.

## mob_source

Ten independent worksite templates contain no authored entities, unresolved entity compounds or generation markers. Selected waterlogging_fix_processor only schedules dispenser/dropper ticks; it does not assign entities. Machinery and seats in block contents are not proof of operating contraptions or a population.

## loot_table_source

No literal loot-table references in the ten templates. Selected ticking processor adds no loot-table NBT. Fixed toolbox or sack contents are not thereby declared empty; source absence is not an absence of all obtainable material.

## generated_spawners

No ordinary or trial spawner blocks or generation markers across ten templates. Selected dispenser/dropper ticking processor does not introduce spawners. Natural spawning is separate.

## authored_or_natural_enemies

No authored entity or spawner source in the templates; all ten roots have empty spawn_overrides. Ordinary environmental spawning remains possible wherever eligible variants generate. Missing biome tags do not create an alternative authored enemy source.

## intended_hostility

Small logging worksites with no identified authored hostile encounter source. Logs, campfire, toolbox and saw/hand-crank arrangement establish worksite intent, not tested machinery operation or guaranteed safety from natural enemies.

## visual_discoverability

Low open campfire, log piles and worksite equipment provide local cues. Four-block template height and wooded surroundings can make sites easy to overlook. No measured visibility range or reliable discovery marker is established.

## underground_surface_classification

Surface-associated worksite intent: generic_structure roots project to WORLD_SURFACE_WG with offset0, size1, beard_thin and empty natural overrides. Packaged geometry is known for all variants; three missing biome-tag variants lack eligible biome membership in the fresh baseline. Nominal template height is not foundation burial or terrain relief.

## Missing biome tags: resolved eligibility derivation

Seven variants have recorded Overworld biome overlap. The following three
required tag definitions are absent from packaged sources and explicitly named
in registry-r1/debug.log line19005's MappedRegistry warning:

- idas:has_structure/bopmahogany_biomes
- idas:has_structure/bygmahogany_biomes
- idas:has_structure/bygredwood_biomes

Their structure roots remain registered at dump lines359,361,362. Do not confuse
registration with generation eligibility or delete these variants from inventory.
The frozen fresh runtime initializes HolderSet.Named.contents to List.of().
MappedRegistry.bindTags warns about defined-but-missing tags, binds only supplied
tag lists and rebuilds holder memberships from supplied tags. Thus these missing
fresh named sets retain empty contents and confer no biome membership. Named
contains delegates to Holder.is(tag). No matching biome in a dimension can satisfy
the absent tag. This resolves eligible dimension sets to empty for these three
variants, without pretending the packaged definitions exist or claiming a failed
world-generation trial. The original missing_required evidence remains unchanged.
This derivation concerns fresh baseline loading, not stale tags after hot reload.

Direct identities in the pinned mapped Minecraft server JAR:

- net/minecraft/core/MappedRegistry.class:
  de66fcdbe6ac3d42a256ed032992af0b845e28e801a93eca9e76fb1620e4ff5a.
- net/minecraft/core/HolderSet$Named.class:
  292ecf890ee3082082e0dca0ffa7dc1ddba3d861234a2d93b371b86ebb5c1e66.

The raw catalog resolver retains its unresolved-source result; the assessed
dimension attribute supplies this explicit runtime-semantics disposition.
No tags, configuration, candidate set or frozen defaults are modified.

## Content and processor evidence

All ten pool graphs select idas:waterlogging_fix_processor. Its sole processor
is Integrated API tick_blocks_processor for dispensers/droppers; reuse the
exact class identity and processBlock inspection in idas-desert-market-assessment.
It returns incoming block info and does not inject entities or loot NBT.
Prior variant views and exact template contents retain log/campfire/toolbox and
saw arrangements. Optional material declarations do not prove working machinery.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-lumber-camp-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c -classpath instances/pristine-baseline-v0/libraries/net/minecraft/server/1.21.1-20240808.144430/server-1.21.1-20240808.144430-srg.jar net.minecraft.core.MappedRegistry 'net.minecraft.core.HolderSet$Named'
```

Use a fresh output path. Only lumber_camp and input identity may change.
Final Item8 integration, acceptance and PR/review/main remain open.
