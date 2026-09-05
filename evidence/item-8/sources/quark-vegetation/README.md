# Quark tree and water-petal generation

Captured at extractor revision b856c2f. identities.json binds the four captures
to the retained archive. All captures and identities reproduced byte for byte
before this README was added:

```sh
uv run -m tools.inspect_item8_pool_elements --archive Quark-4.1-480.jar --class-name org/violetmoon/quark/content/world/module/BlossomTreesModule.class --class-name org/violetmoon/quark/content/world/module/CherryGroveWaterPetalsModule.class --class-name org/violetmoon/quark/content/world/gen/BlossomTreeGenerator.class --class-name org/violetmoon/quark/content/world/gen/CherryGroveWaterPetalsGenerator.class --output evidence/raw/item8/quark-vegetation-b856c2f
```

BlossomTreesModule registers BlossomTreeGenerator for its tree entries at
TOP_LAYER_MODIFICATION, weight two. The generator applies the tree's biome
predicate and rarity draw, then checks soil support near MOTION_BLOCKING height.
It looks up the supplied configured-feature key, returns if absent, casts its
configuration to TreeConfiguration, and invokes Feature.TREE with that context.
It may clear a replaceable block at the tree origin first. The tree placement
result is discarded. This is evidence of delegated tree placement, not a new
structure template or successful observed tree. Exact selected tree entries and
their decorators are not established by these outer classes alone.

CherryGroveWaterPetalsModule registers its generator at TOP_LAYER_MODIFICATION,
weight one. Generation requires staticEnabled and a chance draw, then performs
the configured number of local attempts. It checks the configured biome and
scans downward from an offset of 70 while Y>10 for water below the candidate.
The place method has two explicit modes: leaf carpet when useCarpet and
LeafCarpetModule enablement permit it, or petal patches when useCarpet is false
and PetalsOnWaterModule is enabled. Otherwise it logs that configuration
prevented placement. Core positions require air over water. The petal branch
adds variable edges. This is water-surface vegetation placement; no authored
room, spawner or chest operation is present in this direct generator.

Working boundary: the inspected water-petal placement is vegetation, not an
additional structure family. Blossom generation is a tree contribution, but
selected configured-feature/decorator attribution remains open before its
coverage disposition is finalized. Do not turn petal counts or random tree
instances into families, or expand into unrelated crafting/material audits.
Effective configuration and observed occurrence are not claimed here. Scoped
extractor Ruff and Basedpyright checks passed. No new measurement or server run.

## Selected blossom definitions reconciled

The selected packaged definitions now resolve the decorator gap above.
BlossomTreesModule supplies blue_blossom, lavender_blossom, orange_blossom,
yellow_blossom and red_blossom through registerKey and its configured-feature
fields. All five corresponding Quark definitions select minecraft:tree,
minecraft:fancy_trunk_placer and minecraft:fancy_foliage_placer, with empty
decorators. The committed test binds the catalog, selected archive and each
definition hash, then checks these properties:

```sh
uv run pytest -q tests/item8/test_feature_modifier_references.py -k blossom
```

Together with the preserved generator's explicit Feature.TREE delegation, this
supports a working vegetation disposition for blossom trees. Water petals have
the same no-additional-family disposition from their direct placement path.
This resolves the selected-definition gap, not effective occurrence or complete
provider coverage. No new measurement is needed for these family boundaries.
