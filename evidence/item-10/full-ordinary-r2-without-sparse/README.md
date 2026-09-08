# Ordinary repetition-2 without-Sparse control

Status: GENERATED, CONFIGURATION VERIFIED, RAW CUSTODY VERIFIED. Full census
acceptance remains pending. Protocol: `item10-full-v1`; seed: `42`.
Generation source: `6747b6b1470b6e90a168fdec89a996b9f419d889`.

The unchanged [run receipt](run.json) records all eleven completed selections,
readiness, correlated save flush and clean stop with Java exit 0 after 561.808
seconds. Its complete `run.preflight`, `probe` and lifecycle `selections` objects
equal those in the [first control](../full-ordinary-r1-without-sparse/run.json).
This verifies the same seed, retained source, declared omission, frozen identities
and observer. Repetition is 2 and the instance was fresh. All 228 frozen files and
eleven declared Chunky files pass configuration capture. The console retains 355
invalid-air-item diagnostics, the same count as the first control; raw context is
preserved, not treated as gameplay or loot validation.

## Raw custody

The stopped world backup contains 504 files totaling 434,640,568 bytes.
`world.tar.gz` is 170,090,793 bytes, SHA-256
`369132c89161ec00228c4b9d1376474fb83f62559523280557405c098863b780`.
The [world restore](world-restore.json) verified all 504 files into a new world.

The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-ordinary-r2-without-sparse-6747b6b1)
contains the outer archive and [manifest](archive-manifest.json). The fetched tag
resolves to the exact generation source above. Archive size is 170,501,208 bytes,
SHA-256 `0f65280924909cbde74146c0acfebd44fdf79ce7c404f0431f54d3aa6d19b287`;
313 files total 194,331,412 uncompressed bytes. Both [local](local-restore.json)
and [downloaded](download-restore.json) restores verified all members, and the
downloaded manifest matches byte-for-byte. No server was restarted for these
offline restore checks. This is custody, not Item 10 completion.

## Reproduction

The existing [first-control procedure](../full-ordinary-r1-without-sparse/README.md#reproduction)
applies with this run name, revision, archive and world hash. Create destination
parents first; every output must be absent. Executed generation and archive:

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-ordinary-r2-without-sparse --mode probe --preset item10 --role ordinary --arm without-sparse --repetition 2
uv run --no-sync python -m tools.archive_item7_evidence create --root evidence/raw/item10/full-ordinary-r2-without-sparse --archive evidence/raw/item10/item10-full-ordinary-r2-without-sparse-6747b6b1.tar.gz --manifest evidence/item-10/full-ordinary-r2-without-sparse/archive-manifest.json --revision 6747b6b1470b6e90a168fdec89a996b9f419d889
```

Full analysis is running on the restored world with this command:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-ordinary-r2-without-sparse-custody/restored-world/world evidence/raw/item10/full-ordinary-r2-without-sparse-analysis/all-strata.json --all-strata --dimension-geometry evidence/item-10/dimension-geometry.json --trace-root evidence/raw/item10/full-ordinary-r2-without-sparse-custody/restored-local --trace-manifest evidence/item-10/full-ordinary-r2-without-sparse/archive-manifest.json
```

Timing/diagnostics are beside the output in `all-strata-runtime.txt`. Full class,
chunk, location, exclusion and repetition-comparison acceptance remain pending.
