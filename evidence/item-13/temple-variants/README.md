# Four missing temple material outcomes

Status: r5 completes all four placements and local saved-state verification.
Four earlier attempts remain rejected. External custody and report integration
now pass; Item 13 remains IN PROGRESS.

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

The specific placement mode is implemented and passes focused Python lint/type
checks plus pinned javac -Xlint:all -Werror. Runtime execution is still pending
at this implementation milestone. The existing attach subprocess has a45-second
total timeout, in addition to each case's30-second task limit. No timeout or
watchdog setting is relaxed. Execute once with new paths:

```sh
uv run python -m evidence.item-13.collision.run --temple-variants evidence/raw/item13/temple-variants-r1 instances/item13-temple-variants-r1
```

The probe writes the attempted case and partial successful rows on an exception;
the existing launcher retains rejection, console and configuration/lifecycle
records. Stopped-world custody and material-report integration follow successful
execution. A compiled implementation is not evidence that placement works.

The selector also compiles with -Xlint:all -Werror using an explicit temporary
classpath, matching the existing probe builder. An initial compile inherited an
invalid ambient classpath entry and was rejected by -Werror; specifying the
output directory as classpath corrected that build invocation without changing
source or suppressing warnings. No runtime experiment was attempted.


## Rejected r1 and narrowly revised r2

Producer ba86a2d33f758dc7a57fc0b7d847cb95967f2cff reached readiness, but the
first case's30-second task timed out. No case completed; no successful placement
or outcome is claimed. The lifecycle killed the entire process group (return-9),
without a correlated save or clean stop, at163.28 seconds overall. The
[r1 core retention](r1-retention.json), partial projection and redacted console
preserve the failure. Full raw files and instance remain at their original paths.
The available trace does not pinpoint the blocking operation; chunk preparation
was included inside the per-case task. Do not infer a material mismatch.

For r2, keep every origin, processor, template, actor exclusion and timeout.
Replace avoidable new-world generation with a fresh byte-verified copy of accepted
full-ordinary-r1-baseline. The source is the existing custody restored-world/world;
verify its complete inventory before and after copying under the existing POSIX
lock, and verify the destination against the same inventory before boot. Source
archive/backup identities are bound in capture.json. A new prepared target's frozen
server configuration must match the copied world inventory; fail on extra/drifted
files. Ignore session.lock during copying, as required by world custody. This is
fresh materialization for the new experiment, not reuse of the failed instance.
Add phase logging to show chunk preparation, air check, placement and verification.
No timeout relaxation or configuration tuning is introduced.

The original2-GiB instance/20-MiB capture budgets and5-GiB free floor remain.
The accepted world copy is existing data, not a regenerated survey. Execute with
new paths after committing the revised producer:

```sh
uv run python -m evidence.item-13.collision.run --temple-variants evidence/raw/item13/temple-variants-r2 instances/item13-temple-variants-r2
uv run python -m evidence.item-13.collision.retain --temple-attempt 2
```

r2 runtime execution is pending at this correction milestone. The retention
extension uses the existing lossless/redacted format for either of the two named
attempts. Its focused lint/type checks and the probe's pinned strict compilation
pass. The launch function keeps one lifecycle/failure boundary; its existing
complexity exception is extended to the narrowly added fixed probe branch rather
than creating a second lifecycle framework.


r2 was rejected before server launch: the materializer leaves world absent, and
opening its destination POSIX lock raised FileNotFoundError. No probe or runtime
observation occurred. Of the five core probe outputs, only [capture.json](r2-capture.json.gz) exists for
this prelaunch rejection; missing console/projection files are not fabricated.
The raw directory also retains copied latest.log/debug.log from the materialized
instance. Those logs do not prove an r2 server launch.
The narrow fix creates the new target world directory before locking/copying.
No existing target is reused. r3 uses the same protocol/limits and fresh paths:

```sh
uv run python -m evidence.item-13.collision.run --temple-variants evidence/raw/item13/temple-variants-r3 instances/item13-temple-variants-r3
uv run python -m evidence.item-13.collision.retain --temple-attempt 3
```

