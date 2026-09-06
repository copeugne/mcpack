# C2ME declared hooks: c2me-notickvd-remaining-hooks

Extractor 5347ff21fd07a10e07ed7fc4c6057342100cf211. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
e58c5347ca3360323cce37e6be5077dd245f3cad7609272ee92558d1e1e59fc3

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-notickvd-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/notickvd/mixin/MixinChunkDataSender.class --class-name com/ishland/c2me/notickvd/mixin/MixinChunkHolder.class --class-name com/ishland/c2me/notickvd/mixin/MixinChunkTicketManager.class --class-name com/ishland/c2me/notickvd/mixin/MixinChunkTicketManagerNearbyChunkTicketUpdater.class --class-name com/ishland/c2me/notickvd/mixin/MixinMinecraftServer.class --class-name com/ishland/c2me/notickvd/mixin/MixinPlayerManager.class --class-name com/ishland/c2me/notickvd/mixin/MixinServerAccessibleChunkSending.class --class-name com/ishland/c2me/notickvd/mixin/MixinServerBlockTicking.class --class-name com/ishland/c2me/notickvd/mixin/MixinServerChunkManager.class --class-name com/ishland/c2me/notickvd/mixin/MixinSimulationDistanceLevelPropagator.class --class-name com/ishland/c2me/notickvd/mixin/MixinThreadedAnvilChunkStorage.class --class-name com/ishland/c2me/notickvd/mixin/MixinWorld.class --class-name com/ishland/c2me/notickvd/mixin/MixinWorldChunk.class --class-name com/ishland/c2me/notickvd/mixin/ext_render_distance/MixinServerConfigurationNetworkHandler.class --class-name com/ishland/c2me/notickvd/mixin/ext_render_distance/MixinServerPlayNetworkHandler.class --class-name com/ishland/c2me/notickvd/mixin/servercore/MixinServerChunkManager.class --output evidence/raw/item8/c2me-notickvd-remaining-hooks-r1
```

This retains the remaining declared common/server hooks in this module.
Previously captured hooks are reused. The null scheduling declaration has
no class target and is preserved as packaged, not replaced or counted.
The raw disassemblies are isolated generated evidence for membership review;
this capture alone is not whole-provider closure or operational validation.

Hooks manage player chunk tickets, view distance, chunk sending and simulation visibility. Existing chunk state is delivered to players; no family is defined.

This identifies membership roles. It does not prove runtime activation,
unchanged world generation, persistence safety or concurrency correctness.
Do not turn this into a generic scheduler, I/O or network implementation audit.
