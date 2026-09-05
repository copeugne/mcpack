# Better Village contribution inspection

Reproduction command using the existing tool at `cd2d54f`, with an absent output
directory:

```sh
uv run -m tools.inspect_item8_pool_elements --archive bettervillage-neoforge-1.21.1-3.3.1.jar --output evidence/item-8/sources/bettervillage-code
```

The command succeeded. All seven classes in the retained provider were inspected;
their archive, member and disassembly identities are in `identities.json`.
Scoped Ruff and basedpyright passed for the tool. Whole-class output preserves
the methods and mixin annotations needed to review the behavior without a
second extraction format or measurement system.

`Main.VILLAGE_WHITELIST_REPLACEMENT` contains the five vanilla village IDs.
`StructureSetMixin` checks enabled custom configuration and whether any entry
belongs to that set. It then substitutes `Main.STRUCTURE_CONFIG` when returning
placement. `Config` binds enabled=true, spacing=45, separation=20 and
salt=10387312, matching `evidence/item-6/frozen/config/bettervillage_1.properties`.
`Main` constructs a LINEAR random-spread placement. This hook does not add a
structure family or alter the biome constraints in the structure definitions.
The hash-bound captured debug log at `evidence/raw/item8/registry-r1/debug.log`
records activation on line 18029. This does not claim measured encounter pacing
or rule out other mods' later placement changes.

The compatibility path reads `bettervillage_compat` resources. Its processor
calls `CompatMetaData.requireApplyCompat`, which requires both loaded target mod
and enabled metadata. The retained catalog contains four such resources, all
disabled, for Bountiful, Ice and Fire, Immersive Engineering and More Villagers.
Their target IDs are absent from the captured Mod List. Their pool replacement
paths therefore contribute no extra content in this frozen stack. A new general
compatibility simulator would not close a current evidence gap.

`AbstractDecorationEntityMixin` changes an error-level log operation to debug
while reading decoration data. It does not add enemies, loot or structure roots.
Preserve this logging limitation when interpreting the absence of error logs.

Template replacements are already selected through the retained resource
catalog and pool trace, using vanilla template IDs. Their source identity must
be attributed to Better Village within the existing village family, rather
than counted as new registered families. The family regression records the
reachable templates and the packaged templates absent from current reachability.
Other village contributors and incomplete Item 8 attributes remain open.

## Family attribution

Decision and regression implementation: `9595c52`. Validation commands:

```sh
uv run pytest -q tests/item8/test_family_decisions.py -k better_village
uv run ruff check tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-bettervillage.json
```

The focused test passed (57 unrelated cases deselected), and both quality checks
passed after correcting JSON type annotations and line lengths. The test binds
all village evidence hashes and verifies 246 packaged replacements, 244 selected
reachable replacements, the exact two unreachable snowy-street templates,
disabled/absent compatibility targets, frozen config and the activation log.
No Better Village family was introduced. Only the existing vanilla village
record changed in the generated inventory, apart from the top-level decision
input hash. The working inventory remains incomplete.

Decision SHA-256:
`ac85610fd8f09a8fd4c35cbecfe924ce1e8c01313fa64587000da6d5cd7e50e3`.
Inventory SHA-256:
`f8f649f13b19f4ed97f3c234be1346298239dc9ebc977f6eacb3ef2c1f9171ed`.
