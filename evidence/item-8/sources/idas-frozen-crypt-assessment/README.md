# IDAS frozen crypt assessment

Nine remaining entries for entrance/crypt components. Existing catalogs and
processor inspection suffice; no new runtime or measurement system.

## mob_source

Entrance has no authored entities; crypt component authors strays and iceandfire:troll. Ice and Fire is absent from the frozen runtime, so troll declaration is not a confirmed inhabitant. No unresolved authored entity compounds. Crypt ordinary spawners are a separate source; selected frozen_crypt_processor replaces their NBT using sole minecraft:stray weight5. No realized population is claimed.

## loot_table_source

Crypt component references the defined idas:chests/frozen_crypt/frozen_crypt table; entrance has no literal loot reference. Selected spawner-only processor assigns no container loot NBT. Source attribution is not measured reward yield.

## generated_spawners

Crypt has five ordinary spawners: four raw SpawnData.entity compounds are empty and one declares stray; all potentials empty. Preserve unresolved raw paths for block_entities0,1,5,7. Selected frozen_crypt_processor acts on every existing spawner and replaces NBT using idas:frozen_crypt, sole minecraft:stray weight5. Delay20,min200,max800,count4,nearby6,player range16,spawn range4,block-light0..7. Existing processor/manager semantics and fallback limitations apply. No entrance/trial spawners. Crypt /block_entities/9 is CORNER with empty metadata, not DATA enemy instructions. Selected sources are not observed successful spawns.

## authored_or_natural_enemies

Direct authored strays and processor-selected stray spawners are distinct hostile sources. Optional troll has an absent provider. Empty root spawn_overrides declares no family-specific natural override; environmental spawning remains separate. Raw empty spawner data is preserved, not treated as an unidentified effective mob after supported processor replacement.

## intended_hostility

Small entrance attached to a larger crypt with direct strays and five ordinary spawner inputs selecting strays. Hostile potential is supported without relying on the absent optional troll, assigning an Item9 tier or measuring encounter intensity.

## visual_discoverability

Surface entrance is a smaller discovery cue than the attached lower crypt. Nominal29 by36 footprint and21 height include hidden lower geometry and padding, not measured visible silhouette or sightlines. Terrain and snow may obscure access.

## underground_surface_classification

Surface-associated entrance with lower crypt. Root generic_structure projects WORLD_SURFACE_WG offset0,size2,terrain range10/radius1,ignore_waterlogging,enhanced adaptation none. Entrance element separately declares custom beards/carves,kernel size10/distance10. Both rigid. Nominal crypt origin(-7,-15,-14) does not establish measured burial or terrain alteration.

## Geometry and evidence

Family evidence binds templates-redacted, pool-traces-content and packaged JSON.
Under data/idas/structure/frozen_crypt/, frozen_crypt1.nbt is16,6,14 with down_west
connector0,0,13; frozen_crypt2.nbt is29,15,36 with up_west connector7,14,27.
Matching frozen_crypt aligned joints give adjacent crypt origin-7,-15,-14.
Inclusive union x-7..21,z-14..21,y-15..5 gives29 by36 horizontal and21 vertical.
Nominal complete layout is not observed burial or guaranteed placement. Each
corresponding pool has one rigid element. Trace has no missing components or
unresolved elements. Entrance terrain kernel10/10 is separate from root none.

Both pools select worldgen/processor_list/frozen_crypt_processor.json, containing
only ordinary spawner randomization. integrated_structure_spawners/frozen_crypt.json
contains sole minecraft:stray weight5. Reuse integrated-villages-provider's pinned
SpawnerRandomizingProcessor/MobSpawnerManager inspection, which establishes NBT
replacement for existing spawner blocks. Thus the four empty raw entity compounds
are not unresolved selected mob identities. Preserve them at /block_entities/0,1,5,7;
/block_entities/8 has raw stray. All potentials empty. /block_entities/9 is CORNER
with empty metadata. No trial spawners or authored entity-ID gaps.

The literal loot definition exists under data/idas/loot_table/chests/frozen_crypt/.
Existing runtime_mod_ids parsing of registry-r1/debug.log confirms iceandfire absent;
log SHA-256 e5b47378d791027242ba28dd36c999c07ae4e01a1b90e1534e66bcd42c1e694b.
The optional troll is not a demonstrated encounter. No population or reward-yield
measurement is required to inventory these declarations and selected sources.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-frozen-crypt-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only frozen_crypt and input identity may change.
Final integration, acceptance and PR/review/main remain open.
