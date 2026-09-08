# Nonregistry placement probe diagnostic

Status: REAL-RUN VALIDATION INCOMPLETE. r1 had no target execution; r2
failed helper classloading; r3 passes capture health but fails declared equality. No nonregistry
density or runtime generation equivalence is accepted from this probe.

The retained [scarecrow writer evidence](../item-8/sources/explorations-scarecrow-scope/README.md)
shows five direct WorldGenLevel.setBlock calls whose booleans are discarded.
A feature return is therefore insufficient proof of complete placement. This
is the concrete gap requiring instrumentation beyond the existing registry and
dimension reader. No new classification or provider audit was performed.

[Item10PlacementProbe](../../tools/Item10PlacementProbe.java) instruments only
ScarecrowFeature.place. It requires exactly one matching method and five matching
write call sites. It preserves each original write invocation and boolean and
records attempt origin/dimension, write position/state/flags/result, normal exit,
write exceptions, installation identity and unfinished attempts at shutdown.
It does not consume random values or change arguments. Runtime equivalence has
not been established. Exceptions outside write calls leave unfinished attempts;
those traces cannot be accepted as a complete census. Installation failures,
missing installation records, duplicate installations or missing shutdown are
also invalid evidence, even if the JVM continues running.

The pinned JDK's internal ASM is used through an explicit module export. Its
observational JVM flag and the compiled probe hash will need to be recorded as
an instrumentation overlay before any controlled experiment. No provider JAR is
modified. A future matched fresh-world control must compare generated content;
passing the fixture below is not a substitute for that experiment.

## Executed checks

```sh
uv run --no-sync pytest tests/item10/test_placement_probe.py -q
uv run --no-sync ruff check tests/item10/test_placement_probe.py
uv run --no-sync basedpyright tests/item10/test_placement_probe.py
```

The single fixture test passes using pinned Temurin 21.0.12.1+1. Compilation
uses `-Xlint:all -Werror`, an explicit classpath and the declared ASM export.
It verifies the retained Explorations archive and class hashes from the accepted
Item 8 identity, then successfully transforms that exact class. Separate JVMs
compare synthetic original and instrumented execution for normal writes, early
return and a thrown write exception. Return values, original call counts and
exception messages match; the refused write remains false and the exceptional
attempt remains explicitly unfinished. Ruff and type checks pass.

The fixture consumes write booleans to test preservation even though the actual
retained generator ignores them. It does not represent Minecraft terrain or
placement success. The first manual compile failed on an inherited invalid
classpath; the explicit classpath used in the reproducible test resolves that
build-input problem. No server was launched during this diagnostic.

Next: connect this bounded probe to the existing verified generation lifecycle,
predeclare the matched control and capture acceptance checks, and validate actual
Minecraft behavior before extending the hook set to other nonregistry writers.

## Predeclared Minecraft diagnostic r1

Declare this protocol and commit its executable sources before launching.
Use `tools.run_item10_probe` from the repository root, ordinary seed 42, with
the unchanged Item 7 RUN_SELECTIONS: 3,969 Overworld chunks and 961 each in
Nether, central End and outer End. Both members use fresh hash-verified
materializations, the 136 retained candidates plus the verified Chunky overlay,
pinned Temurin and the frozen Item 6 configuration. No player world is reused.

Run the probe first as `scarecrow-probe-r1`, with a 900-second lifecycle deadline.
Record the probe source/JAR hashes and exact JAVA_TOOL_OPTIONS in diagnostic.json.
The only added JVM options export the pinned JDK's internal ASM package and load
the probe. The control `scarecrow-control-r1` has no additional JVM options.
Undeclared inherited JVM options, reused instances and reused output directories
are rejected. Compilation output, console, configuration capture and all trace
records remain raw observations. Lifecycle success alone is not probe acceptance.

A probe with failed/missing installation, missing shutdown, unfinished attempts,
malformed records or no executed five-write placement is rejected or insufficient,
not a zero-density acceptance. Preserve it and diagnose before expanding. Run the
matched control only once the actual probe has exercised the target method and
its capture is complete. The matched comparison must verify the same complete
selected slots and generated block states, biomes and structure placements.
For each selected chunk compare section Y, block_states and biomes, plus full
block_entities and structures compounds; sort compound keys and section/block
entity ordering by stored coordinates while preserving palette/index order. No
other field is part of this generation-content projection.
Tick timestamps and dynamic entity movement are not world-generation equality;
no performance or dynamic-gameplay equivalence is claimed. The comparison
projection above is frozen before collection. Retain mismatches rather than
loosening equality after seeing them. This is instrument validation, not the
full Item 10 density sample or proof for other nonregistry families.

Host inspection before declaration: 13 GiB free persistent storage and about
9.4 GiB available RAM. Run one JVM at a time with the existing 1 to 4 GiB heap.
The earlier diagnostic took 260 seconds for the same generation selection and
127,167,697 world bytes. Reserve 3 GiB for this pair's instances, raw observations,
archives and restore workspace; expect roughly nine minutes for two generation
runs plus build, analysis and custody. These are planning estimates, not measured
probe overhead. No additional cleanup is authorized by this protocol.

```sh
uv run --no-sync python -m tools.run_item10_probe --name scarecrow-probe-r1 --mode probe --role ordinary
# After probe health and actual five-write execution are verified:
uv run --no-sync python -m tools.run_item10_probe --name scarecrow-control-r1 --mode control --role ordinary
```

