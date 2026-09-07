# Repurposed witch-hut assessment

Six remaining attributes are integrated for the six-variant witch-hut family.
Dimension, template footprint/height and intended hostility were already assessed.
This increment uses existing sources, without new capture or tooling.

## Exact evidence and derivation

In packaged-json-redacted.json.gz inspect the six root definitions
`data/repurposed_structures/worldgen/structure/witch_hut_*.json`, their start pools
under `worldgen/template_pool/witch_huts/` and six selected processor lists under
`worldgen/processor_list/witch_huts/`. The common definition and variant roots are
preserved in family-decisions.json. The existing pool-traces-content.json.gz
structures entries resolve all six to one corresponding template each, with no
missing resources, unresolved entities, generation markers or spawner blocks.

Each pool has one rigid minecraft:single_pool_element and minecraft:empty fallback.
Each template authors a witch and cat. The root separately specifies piece-bounded
witch monster and cat creature spawn overrides, each weight1 and min/max1. These
are two source mechanisms, not proof of a generated count or natural-spawn rate.
No template loot-table reference exists. Entity drops are outside this structure
container-source claim.

All six processors replace red stained glass triggers and extend downward pillars:
birch uses stripped oak log; dark forest and taiga use dark oak log; oak uses oak
log; mangrove uses stripped mangrove log; giant tree taiga uses cracked stone
bricks. Preserve the birch material as authored rather than infer it from the name.
Giant tree taiga additionally replaces cobblestone with mossy cobblestone at its
configured probability0.75 and cracked bricks with mossy bricks at0.33. Its pillar
processor references the same list: generated replacement states no longer match
the red-glass trigger, so that nested pillar call returns unchanged before the
material rules. It is not unbounded pillar recursion or a new content family.

The already captured PillarProcessor in repurposed-monument-processors matches
full input block state, extends subject to terrain/build bounds and writes block
states. Its selected replacement materials are not spawners and its rule list
adds no loot or mobs. The source report details WorldGenRegion chunk bounds,
land checks, optional child processing and the difference between original block
and extension writes. No extra processor audit is required for this direct use.

GenericJigsawStructure and PieceLimitedJigsawManager are already captured in
repurposed-assembly. Common WORLD_SURFACE_WG projection, absolute offset0 and no
terrain adaptation support surface placement. Downward pillars can extend below
the 7x8x9 template envelope; existing size limitations explicitly exclude foundation
extent. Small roofed hut form supplies a qualitative visual cue, with terrain and
vegetation occlusion possible. No sightline, exposure guarantee or population
measurement is introduced.

The authoritative attributes link this report. Both existing code identity
manifests and the packaged template/source artifacts are hash-bound in the family
evidence map. A single family retains six variants; pools, templates and supports
are not additional families.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/repurposed-witch-hut-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Semantic comparison requires only witch_hut and input
identity to change. Source inspection supports the descriptive assessment; focused
tests validate existing integration and evidence boundaries, not Item 8 closure.
