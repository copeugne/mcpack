# BetterEnd remaining root consumers

Selector 95997cf captures eighteen classes for remaining custom-root generators,
the cave-biome feature consumers, village keys and three concrete integrations.
The complete generated capture reproduces byte for byte against fresh r1 output.
This is an isolated generated-source increment. No new measurement mechanism,
world experiment or baseline modification is involved.

Manifest SHA-256: eb0d8ea37b2766dc0081c0e84035d9c37168758023bb33400d3028ef73363dbd.

```sh
uv run -m tools.inspect_item8_pool_elements --archive BetterEnd-21.0.31.jar --class-name org/betterx/betterend/integration/DyeDepotIntegration.class --class-name org/betterx/betterend/integration/FlamboyantRefabricatedIntegration.class --class-name org/betterx/betterend/integration/byg/BYGIntegration.class --class-name org/betterx/betterend/world/features/terrain/caves/CaveChunkPopulatorFeature.class --class-name org/betterx/betterend/world/features/terrain/caves/EndCaveFeatures.class --class-name 'org/betterx/betterend/world/structures/features/EndBridgeStructure$Anchor.class' --class-name org/betterx/betterend/world/structures/features/EndBridgeStructure.class --class-name org/betterx/betterend/world/structures/features/EndSulphuricCaveStructure.class --class-name org/betterx/betterend/world/structures/features/GiantIceStarStructure.class --class-name org/betterx/betterend/world/structures/features/GiantMossyGlowshroomStructure.class --class-name org/betterx/betterend/world/structures/features/SDFStructureFeature.class --class-name 'org/betterx/betterend/world/structures/features/SmallIslandStructure$IslandGeometry.class' --class-name org/betterx/betterend/world/structures/features/SmallIslandStructure.class --class-name org/betterx/betterend/world/structures/piece/CavePiece.class --class-name org/betterx/betterend/world/structures/piece/EndBridgePiece.class --class-name org/betterx/betterend/world/structures/piece/SulphuricCavePiece.class --class-name org/betterx/betterend/world/structures/piece/VoxelPiece.class --class-name org/betterx/betterend/world/structures/village/VillagePools.class --output evidence/raw/item8/betterend-remaining-root-consumers-r1
```

The five newly bound custom roots are end_bridge, sulphuric_cave,
giant_ice_star, giant_mossy_glowshroom and small_island. Existing registration
source and packaged definitions supply their identities; these are existing
runtime roots, not five newly discovered families.

EndBridgeStructure selects terrain anchors and creates an EndBridgePiece.
The piece writes an end-stone-brick deck and walls with material variation.
Its anchor search can return without a piece. Preserve one bridge-design
candidate; anchors, span variation and piece serialization are not families.

EndSulphuricCaveStructure creates SulphuricCavePiece, whose placement concerns
cave air, water, sulphuric rock, vents, brimstone, crystals and tube worms.
GiantIceStarStructure fills an SDF with snow and emerald ice materials.
GiantMossyGlowshroomStructure fills a fungal SDF. SmallIslandStructure builds
terrain with flower/vine or waterfall/stalactite treatments. These are named
terrain/vegetation root candidates; final family grouping must reconcile them
with the previously preserved formation decisions. Shared SDFStructureFeature
and VoxelPiece construct and serialize the selected geometry, not more designs.
No detailed geometry or world-occurrence claim follows from this capture.

VillagePools creates keys for the already accounted village pools and the
village_chorus placed feature. The latter's packaged definition uses vanilla
chorus_plant, not another settlement generator.

EndCaveFeatures consumes EndBiomes.getCaveBiome, sets cave biome information and
dispatches selected cave floor/ceiling features. CaveChunkPopulatorFeature also
uses selected cave floor/ceiling features. This establishes a consumer for the
separate cave-biome path; it does not prove every feature attached to a surface
biome also runs in caves.

BYGIntegration delegates blocks, features and biomes to BYG-specific registries.
Flamboyant's init is empty and its explicit block registration concerns colors;
DyeDepot supplies colored crafting recipes. Preserve actual conditional dispatch
through BCLib as an unresolved shared input. Do not recursively inspect inactive
compatibility trees merely because they exist in the archive.

Remaining provider work: reconcile other feature registration consumers,
remaining common mixin generation hooks and shared integration/modifier
activation. Do not reopen the completed 128-template partition. Whole-provider
coverage and canonical family totals remain incomplete.

## Bridge assessment

Provider discovery above is historical and is now closed. This increment assesses
the nine remaining bridge attributes using the already captured EndBridgeStructure,
its Anchor, EndBridgePiece and the existing full-start observations. No new
capture, source extractor or measurement system is needed.

