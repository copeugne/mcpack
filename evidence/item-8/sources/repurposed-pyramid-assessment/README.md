# Repurposed pyramid assessment

Seven remaining requirements are integrated for one family, 11 variants and22
pool-traced templates. Existing size evidence remains in the mineshaft/pyramid
geometry assessment. No new runtime or tool is needed.

## Content and source distinctions

Template content authors creeper in flower_forest_pit, drowned in ocean_body,
endermite in end_body, mooshroom in mushroom_body and tropical fish in mushroom_pit.
Mooshroom/fish are non-hostile. The pool trace has no missing components,
unresolved entity sources or generation markers.

Badlands, End and Nether processors select rs_spawners/pyramids/{variant}:
husk, endermite and zombified_piglin respectively, each a sole required entity
with weight10. Badlands additionally sets block-light0..7. The snowy body stray
spawner has no replacement processor. These are ordinary spawners, not trial
spawners. Captured SpawnerRandomizingProcessor/MobSpawnerManager behavior in
repurposed-mansion-processors distinguishes the selected sources from original
NBT and preserves failure paths. Other variants have no ordinary spawner in the
trace. All root spawn overrides are empty, leaving natural biome mobs separate.

Jungle body and pit palettes contain infested blocks. jungle and jungle_hidden_room
rules can change infested stone bricks to infested mossy/cracked forms; hidden-room
rules also remove infestation on matching blocks with probability0.65. These are
conditional silverfish sources, not guaranteed occupants. The pinned vanilla
InfestedBlock inspection and break guards are already recorded in
repurposed-igloo-assessment: drops rule and prevention enchantment checks apply.
No new class capture is needed for that shared behavior.

Thirteen literal loot references comprise eight chest tables, one dark-forest
dispenser table and four trapped-chest tables (badlands,end,nether,ocean).
The authoritative mapping retains their exact template associations.
jungle_hidden_room adds repurposed_structures:archaeology/pyramid_jungle through
a gravel random-match0.1 append_loot rule producing suspicious gravel. All14
corresponding definitions exist under data/repurposed_structures/loot_table/ in
the packaged catalog. Rule eligibility does not establish archaeology counts.
TNT in several pits and dark-forest body, plus magma blocks in icy/ocean templates,
support physical hazard potential without asserting working traps or rewards.

The selected trace references15 processor lists including minecraft:empty.
Pillar delegates also reach icy_pillar, which only randomizes packed ice into
blue ice/ice. Badlands and jungle self-list delegates replace red stained glass
with nontrigger materials; Nether self-list delegates similarly replace colored
glass with blackstone. Existing PillarProcessor inspection in
repurposed-monument-processors explains sequential block processing and limits.
Support extensions are excluded from saved-piece geometry. Material replacement,
ForcePlaceMushroomBlocksProcessor and StructureVoidProcessor retain their existing
source interpretations. Decoration features select flowers, grass, vines and
ocean plants; they are not new families or enemy sources.

## Placement and limited visual assessment

Most Overworld roots select WORLD_SURFACE_WG, LOWEST_CORNER, offset-3, size3 and
no terrain adaptation. This supports a terrain-rooted pyramid body with buried
pit intent. Ocean substitutes OCEAN_FLOOR_WG and permits liquids. End selects
WORLD_SURFACE_WG, AVERAGE_LAND, offset-2, radius1 and minimum-Y50. Nether selects
GenericNetherJigsawStructure LOWEST_LAND, offset-2, size1 and beard_thin.
The pinned GenericNetherJigsawStructure codec reads land_search_direction;
it does not use the additional packaged search_for_highest_land key as its
selector. The existing repurposed-assembly capture preserves that distinction.
Exposed pyramid bodies provide qualitative architectural cues; buried rooms,
vegetation and ocean placement can obscure access. No visibility range, guaranteed
entrance exposure or measured water depth is claimed.

## Direct processor inspection

Pinned repurposed_structures-7.5.21+1.21.1-neoforge.jar members under
com/telepathicgrunt/repurposedstructures/world/processors/:

- AirProcessor.class SHA-256 c2412eb1be5afe7ac7c659f4f4d34a26a7c1f415ba90f2032ca549cb74b94392.
  For incoming air, eligible center-chunk/world-generation positions within build
  bounds are directly written unless the existing block is in its ignore set.
  The method returns incoming block info; it does not spawn mobs or assign loot.
  The flower-forest pit list supplies the plant ignore set. The direct-write guard
  does not establish that subsequent ordinary placement preserves every plant.
- TickBlocksProcessor.class SHA-256 6117f24265b3de8bb77bf5e9136d9c75e75a77784c93a09a72a95bc1cab67410.
  Matching configured blocks schedule a zero-delay block tick, subject to its
  center-chunk and Y checks, and return incoming info. Selected lists target
  daylight_detector in dark forest and bubble_column in ocean. Scheduling does
  not prove trap operation or a resulting world state.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/repurposed-pyramid-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c -classpath downloads/item3/candidates/repurposed_structures-7.5.21+1.21.1-neoforge.jar com.telepathicgrunt.repurposedstructures.world.processors.AirProcessor com.telepathicgrunt.repurposedstructures.world.processors.TickBlocksProcessor
```

Use a fresh inventory output path. Only pyramid and input identity may change.
Catalog and captured-source identities are bound in the decision. Direct immutable
artifact inspection supplies descriptive derivations without another tool/schema.
Item8 final acceptance and PR/review/main delivery remain open.
