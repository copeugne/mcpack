# Biomes O' Plenty feature scope candidates

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
