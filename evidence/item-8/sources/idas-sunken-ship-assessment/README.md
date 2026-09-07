# IDAS sunken ship assessment

Nine entries integrated for one family/two roots/three independent hull templates.
All template sizes17 by28 by45 in x,y,z. These nominal dimensions need no new
runtime capture; independent alternatives are not combined into a larger ship.

## mob_source

Three independent hull alternatives. Coral declares an authored alexsmobs:frilled_shark, but alexsmobs is absent from the frozen Mod List; no successful shark creation is asserted. First ordinary and coral templates select drowned spawner randomization, while ordinary2 preserves raw spawner data. Natural wraith overrides are separate. No missing graph components, unresolved entity compounds or generation markers.

## loot_table_source

All three alternatives reference defined idas:chests/sunken_ship/sunken_ship_supply and idas:chests/sunken_ship/sunken_ship_treasure. Selected spawner processor does not append loot NBT; ordinary2 uses empty processors. Literal references establish source identity, not realized rewards or container availability.

## generated_spawners

Ordinary1 and ordinary2 each contain two ordinary spawner blocks with raw frilled_shark and drowned SpawnData, empty SpawnPotentials. Coral has one raw frilled_shark spawner. Ordinary1 and coral select idas:sunken_ship_processor and integrated_structure_spawners/sunken_ship, sole drowned weight15; ordinary2 uses minecraft:empty and retains both raw declarations. AlexsMobs is absent, so its unrandomized shark entry is not a verified viable enemy source. No trial spawners. Existing manager failure/fallback branches and unmeasured spawn success remain explicit.

## authored_or_natural_enemies

Authored sources distinguish randomized drowned spawners from ordinary2 raw drowned/shark data and coral direct shark entity. The shark provider is absent. Both roots separately declare piece-bound natural quark:wraith weight5 group1..2; Quark is present. Weights and group settings are source parameters, not observed populations.

## intended_hostility

Loot-bearing submerged ship hulls with ordinary spawners and natural wraith overrides. Variant processor differences and absent optional shark provider prevent a uniform enemy claim. Underwater access adds environmental pressure; no measured intensity or difficulty tier is assigned.

## visual_discoverability

Long hull, mast/deck and furnishings provide ship-shaped cues, with coral decoration in its variant. Water and seabed terrain may obscure the wreck. This differs from detached debris but does not establish visible masts above water, a surface marker or measured sightline.

## underground_surface_classification

Both generic_structure roots use OCEAN_FLOOR_WG, LOWEST_CORNER, start offset-1, apply_waterlogging, size1, beard_box and biome radius1. Seabed/submerged intent, with variant biome constraints preserved. No measured burial fraction, water depth or final occupied terrain extent.

## Evidence and variant differences

The ordinary pool weights first ship2 and second ship1. First selects
idas:sunken_ship_processor; second selects minecraft:empty. Coral selects the
same spawner processor at weight1 in its separate pool. Both graphs are complete.
The selected spawner list contains only minecraft:drowned weight15. Raw spawner
counts are per authored template, not observations of final generated worlds.
Reuse integrated-villages-provider's SpawnerRandomizingProcessor and manager
inspection: matching blocks receive new NBT; missing lists, unresolved entries,
zero totals and exceptions retain documented fallback/failure handling. This
source analysis does not prove successful reload, placement or live spawning.

Existing runtime_mod_ids parser confirms alexsmobs absent and quark present in
the hash-bound registry-r1 Mod List. Coral's authored shark and ordinary2's raw
shark spawner are preserved without inventing a replacement mob. Other ordinary
raw drowned data and the two randomized paths remain distinct viable declarations.
Both literal loot tables were verified in the preceding ship-ruins assessment;
exact references and template mappings remain in inventory.json.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-sunken-ship-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only sunken_ship and input identity may change.
No new runtime, renderer or measurement system. Final integration, acceptance
and PR/review/main remain open.
