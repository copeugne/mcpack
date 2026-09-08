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
