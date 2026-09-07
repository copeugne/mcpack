# IDAS necromancer spire assessment

Nine remaining entries for four connected components. Existing catalogs and
processor inspection suffice; no new runtime or measurement system.

## mob_source

Pieces1,3 author illusioners and optional soul vultures; piece1 adds skeletons; pieces1,2,3 author wither skeletons. Piece2 also authors a skeleton horse, distinct from the hostile skeleton mobs; glass frames are non-mob entities. AlexsMobs is absent, so soul-vulture declarations do not prove successful inhabitants. Piece4 has no authored entities. No unresolved entity compounds. Spawner and natural override sources remain separate; ticking-only processor does not randomize these sources.

## loot_table_source

Pieces1,2,3 reference the defined idas:chests/necromancers_spire/necromancers_spire table. Piece4 has no literal loot reference. Selected ticking-only waterlogging_fix_processor assigns no loot NBT. This identifies sources without measuring yields or asserting operating machinery.

## generated_spawners

Pieces1 and3 each contain one skeleton and one alexsmobs:soul_vulture ordinary spawner, all with empty SpawnPotentials. Selected ticking-only processor does not randomize their raw data. Absent AlexsMobs means the soul-vulture spawners are not confirmed successful spawning sources. Pieces2,4 have none; no trial spawners. Piece2 /block_entities/22 is CORNER with empty metadata, not a DATA enemy instruction. Four physical source blocks are not four demonstrated functioning spawners.

## authored_or_natural_enemies

Direct illusioners,skeletons,wither skeletons and ordinary skeleton spawners are distinct authored hostile sources. Soul-vulture entity/spawner declarations have an absent provider. Skeleton horse and frames are not counted as hostile skeleton mobs. Root natural monster override uses piece bounds with quark:wraith weight10,group1..1. This natural source is distinct from authored placement and does not measure realized population.

## intended_hostility

Nether spire with directly authored hostile mobs, ordinary spawner sources and natural wraith override. These establish hostile potential while preserving the failed optional-provider assumptions. No Item9 tier, measured encounter intensity or player spell-progression system is introduced.

## visual_discoverability

Tall connected spire provides an architectural cue in Nether terrain. Nominal27 by46 footprint and89 height include padding and all four pieces, not a measured visible silhouette, sightline or safe approach. Nearby terrain can obscure the tower; no visibility guarantee.

## underground_surface_classification

Nether lava-associated spire using integrated_api:over_lava_nether_structure,absolute start-height31,size4,surface_structures step,terrain adaptation none,ignore_waterlogging. All components rigid. These root settings do not prove observed lava clearance or terrain burial. Nominal upper piece starts43 blocks above main; actual complete placement is unmeasured.

## Geometry and evidence

Family evidence binds templates-redacted, pool-traces-content and packaged JSON.
Under data/idas/structure/necromancers_spire/, piece1 up_south at23,42,26 joins
piece2 down_south at23,0,26, giving piece2 origin0,43,0. Piece1 south_up at22,42,26
joins piece3 north_up at18,40,0, giving piece3 origin4,2,27. Piece2 south_up at22,0,26
joins piece4 north_up at18,0,0, giving piece4 origin4,43,27. All joints aligned
and names/targets match numbered next components. Sizes27,43,27;27,46,27;
19,41,19;19,29,19 produce inclusive union x0..26,z0..45,y0..88, hence27 by46
horizontal and89 vertical. Nominal complete assembly is not observed successful
placement. Corresponding template_pool resources each have one rigid element;
trace has no missing components or unresolved elements.

All select waterlogging_fix_processor; reuse the pinned ticking-only inspection
in idas-desert-market-assessment. It does not randomize source spawners or assign
entity/container-loot NBT. Pieces1,3 retain skeleton and soul-vulture SpawnData
with empty potentials. AlexsMobs absence is established by the frozen Mod List
identity in idas-ruins-of-the-deep-assessment. Preserve optional-source failures
without changing the baseline or declaring the whole family inactive.
Piece2 /block_entities/22 is CORNER with empty metadata. The shared literal loot
definition exists under data/idas/loot_table/chests/necromancers_spire/.
Root spawn_overrides.monster uses piece bounds, quark:wraith weight10,min/max1.
Quark is present; override inputs are not observed encounter quantities.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-necromancers-spire-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only necromancers_spire and input identity may change.
Final integration, acceptance and PR/review/main remain open.
