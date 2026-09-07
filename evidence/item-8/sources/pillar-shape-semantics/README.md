# Ruined pillar shape semantics

Two additional selections in the existing extractor resolve the height convention
and rotation used by the retained pillar writers. They are necessary to avoid
mistaking a half-height for total height or the name fallen_pillar for horizontal
orientation. No new tool, runtime measurement or geometry framework was added.

```sh
uv run -m tools.inspect_item8_pool_elements --archive bclib-21.0.24.jar --class-name org/betterx/bclib/sdf/primitive/SDFCappedCone.class --class-name org/betterx/bclib/sdf/operator/SDFRotation.class --output evidence/raw/item8/pillar-shape-semantics-r1
uv run pytest -q tests/item8/test_betterend_feature_candidates.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-pillar-descriptions.json
uv run ruff check tools/build_item8_inventory.py tools/inspect_item8_pool_elements.py
uv run basedpyright tools/build_item8_inventory.py tools/inspect_item8_pool_elements.py
```

identities.json binds the exact archive, classes and disassemblies. CappedCone
uses abs(y)-height and twice-height in its distance calculation. Equal radii
therefore define a centered parent cylinder with total axial length twice the
setHeight parameter. The two writers pass L/2, with nominal L ranges 20..40 and
10..35 and radii 2..4 and 2..5 respectively. SDFRotation sets an angle-axis
quaternion and rotates the sampled coordinates before evaluating the source.

For an unweathered parent cylinder, a horizontal-axis tilt theta gives vertical
span L*abs(cos(theta))+2*r*abs(sin(theta)), span along the horizontal tilt direction
L*abs(sin(theta))+2*r*abs(cos(theta)), and transverse span 2*r. These are elementary
projections of its axial and circular sections, not measured voxel extents.
FallenPillar uses pi+0.05*nextGaussian(); do not assert a horizontal orientation.
Basement's final tilt is 0.2*nextFloat(); its rotated/displaced cutting plane is
separate. Translation affects position, not these parent spans.

Both original writers and supplied callbacks are in betterend-pillar-end-hooks.
They write obsidian/mossy-obsidian material and define no mob, physical spawner
or container-loot source. Source-supplied material attribution is distinct from
natural spawning, harvest rewards and observed safe terrain. Geometry retains
weathering, subtraction, replacement and voxelization limitations. Eight answers
were integrated into the authoritative family and inventory in this increment.