Retain rejected runs as well as accepted ones. Use the existing world-backup and
raw-archive tools for immutable archive, manifest, download and restore checks
before relying on externally stored results. No instrumented generation has yet
run at this predeclaration checkpoint.

## r1 disposition and predeclared r2

The [r1 receipt](scarecrow-probe-r1/diagnostic.json) records 253.354 seconds,
all four selections completed, correlated save confirmation, clean stop and exit
0 under source `8b0850622ceb2be5730410d54f793d6bcf2fd0da`. The
[trace](scarecrow-probe-r1/trace.jsonl) contains one installation and one shutdown,
with zero attempted placements. Status: INSUFFICIENT for writer validation.
The [stopped-world backup](scarecrow-probe-r1/world-backup.json) retains the world;
raw console and configuration remain under `evidence/raw/item10/scarecrow-probe-r1`.
Do not run the r1 control or interpret absent calls as complete family coverage.

The initial seed choice failed to use available eligibility evidence. Directly
reusing the hash-verified r14 `run-a/<role>/analysis/overworld.json` artifacts in
[the retained core manifest](../item-7/archive/r14/core-manifest.json), intersect
their biome rows with the union of `families["explorations:scarecrow"]`.
`biome_constraints.resolved_variants[*].biomes` in the accepted Item 8 inventory.
Summing the existing `quart_cells` for matching rows gives ordinary 0,
mountainous 13,459, biome-diverse 3,038 and ocean-heavy 3,151. These are existing
surface exposure counts, not new placement measurements. The restored core
artifacts were rehashed against that manifest before reuse; no Item 7 audit or
world measurement was repeated.

Predeclare r2 on mountainous seed `6671238423019257953`, keeping the same fixed
selection sizes, frozen identities, probe source and comparison projection.
Use new `scarecrow-probe-r2` and `scarecrow-control-r2` paths. Targeting a region
with known eligible biomes is appropriate for instrumentation validation; this
is not a representative density estimate or a change to the full sampling frame.
Keep the same probe-health and five-write-execution gate before launching the
control. Do not change selection or seed again without preserving and
explicitly dispositioning this attempt. The same sequential 3 GiB pair allowance
and 900-second per-run deadline apply, in addition to retaining r1.

```sh
uv run --no-sync python -m tools.run_item10_probe --name scarecrow-probe-r2 --mode probe --role mountainous
# Only after complete actual five-write execution is verified:
uv run --no-sync python -m tools.run_item10_probe --name scarecrow-control-r2 --mode control --role mountainous
```

## r2 rejection and predeclared r3

The [r2 receipt](scarecrow-probe-r2/diagnostic.json) records a 900.4-second
timeout, incomplete generation, no save confirmation and process-group kill
(return code -9). The target executed but could not resolve Item10PlacementProbe
from NeoForge's game classloader. Raw console lines 2816 onward retain
NoClassDefFoundError and its ClassNotFoundException cause. This world is rejected,
not a density sample or a valid control. No r2 control was run. The raw directory
retains its incomplete world, console, trace and instrumentation artifacts.

An isolated classloader fixture reproduced the failure before the fix. The fix
adds three private synthetic bridges within the target class that resolve the
existing helper explicitly through the system classloader. MethodHandle.invokeExact
preserves original thrown exceptions. The added module read edge was removed:
it did not provide class visibility. Existing normal, early-return and exception
cases and the new isolated-loader case pass. The exact retained class still
transforms; real runtime equivalence remains unproven.

Predeclare r3 with the same mountainous seed, selections, frozen identities,
900-second deadline, projection and capture acceptance conditions as r2. Use the
corrected probe from this committed source, recording its compiled hash. Keep
all rejected evidence. Run a fresh control only after healthy actual execution.
Storage allowance remains 3 GiB for the new pair, with prior runs preserved.

```sh
uv run --no-sync python -m tools.run_item10_probe --name scarecrow-probe-r3 --mode probe --role mountainous
# Only after complete actual five-write execution and capture health are verified:
uv run --no-sync python -m tools.run_item10_probe --name scarecrow-control-r3 --mode control --role mountainous
```

## Generation comparison implementation

The existing density reader now exposes optional `--generation` output using
the projection declared above. Each selected chunk retains its coordinates and
content SHA-256. The ordinary census output is unchanged without the option.
Tests verify that tick timestamps are excluded, block and biome changes alter
the digest, and the output remains bound to the selected full-chunk denominator.
The Item 10 suite passes 27 tests; focused Ruff checks pass. A direct strict
basedpyright invocation on the whole standalone analysis tool failed on its
existing untyped JSON/CLI paths and the new projection. This invocation is outside
the configured `src`/`tests` checking surface and is not recorded as a pass.
The probe fixture's configured type check passes. No type-check policy was relaxed.

