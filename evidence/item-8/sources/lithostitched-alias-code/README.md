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
