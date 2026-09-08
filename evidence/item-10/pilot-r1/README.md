# Fresh registry diagnostic

The predeclared r1 attempt failed before Java launch: `/usr/bin/time` was absent
(exit 127). Its ignored raw output directory is retained. No world was created.
The corrected command uses Bash timing and fresh `pilot-r2` paths, with identical
seed, generation preset and census bounds. Run from the repository root:

```sh
bash evidence/item-10/pilot-r1/run.sh
```

Source code and predeclaration revision: `5f9ef4af`. The script is preserved here
with the corrected invocation; r1's failed invocation was the same command
preceded by `/usr/bin/time -p -o evidence/raw/item10/pilot-r1/time.txt` instead of
Bash timing. Results and verified custody follow below.

## Result and limits

The corrected r2 run completed under source/predeclaration revision
`5f9ef4af72ce780640984a2051e638aa2f0bf882`. [Run receipt](run-r2.json)
records the frozen runtime/configuration identity, readiness, all four generation
selections, correlated save confirmation, clean stop and exit 0. Lifecycle time
was 258.153 seconds; Bash elapsed time was 260.046 seconds. The stopped world
occupied 127,167,697 bytes before backup. These costs describe this diagnostic,
not a prediction of full-baseline runtime.

[Registry census](registry-census.json) accepted all 3,969 selected full Overworld
chunks, with 24 registry starts: 6.046863189720333 starts per 1,000 chunks.
The other three generated selections are retained but excluded from this
predeclared denominator. This does not count all canonical families, nonregistry
features, actionable locations or actual combat. It does not establish exploration
pacing, representativeness across seeds, or Item 10 completion.

## Reproduction and custody

After generation and clean shutdown:

```sh
uv run --no-sync python -m tools.analyze_structure_density instances/item10/pilot-r2/world evidence/raw/item10/pilot-r2/registry-census.json --dimension minecraft:overworld --bounds -31 31 -31 31
uv run --no-sync python -m tools.manage_item4_environment backup --world instances/item10/pilot-r2/world --archive evidence/raw/item10/pilot-r2/world.tar.gz --receipt evidence/item-10/pilot-r1/world-backup.json
```

[World backup receipt](world-backup.json) hashes 158 files and excludes
`session.lock`. [Archive manifest](archive-manifest.json) covers 243 raw files,
including that backup, logs, captured configuration, timing and original census.
The immutable archive is 75,841,389 bytes, SHA-256
`4b554017bd8fe320cff91d0a9b69290d8d4822a86417e2fdecc50531749e036d`.
The [release](https://github.com/copeugne/mcpack/releases/tag/item-10-pilot-raw-2026-09-08-r1)
retains the archive and manifest; [release metadata](release.json) records assets.
The fetched release tag resolves to the full source revision above.

[Local restore](local-restore.json) and [download restore](download-restore.json)
verified every archive member. [Nested world restore](world-restore.json) restored
all 158 world files. Running the census against the restored `world` with the same
dimension and bounds produced byte-identical JSON, checked with `cmp` against
`registry-census.json`. Commands for restoring downloaded evidence into absent
paths, from the repository root:

```sh
gh release download item-10-pilot-raw-2026-09-08-r1 --repo copeugne/mcpack --dir RESTORE_INPUT
uv run --no-sync python -m tools.archive_item7_evidence restore --archive RESTORE_INPUT/item10-pilot-r2-5f9ef4af.tar.gz --manifest evidence/item-10/pilot-r1/archive-manifest.json --target RESTORED_RAW --receipt RESTORE_RECEIPT.json
uv run --no-sync python -m tools.manage_item4_environment restore --archive RESTORED_RAW/world.tar.gz --sha256 cd08d41dc64f86950e50380a0c37c2486f3de8bdc6b859c78ef3b6952f654e9f --target RESTORED_WORLD
uv run --no-sync python -m tools.analyze_structure_density RESTORED_WORLD/world RESTORED_CENSUS.json --dimension minecraft:overworld --bounds -31 31 -31 31
cmp evidence/item-10/pilot-r1/registry-census.json RESTORED_CENSUS.json
```

The initial outer manifest mistakenly received an incorrect revision argument.
It was rejected before publication and corrected against `git rev-parse HEAD`;
archive contents and hash were unchanged. The rejected metadata remains locally
at `evidence/raw/item10/pilot-custody-r1/rejected-wrong-revision-manifest.json`.
No accepted measurement uses that revision. The prelaunch timer failure above
and this metadata correction do not become successful experiment observations.
