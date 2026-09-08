# Nonregistry placement probe diagnostic

Status: SYNTHETIC VALIDATION ONLY. No Minecraft generation run has used this
probe, and no nonregistry density is accepted from it.

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
