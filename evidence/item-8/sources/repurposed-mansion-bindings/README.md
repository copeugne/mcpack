# Mansion pool-name bindings

Captured at extractor revision 87f834b. All four verbose captures and identities
reproduced byte for byte before this README was added:

```sh
uv run -m tools.inspect_item8_pool_elements --archive repurposed_structures-7.5.21+1.21.1-neoforge.jar --class-name 'com/telepathicgrunt/repurposedstructures/world/structures/pieces/MansionPieces$LayoutGenerator.class' --class-name 'com/telepathicgrunt/repurposedstructures/world/structures/pieces/MansionPieces$FirstFloor.class' --class-name 'com/telepathicgrunt/repurposedstructures/world/structures/pieces/MansionPieces$SecondFloor.class' --class-name 'com/telepathicgrunt/repurposedstructures/world/structures/pieces/MansionPieces$ThirdFloor.class' --output evidence/raw/item8/repurposed-mansion-bindings-87f834b
```

This resolves the missing concatenation recipes in repurposed-mansion-layout.
The bootstrap constants and their operand order bind the namespace/prefix to
repurposed_structures:mansions/{mansionType}/. Floor room selectors append
first_floor, second_floor or third_floor and a room suffix. FirstFloor has
1x1, 1x1_secret, 1x2, 1x2_alternative, 1x2_secret, 2x2 and 2x2_secret room
selectors. Second and third floors additionally select _1x2_c_stairs or
_1x2_d_stairs when their boolean argument is true. These are component pool
selectors, not additional families or guaranteed rooms in every layout.

Layout bootstrap constants cover fixed roof, entrance, wall-corner and carpet
paths plus dynamic wall/door/carpet and corridor suffixes. Exact reachable pool
sets still require joining all call-site operands with selected mansion types;
the strings alone do not prove control-flow reachability or occurrence.

The child attachment path is custom: after reading a jigsaw's pool and checking
it, spawnChildPieces obtains that pool's fallback and weights its raw templates.
It selects from that fallback, requires a SinglePoolElement, then attempts
attachment using GeneralUtils.canJigsawsAttach. A generic recursive pool trace
must not be presented as this algorithm's exact selection behavior. Reconcile
this path and reuse the preserved MirroringSingleJigsawPiece before accepting
component/content coverage. Do not add an unrelated layout simulator.

Scoped extractor Ruff and Basedpyright passed. No new measurement or server run.
The original incomplete disassemblies remain preserved. Family attribution and
the Item 8 gate remain incomplete.
