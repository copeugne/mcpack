# Trial-chamber alias replacement

The current pool trace uses the structure definition's original aliases, but
the retained catalog contains `lithostitched:set_trial_chambers_pool_aliases`
with `append=false`. Its melee tag also has a Regions Unexplored contribution.
This is a demonstrated content omission, requiring a correction to the existing
trace rather than another measurement system.

Reproduction with tool `484ff42`, into an absent output directory:

```sh
uv run -m tools.inspect_item8_pool_elements --archive lithostitched-1.7.10+beta4-neoforge-21.1.jar --class-name dev/worldgen/lithostitched/worldgen/modifier/SetPoolAliasesModifier.class --class-name dev/worldgen/lithostitched/worldgen/poolalias/RandomEntries.class --class-name dev/worldgen/lithostitched/mixin/common/PoolAliasLookupMixin.class --class-name dev/worldgen/lithostitched/worldgen/modifier/internal/CompileRawTemplatesModifier.class --output evidence/item-8/sources/lithostitched-alias-code
```

This command succeeded. The four outputs match the corresponding classes in
the initial broader extraction, preserved locally under
`evidence/raw/item8/lithostitched-alias-code`. The exact-class option avoids
committing duplicate disassemblies or revising unrelated evidence identities.
Scoped Ruff and basedpyright passed. No binary is committed.

`SetPoolAliasesModifier.applyModifier` replaces a vanilla JigsawStructure's
alias list when append is false. It appends the prior aliases only when true.
It also handles delegating and alternate jigsaw structures, which are not
needed to establish this vanilla trial-chamber replacement.

`RandomEntries.forEachResolved` draws one index bounded by the first holder
set's size and uses that same index across its aliases and holder sets.
Its `allTargets` returns an empty stream, so that method alone cannot be used
as evidence that the aliases have no possible targets. The lookup mixin uses
`buildKeepingLast` for duplicate alias keys.

The retained packaged JSON catalog contains the replacement and its four pool
tags under `data/lithostitched/tags/worldgen/template_pool/trial_spawner/`.
Regions Unexplored appends `regions_unexplored:trial_chambers/ashen` to the melee
tag. Ranged and slow-ranged tags each contain skeleton, stray and poison-skeleton
variants; melee also includes zombie, husk and spider; small melee includes
slime, cave spider, silverfish and baby zombie. Preserve tag source identities,
the replacement document and the shared-index relationship. A union of possible
targets does not establish their joint spawn frequency or actual encounter mix.

`CompileRawTemplatesModifier` runs at priority 2147483647 and invokes each pool's
`compileRawTemplates` method. The method's implementation remains to inspect
before claiming the modifier has no other effect.

The alias correction, merged tag evidence and affected regression are still
outstanding. The current accepted trace and working inventory are unchanged
by this source-inspection increment. Item 8 remains incomplete.

## Trace correction

Decoder/tag merge implementation is `749c1a2`; trace integration is `f4efdcc`.
The existing biome-tag merge was renamed `tag_inputs` and given a resource-kind
argument, serving both current consumers without a parallel tag implementation.
Unsupported tag forms, competing replacements and incompatible holder-set sizes
fail explicitly. This implementation supports the observed replacement shape;
it does not generalize to unobserved modifier stacks.

Executed commands:

```sh
uv run -m tools.trace_item8_structure_pools --output evidence/raw/item8/pool-traces-alias-pilot.json.gz
uv run -m tools.trace_item8_structure_pools --output evidence/raw/item8/pool-traces-alias-reproduction.json.gz
cmp evidence/raw/item8/pool-traces-alias-pilot.json.gz evidence/raw/item8/pool-traces-alias-reproduction.json.gz
uv run pytest -q tests/item8/test_pool_links.py tests/item8/test_pool_trace.py tests/item8/test_biome_tag_inputs.py
```

The two traces matched byte-for-byte. All 22 affected tests passed, including
the extended frozen-output regression proving ashen template reachability and
both normal and ominous spawner entity IDs. Scoped Ruff and basedpyright passed.
Trace SHA-256:
`b78541655c69fbc3599a670ccc424d60dd08cbb642bd796a9b69bcb9c1f223d9`.

The trace retains original aliases, the replacement document and its identity,
and the merged tag inputs with all contributing source identities. Its target
sets are possible content, not evidence of runtime tag order or encounter
probabilities. The modifier report now includes one alias replacement and
retains 37 other selected modifier types as untraced. Trial chambers remain one
working family. Decision references are updated to the new trace hash; the
trial-chamber rationale now records this replacement and its ashen contribution.
Other modifier types and Item 8 closure remain outstanding.

The three affected family checks passed (55 unrelated cases deselected), and
the existing structure/biome source output reproduced byte-for-byte:

```sh
uv run pytest -q tests/item8/test_family_decisions.py -k 'minecraft or better_village or all_runtime'
uv run -m tools.build_item8_structure_inputs --output evidence/raw/item8/structure-inputs-tag-refactor.json
cmp evidence/item-8/sources/structure-inputs.json evidence/raw/item8/structure-inputs-tag-refactor.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-trial-aliases.json
```

The inventory was regenerated from delivered inputs at `48df0e9`. Apart from
required source-hash substitutions, only the trial-chamber family changed.
It now carries the ashen template's explicit normal/ominous spawner sources and
loot references. Other spawner configuration references still need resolution;
this is not a complete effective encounter inventory.

Decision SHA-256:
`3fc8ed59195ee040f746b9aeef957d1d4a72293016bab2a13b5e5b37eda518bc`.
Inventory SHA-256:
`d5b51f2f140e2d88bf77d9f3dac5168f0b4dfacd827ae9cf1908d42abbf4d369`.
