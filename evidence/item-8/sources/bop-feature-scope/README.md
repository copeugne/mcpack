# Biomes O' Plenty feature scope candidates

## Landmark descriptive attributes

Anomaly and monolith now have all eleven Item 8 descriptive attributes in the
family decisions and generated inventory. Sixteen added answers use the existing
full writers; no additional capture or runtime sample was needed.

Monolith chooses X/Z limits 1+nextInt(3) and loops inclusively from zero,
giving 2..4 blocks per axis. Its height limit h=5+nextInt(7) gives a write
range -6..h relative to support.above(), hence 12..18 blocks including the
below-origin part. The h-1 layer retains only corner columns. All writes use
the replace predicate; do not claim an intact solid foundation. Support must
be UNMAPPED_END_STONE and checked upper space must remain below Y=255.

Anomaly chooses n=2+nextInt(3), with inclusive cube coordinates 0..n, hence
a 3..5-block cube. Its offset o=nextInt(4) places that cube at Y=o..o+n
relative to selected support. Separate terrain loops run X/Z -3..n+3 and
Y=4 down through -127. The conservative combined envelope is therefore
9..11 blocks per horizontal axis and 132..135 vertically, including deep
conditional terrain processing. This is not visible cube height or occupied
volume. The cube requires air/ANOMALY space below Y=255; terrain writes remain
predicate-dependent and subject to world bounds.

Neither writer directly creates mobs, physical spawners or loot containers.
This supports direct source attribution, not a safety guarantee or proof about
later block interactions, harvested drops or ambient population. Preserve the
anomaly's stable interior and randomized surface states without inferring their
interaction behavior merely from enum names.

```sh
uv run pytest -q tests/item8/test_bop_feature_candidates.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-bop-landmark-descriptions.json
```

Extractor revision f92c2d3. Three class captures reproduce byte for byte.
Manifest SHA-256: 784dbe3703e88c8720cacd937195f867735f3b13c892d755cb0aaff389f18296.

```sh
uv run -m tools.inspect_item8_pool_elements --archive BiomesOPlenty-neoforge-1.21.1-21.1.0.13.jar --class-name biomesoplenty/worldgen/feature/misc/AnomalyFeature.class --class-name biomesoplenty/worldgen/feature/misc/MonolithFeature.class --class-name biomesoplenty/worldgen/feature/misc/BoneSpineFeature.class --output evidence/raw/item8/bop-feature-scope-r1
```

The packaged configured-feature catalog declares anomaly, monolith, bone_spine
and nether_bone_spine. The last two use the same biomesoplenty:bone_spine type.
All four names occur in the preserved live configured-feature registry. They
are not additional structure-registry roots.

MonolithFeature directly builds an obsidian form. BoneSpineFeature directly
places a bone-block column. AnomalyFeature changes terrain with AIR, NULL_BLOCK,
NULL_END_STONE and ANOMALY states. These are concrete landmark/terrain boundary
candidates; none requires reconstructing a template-pool graph. The full direct
writers are retained so final family-boundary decisions can cite actual content.
Do not turn the two bone-spine configured variants into two families by name.

This capture does not bind the feature registration class, prove placed-feature
or biome activation, or decide whether every natural decoration is a family.
Resolve these named boundaries in the scope inventory before detailed attributes.
No new world sample, measurement or material-balance work.
