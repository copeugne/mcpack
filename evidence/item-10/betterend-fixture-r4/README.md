# BetterEnd fixture r4: loaded but rejected by feature

Source: `3cb164d83bbc15e892502dba3320c63e00612ef6`. The [diagnostic](diagnostic.json) records
clean lifecycle completion in 89.498 seconds.
Archived `minecraft-latest.log` line 2618 confirms 25 force-loaded chunks;
line 2649 confirms 256 filled blocks. Line 2650 records `Failed to place feature`.
The [trace](trace.jsonl) has 27 rows, seven complete feature attempts and zero
unfinished attempts. The final attempt is the commanded building at `[8,81,8]`;
it returns false without a template call. The loading defect is resolved, but
the positive-placement gate still fails. No occurrence counts are accepted.
The specific rejecting terrain/height predicate remains UNKNOWN. Inspect it
before another experiment; do not bypass it or reuse this world.

## Custody

[Release](https://github.com/copeugne/mcpack/releases/tag/item-10-betterend-fixture-2026-09-08-r4).
The archive has 5355466 bytes and SHA-256
`b795c96d61af172a06a36932911aa99f5d1a9af13312ccba1247b525620fd575`. [Download restore](download-restore.json) verifies all
254 raw files. The downloaded manifest is byte-identical.
[Nested restore](world-restore.json) matches all 97 world paths, sizes and
hashes in [world backup](world-backup.json), without booting the restored world.

The existing archive tool created this archive from
`evidence/raw/item10/betterend-fixture-r4` with `--revision 3cb164d8`.
Use `tools.archive_item7_evidence restore` with the downloaded archive and this
[manifest](archive-manifest.json), then `tools.manage_item4_environment restore`
with the nested `world.tar.gz` and SHA-256 `1e98ce931c6260fc6720244c90788aa1b54889c5a8bf38cb55ff0515ed7b38ae`.
