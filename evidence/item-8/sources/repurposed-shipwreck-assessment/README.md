# Repurposed shipwreck assessment

Nine remaining attributes are integrated using existing source and world evidence.
No new capture or tool is needed. The family retains four variants, not21 families.

## Evidence and derivation

Selected roots shipwreck_crimson, shipwreck_warped and shipwreck_nether_bricks each
reach one corresponding Nether template. shipwreck_end reaches18 fragment/position
alternatives. The pool trace reports no missing components; all selected processor
lists are minecraft:empty. Three Nether templates author wither skeletons, and
nether_bricks also authors an item frame, which is not a mob. End template entity
lists are empty. No template spawners, generation markers or unresolved entities
are present.

Nether roots separately override monster spawning with piece bounds, wither_skeleton
weight10 and min/max1. This is a natural-spawn rule separate from template occupants,
not an ordinary spawner or population guarantee. End spawn overrides are empty;
ordinary biome spawning remains possible. This supports different hostility
assessments for Nether and End without asserting a safe area or encounter intensity.

Ten literal loot tables exist under data/repurposed_structures/loot_table/chests/
shipwrecks/: map/supply/treasure for crimson,warped,end and nether_bricks/treasure.
Exact template associations remain in the authoritative loot_table_source mapping.
Not every fragment necessarily contains every table and empty processors add no
alternate table source.

Existing full-start world evidence at run-a/ocean-heavy/chunks.jsonl line7794,
seed95920844204830198, End chunk110,3 records shipwreck_end envelope
[1748,56,44,1771,64,52],size24x9x9. Run-b reports the same envelope. It supports one
saved assembled example, not every fragment/orientation, Nether variant, occupied
volume or exposed height. The world-bounds artifact and linked observations retain
the raw provenance; the family now explicitly references this example.

The End root uses WORLD_SURFACE_WG, LOWEST_SIDE adjustment, offset-3, minimum-Y
allowance35 and no terrain adaptation. This is terrain-associated partly buried
intent. Nether crimson/warped roots use anchor28, nether_bricks29, with no terrain
adaptation. The existing repurposed-assembly capture of ShipwreckNetherStructure
shows inheritance from GenericJigsawStructure. Its extraSpawningChecks first
requires the base check, then samples base-column positions and rejects a sampled
state that is neither air nor fluid-bearing. This is a limited air/fluid check,
not proof of whole-template clearance or open-sky exposure.

Ship hull/fragment architecture supplies a qualitative visual cue. Terrain, partial
burial and Nether liquids can obscure it; no sightline or guaranteed visible form
is measured. Raw source identities, template catalogs and world evidence are bound
in the family decision. These attributes do not establish Item8 delivery.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/repurposed-shipwreck-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only this family and input identity may change. Source
inspection supports descriptions; tests validate existing evidence/integration paths.