The accepted source inventory has503 files totaling428,092,106 bytes. This fits
the2-GiB instance allocation with the existing runtime. Source and destination
inventory checks remain mandatory. The r2 capture is losslessly retained with
`gzip.compress(raw,mtime=0)`; its original SHA-256/size are recorded below.

Original r2 capture: SHA-256 305e39811cd20544ec775c0ad089e3e396e124cf6594c098b4c9569768b795a2, 982 bytes.


## Rejected r3 and asynchronous chunk request correction

Producer f851a37f9e43ddbe381a78c8f60743a7ac768154 passed source/destination
inventory verification and server readiness. The first case timed out in the
logged chunks phase, before air check or placement. Zero cases completed.
Overall elapsed time was126.56 seconds; no matched flush or clean stop occurred,
and the process group was killed with return-9. The [r3 core retention](r3-retention.json)
preserves the projection, capture, console, attach failure and build output.

Read-only inspection of the accepted source's hash-bound Nether regions
r.0.-1.mca and r.0.0.mca confirms that all four first-case padded chunks
(9,-1),(10,-1),(9,0),(10,0) already have full status. The source inventory check
still gates every fresh copy. This locates the timeout in synchronous loading, not evidence
that the accepted source lacks generated chunks or that a material mismatched.

Pinned ServerChunkCache.getChunkFuture bytecode offsets17..52 call managedBlock
when invoked on the server thread; offsets55..81 instead queue getChunkFutureMainThread
on the chunk executor and compose its future when called off-thread. Therefore
r4 calls the public future method from the attach thread, waits off-thread for
all padded chunks, and only then queues the placement/readback task on the server.
Calling the future method from a server task would retain the demonstrated stall.
The complete request/wait/place sequence shares one30-second per-case deadline;
the45-second attach limit and frozen watchdog/configuration remain unchanged.
Strict pinned Java compilation and focused Python lint/types pass.

Fresh r4 command, not yet executed at this producer milestone:

```sh
uv run python -m evidence.item-13.collision.run --temple-variants evidence/raw/item13/temple-variants-r4 instances/item13-temple-variants-r4
uv run python -m evidence.item-13.collision.retain --temple-attempt 4
```


## Rejected r4 and processed-command barrier for r5

Producer190902b376050f1ee05f897808d17280f9f7e65c reached readiness and requested
chunk futures, but the first case's shared30-second deadline expired before
placement. Zero cases completed. Elapsed time132.632 seconds; no flush/clean stop;
process-group cleanup returned-9. [Core retention](r4-retention.json) preserves
this failure. A requested SIGQUIT diagnostic raced with cleanup and found no
process; no thread dump was produced or claimed.

The log places readiness at04:24:28, post-start permission/travel-map hooks
at04:24:30, temporary test-level work at04:24:33 and04:24:48, then tick overload
at04:24:51. Thus expensive startup continued inside the probe's deadline.
This is evidence for separating post-start work from the diagnostic, not proof
that startup alone caused every earlier timeout.

For fresh r5, reuse the existing lifecycle with its small opt-in console barrier.
After readiness, send a fresh random `say mcpack-probe-ready-...` marker and wait
for its exact server response before attaching. The server must process this
command after startup before any probe work starts. No fixed sleep, extra world
generation, configuration change or deadline relaxation is introduced. Missing
response is a lifecycle timeout/failure with cleanup, never implicit permission
to attach. The default path for previous consumers remains unchanged. The
barrier addresses this observed startup overlap; it is not a new review framework.

Focused lifecycle/runner tests pass27 cases, including successful barrier-before-
probe ordering and a missing response that never attaches and kills the process
group. Lint, formatting and types are checked on affected files.

```sh
uv run python -m evidence.item-13.collision.run --temple-variants evidence/raw/item13/temple-variants-r5 instances/item13-temple-variants-r5
uv run python -m evidence.item-13.collision.retain --temple-attempt 5
```

This r5 command is pending at its producer milestone. Keep the four earlier
attempts and their original instances. If r5 fails, inspect that specific failure
before proposing any further experiment; do not run an automatic retry series.


## r5 runtime result and saved-state acceptance work

