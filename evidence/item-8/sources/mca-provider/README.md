# MCA membership source checkpoint

Extractor dd1cece. All 28 sources and the manifest independently reproduce
byte for byte. Manifest SHA-256:
d57838eeff0a970043dd26410cff0ac901fd70bbc498446b510366b0a88b77e1

```sh
uv run -m tools.inspect_item8_pool_elements --archive mca-neoforge-7.7.11+1.21.1.jar --class-name net/conczin/mca/mixin/MixinAbstractFurnaceBlockEntity.class --class-name net/conczin/mca/mixin/MixinActivity.class --class-name net/conczin/mca/mixin/MixinEntityType.class --class-name net/conczin/mca/mixin/MixinFlintAndSteelItem.class --class-name net/conczin/mca/mixin/MixinGoat.class --class-name net/conczin/mca/mixin/MixinHorseBase.class --class-name net/conczin/mca/mixin/MixinInventory.class --class-name net/conczin/mca/mixin/MixinMemoryModuleType.class --class-name net/conczin/mca/mixin/MixinMilkBucketItem.class --class-name net/conczin/mca/mixin/MixinPlayer.class --class-name net/conczin/mca/mixin/MixinProtoChunk.class --class-name net/conczin/mca/mixin/MixinSensorType.class --class-name net/conczin/mca/mixin/MixinServerGamePacketListenerImpl.class --class-name net/conczin/mca/mixin/MixinServerWorld.class --class-name net/conczin/mca/mixin/MixinSimpleParticleType.class --class-name net/conczin/mca/mixin/MixinTranslatableContents.class --class-name net/conczin/mca/mixin/MixinVillager.class --class-name net/conczin/mca/mixin/MixinVillagerInvoker.class --class-name net/conczin/mca/mixin/MixinVillagerProfession.class --class-name net/conczin/mca/mixin/MixinZombie.class --class-name net/conczin/mca/mixin/MixinZombieVillager.class --class-name net/conczin/mca/neoforge/ClientNeoForge.class --class-name net/conczin/mca/neoforge/CommonNeoForge.class --class-name net/conczin/mca/network/c2s/DestinyMessage.class --class-name net/conczin/mca/server/world/data/Village.class --class-name net/conczin/mca/server/world/data/VillageManager.class --class-name net/conczin/mca/util/BlockBoxExtended.class --class-name net/conczin/mca/util/WorldUtils.class --output evidence/raw/item8/mca-provider-r1
```

Preserves the automatic NeoForge entries, all 21 common mixins and the six
indexed structure-reference classes. WorldUtils locates existing registry
structures; DestinyMessage uses that location to teleport and set spawn state.
Chunk/world mixins forward existing villagers to SpawnQueue. VillageManager
scans and validates reported buildings and manages existing village records.
The building-type data consumer remains the next concrete membership question;
this source checkpoint does not close the provider or final family count.
