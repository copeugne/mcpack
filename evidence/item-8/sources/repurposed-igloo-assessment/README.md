# Repurposed igloo assessment

Nine remaining entries are integrated for the four-variant family. No new capture
or measurement tool is needed. The dimension assessment was already integrated.

## Evidence and derivation

The four selected roots are igloo_grassy, igloo_mangrove, igloo_mushroom and
igloo_stone under data/repurposed_structures/worldgen/structure/. Their traced pools
resolve24 templates: top, top_trapdoor, ladder_short/medium/long and basement for
each variant, with no missing components. Roofed shelters and optional ladder/
basement assemblies remain components of one family.

The existing world-bounds catalog records a full igloo_stone start in mountainous
seed6671238423019257953, run-a/mountainous/chunks.jsonl line14209, chunk3,27.
Envelope[45,195,428,51,231,437] gives7x37x10 inclusive bounds. Run-b has the same
reported envelope. This supports an approximate assembled example, not all ladder
lengths/variants, typical size, occupied volume or exposed shelter height. Existing
world_observations retain the underlying records; the family now explicitly links
the run-a example.

Template content assigns villager and zombie_villager to grassy/stone basements,
frog and magma_cube to mangrove, cow/mooshroom and item_frame to mushroom. The
frame is not a mob. Each basement references the matching defined table
repurposed_structures:chests/igloos/{grassy,mangrove,mushroom,stone}. No template
spawner blocks, generation markers or unresolved entities occur in the trace.
Empty root spawn overrides leave ordinary biome spawning possible.

Four selected processor lists under worldgen/processor_list/igloos/ alter masonry
and material states. Grassy and stone include conditional infested-masonry rules
with probability0.06 per applicable rule. This is a potential triggered silverfish
source, not a guaranteed count. Grassy/mangrove additionally use the already
captured ForcePlaceMushroomBlocksProcessor, which handles mushroom block placement
and does not create an entity or loot source. Mushroom uses only material rules.
No selected processor introduces an ordinary/trial spawner or alternate loot table.

Direct inspection of mapped-server InfestedBlock.spawnAfterBreak shows the block
spawn gate: RULE_DOBLOCKDROPS and absence of an enchantment tagged
PREVENTS_INFESTED_SPAWNS. spawnInfestation creates a silverfish, checks creation
for null, positions it and requests insertion. This is a source mechanism, not an
observed population. Inspect with pinned Temurin javap -p -c against mapped server
SHA-256 26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71.
Class net/minecraft/world/level/block/InfestedBlock.class SHA-256:
e54092b7bea71d431cac53ed7717be601b3ae2f485e4fd7ac7474784ad1117a7.
No new inspection tool is required for this direct immutable-artifact derivation.

All roots use WORLD_SURFACE_WG offset0 and beard_thin. Mangrove permits liquids;
the other three prohibit liquid placement. Source intent is surface shelter plus
optional buried shaft/basement, not a uniform underground or surface-only family.
Hostility is variant-dependent; mushroom cattle do not establish a hostile dungeon,
while zombie villagers, magma cube and infested masonry carry conditional hazards.
Visibility is qualitative and terrain/vegetation-dependent, with no sightline claim.

The authoritative family binds packaged catalogs, runtime/world evidence and the
existing repurposed-assembly and repurposed-mansion-processors identity manifests.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/repurposed-igloo-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use an unused output path. Only this family and input identity change. Descriptive
claims rely on inspected artifacts; tests validate existing integration/evidence
boundaries rather than establish Item8 completion.
