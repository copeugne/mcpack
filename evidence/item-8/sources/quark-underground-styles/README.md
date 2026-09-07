# Quark underground contributions

Captured at extractor revision 5898af6. identities.json binds four disassemblies
to the retained Quark archive. All four captures and identities reproduced byte
for byte before this README was added:

```sh
uv run -m tools.inspect_item8_pool_elements --archive Quark-4.1-480.jar --class-name org/violetmoon/quark/content/world/module/CorundumModule.class --class-name org/violetmoon/quark/content/world/module/PermafrostModule.class --class-name org/violetmoon/quark/content/world/undergroundstyle/CorundumStyle.class --class-name org/violetmoon/quark/content/world/undergroundstyle/PermafrostStyle.class --output evidence/raw/item8/quark-underground-5898af6
```

Both module setup methods register UndergroundStyleGenerator through Zeta at
UNDERGROUND_DECORATION, weight one. Each supplies its generationSettings and a
style name, corundum or permafrost. This is a direct generation contribution
outside registered structure roots. It must receive a coverage disposition;
module names alone cannot determine whether it constitutes a family.

PermafrostStyle extends BasicUndergroundStyle. Its constructor supplies packed
ice states and true to the base constructor. setBlock replaces floorState and
ceilingState. Its fillFloor first invokes the base implementation, then draws
against 0.015. A successful draw attempts a pillar three through five blocks
above the supplied floor, stopping at the first non-air block. Each placed
pillar block uses floorState, with write flag two and discarded write result.
This describes decoration of supplied floor positions, not the complete spatial
extent or applicability of the delegated generator.

CorundumStyle also extends BasicUndergroundStyle. Its fillFloor and fillCeiling
use the source-position color data, draw against crystalChance, and delegate
crystal placement upward or downward respectively. The captured helpers contain
crystal and cluster block placement, including facing and waterlogged state.
The shared cave-generation path and inherited base-style behavior remain
unresolved. No final terrain-only exclusion, family count, successful placement
or effective configuration claim is made from these leaf implementations.

Next inspect UndergroundStyleGenerator and BasicUndergroundStyle, reusing this
capture for their two consumers. That direct dependency determines whether the
styles create distinct sites or decorate terrain. Do not expand into unrelated
Corundum crafting or piston behavior. Scoped extractor Ruff and Basedpyright
checks passed; no new measurement system or server run was added.
