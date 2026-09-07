# IDAS nexus assessment

Seven remaining entries integrated for one family/six alternatives. Existing
nominal dimensions are reused. No new runtime or tooling is added.

## mob_source

Six independent alternatives each contain an ordinary spawner with raw pig SpawnData; selected nexus_processor instead declares Integrated API randomization using idas:nexus, whose sole listed entity is quark:wraith weight5. Sculk additionally authors chicken and item entities. No missing components, unresolved template entities or generation markers. Natural silverfish/wraith overrides are separate. These source selections are not observed populations.

## loot_table_source

No literal template loot-table references. nexus_processor declares output_nbt.LootTable=idas:chests/nexus/nexus on a minecraft:rule, and that table definition exists. However the pinned ProcessorRule codec reads block_entity_modifier, not output_nbt, defaulting to Passthrough, so this legacy field does not assign the declared loot table. Record ineffective processor assignment as a baseline defect, not verified barrel loot or proof that all fixed contents are empty.

## generated_spawners

One ordinary raw-pig spawner per template alternative; no trial spawner. All select integrated_api:spawner_randomizing_processor with idas:nexus list: quark:wraith weight5. Settings delay20,min200,max800,count4,nearby6,player range16,spawn range4,block-light0..7. Existing manager inspection preserves missing-list fallback, unresolved-entry filtering, zero-total/null replacement and exception-to-pig branches; source configuration is not live spawn success.

## authored_or_natural_enemies

Processor-selected wraith is an authored spawner source, distinct from the raw pig template default. Root piece-bound natural overrides select silverfish and quark:wraith, each weight3 and group1..4. Sculk chicken and item entities are not hostile enemy declarations. No measured encounter population or spawning success is claimed.

## intended_hostility

Underground chamber design with ordinary spawner randomization declaring wraiths and natural silverfish/wraith overrides. The apparent barrel reward assignment uses unsupported legacy rule NBT and is ineffective by source inspection. Preserve hostile potential and the reward-assignment defect without inventing a difficulty tier or treating raw pig as the intended encounter.

## visual_discoverability

Broad multi-lobed underground chamber alternatives with central spawner, barrels, material variation and sculk detail. These offer local interior cues but no surface discovery marker is established. No visible entrance, sightline distance or generated exposure measurement.

## underground_surface_classification

Underground intent: generic_structure root, absolute startY-50, underground_structures step, size1, terrain_adaptation none, no heightmap projection. Six rigid single-template alternatives have preserved nominal dimensions. Fixed start height does not prove exact burial beneath every terrain column or realized occupied volume.

## Legacy loot assignment defect

Selected data/idas/worldgen/processor_list/nexus_processor.json first applies
minecraft:rule to barrels with probability1 and declares output_nbt containing
LootTable. There is no block_entity_modifier. In the pinned mapped Minecraft
server JAR, ProcessorRule's codec reads input_predicate,location_predicate,
position_predicate,output_state and block_entity_modifier. The last defaults to
Passthrough.INSTANCE. Passthrough.apply returns its input CompoundTag unchanged.
Thus the legacy declaration is not an effective loot assignment. The template
trace has no literal loot tables to supply the missing assignment independently.
This is not proof that fixed container contents are empty or measured loot yield.

Direct class identities in the frozen mapped server JAR:

- net/minecraft/world/level/levelgen/structure/templatesystem/ProcessorRule.class:
  634c46a5d148737f9b3646941d81c1cae912c7a7d05ca4504bf43bee6e35abc8.
- net/minecraft/world/level/levelgen/structure/templatesystem/rule/blockentity/Passthrough.class:
  ae61585b6d0daa9a4ad498147a16092cb8b88d4087c53e23e0bfb4b0082797dd.

Retained candidate class inspection found output_nbt in IntegratedBlockReplaceProcessor,
a different custom processor, not selected by this minecraft:rule. Direct
ProcessorRule references occur in builders, datagen and dungeon construction;
no corresponding codec compatibility hook was found in the retained candidates.
The mapped server JAR identity remains the existing frozen source identity.

Disposition: preserve the baseline defect; do not change frozen configuration.
A targeted inspection of top-level minecraft:rule processors in the packaged
catalog found only nexus_processor declaring output_nbt.LootTable. Comparing
these identities against direct processor edges of assessed families found only
nexus itself. No additional accepted family repair is identified by this check;
no broad regression surface or baseline change is added.

## Spawner interpretation

Reuse integrated-villages-provider content assessment and its processor_inspection
identities for Integrated API SpawnerRandomizingProcessor and MobSpawnerManager.
The processor replaces SpawnerBlock NBT; the manager reads
integrated_structure_spawners/nexus.json. Quark is present in the existing frozen
Mod List. Do not equate positive configuration weight with realized spawning.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-nexus-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c -classpath instances/pristine-baseline-v0/libraries/net/minecraft/server/1.21.1-20240808.144430/server-1.21.1-20240808.144430-srg.jar net.minecraft.world.level.levelgen.structure.templatesystem.ProcessorRule net.minecraft.world.level.levelgen.structure.templatesystem.rule.blockentity.Passthrough
```

Use a fresh output path. Only nexus and input identity may change.
Final integration, acceptance and PR/review/main remain open.
