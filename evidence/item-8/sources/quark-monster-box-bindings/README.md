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
