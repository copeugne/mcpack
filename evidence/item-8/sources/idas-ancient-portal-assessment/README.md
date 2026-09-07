# IDAS ancient portal assessment

Seven remaining entries integrated for one family/two variants/four components.
Previously accepted sampled geometry in idas-existing-world-geometry is reused.
No new runtime capture or tooling is needed.

## mob_source

Four connected templates across two variants have no directly authored entities, unresolved entity compounds or generation markers. Overworld pieces select generic spawner randomization; Nether pieces retain raw spawner data under ticking-only processing. Natural silverfish/wraith overrides are separate. No missing graph components; source declarations do not establish live populations.

## loot_table_source

Both Overworld components reference defined idas:chests/ancient_portal/ancient_portal_overworld; both Nether components reference defined idas:chests/ancient_portal/ancient_portal_nether. Selected ticking/spawner processors append no container loot NBT. Trapped-chest source references do not establish successful trap behavior or reward quantities.

## generated_spawners

Each Overworld template contains one ordinary raw-wraith spawner and selects idas:generic_processor, whose idas:generic list declares zombie15,skeleton10,wraith5. Each Nether template contains three ordinary spawners with raw wraith/soul_vulture sources and selects only waterlogging_fix_processor, so those declarations are not randomized. AlexsMobs is absent; soul_vulture is not a verified viable spawn source. No trial spawners. Counts are authored blocks per component, not observed generated counts. Existing manager failure/fallback limits apply to the randomized path.

## authored_or_natural_enemies

Authored sources are ordinary spawners with variant-specific processing. Overworld natural piece overrides separately declare silverfish and wraith each weight3 group1..4; Nether declares wraith weight10 group1. Quark is present but AlexsMobs is absent in the frozen Mod List. Spawner source selection and natural weights do not establish realized encounters.

## intended_hostility

Loot-bearing monumental frame assemblies with ordinary spawners and natural monster overrides. Optional absent soul-vulture provider limits Nether source viability. No measured intensity, guaranteed trap operation or difficulty tier. Obsidian/crying-obsidian frame form does not prove an active or usable portal.

## visual_discoverability

Large portal-frame architecture provides an interior landmark when exposed; underground placement and Nether terrain can obscure it. No surface marker, visible entrance, measured sightline or tested portal navigation is established.

## underground_surface_classification

Overworld generic_structure root uses absoluteY-45, underground_structures, size2 and beard_box: underground intent without measured burial. Nether uses nether_structure, HIGHEST_LAND offset0, surface_structures, size2 and beard_box: Nether land-associated frame. Accepted Nether saved-piece sample does not bound every variant or measure occupied volume.

## Evidence

The two Overworld pool elements select idas:generic_processor. Its sole spawner
list declares zombie15,skeleton10,quark:wraith5 and its other processor ticks
dispensers. The two Nether elements instead select ticking-only
idas:waterlogging_fix_processor. Reuse the direct Integrated API spawner/manager
inspection in integrated-villages-provider and ticking inspection in
idas-desert-market-assessment. Those consumers distinguish input NBT from
processed sources and preserve failure/fallback branches.

Both graphs are complete with no missing components. Both literal loot-table
definitions exist in the packaged catalog. Raw entity and spawner attribution
remains explicit in inventory.json. Existing runtime Mod List evidence confirms
Quark present and AlexsMobs absent. Preserve raw optional sources rather than
inventing substitutes or declaring successful spawning. Prior template/pool
inspection establishes paired frame architecture, not tested portal operation.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-ancient-portal-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only ancient_portal and input identity may change.
Final integration, acceptance and PR/review/main remain open.
