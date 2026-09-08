# Natural urn diagnostic r1

The [predeclared fixed-frame diagnostic](../protocol.md#bounded-urn-diagnostic-r1)
ran at source `cf3a990d2b71c081d2e0f5ea38da4a78830d68ed`. The
[run record](diagnostic.json) binds the fresh frozen materialization, source/JAR
identity and lifecycle. All four 81-chunk selections completed, followed by the
correlated save and clean exit 0 in 89.42 seconds. No process-group kill occurred.

## Raw observation and limits

The trace contains 1,074 urn patch attempts, all with parent
`supplementaries:cave_urns`, and 161 successful urn writes across 87 attempts.
There are no recorded refused urn writes or urn exceptions. The complete mixed
trace ends with zero unfinished attempts. These are raw capture totals, including
halo activity, not selected-area densities or accepted distinct cache counts.
Archive-bound trace validation and saved-block corroboration are recorded below.
Selected-area occurrence acceptance remains open. Do not expand the sample or infer zeroes outside its observed scope.

Trace size is 451,228 bytes, SHA-256
`28411caa562664358a3cf07ede1716eb7cfedd1a83eb4a5777574f7c7a3b2d88`.
Reproduce the raw urn totals after the verified restore below:

```sh
uv run --no-sync python - <<'PY'
import json
from pathlib import Path
raw = Path('evidence/raw/item10/urn-pilot-r1-custody/restored')
rows = [json.loads(line) for line in (raw / 'trace.jsonl').read_text().splitlines()]
parents = [row for row in rows if row['kind'] == 'urn_parent']
ids = {row['attempt'] for row in parents}
writes = [row for row in rows if row['kind'] == 'write' and row['attempt'] in ids]
print(len(parents), len(writes), len({row['attempt'] for row in writes}))
print({row['placed_feature'] for row in parents}, {row['returned'] for row in writes})
PY
```

SimpleBlockFeature's incoming class matches its declared SHA-256
`17907c21c8e522ac39fa9dcc838dd8f4afdcd7bcfc200480b14187b7a01875e2`.
PlacedFeature's incoming SHA-256 is
`335b4b632313b226e57104600197b10522757e325598314111342071ed27fc32`.
It differs from the bare retained class and is preserved at
`trace.jsonl.classes/net/minecraft/world/level/levelgen/placement/PlacedFeature.class`.
Pinned `javap -c -p` inspection shows Structure Essentials' outer timing redirects;
`lambda$placeWithContext$4` still loads context local 1, calls getLevel at 2,
generator at 6, ConfiguredFeature.place at 12, and branches on that result at 15.
The probe's matching callback was therefore present in the actual incoming class.
This is an explicit identity disposition, not a claim that the bare class was loaded
or that observer overhead is negligible. Both incoming classes are archive-bound.

## Raw custody and reproduction

[Archive manifest](archive-manifest.json) binds 264 files, 7,658,499 uncompressed
bytes. The immutable archive `item10-urn-pilot-r1-cf3a990d.tar.gz` is 5,600,750
bytes, SHA-256 `e7527fc76aed6add71948994c054a7f9824524fe0e34b5377ac9483d9140229c`.
The [release](https://github.com/copeugne/mcpack/releases/tag/item-10-urn-pilot-2026-09-08-r1)
retains archive and manifest; the fetched tag resolves to the exact source above.
The downloaded manifest matches byte for byte. [Download restore](download-restore.json)
verified every raw member with the existing archive tool.

[World backup](world-backup.json) binds 103 files and nested archive SHA-256
`6c4ce1dad08eb383ec37c54a035dd0328b692dfc330f55a5d306533a0a79ff3a`.
[World restore](world-restore.json) succeeded. Every sorted restored path, size and
SHA-256 matched the backup's world_files list without booting. session.lock is
excluded. Reproduce into absent paths using the existing tools:

```sh
gh release download item-10-urn-pilot-2026-09-08-r1 --dir DOWNLOAD
uv run --no-sync python -m tools.archive_item7_evidence restore --archive DOWNLOAD/item10-urn-pilot-r1-cf3a990d.tar.gz --manifest evidence/item-10/urn-pilot-r1/archive-manifest.json --target RESTORED_RAW --receipt RESTORE_RECEIPT.json
uv run --no-sync python -m tools.manage_item4_environment restore --archive RESTORED_RAW/world.tar.gz --sha256 6c4ce1dad08eb383ec37c54a035dd0328b692dfc330f55a5d306533a0a79ff3a --target RESTORED_WORLD
```

Local custody uses `evidence/raw/item10/urn-pilot-r1-custody/` with `downloaded`,
`restored` and `restored-world` children. The instance is stopped and preserved.
Collector preparation passed 360 Item 7/10 tests and eight affected urn tests
as recorded in the [probe report](../placement-probe.md#cave-urn-callback-and-direct-write-capture).
This batch adds actual raw capture and verified custody. The subsequent block-ID corroboration below passes; this does not complete Item 10. No Item 11 workflow ran.

## Archive-bound capture and saved-block corroboration

[Trace validation](trace-validation.json) passes with the retained incoming
identities. It requires one parent event before each urn result, flags 2, an urn
block ID, at most nine direct writes within the declared patch spread, and a
return consistent with writer attempts. It preserves the difference between a
refused write and the helper's true return. This bounded successful diagnostic
contains no exceptional attempts; unhandled failure events remain rejected rather
than silently accepted. The mixed zero-write spiral parts remain intact.

[Write corroboration](write-corroboration.json) verifies all 429 mixed-trace
successful coordinates against archive-bound saved region files. All block IDs
match. The urn subset has 161 writes at 161 distinct coordinates across 87
successful patch attempts, with no repeated written coordinates. Urn writes are
in 108 full, 51 initialize_light and two carvers chunk states. Partial chunks and
halo observations do not become density denominators. Full block-state equality,
observer-free equivalence and selected-area cache density are not established.

Reproduce from the previously verified local restores:

```sh
uv run --no-sync python -m tools.validate_item10_trace --urn-r1 evidence/raw/item10/urn-pilot-r1-custody/restored
PYTHONPATH=. uv run --no-sync python evidence/item-10/scarecrow-probe-r3/inspect-writes.py --urn-r1
```

The initial direct script invocation omitted `PYTHONPATH=.` and failed to import
`tools`; no inspection occurred in that attempt. The corrected existing invocation
above completed. Negative tests cover absent, duplicate or malformed parents,
wrong flags/block/coordinates, inconsistent returns, and changed trace, world
manifest, region or saved block. All five prior feature trace reports reproduce
unchanged. No new raw archive was created for this deterministic reader extension.

Validation: all 371 Item 7/10 tests passed in 74.50 seconds. After removing the
redundant mixed-attempt list from the urn-only summary, its four affected integrity
regressions passed in 3.21 seconds and the real inspector reproduced the result.
The immutable trace remains the per-attempt authority; the summary retains all
161 urn observations and the 987 zero-successful-write patch attempts as a count.
Changed trace-reader and test Ruff/basedpyright checks pass. Initial lint/type
findings were corrected before these results. No Item 11 workflow ran.