The packaged root has empty spawn_overrides and surface_structures generation
step. Its custom findGenerationPoint supplies a stub at Y0, then generatePieces
samples terrain heights and chooses two anchors. The stub is not deck elevation.
Candidate endpoints require horizontal separation24 to96 and height difference
at most12, with other terrain/island/angular predicates. Missing suitable anchors
can produce no piece; these are placement constraints, not separate families.

EndBridgePiece constructs a deck, railings, landings and supporting columns.
Its write paths use END_STONE_BRICKS, the CRACKED and WEATHERED slots of
END_STONE_BRICK_VARIATIONS, and END_STONE_BRICK_WALL. BlocksHelper is consulted
for replaceability; it is not a content generator. The root/piece path has no
entity creation, template entity loading, container-loot assignment or explicit
spawner configuration. It therefore authors a traversal structure without a
direct encounter or container reward. Empty spawn overrides do not suppress
natural biome enemies. These source statements do not assert complete runtime
absence of external mobs or loot injections.

Deck and railings provide visual cues, with weathered/cracked material variation
and possible railing gaps. Supports extend below the crossing. Exposure and
terrain occlusion are qualitative assessments; no visibility-distance or player
discovery measurement is inferred from source code or structure-start presence.

Five retained full starts represent four distinct layouts:

| Seed | Run and decoded line | Chunk | Saved size X,Y,Z |
| --- | --- | --- | --- |
| 6671238423019257953 | run-a/mountainous:6443 | 88,5 | 35,23,35 |
| 6671238423019257953 | run-a/mountainous:6654 | 91,13 | 24,19,40 |
| 95920844204830198 | run-a/ocean-heavy:8106 | 98,15 | 64,27,80 |
| 95920844204830198 | run-b/ocean-heavy:8106 | 98,15 | 64,27,80 |
| -3503646078644842058 | run-b/biome-diverse:7457 | 97,-9 | 24,23,40 |

Each source is the corresponding chunks.jsonl in preserved Item7 custody, joined
by world-bounds.json.gz. Exact envelopes and references are integrated in the
authoritative attributes. The existing observed_bounds implementation supplies
inclusive spans. makeBoundingBox expands endpoint minima/maxima by six on X/Z,
and uses min(endpointY)-12 to max(endpointY)+6 vertically. Thus the reported
examples include margins and support allowance, not occupied area, deck thickness,
typical dimensions or all-layout maxima. The ocean-heavy record repeats the
same layout; it is not a fifth independent sample. The bridge is now assessed
for all Item8 attributes without claiming Item8 as a whole is complete.

## Ice star assessment

Nine remaining attributes are integrated from GiantIceStarStructure, the retained
VoxelPiece and FeatureBaseStructure, and existing cone/rotation semantics under
pillar-shape-semantics. No runtime observation or new measurement tool is needed.

getSDF selects S using randRange(20,35) and25..40 Fibonacci direction points.
Each parent cone has half-height S, lower/upper radii3+0.2*(S-5) and0, then
translation Y=S-0.5. It rotates these cones and unions them. The already captured
SDFCappedCone uses height as half-height, so20..35 is not total spike length.
Special near-pole handling uses the actual Y-axis rotation branch; do not replace
it with an idealized perfectly symmetric star.

A cylinder enclosing a translated cone has |Y| at most2*S-0.5 and lateral radius
r=3+0.2*(S-5). It fits a sphere of radius sqrt((2*S-0.5)^2+r^2). Rotations and
unions preserve that enclosing sphere, giving a conservative continuous diameter
of2*sqrt((2*S-0.5)^2+r^2), approximately80 to141 blocks over the nominal parameter
range. This is an approximate parent scale on all three axes, not a measured
occupied footprint, attained size or strict floating-point voxel bound.

