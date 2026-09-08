# Ordinary repetition-1 without-Sparse control

Status: GENERATED, CONFIGURATION VERIFIED, RAW CUSTODY VERIFIED. Full census
acceptance remains pending. Protocol: `item10-full-v1`; seed: `42`.
Generation source: `5ceb171ce09c241c613cabb0dc1b34a4d1efe619`.

The unchanged [run receipt](run.json) records all eleven completed selections,
readiness, correlated save flush and clean stop with Java exit 0. Duration was
559.034 seconds. The runtime omits only Sparse Structures: deployed candidate
count including Chunky is 136, SHA-256
`84a884f99e4ac48defb9ea0b2c9e45bf3d0f4f6e881a4be4d8968dc2be14d4da`.
All 228 frozen configuration files pass the existing semantic comparison;
eleven declared Chunky files are captured. The collector source/JAR hashes match
the frozen protocol. Full incoming-class and observation acceptance is still
required during analysis. No configuration was tuned or world reused.

The console retains 355 `Tried to load invalid item: 'Item must not be
minecraft:air'` messages; the matched baseline retains 300. These are existing
item-loading diagnostics, not missing structure observations or accepted loot
validation. Their full context remains in the raw logs. Structure/placement
acceptance relies on the explicit census and saved-content checks, not log silence.

## Raw custody

The stopped world backup contains 504 files totaling 434,558,526 bytes.
`world.tar.gz` is 169,798,947 bytes, SHA-256
`44c2327cac7a47ff0c7f10a57f10eddbe892e46b14d4ec7b0836b72f41dfb7b4`.
The [world restore](world-restore.json) verified all 504 members into a separate
world. No server restart was required for this offline evidence restore.

The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-ordinary-r1-without-sparse-5ceb171c)
contains `item10-full-ordinary-r1-without-sparse-5ceb171c.tar.gz` and the
[archive manifest](archive-manifest.json). Its fetched tag resolves to the exact
generation source above. The outer archive is 170,417,446 bytes, SHA-256
`d183a00212cf4f1449e533d407319e3d7d181d4df2371273a8561c8bd64d2b93`,
with 313 files totaling 203,068,750 uncompressed bytes.
Both [local](local-restore.json) and [downloaded](download-restore.json) restores
verified all 313 files. The downloaded manifest is byte-identical to the committed
manifest. This release is evidence custody, not the Item 10 completion boundary.

The initial outer archive command failed before creation because its manifest
parent directory did not exist. Creating that directory and retrying succeeded.
No raw capture or world was modified by the failed invocation.

## Reproduction

Generation command (requires absent instance and raw output):

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-ordinary-r1-without-sparse --mode probe --preset item10 --role ordinary --arm without-sparse --repetition 1
```

The existing backup, archive and restore tools are used without modification.
Create destination parents first; each output must be absent. Executed archive:

```sh
uv run --no-sync python -m tools.archive_item7_evidence create --root evidence/raw/item10/full-ordinary-r1-without-sparse --archive evidence/raw/item10/item10-full-ordinary-r1-without-sparse-5ceb171c.tar.gz --manifest evidence/item-10/full-ordinary-r1-without-sparse/archive-manifest.json --revision 5ceb171ce09c241c613cabb0dc1b34a4d1efe619
```

Download with `gh release download item10-full-ordinary-r1-without-sparse-5ceb171c
--repo copeugne/mcpack --dir DOWNLOAD`, then use `tools.archive_item7_evidence
restore` with the downloaded archive, this manifest, a new target and receipt.
Restore its nested world using `tools.manage_item4_environment restore` and the
world SHA-256 above. The exact restored paths are recorded in the receipts.

Full analysis invocation, currently pending:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-ordinary-r1-without-sparse-custody/restored-world/world evidence/raw/item10/full-ordinary-r1-without-sparse-analysis/all-strata.json --all-strata --dimension-geometry evidence/item-10/dimension-geometry.json --trace-root evidence/raw/item10/full-ordinary-r1-without-sparse-custody/restored-local --trace-manifest evidence/item-10/full-ordinary-r1-without-sparse/archive-manifest.json
```

Its timing/diagnostics are retained in the same analysis directory as
`all-strata-runtime.txt`. Generation completion is not census acceptance.
