# Monster Box callback bindings

Verbose captures at `0b8d3d5`, with exact identities in identities.json. Ordinary
captures remain preserved under quark-monster-box-behavior and reproduce using
their recorded extractor revision. This additional output is needed for actual
bootstrap targets and annotations, which ordinary javap omitted. Reproduction
matched all four captures and identities byte for byte:

```sh
uv run -m tools.inspect_item8_pool_elements --archive Quark-4.1-480.jar --class-name org/violetmoon/quark/content/world/module/MonsterBoxModule.class --class-name org/violetmoon/quark/content/world/block/MonsterBoxBlock.class --class-name org/violetmoon/quark/content/world/block/be/MonsterBoxBlockEntity.class --class-name org/violetmoon/quark/mixin/mixins/accessor/AccessorLivingEntity.class --output evidence/raw/item8/quark-monster-box-bindings-0b8d3d5
```

MonsterBoxBlock.getTicker passes a callback whose bootstrap target is
MonsterBoxBlockEntity.tick. The block-entity spawnMobs consumer's bootstrap target
is lambda$spawnMobs$0, the already interpreted spawn-egg consumer. Module block
entity registration binds the MonsterBoxBlockEntity constructor. The module's
onDrops method has the Zeta PlayEvent annotation. This proves source bindings,
not an observed trigger or death event.

AccessorLivingEntity is a mixin targeting LivingEntity. Its accessors explicitly
target lastHurtByPlayer and lastHurtByPlayerTime. Thus the captured onDrops check
requires a positive value of the actual lastHurtByPlayerTime field. The preserved
registry-r1 debug log confirms this accessor mixin was applied at line 9911.
The log is retained by existing custody, with SHA-256
e5b47378d791027242ba28dd36c999c07ae4e01a1b90e1534e66bcd42c1e694b.

```sh
sha256sum evidence/raw/item8/custody-r1/restored-download/debug.log
sed -n '9911p' evidence/raw/item8/custody-r1/restored-download/debug.log
```

These resolve the ticker/consumer identity and accessor-target gaps from the
prior interpretation. Effective module enablement, configuration mapping and
world attribution remain open. Do not repeat the spawn-table extraction or
broaden this into unrelated living-entity internals. Scoped extractor checks
passed; no runtime or measurement system was added.

## Frozen setting attribution

The module's captured category annotation is world. The retained debug log at
line 13897 records construction under display name Monster Box. The already
captured TentativeModule and ZetaModuleManager naming/assignment path therefore
maps it to world.monster_box. Its chancePerChunk, minY, maxY, minMobCount,
maxMobCount, dimensions, enableExtraLootTable, activationRange and searchRange
fields all have Config annotations. The shared ConfigObjectMapper maps their
names and nested dimensions to the corresponding frozen settings.

The loaded-file identity and initial-refresh execution are already established
in zeta-module-section and zeta-config-event-fields. Reusing that evidence gives
the following initial settings: chancePerChunk 0.2, minY -50, maxY 0, minMobCount
5, maxMobCount 8, enableExtraLootTable true, activationRange 2.5, searchRange 15,
and an Overworld dimension allowlist. The module toggle is true in the frozen
world section; this value alone does not establish category/overlap enablement.

The direct generation code has no biome filter. Its terrain/support predicate
and flat-world rejection still apply. Initial candidate Y is in [-50,0), and
the search checks at most 15 positions while remaining strictly above -50.
Each qualifying placement writes one block. At chance 0.2 the loop permits at
most one placement attempt per chunk; this is not an observed density claim.

For an active ticking box outside Peaceful, the captured block-entity code
starts on non-spectator player distance strictly below 2.5 blocks. At uninterrupted
ticks the action occurs on the 41st active tick. This is a tick count, not a
wall-clock timing claim. The source requests five through eight spawn-table
draws under these settings, not five through eight guaranteed successful mobs.

These are source/configuration/log-derived initial values, not a direct field
dump. Recheck the preserved evidence without rerunning a server:

```sh
sed -n '13897p' evidence/raw/item8/custody-r1/restored-download/debug.log
sed -n '1147,1162p' evidence/item-6/frozen/config/quark-common.toml
cmp evidence/raw/item8/custody-r1/restored-download/configuration/config/quark-common.toml evidence/item-6/frozen/config/quark-common.toml
```

No additional source capture is needed for these field mappings. Remaining
work is effective module enablement, family disposition/integration and world
attribution, alongside broader provider coverage.
