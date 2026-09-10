# Four missing temple material outcomes

Status: source-derived origins and bounded experiment declared. Runtime placement
and saved results are NOT EXECUTED. Item 13 remains IN PROGRESS.

## Exact missing evidence and smallest experiment

The [coverage record](../coverage.md#temple-processor-outcome-availability-and-bounded-remaining-read)
exhausts the three indexed baseline starts: two blackstone temples and one Nether
temple, all gold. Existing Item 7/8 start references add no candidate. The missing
cells are debris and lodestone for each fixed family. Reuse the natural gold-case
geometry/quality reports; do not generate another density survey or reclassify.

Perform exactly four forced template placements with the **existing packaged
randomize_gold_block processor**, on one freshly hash-verified retained runtime.
This is a material-outcome diagnostic in an actual disposable world. It does not
measure natural frequency, validate the structure locator/generation-height rule,
create real players or test the structure's natural-spawn override. Direct template
placement does not create an accepted natural structure-start observation.

No template, processor, retained JAR or frozen configuration may be edited to
force an outcome. Runtime output must independently confirm the preselected
material. A mismatch is a retained failure, never corrected by /setblock.

## Source-derived position choice

Pinned SRG jar SHA-256:
26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71.
RuleProcessor.processBlock offsets0..11 seed RandomSource.create with
Mth.getSeed(transformedBlockPosition), independently of world seed or the
StructurePlaceSettings random. Mth.getSeed(int,int,int) performs an int multiply
x*3129871, XORs it with z*116129781L and y, then returns
(seed*seed*42317861L+seed*11L)>>16 using Java overflow. RandomSource.create(long)
constructs LegacyRandomSource. The shared processor's ordered .2 debris then .1
lodestone random-block-match rules use the ordinary nextFloat draws. Repeating
an origin therefore does not constitute another material trial.

[SelectOrigins.java](SelectOrigins.java) reproduces these source calculations with
Java's matching48-bit Random sequence. It also checks agreement with the two
already observed gold coordinates. This is a prediction to verify in the retained
runtime, not a replacement for that verification. Its purpose is to reduce a
potential random placement search to exactly four actual placements. No generalized
sampling framework or new validator is added.

The fixed search order is each root in blackstone/Nether order, each material in
debris/lodestone order, then first unused grid index0..255. Origins are
(32*(index%16),160,32*(index/16)); central local offsets are(3,4,3) and(6,4,6).
One grid cell is reserved per selected case to prevent overlap. The
[selection](selection.json) is explicitly SOURCE-DERIVED, not observed outcomes:

| Template | Origin | Expected central material |
| --- | --- | --- |
| blackstone_temple_small_1 | 160,160,0 | ancient_debris |
| blackstone_temple_small_1 | 32,160,0 | lodestone |
| nether_temple_medium_1 | 416,160,0 | ancient_debris |
| nether_temple_medium_1 | 64,160,0 | lodestone |

All are in minecraft:the_nether, rotation NONE, mirror NONE. Y160 isolates the
experiment from natural terrain; this artificial elevation is not natural burial
or playable entry evidence. Require the full target volumes to be air before
placement and within the runtime's build limits. Abort rather than clear terrain
or silently move a selected origin. No players, equipment, combat, harvest, elapsed
playtime or realized encounters are part of this experiment.

## Protocol, budget and implementation boundary

Reuse collision/run.py's exact retained136 materialization, frozen configuration,
pinned Temurin, port check, source-commit binding, build/attach path and existing
registry lifecycle. Extend it only with a specific temple-variant mode and one
small placement probe; the current collision/spawner measurements must not rerun.
The existing collision probe cannot call StructureTemplate.placeInWorld or retain
these world outputs, which is the concrete reason a placement branch is needed.
Do not duplicate the lifecycle, materialization or custody implementations.

Use ordinary seed42, -Xms1G -Xmx4G, the same pinned runtime/configuration identities
as the completed Item 13 captures. Every retry needs new instance/output paths
and fresh verified materialization. Neither accepted source worlds nor earlier
proof instances are modified. Preserve all attempts and errors.

Load each exact packaged template through the runtime template manager, add the
registered processor list to ordinary StructurePlaceSettings, and place through
StructureTemplate.placeInWorld with rotation/mirror NONE, declared origin and
update flags2. Capture exact settings, return
value, processed central state and all saved blocks in each envelope plus three
blocks of padding. Require source template dimensions7x8x7 and13x9x13 and no
placed entities/block entities, as established by packaged inspection. Do not
substitute a processor-only list projection for actual saved blocks.

The first blackstone/debris placement is the representative. Verify its expected
outcome and complete block readback before expanding to the other three placements
within this same predeclared experiment. Stop on any failure. A source-prediction
mismatch, occupied target, missing template/processor, incomplete chunk, lifecycle
failure or overrun is retained and does not trigger an automatic broader search.
After placement, use the existing correlated save-all flush, matching confirmation,
stop and clean-exit sequence. Retain stopped-world evidence through the existing
archive/restore path; immediate readback alone is not durable world custody.

Budget: four templates,3826 authored-envelope cells,15,562 padded readback cells,
at most16 distinct padded chunks (the four origins occupy distinct chunk pairs).
The templates stay within four core chunks; padding adds neighboring reads.
Allocate2 GiB disposable instance and20 MiB capture output, with5 GiB free required,
600-second lifecycle/readiness limit and120-second clean-stop limit. Prior fresh
captures took206..229 seconds and about650 MiB instance/6.4 MiB raw output; those
are reference costs, not measured placement timing. Each per-case server-thread task has a30-second timeout; do not disable the
frozen watchdog to hide an expensive query. Record actual duration and storage before another experiment.

No raw runtime outcome exists yet. After successful saved-state verification,
integrate material-specific mining, drop/fire behavior and existing route relevance
into the two authoritative temple reports. These diagnostics are selected variants,
not independent seeds or empirical processor probabilities. Full Item 13 family
coverage and required clean PR review/merge remain separate unfinished gates.

## Reproduction and current verification

The source-selection command has executed successfully with the pinned Java:

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/java evidence/item-13/temple-variants/SelectOrigins.java > /tmp/item13-temple-origins.json
cmp evidence/item-13/temple-variants/selection.json /tmp/item13-temple-origins.json
```

The runtime command will be recorded after the specific mode is implemented;
it is not falsely listed as an executed or validated workflow here.

The selector also compiles with -Xlint:all -Werror using an explicit temporary
classpath, matching the existing probe builder. An initial compile inherited an
invalid ambient classpath entry and was rejected by -Werror; specifying the
output directory as classpath corrected that build invocation without changing
source or suppressing warnings. No runtime experiment was attempted.
