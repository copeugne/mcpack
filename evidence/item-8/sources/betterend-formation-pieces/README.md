# BetterEnd formation piece sources

These six classes extend the existing Item 8 source extraction to the pieces
instantiated by the already preserved lake and mountain generators. Packaged
definitions and template traces do not expose their procedural geometry or
content. This source set supports the required footprint, vertical size and
content attributes without another runtime experiment or measurement system.

Retained archive: `BetterEnd-21.0.31.jar`, SHA-256
`dd883e2f91fa7ee8a0594dc3844de38bf3e550d91ff1247b2801808904fd013a`.
Identity manifest SHA-256:
`2ecc0877f072bee316254a4e5df4395c43e24802d923a29bd83c19c8a7718f39`.
The manifest binds each class and disassembly to that archive.

Reproduce with the frozen inputs into a fresh output directory:

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive BetterEnd-21.0.31.jar \
  --output evidence/raw/item8/betterend-formation-pieces-reproduction \
  --class-name org/betterx/betterend/world/structures/piece/BasePiece.class \
  --class-name org/betterx/betterend/world/structures/piece/EndLakePiece.class \
  --class-name org/betterx/betterend/world/structures/piece/LakePiece.class \
  --class-name org/betterx/betterend/world/structures/piece/MountainPiece.class \
  --class-name org/betterx/betterend/world/structures/piece/CrystalMountainPiece.class \
  --class-name org/betterx/betterend/world/structures/piece/PaintedMountainPiece.class
cmp evidence/item-8/sources/betterend-formation-pieces/identities.json evidence/raw/item8/betterend-formation-pieces-reproduction/identities.json
uv run ruff check tools/inspect_item8_pool_elements.py
uv run basedpyright tools/inspect_item8_pool_elements.py
```

Initial extraction and fresh reproduction succeeded. Their identity manifests
match byte-for-byte, including all six disassembly hashes. Scoped Ruff and
Basedpyright passed for the extractor change.

Initial inspection: MountainPiece stores separate radius and height parameters,
but makeBoundingBox uses radius for all three axes, including Y. Consequently,
the saved piece envelope must not be presented as measured occupied mountain
height. Content inspection and inventory attribute integration remain pending.
This capture does not establish absence of indirect content, final geometry,
observed discoverability, or Item 8 completion.

## Lake geometry and dimension assessment

This increment integrates eleven existing facts: dimension eligibility for all
nine BetterEnd families and the lake family's two size attributes. The effective
root biome sets in structure-inputs.json intersect only minecraft:the_end in the
captured dimension-r3/dimension-biomes.json. Eligibility is not generation success.
The lake family now has all required Item8 attributes; the other eight BetterEnd
families still need assessment. No new capture or measurement tool is needed.

The preserved world-bounds.json.gz contains three full-start lake observations:

| Root | Seed | Decoded source and line | Chunk | Saved size X,Y,Z |
| --- | --- | --- | --- | --- |
| end_lake_normal | 42 | run-a/ordinary/chunks.jsonl:6419 | 90,4 | 57,44,57 |
| end_lake_rare | -3503646078644842058 | run-a/biome-diverse/chunks.jsonl:7809 | 98,4 | 75,45,75 |
| end_lake_rare | -3503646078644842058 | run-b/biome-diverse/chunks.jsonl:7441 | 108,-10 | 77,46,77 |

These are three distinct observed starts, not repeated measurements of one
identical layout. Preserve their different positions and dimensions across runs.
The exact envelopes and identities are integrated in family-decisions.json.
Inclusive envelope subtraction is performed by the existing observed_bounds
implementation; the world-bounds artifact and underlying Item7 custody remain
the evidence source. No new runtime or archive is introduced.

EndLakePiece.makeBoundingBox uses floor(1.5 * radius), with ten blocks of additional
margin on each side horizontally. Its lower Y is waterLevel minus floor(depth)
minus twelve, and upper Y is centerY plus22. The saved vertical span consequently
includes support and clearance, not just water depth. These explicitly labelled
generation envelopes provide approximate examples for this procedural family;
they are not occupied volumes, typical dimensions, or all-variant maxima.
No full-start megalake example is present in this set. That limitation does not
turn variant sampling or a water-depth measurement into additional Item8 work.

The source inspection and exact class identities above explain the envelope's
meaning. The mountain family must retain its separate warning: MountainPiece
uses radius on Y, so a cubic saved box must not be described as occupied mountain
height. Its two size attributes remain open after this increment.

## Mountain geometry assessment

The two mountain size attributes use the existing generator/piece sources and
six full-start saved envelopes. This resolves their approximate scale without
a new world capture or an occupied-block measurement implementation.

Both root generators select integer radius R with randRange(50,100). Crystal
mountain selects height parameter H=R*randRange(0.8,1.2); painted mountain uses
H=R*randRange(0.4,0.6). Thus the nominal terrain-body diameter is100 to200 blocks,
with nominal height scales40 to120 and20 to60 respectively. These are parameter
scales, not attained heights or probability distributions of actual mountain size.

Direct inspection of bclib-21.0.24.jar, SHA-256
a7efd02dd3409dbac9c8455c5ed4fa4ca340e2af1c39f211038198dfa1c92093,
member org/betterx/bclib/util/MHelper.class, SHA-256
2367076b2f831616da7540e03fc3fa09255c178faec1b6ecea4fcf1577e41423,
establishes randRange(int,int,RandomSource) as min+nextInt(max-min+1).
The float overload computes min+nextFloat()*(max-min), with Java float rounding.
These endpoints are not described as strict floating-point extrema.

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c -classpath downloads/item3/candidates/bclib-21.0.24.jar org.betterx.bclib.util.MHelper
```

