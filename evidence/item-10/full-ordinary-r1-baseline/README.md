# First full ordinary baseline

Status: GENERATED, CONFIGURATION REVALIDATED, RAW CUSTODY VERIFIED; census and location
acceptance remain pending. Generation source: `7b977af6`. Seed: `42`.

The original [run receipt](run.json) is preserved unchanged. All eleven declared
generation selections finished, the correlated flush passed, and Java exited
cleanly with code 0 after 497.453 seconds. This is 46,475 requested generation
chunks, not yet proof of the 45,056 selected saved-chunk denominator.

The harness then rejected configuration capture because its Item 7 default
allowlist included only three dimension task files. The exact difference was
the seven Chunky task files for Aether and the six Creating Space dimensions.
No frozen configuration file was missing. The capture boundary now derives the
full allowlist from the already-fixed Item 10 selections; Item 7 defaults and
explicit single-dimension overrides remain unchanged. It still rejects missing
or unexplained files and semantic drift in all 228 frozen files.

[Configuration revalidation](configuration-revalidation.json) accepts the stopped
instance. Its new sanitized capture matches all 239 original captured files
byte-for-byte: 228 frozen files plus 11 Chunky files. The original rejection was
not rewritten, the configuration was not tuned, and the world was not regenerated.
Focused validation: `uv run --no-sync pytest -q
tests/item7/test_worldgen_config_capture.py tests/item7/test_worldgen_lifecycle.py
tests/item10/test_collection_runner.py` (37 passed); focused Ruff and type checks
also pass. Negative cases retain rejection of a missing task or unexplained file.

## Revalidation command

The following executed command requires the preserved stopped instance and an
absent `config-revalidation` output. Do not overwrite the retained outputs.

```sh
uv run --no-sync python - <<'PY'
import json
from pathlib import Path
from mcpack_evidence.item7_config import capture_runtime_configuration
from mcpack_evidence.item7_runtime import WorldgenRequest, sha256_file
from mcpack_evidence.item7_selections import ITEM10_SELECTIONS
raw = Path('evidence/raw/item10/full-ordinary-r1-baseline')
request = WorldgenRequest(
    pristine=Path('instances/pristine-baseline-v0'),
    artifact_manifest=Path('evidence/item-3/artifact-acquisition-manifest.json'),
    retained_manifest=Path('evidence/item-3/runtime/retained-server-candidates.txt'),
    seed_suite=Path('test-environment/seed-suite.json'),
    frozen_config=Path('evidence/item-6/frozen'),
    frozen_manifest=Path('evidence/item-6/generated-config-manifest.json'),
    config_audit=Path('evidence/item-6/config-audit.json'),
    java_home=Path('downloads/item2/temurin/extracted/jdk-21.0.12.1+1'),
    role='ordinary', target=Path('instances/item10/full-ordinary-r1-baseline'),
    log_path=raw/'console.log', captured_config=raw/'config-revalidation/captured-config',
    mode='item10', selections=ITEM10_SELECTIONS, timeout_seconds=14400,
)
receipt = capture_runtime_configuration(request)
original = {p.relative_to(raw/'captured-config').as_posix(): sha256_file(p)
            for p in (raw/'captured-config').rglob('*') if p.is_file()}
new = {p.relative_to(request.captured_config).as_posix(): sha256_file(p)
       for p in request.captured_config.rglob('*') if p.is_file()}
assert original == new
result = {'original_diagnostic_sha256': sha256_file(raw/'diagnostic.json'),
          'unchanged_captured_files': len(original), 'configuration': receipt.model_dump()}
with (raw/'configuration-revalidation.json').open('x') as output:
    json.dump(result, output, indent=2)
    output.write('\n')
PY
```

The initial direct trace pass finds 50 incoming classes, 28,908 complete attempts
and 108,596 write events. These are raw attempt/write counts, not location counts.
World backup completed with 503 files totaling 428,092,106 bytes; its archive is
162,363,995 bytes with SHA-256
`3aa87e98bf90e00aaa20101412d429c2b163b36a0bff45aee51f42164b6c4580`.
Trace size is 22,100,158 bytes. Complete saved-world analysis must pass before
another world starts.

## Durable raw custody

The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-ordinary-r1-baseline-aa409114)
retains `item10-full-ordinary-r1-baseline-aa409114.tar.gz` and its
[committed manifest](archive-manifest.json). The tag binds
`aa4091143b26698347731fb1181efd12d50336ed`, which contains the narrow configuration
correction; the unchanged run receipt separately binds generation source `7b977af6`.
Archive SHA-256 is
`76e53df7a6a9cf43e1ace97b1670e63492b95cbcb1d1ab83a4f71dcb9b4959a8`.
It contains 554 files totaling 187,391,532 uncompressed bytes; archive size is
162,883,215 bytes. Both the [local restore](local-restore.json) and
[downloaded restore](download-restore.json) verified all members. The downloaded
manifest matches the committed manifest byte-for-byte. The nested
[world restore](world-restore.json) restored all 503 world files from the verified
world archive. No server was restarted during these checks.

