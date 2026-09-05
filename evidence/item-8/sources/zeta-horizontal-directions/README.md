# Shared horizontal directions

Captured with extractor revision 6a1bf7c. identities.json binds the retained
Zeta archive, class and disassembly. Capture and identities reproduced byte
for byte before this README was added:

```sh
uv run -m tools.inspect_item8_pool_elements --archive Zeta-1.1-40.jar --class-name org/violetmoon/zeta/util/MiscUtil.class --output evidence/raw/item8/zeta-horizontal-6a1bf7c
```

MiscUtil's static initializer creates HORIZONTALS with four entries in order:
NORTH, SOUTH, WEST, EAST. No utility methods outside this initialization are
needed for the two current geometry questions.

The captured Nether spike generator iterates these four directions for each
middle-layer center. Its middle is a five-block cross inside a 3 by 3 square;
the base is a 3 by 3 square and the tip is one block wide. Therefore the direct
requested spike footprint is 3 by 3, not the 5 by 5 clearance volume. This does
not change the recorded vertical envelopes or establish an observed placement.

The captured FallenLogGenerator chooses an index into this array and passes
that index to createLog. Its side-direction table uses EAST/WEST at indices
zero and one, and NORTH/SOUTH at indices two and three. The optional side
decoration is consequently perpendicular to the log axis. With length three
or four, optional decoration extends one block beyond each end and one block
to either side: a source bounding rectangle of 5 by 3 or 6 by 3, rotated with
the log. This is a possible write envelope, not a fully occupied rectangle.
The previously recorded two-block vertical envelope is unchanged.

Scoped extractor Ruff and Basedpyright checks passed. No new measurement
system or server run was added. Do not repeat the array investigation.