Reproduction for the retained ordinary pilot (read-only, new output path):

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/pilot-custody-r1/restored-world/world evidence/raw/item10/pilot-custody-r1/generation-projection.json --dimension minecraft:overworld --bounds -31 31 -31 31 --generation
```

This is a processing check on retained evidence, not another world experiment or
an Item 7 audit. Pair comparisons must compare the complete `generation_content`
arrays for matching seed, dimension and bounds; archive input hashes will differ
and are not substitutes for this content comparison.

The retained-pilot command completed with exactly 3,969 selected full chunks and
3,969 content digests. Output SHA-256:
`a2dcc24fff88c05dfd973ebe6084641daf5d1b0011b478f088682df567aacdbb`.
This proves processing completed, not equality with an instrumented world.

## Unsuccessful-run durability

Both r1 and r2 raw directories are retained together in
[the immutable release](https://github.com/copeugne/mcpack/releases/tag/item-10-probe-rejections-2026-09-08-r1).
The [manifest](scarecrow-probe-r2/archive-manifest.json) binds 258 files,
including both nested world archives, to custody source
`f48066f095e26162a0283041da04286db4784327`; the fetched tag resolves to that
commit. Individual diagnostic receipts retain their actual run revisions.
[Release metadata](scarecrow-probe-r2/release.json),
[local restore](scarecrow-probe-r2/archive-restore.json) and
[download restore](scarecrow-probe-r2/download-restore.json) record delivery.
The downloaded manifest matched the committed manifest byte for byte.
Nested world restores verified [r1's 158 files](scarecrow-probe-r1/world-restore.json)
and [r2's 86 files](scarecrow-probe-r2/world-restore.json). Restore integrity does
not make either rejected or insufficient experiment acceptable.

```sh
gh release download item-10-probe-rejections-2026-09-08-r1 --repo copeugne/mcpack --dir RESTORE_INPUT
uv run --no-sync python -m tools.archive_item7_evidence restore --archive RESTORE_INPUT/item10-probe-rejections-r1-r2-f48066f0.tar.gz --manifest evidence/item-10/scarecrow-probe-r2/archive-manifest.json --target RESTORED_RAW --receipt RESTORE_RECEIPT.json
```

The equivalent commands were executed under
`evidence/raw/item10/probe-rejections-r1-r2-custody`. Use each committed
world-backup receipt's SHA-256 with the existing world restore command for its
nested archive. No archive was booted. Initial local manifest metadata used an
abbreviated revision; it was expanded before publication, with the initial copy
retained locally. Archive bytes were unchanged.

## r3 observed lifecycle and pending comparison

The [probe receipt](scarecrow-probe-r3/diagnostic.json) records all four selections,
correlated save and clean stop in 348.93 seconds. Its [trace](scarecrow-probe-r3/trace.jsonl)
contains one correct class installation, six begin/end pairs, five successful
writes in each pair and one shutdown with zero unfinished attempts. This passes
the predeclared capture-health gate, not generation equivalence or density.

The [control receipt](scarecrow-control-r3/diagnostic.json) records the same
preflight identity and selections, no probe JVM options, correlated save and
clean stop in 366.501 seconds. Both stopped worlds are backed up locally; external
pair custody is pending. The probe content reader completed all 6,852 selected
chunks across four strata. Control content and biome processing is running.
Compare the declared projection without changing its fields or ignoring mismatches.

Measured storage from the backup receipts' `world_files[*].size_bytes` sums:
probe 138,788,002 bytes in 154 files; control 137,748,133 bytes in 155 files.
Compressed nested archives are respectively 89,301,602 and 88,170,980 bytes.
These include generated halo and lifecycle data beyond the 6,852 selected chunks.
Different total file sizes are not a substitute for generation-content comparison.
Neither the two elapsed runtimes nor their difference is a performance estimate.

Reproduce the pair comparison after all four reader outputs exist. This retains
both directions of every content mismatch instead of accepting equal counts:

```sh
for stratum in overworld nether end-central end-outer; do
  jq -n --slurpfile probe "evidence/raw/item10/scarecrow-probe-r3/generation-$stratum.json" --slurpfile control "evidence/raw/item10/scarecrow-control-r3/generation-$stratum.json" '
    $probe[0] as $p | $control[0] as $c |
    {dimension: $p.dimension, bounds_chunks: $p.bounds_chunks,
     probe_chunks: $p.full_chunks, control_chunks: $c.full_chunks,
     same_frame: ([$p.dimension,$p.bounds_chunks,$p.full_chunks] == [$c.dimension,$c.bounds_chunks,$c.full_chunks]),
     same_content: ($p.generation_content == $c.generation_content),
     probe_only: ($p.generation_content - $c.generation_content),
     control_only: ($c.generation_content - $p.generation_content)}
  ' > "evidence/raw/item10/scarecrow-probe-r3/comparison-$stratum.json"
