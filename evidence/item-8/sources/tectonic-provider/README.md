# Tectonic generation boundaries

Frozen archive: tectonic-3.0.22-neoforge-21.1.jar.
SHA-256: bf5cf7e351586865905eceb2a63e06769f8cd0f9c826864b6a30541e20cffc56.
Selector bde0d25 captures 30 entry, command, compatibility, generation and mixin
classes. Identity manifest SHA-256:
b807dc5f98fab2557300678fb3b69e5504fef767f1c84ab160590924452fafd9.
The following command was run at that selector revision and reproduced exactly:

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive tectonic-3.0.22-neoforge-21.1.jar \
  --output evidence/raw/item8/tectonic-provider-r1
```

The separately captured ConfigState resolves the concrete predicate dependency
exposed by ConfigLoadPredicate. Selector 1343b1c, manifest SHA-256
cf630dfe5cf8b8ff093d293db9cdd0a259eb1050a1f43f30dedf8d8f5d3951c4:

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive tectonic-3.0.22-neoforge-21.1.jar \
  --class-name dev/worldgen/tectonic/config/state/ConfigState.class \
  --output evidence/raw/item8/tectonic-config-selection-r1
```

Both source captures were independently reproduced before adding this README.
The second manifest is in ../tectonic-config-selection/identities.json.
No new runtime experiment or configuration change was needed.

TectonicNeoforge initializes configuration, registers four density-function
codecs, height_stabilized_count, set_height_limits and configuration predicates,
adds the resourcepacks/tectonic server-data pack when enabled, and registers
commands. The client entry installs configuration UI. The command searches
density-function conditions for terrain locations and produces debug output;
the toolkit exporter produces configuration JSON, not world layouts.

ConfigClamp, ConfigConstant, ConfigNoise and Invert compute scalar terrain
values. HeightStabilizedCount supplies positions to a consuming feature.
SetHeightLimitsModifier changes the configured dimension and noise height limits.
Neither supplies an independently authored structure. ConfigLoadPredicate and
ConfigResourceCondition delegate to ConfigState.test. In that switch,
river_lanterns and river_ice read the corresponding continent settings;
no_carvers negates carversEnabled; ore_fix and ultrasmooth read their settings.

StructurePieceMixin shifts OCEAN_MONUMENT_BUILDING bounding boxes by the
configured monumentOffset while the mod is enabled. This modifies an existing
structure candidate, not a new design. Other declared mixins adjust snow height,
terrain blending and serialization, heightmaps, lava level, noise identities and
world-preset UI. WorldCarverMixin is packaged but absent from both declared lists;
do not infer its activation. Retain these effects for applicable family attributes
without expanding candidate enumeration into a terrain correctness audit.

Packaged feature and overlay reconciliation is recorded in provider-scope.md.
In particular underground-river lanterns require a named candidate disposition;
the absence of structure-registry definitions is not an absence proof.
