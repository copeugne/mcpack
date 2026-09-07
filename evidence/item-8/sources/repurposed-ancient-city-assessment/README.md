# Repurposed ancient city assessment

Seven required entries integrated for one family, three variants and173 templates.
The existing ocean saved geometry in repurposed-final-geometry remains the family
example. No new runtime capture, measurement system or executable logic is added.

## Sources and assessment

### mob_source

173 pool-traced templates across End57, Nether57 and ocean59. Ocean authors drowned and guardian; Nether authors ghast; End authors end_crystal, an entity rather than a mob. No missing graph components, unresolved entities or generation markers. Selected features are vanilla chorus plants, structure fire and structure seagrass. Ordinary spawners and natural overrides are separate sources; population is not measured.

### loot_table_source

Six defined literal chest tables: ancient_cities/end, end_spawner_box, nether, nether_magma_box, ocean and ocean_ice_box. Ocean capped rule delegates additionally append archaeology/ancient_city_ocean to suspicious sand or gravel. Seven definitions verified. Configured caps are per processor application, not family-wide loot counts or guaranteed availability.

### generated_spawners

End spawner_box_1 contains an ordinary endermite spawner; Nether magma_box_1 contains an ordinary magma_cube spawner. Selected randomizers reference rs_spawners/ancient_cities/end and nether respectively, each with its matching sole entity at weight100 and block-light0..7. No ocean or trial spawner in the traced templates. Source selection does not establish successful spawn counts.

### authored_or_natural_enemies

Authored ocean drowned/guardian, Nether ghast and ordinary End endermite/Nether magma_cube spawners coexist with natural overrides. End full-bounds monster rules: phantom weight3 group1, endermite weight2 group3..7. Nether full-bounds rules: ghast weight10 group6..10, wither_skeleton weight1 group1..3. Ocean piece-bounds rule: drowned weight10 group2..5. End crystals are authored non-mob entities. Selection weights are not realized populations.

### intended_hostility

Loot-bearing ruined cities with variant-specific hostile template entities, ordinary spawners and natural monster overrides. Ocean traversal adds submerged-environment pressure; Nether selects a fire decoration feature. End crystals are separate authored non-mob entities. No difficulty tier, combat intensity or successful population is inferred.

### visual_discoverability

Large ruined city centers, walls, entrances and pillars provide architectural cues. End uses end-stone/purpur materials and chorus decoration; Nether uses dark/red masonry and fire decoration; ocean uses prismarine, seagrass and submerged ruins. Terrain and water may obscure these cues. No guaranteed visible entrance or measured sightline.

### underground_surface_classification

Variant-specific terrain placement, all size7 and beard_box adaptation. Ocean projects to OCEAN_FLOOR_WG using LOWEST_CORNER with offset-1, allows liquid and biome radius1: seabed/submerged intent. Nether uses absolute start32 and vegetal_decoration step: Nether terrain-associated city, not proven fully buried. End declares AVERAGE_LAND, start-3, minimum allowedY45 and terrain-height radius3: island-associated placement. These inputs are not final occupied height or measured burial. Accepted ocean saved geometry is a family example, not a bound on every variant.

## Processor scope and limits

The packaged catalog selects twelve ancient_cities processor lists, four per
variant, plus minecraft:empty. The pool trace has no missing components or
unresolved elements. End and Nether randomizer lists select the exact spawner
resources above. Existing repurposed-mansion-processors inspection binds the
manager and spawner processor behavior; base template IDs alone are not treated
as proof of effective replacement.

Ocean lists append the archaeology source via vanilla capped rule delegates.
Configured limits: generic4 and2, randomizer3 and3 and2, start10, walls2.
They select sand/gravel inputs, existing-world sand/gravel, or yellow-glass
markers against sand/gravel according to each rule. Yellow-glass removal follows
in generic/randomizer/walls lists. Bubble columns are selected for ticking.
These declarations do not prove realized archaeology counts or bubble behavior.
End start selects end_gateway_processor; no functional transport claim is made.
Other lists apply block rot, material rules, protected blocks and Nether noise
replacement. These are placement/degradation mechanisms, not extra families.

Authoritative references: family-decisions.json binds the packaged JSON catalog,
pool trace, template catalog, assembly identities, spawner-processor identities
and accepted geometry custody. Root definitions are retained in variants.
Literal loot references, template entity IDs and spawners remain explicitly
listed in the inventory, including non-mob end crystals. Configured feature
references resolve to minecraft:chorus_plant, structure_fire and structure_seagrass.
No population, detailed reward or sightline experiment is required for these
source and qualitative descriptions.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/repurposed-ancient-city-assessment-r2.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

The r1 attempt followed a failed in-memory edit (KeyError before any file write)
and therefore built unchanged inputs. It is not accepted as this assessment.
Use a fresh output path. Only this family and the input identity may change.
Item8 final integration, acceptance and PR/review/main delivery remain open.
