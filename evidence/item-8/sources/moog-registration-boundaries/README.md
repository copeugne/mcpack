# Moog registration and lifecycle boundaries

Five classes captured with extractor f28c96b. Independent extraction reproduced
all files byte for byte before this README. Identity manifest SHA-256:
ec022b522c0208356afa7e2042b5af071139809e1d39db68980a07618847f252.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive moogs_structures-neoforge-1.21.1-alpha-3.0.0.jar \
  --class-name com/finndog/moogs_structures/modinit/registry/neoforge/NeoForgeResourcefulRegistry.class \
  --class-name com/finndog/moogs_structures/modinit/registry/ResourcefulRegistries.class \
  --class-name com/finndog/moogs_structures/utils/AsyncLocator.class \
  --class-name com/finndog/moogs_structures/utils/neoforge/PlatformHooksImpl.class \
  --class-name com/finndog/moogs_structures/datagen/StructureNbtUpdaterDatagen.class \
  --output evidence/raw/item8/moog-registration-boundaries-r1
```

ResourcefulRegistries forwards caller inputs to the already inspected platform
service. NeoForgeResourcefulRegistry creates DeferredRegister with the supplied
registry and namespace, registers supplied names and suppliers, and attaches it
to the mod event bus at init. It does not declare extra content or scan for it.
Registry-entry containers need no independent family interpretation.

AsyncLocator's lifecycle handlers create/shut down an executor. Its two locate
paths use the supplied tag or holder set with vanilla findNearestMapStructure,
then complete the associated future. They locate existing registered structures;
this does not establish that locating has no chunk-generation side effects.
PlatformHooksImpl answers mod-presence and development-environment queries only.

StructureNbtUpdaterDatagen.gatherData accepts GatherDataEvent and adds the NBT
updater to its DataGenerator when server data is included. This is a build-time
resource writer, not a world-generation event or additional live family. The
frozen packaged archive, not hypothetical later generated output, is the input.

These direct boundaries, together with prior entries, mixins, service, helper,
generator and pool captures, support the separate full-provider scope check.
They do not resolve downstream footprint, effective loot or spawner attributes.
