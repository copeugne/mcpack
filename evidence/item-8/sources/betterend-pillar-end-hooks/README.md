# BetterEnd pillar and vanilla End hooks

Selector d6f6c51 captures eight classes. The independent r1 capture reproduces all
files byte for byte. Manifest SHA-256:
f39ee57a16f67349f29e98bfdd3fe2acf567b39b9d56f737f9d8d3655f860e04.

```sh
uv run -m tools.inspect_item8_pool_elements --archive BetterEnd-21.0.31.jar --class-name org/betterx/betterend/world/features/terrain/FallenPillarFeature.class --class-name org/betterx/betterend/world/features/terrain/ObsidianPillarBasementFeature.class --class-name org/betterx/betterend/mixin/common/EndPlatformFeatureMixin.class --class-name org/betterx/betterend/mixin/common/EndPodiumFeatureMixin.class --class-name org/betterx/betterend/mixin/common/SpikeFeatureMixin.class --class-name org/betterx/betterend/mixin/common/EndSpikeMixin.class --class-name org/betterx/betterend/mixin/common/EndDragonFightMixin.class --class-name org/betterx/betterend/mixin/common/EndCityFeatureMixin.class --output evidence/raw/item8/betterend-pillar-end-hooks-r1
```

FallenPillarFeature and ObsidianPillarBasementFeature construct obsidian forms
using capped cones, displacement, rotation and mossy-obsidian postprocessing.
They require End-stone-tag support five blocks below the selected surface point;
FallenPillar also requires air at that point. Both fill through the existing
BCLib SDF implementation. Neither selects templates nor defines another authored
building in its own body. Keep named fallen-pillar and pillar-basement candidates
for the landmark/terrain decision; the class package name does not settle it.
Do not audit SDF geometry or measure dimensions merely to establish membership.

The six mixins are declared in betterend.mixins.common.json:

- EndPlatformFeatureMixin forwards vanilla createEndPlatform to TerrainGenerator.
  That helper remains an explicit consumer to reconcile.
- EndPodiumFeatureMixin uses GeneratorOptions.hasPortal/replacePortal and the
  active state to request portal/end_portal_active or portal/end_portal_inactive.
  These are alternative components of the existing exit portal.
- SpikeFeatureMixin checks hasPillars and replacePillars. For radius 2 through 5,
  it subtracts one to select pillar_base_1 through 4 and pillar_top_1 through 4,
  with the _cage suffix for guarded spikes. These twelve templates modify the
  existing central pillars; they are not twelve independent families. Other code
  preserves position/height state and places column/crystal content.
- EndSpikeMixin reads persisted pillar height unless direct-height mode is set.
- EndDragonFightMixin adapts existing portal discovery and crystal-based respawn
  to the replacement portal. It is not an independently located dungeon.
- EndCityFeatureMixin optionally rejects an existing End-city generation stub
  when useNewGenerator is true and nextInt(getEndCityFailChance()) is nonzero.
  A returned chance of 1 never rejects via that random branch. Configuration
  binding and interactions with other providers remain separate responsibilities.

These source boundaries establish candidate/component roles. They do not prove
which competing mixin wins, successful placement, gameplay or full provider
coverage. Reuse prior YUNG End Island captures when reconciling those interactions.
