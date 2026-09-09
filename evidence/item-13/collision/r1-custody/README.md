# First collision capture: raw custody

Status: local archive and restore VERIFIED; external archival delivery pending.
This is custody work for the existing completed capture, not another runtime
experiment or authorization to resume layout expansion.

The original five core files match every original size and SHA-256 in
[r1-retention.json](../r1-retention.json). The full raw tree contains 240 files,
5,929,253 bytes, with no symlinks. Capture source_revision is
7320840758736e360697d6f932b5f524ec94a2aa and rejection_reason is null. The
archive's short revision 73208407 resolves to that exact preserved commit.

Using the existing archive implementation produced a 574,201-byte archive,
SHA-256 520f2fe9411b81a7f45fae733001c5488ec15f7f998dd164c4b24e14d1f2c72c.
The [manifest](archive-manifest.json) retains all 240 member paths, sizes and
hashes. The [local restore](local-restore.json) verifies every member in a new
target, bound to manifest SHA-256
5fd887ec8b4e1bb7578c61911a20916ae215582f2594b5bda5eabc345a81387c.
Original files remain untouched. No world or server was started or changed.
Raw bytes remain ignored; only the manifest, restore receipt and this custody
record enter ordinary Git. The raw archive has not yet been independently
downloaded from durable external storage, so full custody is not claimed.

Executed commands, requiring absent output paths for reproduction:

```sh
mkdir evidence/raw/item13/collision-r1-custody evidence/item-13/collision/r1-custody
uv run python -m tools.archive_item7_evidence create --root evidence/raw/item13/collision-r1 --archive evidence/raw/item13/collision-r1-custody/item13-collision-r1-73208407.tar.gz --manifest evidence/item-13/collision/r1-custody/archive-manifest.json --revision 73208407
uv run python -m tools.archive_item7_evidence restore --archive evidence/raw/item13/collision-r1-custody/item13-collision-r1-73208407.tar.gz --manifest evidence/item-13/collision/r1-custody/archive-manifest.json --target evidence/raw/item13/collision-r1-custody/restored-local --receipt evidence/item-13/collision/r1-custody/local-restore.json
```

The manifest is an irreducible generated member inventory, isolated with this
single capture's custody result. No new archive schema or validation machinery
was introduced. The timing acceptance question remains pending; Item 14 remains
UNSTARTED.
