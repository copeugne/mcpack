# Vanilla End platform caller

Extractor revision: `159dc4da259d94ddb5d3e6ffb92e231e17001c72`.
The identity manifest records the pinned archive, exact class and disassembly
hashes. This exact class closes the missing link between the packaged
end_platform feature and the captured Better End Island static-method hook.

Reproduce into a fresh directory:

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive server-1.21.1-20240808.144430-srg.jar \
  --class-name net/minecraft/world/level/levelgen/feature/EndPlatformFeature.class \
  --output evidence/raw/item8/vanilla-end-platform-159dc4d-reproduction
diff -r --exclude=README.md evidence/item-8/sources/vanilla-end-platform-caller \
  evidence/raw/item8/vanilla-end-platform-159dc4d-reproduction
```

The fresh reproduction matched exactly before this README was added. Scoped
Ruff and Basedpyright passed after correcting the selection's line wrapping.

Manual disassembly inspection: place(context) passes context.level(),
context.origin() and false to createEndPlatform, then returns true. It performs
no additional biome or dimension check. This establishes the direct call into
the static method targeted by the already captured cancellable mixin. The frozen
false vanilla-platform toggle selects the custom placement through that hook.
The unconditional true return is not evidence of successful template placement.

For the packaged fixed origin (100,49,0), the custom generator's down-14 and
half-X/Z offsets give nominal template origin (97,35,-3). The 7x22x7 envelope
therefore spans X=97..103, Y=35..56, Z=-3..3, including air. This is a derivation
from the packaged placement, this caller, the captured mixin/generator and
template dimensions. It is not a saved-world occupied-block measurement, and
other callers may supply a different origin or destroyBlocks value.