done
```

## r3 equality failure and upstream evidence reuse

The [comparison summary](scarecrow-probe-r3/comparison.json) records matching
frames but only central End equal. All 3,969 Overworld chunks, 960/961 Nether
chunks and 671/961 outer End chunks fail the declared content projection.
The raw comparison files retain both sides of every mismatch; their hashes are
in the summary. Do not remove differing fields or relabel this gate as passed.
Registry starts are 42 versus 42 in Overworld with identical origins, 16 versus
20 in Nether, and two versus two with different origins in outer End. Central
End has zero starts in both. These are diagnostic counts, not all-family density.
All 64 control registry starts have biome attribution with no unavailable reason.

The accepted [Item 7 repeatability result](../../docs/items/Item-7-Baseline-Worldgen-Audit.md#repeatability-and-control-result)
already establishes semantic nondeterminism in fresh frozen-stack runs. It
explicitly keeps provider causality UNKNOWN and the prior Chunky control
unattributable. This should have informed the probe protocol before execution.
No Item 7 audit or baseline repetition is required to re-establish that fact.
R3 therefore cannot attribute its differences to the probe, and cannot validate
whole-world equivalence. The prior accepted upstream result is consistent with
these observations, not contradicted or reopened by them.

Direct inspection of chunk (0,0), region r.0.0.mca, in both retained r3 Overworlds
shows equal structures and block entities but differing section block_states,
including sculk-vein palettes at section Y=-4. This is not solely a timestamp
comparison. It is a specific raw-artifact inspection, not a causal diagnosis.

Stop expansion of the probe and do not launch r4. Reassess the validation claim
against the already measured stack nondeterminism before selecting further
experiments. Preserve the failed exact-equality gate and both raw worlds.
Do not tune C2ME or any frozen baseline configuration to force equality.

## r3 durable custody

The [r3 release](https://github.com/copeugne/mcpack/releases/tag/item-10-probe-pair-2026-09-08-r3)
retains both raw directories, including eight reader outputs and every mismatch.
The [498-file manifest](scarecrow-probe-r3/archive-manifest.json) binds custody
source `1658d44ed3cdb50a1a13e44fda2ea35cb46b6eae`; the fetched tag resolves to
that exact commit. [Local restore](scarecrow-probe-r3/archive-restore.json),
[download restore](scarecrow-probe-r3/download-restore.json) and
[release metadata](scarecrow-probe-r3/release.json) verify durable delivery.
The downloaded manifest matches byte for byte. Nested restores verified
[154 probe world files](scarecrow-probe-r3/world-restore.json) and
[155 control world files](scarecrow-control-r3/world-restore.json). Neither was booted.

```sh
gh release download item-10-probe-pair-2026-09-08-r3 --repo copeugne/mcpack --dir RESTORE_INPUT
uv run --no-sync python -m tools.archive_item7_evidence restore --archive RESTORE_INPUT/item10-probe-pair-r3-1658d44e.tar.gz --manifest evidence/item-10/scarecrow-probe-r3/archive-manifest.json --target RESTORED_RAW --receipt RESTORE_RECEIPT.json
```

Equivalent commands were executed under `evidence/raw/item10/probe-pair-r3-custody`.
Use each committed world-backup receipt's SHA-256 with the existing world restore
command for its nested archive. Custody success does not reverse the failed
equality result or prove probe causality.

## Coordinate corroboration and prospective validation correction

The committed [bounded inspection](scarecrow-probe-r3/inspect-writes.py) reads
the downloaded/restored probe world with the existing Anvil decoder and packed
NBT reader. It inspects all 30 recorded write coordinates using palette index
`localX + 16*localZ + 256*localY` and the saved section's palette. All 30 retain
the recorded block ID. [Full observations](scarecrow-probe-r3/world-crosscheck.json)
retain recorded state strings, complete saved states, coordinates and raw input
hashes. Fence properties may reflect subsequent neighbor updates; block-ID
corroboration is explicitly narrower than exact state equality.

```sh
uv run --no-sync python -c "import runpy; runpy.run_path('evidence/item-10/scarecrow-probe-r3/inspect-writes.py')" > CROSSCHECK.json
```

This command was executed from the repository root. A prior direct script-path
invocation could not import the root `tools` package and produced no inspection;
`runpy` uses the documented repository-root import context. This is a direct
inspection of retained immutable evidence, not a new generation or a generic
occurrence validator.

The [prospective protocol correction](protocol.md#collector-validation-under-established-baseline-variability)
replaces whole-world equality as a collector-correctness criterion because its
premise conflicts with already accepted Item 7 evidence. The r3 equality result
remains FAILED. Scarecrow capture health, bounded call-preservation checks and
coordinate corroboration pass; observer-free equivalence remains unproven.
No other nonregistry writer is validated by these six attempts. Do not extend
this result to complete Item 10 or silently omit the measurement overlay.

Review-candidate validation: `uv run --no-sync pytest -q tests/item7 tests/item10`
passes 255 tests. Focused Ruff checks pass for the changed lifecycle, diagnostic
runner, reader and tests. Type checks pass for the lifecycle, runner and changed
tests after annotating the runner's argparse strings; the direct runner check
initially exposed untyped CLI values. No runtime behavior or type-check policy
was changed by that annotation fix. The legacy whole-reader strict type-check
limitation recorded above remains explicit. No Item 11 workflow was tested.

## PR23 retained-trace review fix

[Finding 3953767367](https://github.com/copeugne/mcpack/pull/23#discussion_r3953767367)
is valid: the session-only capture-health check was not a reproducible repository
boundary. [The retained-trace validator](../../tools/validate_item10_trace.py)
now binds input bytes to the published r3 archive member before checking exact
installation identity, strict JSON records, sequential attempt identities,
pairing, zero-or-five writer counts, return/coordinate field types, shutdown and
absence of unfinished attempts. Whole-attempt omissions cannot bypass the
immutable archive hash. It reuses the existing strict JSON parser.

```sh
uv run --no-sync pytest -q tests/item10/test_retained_trace.py
uv run --no-sync python -m tools.validate_item10_trace evidence/item-10/scarecrow-probe-r3/trace.jsonl
```

Ten regressions pass, and [the result](scarecrow-probe-r3/trace-validation.json)
records six attempts and 30 writes, with zero refused writes. Ruff and type checks
pass for the validator and tests. This validates capture health only; it does not
reverse the world-equality failure or close the remaining NBT-type review finding.

## PR23 typed-NBT review fix

[Finding 3953767365](https://github.com/copeugne/mcpack/pull/23#discussion_r3953767365)
is valid. The original JSON normalization conflated NBT scalar widths and array
representations. The shared parser now has opt-in typed decoding that retains
every tag ID and list element type, including empty lists. Existing untyped
consumers keep their output. Generation projections use `typed-nbt-v2`, retain
compound-key canonicalization and the declared section/entity ordering, and keep
palette/index order. Missing block-entity fields remain distinct from empty lists.

The original r3 hashes and comparison remain retained as legacy normalized
results, not typed equality evidence. Read-only reprocessing of both restored
worlds is running under the corrected encoding. No world was regenerated.

Validation: 771 Item 7/8/10 tests pass, exercising shared-parser consumers. The
final focused projection suite passes 14 tests, including the separately added
float/double collision case. Ruff and parser/test type checks pass. The collision
regressions demonstrate equal untyped values with distinct typed digests for
integer widths, floating widths, array types and empty-list element types.

```sh
uv run --no-sync pytest -q tests/item7 tests/item8 tests/item10
uv run --no-sync pytest -q tests/item10/test_generation_projection.py
```

For typed reprocessing, use each restored r3 world and the same four declared
CLI selections, writing new files under `evidence/raw/item10/probe-pair-r3-typed`.
Require both comparison inputs to declare `generation_encoding=typed-nbt-v2`;
legacy and typed hash arrays are not comparable. Retain the resulting mismatch
records separately. This correction does not establish observer-free equivalence.

## Corrected typed r3 comparison

[Typed summary](scarecrow-probe-r3/typed-comparison.json) confirms complete matching
frames with the `typed-nbt-v2` encoding. Mismatches remain 3,969/3,969 Overworld,
960/961 Nether, 0/961 central End and 671/961 outer End. The corrected parser
therefore preserves the failed overall equality conclusion; observer causality
remains unproven. Legacy normalized results remain retained separately.

[The compressed evidence](scarecrow-probe-r3/typed-comparison.json.gz) contains
all eight reader data objects, every hash vector and every mismatch coordinate.
It is 516,390 bytes. Decompression matched the committed uncompressed SHA-256
and recovered eight inputs and four comparisons covering 6,852 chunks per member.
The summary also records each original CLI output hash. Compound-key ordering
inside this semantic bundle is canonical; regenerate original CLI byte formatting
with the reader when checking those per-input hashes.

[The bounded comparison script](scarecrow-probe-r3/compare-typed.py) rejects mixed
encodings and incomplete or duplicate coordinate frames before producing the
bundle. Reproduce the reader outputs from the previously verified nested r3 world
restores, with the following fixed selections and `--generation`:

| Output suffix | Dimension | Inclusive chunk bounds |
| --- | --- | --- |
| overworld | minecraft:overworld | -31 31 -31 31 |
| nether | minecraft:the_nether | -15 15 -15 15 |
| end-central | minecraft:the_end | -15 15 -15 15 |
| end-outer | minecraft:the_end | 81 111 -15 15 |

For each `MEMBER` equal to `probe` or `control`, use the existing reader invocation:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/probe-pair-r3-custody/world-scarecrow-MEMBER-r3/world evidence/raw/item10/probe-pair-r3-typed/MEMBER-SUFFIX.json --dimension DIMENSION --bounds MIN_X MAX_X MIN_Z MAX_Z --generation
uv run --no-sync python evidence/item-10/scarecrow-probe-r3/compare-typed.py
```

