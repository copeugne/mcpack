# Chef's Delight village component injection

Captured with extractor revision d052bb2. Both verbose disassemblies and
identities reproduced byte for byte. This closes a provider relationship gap:
packaged templates lack corresponding standalone structure roots or pool JSON.

```sh
uv run -m tools.inspect_item8_pool_elements --archive chefsdelight-1.0.5-neoforge-1.21.1.jar --class-name net/redstonegames/chefsdelight/ChefsDelight.class --class-name net/redstonegames/chefsdelight/worldgen/village/VillageStructures.class --output evidence/raw/item8/chefsdelight-villages-r1
```

ChefsDelight's constructor registers a NeoForge.EVENT_BUS listener whose
bootstrap entry 2 targets VillageStructures.addNewVillageBuilding. Its event
parameter is ServerAboutToStartEvent. That handler obtains the server's template
pool and processor registries and requests cook-house and chef-house additions
for plains, desert, taiga, savanna and snowy vanilla village house pools.
Template names are chefsdelight:<variant>_cook_house and
chefsdelight:<variant>_chef_house. These are village components, not independent
structure families. Both plains additions read Config.cookHousePlains; do not
substitute a presumed chefHousePlains input for the chef-house call site.

addBuildingToPool returns if the target pool is absent. Otherwise it resolves
minecraft:empty processors, creates a rigid SinglePoolElement and appends it
to StructureTemplatePool.templates once per iteration below the supplied weight.
The method does not update rawTemplates. Therefore a packaged pool trace or
serialized raw entry list alone cannot prove these additions absent. A zero
or negative supplied weight produces no append; frozen effective settings
remain to be joined before claiming activation or counts.

Next: record this provider's component relationship in the existing decisions,
join the frozen weights and selected template content where required by the
village attributes, and reconcile runtime pool evidence with the mutation path.
Do not create separate families for chef/cook houses or expand into villager
trade economics. Scoped extractor Ruff and Basedpyright passed. No new runtime
sample or measurement system.

## Packaged content of injected houses

The focused catalog join binds all ten direct house templates to the retained
Chef's Delight archive. Each has an empty authored entity list and no vanilla
spawner block-entity entry; all explicit LootTable references use
chefsdelight:chests/cooker, which resolves in the selected packaged loot catalog.
This is base component content, not proof of no enemies or effective loot.

The snowy cook house additionally connects to minecraft:village/snowy/villagers.
Cook houses in plains, desert and taiga reference minecraft:village/plains/streets.
Other entrance connectors reference minecraft:empty. Do not infer no villagers
from empty direct entity lists or normalize the non-plains street references.
Jigsaw expansion and the consuming village remain relevant to generated content.

```sh
uv run pytest -q tests/item8/test_chefsdelight_components.py
```

The focused test and Ruff pass. Basedpyright initially reported an unhashable
JsonValue in the loot-reference assertion; a string type annotation corrected
that static finding and Basedpyright now passes. No additional runtime sample.
