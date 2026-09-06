# Nether landmark and well comparisons

Renderer b6514372 selects fourteen templates from the hash-verified retained
MoogsNetherStructures-1.21-3.0.0-alpha.2.jar archive. Seven landmarks and seven
existing well and circular-ruin components provide the remaining Nether design
comparisons. Both sheets were manually inspected and independently reproduced
byte for byte. The selected-path pilot succeeded. Scoped Ruff and Basedpyright
pass.

```sh
uv run -m tools.view_item8_betterend_ruins --nether-landmarks --output evidence/raw/item8/nether-landmark-views-r1
```

The existing cube projection omits occluded cells and rescales each template
separately. It does not render partial block models, hidden interiors or actual
generated-world placement. Lower well templates are components, not additional
families. The last circular-ruin projection approaches the sheet edge. Use the
preserved template contents and pool traces for membership and contents; these
views support layout comparisons, not dimension measurements.

Compressed SHA-256 identities:

- landmarks.svg.gz: 41da851782f11d2d95850c402c327eca034c52052f2e19a03abf20a68ce9679d
- well_ruin_comparison.svg.gz: 3694f4b4ae53c9ec16dd3de3b0742bce94199c3c5dea6da18a69735aa03d10c2
