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

## Candidate catalog reconciliation

The focused test binds 19 direct building/fitter candidate suffixes across the
four monument variants: 76 selected pools reference 88 distinct templates.
All candidate templates exist. Entries have positive weights and use single
pool elements; pool fallbacks are minecraft:empty. Processor references are
minecraft:empty plus desert_randomize, icy_randomize, jungle_randomize,
nether_randomize and nether_openings under repurposed_structures:monuments/.
Their effects remain to be reconciled before effective content attribution.

```sh
uv run pytest -q tests/item8/test_monument_components.py
```

The focused test and scoped Ruff/Basedpyright pass. This is candidate-resource
coverage, not complete graph reachability, assembly geometry, generation
success or an accepted family count. The packaged openings/wall_2 resources
are not included in the captured direct candidate suffixes. Their existence
does not establish an active call path or justify calling them unreachable.

## Packaged encounter and loot inputs

The candidate-template test now binds base entity IDs separately for each
variant. Desert/jungle contain skeleton, creeper, husk and guardian sources;
icy contains stray, vex and guardian; Nether contains wither skeleton, magma
cube and strider. These are component contents, not generated population counts.
All candidate block entities are chests, with the variant-specific monument
loot table. No candidate spawner block entities were found. This does not
exclude processors or other retained generation effects.

The processor test selects the five referenced nonempty lists and binds the
jungle surface processor's delegated append_loot rules to
repurposed_structures:archaeology/monument_jungle. All five chest/archaeology
table references resolve. The rules' execution and the custom pillar, surface,
noise, random-replacement and Y-position implementations are not yet attributed.
In particular, pillar configuration prevents assuming template height equals
the final occupied structure height. No new measurement was performed.

These inputs are integrated in the working monument decision. The initial
template test used a slash where the resource namespace requires a colon and
matched no documents; correcting the prefix exposed the intended selected set.
Ruff then rejected two long lines, which were split. Final validation: six
monument/inventory-source tests and scoped Ruff/Basedpyright passed.
