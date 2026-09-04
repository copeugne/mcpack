# Supplementaries dynamic biome tags

The retained `supplementaries-neoforge-1.21.1-3.6.8.jar` creates biome tags in
`ModServerDynamicResources`, rather than packaging them as static JSON files.
`identities.json` binds the original archive/class hashes to each disassembly.
Its SHA-256 is
`1b6470427cc06bc41e6d3e690b0475568c0ef274d1101ea05a912eeb87edc30d`.
Extraction source: `5a5f752`, extending `9124154`.

```sh
uv run -m tools.inspect_item8_pool_elements --archive supplementaries-neoforge-1.21.1-3.6.8.jar --output evidence/raw/item8/supplementaries-tags-reproduction
```

The preserved text output reproduced byte for byte. No JAR or class binaries
are committed. The generated increment is isolated because resolving these
missing packaged tags requires their generator and configuration-supplier code.

`ModServerDynamicResources` constructs `ModTags.HAS_ROAD_SIGNS`, adds
`BiomeTags.IS_OVERWORLD` when `CommonConfigs.Building.ROAD_SIGN_ENABLED` is true,
and publishes it as a biome tag. It constructs `ModTags.HAS_GALLEONS`, adds
`BiomeTags.IS_OCEAN` when `CommonConfigs.Functional.GALLEONS_ENABLED` is true,
and likewise publishes it. The tag builders are published even if empty.
`ModTags` supplies the names `supplementaries:has_road_signs` and
`supplementaries:has_galleons`.

The config binding paths are `building.way_sign.road_signs.enabled` and
`functional.cannon.plunderer.galleon`. `CommonConfigs.feature` combines a feature
supplier with an existing parent-category supplier using logical AND, so inspect
the relevant enabled parent toggles as well. The frozen config is
`evidence/item-6/frozen/config/supplementaries-common.toml`, SHA-256
`14210291891759b831951eba24c65985ed5bd27a7d09b6383aeb9fd3e8f1bc8c`.
The runtime's enabled pack list includes `supplementaries:generated_pack` in
`evidence/item-8/runtime/registry-r1/world-context.json`.

This resolves the source of the two missing packaged tags. Do not classify them
as absent or their structures as disabled from the static catalog alone. Merge
the verified conditional contributions into the biome input path, retaining
their code/config provenance. That integration and downstream attribute work
remain outstanding; this is not a direct runtime tag dump or Item 8 closure.