Producer2f653748a6f46d48be14a9537677a0454bcd6f46 completes all four placements
with their expected materials, matched flush, clean exit0 and frozen configuration.
The [r5 core retention](r5-retention.json) binds the raw projection to SHA-256
b3e1a088879bf6fd02039c2768e3d40912abfb18012fe11d199038629a326093.
Total runtime140.95 seconds. Per-case placement/readback times (excluding chunk
preparation) are1.195317692,0.385737464,1.122853491,0.551276356 seconds in selection
order. These are probe costs, not gameplay times. The attempted SIGQUIT diagnostic
found the server already exited; it had no effect and produced no thread dump.

Measured instance storage is1,103,609,840 bytes across1103 files; raw capture is
5,888,474 bytes across240 files. The stopped world is428,261,145 bytes across504
files including session.lock. The2-GiB instance and20-MiB capture budgets pass.
For custody/readback allocate3 GiB additional storage and120 seconds per local
archive, restore or saved-block read, with5 GiB free floor. Current free space
is34,682,707,968 bytes. Reuse the existing stopped-world backup/restore and archive
publication tools, excluding session.lock. Verify a fresh restored copy's complete
inventory before/after reading the four padded volumes (15,562 cells).
Compare every saved block with immediate readback and preserve any changed blocks;
require the four central outcomes and inspect changes before material acceptance.
The natural gold cases remain terrain/access evidence. Forced Y160 cases are
processor/material diagnostics and do not establish new natural starts or encounters.


The [saved comparison](r5-saved-verification.json) passes all15,562 cells with
zero differences from immediate readback and all four expected central blocks.
The [local world restore](r5-world-restore.json) binds503 files to world archive
SHA-256451c9de1804e859f8daf18cfb545a4879cd994cf677ef9e1a46cf1949a40a37c
(162,749,467 bytes), excluding session.lock. The complete backup receipt hash is
cf6d6b5fc690fbceab9941ad1b0bc4b4a74d192e4ae1597469e4b5a9039836d1.
[verify_saved.py](verify_saved.py) reuses existing inventory, POSIX lock, region/NBT
and block-section readers. The ordinary extractor requires a natural structure
start and cannot represent these deliberately unregistered placements; this small
reader instead compares the four immutable probe volumes with the verified restore.
It does not invent starts or count templates as rooms.

Executed commands:

```sh
uv run python -m tools.manage_item4_environment backup --world instances/item13-temple-variants-r5/world --archive evidence/raw/item13/temple-r5-custody/world.tar.gz --receipt evidence/raw/item13/temple-r5-custody/world-backup.json
uv run python -m tools.manage_item4_environment restore --archive evidence/raw/item13/temple-r5-custody/world.tar.gz --sha256 451c9de1804e859f8daf18cfb545a4879cd994cf677ef9e1a46cf1949a40a37c --target evidence/raw/item13/temple-r5-custody/restored-world > evidence/raw/item13/temple-r5-custody/world-restore.json
timeout 120 uv run python -m evidence.item-13.temple-variants.verify_saved evidence/raw/item13/temple-r5-custody/restored-world/world > evidence/raw/item13/temple-r5-custody/saved-verification.json
cmp evidence/item-13/temple-variants/r5-saved-verification.json evidence/raw/item13/temple-r5-custody/saved-verification.json
```

Within each family, align the two forced padded arrays by relative coordinate and
compare palette-decoded blocks. Exactly one cell differs: central index1267 in
the2366-cell blackstone volume, index2707 in the5415-cell Nether volume. Every
other block state is equal. Saved verification makes this relationship valid for
the stopped copies too. Combined with the registered processor's only gold-target
rules and the source-supported full-cube replacement shapes, the existing gold
route can carry a conditional material substitution. The two reports below retain
terrain/access from natural gold observations and never relabel forced Y160 stages
as natural entry or realized encounters. External raw custody remains pending.


[External raw custody](custody/README.md) now passes all280 archive members,
local/download restores, the503-file nested downloaded-world restore and identical
15,562-cell saved verification. The release tag resolves to the exact successful
producer. The two authoritative temple reports integrate conditional material
models; full Item 13 family/repetition coverage and final reviewed delivery remain.
