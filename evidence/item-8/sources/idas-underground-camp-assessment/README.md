# IDAS underground camp assessment

Nine entries integrated for one family/two roots/four template alternatives.
Ordinary1/deep1 templates are6 by3 by6; ordinary2/deep2 are6 by3 by5 in x,y,z.
These independent alternatives supply nominal dimensions without another capture.

## mob_source

Four independent template alternatives contain no authored entities, unresolved entity compounds or generation markers. Selected waterlogging_fix_processor only schedules dispenser/dropper ticks and does not introduce entity sources. Workstation blocks and machinery parts are not proof of operators or functioning contraptions.

## loot_table_source

All four alternatives reference defined idas:archeology/suspicious_gravel_mining. underground_camp_deep2 additionally references defined idas:archeology/suspicious_gravel_surface. These are literal template archaeology sources, not inferred from the mining theme. Selected ticking processor adds no loot NBT. Fixed toolbox/sack contents and raw-material blocks are distinct from loot-table yield.

## generated_spawners

No ordinary or trial spawner blocks and no generation markers in any of the four templates. The selected ticking processor introduces no spawner. Natural spawning is not excluded.

## authored_or_natural_enemies

No authored entities or physical spawners, and both roots have empty spawn_overrides. Thus no family-specific authored enemy or natural override is identified, while ordinary underground environmental spawning remains possible.

## intended_hostility

Small underground workstation and archaeology cache design with no identified authored hostile encounter source. Saw/hand-crank or drill arrangements do not prove operation, and lack of spawners does not establish a safe cave environment.

## visual_discoverability

Small workstation, toolbox, crafting/sack and suspicious-gravel cues distinguish the camp from nearby rock once exposed. Deep alternatives use deepslate and raw-metal blocks. No surface marker, visible cave route or discovery distance is established.

## underground_surface_classification

Both generic_structure roots use underground_structures, size1, beard_box and no heightmap projection. Ordinary starts at absoluteY20; deep starts at absoluteY-10. These are underground placement inputs, not measured depth below the local surface. Nominal template height excludes terrain adaptation and site relief.

## Evidence

Both pool graphs have no missing or unresolved components. All alternatives
select idas:waterlogging_fix_processor. Reuse its Integrated API ticking class
identity and processBlock inspection from idas-desert-market-assessment: it
schedules dispenser/dropper ticks and returns input block info without injecting
loot NBT, entities or spawners.

Both archaeology table definitions exist in the preserved packaged catalog.
Exact literal references and template mappings remain in the authoritative
inventory. Prior worksite and family comparisons retain the saw/drill, sack,
toolbox and suspicious-gravel arrangements. Apparent equipment does not prove
working machinery. Existing world observations remain preserved, distinct from
the nominal template dimensions used here.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-underground-camp-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only underground_camp and input identity may change.
No new runtime, renderer or measurement system. Final integration, acceptance
and PR/review/main remain open.
