# Crashed-ship erosion attribution

The existing extractor gained one class selection because CrashedShipFeature
calls erodeIntense after template placement. The previous capture did not include
that callee, so it could not justify attributing the complete direct path or
bounding debris by the template. No new tool or runtime experiment was added.

```sh
uv run -m tools.inspect_item8_pool_elements --archive bclib-21.0.24.jar --class-name org/betterx/bclib/util/StructureErode.class --output evidence/raw/item8/crashed-ship-erosion-r1
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-crashed-ship-descriptions.json
uv run pytest -q tests/item8/test_betterend_feature_candidates.py
uv run ruff check tools/build_item8_inventory.py tools/inspect_item8_pool_elements.py
uv run basedpyright tools/build_item8_inventory.py tools/inspect_item8_pool_elements.py
```

identities.json binds the frozen archive/member and captured disassembly.
erodeIntense scans the intersected box and calls ignore, then probabilistically
removes or relocates eligible block states. Relocation uses independent Gaussian
X/Z offsets without an explicit horizontal clamp; its downward search limit is
box.minY()-10. drop builds terrain-connected sets inside the box and may lower
unconnected states. These paths write block states, not mobs or loot tables;
they do not preserve complete container NBT as a separate relocation operation.
No exact surviving population, inventory or occupied debris bounds are inferred.

The authoritative crashed-ship attributes preserve the 13x24x29 nominal vanilla
hull, negative height-derived placement offset, actual X-only distance predicate,
ignored entities and structure markers, replacer behavior and erosion limits.
The selected template has no entities, physical spawners or LootTable fields.
Its two empty chest compounds and two fixed strong-healing potions are distinct
from marker-generated chest tables and the ignored Elytra/Sentry markers.
See betterend-feature-scope, betterend-remaining-features and the template catalog
for these existing inputs. No EndCityPiece marker handler is called here.

The eight required answers are integrated in the same increment as this capture.
Nominal hull geometry satisfies approximate description without inventing a
finite bound on Gaussian debris or requiring a new world-size measurement.
