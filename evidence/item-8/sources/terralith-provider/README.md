# Terralith provider entry boundaries

Selector 21eac3c captures all eleven classes from the frozen Terralith archive.
The second capture reproduced exactly before this README was added.
Archive SHA-256: d38bd304897731b42f6c013cdc07e082e74411e80c74aabcee385251beb3b546.
Identity manifest SHA-256:
cf0cdfa21a06651e123ae119eadc733c62cc9457fc1131311aac614d5148b1c9.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive Terralith_1.21.1_v2.6.2_Neoforge.jar \
  --output evidence/raw/item8/terralith-provider-r1
```

TerralithNeoforge loads ConfigHandler from the loader configuration directory
and attaches RegisterEvent. Its callback registers only the terralith:config
condition codec. TerralithNeoforgeClient installs the configuration screen.
The remaining classes implement configuration state, serialization, the screen
and list entries, identifiers and logging. These classes do not implement a
separate authored generator. The declared mixin list is empty.

ConfigResourceCondition.test returns config.test(key) != invert. The codec's
default invert is false. ConfigState delegates keys to its Modules record;
ConfigHandler loads and saves that state. The packaged NeoForge overlays use
this condition. Their disposition must use the frozen configuration rather
than assuming that all packaged overlay resources are active.

This capture closes the executable entry inspection, not the complete provider
row. Packaged roots, disconnected components, features, functions and overlays
still require their data reconciliation. Preserve that distinction until the
provider scope check is delivered.

## Six single-template family assessments

Forty-five attributes finish Desert Outpost, Igloo, Witch Hut, Frosted Dungeon,
Old Refinery and Sunken Tower. Seven registry roots select six unique templates;
Witch Hut's two roots share one template. Existing source geometry is preserved.
Exact source identities and per-template refs are integrated in family-decisions.
All selected pools use empty processors; templates have no jigsaw attachments.

Desert Outpost has no saved enemies or spawners; its full-bounds override permits
natural single pillagers. Its source includes terralith:desert_outpost container
loot and vanilla desert_well/desert_pyramid archaeology tables. Igloo saves a
snow-type fox, Health 10 and PersistenceRequired 0, and terralith:igloo loot.
It does not select a vanilla-style basement encounter.

Frosted Dungeon's underground/dungeon1 block_entities 3 is an ordinary stray
spawner (delay 200..800, nearby 6, count 4, range 4, player range 16).
No other selected template has spawners. Old Refinery and Sunken Tower have no
saved entities, spawners or natural spawn overrides beyond the ordinary world.
Their industrial/tower forms do not prove machinery or an authored encounter.
All three underground roots use absolute uniform start Y -40..40, beard_box,
ignore_waterlogging and no surface projection. The surface_structures step
label is not evidence of surface placement. Loot refs use terralith:underground/chest.

Witch Hut saves two minecraft:item entities containing moss_carpet, each with
Age2229. It does not save witches/cats. Its active regular root configures
piece-bounded natural witches (group1..2) and cats (group1). The underground-ID
root also declares surface projection but uses the empty has_structure/none
biome tag and empty spawn overrides. Preserve that ineligible variant rather
than inferring underground placement or additional family identity from its ID.
Both select terralith:witch_hut loot. Saved item lifetime is not guaranteed loot.

Runtime biome intersections are Overworld except the ineligible Witch Hut root.
No direct retained starts are asserted. Visibility is qualitative template and
placement inference; no exposed-height, sight-distance or pacing measurement.
No nonempty fixed Items/item container payload occurs in these six templates.

Rebuild: `uv run -m tools.build_item8_inventory --output <absent-path>`.
Validation: `uv run pytest -q tests/item8/test_terralith_provider_scope.py tests/item8/test_inventory_sources.py`.
Seven tests pass. Semantic comparison changes only these six families and the
decisions pin; existing geometry, identities, biomes and observations remain
unchanged. Inventory SHA-256:
`9d18d1d522871d0f25c2e95a0e392ba858f167147746098416830fecbc5274ea`.
