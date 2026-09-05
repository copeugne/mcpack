# Monument room and opening rules

Captured with extractor revision fce6a4a. All nine captures and identities
reproduced byte for byte before this README was added. Reproduce:

```sh
uv run -m tools.inspect_item8_pool_elements --archive repurposed_structures-7.5.21+1.21.1-neoforge.jar --class-name 'com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$FitDoubleXYRoom.class' --class-name 'com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$FitDoubleYZRoom.class' --class-name 'com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$FitDoubleZRoom.class' --class-name 'com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$FitDoubleXRoom.class' --class-name 'com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$FitDoubleYRoom.class' --class-name 'com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$FitSimpleTopRoom.class' --class-name 'com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$FitSimplePillarRoom.class' --class-name 'com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$FitSimpleRoom.class' --class-name 'com/telepathicgrunt/repurposedstructures/world/structures/pieces/MonumentPieces$MonumentRoomFitter.class' --output evidence/raw/item8/repurposed-monument-rooms-r1
```

The initial handoff called createOpenings a default implementation. Inspection
contradicts that premise: MonumentRoomFitter declares three abstract methods.
Each concrete fitter supplies its own room and opening logic.

Verbose recipes bind room suffixes double_x, double_xy, double_y, double_yz,
double_z, simple_pillar, simple and simple_top under
repurposed_structures:monuments/{monument_type}/rooms/. The create methods pass
the monument type into these recipes and delegate the selected name to
MonumentPieces.getJigsawPiece. Their claimed graph cells differ by room shape.
Opening recipes add wall_3, arch and wall_shelf to the already captured wall_1,
entrance_wall and floor possibilities. The selected graph and fitter determine
which openings are requested; the recipe set is not an observed layout.

Next: reconcile the direct building and fitter pool candidates against all four
selected monument types, then their template contents and processors. Room
fitters, graph cells and opening pieces are components, not families. Do not
substitute recursive jigsaw traversal for these direct custom calls or infer
successful placement from the presence of packaged resources. Scoped extractor
Ruff and Basedpyright passed. No new world measurement or acceptance claim.
