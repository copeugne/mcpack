# Repurposed mineshaft assessment

Seven remaining requirements are integrated for one family with 16 variants.
Existing catalogs, assembly/feature captures and direct processor inspection
suffice. No runtime capture or new tool is needed. Sizes were already accepted
in repurposed-mineshaft-pyramid-geometry; those saved-piece limits still apply,
including exclusion of unmeasured support extensions and occupied volume.

## Content sources

The pool trace reaches 226 templates with no missing components, authored
entities, unresolved entity sources or generation markers. Its ordinary spawner
NBT contains cave spiders. That initial data is not the effective attribution:
selected mineshafts/{variant}_spawner processor lists point to the matching
rs_spawners/mineshafts/{variant}.json. Each has one required entity at weight10.

- birch, dark_forest, desert, jungle, savanna, stone, swamp, taiga: cave_spider.
- icy: stray. Ocean: drowned. End: endermite.
- basalt, crimson, nether, soul, warped: blaze.

The captured SpawnerRandomizingProcessor and MobSpawnerManager in
repurposed-mansion-processors establish replacement SpawnData and a single
weight-one SpawnPotentials entry. Selection failures/fallbacks remain recorded
there. Valid packaged source selection does not prove live spawning, successful
placement of each block or an encounter population. No trial spawners occur in
the traced templates.

End separately specifies piece-bounded natural monster overrides: endermite
weight10, group2..5; enderman weight5, group1..3. Other roots have empty overrides.
These are natural spawn rules, not authored occupants or guaranteed groups.
Corridor spawners support intended hostile potential without a difficulty tier.

## Feature-selected loot

The ordinary pool trace has no literal loot references. Its terminal feature
edges select minecarts/{variant}_mineshaft_minecart. The corresponding configured
feature uses mineshaft_minecarts and minecart_nbt_file
repurposed_structures:mineshafts/{variant}/minecart. All16 selected templates
exist in templates-redacted.json.gz, each with one minecraft:chest_minecart entity
whose LootTable is repurposed_structures:chests/mineshafts/{variant}. All16 loot
definitions exist in packaged-json-redacted.json.gz. Exact variant associations
are now in the authoritative loot_table_source mapping. These feature templates
are components, not new families or hostile mobs.

The existing MinecartFeature capture in repurposed-feature-roles shows a required
occluding block below, then water-fluid eligibility for waterBased (ocean) or
empty fluid otherwise. A missing configured template warns and returns false.
Placement uses random rotation, permits entities and ignores structure-void
blocks. It calls placeInWorld, discards that boolean and returns true. Therefore
neither feature return success nor the source template establishes an observed
cart count or loot availability. Feature decorations/supports remain separate
from literal template content and from the accepted saved-piece geometry.

## Placement and visual interpretation

Generic Overworld roots use generic_mineshaft: starting heights35..130, icy35..150,
ocean5..30. MineshaftStructure.postLayoutAdjustments uses a terrain-derived target
minus15, constrained by its passed lower bound, and can shift all pieces downward
when the target is below the passed upper bound and highest piece. getTerrainHeight
samples OCEAN_FLOOR_WG at the center and four horizontal positions16 blocks away,
with its recorded subtraction order. Thus configured starting heights are not
final piece bounds or measured cover depths.

Five Nether roots use generic_jigsaw_structure starts6..13 and minimum-Y allowance2.
End uses MineshaftEndStructure island-aware placement with minimum thickness30;
its configured start_height0 must not be reported as the final Y. Existing
repurposed-assembly captures preserve those algorithms. All roots specify no
terrain adaptation. The supported/railed branching architecture provides local
cave or excavation cues; underground intent is not a guaranteed absence of
surface exposure, nor a measured sightline or water depth.

Direct inspection of pinned candidate
repurposed_structures-7.5.21+1.21.1-neoforge.jar member
com/telepathicgrunt/repurposedstructures/world/processors/MineshaftSkyViewProcessor.class
(SHA-256 c3ca66652bbbc976ad6035ad545e675d633276b24382ad93352027faa4387005)
shows a supported RAIL exception that copies waterlogging from the world fluid
and preserves NBT. Other incoming blocks at or above local OCEAN_FLOOR_WG are
suppressed; those below are returned unchanged. This qualifies discoverability,
not a proof that every assembled component is underground.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/repurposed-mineshaft-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c -classpath downloads/item3/candidates/repurposed_structures-7.5.21+1.21.1-neoforge.jar com.telepathicgrunt.repurposedstructures.world.processors.MineshaftSkyViewProcessor
```

Use a fresh inventory output path. Only mineshaft and input identity may change.
Catalog and captured-source identities are bound in the family decision. Existing
tracked extraction/assembly evidence remains authoritative; direct inspection
above needs no separate parser or validation framework. Item8 acceptance and
PR/review/main delivery remain open.
