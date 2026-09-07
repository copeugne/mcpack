# Remaining-provider dimension integration

This increment integrates 54 existing dimension assessments: all 17 remaining
Repurposed Structures families and 37 of the 38 remaining IDAS families. It uses
the existing builder's biome overlap and observed-dimension fields, without a new
measurement, capture or inference from names. Lumber camp is excluded because
three variant biome constraints remain unresolved.

## Evidence and limits

`tools/build_item8_inventory.py` computes biome_compatible_by_structure from
`sources/structure-inputs.json` resolved biome sets and
`runtime/dimension-r3/dimension-biomes.json` captured dimension membership. It
rejects unresolved constraints as UNKNOWN rather than treating them as empty.
The observed field separately lists dimensions of retained starts in
`sources/world-bounds.json.gz`. These three source identities are bound in each
updated family decision. A start observation is not a guarantee of placement in
every eligible dimension, completed population, or a density measurement.

All 54 integrated mappings contain resolved lists. The empty list for
idas:desert_camp/desert_camp_bygwindswept means no overlap with the captured
possible-biome sets. It is not evidence of a failed generation attempt. Other
members of its family have their own preserved dimension mappings.

The unresolved lumber-camp variants are:

- idas:lumber_camp/lumber_camp_bopmahogany
- idas:lumber_camp/lumber_camp_bygmahogany
- idas:lumber_camp/lumber_camp_bygredwood

Their unresolved strings and family assessment remain unchanged. Resolving their
biome references is required before accepting that family's dimension entry.
This does not create a backlog of optional measurements.

The authoritative integration copies the established maps and observed lists into
the family decision attributes. Semantic comparison confirms those maps/lists
are unchanged and that only the 54 dimension assessments, grouping evidence and
input identity change. Other attributes still need their own assessment.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/remaining-provider-dimensions-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. No code behavior changes beyond the decisions hash pin.
Item 8 remains open pending the remaining attributes, canonical integration,
acceptance and reviewed delivery.