The first local restore invocation failed before extraction because the custody
parent directory was absent. Creating that parent and retrying succeeded. An
attempt to use `/usr/bin/time` for analysis also stopped before analysis because
that optional executable is absent; the shell's existing `time` keyword is used.
Neither preparation failure modified the retained raw archive or world.

Executed archive command:

```sh
uv run --no-sync python -m tools.archive_item7_evidence create --root evidence/raw/item10/full-ordinary-r1-baseline --archive evidence/raw/item10/item10-full-ordinary-r1-baseline-aa409114.tar.gz --manifest evidence/item-10/full-ordinary-r1-baseline/archive-manifest.json --revision aa4091143b26698347731fb1181efd12d50336ed
```

Download into a new directory with `gh release download
item10-full-ordinary-r1-baseline-aa409114 --repo copeugne/mcpack --dir DOWNLOAD`.
Then use the existing archive restore command with that archive, the committed
manifest, an absent restore target and an absent receipt path. Create the target
parent first. The world restore uses the nested `world.tar.gz` and the world
SHA-256 above, through `tools.manage_item4_environment restore`.

The first full offline analysis completed against the restored world in
3 minutes 28.539 seconds (shell `time`). All 4,096 selected Overworld chunks
passed complete-census validation. There are 24 registry starts and 931 observed
nonregistry locations: 94 Quark monster boxes and 837 cave urn caches. Combined
classification gives 955 locations: T0 8, C 1, T1 939, T2 7, T3 0, T4 0, with
one village. These are provisional location categories, not observed fights.
The full output is 79,299,838 bytes, SHA-256
`bef29dfa0bcf52392edd4ae9b96d1425f395f658d5e109702d77a36c9bad1c8c`.
Its command and durable raw inputs reproduce this derived result; the other ten
strata remain unaccepted.

The `nonregistry_candidates` object alone serializes to 68,411,635 bytes with
`json.dumps(value, indent=2)`. It contains whole-world observations despite the
single-stratum census. Repeating the same capture processing and storing that
object in every stratum is unnecessary. The next analysis integration will reuse
one whole-world nonregistry result across all eleven existing census calls,
preserving this completed Overworld result as a comparison. This changes neither
the sample nor occurrence rules and does not require a new world experiment.

The first all-strata analysis failed after 7m46.709s (user 7m41.868s,
system 0m1.236s) during classification with `observed registry start is outside
accepted active families: aether:large_aercloud`. The diagnostic is retained at
`evidence/raw/item10/full-ordinary-r1-baseline-analysis/all-strata-runtime.txt`.
No result JSON was produced. This is an integration defect: Item 8's hash-bound
`other_registry_groups["aether:large_aercloud"].grouping_decision` already explicitly
excludes the root as a terrain/cloud block formation. It is not evidence that the
accepted family inventory or classification needs to be repeated.

The existing classifier now preserves these raw starts in the census and retains
their exact Item 8 disposition in `classification.excluded_registry_occurrences`.
They do not enter authored-location category counts or spatial summaries.
Unknown roots and roots dispositioned as inactive still reject classification;
the regression includes the inactive Small Nether Dungeon. All other attribution
rules remain unchanged. The shared full-world path requires all 50 observer
classes and preserves one whole-world observation object with per-stratum
classification and spatial results. Focused validation passes 59 tests with
`uv run --no-sync pytest -q tests/item10/test_full_world_census.py
tests/item10/test_density_census.py tests/item10/test_density_spatial.py
tests/item10/test_collection_trace.py`; scoped Ruff and changed-test type checks
pass. The corrected full analysis is pending; this is not first-world acceptance.

Full analysis command (uses the same restored raw inputs; output must be absent):

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-ordinary-r1-baseline-custody/restored-world/world evidence/raw/item10/full-ordinary-r1-baseline-analysis/all-strata.json --all-strata --dimension-geometry evidence/item-10/dimension-geometry.json --trace-root evidence/raw/item10/full-ordinary-r1-baseline-custody/restored-local --trace-manifest evidence/item-10/full-ordinary-r1-baseline/archive-manifest.json
```

Executed command:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-ordinary-r1-baseline-custody/restored-world/world evidence/raw/item10/full-ordinary-r1-baseline-analysis/overworld.json --dimension minecraft:overworld --bounds -32 31 -32 31 --dimension-geometry evidence/item-10/dimension-geometry.json --classify --spatial --biomes --trace-root evidence/raw/item10/full-ordinary-r1-baseline-custody/restored-local --trace-manifest evidence/item-10/full-ordinary-r1-baseline/archive-manifest.json --require-complete-observer
```
