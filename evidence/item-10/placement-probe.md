# Nonregistry placement probe diagnostic

Status: REAL-RUN VALIDATION INCOMPLETE. r1 had no target execution; r2
was rejected after a reproduced helper classloader failure. No nonregistry
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
