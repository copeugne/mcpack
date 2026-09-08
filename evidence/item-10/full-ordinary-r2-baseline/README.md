# Ordinary repetition-2 baseline

Status: GENERATED, CONFIGURATION VERIFIED, RAW CUSTODY VERIFIED. Census acceptance
remains pending. Protocol: `item10-full-v1`; seed: `42`.
Generation source: `004b1724a3242c0bf8fc9faf43e4b4e4f37dc23e`.

The unchanged [run receipt](run.json) records all eleven selections completed,
readiness, correlated save flush and clean stop with Java exit 0 after 513.589
seconds. Its entire `run.preflight`, `probe` and lifecycle `selections` objects
equal the [first baseline](../full-ordinary-r1-baseline/run.json), with repetition
2 and a fresh instance. All 228 frozen files and eleven declared Chunky files
pass capture. The console retains 300 invalid-air-item diagnostics, matching the
first baseline's count. Raw log context remains preserved; this is not loot or
gameplay validation. The original first-baseline capture rejection and subsequent
revalidation remain separately documented, not rewritten.

## Raw custody

The stopped world backup contains 503 files totaling 427,985,630 bytes.
`world.tar.gz` is 162,071,075 bytes, SHA-256
`b13e992bc23b96c4d6e382b4103185ac85953cab7e912a8fa3fa910a0d8fc61a`.
The [world restore](world-restore.json) verified all 503 files into a new world.

The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-ordinary-r2-baseline-004b1724)
contains the outer archive and [manifest](archive-manifest.json). The fetched tag
resolves to the exact generation source above. Archive size is 162,552,858 bytes,
SHA-256 `86207dadba050cb1f5ec00ba618d2847b614d19d463860693a306d9782d722c6`;
313 files total 190,621,130 uncompressed bytes. Both [local](local-restore.json)
and [downloaded](download-restore.json) restores verified all members, and the
downloaded manifest matches byte-for-byte. No server restart was required for
these offline restore checks. This is custody, not Item 10 completion.

## Reproduction

Use the existing [custody procedure](../full-ordinary-r1-without-sparse/README.md#reproduction)
with this name, revision, archive and world hash. Destination parents must exist;
outputs must be absent. Executed generation and archive commands:

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-ordinary-r2-baseline --mode probe --preset item10 --role ordinary --arm baseline --repetition 2
uv run --no-sync python -m tools.archive_item7_evidence create --root evidence/raw/item10/full-ordinary-r2-baseline --archive evidence/raw/item10/item10-full-ordinary-r2-baseline-004b1724.tar.gz --manifest evidence/item-10/full-ordinary-r2-baseline/archive-manifest.json --revision 004b1724a3242c0bf8fc9faf43e4b4e4f37dc23e
```

The full census is running on the restored world:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-ordinary-r2-baseline-custody/restored-world/world evidence/raw/item10/full-ordinary-r2-baseline-analysis/all-strata.json --all-strata --dimension-geometry evidence/item-10/dimension-geometry.json --trace-root evidence/raw/item10/full-ordinary-r2-baseline-custody/restored-local --trace-manifest evidence/item-10/full-ordinary-r2-baseline/archive-manifest.json
```

Timing/diagnostics are beside the output in `all-strata-runtime.txt`. Full class,
chunk, location and repetition-comparison acceptance remain pending.
