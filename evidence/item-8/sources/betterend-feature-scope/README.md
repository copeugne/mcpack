# BetterEnd feature family scope

Captured with f92c2d3. Three disassemblies and identities reproduce byte for byte.
Identity manifest SHA-256:
7a3fe03fddacad093573ad808d94b41463643acf11df321dc2b7a6fdeb5dd30d.

```sh
uv run -m tools.inspect_item8_pool_elements --archive BetterEnd-21.0.31.jar --class-name org/betterx/betterend/registry/EndFeatures.class --class-name org/betterx/betterend/world/features/BuildingListFeature.class --class-name org/betterx/betterend/world/features/CrashedShipFeature.class --output evidence/raw/item8/betterend-feature-scope-r1
```

EndFeatures registers building_list_feature with BUILDING_LIST_FEATURE and
crashed_ship with CRASHED_SHIP_FEATURE; static initialization binds the captured
classes. BuildingListFeature chooses StructureInfo using the configuration's
getRandom method, obtains its template and adds a ChestProcessor. It is a
feature-level template selector, not a structure-registry family root.

The existing packaged configured-feature catalog and live configured-feature
registry contain these six building-list definitions:

- betterend:blossoming_spires_structures: ruins.
- betterend:chorus_forest_structures: fallen trees, stumps and ruins.
- betterend:foggy_mushroomland_structures: fallen trees, stumps, library, ruins
  and tree house.
- betterend:lantern_woods_structures: cabin, light, logs, ruins and stumps.
- betterend:shadow_forest_structures: stumps, fallen logs, ruins and small mansion.
- betterend:umbrella_jungle_structures: jellyshroom cluster, houses and ruins.

Their explicit template paths, offsets, terrain-merger modes and default states
are preserved in sources/packaged-json-redacted.json.gz. Their IDs appear in
runtime/registry-r1/dumps/registry/minecraft/worldgen_configured_feature.txt.
These candidates are not represented by an explicit non_registry_content
contribution in the current decisions. Reconcile designs and variants next;
neither six feature definitions nor the individual template count is automatically
the number of canonical families. Separate vegetation candidates from authored
buildings and landmarks using actual content.

CrashedShipFeature selects minecraft:end_city/ship and has a dedicated placement
and erosion path. Its processor settings ignore stored entities. The captured
code's distance test reads X for both coordinates; do not silently describe this
as an X/Z radial test. Registration of the feature type does not prove an active
configured/placed instance. Active use remains to be established before including
it as another family. Do not investigate erosion details merely to decide whether
an active family exists.

This capture resolves candidate provenance for the scope pass. It does not close
family attributes, runtime occurrence or the final family count. Scoped extractor
Ruff and Basedpyright pass. No new world generation or measurement system.