Replace the uppercase placeholders with the fixed member/table values. All eight
concrete reader invocations and the comparison script were executed. Output paths
must be absent; reproduce in a separate checkout to preserve the committed bundle.
No world generation, Item 8 audit or Item 11 workflow was rerun for this correction.

### Retained-world identity binding (PR23 second review)

The second review found that `compare-typed.py` checked the coordinate frame but
not the source region identities. The corrected derivation binds each probe and
control `world-backup.json` to its exact member hash and size in the published r3
archive manifest. Each reader's complete, unique region input map must then
match that world's dimension-specific region files and hashes. Missing,
duplicate, stale or substituted inputs fail before outputs are written.

Reprocessing all eight existing typed inputs with this check produced
byte-identical `typed-comparison.json` and `typed-comparison.json.gz`. No world
was regenerated and no accepted mismatch count changed. Five focused regressions
cover the accepted inputs, a wrong region hash, an omitted region, a duplicate
region and an altered world manifest:

```sh
uv run --no-sync pytest -q tests/item10/test_typed_comparison_identity.py
```

Focused Ruff checks pass. This standalone evidence script is checked with
`--ignore INP001` because its evidence directory is not a Python package.

### Coordinate inspection identity and acceptance (PR23 third review)

The third review found the same missing identity boundary in `inspect-writes.py`.
The corrected inspection invokes the existing retained-trace validator, binds the
world manifest to the published archive member, and verifies each consumed region
hash before and after decoding under the existing world lock. Unexpected external
chunks are rejected in this bounded inspection. Its JSON preserves observations,
including mismatches, and the process fails unless all 30 recorded block IDs match.

The real retained-world rerun passes with an unchanged result. Four regressions
reject changed trace bytes, world manifest bytes, region bytes and decoded block
IDs. They require the documented restored r3 world and skip explicitly if it is
unavailable. No raw world or previously accepted cross-check output was changed.

