# Moog callback bindings and direct handlers

Extractor 6d7a961 enables verbose output for the two entry classes to resolve
missing invokedynamic bootstrap targets in the earlier non-verbose capture.
Earlier source evidence remains unchanged. Four classes reproduced byte for byte
before adding this README. Identity manifest SHA-256:
be01c1767b415e6898cb9ec54fe4e91b80ea2a10f3a3cd29cc9ecedbe8d45cbf.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive moogs_structures-neoforge-1.21.1-alpha-3.0.0.jar \
  --class-name com/finndog/moogs_structures/MoogsStructuresCommon.class \
  --class-name com/finndog/moogs_structures/neoforge/MoogsStructuresNeoforge.class \
  --class-name com/finndog/moogs_structures/commands/DebugCommand.class \
  --class-name com/finndog/moogs_structures/misc/trialspawnerconfig/TrialSpawnerConfigManager.class \
  --output evidence/raw/item8/moog-provider-callbacks-r1
```

The common entry's four callback targets are setup, registerDatapackListener,
serverAboutToStart and onServerStopping. NeoForge's six entry targets are
ResourcefulRegistriesImpl.onRegisterForgeRegistries, onSetup, onServerStarting,
onServerStopping, onAddReloadListeners and onRegisterCommands. The reload adapter
calls AddReloadListenerEvent.addListener. These bindings close the explicitly
recorded bootstrap omission; registry dispatch itself remains to be reconciled.

TrialSpawnerConfigManager reads the trial_spawner resource directory and converts
JSON into NBT compound values in a replacement map. Non-object values and parse
exceptions are logged and skipped. get returns the stored value (or null for an
absent key). It does not place structures or add a configured feature. Its data
consumers still determine effective spawner attributes; parsing is not validation
of successful gameplay behavior.

DebugCommand registers debug and keepjigsaws toggle/on/off/status branches under
moogs_structures. Its permission predicate checks level 2. Bodies call DebugFlags
and send/log status messages. They contain no authored-template or root definition.
Do not infer the initial flag values or all downstream effects from command names.
The keep-jigsaw behavior belongs to the declared replacement mixin and remains
part of that pending inspection.

Provider remains open for declared mixins and shared registry/service dispatch.
Do not recapture these callback targets or reinterpret the reload handler. Scoped
extractor Ruff/Basedpyright pass; no new measurement system or runtime experiment.
