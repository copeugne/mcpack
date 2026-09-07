# Explorify standalone source descriptions

Six families cover 15 roots and 16 standalone templates: badlands_pyramid,
desert_shrine, guide_post, supply_cache, watchtower and mausoleum. Integrated
32 missing descriptions and reconciled 24 existing attribution answers. All
traces and biome resolutions have no missing/unresolved entries. Raw templates
contain no jigsaw block entities; two mausoleums are whole-building alternatives.
Geometry reads template_size_xyz directly, including padding and rotation limits.

Exact root definitions come from packaged-json-redacted.json.gz. Standard jigsaw
surface offsets are pyramid -12..-9, shrine -10..-6, guide post -11 and others 0.
Mausoleum projects to WORLD_SURFACE; others WORLD_SURFACE_WG. No measured burial
or exposed height is inferred. Existing whole-template geometry is retained.

No top-level entity source occurs. Mausoleum supplies legacy zombie-spawner NBT;
other selected templates have no physical-spawner input. All spawn overrides are
empty, which does not suppress biome spawning. Pyramid includes TNT, not tested
trap operation. Exact saved loot references remain attributed to templates.
Guide post processors can change signal_fire or remove a campfire, so a guaranteed
smoke cue is not asserted. Stone/moss/cobweb/candle processors alter material and
presentation, not a measured discovery distance.

## Mausoleum overlay attribution

The existing generic resource selector excludes non-Lithostitched prefixes, so
its root-only processor selection cannot alone describe mausoleum loot. Direct
retained archive inspection establishes an additional source without changing
the selection framework. pack.mcmeta is copied byte-for-byte from
Explorify v1.6.5.mod.jar, archive SHA-256
2dc76398b48b2aae9b4024642da098b0880125572de160cb5ecf91d102890cad.
Metadata SHA-256 is
eb6b11cfa493820b871090a5b58abe2f4f132a56eca77b3218e3df9e3084ed2b.

It declares overlay f15 formats 15..512, covering baseline data format 48.
The retained f15/data/explorify/worldgen/processor_list/mausoleum_processor.json
adds a rule matching potted_dead_bush with probability 0.33, producing decorated_pot
and append_loot explorify:chest/mausoleum_pot. Both mausoleum templates contain
that input block. The exact processor hash and source-declared overlay attribution
are in loot_table_source, separate from saved dungeon loot references. This is
not a runtime pot-yield observation. Metadata capture is necessary to explain why
the root processor is insufficient; no new measurement or generalized tool.

Direct metadata reproduction: use retained_sources(Path.cwd()) to select the
exact named archive, verify its SHA-256 above, and read ZipFile member pack.mcmeta
without transformation. Compare its bytes/hash with the committed file. Processor
and template logic already reside in the retained catalogs with exact identities.
An initial inspection assumed an AdoraBuild-specific variants key; Explorify
instead uses generation_settings/common_generation_definition. The lookup failed
without edits; exact root JSON was then inspected and used for these answers.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-explorify-standalone-descriptions.json
uv run pytest -q tests/item8/test_explorify_provider_scope.py tests/item8/test_inventory_sources.py
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

## Black Spiral assembly

Ten explicit answers complete source assessment: six missing descriptions and
four reconciled attributions. Existing resolved biome answers are retained.
world-bounds observations 225/620 are the same ocean-heavy-seed start in two runs
at structure_starts, not full chunks. Inclusive envelope [116,31,346,128,78,442]
gives 13x48x97 planned-layout blocks. This is one layout reproduced, not two
independent samples, populated blocks or a family-wide bound. The root uses
standard jigsaw absolute 32, depth 7, no projection and no terrain adaptation.

Twenty reachable templates include the tower, bridges, resource/dungeon features
and vanilla bastion mob components. There are no missing graph references,
unresolved entity IDs or generation markers. Preserve template-owned piglin/brute
entities and legacy blaze/hoglin spawner inputs separately. No realized population,
conversion or simultaneous component selection is asserted. Empty spawn overrides
do not disable ambient spawning. Exact bridge/treasure chest sources remain saved
loot references; resource blocks remain distinct from container rewards.

Complete retained spiral_tower_randomization rules only replace material, including
blackstone to lava at a configured 0.01 match probability. The bridge processor
removes matching blackstone at 0.25. These are authored hazard ingredients and
rule probabilities, not observed hazard frequency or tested traversal difficulty.
No processor adds a mob, physical spawner or loot assignment. The graph and saved
assembly supply visual form while Nether terrain and chunk stage limit exposure
claims. No new source capture or measurement was necessary.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-explorify-spiral-descriptions.json
uv run pytest -q tests/item8/test_explorify_provider_scope.py tests/item8/test_inventory_sources.py
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```