For a column at squared horizontal distance D2<R*R from center C, the painted
piece computes a radial factor F=1-D2/(R*R). Crystal placeMountain instead uses
F=1-(D2/(R*R))^0.3. Let N05 and N10 be noise1 evaluated at horizontal coordinate
scales0.05 and0.1. Let K be getHeightClamp with radius10 for painted or12 for
crystal. The helper computes a weighted local support-height average, divides
by that sampling radius, then clamps to[0,1]. The intended column top T is:

- Painted: C.y + F*H*K*(0.7+0.3*N05)*(0.9+0.1*N10).
- Crystal body: C.y + F*H*K*(0.7+0.3*N05)*(0.8+0.1*N10).

The code retains terrain support only above C.y-8. It writes from supportY-1,
with painted integer Y<T and crystal integer Y<int(T), where int is Java's
float-to-int conversion. Terrain sampling, noise and integer endpoints determine
the realized relief; neither H nor the saved vertical span is that relief.

Crystal decoration follows body placement and uses current surface height h.
Two candidate loops choose lateral radius r=2..3 or1..2, with centers constrained
to[r,15-r] in each processed chunk. The helper writes only inside that chunk,
subject to its clipped cross-section. It computes L=floor(r*randRange(1.5,3.0)
+0.3*(h-80)). For local offsets dx,dz, top is h+L+a*dx+b*dz, with a,b selected
from[-1,1]; integer Y is strictly below that top. Its bottom is the larger of
local surface minus randRange(3,7) and h-8. Candidate height/base predicates and
empty intervals can reject writes. These additions depend on terrain and may
extend beyond the body disk; they are not a fixed extra height or new families.

MountainPiece.makeBoundingBox uses floor(C.axis-R) to floor(C.axis+R+1) on
every axis, including Y, rather than using H for its vertical extent. Six
retained full starts provide horizontal generation-envelope examples, with
sizes and exact positions in the authoritative attributes. Their saved Y spans
are retained as context only. Do not infer repeated identical layouts across
runs or a typical/all-layout maximum from these six starts.

The approximate footprint is therefore the nominal100 to200-block body diameter,
supported by saved horizontal examples and the separate chunk-local decoration
rule. The approximate vertical size is the two parameter scales plus the explicit
terrain/noise and crystal formulas. Actual occupied relief is unmeasured and is
not an additional Item8 backlog item. Both required size assessments are now
integrated; no procedural size simulation is needed.
