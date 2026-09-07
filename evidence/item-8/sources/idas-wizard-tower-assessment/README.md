# IDAS wizard tower assessment

Nine remaining entries for three paired variants/six templates. Existing catalogs
and processor inspection suffice; no new runtime or measurement system.

## mob_source

Each of the three matching lower templates authors minecraft:zoglin. Main templates contain no authored entities; purple and yellow separately contain ordinary spawners. No unresolved entity compounds or generation markers. All six components select wizard_tower_processor, which randomizes existing ordinary spawners using sole quark:wraith weight5. Direct zoglins and spawner sources remain separate; realized inhabitants are unmeasured.

## loot_table_source

Four defined literal sources. All main variants reference idas:chests/wizardtower/wizardtower_basic. Purple/yellow additionally reference wizardtower_library and wizardtower_top in that directory; red instead adds minecraft:chests/village/village_cartographer. Bottom components have no literal loot references. Selected spawner-only processor assigns no container loot NBT. Source differences are preserved without measured reward yields.

## generated_spawners

Purple and yellow main templates each contain two ordinary spawners with raw quark:wraith data; red and all bottoms have none. Selected wizard_tower_processor uses idas:wizard_tower with sole quark:wraith weight5. Delay20,min200,max800,count4,nearby6,player range16,spawn range4,block-light0..7. Existing Integrated API processor/manager semantics and fallback limitations apply. No trial spawners or generation markers. Four source blocks across alternatives are not four spawners per generated tower.

## authored_or_natural_enemies

All three lower variants directly author zoglins. Purple/yellow add processor-selected wraith spawners; red does not. Empty root spawn_overrides declares no family-specific natural override; environmental spawning remains separate. Variant source differences do not establish measured encounter intensity or realized population.

## intended_hostility

Tall tower assembly with hostile lower-component zoglin sources and additional wraith spawners in purple/yellow variants. Red retains a distinct encounter and loot composition. This inventories existing content without introducing player spell progression, an Item9 tier or a claim of measured combat difficulty.

## visual_discoverability

Narrow tower shaft with enlarged capped upper room supplies a tall architectural cue. The24 by25 footprint and48 height are nominal complete assembly dimensions including lower component and padding, not measured sightlines or exposed silhouette. Terrain and vegetation may conceal lower access.

## underground_surface_classification

Surface-associated tower with matching lower section. Root generic_structure projects WORLD_SURFACE_WG offset0,size2,beard_thin adaptation,terrain range10/radius1,biome radius1,ignore_waterlogging. All pools rigid; nominal bottom origin is six blocks below main. Actual burial and successful complete placement are not measured.

## Geometry and evidence

Family evidence binds templates-redacted, pool-traces-content and packaged JSON.
Under data/idas/structure/wizard_tower/, purple/red/yellowwizardtower1.nbt each
have size24,42,25 and down_west aligned connector at0,0,24. Matching color2.nbt
has size24,6,25 and up_west aligned connector at0,5,24. Color-specific name/target
pairs join adjacent blocks, giving bottom origin0,-6,0 relative to main0,0,0.
Inclusive union x0..23,z0..24,y-6..41 gives24 by25 horizontal and48 vertical for
each alternative. This is nominal complete reference geometry, not observed
burial or guaranteed bottom placement. worldgen/template_pool/wizard_tower/
wizardtower.json selects three main alternatives weight1 each; each bottom pool
has one rigid element. All have empty fallback, no missing components or
unresolved pool elements. Alternatives are not additional families or summed sizes.

worldgen/processor_list/wizard_tower_processor.json contains only ordinary
spawner randomization using integrated_structure_spawners/wizard_tower.json,
which declares sole quark:wraith weight5. Reuse integrated-villages-provider's
pinned SpawnerRandomizingProcessor and MobSpawnerManager inspection. Processor
presence in red/bottom elements adds no spawner without an existing input block.
Quark is present in the frozen runtime, as documented by the captured Mod List.

The three IDAS wizardtower loot definitions and vanilla village_cartographer
exist in the preserved packaged catalog. Full-template views and retained source
rationale supply tower-form context without inferring measured sightlines,
reward yields or a player spell-progression system.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-wizard-tower-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only wizard_tower and input identity may change.
Final integration, acceptance and PR/review/main remain open.
