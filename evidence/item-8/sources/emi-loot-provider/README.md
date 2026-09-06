# EMI Loot membership entry paths

Extractor bd44128d. Independent r1 reproduction matches all source and manifest
bytes. Manifest SHA-256: 30d1b35994e3b901231cf0a42e4830a1e851e8e8dbf2801164b656ca15cc5196

```sh
uv run -m tools.inspect_item8_pool_elements --archive emi_loot-0.7.9+1.21+neoforge.jar --class-name fzzyhmstrs/emi_loot/EMILoot.class --class-name fzzyhmstrs/emi_loot/neoforge/EMILootNeoForge.class --class-name fzzyhmstrs/emi_loot/neoforge/EMILootAgnosNeoForge.class --class-name fzzyhmstrs/emi_loot/neoforge/events/EMILootGameEvents.class --class-name fzzyhmstrs/emi_loot/neoforge/events/EMILootClientGameEvents.class --class-name fzzyhmstrs/emi_loot/neoforge/events/EMILootClientModEvents.class --class-name fzzyhmstrs/emi_loot/mixins/DataPackContentsMixin.class --class-name fzzyhmstrs/emi_loot/mixins/ReloadableRegistriesMixin.class --class-name fzzyhmstrs/emi_loot/server/ServerResourceData.class --class-name fzzyhmstrs/emi_loot/server/LootBuilder.class --output evidence/raw/item8/emi-loot-provider-r1
```

Four automatic entries register loot condition/function codecs, client display,
client-bound synchronization and reload parsing. The two injection hooks invoke
loot parsing and postprocessing. Direct-drop resources populate a private map;
NeoForge table-load events may transform those parsed tables. Remaining check:
parser output role and the accessor-only hooks before membership closure.
