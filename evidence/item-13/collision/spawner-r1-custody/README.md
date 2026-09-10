# Spawner lookup: raw custody

Status: local and downloaded restores VERIFIED; external delivery verified
against launch revision 48089961fc50210bc65e923bad8e14c3cca5e8e5. This closes this capture's raw custody, not
Item 13 quality/timing or its review and merge gates.

All five core files match the original sizes and hashes in
[the retention record](../spawner-r1-retention.json). The full raw tree has
240 files, 5,921,136 bytes and no symlinks. The original capture's
source_revision matches the release tag; rejection_reason is null. Its existing
configuration sanitization redacts one generated web-config credential. RCON
password is empty. A targeted credential-assignment search found no additional
matches in the logs/configurations. No raw files were rewritten for publication.

The [member manifest](archive-manifest.json) records an archive of
576,277 bytes, SHA-256
ba3016c629e6c5706c2838274010a70854ab14ca673193637f7cf1e1bc34dbda.
[Local restore](local-restore.json) and [downloaded restore](download-restore.json)
verify all members in separate new targets. The downloaded manifest is
byte-identical. The [raw release](https://github.com/copeugne/mcpack/releases/tag/item13-spawner-r1-48089961)
and preserved local raw/archive/restored copies provide external and local
custody. The fetched tag resolves to the full launch revision above.

Only the manifest, receipts and this record enter ordinary Git. The generated
member inventory is isolated with its one capture's custody outcome. Existing
archive/restore tools were reused; no new schema, validation framework, world,
server run or gameplay observation was introduced. Item 14 remains UNSTARTED.

Executed creation and retrieval commands (output paths must be absent):

```sh
mkdir evidence/raw/item13/spawner-r1-custody evidence/item-13/collision/spawner-r1-custody
uv run python -m tools.archive_item7_evidence create --root evidence/raw/item13/spawner-lookup-r1 --archive evidence/raw/item13/spawner-r1-custody/item13-spawner-r1-48089961.tar.gz --manifest evidence/item-13/collision/spawner-r1-custody/archive-manifest.json --revision 48089961fc50210bc65e923bad8e14c3cca5e8e5
uv run python -m tools.archive_item7_evidence restore --archive evidence/raw/item13/spawner-r1-custody/item13-spawner-r1-48089961.tar.gz --manifest evidence/item-13/collision/spawner-r1-custody/archive-manifest.json --target evidence/raw/item13/spawner-r1-custody/restored-local --receipt evidence/item-13/collision/spawner-r1-custody/local-restore.json
gh release download item13-spawner-r1-48089961 --repo copeugne/mcpack --dir evidence/raw/item13/spawner-r1-custody/downloaded
cmp evidence/item-13/collision/spawner-r1-custody/archive-manifest.json evidence/raw/item13/spawner-r1-custody/downloaded/archive-manifest.json
uv run python -m tools.archive_item7_evidence restore --archive evidence/raw/item13/spawner-r1-custody/downloaded/item13-spawner-r1-48089961.tar.gz --manifest evidence/item-13/collision/spawner-r1-custody/archive-manifest.json --target evidence/raw/item13/spawner-r1-custody/restored-download --receipt evidence/item-13/collision/spawner-r1-custody/download-restore.json
git fetch origin tag item13-spawner-r1-48089961
git rev-parse item13-spawner-r1-48089961
```
