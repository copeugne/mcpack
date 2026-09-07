# IDAS haunted manor assessment

Nine remaining entries. Existing connector defect required inspecting the pinned
consumer, not a repair or new runtime measurement system.

## mob_source

Frozen default start piece1 authors skeletons. Its outgoing target/name namespace mismatches reject pieces2 and4; piece3 depends on2. Retain packaged piece2 skeleton/item and pieces2,3 glass-frame declarations without attributing them to the connected frozen layout. No unresolved authored entity compounds. Ice and Fire absent means ModAdaptiveStructure retains default pool, not compatibility templates. Ticking-only processor does not inject mobs.

## loot_table_source

Three defined literal idas:chests/haunted_manor/ tables: haunted_manor,haunted_manor_tools,haunted_manor_treasure all occur in starting piece1. Detached piece2 additionally references manor/treasure, preserved as packaged attribution only. Pieces3,4 have no literal references. Ticking-only processor assigns no loot NBT. No measured reward yield.

## generated_spawners

Starting piece1 has two ordinary spawners with skeleton and cave_spider SpawnData, empty potentials. Detached piece2 contains three (zombie,skeleton,skeleton), preserved as packaged sources rather than connected generated sources. Ticking-only processor does not randomize them. No trial spawners or generation markers. Five packaged blocks are not five spawners in the frozen connected layout or demonstrated successful spawns.

## authored_or_natural_enemies

Starting piece skeletons and ordinary skeleton/cave-spider spawners are authored sources. Root natural monster override uses full bounds with quark:wraith weight3,group3..4. Detached piece2 contents are preserved separately. Exact connector failure limits assembled bounds; natural spawning rule is not a measured population. Quark is present.

## intended_hostility

Intended multi-piece haunted manor has a frozen connector namespace defect. Starting piece still declares hostile skeletons and spawner sources, plus natural wraith override. Preserve defect and detached content without repairing baseline, declaring the whole family inactive, assigning an Item9 tier or claiming full intended encounters.

## visual_discoverability

Surviving starting piece supplies a manor architectural cue with nominal47 by36 footprint and48 height. Intended detached wings do not enlarge the frozen connected estimate. Source extents include padding and do not measure sightlines, exposed silhouette or complete appearance in terrain.

## underground_surface_classification

Surface-associated mod_adaptive_structure: WORLD_SURFACE_WG offset0,size4,terrain range10/radius3,ignore_waterlogging,custom beards/carves,kernel size15/distance15. Ice and Fire absent selects default pool. Both outgoing default joints fail exact target/name equality; no joined second/fourth component or downstream third. Actual terrain burial and alteration remain unmeasured.

## Connector defect and evidence

Family evidence binds templates-redacted, pool-traces-content and packaged JSON.
Default haunted_manor1.nbt size47,48,36 has two outgoing joints targeting
minecraft:haunted_manor2 and minecraft:haunted_manor4. Receiver names in default
pieces2,4 use idas:, not minecraft:. Piece2's connector to3 cannot be reached
after both start connections are rejected. All four pools contain one rigid
element and empty fallback. Pool graph completeness is not connector compatibility.
No target, raw template or pool is repaired. Existing ModAdaptiveStructure
inspection and absent iceandfire runtime declaration establish default selection.

Direct javap inspection of the pinned Integrated API classes establishes:
PieceLimitedJigsawManager$Assembler invokes GeneralUtils.canJigsawsAttach at
bytecode660 and skips attachment on false at663. GeneralUtils.canJigsawsAttach
checks opposing fronts, compatible top/joint orientation and exact String.equals
between parent target and child name at81. Thus neither start edge can pass;
rotation cannot repair the namespace difference. Class identities:

- com/craisinlord/integrated_api/utils/GeneralUtils.class: 7e7b059090c26be6af8dd106d368c842670a40ceab80bde7ffaf8d5d4dcd5dbb
- com/craisinlord/integrated_api/world/structures/pieces/manager/PieceLimitedJigsawManager$Assembler.class: 0d57b618a364d45e1fa71806d957ca299d547f6762f169e42592a0041b021418

Inspect with pinned javap -p -c against
 downloads/item3/candidates/integrated_api-1.7.3+1.21.1-neoforge.jar,
using dotted class names corresponding to the identities above. Existing
integrated-villages-provider records the pinned provider identity and consumer
context. Vanilla JigsawBlock was also checked, but the Integrated API predicate
above is the relevant assembler dependency.

Starting piece alone gives47 by36 horizontal and48 vertical. This is a derived
frozen-layout estimate, not a measured world sample or repaired design. Preserve
all four source template mappings. Piece1 skeleton/cave-spider spawners and piece2
zombie/skeleton/skeleton spawners have empty potentials; selected ticking-only
processor leaves these sources unchanged. Reuse idas-desert-market-assessment's
pinned processor inspection. Three literal tables are defined under
 data/idas/loot_table/chests/haunted_manor/. No trial spawners or markers.
Root full-bounds wraith3,group3..4 is a separate natural source, not population.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-haunted-manor-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only haunted_manor and input identity may change.
Final integration, acceptance and PR/review/main remain open.
