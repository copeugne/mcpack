# First collision capture: raw custody

Status: local and downloaded archive restores VERIFIED; external raw delivery
verified against the launch revision. Item 13 completion is not claimed.
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
record enter ordinary Git. The external download verification below completes
this raw capture's custody, not the other captures or the Item 13 exit gate.

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

## External delivery and downloaded restore

The [raw release](https://github.com/copeugne/mcpack/releases/tag/item13-collision-r1-73208407)
contains the unchanged archive and member manifest. The fetched tag resolves
exactly to 7320840758736e360697d6f932b5f524ec94a2aa, matching capture.source_revision.
The release is evidence storage, not a production/gameplay release or an Item 13
acceptance claim. Original local raw files, local archive and restored copies
remain preserved alongside this independent remote copy.

Before publication, the recorded config-sanitization result was inspected:
its one generated Resourceful Config Web credential was already replaced with
the declared redaction sentinel. RCON password is empty. A targeted search for
additional credential assignments in logs/configurations found no other matches;
this is a focused publication check, not a general security audit. No raw bytes
were changed or silently re-sanitized for publication.

The downloaded manifest is byte-identical to the committed manifest. The
[download restore receipt](download-restore.json) verifies the archive SHA-256
and every one of its 240 members in a second, absent restore target. No restored
server was booted; this is a raw capture restore, not a new gameplay experiment.

Executed retrieval and verification commands:

```sh
gh release download item13-collision-r1-73208407 --repo copeugne/mcpack --dir evidence/raw/item13/collision-r1-custody/downloaded
cmp evidence/item-13/collision/r1-custody/archive-manifest.json evidence/raw/item13/collision-r1-custody/downloaded/archive-manifest.json
uv run python -m tools.archive_item7_evidence restore --archive evidence/raw/item13/collision-r1-custody/downloaded/item13-collision-r1-73208407.tar.gz --manifest evidence/item-13/collision/r1-custody/archive-manifest.json --target evidence/raw/item13/collision-r1-custody/restored-download --receipt evidence/item-13/collision/r1-custody/download-restore.json
git fetch origin tag item13-collision-r1-73208407
git rev-parse item13-collision-r1-73208407
```
