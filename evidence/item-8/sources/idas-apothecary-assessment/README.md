# IDAS apothecary abode assessment

Seven remaining entries integrated for one family/two connected templates.
Accepted sampled geometry in idas-existing-world-geometry is reused; no new
runtime capture, renderer or measurement system is needed.

## mob_source

Both connected templates author minecraft:illusioner and minecraft:pillager. Main component additionally has item and experience-orb entities, which are not enemies. No unresolved entity compounds, missing components or generation markers. Selected processor randomizes ordinary spawners using the pillager list; direct illagers and spawner sources remain separate. No realized population is measured.

## loot_table_source

Both components reference defined idas:chests/apothecary_abode/apothecary_abode; main additionally references defined idas:chests/apothecary_abode/apothecary_abode_books. Selected spawner processor appends no container loot NBT. Literal sources are not measured reward quantities or proof of working brewing/storage interactions.

## generated_spawners

Ordinary pillager spawner blocks occur in both templates; no trial spawners or generation markers. All select apothecary_abode_processor, referencing integrated_structure_spawners/pillager with sole minecraft:pillager weight15. Settings delay20,min200,max800,count4,nearby6,player range16,spawn range4,block-light0..7. Existing manager failure/fallback behavior remains applicable; configuration is not observed spawning success.

## authored_or_natural_enemies

Illusioners and pillagers are directly authored hostile sources; processor-selected pillager spawners are a separate authored source. Item and experience-orb entities are not additional enemies. Root spawn_overrides is empty, so no family-specific natural override is declared. Ordinary environmental spawning remains possible.

## intended_hostility

Furnished brewing/storage abode with authored illagers and ordinary pillager spawners. Its domestic name does not establish a peaceful building. Hostile potential is supported without assigning a tier, measured intensity, successful encounter population or spell-progression system.

## visual_discoverability

Connected furnished buildings with brewing, beds, crops and storage provide architectural cues. Terrain and vegetation may conceal parts of the compound; domestic appearance does not reveal every hostile source. No measured sightline or visible-entry guarantee.

## underground_surface_classification

Surface-associated generic_structure assembly: WORLD_SURFACE_WG offset0,size3,terrain range10/radius1,biome radius1. Enhanced custom terrain adaptation declares beards/carves and kernel size/distance20. These settings are not measured terrain alteration or burial. Accepted saved-piece geometry remains a sample excluding occupied-volume and all-component-population claims.

## Evidence

The complete pool trace has no missing or unresolved components. Selected
apothecary_abode_processor consists only of Integrated API's ordinary spawner
randomizer using idas:pillager. The packaged list contains pillager weight15.
Reuse integrated-villages-provider's exact SpawnerRandomizingProcessor and
MobSpawnerManager inspection, including failure/fallback limits and NBT replacement.
Both literal loot definitions exist in the preserved packaged JSON catalog.

Template mappings preserve the two authored illager types and non-mob entities.
Prior connected-component and full-template inspection supplies architectural
and furnishing context. Source declarations do not prove operating equipment,
complete placement, encounter intensity or effective reward yield.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-apothecary-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only apothecary_abode and input identity may change.
Final integration, acceptance and PR/review/main remain open.
