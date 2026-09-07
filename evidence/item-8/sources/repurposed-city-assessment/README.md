# Repurposed city assessment

Seven remaining requirements are integrated for two variants/87 pool-traced
templates in one family. Existing Overworld full-start geometry is accepted
under repurposed-final-geometry. No additional runtime or tool is needed.

## Content evidence

The pool trace resolves all components with no unresolved entities, generation
markers or ordinary/trial spawners. Overworld templates author villager baby,
nitwit and unemployed variants, plus armor stand, item/glow frames and minecart.
The latter are furnishings, not mobs. Nether templates author blazes and wither
skeletons. Exact template/entity mappings remain in the inventory; alternative
rooms are not necessarily all present in an assembled city.

Nether terminal edges also select mobs/wither_skeleton_with_bow. The packaged
placed/configured feature selects the WitherSkeletonWithBow implementation
captured in repurposed-feature-roles. Its place method creates a persistent
wither skeleton below the origin, equips an enchanted bow, sets equipment drop
chance and handedness, applies a randomized follow-range modifier and calls
addFreshEntityWithPassengers. This is an authored feature enemy, not a spawner.
The inventory identifies the source without measuring combat behavior, count,
loot yield or granting a guarantee from the feature return value.

Nether root spawn overrides separately select piece-bounded monsters:
wither_skeleton weight10,min2,max3 and blaze weight120,min1,max4. These are natural
spawn selection/group settings, not observed groups. Overworld overrides are
empty; natural biome spawning is separate from its authored villagers. The two
variants therefore have different intended hostility without a uniform tier or
safe-area claim.

Two literal loot tables exist: repurposed_structures:chests/cities/nether and
repurposed_structures:chests/cities/overworld. Their template associations remain
explicit. Selected processor lists are minecraft:empty, cities/nether_randomize
and cities/overworld_randomize. They apply material, crop, workstation and
support changes, with no append-loot or spawner processor. Template item frames
and equipped feature-mob items do not add container table sources. Detailed
rewards and availability are not assessed here.

## Placement and support limits

Overworld uses GenericJigsawStructure, WORLD_SURFACE_WG offset0,beard_thin and
cannot_spawn_in_liquid. Nether uses CityNetherStructure, start_height33 and
beard_thin. Both size5 roots list bridge_end,tower_top,fat_tower_top pools as
boundary exceptions; individual template dimensions cannot substitute for the
accepted assembled sample.

Existing CityNetherStructure.extraSpawningChecks first requires the base check.
For eight neighboring chunk-origin columns (the3x3 set excluding the center),
it examines Y from sea-level+20 up to, but excluding, min(maxTerrainLimit,
sea-level+45), rejecting any sampled nonair block. This is a limited column
clearance check, not whole-city clearance or open-sky exposure. The existing
repurposed-assembly identities bind this method.

Overworld red-glass pillars specify length15; orange-glass pillars omit length.
Both select cobblestone and delegate to overworld_randomize, which does not
turn the replacement material back into those triggers. Existing PillarProcessor
and noise/random replacement captures in repurposed-monument-processors preserve
the direct state writes, land/build limits and NBT behavior. Extensions are not
included in the saved-piece envelope. No occupied support height is inferred.
Tower/bridge architecture gives qualitative visible cues when exposed, while
terrain and vegetation may obscure lower rooms. No sightline is measured.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/repurposed-city-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only city and input identity may change. Source identities
are bound in the decision; the existing assembly/feature/processor READMEs give
reproducible extraction commands. Final Item8 acceptance and PR/review/main remain
open.