Direct pinned BCLib getDistance inspection confirms SDFTranslate subtracts its
translation from query coordinates and SDFUnion returns the minimum of the two
source distances. Exact class/JAR identities are in processor_inspection.

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c -classpath downloads/item3/candidates/bclib-21.0.24.jar org.betterx.bclib.sdf.operator.SDFTranslate org.betterx.bclib.sdf.operator.SDFUnion
```

The supplied postprocess callback chooses ANCIENT_EMERALD_ICE,
DENSE_EMERALD_ICE, EMERALD_ICE or original DENSE_SNOW from distance/random
thresholds. It returns a block state, without adding geometry or an encounter.
The root's fillRecursive callback builds the StructureWorld consumed by
VoxelPiece; that piece places stored chunks and primes heightmaps. The inspected
root/callback/piece paths have no direct entities, spawners or container-loot
assignment. Empty packaged spawn_overrides leave natural spawning and other
systems possible; harvested materials are not a structure loot-table source.

findVoidGenerationPoint supplies a stub at Y80 without a terrain-height test.
The root overrides generation and independently selects center Y32..128, plus
local X/Z offsets4..12. Do not apply SDFStructureFeature's separate surface-rooted
static generation method to this override. The formation has floating intent,
but source placement does not guarantee clearance from terrain. Its radial
spikes and snow/ice zones are qualitative discovery cues, not measured visibility.

## Glowshroom content assessment

Seven descriptive attributes are integrated from the retained
GiantMossyGlowshroomStructure, SDFStructureFeature, FeatureBaseStructure and
VoxelPiece code. Footprint and vertical size remain open. No new source capture,
world experiment or measurement implementation was introduced.

The root uses the shared surface generator, unlike giant ice star's override.
FeatureBaseStructure first samples WORLD_SURFACE_WG for its generation point and
requires sampled height at least10. The separate SDFStructureFeature generator
chooses local X/Z offsets4..12, samples base surface height, requires height>5,
and positions the volume at that sample. Preserve the two distinct checks.
Packaged spawn_overrides are empty. The result is surface-rooted by design, not
proof of actual complete exposure.

The root builds a cap from cone/subtraction/wave/smoothing components, a stem
from a spline, and a basal sphere. It selects cap, hymenophore and mossy-glowshroom
wood/bark states. The postprocessor creates cap-transition states where wood and
cap meet, and can add MOSSY_GLOWSHROOM_FUR to adjacent air and beneath hymenophore.
These are material/vegetation writes, not direct entity insertion, spawner
configuration or container-loot assignment. The callbacks and VoxelPiece path
therefore support no directly authored encounter or table reward. This does not
exclude natural biome enemies, external systems or harvested material drops.

Stem, cap, underside and fur are qualitative visual cues, not a measured sight
distance. The selected stem-length parameter is10..25 and final scale2..3.5,
but these alone do not describe total occupied size. Cap coordinate modification,
flat waves, smooth unions, final round radius1.5 and neighboring fur writes must
be accounted for before final size attribution. Reuse the already known cone,
translation and union semantics, and inspect only the remaining shared operators
needed for the two outstanding geometry claims. Do not introduce a new simulation
or measurement framework merely to reproduce this source description.

## Glowshroom geometry assessment

Both size attributes now describe nominal parent scale with explicit deformation
limits. This uses the retained root and direct inspection of its BCLib helpers,
with exact identities in processor_inspection. No new capture or simulator is
needed to satisfy an approximate description.

The positive cap parents are a centered half-height2.5 cone, a half-height3 cone
translated upward5, a copy of that cut cone translated another1.25 and scaled
X/Z by1.2, and an inner half-height3 cone translated4.25. Subtracted geometry
cannot enlarge these undeformed parents. Their maximum lateral radius is15.6,
and parent Y range is[-2.5,9.25]. The later +2.5 translation and stem-tip
attachment give cap parent Y[L,L+11.75]. The basal sphere has radius4 and Y
scale0.7, reaching -2.8. L is selected10..25 and final uniform scale Q is2..3.5.
Thus nominal cap diameter31.2*Q is62.4..109.2; scaled stem endpoint length L*Q
is20..87.5; the undeformed parent vertical span (L+14.55)*Q is49.1..138.425.
These component/parent scales are not occupied dimensions or all-layout maxima.

The direct helper interpretation is:

- SDFScale evaluates source at coordinates divided by Q, then multiplies distance
  by Q. SDFScale3D divides coordinates separately, without distance rescaling.
- SDFFlatWave adds cos(atan2(x,z)*rays+angle)*intensity to source distance via
  SDFDisplacement. Cap uses12 rays/intensity1.3; base uses5 rays/intensity1.5.
- Smooth union uses h=clamp(0.5+0.5*(b-a)/k,0,1), then
  lerp(h,b,a)-k*h*(1-h). The root uses smoothing radii3 and4.
- The cap coordinate callback changes query Y to Y+0.3*R*N-0.15*R, where
  R=sqrt(x*x+z*z) and N is the captured position-dependent noise sample.
- Final SDFRound subtracts1.5 from distance after uniform scaling. The material
  postprocessor can add neighboring fur, including one block below hymenophore.

SplineHelper.offsetParts iterates from index1 through the final point and adds
nextGaussian times the supplied per-axis scale. The root supplies(1,0,1), so
horizontal offsets have no explicit clamp and include the cap attachment tip.
Do not invent a finite universal footprint or call the nominal cap diameter the
whole realized formation width. These limitations are part of the assessment,
not a requirement to simulate every random layout or measure live occupied size.

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c -classpath downloads/item3/candidates/bclib-21.0.24.jar org.betterx.bclib.sdf.operator.SDFScale org.betterx.bclib.sdf.operator.SDFScale3D org.betterx.bclib.sdf.operator.SDFFlatWave org.betterx.bclib.sdf.operator.SDFDisplacement org.betterx.bclib.sdf.operator.SDFSmoothUnion org.betterx.bclib.sdf.operator.SDFRound org.betterx.bclib.util.SplineHelper
```
