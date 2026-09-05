# Moog library entry and registry declarations

Extractor e5341ca. Eight exact classes reproduced byte for byte before this
README was added. Identity manifest SHA-256:
b41a6b467762f7a23db7ac092adf820b9ada334421ce6ab4fff420f034689210.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive moogs_structures-neoforge-1.21.1-alpha-3.0.0.jar \
  --class-name com/finndog/moogs_structures/MoogsStructuresCommon.class \
  --class-name com/finndog/moogs_structures/neoforge/MoogsStructuresNeoforge.class \
  --class-name com/finndog/moogs_structures/modinit/MoogsStructuresConditionsRegistry.class \
  --class-name com/finndog/moogs_structures/modinit/MoogsStructuresPlacements.class \
  --class-name com/finndog/moogs_structures/modinit/MoogsStructuresProcessors.class \
  --class-name com/finndog/moogs_structures/modinit/MoogsStructuresStructurePlacementType.class \
  --class-name com/finndog/moogs_structures/modinit/MoogsStructuresStructures.class \
  --class-name com/finndog/moogs_structures/modinit/MoogsStructuresTags.class \
  --output evidence/raw/item8/moog-provider-entries-r1
```

Common initialization initializes tags, structure types, placement modifiers,
processors, pieces, pool elements and structure placement types. It attaches
setup, reload and server-start/stop listeners. Setup is empty; server lifecycle
methods call AsyncLocator. Reload attaches TrialSpawnerConfigManager. The NeoForge
entry forwards lifecycle/reload events and registers DebugCommand. Non-verbose
output preserves the defined callback bodies but does not bind every invokedynamic
bootstrap target. Do not claim complete callback dispatch from this capture alone.

Declarations expose the two already captured generic jigsaw structure codecs;
advanced_random_spread; minus_eight_placement, unlimited_count and
snap_to_lower_non_air_placement; and ten processor types. The processor types are
pillar, close-off-fluid, remove-floating-blocks, random-replace-with-properties,
super-gravity, flood-with-water, spawner, armor-stand, trial-spawner and vault.
Their implementations and retained consumers determine component effects, not
these names alone. ConditionsRegistry declares always_true/always_false; this
capture does not establish that its registry is initialized by the entry path.

The tag declarations are larger_locate_search, no_basalt and no_delta. These
reference existing structures, not additional authored roots. The four Moog data
providers' root/component coverage is already delivered and must not be repeated.

Remaining provider scope: declared mixin behavior (including pool replacement,
basalt/delta suppression, terrain adaptation and locate hooks), registry/service
dispatch, TrialSpawnerConfigManager and DebugCommand. Resolve these direct entry
routes before deciding whether any independent candidate is missing. Do not
exhaustively trace noise, geometry or unrelated utilities. The provider remains
open; no final family count or new measurement system is claimed.
