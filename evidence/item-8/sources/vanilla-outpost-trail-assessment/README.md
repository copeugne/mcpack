# Outpost and trail-ruin content assessment

This increment resolves six descriptive attributes for each family. Assembled
footprint and vertical size remain open: the retained world-bounds catalog has
no full-start observation for either root. It does not introduce a capture or tool.

## Inspection references and derivation

Use `pool-traces-content.json.gz` structures `minecraft:pillager_outpost` and
`minecraft:trail_ruins`, and their referenced `template_contents` entries. The
trace identities are pinned in each family decision. Eleven outpost templates
and 84 trail-ruin templates are reachable, with no missing templates or unresolved
entities. Neither set contains generation markers or spawner blocks. The outpost
cage templates author an iron golem and allays; trail ruins author no entities.
These are template possibilities, not observed generated populations.

In `packaged-json-redacted.json.gz`, inspect these resource paths:

- `data/minecraft/worldgen/structure/pillager_outpost.json`
- `data/minecraft/worldgen/structure/trail_ruins.json`
- `data/minecraft/worldgen/processor_list/outpost_rot.json`
- `data/minecraft/worldgen/processor_list/trail_ruins_houses_archaeology.json`
- `data/minecraft/worldgen/processor_list/trail_ruins_roads_archaeology.json`
- `data/minecraft/worldgen/processor_list/trail_ruins_tower_top_archaeology.json`

The outpost monster override applies to full structure bounds and selects pillager
with weight 1 and group bounds 1 to 1. It is a spawn rule, not a spawner block or
population guarantee. `outpost_rot` is block rot with integrity 0.05. Watchtower
and overgrown-watchtower NBT reference `minecraft:chests/pillager_outpost`.

Trail-ruin processors append loot to suspicious gravel. Houses select common and
rare archaeology tables with caps 6 and 3; roads and tower tops select common with
cap 2. These are processor caps, not family-wide counts. The empty literal template
loot list therefore does not establish absence of loot. Root spawn overrides are
empty and processors do not introduce enemies; ordinary biome spawning is possible.

All three loot definitions exist under `data/minecraft/loot_table/`:

- `chests/pillager_outpost.json`: SHA-256 `992d9ec7da80b93732342a0992378f11afa9984ab1fa9fa00dd83357116796b0`
- `archaeology/trail_ruins_common.json`: SHA-256 `c0d45237b48f09e230244e419380d2e63225618de329437c502e0f14a9a8c6a9`
- `archaeology/trail_ruins_rare.json`: SHA-256 `72d0b3e21d2bea992468385ad05fea82973d3557605b7a2d9050acd7459e086f`

Visual descriptions derive from root projection and template roles: surface
watchtower and optional camp features for outposts; buried rooms, roads and tower
for trail ruins. The latter uses WORLD_SURFACE_WG offset -15 and bury adaptation.
No sightline, exposure guarantee, occupied volume or typical size is asserted.

## Reproduction and validation

The authoritative assessments are the two groups' attributes in
`evidence/item-8/family-decisions.json`. Rebuild with an unused output path:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/outpost-trail-content-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Direct source inspection supports the descriptions. Existing tests validate the
inventory integration and source identities; they do not certify prose or prove
Item 8 completion. No executable behavior changed beyond the decisions hash pin.

## Remaining vanilla geometry capture declaration

After ea6bf76a, inspect additional retained Item 8 captures before new generation.
The CTOV outpost capture has a vanilla outpost at chunks.jsonl line 1803, but its
status is minecraft:structure_starts and full is false. It does not satisfy the
existing full-start-chunk geometry standard. No mansion or trail-ruin records were
found in those additional original chunks.jsonl captures. The main world-bounds
catalog also has no full-start observations for these three roots.

Predeclare one fresh ordinary seed 42 Overworld run with targets, in order:
minecraft:pillager_outpost, minecraft:trail_ruins, minecraft:mansion. Request 81
chunks around each located target using the existing gap runner. Preserve readiness,
matching completion, save-all flush confirmation, clean stop and frozen configuration
validation. Accept saved assembled envelopes only after raw archive and verified
local and downloaded restores. This is six required size entries, not a population,
all-layout or pacing experiment. No new tool or baseline change is required.

```sh
uv run -m tools.run_item7_gap_targets \
  --pristine instances/pristine-baseline-v0 \
  --artifact-manifest evidence/item-3/artifact-acquisition-manifest.json \
  --retained-manifest evidence/item-3/runtime/retained-server-candidates.txt \
  --seed-suite test-environment/seed-suite.json \
  --frozen-config evidence/item-6/frozen \
  --frozen-manifest evidence/item-6/generated-config-manifest.json \
  --config-audit evidence/item-6/config-audit.json \
  --java-home downloads/item2/temurin/extracted/jdk-21.0.12.1+1 \
  --target instances/item8/vanilla-final-geometry-r1 \
  --log-path evidence/raw/item8/vanilla-final-geometry-r1/console.log \
  --captured-config evidence/raw/item8/vanilla-final-geometry-r1/configuration \
  --receipt evidence/raw/item8/vanilla-final-geometry-r1/run.json \
  --timeout-seconds 900 \
  --structure minecraft:pillager_outpost --structure minecraft:trail_ruins \
  --structure minecraft:mansion
```
