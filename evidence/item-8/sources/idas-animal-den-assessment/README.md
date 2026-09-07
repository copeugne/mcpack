# IDAS animal den assessment

Nine remaining entries integrated for one family/three independent templates.
All have exact packaged size13,8,15 in x,y,z blocks. This nominal design envelope
satisfies approximate dimensions without a new runtime capture. Existing world
observations remain retained but are not promoted into a new measurement here.

## mob_source

Three independent templates author minecraft:wolf, minecraft:polar_bear and quark:foxhound in their corresponding forest, polar-bear and Nether variants. Quark glass frames in wolf/polar templates are non-mob entities. No unresolved template entities, markers or missing components. Quark is present in the frozen Mod List; references still do not prove realized population. The selected ticking processor does not substitute entities.

## loot_table_source

No template block entities or literal loot-table references in the three den templates. Selected waterlogging_fix_processor only schedules dispenser/dropper ticks and adds no loot NBT. This is source absence, not a claim that animal drops or ordinary mined materials have no value.

## generated_spawners

No ordinary or trial spawners or generation markers in any of the three templates. Selected ticking processor does not create spawner blocks. Authored animal entities are not spawner sources.

## authored_or_natural_enemies

Wolf, polar bear and foxhound are authored animal sources, while glass frames are non-mob entities. All three roots have empty spawn_overrides, with no family-specific natural enemy rule. Ambient spawning remains possible. Creature reference alone does not establish aggression at a particular visit or effective encounter population.

## intended_hostility

Animal-occupied mound/cavity design with no authored spawner or dedicated loot-table source. Treat the inhabitants as potential creature interactions rather than declaring a uniformly peaceful or uniformly hostile dungeon. No tested aggression, difficulty tier or measured combat intensity is inferred.

## visual_discoverability

Small mound and den cavity, with biome-related materials, provide terrain-like local cues. The8-block template height and surrounding vegetation or terrain can obscure the opening. No guaranteed visible entrance or measured discovery distance.

## underground_surface_classification

Forest and polar-bear roots project to WORLD_SURFACE_WG at offset0, size1, beard_thin and biome radius1: surface mound/cavity intent. Foxhound uses integrated_api:nether_structure, HIGHEST_LAND offset0 and beard_box: Nether land-associated den. None of these parameters measures actual burial or terrain relief.

## Evidence

The forest root selects wolf_den; polar_bear_den and foxhound_den select their
matching templates. Every graph has no missing or unresolved components. Each
pool is an independent single-template design, not a connected assembly.
All select idas:waterlogging_fix_processor, whose sole tick_blocks_processor
schedules dispensers/droppers and returns incoming block info. Reuse the direct
class identity and inspection in idas-desert-market-assessment.

The hash-bound template catalog and pool trace preserve entity IDs, empty block
entity contents and exact dimensions. Existing idas-variant-views comparisons
and family rationale establish common mound/cavity design, not merely matching
sizes. Captured dimension membership and original world bounds remain separate
from the nominal dimensions and qualitative descriptions integrated here.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-animal-den-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only animal_den and input identity may change.
No runtime, renderer or measurement system is added. Final Item8 integration,
acceptance and PR/review/main remain open.
