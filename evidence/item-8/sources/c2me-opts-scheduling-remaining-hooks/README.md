# C2ME declared hooks: c2me-opts-scheduling-remaining-hooks

Extractor 5347ff21fd07a10e07ed7fc4c6057342100cf211. Independent r1 reproduction
matches every disassembly and identity manifest. Manifest SHA-256:
8eba7c80e0dfe78ef5881b00722855887bde370722f80d8bf466aae1577c165e

```sh
uv run -m tools.inspect_item8_pool_elements --archive c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar --nested-archive META-INF/jars/c2me-opts-scheduling-mc1.21.1-0.3.0+alpha.0.93.jar --class-name com/ishland/c2me/opts/scheduling/mixin/general_overheads/MixinThreadedAnvilChunkStorage.class --class-name com/ishland/c2me/opts/scheduling/mixin/idle_tasks/autosave/disable_vanilla_mid_tick_autosave/MixinThreadedAnvilChunkStorage.class --class-name com/ishland/c2me/opts/scheduling/mixin/idle_tasks/autosave/enhanced_autosave/MixinMinecraftServer.class --class-name com/ishland/c2me/opts/scheduling/mixin/idle_tasks/autosave/enhanced_autosave/MixinThreadedAnvilChunkStorage.class --class-name com/ishland/c2me/opts/scheduling/mixin/mid_tick_chunk_tasks/MixinMinecraftServer.class --class-name com/ishland/c2me/opts/scheduling/mixin/mid_tick_chunk_tasks/MixinServerChunkManager.class --class-name com/ishland/c2me/opts/scheduling/mixin/mid_tick_chunk_tasks/MixinServerWorld.class --class-name com/ishland/c2me/opts/scheduling/mixin/mid_tick_chunk_tasks/MixinWorld.class --class-name com/ishland/c2me/opts/scheduling/mixin/ordering/player_move/MixinServerPlayNetworkHandler.class --class-name com/ishland/c2me/opts/scheduling/mixin/shutdown/MixinMinecraftServer.class --class-name com/ishland/c2me/opts/scheduling/mixin/shutdown/MixinServerEntityManager.class --class-name com/ishland/c2me/opts/scheduling/mixin/shutdown/MixinServerWorld.class --class-name com/ishland/c2me/opts/scheduling/mixin/task_scheduling/MixinChunkHolder.class --class-name com/ishland/c2me/opts/scheduling/mixin/task_scheduling/MixinEntityChunkDataAccess.class --class-name com/ishland/c2me/opts/scheduling/mixin/task_scheduling/MixinServerChunkManager.class --output evidence/raw/item8/c2me-opts-scheduling-remaining-hooks-r1
```

This retains the remaining declared common/server hooks in this module.
Previously captured hooks are reused. The null scheduling declaration has
no class target and is preserved as packaged, not replaced or counted.
The raw disassemblies are isolated generated evidence for membership review;
this capture alone is not whole-provider closure or operational validation.

Hooks change autosave, mid-tick tasks, shutdown flushing, lighting-dirty scheduling and executor choice. These manage existing server work; no family is defined.

This identifies membership roles. It does not prove runtime activation,
unchanged world generation, persistence safety or concurrency correctness.
Do not turn this into a generic scheduler, I/O or network implementation audit.