```sh
uv run --no-sync pytest -q tests/item10/test_write_corroboration.py tests/item10/test_retained_trace.py tests/item10/test_typed_comparison_identity.py
```

### Reviewed diagnostic delivery

PR23 merged as `eabc9ce30f731e9a3471267e09fff615293c1b26` on 2026-09-08.
Fetched `origin/main` contains reviewed head
`73f25aed57bcdc952ea6d65a1c93ae92ff8dc9b2`. The
[final review](https://github.com/copeugne/mcpack/pull/23#issuecomment-5578556110)
completed at 03:15:05 UTC with no new findings and a Codex bot thumbs-up on the
pull request. All four valid findings from earlier cycles were fixed. This
closes the bounded diagnostic delivery, not Item 10's full measurement gate.

## BetterEnd template collector extension (fixture gate only)

The existing Java probe now targets `NBTFeature.place`, `CrashedShipFeature.place`,
`BuildingListFeature$StructureInfo.getStructure` and the content-write call site
in `StructureTemplate.placeInWorld`. It records the actual returned template's
source path by object identity, feature attempt, template origin/pivot, rotation,
mirror, flags, content write arguments/results and template return/exception.
The ship route is attributed to `minecraft:end_city/ship`. A conflicting path for
one template object fails explicitly. Template success is not counted as a site.

Only the second of the retained template method's three direct `setBlock` sites
is traced: content placement. Temporary barriers and subsequent shape updates
are excluded. Calls outside targeted BetterEnd placements retain their original
interface invocation without emitting placement observations. Terrain merge and
ship erosion occur outside the template trace. Raw content writes remain evidence
of placement attempts, not proof that every block survives later erosion.

The extension reuses the original probe's explicit system-loader bridges and
existing test compiler/archive path. Focused validation compiles with pinned
Temurin `-Xlint:all -Werror`, transforms all four exact classes verified against
Item 8 artifact identities, and compares ordinary and instrumented fixture output
including world-call arguments. Cases cover normal, early return, empty template,
all refused writes, original exception propagation, isolated loader and an
unobserved template invocation. The selected source remains `original.nbt` even
when the fixture replaces the feature's mutable selection before placement.
The original scarecrow preservation cases still pass.

```sh
uv run --no-sync pytest -q tests/item10/test_placement_probe.py
uv run --no-sync ruff check tests/item10/test_placement_probe.py
uv run --no-sync basedpyright tests/item10/test_placement_probe.py
```

Both test functions pass; Ruff and the test's type check pass. Runtime transformed
class identity, installation completeness, real BetterEnd observations, trace
validation, saved-world corroboration and collector cost remain unverified.
No new server experiment or accepted nonregistry density result is supplied by
this fixture gate. Extend the existing diagnostic runner for a predeclared fresh
runtime check before incorporating these observations into Item 10 results.

### Incoming runtime class retention

During BetterEnd diagnostic r1, the three provider classes matched their retained
hashes, but the incoming Minecraft `StructureTemplate` hash was
`579560f5341cba7e3a23064fdc7d1938922dd14e18a1ca4ecab434f57379a2bd`,
instead of the packaged class hash
`f3fc7951f1e273e94e754ca4dc2ca9475d8b1eac24bcfb4ccd2d583e126e1121`.
This rejects r1's predeclared runtime identity gate. The exact cause is UNKNOWN
until the incoming bytes can be inspected; a hash alone cannot explain the change.

The probe now saves each incoming target class before transformation under its
trace-specific `.classes` directory. This is the smallest addition that makes
such a mismatch inspectable. The running r1 uses its already-built agent and is
unaffected; its missing incoming bytes cannot be recreated retrospectively.
An initial shared directory collided across fixture processes; trace-specific
paths fixed that defect. Both preservation fixtures pass, including checks that
retained incoming bytes match each emitted installation hash. No new runtime
identity has been accepted by this change.


## BetterEnd diagnostic milestone, current disposition

The shared template collector and optional lifecycle fixture commands are ready
for review as a diagnostic milestone. They do not close Item 10 or establish a
complete occurrence collector. Reuse these authoritative attempt records:

- [r1](betterend-probe-r1/README.md): no template placements; incoming class bytes
  were not retained, so its identity gate failed.
- [r2](betterend-identity-r2/README.md): retained and inspected patched class,
  no feature attempts in the small identity pilot.
- [r3](betterend-fixture-r3/README.md): fixture commands refused unloaded targets.
- [r4](betterend-fixture-r4/README.md): loading and fill succeed, feature refuses.
- [r5](betterend-ground-r5/README.md): actual ground matches the platform position.
- [r6](betterend-tags-r6/README.md): air check passes, terrain tag is unknown to
  command lookup. Retained source inspection distinguishes datagen definitions
  from runtime tag loading. The runtime registration/resource gap is unresolved.

Each raw diagnostic is durably archived with verified download and nested-world
restores. None supplies accepted BetterEnd occurrence counts. Synthetic probes
preserve original calls, arguments, return values, refusal and exception behavior;
real template writes and saved-world corroboration remain unexercised here.
Do not force a positive fixture by adding tags to the frozen baseline. Resolve
runtime availability and the affected inventory assumptions before accepting
counts or revising the full sampling gate. No Item 8/9 general audit was repeated.

Validation for the current candidate:

```sh
uv run --no-sync pytest -q tests/item7 tests/item10
uv run --no-sync ruff check src/mcpack_evidence/item7_lifecycle.py tests/item10/test_placement_probe.py tests/item7/test_worldgen_lifecycle.py tools/run_item10_probe.py tools/run_item7_worldgen.py
uv run --no-sync basedpyright src/mcpack_evidence/item7_lifecycle.py tests/item10/test_placement_probe.py tests/item7/test_worldgen_lifecycle.py tools/run_item10_probe.py tools/run_item7_worldgen.py
```

All 296 tests pass (42.40 seconds); changed Python lint, formatting and type
checks pass. No Item 11 workflow was implemented, run, repaired or linted.


### Reviewed diagnostic delivery

[PR24](https://github.com/copeugne/mcpack/pull/24) merged on 2026-09-08 as
`a96a2cbad752ca0023058b39c122c66ffa4370ec`. Fetched `origin/main` contains
that merge and reviewed head `d38099feffee9281abc947b3434557943751db5d`.
The [clean review](https://github.com/copeugne/mcpack/pull/24#issuecomment-5579244068)
completed at 04:30:11 UTC, returned a thumbs-up, and introduced no inline,
review or discussion findings. This delivers the bounded diagnostic only.
Full Item 10 occurrence coverage, measurement and final acceptance remain open.


## Anomaly and monolith direct-write extension

The accepted Item 8 `bop-feature-scope` disassemblies show both providers'
setBlock helpers calling Feature.setBlock and returning true after that void
call, regardless of the underlying world's result. The exact Minecraft helper
calls LevelWriter.setBlock with flags 3 and discards its boolean. Counting the
outer helper return would therefore misclassify refused writes.

The existing probe now brackets each provider's place method with the existing
feature/attempt events. It wraps the one direct write in the shared Minecraft
helper, recording writes only during those two feature classes. Outside that
scope it invokes the same LevelWriter interface method without a write event.
The helper's original POP still discards the unchanged boolean. Provider methods,
random draws, replacement predicates and feature-return behavior remain in place.
Incoming bytes and installation records use the existing retention path.

The shared helper is touched because both current consumers discard the needed
result; no second collector or generalized event framework is introduced.
The new call adds observer overhead even outside target attempts. Measure that
cost before full sampling, and inspect the actual incoming helper class before
acceptance. Synthetic preservation does not prove observer-free world equivalence.

The existing probe test command now passes three tests, covering both new
providers in normal, early-return, all-refused, exceptional, isolated-loader and
outside-target cases. Original and observed stdout include complete argument
sequences and match. Exact retained BOP classes and the hash-verified Minecraft
helper transform successfully. Changed test lint and type checks pass. No live
run or accepted occurrence count is supplied by this implementation milestone.


### Anomaly direct final-write coverage correction

Before live collection, inspection of accepted AnomalyFeature.place found its
additional direct WorldGenLevel.setBlock call at bytecode offset 938 (flags 2),
which places the final anomaly blocks outside Feature.setBlock. The initial
shared-helper extension did not capture it. No live evidence used that version.
The probe now requires and wraps this one extra call site with its existing
write bridge. The synthetic anomaly case adds a flags-2 write after its three
helper writes; normal, refusal and exception comparisons retain the distinction.
Exact retained-class transformation checks now require this call as well.


### BOP positive fixture validation

[BOP fixture r1](bop-fixture-r1/README.md) retains the live capture, incoming
class identity, raw/world custody, complete trace validation and saved-block
corroboration. All 22,769 writes match saved block IDs. This includes writes in
partially generated neighbors, explicitly excluded from full-chunk density
exposure. The artificial fixture is not a density sample. Both supported BOP
writers now have positive capture evidence; other mechanism coverage and
observer cost still gate full sampling.


## Monster Box generator extension

Reuse the accepted [generator identity](../item-8/sources/quark-landmark-encounter-generators/identities.json)
and frozen Monster Box interpretation. The retained generateChunk method returns
void and its single WorldGenRegion.setBlock call (offset 122, flags 0) discards
the actual boolean. The existing collector now brackets this exact method,
records the actual write result, and emits generator_end without inventing a
boolean return. Early normal returns, refused writes and exceptional incomplete
attempts remain distinct. The anchor is the passed generator chunk position;
actual block coordinates come from write records, not that anchor.

The existing fixtures now cover this fourth collector test: normal, early,
refused, exceptional, isolated-loader and outside-method execution preserve
stdout and complete world-call arguments. The exact retained Quark archive and
MonsterBoxGenerator class hashes are checked before transformation. All four
collector tests pass in 7.78 seconds; changed-test Ruff and basedpyright pass.
No live run or accepted occurrence count is supplied. The collection consumer
must support generator_end and count successful monster-box writes under the
frozen at-most-one-write-per-chunk setting; a completed void call is not success.
Fairy-ring delegated flower writes remain separate missing coverage. No frozen
configuration or random draw is changed by this extension.


## Nether obsidian spike static-writer extension

Reuse [the accepted spike source](../item-8/sources/quark-nether-spikes/identities.json).
ObsidianSpikeGenerator.placeSpikeAt is a static void method with seven direct
WorldGenRegion.setBlock call sites, all flags 0. The existing generator hook now
accepts its class identity and brackets that placement method. It captures every
actual write result without substituting the discarded booleans or changing the
original method return. The passed placement position is the anchor; individual
writes retain their own coordinates. One call is a placement attempt, not seven
locations. Outer generateChunk calls which never invoke this method are outside
this trace population. Spawner/chest block-entity configuration is unchanged and
not separately observed by these block-write hooks.

The existing fixtures cover all seven sites, refused writes, early returns,
exceptions, isolated classloading and calls outside the selected method. The
exact Quark archive and retained class hashes are checked before transformation.
All five collector tests pass in 9.46 seconds; changed-test Ruff and basedpyright
pass. This implementation adds no server commands or experiment. Live positive
capture, incoming runtime identity, trace validation and saved-block corroboration
remain required before this contribution can enter full sampling.

## Spiral spire source/part hook

The existing collector now brackets SpiralSpireGenerator.generateChunkPart,
recording the source in begin.origin and the destination chunk in a part event.
Its two delegated makeSpike write sites use a scoped bridge; direct calls outside
the outer attempt invoke the original WorldGenRegion method without tracing.
This extra bridge is required because the writer is public and distinct from
the source boundary. Treating its direct calls as complete source observations
or throwing outside an active attempt would change behavior. No new collector
framework was introduced.

All 341 Item 7/10 tests pass on the final candidate in 61.55 seconds.
The spiral fixture covers normal, early, refused, exceptional, isolated-loader,
outside and outside-exception cases. Original stdout includes complete write
arguments and terminal outcomes; observed stdout matches. Traced write results
match the fixture refusal setting. Three completed chunk attempts
retain two source keys, with separate raw attempts and no fabricated boolean
generator result. The exact retained Quark archive and SpiralSpireGenerator
class are hash-checked and transform successfully. Class SHA-256:
`dd57fdac61e67cece06adc078a4538e3949573baff8f65df9819218bd282b771`.
Reproduce with `uv run --no-sync pytest tests/item10/test_placement_probe.py -q`.
Changed-test Ruff and basedpyright pass. This is synthetic collector acceptance
only. A predeclared fresh pilot, mixed-trace reader integration and saved-block
corroboration remain necessary before accepting natural spiral occurrences.

## Fairy-ring direct and delegated content hook

The collector now brackets the exact static spawnFairyRing method. A writer
event identifies each of its four direct call sites: 1 cleanup, 2 surface copy,
3 ore center, 4 ore neighbor. The following write retains the original returned
boolean. Cleanup success is not construction success. The one delegated flower
call records origin, actual return or exception, and the caller's existing third
getBlockState result records flower_state. No additional world read is inserted.
The entire delegated footprint is not captured; this records the requested
origin content and direct ring/deposit writes only, as predeclared.

All 342 Item 7/10 tests pass in 64.32 seconds, including seven focused collector
tests. The new fixture confirms
false-with-content and true-with-air stay distinct, refused writes retain false,
early exits retain no writes, direct/delegated exceptions survive, and isolated
loading preserves calls. Original/observed stdout matches complete write arguments
and the five-read count. The first test run rejected an incorrect expected string
for the fixture's BlockState record; correcting that assertion required no
collector change. Changed-test Ruff and basedpyright pass.

The retained Quark archive is hash-checked and the exact FairyRingGenerator
class transforms successfully, with four writes, five reads and one delegated
call required. Retained packaged class SHA-256:
`3a30145aaad2e116ab762a6c090659a3f02f125dfd98972c3df72f4319691a74`.
Reproduce with `uv run --no-sync pytest tests/item10/test_placement_probe.py -q`.
A natural pilot and raw-reader integration remain pending. No natural fairy-ring
occurrences or density estimates are accepted by these synthetic checks.

## Cave urn callback and direct-write capture

The existing probe now wraps the configured-feature invocation in
`PlacedFeature.lambda$placeWithContext$4`, after placement modifiers choose each
origin. It identifies `supplementaries:urns_patch` through the world's configured
feature registry, retains the calling placed-feature registry key (or null when
unavailable), and brackets the original invocation without a new context stack.
This implements the [declared urn boundary](protocol.md#cave-urn-occurrence-boundary)
using two hooks. No separate RandomPatchFeature transformation is necessary.

The SimpleBlockFeature write wrapper records the actual flags-2 result only
inside the traced urn attempt. Unrelated writes invoke the original method.
A refused write and the caller's true return remain separate observations.
Thrown target exceptions retain their original cause, produce an
`attempt_exception` record and clear the completed exceptional attempt so a later
patch can be recorded. Parent keys do not become additional occurrences.
Non-cave and null-parent observations remain distinguishable from the standalone
cave population. Overlapping writes and saved-content acceptance remain pending.

Validation commands:

```sh
uv run --no-sync pytest -q tests/item10 tests/item7
uv run --no-sync pytest -q tests/item10/test_placement_probe.py -k urn
uv run --no-sync ruff check tests/item10/test_placement_probe.py
uv run --no-sync basedpyright tests/item10/test_placement_probe.py
```

All 360 Item 7/10 tests passed in 73.01 seconds. After tightening the callback's
static/context signature check, all eight affected urn tests passed in 7.75
seconds. Focused lint and type checks pass; initial formatting and JSON typing
findings were fixed. The tests compile with pinned Temurin and `-Xlint:all -Werror`.
They compare uninstrumented and observed return values, exceptions and complete
write arguments for normal, refused, exceptional-then-recovery, non-cave,
absent-parent, unrelated-patch and isolated-loader cases. The final test verifies
the retained archive/class hashes and transforms both exact classes. This is
collector preparation, not a positive runtime capture or urn density result.
No server experiment or Item 11 workflow ran in this batch.
