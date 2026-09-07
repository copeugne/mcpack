# Repurposed End portal-ruin assessment

Nine remaining attributes are integrated using existing packaged and generator
sources. No fresh capture or new measurement tool is needed for this single-piece
design. Runtime dimension attribution was already integrated.

## Evidence and derivation

The selected root is data/repurposed_structures/worldgen/structure/ruined_portal_end.json.
Its start pool worldgen/template_pool/ruined_portals/end.json chooses one rigid
minecraft:single_pool_element: end_1 weight1 or end_2 weight3, with empty processors
and minecraft:empty fallback. Pool-traces-content resolves both templates with
no missing resources or unresolved elements. They have no jigsaw block in their
palettes, so there is no attached child-template assembly to measure.

In templates-redacted.json.gz, inspect these two resources:

| Template under data/repurposed_structures/structure/ | Size XYZ | SHA-256 |
| --- | --- | --- |
| ruined_portals/end_1.nbt | 14x23x17 | 31e9e0e78978009977fdee7f7b4101ee85327d93e9b03a956f11f8502d22a751 |
| ruined_portals/end_2.nbt | 9x16x11 | 33ef07f785c17d43fba6c76dbb16ae3438e951187206dd00fb8e4162ecac9dc2 |

These nominal envelopes include air/padding and rotate in X/Z. The existing
GenericJigsawStructure source under repurposed-assembly centers/translates placed
pieces during postLayoutAdjustments; burial translation does not alter template
dimensions. No occupied-volume, exposed-height or typical-world-size claim follows.

Both template entity lists are empty, with no generation markers, ordinary/trial
spawners or unresolved entity sources in the content trace. Root spawn overrides
are empty; ordinary biome spawning is possible. Neither empty processors nor the
single-piece layout adds an authored encounter. The large template contains lava,
which is an environmental hazard, not a mob source.

end_1 LootTable references repurposed_structures:chests/ruined_portals/end/large_portal;
end_2 references repurposed_structures:chests/ruined_portals/end/small_portal. Both
have packaged definitions under data/repurposed_structures/loot_table/. Pool weights
are selection inputs, not measured frequencies or reward probabilities.

Root burying_type AVERAGE_LAND, start offset-6, terrain radius check1 and minimum-Y
allowance45 support a terrain-associated partially buried ruin classification.
Terrain adaptation is none. These are placement inputs, not actual burial depth or
guaranteed exposure. Obsidian/crying obsidian, purpur, End stone and gold provide a
qualitative architectural cue; terrain can conceal the base. No sightline is
measured and frame blocks do not establish a functional travel route.

The authoritative family decision binds packaged JSON, template/content catalogs,
runtime sources and the existing repurposed-assembly identity manifest. Alternatives
remain two components of one family, not separate families.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/repurposed-end-portal-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Semantic comparison requires only this family and input
identity to change. Source inspection supports the descriptions; tests validate
the existing inventory/evidence boundaries rather than certify Item8 completion.
