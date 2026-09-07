# IDAS existing geometry assessment

The38 remaining IDAS families were compared with the original world-bounds
catalog and23 original decoded Item8 captures, excluding restore copies.
Ten have full-chunk start candidates with boxes: ancient_portal,animal_den,
apothecary_abode,bearclaw_inn,desert_camp,pillager_fortress,ruins_of_the_deep,
sunken_ship,sunken_ship/sunken_ship_ruins,underground_camp. This is availability,
not acceptance of those bounds or their custody.

Four candidates beyond the six original catalog families, under evidence/raw/item8:

- apothecary_abode: integrated-stronghold-geometry-r1/chunks.jsonl line202.
- desert_camp: repurposed-mansion-monument-geometry-r1/chunks.jsonl line1945.
- pillager_fortress: illager-geometry-r1/chunks.jsonl line2151.
- ruins_of_the_deep: vanilla-final-geometry-r1/chunks.jsonl line2122.

Verify existing committed custody before integrating these candidates.

## Eight required size entries integrated

Four other families have independent single-template alternatives, not connected
assemblies. Their preserved pool definitions and template sizes supply nominal
design envelopes. Axis order below is x,y,z, in blocks.

- enchantingtower: blue,orange,red each11,26,11. Existing ModAdaptiveStructure
  evidence selects the default pool because ars_nouveau is absent.
- desert_market: ordinary,orange,red each17,16,17.
- lumber_camp: nine alternatives14,4,12; BYG redwood13,4,12.
- nexus: default/white57,21,57; blue/red57,22,57; prismarine58,21,57;
  sculk53,24,53. Six alternatives in one pool, not six assembled components.

22 templates total. Exact identifiers and dimensions are now family attributes.
Values directly project x/z and y from template_size_xyz in the hash-bound
pool-traces-content.json.gz and templates-redacted.json.gz. No component-size
aggregation or new measurement logic is needed. Rotation can exchange x and z;
terrain adaptation and occupied volume are excluded. Lumber camp's unresolved
biome eligibility is not silently resolved by its known packaged dimensions.

## Remaining geometry and defects

The other24 families are connected assemblies without candidates in these
sources. This is not24 new experiments: existing connector evidence may support
nominal assembled dimensions. Assess it before scheduling runtime work.
Ancient mines has a missing entrance2 pool; desert pyramid a missing villager
pool. These existing defects and lumber-camp biome constraints need dispositions.
The previous family rationales and preserved views retain substantial content
and connector evidence; do not repeat their discovery.

## Reproduction

Directly inspect named templates and pool definitions in the preserved catalogs.
Use the existing builder for the authoritative result:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-existing-geometry-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only these four families and input identity change.
An initial in-memory edit encountered missing attributes on lumber_camp and
stopped before file writes; the retry uses the existing optional-attributes form.
No runtime, renderer, validator or measurement system is added. Other required
attributes, final integration, acceptance and reviewed delivery remain open.
