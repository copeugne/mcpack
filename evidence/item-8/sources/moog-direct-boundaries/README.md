# Moog direct helper and registry boundaries

Six classes captured with extractor 266938e and reproduced byte for byte before
adding this README. Identity manifest SHA-256:
3510352c83508427eb6205590804a8b2121376214f6566a9dd4cd304ae9580d6.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive moogs_structures-neoforge-1.21.1-alpha-3.0.0.jar \
  --class-name com/finndog/moogs_structures/utils/MixinUtils.class \
  --class-name com/finndog/moogs_structures/utils/DebugFlags.class \
  --class-name com/finndog/moogs_structures/world/structures/terrainadaptation/beardifier/EnhancedBeardifierHelper.class \
  --class-name com/finndog/moogs_structures/platform/Services.class \
  --class-name com/finndog/moogs_structures/platform/IRegistryPlatform.class \
  --class-name com/finndog/moogs_structures/modinit/registry/neoforge/ResourcefulRegistriesImpl.class \
  --output evidence/raw/item8/moog-direct-boundaries-r1
```

MixinUtils checks existing structure references, tags, starts and piece bounds
for the basalt/delta suppression hooks. It reads chunks at structure lifecycle
statuses; this is not a claim of side-effect-free world access. It defines no
new authored design. DebugFlags contains two static booleans with no initializer,
so both initially default to false. Commands can subsequently change them.

EnhancedBeardifierHelper selects existing starts implementing enhanced terrain
adaptation, derives piece and junction iterators, and adjusts the incoming
density using their bounds and adaptation settings. This is terrain adaptation
around existing structures, not a separate authored family. Geometry and noise
internals are unnecessary for this candidate-boundary decision.

Services loads the first IRegistryPlatform service or throws when none exists.
The interface accepts caller-supplied registries and names. Its packaged service
implementation creates NeoForgeResourcefulRegistry wrappers; custom-registry
requests are queued for NewRegistryEvent. Neither class declares an additional
authored root. The wrapper's registration behavior remains a direct unresolved
boundary, distinct from unrelated registry convenience methods.

This capture resolves these helper interpretations, not whole-provider closure
or effective family attributes. Existing entry, mixin and generator captures must
be reused rather than repeated.
