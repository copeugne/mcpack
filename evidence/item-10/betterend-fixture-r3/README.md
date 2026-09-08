# BetterEnd fixture r3: rejected before placement

Source: `6389bea1164c370c9ca211f31bcf2d516a4bd160`. The predeclared
324-chunk mountainous diagnostic completed in 88.834 seconds with frozen
preflight, correlated save-flush and clean exit 0. See [receipt](diagnostic.json).

Both fixture commands were refused with `That position is not loaded`, recorded
in archived `minecraft-latest.log` lines 2645 and 2646. Pregeneration did not
keep the central End target loaded until these commands. Neither the platform
nor the requested building placement executed. The [trace](trace.jsonl) contains
five installation records, one naturally attempted crashed ship returning false,
and shutdown with zero unfinished attempts. There are no template calls or writes.
This fails the predeclared positive-placement gate. No density counts or collector
acceptance follow from this run. The incoming class bytes remain retained but
require inspection before any future claim based on their content hook.

The next fixture must explicitly load its target before attempting commands.
Do not reuse this world or bypass BetterEnd placement predicates. Preserve command
refusals independently of lifecycle success.

## Durable custody

The [release](https://github.com/copeugne/mcpack/releases/tag/item-10-betterend-fixture-2026-09-08-r3)
tag was fetched and verified to point to the launch revision. Its 5,138,678-byte
archive has SHA-256 `11feafaf4aa2c5e7b15c1b0e2847f15d412149aac311a89b74cba34191cc6b5e`.
The [manifest](archive-manifest.json) retains all 254 raw files. The downloaded
manifest is byte-identical and [download restore](download-restore.json) passes.
The [nested world restore](world-restore.json) has exactly the 96 paths, sizes and
SHA-256 values in [world backup](world-backup.json). It was not booted.

Reproduction uses the existing custody tools; the manifest revision is the exact
launch commit and the root is `evidence/raw/item10/betterend-fixture-r3`:

```sh
uv run --no-sync python -m tools.archive_item7_evidence create --root evidence/raw/item10/betterend-fixture-r3 --archive evidence/raw/item10/betterend-fixture-r3-custody/item10-betterend-fixture-r3-6389bea1.tar.gz --manifest evidence/item-10/betterend-fixture-r3/archive-manifest.json --revision 6389bea1164c370c9ca211f31bcf2d516a4bd160
gh release download item-10-betterend-fixture-2026-09-08-r3 --repo copeugne/mcpack --dir RESTORE_INPUT
uv run --no-sync python -m tools.archive_item7_evidence restore --archive RESTORE_INPUT/item10-betterend-fixture-r3-6389bea1.tar.gz --manifest evidence/item-10/betterend-fixture-r3/archive-manifest.json --target RESTORED_RAW --receipt RESTORE_RECEIPT.json
uv run --no-sync python -m tools.manage_item4_environment restore --archive RESTORED_RAW/world.tar.gz --sha256 572ca2fc0498ff526f7443e1d234ccc05a72536e3ce3956a6b71f5f5e9e4cc22 --target RESTORED_WORLD
```
